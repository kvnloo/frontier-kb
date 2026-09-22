#!/usr/bin/env python3
"""Fail CI if markdown notes under literature/permanent/harnesses miss required frontmatter."""
from __future__ import annotations
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REQUIRED = {"id", "title", "type", "status", "created", "updated"}
DIRS = ["literature", "permanent", "harnesses", "domains", "atlas", "inbox", "templates", "notes"]

def parse_frontmatter(text: str) -> dict:
    if not text.startswith("---"):
        return {}
    parts = text.split("---", 2)
    if len(parts) < 3:
        return {}
    meta = {}
    for line in parts[1].strip().splitlines():
        if ":" in line:
            k, v = line.split(":", 1)
            meta[k.strip()] = v.strip()
    return meta

def main() -> int:
    errors = []
    for d in DIRS:
        folder = ROOT / d
        if not folder.exists():
            continue
        for path in folder.rglob("*.md"):
            # Skip README.md, .gitkeep files, and template placeholders
            if path.name in ("README.md", ".gitkeep"):
                continue
            meta = parse_frontmatter(path.read_text(encoding="utf-8"))
            missing = REQUIRED - set(meta)
            if missing:
                errors.append(f"{path.relative_to(ROOT)}: missing {sorted(missing)}")
    # The store schema exists TWICE on purpose: `scripts/kb_store.py` declares
    # `SCHEMA_CANDIDATES = (store/schema.sql, scripts/schema.sql)`, so the second
    # copy is a code-referenced fallback, not accidental duplication. They are
    # byte-identical today. Two copies of one schema can drift, and the fallback
    # is precisely the path nobody exercises -- so the drift would surface only
    # when the primary is missing, which is the worst moment to find it.
    primary = ROOT / "store" / "schema.sql"
    fallback = ROOT / "scripts" / "schema.sql"
    if primary.is_file() and fallback.is_file():
        if primary.read_bytes() != fallback.read_bytes():
            errors.append(
                "store/schema.sql and scripts/schema.sql have DRIFTED. The second "
                "is kb_store.py's declared fallback; they must stay identical or "
                "the fallback path silently loads a different schema."
            )

    if errors:
        print("schema errors:")
        print("\n".join(errors))
        return 1
    print(f"ok: validated notes under {', '.join(DIRS)}")
    return 0

if __name__ == "__main__":
    sys.exit(main())
