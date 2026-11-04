#!/usr/bin/env python3
"""Verify the ExaAiAgent installation (entry points, version, modules).

Stdlib only. Never uses a shell.
"""
from __future__ import annotations

import argparse
import importlib.util
import json
import shutil
import subprocess
import sys

ENTRY_POINTS = ["exaai", "exaaiagent", "ExaAiAgent"]


def check_entry_points() -> dict[str, bool]:
    return {name: shutil.which(name) is not None for name in ENTRY_POINTS}


def check_package() -> dict[str, object]:
    spec = importlib.util.find_spec("exaaiagnt")
    return {"exaaiagnt_importable": spec is not None, "spec_found": spec is not None}


def run_help() -> dict[str, object]:
    exe = shutil.which("exaai")
    if exe is None:
        return {"ran": False, "reason": "exaai not on PATH"}
    try:
        proc = subprocess.run(
            [exe, "--version"],
            capture_output=True,
            text=True,
            timeout=30,
            check=False,
        )
    except (OSError, subprocess.TimeoutExpired) as exc:
        return {"ran": False, "reason": str(exc)}
    return {
        "ran": True,
        "returncode": proc.returncode,
        "stdout": proc.stdout.strip()[:200],
        "stderr": proc.stderr.strip()[:200],
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--json", action="store_true", help="Emit JSON output")
    args = parser.parse_args(argv)

    entry_points = check_entry_points()
    report: dict[str, object] = {
        "entry_points": entry_points,
        "package": check_package(),
        "version_command": run_help(),
        "installed": any(entry_points.values()),
    }
    if args.json:
        print(json.dumps(report, indent=2))
    else:
        print(f"entry_points: {entry_points}")
        print(f"package: {report['package']}")
        print(f"version_command: {report['version_command']}")
        print(f"installed: {report['installed']}")
    if not report["installed"]:
        print("exaai not found; install with: pip install exaai-agent==3.0.1", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
