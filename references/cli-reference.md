# CLI Reference (ExaAiAgent 3.0.1)

Entry points: `exaai`, `exaaiagent`, `ExaAiAgent` →
`exaaiagnt.interface.main:main`.

## Flags

| Flag | Type / default | Description |
|---|---|---|
| `-V`, `--version` | flag | Print version and exit |
| `-t`, `--target` | repeatable string | Target: URL, repository, local path, domain, or IP |
| `-i`, `--instruction` | string | Custom instructions or path to instruction file |
| `--prompt-modules` | string | Comma-separated prompt modules (overrides auto-detection) |
| `--profile` | string | v3 run profile |
| `--mode` | string | v3 run mode |
| `--no-pull` | string | v3 no-pull control |
| `--output-format` | `json\|sarif\|csv\|html\|md`, default `json` | Unified report format |
| `--output-dir` | string, default `exaai_runs` | Report output directory |
| `--severity-threshold` | `critical\|high\|medium\|low\|info`, default `info` | Minimum reported severity |
| `--timeout` | int, default `0` | Scan timeout in seconds (0 = default) |
| `--max-agents` | int, default `0` | Maximum parallel agents (0 = default) |
| `--list-modules` | flag | List prompt modules and exit |
| `--dry-run` | flag | Validate config and exit without scanning |
| `--resume` | string (path) | Resume a previous run directory |
| `--legacy-report` | flag | Legacy per-finding `./reports/*.json` (deprecated) |
| `--run-name` | string | Custom run name |
| `-n`, `--non-interactive` | flag | Non-interactive mode (no TUI; exit on completion) |

## Subcommands

- `tui` — launch the interactive TUI without a target.

## Examples

```bash
exaai tui
exaai --version
exaai -t https://example.com -n
exaai -t https://github.com/user/repo -t ./local-dir -n
exaai -t example.com -i "Focus on IDOR and XSS" -n
exaai -t example.com -i ./instructions.txt -n
exaai -t example.com --prompt-modules kubernetes_security,prompt_injection -n
exaai -t example.com --dry-run -n
exaai --list-modules
```

## Exit behavior

Invalid usage (e.g. scan without `--target`) exits with an argparse
error. Use `exaai tui` to start interactively without a target, or
supply `-t` for a scan.
