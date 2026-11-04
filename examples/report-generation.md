# Example: Report Generation

```bash
# Produce reports in each format (authorized target only)
exaai -t https://example.com -n --output-format json  --output-dir exaai_runs
exaai -t https://example.com -n --output-format sarif --output-dir exaai_runs
exaai -t https://example.com -n --output-format csv   --output-dir exaai_runs
exaai -t https://example.com -n --output-format html  --output-dir exaai_runs
exaai -t https://example.com -n --output-format md    --output-dir exaai_runs

# Validate the JSON report
python3 scripts/report_validator.py exaai_runs/<run>/report.json --json
```

Format for the audience:

- Engineers: `templates/vulnerability-report.md`, `remediation-plan.md`.
- Management: `templates/executive-summary.md`.
- Full package: `templates/security-assessment.md` + `assessment-checklist.md`.

Always redact secrets and attach the raw report.
