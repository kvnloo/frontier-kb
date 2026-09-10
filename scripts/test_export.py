#!/usr/bin/env python3
"""Export projection: ingested vault notes roundtrip to a dest dir."""
from __future__ import annotations

import json
import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from kb_store import NOTE_DIRS, REQUIRED, ROOT, apply_schema, connect, export, ingest, parse_frontmatter  # noqa: E402

KNOWN = (
    "perm-20260910-git-vault-fails-at-100-writers",
    "perm-20260910-postgres-is-the-operational-kb",
    "lit-20260910-agent-kb-concurrency",
    "atlas-home",
)


def source_ids() -> set[str]:
    ids: set[str] = set()
    for folder in NOTE_DIRS:
        base = ROOT / folder
        if not base.exists():
            continue
        for path in base.rglob("*.md"):
            meta, _ = parse_frontmatter(path.read_text(encoding="utf-8"))
            if not (REQUIRED - set(meta)):
                ids.add(meta["id"])
    return ids


def main() -> int:
    dest = Path(tempfile.mkdtemp()) / "export"
    dest.mkdir()
    conn = connect()
    try:
        apply_schema(conn)
        ingested = ingest(conn, "export-test")
        result = export(conn, dest)
    finally:
        conn.close()

    errors: list[str] = []
    found: set[str] = set()
    for folder in NOTE_DIRS:
        folder_path = dest / folder
        if not folder_path.exists():
            continue
        for path in folder_path.rglob("*.md"):
            meta, _ = parse_frontmatter(path.read_text(encoding="utf-8"))
            missing = REQUIRED - set(meta)
            if missing:
                errors.append(f"{path.relative_to(dest)}: missing {sorted(missing)}")
            if meta.get("id"):
                found.add(meta["id"])
    src = source_ids()
    for kid in KNOWN:
        if kid not in found:
            errors.append(f"missing known id {kid}")
    missing = sorted(src - found)
    extra = sorted(found - src)
    if missing:
        errors.append(f"export missing {missing[:10]}")
    if extra:
        errors.append(f"export extra {extra[:10]}")
    report = {
        "ok": not errors,
        "written": result.get("written"),
        "unchanged": result.get("unchanged"),
        "skipped": result.get("skipped"),
        "exported": len(found),
        "source": len(src),
        "ingested": ingested,
        "errors": errors[:20],
    }
    print(json.dumps(report))
    return 0 if report["ok"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
