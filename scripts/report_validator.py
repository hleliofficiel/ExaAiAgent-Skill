#!/usr/bin/env python3
"""Validate a JSON report against the skill schemas (structural checks).

Stdlib only (no jsonschema dependency). Performs required-field and
enum checks mirroring schemas/vulnerability-report.schema.json and
schemas/assessment.schema.json. Never uses a shell.
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

SEVERITIES = {"critical", "high", "medium", "low", "info"}
STATUSES = {"confirmed", "unverified", "false-positive", "remediated"}
REPORT_FORMATS = {"json", "sarif", "csv", "html", "md"}

FINDING_REQUIRED = ["title", "severity", "target", "description", "status"]
ASSESSMENT_REQUIRED = ["assessment_id", "target", "findings"]


def validate_finding(finding: object, index: int) -> list[str]:
    errors: list[str] = []
    prefix = f"findings[{index}]"
    if not isinstance(finding, dict):
        return [f"{prefix}: not an object"]
    for field in FINDING_REQUIRED:
        if field not in finding:
            errors.append(f"{prefix}: missing required field '{field}'")
    severity = finding.get("severity")
    if severity is not None and severity not in SEVERITIES:
        errors.append(f"{prefix}: invalid severity {severity!r}")
    status = finding.get("status")
    if status is not None and status not in STATUSES:
        errors.append(f"{prefix}: invalid status {status!r}")
    return errors


def validate_report(data: object) -> list[str]:
    errors: list[str] = []
    if not isinstance(data, dict):
        return ["report: top level must be an object"]
    if "findings" in data:
        findings = data["findings"]
        if not isinstance(findings, list):
            errors.append("findings: must be a list")
        else:
            for idx, finding in enumerate(findings):
                errors.extend(validate_finding(finding, idx))
    fmt = data.get("output_format")
    if fmt is not None and fmt not in REPORT_FORMATS:
        errors.append(f"output_format: invalid format {fmt!r}")
    return errors


def validate_assessment(data: object) -> list[str]:
    errors: list[str] = []
    if not isinstance(data, dict):
        return ["assessment: top level must be an object"]
    for field in ASSESSMENT_REQUIRED:
        if field not in data:
            errors.append(f"assessment: missing required field '{field}'")
    findings = data.get("findings")
    if isinstance(findings, list):
        for idx, finding in enumerate(findings):
            errors.extend(validate_finding(finding, idx))
    return errors


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("report", help="Path to a JSON report file")
    parser.add_argument("--kind", choices=["report", "assessment"], default="report")
    parser.add_argument("--json", action="store_true", help="Emit JSON output")
    args = parser.parse_args(argv)

    path = Path(args.report)
    if not path.is_file():
        print(f"report not found: {path}", file=sys.stderr)
        return 2
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        print(f"invalid JSON: {exc}", file=sys.stderr)
        return 2

    errors = validate_assessment(data) if args.kind == "assessment" else validate_report(data)
    result: dict[str, object] = {"file": str(path), "valid": not errors, "errors": errors}
    if args.json:
        print(json.dumps(result, indent=2))
    else:
        print(f"valid: {not errors}")
        for err in errors:
            print(f"  - {err}")
    return 0 if not errors else 1


if __name__ == "__main__":
    raise SystemExit(main())
