#!/usr/bin/env python3
"""Fail CI if markdown notes under literature/permanent/harnesses miss required frontmatter."""
from __future__ import annotations
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REQUIRED = {"id", "title", "type", "status", "created", "updated"}
DIRS = ["literature", "permanent", "harnesses", "domains", "atlas", "inbox", "templates"]

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
    if errors:
        print("schema errors:")
        print("\n".join(errors))
        return 1
    print(f"ok: validated notes under {', '.join(DIRS)}")
    return 0

if __name__ == "__main__":
    sys.exit(main())
