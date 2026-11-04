#!/usr/bin/env python3
"""Check environment compatibility against references/compatibility.md.

Stdlib only. Never uses a shell.
"""
from __future__ import annotations

import argparse
import json
import sys

EXPECTED = {
    "upstream_package": "exaai-agent",
    "upstream_version": "3.0.1",
    "upstream_python_min": (3, 12),
    "skill_python_min": (3, 10),
    "entry_points": ["exaai", "exaaiagent", "ExaAiAgent"],
    "report_formats": ["json", "sarif", "csv", "html", "md"],
    "severities": ["critical", "high", "medium", "low", "info"],
}


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--json", action="store_true", help="Emit JSON output")
    args = parser.parse_args(argv)

    version = sys.version_info
    checks: dict[str, object] = {
        "python": f"{version.major}.{version.minor}.{version.micro}",
        "python_meets_upstream_3_12": version >= EXPECTED["upstream_python_min"],
        "python_meets_skill_3_10": version >= EXPECTED["skill_python_min"],
        "expected": {
            "upstream_package": EXPECTED["upstream_package"],
            "upstream_version": EXPECTED["upstream_version"],
            "entry_points": EXPECTED["entry_points"],
            "report_formats": EXPECTED["report_formats"],
            "severities": EXPECTED["severities"],
        },
    }
    ok = bool(checks["python_meets_skill_3_10"])
    checks["compatible"] = ok
    if args.json:
        print(json.dumps(checks, indent=2))
    else:
        for key, value in checks.items():
            print(f"{key}: {value}")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
