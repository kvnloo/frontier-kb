#!/usr/bin/env python3
"""100 unique inserts succeed; 100 CAS updates of one id yield 1 winner, version=2."""
from __future__ import annotations

import json
import sys
import time
import uuid
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone
from pathlib import Path

import psycopg

sys.path.insert(0, str(Path(__file__).resolve().parent))

from kb_store import apply_schema, connect, put_cas  # noqa: E402

N = 100
SHARED = "cas-shared"


def _now():
    return datetime.now(timezone.utc)


def _put(note_id: str, body: str, expected_version: int | None, writer: str) -> dict:
    conn = connect()
    try:
        return put_cas(
            conn,
            note_id=note_id,
            path=f"inbox/{note_id}.md",
            title=note_id,
            type_="inbox",
            status="draft",
            body=body,
            frontmatter={"id": note_id},
            writer=writer,
            created=_now(),
            expected_version=expected_version,
        )
    finally:
        conn.close()


def unique_insert(_: int) -> dict:
    nid = f"smokeu-{uuid.uuid4()}"
    return _put(nid, f"unique {nid}", None, "smoke-insert")


def cas_update(i: int) -> dict:
    return _put(SHARED, f"cas writer {i}", 1, f"smoke-cas-{i}")


def _reset(conn) -> None:
    stmts = (
        "DELETE FROM links WHERE src LIKE %s OR src LIKE %s OR src = %s",
        "DELETE FROM events WHERE note_id LIKE %s OR note_id LIKE %s OR note_id = %s",
        "DELETE FROM notes WHERE id LIKE %s OR id LIKE %s OR id = %s",
    )
    args = ("smokeu-%", "unique-%", SHARED)
    for _ in range(12):
        try:
            for sql in stmts:
                conn.execute(sql, args)
            conn.commit()
            return
        except psycopg.errors.DeadlockDetected:
            conn.rollback()
            time.sleep(0.2)
    raise RuntimeError("could not reset smoke rows")


def main() -> int:
    conn = connect()
    try:
        apply_schema(conn)
        _reset(conn)
    finally:
        conn.close()

    seed = _put(SHARED, "seed", None, "smoke-seed")
    if not seed.get("ok"):
        print(json.dumps({"ok": False, "error": "seed", "seed": seed}))
        return 1

    insert_ok = 0
    with ThreadPoolExecutor(max_workers=32) as pool:
        futs = [pool.submit(unique_insert, i) for i in range(N)]
        for fut in as_completed(futs):
            if fut.result().get("ok"):
                insert_ok += 1

    cas_ok = 0
    cas_conflict = 0
    with ThreadPoolExecutor(max_workers=32) as pool:
        futs = [pool.submit(cas_update, i) for i in range(N)]
        for fut in as_completed(futs):
            result = fut.result()
            if result.get("ok"):
                cas_ok += 1
            elif result.get("error") == "cas_conflict":
                cas_conflict += 1

    conn = connect()
    try:
        shared = conn.execute(
            "SELECT id, version FROM notes WHERE id = %s", (SHARED,)
        ).fetchone()
        n_notes = conn.execute("SELECT count(*) AS n FROM notes").fetchone()["n"]
        n_events = conn.execute("SELECT count(*) AS n FROM events").fetchone()["n"]
    finally:
        conn.close()

    report = {
        "ok": insert_ok == N
        and cas_ok == 1
        and cas_conflict == N - 1
        and shared["version"] == 2,
        "insert_ok": insert_ok,
        "cas_ok": cas_ok,
        "cas_conflict": cas_conflict,
        "shared_version": shared["version"] if shared else None,
        "notes": n_notes,
        "events": n_events,
    }
    print(json.dumps(report))
    return 0 if report["ok"] else 1


if __name__ == "__main__":
    sys.exit(main())
