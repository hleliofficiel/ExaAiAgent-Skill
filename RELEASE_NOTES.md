# Release Notes

## v1.0.0 (2026-11-04)

Initial production release of **ExaAiAgent-Skill**, an independent
AI-agent integration developed by ExaAi for the original ExaAiAgent
(https://github.com/hleliofficiel/ExaAiAgent), targeting upstream
ExaAiAgent **3.0.1**.

### Highlights

- Complete skill package with valid-frontmatter `SKILL.md`.
- 15 reference guides covering architecture, CLI, safety, workflows,
  reporting, Kubernetes security, CVE handling, and troubleshooting.
- 6 stdlib-only helper scripts (checks and validators).
- 5 report templates and 2 JSON Schemas (draft 2020-12).
- 5 worked examples and a stdlib `unittest` suite (8 modules).
- GitHub Actions for validation and release ZIP builds.

### Compatibility

- Upstream: `exaai-agent` 3.0.1, Python ^3.12.
- Skill scripts/tests: Python 3.10+, standard library only.

### Limitations

- External tools (nuclei, httpx/katana, zap, OAST) and LLM providers are
  not live-tested by this package; see `references/limitations.md`.
- Findings must come from real runs — this package never fabricates results.
