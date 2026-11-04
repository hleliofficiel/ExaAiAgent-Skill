# Installation (reference)

See `INSTALLATION.md` for the full guide. Summary:

1. Python ^3.12 required for upstream ExaAiAgent.
2. `pip install exaai-agent==3.0.1` (or `pipx install`).
3. Verify: `exaai --version`, `exaai --list-modules`.
4. Run skill checks: `python3 scripts/environment_check.py`,
   `python3 scripts/installation_check.py`.
5. Dry run: `exaai -t <authorized-target> --dry-run -n`.

Optional external tools: nuclei, httpx/katana, zap, an OAST listener,
and LLM provider credentials (via `litellm`) for reasoning features.
None are required for installation or for the skill's validators/tests.
