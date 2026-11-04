# Compatibility

## Upstream ExaAiAgent

| Requirement | Value |
|---|---|
| Package | `exaai-agent` 3.0.1 |
| Python | ^3.12 |
| Entry points | `exaai`, `exaaiagent`, `ExaAiAgent` → `exaaiagnt.interface.main:main` |
| Report formats | `json`, `sarif`, `csv`, `html`, `md` |
| Severity levels | `critical`, `high`, `medium`, `low`, `info` |

## Skill package

| Requirement | Value |
|---|---|
| Python (scripts/tests) | >=3.10, standard library only |
| Platform | Linux/macOS/Windows (path-agnostic scripts) |
| Network | Not required for skill validators/tests |

Run `python3 scripts/compatibility_check.py` to check the current
environment against this matrix.

## Known constraints

- Upstream LLM features need provider credentials and `litellm`; the
  skill package does not bundle them.
- External scanner wrappers need their binaries installed.
- Behavior described here is verified against upstream 3.0.1
  (`feat/v3.0.1-final-comprehensive`, d491332). Later upstream
  releases may change CLI flags — re-verify with `--list-modules`
  and `--help`.
