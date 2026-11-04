# Configuration

ExaAiAgent is configured primarily through CLI flags (see
`cli-reference.md`). Key knobs:

- **Targets**: `-t/--target` (repeatable; URL, repo, local path, domain, IP).
- **Instructions**: `-i/--instruction` — inline text or a file path.
- **Modules**: `--prompt-modules` (comma-separated) overrides auto-detection.
- **Profiles**: `--profile`, `--mode`, `--no-pull` (v3 run controls).
- **Output**: `--output-format` (`json|sarif|csv|html|md`),
  `--output-dir` (default `exaai_runs`), `--legacy-report`.
- **Limits**: `--timeout` (seconds, 0 = default), `--max-agents`
  (0 = default), `--severity-threshold` (`critical|high|medium|low|info`).
- **Run control**: `--run-name`, `--resume <dir>`, `--dry-run`,
  `-n/--non-interactive`, `tui` subcommand.

## Safe defaults

- Always start with `--dry-run`.
- Use explicit `--timeout` and `--max-agents` for unattended runs.
- Use `--severity-threshold` to reduce noise in large surfaces.
- Keep `--output-dir` inside the workspace; treat reports as confidential.

## Secrets

Pass LLM/API credentials via environment variables or the upstream
config mechanism — never via CLI flags that get logged, never in
committed files, never in reports. Redact before sharing.
