#!/usr/bin/env python3
"""Snapshot clusters must resolve after agent-wave ingest."""
from __future__ import annotations

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from export_vault_snapshot import (  # noqa: E402
    AODL_THESIS_IDS,
    HARNESS_RADAR_IDS,
    LEARNING_IDS,
    LLM_FRONTIER_IDS,
    collect,
)


def main() -> int:
    data = collect()
    notes = {n["id"] for n in data["notes"]}
    problems: list[str] = []
    for name, ids in {
        "LEARNING_ACCELERATION": LEARNING_IDS,
        "LLM_FRONTIER": LLM_FRONTIER_IDS,
        "AODL_THESIS": AODL_THESIS_IDS,
        "HARNESS_RADAR": HARNESS_RADAR_IDS,
    }.items():
        pinned = data["clusters"].get(name) or []
        if list(ids) != list(pinned):
            problems.append(f"{name} snapshot mismatch")
        missing = [i for i in ids if i not in notes]
        if missing:
            problems.append(f"{name} missing {missing}")
    report = {"ok": not problems, "notes": len(notes), "problems": problems}
    print(json.dumps(report))
    return 0 if report["ok"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
