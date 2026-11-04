# Example: Installation

Goal: install upstream ExaAiAgent and verify it, then run the skill
checks. Only install from the official package.

```bash
python3 --version            # expect 3.12+
pip install exaai-agent==3.0.1

exaai --version              # ExaAi v3.0.1
exaai --list-modules         # prompt modules listed

python3 scripts/installation_check.py
python3 scripts/environment_check.py --json
python3 scripts/compatibility_check.py
```

Expected: `installation_check.py` reports `installed: True` and all
three entry points (`exaai`, `exaaiagent`, `ExaAiAgent`) on `PATH`.
If `litellm` is missing, core CLI still works; LLM-backed features
may be limited (see `references/limitations.md`).
