# Architecture

Upstream ExaAiAgent (`exaai-agent` 3.0.1) is a Python 3.12 agent system
organized under the `exaaiagnt` package.

## Layers

- **Interface** (`exaaiagnt/interface/main.py`): argparse CLI with flags and
  a `tui` subcommand; entry points `exaai` / `exaaiagent` / `ExaAiAgent`
  all resolve to `exaaiagnt.interface.main:main`.
- **Agents graph** (`exaaiagnt/tools/agents_graph/`): multi-agent
  orchestration; `--max-agents` caps parallelism.
- **Tools** (`exaaiagnt/tools/`): capability groups — see `capabilities.md`.
- **Prompts** (`exaaiagnt/prompts/`): vulnerability/technology/recon
  prompt modules, selectable via `--prompt-modules` or auto-detected
  from the target.
- **Safety** (`exaaiagnt/safety/`): `scope.py`, `blocklist.py`,
  `command_guard.py`, `target_tracker.py`. Enforce scope before any
  active testing.
- **Verification** (`exaaiagnt/verification/pipeline.py`,
  `hardening.py`): post-scan validation; apply the same mindset to
  findings (reproduce, confirm, de-duplicate).
- **Reporting** (`exaaiagnt/reporting/`): unified report writers for
  `json|sarif|csv|html|md` into `--output-dir` (default `exaai_runs`);
  `--legacy-report` keeps the deprecated per-finding JSON layout.

## Run lifecycle

1. Parse CLI args, resolve targets + instruction.
2. Select prompt modules (`--prompt-modules` or auto-detection).
3. Safety checks: scope, blocklist, command guard.
4. Execute agents/tools against in-scope targets.
5. Verification pipeline filters/confirms findings.
6. Unified report written to `--output-dir` in `--output-format`.
7. `--resume <dir>` reuses a previous run directory.

## Skill package architecture

This skill wraps the upstream CLI for AI-agent use: `SKILL.md` defines
when/how to invoke it; `scripts/` perform checks/validation with the
standard library only; `schemas/` define report contracts; `templates/`
format human-facing output. The skill adds no runtime dependency on the
upstream package.
