#!/usr/bin/env python3
"""Print summary info about this skill package.

Stdlib only. Never uses a shell.
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def read_version() -> str:
    version_file = ROOT / "VERSION"
    if version_file.exists():
        return version_file.read_text(encoding="utf-8").strip()
    return "unknown"


def count_files(subdir: str) -> int:
    path = ROOT / subdir
    if not path.exists():
        return 0
    return sum(1 for item in path.rglob("*") if item.is_file())


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--json", action="store_true", help="Emit JSON output")
    args = parser.parse_args(argv)

    info: dict[str, object] = {
        "name": "exaaiagent-skill",
        "version": read_version(),
        "upstream": {
            "package": "exaai-agent",
            "version": "3.0.1",
            "python": "^3.12",
            "entry_points": ["exaai", "exaaiagent", "ExaAiAgent"],
            "repo": "https://github.com/hleliofficiel/ExaAiAgent",
        },
        "skill_repo": "https://github.com/hleliofficiel/ExaAiAgent-Skill",
        "counts": {
            "references": count_files("references"),
            "scripts": count_files("scripts"),
            "templates": count_files("templates"),
            "schemas": count_files("schemas"),
            "examples": count_files("examples"),
            "tests": count_files("tests"),
        },
        "license": "Apache-2.0",
    }
    if args.json:
        print(json.dumps(info, indent=2))
    else:
        for key, value in info.items():
            print(f"{key}: {value}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
