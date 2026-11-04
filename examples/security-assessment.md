# Example: Security Assessment (authorized target only)

Prerequisite: written authorization for the target. Replace
`https://example.com` with an in-scope target you own.

```bash
# 1. Checks
python3 scripts/environment_check.py
python3 scripts/installation_check.py

# 2. Dry run (no scanning)
exaai -t https://example.com --dry-run -n

# 3. Run
exaai -t https://example.com \
  -i "Focus on authentication vulnerabilities" \
  -n --output-format json --output-dir exaai_runs \
  --severity-threshold info --timeout 600 --run-name example-assessment

# 4. Validate the report
python3 scripts/report_validator.py exaai_runs/<run>/report.json
```

Then verify findings, and present results with
`templates/security-assessment.md` and `templates/executive-summary.md`.
