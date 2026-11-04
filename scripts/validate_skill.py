#!/usr/bin/env python3
"""Validate the ExaAiAgent-Skill package structure and frontmatter.

Stdlib only. Never uses a shell.
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

REQUIRED_FILES = [
    "SKILL.md",
    "README.md",
    "LICENSE",
    "NOTICE",
    "CHANGELOG.md",
    "CONTRIBUTING.md",
    "SECURITY.md",
    "VERSION",
    "INSTALLATION.md",
    "DISTRIBUTION.md",
    "RELEASE_NOTES.md",
    "pyproject.toml",
    ".gitignore",
    "references/architecture.md",
    "references/capabilities.md",
    "references/installation.md",
    "references/configuration.md",
    "references/cli-reference.md",
    "references/security-workflows.md",
    "references/vulnerability-analysis.md",
    "references/cve-reference.md",
    "references/kubernetes-security.md",
    "references/reporting.md",
    "references/troubleshooting.md",
    "references/compatibility.md",
    "references/safety-policy.md",
    "references/limitations.md",
    "references/attribution.md",
    "scripts/environment_check.py",
    "scripts/installation_check.py",
    "scripts/project_info.py",
    "scripts/validate_skill.py",
    "scripts/report_validator.py",
    "scripts/compatibility_check.py",
    "templates/security-assessment.md",
    "templates/vulnerability-report.md",
    "templates/executive-summary.md",
    "templates/remediation-plan.md",
    "templates/assessment-checklist.md",
    "schemas/vulnerability-report.schema.json",
    "schemas/assessment.schema.json",
    "examples/installation.md",
    "examples/security-assessment.md",
    "examples/vulnerability-analysis.md",
    "examples/report-generation.md",
    "examples/troubleshooting.md",
    "tests/test_structure.py",
    "tests/test_frontmatter.py",
    "tests/test_scripts.py",
    "tests/test_schemas.py",
    "tests/test_references.py",
    "tests/test_security.py",
    "tests/test_packaging.py",
    "tests/test_compatibility.py",
    ".github/workflows/validate.yml",
    ".github/workflows/release.yml",
    "distribution/README.md",
]


def check_files() -> list[str]:
    return [name for name in REQUIRED_FILES if not (ROOT / name).is_file()]


def check_skill_frontmatter() -> list[str]:
    errors: list[str] = []
    skill = (ROOT / "SKILL.md").read_text(encoding="utf-8")
    if not skill.startswith("---\n"):
        return ["SKILL.md missing opening frontmatter fence"]
    parts = skill.split("---\n", 2)
    if len(parts) < 3:
        return ["SKILL.md frontmatter not closed"]
    frontmatter = parts[1]
    if "name:" not in frontmatter:
        errors.append("frontmatter missing 'name'")
    if "description:" not in frontmatter:
        errors.append("frontmatter missing 'description'")
    if "exaaiagent-security" not in frontmatter:
        errors.append("frontmatter name should be exaaiagent-security")
    return errors


def check_schemas() -> list[str]:
    errors: list[str] = []
    for name in ("vulnerability-report.schema.json", "assessment.schema.json"):
        path = ROOT / "schemas" / name
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError) as exc:
            errors.append(f"{name}: invalid JSON: {exc}")
            continue
        if data.get("$schema") != "https://json-schema.org/draft/2020-12/schema":
            errors.append(f"{name}: unexpected $schema {data.get('$schema')!r}")
        if "title" not in data:
            errors.append(f"{name}: missing title")
    return errors


def check_no_shell_true() -> list[str]:
    offenders: list[str] = []
    for script in sorted((ROOT / "scripts").glob("*.py")):
        text = script.read_text(encoding="utf-8")
        if "shell" + "=True" in text:
            offenders.append(script.name)
    return offenders


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--json", action="store_true", help="Emit JSON output")
    args = parser.parse_args(argv)

    missing = check_files()
    frontmatter_errors = check_skill_frontmatter()
    schema_errors = check_schemas()
    shell_offenders = check_no_shell_true()
    ok = not (missing or frontmatter_errors or schema_errors or shell_offenders)

    result: dict[str, object] = {
        "ok": ok,
        "missing_files": missing,
        "frontmatter_errors": frontmatter_errors,
        "schema_errors": schema_errors,
        "shell_true_offenders": shell_offenders,
    }
    if args.json:
        print(json.dumps(result, indent=2))
    else:
        print(f"valid: {ok}")
        for key in ("missing_files", "frontmatter_errors", "schema_errors", "shell_true_offenders"):
            for item in result[key]:  # type: ignore[union-attr]
                print(f"  {key}: {item}")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
