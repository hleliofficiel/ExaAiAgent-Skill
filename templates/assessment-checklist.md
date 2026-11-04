# Security Assessment Checklist

- **Assessment ID:** {{assessment_id}}
- **Target:** {{target}}
- **Date:** {{date}}

## Pre-assessment

- [ ] Written authorization recorded (owner, scope, window)
- [ ] In-scope targets and exclusions documented
- [ ] Emergency stop contact agreed
- [ ] Environment checked (`scripts/environment_check.py`)
- [ ] Installation verified (`scripts/installation_check.py`)

## Execution

- [ ] Dry run completed (`--dry-run`)
- [ ] Run executed in scope (`-n`, `--timeout`, `--max-agents`)
- [ ] Report generated (`--output-format`, `--output-dir`)

## Verification

- [ ] Each finding reproduced/confirmed
- [ ] Duplicates grouped by root cause
- [ ] False positives excluded
- [ ] Severities honestly assigned
- [ ] CVE/CWE citations evidence-backed

## Reporting

- [ ] Report validated (`scripts/report_validator.py`)
- [ ] Secrets redacted
- [ ] Audience template applied (`templates/`)
- [ ] Raw report attached
- [ ] Remediation owners and due dates assigned

## Close-out

- [ ] Findings shared with stakeholders
- [ ] Retest scheduled
- [ ] Reports archived/deleted per retention policy
