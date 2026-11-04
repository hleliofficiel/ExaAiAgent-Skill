#!/usr/bin/env python3
"""Check the local environment for ExaAiAgent skill usage.

Stdlib only. Never uses a shell.
"""
from __future__ import annotations

import argparse
import json
import platform
import shutil
import sys
from pathlib import Path


def check_python() -> dict[str, object]:
    version = sys.version_info
    return {
        "python": f"{version.major}.{version.minor}.{version.micro}",
        "meets_upstream_minimum_3_12": version >= (3, 12),
        "meets_skill_minimum_3_10": version >= (3, 10),
    }


def check_platform() -> dict[str, object]:
    return {
        "system": platform.system(),
        "release": platform.release(),
        "machine": platform.machine(),
        "executable": sys.executable,
    }


def check_disk(path: str) -> dict[str, object]:
    resolved = Path(path).resolve()
    total, used, free = shutil.disk_usage(resolved)
    return {
        "path": str(resolved),
        "total_bytes": total,
        "free_bytes": free,
        "free_ok": free > 100 * 1024 * 1024,
    }


def check_optional_tools() -> dict[str, bool]:
    tools = ["nuclei", "httpx", "katana", "zap.sh", "zap", "exaai"]
    return {tool: shutil.which(tool) is not None for tool in tools}


def check_litellm() -> bool:
    import importlib.util

    return importlib.util.find_spec("litellm") is not None


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--disk-path", default=".", help="Path for disk-space check")
    parser.add_argument("--json", action="store_true", help="Emit JSON output")
    args = parser.parse_args(argv)

    report: dict[str, object] = {
        "python": check_python(),
        "platform": check_platform(),
        "disk": check_disk(args.disk_path),
        "optional_tools": check_optional_tools(),
        "litellm_available": check_litellm(),
    }
    if args.json:
        print(json.dumps(report, indent=2))
    else:
        for key, value in report.items():
            print(f"{key}: {value}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
