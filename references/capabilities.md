# Capabilities

Tool groups under `exaaiagnt/tools/` (upstream 3.0.1):

| Directory | Purpose |
|---|---|
| `agents_graph` | Multi-agent graph orchestration |
| `api` | HTTP/API interaction helpers |
| `browser` | Browser automation surface |
| `coordination` | Agent coordination primitives |
| `file_edit` | Sandboxed file editing |
| `finish` | Run completion/report finalization |
| `k8s_scanner` | Kubernetes configuration scanning |
| `knowledge` | Internal knowledge retrieval |
| `llm_tests` | LLM-specific security tests |
| `notes` | Working notes / memory |
| `prompt_injection` | Prompt-injection test scenarios |
| `proxy` | Traffic proxying (HAR capture) |
| `python` | Python execution tool |
| `reporting` | Report generation tools |
| `terminal` | Terminal/command execution (guarded) |
| `thinking` | Reasoning scaffolding |
| `web_search` | Web search for threat intel |
| `wrappers` | External scanner wrappers |

## External scanner wrappers (`tools/wrappers/`)

- `httpx_katana_wrapper.py` — httpx probing + katana crawling.
- `nuclei_wrapper.py` — template-based nuclei scanning.
- `oast_wrapper.py` — out-of-band (OAST) interaction testing.
- `zap_wrapper.py` — OWASP ZAP integration.

These require the respective binaries/services installed; core CLI and
local-code analysis work without them.

## Target types

- Web applications (URLs)
- Git repositories (URLs or local paths)
- Local directories
- Domains and IP addresses

## Prompt modules

Security prompt modules (vulnerabilities, technologies, reconnaissance,
protocols, frameworks) auto-load per target or are chosen explicitly via
`--prompt-modules`. List them with `exaai --list-modules`.
