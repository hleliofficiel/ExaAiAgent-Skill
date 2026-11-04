# Example: Troubleshooting

## `exaai: command not found`

```bash
pip install exaai-agent==3.0.1
python3 scripts/installation_check.py
```

## Python version too old

Upstream needs ^3.12. Use a 3.12+ interpreter and reinstall.

## Scan refused / `--target is required`

- Supply `-t`, or run `exaai tui` for interactive mode.
- A scope/blocklist refusal means the target is out of scope — do not
  bypass it; confirm authorization instead.

## Empty report

Check `--severity-threshold` (try `info`), scope exclusions, and that
the run completed (exit code and run directory under `--output-dir`).

## Validator errors

Re-run with `--output-format json`, then
`python3 scripts/report_validator.py <report>`. Compare against
`schemas/vulnerability-report.schema.json`.

See `references/troubleshooting.md` for the full list.
