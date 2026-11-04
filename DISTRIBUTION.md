# Distribution

## Release artifact

The canonical distribution artifact is a ZIP archive:

```
ExaAiAgent-Skill-v1.0.0.zip
```

It contains the full skill package with `SKILL.md` at the archive root so
AI agents can load it directly after extraction.

Build the ZIP from the repository root of this package:

```bash
python3 - <<'PY'
import zipfile, pathlib
root = pathlib.Path(".")
out = pathlib.Path("ExaAiAgent-Skill-v1.0.0.zip")
with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as z:
    for p in sorted(root.rglob("*")):
        if p.is_file() and "__pycache__" not in p.parts and p.suffix != ".pyc":
            if p.name == out.name:
                continue
            z.write(p, p.as_posix())
print(out)
PY
```

## Verify an artifact

```bash
mkdir /tmp/skill-check && cd /tmp/skill-check
unzip ExaAiAgent-Skill-v1.0.0.zip
test -f SKILL.md && echo "SKILL.md at root: OK"
python3 scripts/validate_skill.py
python3 -m unittest discover -s tests
```

## Publishing

- Tag releases as `v<version>` (e.g. `v1.0.0`).
- The `release.yml` workflow builds and attaches the ZIP to GitHub
  releases on tag push.
- Do **not** push to GitHub until the maintainer explicitly authorizes it.
- Mirror the ZIP on request; always keep `SKILL.md` at the ZIP root and
  never nest the package under an extra top-level folder.
