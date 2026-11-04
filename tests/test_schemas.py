"""Schema tests: valid JSON, draft 2020-12, required structure."""
from __future__ import annotations

import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SCHEMAS = ["vulnerability-report.schema.json", "assessment.schema.json"]
DRAFT = "https://json-schema.org/draft/2020-12/schema"


class TestSchemas(unittest.TestCase):
    def load(self, name: str) -> dict:
        data = json.loads((ROOT / "schemas" / name).read_text(encoding="utf-8"))
        self.assertIsInstance(data, dict)
        return data

    def test_valid_json_and_draft(self) -> None:
        for name in SCHEMAS:
            with self.subTest(schema=name):
                data = self.load(name)
                self.assertEqual(data.get("$schema"), DRAFT)
                self.assertIn("title", data)
                self.assertEqual(data.get("type"), "object")

    def test_required_fields(self) -> None:
        vuln = self.load("vulnerability-report.schema.json")
        for field in ("title", "severity", "target", "description", "status"):
            self.assertIn(field, vuln["required"])
        assess = self.load("assessment.schema.json")
        for field in ("assessment_id", "target", "findings"):
            self.assertIn(field, assess["required"])

    def test_severity_enum(self) -> None:
        vuln = self.load("vulnerability-report.schema.json")
        enum = vuln["properties"]["severity"]["enum"]
        self.assertEqual(enum, ["critical", "high", "medium", "low", "info"])

    def test_output_format_enum(self) -> None:
        vuln = self.load("vulnerability-report.schema.json")
        enum = vuln["properties"]["output_format"]["enum"]
        self.assertEqual(enum, ["json", "sarif", "csv", "html", "md"])


if __name__ == "__main__":
    unittest.main()
