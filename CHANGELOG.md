# Changelog

All notable changes to ExaAiAgent-Skill are documented in this file.
Format follows Keep a Changelog; versioning is SemVer.

## [1.0.0] - 2026-11-04

### Added
- `SKILL.md` skill definition with valid YAML frontmatter.
- Complete production structure: README, LICENSE (Apache-2.0), NOTICE,
  CONTRIBUTING, SECURITY, VERSION, INSTALLATION, DISTRIBUTION, RELEASE_NOTES.
- `references/` (15 files): architecture, capabilities, installation,
  configuration, cli-reference, security-workflows, vulnerability-analysis,
  cve-reference, kubernetes-security, reporting, troubleshooting,
  compatibility, safety-policy, limitations, attribution.
- `scripts/` (6 stdlib-only scripts): environment_check, installation_check,
  project_info, validate_skill, report_validator, compatibility_check.
- `templates/` (5): security-assessment, vulnerability-report,
  executive-summary, remediation-plan, assessment-checklist.
- `schemas/` (2 JSON Schemas, draft 2020-12): vulnerability-report, assessment.
- `examples/` (5): installation, security-assessment, vulnerability-analysis,
  report-generation, troubleshooting.
- `tests/` (8 unittest modules, stdlib only).
- GitHub Actions: `.github/workflows/validate.yml`, `release.yml`.
- `distribution/README.md`, `.gitignore`, `pyproject.toml`.

### Notes
- Skill targets upstream ExaAiAgent 3.0.1 (Python ^3.12).
- No runtime dependencies for the skill package itself; upstream
  `exaai-agent` is installed separately.
