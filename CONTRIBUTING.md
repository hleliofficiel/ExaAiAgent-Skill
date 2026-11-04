# Contributing to ExaAiAgent-Skill

<!-- project: path:/data/home/.openclaw/workspace -->

## Rules

1. **Authorized testing only.** Examples and docs must only show scans
   against systems the reader owns or is authorized to test. Never add
   instructions for attacking third parties without authorization.
2. **No fabrication.** Documentation must describe real ExaAiAgent
   behavior (v3.0.1). If a feature is unverified, say so.
3. **Stdlib only.** Scripts and tests must use only the Python standard
   library (no third-party imports, no `shell=True`).
4. **Tests must pass.** Run `python3 -m unittest discover -s tests -v`
   before submitting.
5. **Frontmatter validity.** `SKILL.md` frontmatter must parse as YAML
   with `name` and `description`.

## Workflow

1. Fork the repository and create a branch.
2. Make changes; keep docs and references in sync with `SKILL.md`.
3. Add or update tests for new scripts/schemas/references.
4. Run the full test suite and the validators:
   `python3 scripts/validate_skill.py`
5. Open a pull request describing the change and its safety implications.

## Code style

- Typed Python (`from __future__ import annotations` where useful),
  `argparse` for CLI, no `shell=True`, no `eval`.
- Markdown: short lines, fenced code blocks with language tags.
