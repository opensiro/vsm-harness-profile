from __future__ import annotations

import importlib.util
import json
import subprocess
import tempfile
import unittest
from pathlib import Path

SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "validate_repository.py"
SPEC = importlib.util.spec_from_file_location("validate_repository", SCRIPT)
assert SPEC and SPEC.loader
VALIDATOR = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(VALIDATOR)


class RepositoryValidationTests(unittest.TestCase):
    def make_repo(self) -> Path:
        temp = tempfile.TemporaryDirectory()
        self.addCleanup(temp.cleanup)
        root = Path(temp.name)
        (root / "VERSION").write_text("0.2.1\n", encoding="utf-8")
        (root / "PROFILE.md").write_text(
            "# VSM Harness Profile\n\n**Version:** 0.2.1\n\nSee [versioning](VERSIONING.md).\n",
            encoding="utf-8",
        )
        (root / "README.md").write_text(
            "# VSM Harness Profile\n\n**Current Profile version: `0.2.1`**\n\nSee [profile](PROFILE.md).\n",
            encoding="utf-8",
        )
        (root / "VERSIONING.md").write_text("# Versioning\n", encoding="utf-8")
        (root / "CONSUMER_CONTRACT.md").write_text("# Consumer contract\n", encoding="utf-8")
        (root / "CHANGELOG.md").write_text(
            "# Changelog\n\n## 0.2.1 — 2026-09-16\n\nCurrent release.\n\n"
            "## 0.2.0 — 2026-09-16\n\nPrevious release.\n",
            encoding="utf-8",
        )
        self.write_impact(
            root,
            [
                {
                    "version": "0.2.0",
                    "previous": "baseline",
                    "compatibility": "compatible",
                    "assessment_impact": "targeted",
                    "selectors": ["concept:decision-ownership"],
                },
                {
                    "version": "0.2.1",
                    "previous": "0.2.0",
                    "compatibility": "compatible",
                    "assessment_impact": "none",
                    "selectors": [],
                },
            ],
        )
        (root / "LICENSE").write_text("license\n", encoding="utf-8")
        return root

    def write_impact(self, root: Path, releases: list[dict[str, object]]) -> None:
        (root / "RELEASE_IMPACT.json").write_text(
            json.dumps(
                {"profile": "opensiro/vsm-harness-profile", "releases": releases},
                indent=2,
            )
            + "\n",
            encoding="utf-8",
        )

    def impact(self, root: Path) -> dict[str, object]:
        return json.loads((root / "RELEASE_IMPACT.json").read_text(encoding="utf-8"))

    def assert_has_error(self, root: Path, needle: str) -> None:
        errors = VALIDATOR.validate(root)
        self.assertTrue(any(needle in error for error in errors), errors)

    def test_valid_fixture_passes(self) -> None:
        self.assertEqual(VALIDATOR.validate(self.make_repo()), [])

    def test_profile_keeps_boundary_provenance_invariant(self) -> None:
        profile = (SCRIPT.parents[1] / "PROFILE.md").read_text(encoding="utf-8")
        self.assertIn("Repository co-location is not evidence of membership in the declared system-in-focus", profile)
        self.assertIn("MUST be reachable in the declared operating or deployment boundary being assessed", profile)
        self.assertIn("Repository co-location as system membership", profile)

    def test_readme_version_drift_fails(self) -> None:
        root = self.make_repo()
        (root / "README.md").write_text(
            "# VSM Harness Profile\n\n**Current Profile version: `0.2.0`**\n",
            encoding="utf-8",
        )
        self.assert_has_error(root, "README.md: declares current Profile 0.2.0")

    def test_missing_required_file_fails(self) -> None:
        root = self.make_repo()
        (root / "CONSUMER_CONTRACT.md").unlink()
        self.assert_has_error(root, "missing required repository file: CONSUMER_CONTRACT.md")

    def test_broken_local_reference_fails(self) -> None:
        root = self.make_repo()
        (root / "README.md").write_text(
            "# VSM Harness Profile\n\n**Current Profile version: `0.2.1`**\n\n[missing](NOPE.md)\n",
            encoding="utf-8",
        )
        self.assert_has_error(root, "broken local link")

    def test_second_profile_document_fails(self) -> None:
        root = self.make_repo()
        extra = root / "docs"
        extra.mkdir()
        (extra / "PROFILE.md").write_text(
            "# VSM Harness Profile\n\n**Version:** 0.2.1\n", encoding="utf-8"
        )
        self.assert_has_error(root, "only independently versioned Profile source")

    def test_release_impact_latest_version_drift_fails(self) -> None:
        root = self.make_repo()
        data = self.impact(root)
        data["releases"] = data["releases"][:-1]
        self.write_impact(root, data["releases"])
        self.assert_has_error(root, "latest release-impact version is 0.2.0")

    def test_patch_cannot_trigger_targeted_reassessment(self) -> None:
        root = self.make_repo()
        data = self.impact(root)
        latest = data["releases"][-1]
        latest["assessment_impact"] = "targeted"
        latest["selectors"] = ["function:S2"]
        self.write_impact(root, data["releases"])
        self.assert_has_error(root, "PATCH releases must be compatible with assessment_impact='none'")

    def test_targeted_impact_requires_selector(self) -> None:
        root = self.make_repo()
        data = self.impact(root)
        first = data["releases"][0]
        first["selectors"] = []
        self.write_impact(root, data["releases"])
        self.assert_has_error(root, "assessment_impact='targeted' requires at least one selector")

    def test_release_impact_chain_must_be_contiguous(self) -> None:
        root = self.make_repo()
        data = self.impact(root)
        data["releases"][-1]["previous"] = "0.1.9"
        self.write_impact(root, data["releases"])
        self.assert_has_error(root, "previous must reference prior release '0.2.0'")

    def test_release_tag_version_mismatch_fails(self) -> None:
        root = self.make_repo()
        subprocess.run(["git", "init", "-q", str(root)], check=True)
        subprocess.run(["git", "-C", str(root), "config", "user.email", "test@example.com"], check=True)
        subprocess.run(["git", "-C", str(root), "config", "user.name", "Test"], check=True)
        subprocess.run(["git", "-C", str(root), "add", "."], check=True)
        subprocess.run(["git", "-C", str(root), "commit", "-qm", "fixture"], check=True)
        subprocess.run(["git", "-C", str(root), "tag", "v0.2.0"], check=True)
        self.assert_has_error(root, "v0.2.0: VERSION at tagged revision")


if __name__ == "__main__":
    unittest.main()
