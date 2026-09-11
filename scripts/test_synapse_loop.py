#!/usr/bin/env python3
"""Unit tests for synaptic homeostasis (no Postgres required)."""
from __future__ import annotations

import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from synapse_loop import (  # noqa: E402
    decay_weight,
    hebbian_strengthen,
    retrieval_due,
    should_prune,
)


def approx(a: float, b: float, eps: float = 1e-9) -> bool:
    return abs(a - b) < eps


def main() -> int:
    errors: list[str] = []

    if not approx(decay_weight(1.0, 0), 1.0):
        errors.append("idle 0 should not decay")
    half = decay_weight(2.0, 14)
    if not approx(half, 1.0, 1e-6):
        errors.append(f"half-life 14d expected 1.0 got {half}")

    up = hebbian_strengthen(1.0)
    if not (up > 1.0 and up < 8.0):
        errors.append(f"hebbian should raise 1.0, got {up}")
    capped = hebbian_strengthen(8.0)
    if capped != 8.0:
        errors.append(f"cap failed {capped}")

    now = datetime(2026, 9, 11, tzinfo=timezone.utc)
    if not retrieval_due(None, now, 0):
        errors.append("never-fired should be due")
    if retrieval_due(now, now, 0):
        errors.append("just-fired should not be due")
    yesterday = now - timedelta(days=2)
    if not retrieval_due(yesterday, now, 0):
        errors.append("interval 1d should be due after 2d")

    if not should_prune(note_type="inbox", status="draft", weight=0.01, days_idle=8, fires=0):
        errors.append("stale inbox should prune")
    if should_prune(note_type="moc", status="active", weight=0.01, days_idle=90, fires=0):
        errors.append("moc must be protected")
    if should_prune(note_type="permanent", status="active", weight=0.9, days_idle=90, fires=5):
        errors.append("hot permanent should not prune")
    if should_prune(note_type="inbox", status="pruned", weight=0.01, days_idle=90, fires=0):
        errors.append("already pruned should skip")

    if errors:
        print("FAIL")
        print("\n".join(errors))
        return 1
    print("ok: synapse math")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
