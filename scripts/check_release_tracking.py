#!/usr/bin/env python3
"""Verify that every explicitly versioned Profile release has a tag and GitHub Release."""
from __future__ import annotations

import json
import os
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CHANGELOG = ROOT / "CHANGELOG.md"
VERSION_FILE = "VERSION"
TRACK_FROM = (0, 2, 0)


def run(*args: str, check: bool = True) -> subprocess.CompletedProcess[str]:
    return subprocess.run(args, cwd=ROOT, text=True, capture_output=True, check=check)


def versions() -> list[str]:
    found = re.findall(r"^## (\d+\.\d+\.\d+) —", CHANGELOG.read_text(encoding="utf-8"), re.MULTILINE)
    return [version for version in found if tuple(map(int, version.split("."))) >= TRACK_FROM]


def tag_sha(repo: str, tag: str) -> str | None:
    result = run("gh", "api", f"repos/{repo}/git/ref/tags/{tag}", check=False)
    if result.returncode != 0:
        return None
    data = json.loads(result.stdout)
    kind = data["object"]["type"]
    sha = data["object"]["sha"]
    if kind == "commit":
        return sha
    if kind == "tag":
        return json.loads(run("gh", "api", f"repos/{repo}/git/tags/{sha}").stdout)["object"]["sha"]
    return None


def main() -> int:
    repo = os.environ.get("GITHUB_REPOSITORY")
    if not repo or not os.environ.get("GH_TOKEN"):
        print("GITHUB_REPOSITORY and GH_TOKEN are required", file=sys.stderr)
        return 2

    failures: list[str] = []
    for version in versions():
        tag = f"v{version}"
        sha = tag_sha(repo, tag)
        if sha is None:
            failures.append(f"{tag}: missing Git tag")
            continue
        result = run("git", "show", f"{sha}:{VERSION_FILE}", check=False)
        if result.returncode != 0 or result.stdout.strip() != version:
            failures.append(f"{tag}: target {sha} does not contain VERSION {version}")
        if run("gh", "release", "view", tag, "--repo", repo, check=False).returncode != 0:
            failures.append(f"{tag}: missing GitHub Release")

    if failures:
        print("\n".join(failures), file=sys.stderr)
        return 1
    print(f"Release tracking complete for {len(versions())} Profile versions")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
