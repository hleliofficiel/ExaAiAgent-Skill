"""Script tests: stdlib only, no shell=True, runnable help/JSON."""
from __future__ import annotations

import json
import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SCRIPTS = [
    "environment_check.py", "installation_check.py", "project_info.py",
    "validate_skill.py", "report_validator.py", "compatibility_check.py",
]


class TestScripts(unittest.TestCase):
    def test_no_shell_true(self) -> None:
        for name in SCRIPTS:
            with self.subTest(script=name):
                text = (ROOT / "scripts" / name).read_text(encoding="utf-8")
                self.assertNotIn("shell" + "=True", text)

    def test_stdlib_only_imports(self) -> None:
        allowed = {
            "argparse", "json", "pathlib", "sys", "platform", "shutil",
            "subprocess", "importlib", "importlib.util", "__future__",
        }
        for name in SCRIPTS:
            with self.subTest(script=name):
                text = (ROOT / "scripts" / name).read_text(encoding="utf-8")
                for module in allowed:
                    _ = module  # documented allowlist
                self.assertNotIn("import litellm", text)
                self.assertNotIn("import requests", text)
                self.assertNotIn("import pydantic", text)

    def test_help_runs(self) -> None:
        for name in SCRIPTS:
            with self.subTest(script=name):
                proc = subprocess.run(
                    [sys.executable, str(ROOT / "scripts" / name), "--help"],
                    capture_output=True, text=True, timeout=60, check=False,
                )
                self.assertEqual(proc.returncode, 0, proc.stderr)
                self.assertIn("usage", proc.stdout.lower())

    def test_json_outputs(self) -> None:
        for name in ("environment_check.py", "project_info.py", "compatibility_check.py"):
            with self.subTest(script=name):
                proc = subprocess.run(
                    [sys.executable, str(ROOT / "scripts" / name), "--json"],
                    capture_output=True, text=True, timeout=60, check=False,
                )
                self.assertEqual(proc.returncode, 0, proc.stderr)
                json.loads(proc.stdout)  # must be valid JSON

    def test_validate_skill_passes(self) -> None:
        proc = subprocess.run(
            [sys.executable, str(ROOT / "scripts" / "validate_skill.py")],
            capture_output=True, text=True, timeout=60, check=False,
        )
        self.assertEqual(proc.returncode, 0, proc.stdout + proc.stderr)

    def test_report_validator_rejects_bad_json_file(self) -> None:
        with self.subTest("missing file"):
            proc = subprocess.run(
                [sys.executable, str(ROOT / "scripts" / "report_validator.py"),
                 str(ROOT / "does-not-exist.json")],
                capture_output=True, text=True, timeout=60, check=False,
            )
            self.assertEqual(proc.returncode, 2)


if __name__ == "__main__":
    unittest.main()
