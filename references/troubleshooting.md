# Troubleshooting

## Installation

- `exaai: command not found` — the package is not installed or not on
  `PATH`. Reinstall (`pip install exaai-agent==3.0.1`) or use the full
  path from `pip show -f exaai-agent`. Check with
  `python3 scripts/installation_check.py`.
- Python version errors — upstream needs ^3.12. Use a 3.12+ interpreter
  (`python3.12 -m pip install ...`).
- `litellm` import errors — install the full dependency set
  (`pip install exaai-agent[proxy]` per upstream) or accept limited
  LLM features; see `limitations.md`.

## Runtime

- `--target is required` — supply `-t`, or use `exaai tui`.
- Blocklist/scope refusal — the target is out of scope or blocklisted
  by `exaaiagnt/safety/`. Do not bypass; confirm authorization.
- TUI issues in non-TTY shells — use `-n` (non-interactive).
- Timeouts — raise `--timeout`, lower `--max-agents`, or narrow scope
  with `-i` / `--prompt-modules`.

## External tools

- Wrapper failures (nuclei/httpx/katana/zap/OAST) — install the
  respective binaries or accept reduced coverage; core analysis still
  works. Check with `scripts/environment_check.py`.

## Reports

- Empty report — check `--severity-threshold` (try `info`), scope
  exclusions, and that the run actually completed (exit code, run dir).
- Validator errors — re-run with `--output-format json` and validate
  against `schemas/`; see `examples/report-generation.md`.

## Skill package

- Tests failing — run `python3 -m unittest discover -s tests -v` and
  `python3 scripts/validate_skill.py` for structure/frontmatter issues.
