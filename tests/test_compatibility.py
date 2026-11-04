"""Compatibility tests: documented matrix matches reality and upstream."""
from __future__ import annotations

import json
import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


class TestCompatibility(unittest.TestCase):
    def test_compatibility_doc(self) -> None:
        text = (ROOT / "references" / "compatibility.md").read_text(encoding="utf-8")
        for fact in ("exaai-agent", "3.0.1", "3.12", "exaai", "exaaiagent",
                     "ExaAiAgent", "json", "sarif", "csv", "html", "md"):
            self.assertIn(fact, text)

    def test_compatibility_check_script(self) -> None:
        proc = subprocess.run(
            [sys.executable, str(ROOT / "scripts" / "compatibility_check.py"), "--json"],
            capture_output=True, text=True, timeout=60, check=False,
        )
        self.assertEqual(proc.returncode, 0, proc.stderr)
        data = json.loads(proc.stdout)
        self.assertTrue(data["compatible"])
        self.assertEqual(data["expected"]["upstream_version"], "3.0.1")

    def test_project_info(self) -> None:
        proc = subprocess.run(
            [sys.executable, str(ROOT / "scripts" / "project_info.py"), "--json"],
            capture_output=True, text=True, timeout=60, check=False,
        )
        self.assertEqual(proc.returncode, 0, proc.stderr)
        data = json.loads(proc.stdout)
        self.assertEqual(data["version"], "1.0.0")
        self.assertEqual(data["upstream"]["entry_points"], ["exaai", "exaaiagent", "ExaAiAgent"])
        self.assertGreaterEqual(data["counts"]["references"], 15)

    def test_github_workflows_python_versions(self) -> None:
        text = (ROOT / ".github" / "workflows" / "validate.yml").read_text(encoding="utf-8")
        self.assertIn("3.10", text)  # skill scripts/tests floor
        self.assertIn("3.12", text)  # upstream requirement documented/tested


if __name__ == "__main__":
    unittest.main()
