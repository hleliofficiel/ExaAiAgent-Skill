# Installation

## Requirements

- Python **^3.12** (upstream ExaAiAgent requirement).
- Network access to install the `exaai-agent` package.
- (Optional) External scanner binaries used by wrapper tools: `nuclei`,
  `httpx`/`katana`, `zap`, and an OAST listener for out-of-band tests.
  These are optional; core CLI and local analysis work without them.
- (Optional) LLM provider credentials for agent reasoning features
  (upstream uses `litellm`). Never commit these.

The skill package itself has **no runtime dependencies** — its scripts and
tests are standard-library only and run on Python 3.10+.

## Install upstream ExaAiAgent

```bash
pip install exaai-agent==3.0.1
# or, isolated:
pipx install exaai-agent==3.0.1
```

Entry points provided: `exaai`, `exaaiagent`, `ExaAiAgent`.

## Verify

```bash
exaai --version          # prints ExaAi v3.0.1
exaai --list-modules     # lists prompt modules
python3 scripts/installation_check.py
python3 scripts/environment_check.py
```

## First smoke test (no scanning)

```bash
exaai -t https://example.com --dry-run -n
```

`--dry-run` validates configuration and exits without scanning.

## Authorized scan example

```bash
exaai -t https://example.com \
  -i "Focus on authentication vulnerabilities" \
  -n --output-format json --output-dir exaai_runs \
  --severity-threshold info --timeout 600
```

Only run this against targets you own or are authorized to test.

## Skill package

The skill is a plain directory/ZIP. Unzip `ExaAiAgent-Skill-v1.0.0.zip`
(anywhere) and point your AI agent at the directory containing `SKILL.md`.
No build step is required.

## Troubleshooting

See `references/troubleshooting.md` and `examples/troubleshooting.md`.
