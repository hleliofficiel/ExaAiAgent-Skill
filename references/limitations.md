# Limitations

1. **Not live-tested end to end.** This skill package was validated
   structurally (docs, scripts, schemas, tests) against upstream
   ExaAiAgent 3.0.1 source. Live scans, external wrappers
   (nuclei, httpx/katana, zap, OAST), browser automation, and LLM
   provider calls were not exercised here.
2. **`litellm` not installed** in the build environment; provider-backed
   agent features could not be verified. Install upstream fully
   (`pip install exaai-agent==3.0.1`) before relying on them.
3. **External binaries optional.** Without nuclei/httpx/katana/zap/OAST,
   coverage is reduced to built-in analysis.
4. **CLI surface pinned to 3.0.1.** Later upstream releases may add or
   rename flags; re-check `exaai --help` and `--list-modules`.
5. **No dynamic security guarantees.** Safety controls are described as
   shipped upstream; this package does not audit their implementation.
6. **Schemas are contracts, not guarantees.** `schemas/` validate shape;
   they cannot prove a finding's truth. Human verification is required.
7. **Platform variance.** Verified on Linux; macOS/Windows behavior is
   best-effort (scripts are path-agnostic, stdlib-only).
