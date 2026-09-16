#!/usr/bin/env python3
"""Validate deterministic repository invariants for VSM Harness Profile maintenance."""

from __future__ import annotations

import argparse
import re
import subprocess
import sys
from pathlib import Path
from urllib.parse import unquote, urlsplit

SEMVER_PATTERN = r"(?:0|[1-9]\d*)\.(?:0|[1-9]\d*)\.(?:0|[1-9]\d*)(?:-[0-9A-Za-z.-]+)?(?:\+[0-9A-Za-z.-]+)?"
SEMVER_RE = re.compile(rf"^{SEMVER_PATTERN}$")
PROFILE_VERSION_RE = re.compile(rf"^\*\*Version:\*\*\s+({SEMVER_PATTERN})\s*$", re.MULTILINE)
README_VERSION_RE = re.compile(
    rf"^\*\*Current Profile version:\s*`({SEMVER_PATTERN})`\*\*\s*$", re.MULTILINE
)
CHANGELOG_VERSION_RE = re.compile(rf"^##\s+({SEMVER_PATTERN})(?:\s+[^\n]*)?$", re.MULTILINE)
MARKDOWN_LINK_RE = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")

REQUIRED_FILES = (
    "PROFILE.md",
    "VERSION",
    "VERSIONING.md",
    "CHANGELOG.md",
    "README.md",
    "LICENSE",
)


def _read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def _one_version(text: str, pattern: re.Pattern[str], surface: str, errors: list[str]) -> str | None:
    matches = pattern.findall(text)
    if len(matches) != 1:
        errors.append(f"{surface}: expected exactly one current version declaration, found {len(matches)}")
        return None
    return matches[0]


def check_required_files(root: Path, errors: list[str]) -> None:
    for relative in REQUIRED_FILES:
        if not (root / relative).is_file():
            errors.append(f"missing required repository file: {relative}")


def check_version_surfaces(root: Path, errors: list[str]) -> str | None:
    version_path = root / "VERSION"
    if not version_path.is_file():
        return None

    version = _read(version_path).strip()
    if not SEMVER_RE.fullmatch(version):
        errors.append(f"VERSION: expected Semantic Version, found {version!r}")
        return None

    profile_path = root / "PROFILE.md"
    if profile_path.is_file():
        profile_version = _one_version(_read(profile_path), PROFILE_VERSION_RE, "PROFILE.md", errors)
        if profile_version is not None and profile_version != version:
            errors.append(f"PROFILE.md: declares {profile_version}, expected {version} from VERSION")

    readme_path = root / "README.md"
    if readme_path.is_file():
        readme_version = _one_version(_read(readme_path), README_VERSION_RE, "README.md", errors)
        if readme_version is not None and readme_version != version:
            errors.append(f"README.md: declares current Profile {readme_version}, expected {version} from VERSION")

    changelog_path = root / "CHANGELOG.md"
    if changelog_path.is_file():
        changelog_versions = CHANGELOG_VERSION_RE.findall(_read(changelog_path))
        if not changelog_versions:
            errors.append("CHANGELOG.md: no version headings found")
        elif changelog_versions[0] != version:
            errors.append(
                f"CHANGELOG.md: latest version heading is {changelog_versions[0]}, expected {version} from VERSION"
            )

    return version


def _link_target(raw: str) -> str | None:
    target = raw.strip()
    if target.startswith("<") and ">" in target:
        target = target[1 : target.index(">")]
    elif any(char.isspace() for char in target):
        # Optional Markdown title follows whitespace. Repository paths containing
        # spaces should be percent-encoded, which keeps this deterministic.
        target = target.split(maxsplit=1)[0]

    if not target or target.startswith("#"):
        return None

    parsed = urlsplit(target)
    if parsed.scheme or parsed.netloc or target.startswith("//"):
        return None
    if parsed.path.startswith("/"):
        return None

    path = unquote(parsed.path)
    return path or None


def check_local_markdown_links(root: Path, errors: list[str]) -> None:
    resolved_root = root.resolve()
    for markdown in sorted(root.rglob("*.md")):
        if ".git" in markdown.parts:
            continue
        text = _read(markdown)
        for match in MARKDOWN_LINK_RE.finditer(text):
            target = _link_target(match.group(1))
            if target is None:
                continue
            candidate = (markdown.parent / target).resolve()
            try:
                candidate.relative_to(resolved_root)
            except ValueError:
                errors.append(
                    f"{markdown.relative_to(root)}: local link escapes repository: {match.group(1)!r}"
                )
                continue
            if not candidate.exists():
                errors.append(
                    f"{markdown.relative_to(root)}: broken local link {match.group(1)!r} -> "
                    f"{candidate.relative_to(resolved_root)}"
                )


def check_single_profile_source(root: Path, errors: list[str]) -> None:
    duplicates: list[Path] = []
    for markdown in sorted(root.rglob("*.md")):
        if ".git" in markdown.parts or markdown == root / "PROFILE.md":
            continue
        if PROFILE_VERSION_RE.search(_read(markdown)):
            duplicates.append(markdown.relative_to(root))
    if duplicates:
        rendered = ", ".join(str(path) for path in duplicates)
        errors.append(
            "PROFILE.md must remain the only independently versioned Profile source; "
            f"found Profile version declaration in: {rendered}"
        )


def _git(root: Path, *args: str) -> subprocess.CompletedProcess[str] | None:
    try:
        return subprocess.run(
            ["git", "-C", str(root), *args],
            check=False,
            capture_output=True,
            text=True,
        )
    except OSError:
        return None


def check_release_tags(root: Path, errors: list[str]) -> None:
    inside = _git(root, "rev-parse", "--is-inside-work-tree")
    if inside is None or inside.returncode != 0 or inside.stdout.strip() != "true":
        return

    tags = _git(root, "tag", "--list", "v*", "--sort=version:refname")
    if tags is None or tags.returncode != 0:
        errors.append("git: unable to enumerate release tags")
        return

    changelog_text = _read(root / "CHANGELOG.md") if (root / "CHANGELOG.md").is_file() else ""
    changelog_versions = set(CHANGELOG_VERSION_RE.findall(changelog_text))

    for tag in (line.strip() for line in tags.stdout.splitlines()):
        if not tag:
            continue
        tag_version = tag[1:]
        if not SEMVER_RE.fullmatch(tag_version):
            continue

        tagged_version = _git(root, "show", f"refs/tags/{tag}:VERSION")
        if tagged_version is None or tagged_version.returncode != 0:
            errors.append(f"{tag}: tagged revision is missing VERSION")
            continue
        if tagged_version.stdout.strip() != tag_version:
            errors.append(
                f"{tag}: VERSION at tagged revision is {tagged_version.stdout.strip()!r}, expected {tag_version!r}"
            )

        tagged_profile = _git(root, "show", f"refs/tags/{tag}:PROFILE.md")
        if tagged_profile is None or tagged_profile.returncode != 0:
            errors.append(f"{tag}: tagged revision is missing PROFILE.md")
        else:
            matches = PROFILE_VERSION_RE.findall(tagged_profile.stdout)
            if matches != [tag_version]:
                errors.append(
                    f"{tag}: PROFILE.md version declaration is {matches!r}, expected [{tag_version!r}]"
                )

        if tag_version not in changelog_versions:
            errors.append(f"{tag}: no matching CHANGELOG.md version heading on current branch")


def validate(root: Path) -> list[str]:
    errors: list[str] = []
    check_required_files(root, errors)
    check_version_surfaces(root, errors)
    check_local_markdown_links(root, errors)
    check_single_profile_source(root, errors)
    check_release_tags(root, errors)
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--root",
        type=Path,
        default=Path(__file__).resolve().parents[1],
        help="repository root (defaults to the script's parent repository)",
    )
    args = parser.parse_args()

    errors = validate(args.root.resolve())
    if errors:
        print("Profile repository validation failed:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1

    print("Profile repository validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
