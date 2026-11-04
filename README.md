# ExaAiAgent-Skill

An independent AI-agent integration (skill package) for the original [ExaAiAgent](https://github.com/hleliofficiel/ExaAiAgent) AI security agent (v3.0.1), developed by ExaAi to help AI assistants run **authorized** penetration testing, vulnerability analysis, and security reporting workflows.

> ExaAiAgent-Skill is an independent AI-agent integration developed by ExaAi for original ExaAiAgent (https://github.com/hleliofficiel/ExaAiAgent). Skill repository: https://github.com/hleliofficiel/ExaAiAgent-Skill.

License: Apache-2.0 (see `LICENSE` and `NOTICE`).

## What is ExaAiAgent?

ExaAiAgent (upstream `exaai-agent` 3.0.1) is a Python 3.12 CLI AI agent for comprehensive penetration testing. It exposes three entry points — `exaai`, `exaaiagent`, `ExaAiAgent` — all pointing at `exaaiagnt.interface.main:main`. It supports web apps, git repositories, local directories, domains, and IP addresses as targets, with an interactive TUI (`exaai tui`) and non-interactive automation mode.

This skill package wraps that capability in:

- `SKILL.md` — the AI-agent skill definition (frontmatter + instructions).
- `references/` — architecture, capabilities, CLI, safety, reporting, troubleshooting, and more.
- `scripts/` — stdlib-only helper scripts (environment/installation checks, validators).
- `templates/` — report templates (assessment, vulnerability, executive summary, remediation, checklist).
- `schemas/` — JSON Schema (draft 2020-12) for reports and assessments.
- `examples/` — worked examples for installation, assessment, analysis, reporting, troubleshooting.
- `tests/` — stdlib `unittest` suite covering structure, frontmatter, scripts, schemas, references, security, packaging, compatibility.

## Quick start

```bash
# Install upstream
pip install exaai-agent==3.0.1

# Verify
exaai --version
exaai --list-modules

# Dry run first (no scanning)
exaai -t https://example.com --dry-run -n

# Authorized scan
exaai -t https://example.com -n --output-format json --output-dir exaai_runs
```

See `INSTALLATION.md` and `examples/installation.md` for details.

## Safety

Only test systems you own or are authorized to test. See `SECURITY.md` and `references/safety-policy.md`. Reports must reflect real run output — never fabricate findings.

## Layout

```
SKILL.md                  Skill definition (YAML frontmatter + instructions)
README.md                 This file
LICENSE / NOTICE          Apache-2.0 license text and notices
CHANGELOG.md              Release history
CONTRIBUTING.md           How to contribute
SECURITY.md               Security policy for this skill package
VERSION                   Package version (1.0.0)
INSTALLATION.md           Installation guide
DISTRIBUTION.md           How the ZIP/skill package is distributed
RELEASE_NOTES.md          Release notes for v1.0.0
pyproject.toml            Skill package metadata (no runtime deps)
references/               Deep-dive references (15 files)
scripts/                  6 stdlib-only helper scripts
templates/                5 report templates
schemas/                  2 JSON Schemas (draft 2020-12)
examples/                 5 worked examples
tests/                    8 unittest test modules
docs/                     Additional documentation
.github/workflows/        CI: validate.yml, release.yml
distribution/README.md    Distribution notes
```

## Tests

```bash
python3 -m unittest discover -s tests -v
```

## Compatibility

Requires Python ^3.12 for upstream ExaAiAgent. The skill's own scripts and tests are stdlib-only and run on Python 3.10+. See `references/compatibility.md`.
