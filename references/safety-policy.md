# Safety Policy

## Authorized testing only

Use ExaAiAgent exclusively against systems you own or have explicit,
documented authorization to test. Before any run, record:

- Authorizing person/organization and date.
- In-scope targets (URLs, repos, paths, domains, IPs).
- Exclusions and prohibited techniques.
- Testing window and emergency stop contact.

If authorization is unclear, do not run. Ask the user to confirm.

## Built-in controls (do not bypass)

Upstream ships safety controls in `exaaiagnt/safety/`:

- `scope.py` — scope enforcement.
- `blocklist.py` — blocklisted targets.
- `command_guard.py` — guarded command execution.
- `target_tracker.py` — target tracking.

Never disable, patch out, or route around these controls. A blocklist
or scope refusal is a stop signal — escalate to the user instead.

## Safe defaults

- Start with `--dry-run`.
- Prefer `-n` non-interactive runs with explicit `--timeout` and
  `--max-agents`.
- Use `--severity-threshold` to limit noise, not to hide findings from
  the final report (report everything, filter presentation).
- Treat the verification pipeline as mandatory: confirm before reporting.

## Data handling

- Reports may contain sensitive target data — store in `--output-dir`
  inside the workspace, restrict access, redact secrets.
- Never print credentials, tokens, or API keys in chat or logs.
- Delete or archive reports per the engagement's retention policy.

## No fabrication

Report only real run output. Unverified items are labeled
`unverified`. Inventing findings, CVEs, or scores is prohibited.
