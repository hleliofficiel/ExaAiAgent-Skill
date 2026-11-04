"""Packaging tests: version consistency, license, pyproject, workflows."""
from __future__ import annotations

import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


class TestPackaging(unittest.TestCase):
    def test_version_file(self) -> None:
        version = (ROOT / "VERSION").read_text(encoding="utf-8").strip()
        self.assertEqual(version, "1.0.0")
        self.assertRegex(version, r"^\d+\.\d+\.\d+$")

    def test_pyproject_version_matches(self) -> None:
        text = (ROOT / "pyproject.toml").read_text(encoding="utf-8")
        self.assertIn('version = "1.0.0"', text)
        self.assertIn("Apache-2.0", text)
        self.assertIn("exaaiagent-skill", text)

    def test_license_is_apache2(self) -> None:
        text = (ROOT / "LICENSE").read_text(encoding="utf-8")
        self.assertIn("Apache License", text)
        self.assertIn("Version 2.0", text)
        self.assertIn("http://www.apache.org/licenses/", text)

    def test_notice_attribution(self) -> None:
        text = (ROOT / "NOTICE").read_text(encoding="utf-8")
        self.assertIn("ExaAi", text)
        self.assertIn("https://github.com/hleliofficiel/ExaAiAgent", text)
        self.assertIn("https://github.com/hleliofficiel/ExaAiAgent-Skill", text)

    def test_workflows_exist_and_reference_unittest(self) -> None:
        for name in ("validate.yml", "release.yml"):
            path = ROOT / ".github" / "workflows" / name
            with self.subTest(workflow=name):
                self.assertTrue(path.is_file())
                text = path.read_text(encoding="utf-8")
                self.assertIn("unittest", text)

    def test_distribution_readme(self) -> None:
        text = (ROOT / "distribution" / "README.md").read_text(encoding="utf-8")
        self.assertIn("ExaAiAgent-Skill-v1.0.0.zip", text)
        self.assertIn("SKILL.md", text)

    def test_no_pycache_committed(self) -> None:
        gitignore = (ROOT / ".gitignore").read_text(encoding="utf-8")
        self.assertIn("__pycache__", gitignore)
        self.assertIn("*.py[cod]", gitignore)


if __name__ == "__main__":
    unittest.main()
