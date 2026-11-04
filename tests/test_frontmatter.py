"""Frontmatter tests for SKILL.md (stdlib parsing, no YAML dependency)."""
from __future__ import annotations

import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def parse_frontmatter(text: str) -> dict[str, str]:
    if not text.startswith("---\n"):
        raise ValueError("missing opening fence")
    parts = text.split("---\n", 2)
    if len(parts) < 3:
        raise ValueError("missing closing fence")
    fields: dict[str, str] = {}
    for line in parts[1].splitlines():
        match = re.match(r"^([A-Za-z0-9_-]+):\s*(.*)$", line)
        if match:
            fields[match.group(1)] = match.group(2).strip()
    return fields


class TestFrontmatter(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.text = (ROOT / "SKILL.md").read_text(encoding="utf-8")
        cls.fields = parse_frontmatter(cls.text)

    def test_has_name_and_description(self) -> None:
        self.assertIn("name", self.fields)
        self.assertIn("description", self.fields)
        self.assertTrue(self.fields["name"])
        self.assertTrue(self.fields["description"])

    def test_name_value(self) -> None:
        self.assertEqual(self.fields["name"], "exaaiagent-security")

    def test_description_mentions_authorized(self) -> None:
        self.assertIn("authorized", self.fields["description"].lower())

    def test_body_nonempty(self) -> None:
        body = self.text.split("---\n", 2)[2]
        self.assertGreater(len(body.strip()), 500)


if __name__ == "__main__":
    unittest.main()
