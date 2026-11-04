---
name: exaaiagent-security
description: Use the ExaAiAgent AI security agent (v3.0.1) for authorized penetration testing, vulnerability analysis, and security assessment reporting. Trigger when a user asks to scan, pentest, audit, or assess a target they own or are authorized to test, review security findings, or generate vulnerability reports.
license: Apache-2.0
metadata:
  version: "1.0.0"
  exaaiagent_version: "3.0.1"
  author: "ExaAi"
  original_repo: "https://github.com/hleliofficiel/ExaAiAgent"
  skill_repo: "https://github.com/hleliofficiel/ExaAiAgent-Skill"
---

# ExaAiAgent Security Skill

> **Attribution:** ExaAiAgent-Skill is an independent AI-agent integration developed by ExaAi for the original ExaAiAgent project (https://github.com/hleliofficiel/ExaAiAgent). This skill is not part of, and is not endorsed by, the upstream ExaAiAgent repository unless stated otherwise. Skill repository: https://github.com/hleliofficiel/ExaAiAgent-Skill.

## When to use this skill

Use this skill when the user asks to:

- run or plan an authorized security assessment / penetration test with ExaAiAgent,
- analyze vulnerabilities in a web app, repository, local codebase, domain, or IP they own or are authorized to test,
- review, triage, or format ExaAiAgent findings (JSON, SARIF, CSV, HTML, Markdown),
- produce security reports: vulnerability reports, executive summaries, remediation plans, checklists.

Do **not** use this skill for targets the user is not authorized to test. Always confirm authorization scope before running any scan.

## Safety rules (mandatory)

1. **Authorized testing only.** Only scan targets the user owns or has explicit written authorization to test. Record the authorized scope (targets, exclusions, time window) before a run.
2. **Safe defaults.** Prefer `--dry-run`, `--severity-threshold`, `--timeout`, and `--max-agents` to limit blast radius. Never disable safety controls.
3. **No fabrication.** Report only findings produced by an actual run or supplied evidence. Mark unverified items as `unverified`. Never invent CVEs, severities, or exploit results.
4. **Secrets.** Never print or commit API keys, credentials, or tokens. Redact them from reports.
5. **Scope enforcement.** ExaAiAgent ships scope/blocklist/command-guard controls (`exaaiagnt/safety/`). Do not bypass them; if a target is blocklisted, stop and escalate to the user.

## Quick start

```bash
# 1. Install upstream ExaAiAgent (Python ^3.12)
pipx install exaai-agent==3.0.1        # or: pip install exaai-agent==3.0.1

# 2. Verify
exaai --version
exaai --list-modules

# 3. Dry-run (validates config, no scanning)
exaai -t https://example.com --dry-run -n

# 4. Authorized scan (example; replace with in-scope target)
exaai -t https://example.com \
  -i "Focus on authentication vulnerabilities" \
  --output-format json --output-dir exaai_runs \
  --severity-threshold info --timeout 600 -n

# 5. Interactive TUI
exaai tui
```

Entry points: `exaai`, `exaaiagent`, `ExaAiAgent` → `exaaiagnt.interface.main:main`.

## Workflow

1. **Confirm authorization and scope** — targets, exclusions, allowed techniques, time window. See `references/safety-policy.md`.
2. **Environment check** — run `scripts/environment_check.py` and `scripts/installation_check.py`.
3. **Dry run** — `exaai -t <target> --dry-run -n`, fix config errors.
4. **Run** — non-interactive (`-n`) for automation; TUI (`exaai tui`) for interactive sessions.
5. **Verify findings** — apply the verification pipeline mindset: reproduce, confirm impact, de-duplicate. See `references/vulnerability-analysis.md`.
6. **Report** — choose format (`json|sarif|csv|html|md`), validate with `scripts/report_validator.py`, use templates in `templates/`.

## CLI reference (summary)

| Flag | Meaning |
|---|---|
| `-V/--version` | Print version |
| `-t/--target` | Target (URL, repo, local path, domain, IP); repeatable |
| `-i/--instruction` | Custom instructions or path to instruction file |
| `--prompt-modules` | Comma-separated modules (overrides auto-detection) |
| `--profile/--mode/--no-pull` | v3 run profile/mode/pull controls |
| `--output-format` | `json` (default), `sarif`, `csv`, `html`, `md` |
| `--output-dir` | Report directory (default `exaai_runs`) |
| `--severity-threshold` | `critical\|high\|medium\|low\|info` |
| `--timeout` | Scan timeout in seconds (0 = default) |
| `--max-agents` | Cap on parallel agents (0 = default) |
| `--list-modules` | List prompt modules and exit |
| `--dry-run` | Validate config and exit without scanning |
| `--resume <dir>` | Resume a previous run directory |
| `--legacy-report` | Legacy per-finding `./reports/*.json` (deprecated) |
| `--run-name` | Custom run name |
| `-n/--non-interactive` | No TUI; exit on completion |
| `tui` subcommand | Launch interactive TUI without a target |

Full reference: `references/cli-reference.md`.

## Tool capabilities

ExaAiAgent tool groups (`exaaiagnt/tools/`): `agents_graph`, `api`, `browser`, `coordination`, `file_edit`, `finish`, `k8s_scanner`, `knowledge`, `llm_tests`, `notes`, `prompt_injection`, `proxy`, `python`, `reporting`, `terminal`, `thinking`, `web_search`, `wrappers` (`httpx_katana`, `nuclei`, `oast`, `zap`). Detail: `references/capabilities.md`.

## References

- Architecture: `references/architecture.md`
- Capabilities: `references/capabilities.md`
- Installation: `references/installation.md` (also `INSTALLATION.md`)
- Configuration: `references/configuration.md`
- CLI reference: `references/cli-reference.md`
- Security workflows: `references/security-workflows.md`
- Vulnerability analysis: `references/vulnerability-analysis.md`
- CVE reference: `references/cve-reference.md`
- Kubernetes security: `references/kubernetes-security.md`
- Reporting: `references/reporting.md`
- Troubleshooting: `references/troubleshooting.md`
- Compatibility: `references/compatibility.md`
- Safety policy: `references/safety-policy.md`
- Limitations: `references/limitations.md`
- Attribution: `references/attribution.md`

## Scripts (stdlib only)

- `scripts/environment_check.py` — Python version, platform, disk, optional deps.
- `scripts/installation_check.py` — `exaai` entry points and version.
- `scripts/project_info.py` — package metadata summary.
- `scripts/validate_skill.py` — validate this skill package structure/frontmatter.
- `scripts/report_validator.py` — validate a report against `schemas/`.
- `scripts/compatibility_check.py` — check environment against compatibility matrix.

## Templates and schemas

- Templates: `templates/security-assessment.md`, `vulnerability-report.md`, `executive-summary.md`, `remediation-plan.md`, `assessment-checklist.md`
- Schemas (JSON Schema draft 2020-12): `schemas/vulnerability-report.schema.json`, `schemas/assessment.schema.json`
- Examples: `examples/installation.md`, `security-assessment.md`, `vulnerability-analysis.md`, `report-generation.md`, `troubleshooting.md`
