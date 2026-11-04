# Security Workflows

## 1. Authorized assessment (standard)

1. Record authorization: owner, scope, exclusions, window.
2. `python3 scripts/environment_check.py` + `installation_check.py`.
3. `exaai -t <target> --dry-run -n`; fix config errors.
4. Run: `exaai -t <target> -n --output-format json --output-dir exaai_runs`.
5. Verify each finding (reproduce/confirm). See `vulnerability-analysis.md`.
6. Validate report: `python3 scripts/report_validator.py <report>`.
7. Present using `templates/`; attach the raw report.

## 2. Focused vulnerability hunt

Use `-i` to narrow scope, e.g. `-i "Focus on authentication
vulnerabilities"` or `-i ./instructions.txt`, and `--prompt-modules`
to pin modules. Keep `--severity-threshold` at `info` for hunts, then
filter.

## 3. Multi-target / repository audit

Repeat `-t` per target. For local code, point `-t` at the directory.
Use `--resume <dir>` to continue a previous run instead of restarting.

## 4. CI / automation

Use `-n` (non-interactive), explicit `--timeout`/`--max-agents`,
`--output-format sarif` for SARIF consumers, and fail the job when
critical/high findings exist. Never run in CI against targets without
documented authorization.

## 5. Kubernetes-focused review

Select the `kubernetes_security` module and/or the `k8s_scanner` tools;
see `kubernetes-security.md`.

## 6. LLM / prompt-injection review

Select the `prompt_injection` module and `llm_tests` tools; treat the
target LLM as untrusted input and report only reproducible behaviors.
