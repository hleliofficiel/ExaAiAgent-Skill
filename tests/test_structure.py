"""Structure tests: required files and directories exist."""
from __future__ import annotations

import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

REQUIRED_FILES = [
    "SKILL.md", "README.md", "LICENSE", "NOTICE", "CHANGELOG.md",
    "CONTRIBUTING.md", "SECURITY.md", "VERSION", "INSTALLATION.md",
    "DISTRIBUTION.md", "RELEASE_NOTES.md", "pyproject.toml", ".gitignore",
    "references/architecture.md", "references/capabilities.md",
    "references/installation.md", "references/configuration.md",
    "references/cli-reference.md", "references/security-workflows.md",
    "references/vulnerability-analysis.md", "references/cve-reference.md",
    "references/kubernetes-security.md", "references/reporting.md",
    "references/troubleshooting.md", "references/compatibility.md",
    "references/safety-policy.md", "references/limitations.md",
    "references/attribution.md",
    "scripts/environment_check.py", "scripts/installation_check.py",
    "scripts/project_info.py", "scripts/validate_skill.py",
    "scripts/report_validator.py", "scripts/compatibility_check.py",
    "templates/security-assessment.md", "templates/vulnerability-report.md",
    "templates/executive-summary.md", "templates/remediation-plan.md",
    "templates/assessment-checklist.md",
    "schemas/vulnerability-report.schema.json", "schemas/assessment.schema.json",
    "examples/installation.md", "examples/security-assessment.md",
    "examples/vulnerability-analysis.md", "examples/report-generation.md",
    "examples/troubleshooting.md",
    "tests/test_structure.py", "tests/test_frontmatter.py",
    "tests/test_scripts.py", "tests/test_schemas.py",
    "tests/test_references.py", "tests/test_security.py",
    "tests/test_packaging.py", "tests/test_compatibility.py",
    ".github/workflows/validate.yml", ".github/workflows/release.yml",
    "distribution/README.md", "docs/README.md",
]

REQUIRED_DIRS = [
    "references", "scripts", "templates", "schemas", "examples",
    "tests", "docs", ".github/workflows", "distribution",
]


class TestStructure(unittest.TestCase):
    def test_required_files_exist(self) -> None:
        for name in REQUIRED_FILES:
            with self.subTest(file=name):
                self.assertTrue((ROOT / name).is_file(), f"missing file: {name}")

    def test_required_dirs_exist(self) -> None:
        for name in REQUIRED_DIRS:
            with self.subTest(dir=name):
                self.assertTrue((ROOT / name).is_dir(), f"missing dir: {name}")

    def test_required_files_nonempty(self) -> None:
        for name in REQUIRED_FILES:
            with self.subTest(file=name):
                self.assertGreater((ROOT / name).stat().st_size, 0, f"empty: {name}")


if __name__ == "__main__":
    unittest.main()
