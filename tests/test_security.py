"""Security tests: safe defaults, no shell=True, no secrets, safe docs."""
from __future__ import annotations

import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


class TestSecurity(unittest.TestCase):
    def test_no_shell_true_anywhere_in_scripts(self) -> None:
        for script in (ROOT / "scripts").glob("*.py"):
            with self.subTest(script=script.name):
                self.assertNotIn("shell" + "=True", script.read_text(encoding="utf-8"))

    def test_no_eval_exec(self) -> None:
        for script in (ROOT / "scripts").glob("*.py"):
            text = script.read_text(encoding="utf-8")
            with self.subTest(script=script.name):
                self.assertNotIn("eval(", text)
                self.assertNotIn("exec(", text.replace("validate_skill", ""))

    def test_no_hardcoded_secrets(self) -> None:
        pattern = re.compile(
            r"(api[_-]?key|secret|password|token)\s*=\s*['\"][^'\"]{8,}['\"]",
            re.IGNORECASE,
        )
        for path in list((ROOT / "scripts").glob("*.py")) + list((ROOT / "tests").glob("*.py")):
            with self.subTest(file=path.name):
                self.assertIsNone(pattern.search(path.read_text(encoding="utf-8")))

    def test_skill_states_authorized_only(self) -> None:
        skill = (ROOT / "SKILL.md").read_text(encoding="utf-8")
        self.assertIn("Authorized testing only", skill)
        self.assertIn("No fabrication", skill)

    def test_security_md_exists(self) -> None:
        self.assertTrue((ROOT / "SECURITY.md").is_file())
        text = (ROOT / "SECURITY.md").read_text(encoding="utf-8")
        self.assertIn("Authorized testing only", text)

    def test_templates_have_no_fake_findings(self) -> None:
        for template in (ROOT / "templates").glob("*.md"):
            text = template.read_text(encoding="utf-8")
            with self.subTest(template=template.name):
                self.assertNotIn("CVE-0000", text)
                self.assertIn("{{", text)  # placeholders, not fabricated data


if __name__ == "__main__":
    unittest.main()
