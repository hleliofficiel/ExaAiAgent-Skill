# Reporting

## Formats

ExaAiAgent writes a unified report to `--output-dir` (default
`exaai_runs`) in `--output-format`:

- `json` (default): machine-readable; validate with
  `scripts/report_validator.py` against `schemas/`.
- `sarif`: SARIF for CI/code-scanning consumers.
- `csv`: spreadsheet/triage friendly.
- `html`, `md`: human-readable.

`--legacy-report` writes the deprecated per-finding `./reports/*.json`
layout; prefer the unified report.

## Pipeline

1. Run the scan (non-interactive for automation).
2. Validate: `python3 scripts/report_validator.py <report.json>`.
3. Verify findings (`vulnerability-analysis.md`).
4. Format for the audience:
   - Engineers: `templates/vulnerability-report.md`, `remediation-plan.md`.
   - Management: `templates/executive-summary.md`.
   - Process: `templates/security-assessment.md`, `assessment-checklist.md`.
5. Redact secrets; attach raw report; state scope and authorization.

## Schemas

- `schemas/vulnerability-report.schema.json` — single finding or report.
- `schemas/assessment.schema.json` — full assessment envelope.

## Retention

Treat reports as confidential. Keep them in the workspace output dir,
restrict access, and delete when retention expires.
