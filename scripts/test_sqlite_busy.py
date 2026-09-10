#!/usr/bin/env python3
"""Show why the original SQLite funnel cannot take 100 concurrent writers."""
from __future__ import annotations

import sqlite3
import tempfile
import threading
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path


def main() -> int:
    tmp = Path(tempfile.mkdtemp()) / "funnel.db"
    con = sqlite3.connect(tmp)
    con.execute("PRAGMA journal_mode=WAL")
    con.execute("CREATE TABLE notes (id TEXT PRIMARY KEY, body TEXT)")
    con.commit()
    con.close()

    busy = 0
    ok = 0
    lock = threading.Lock()
    elapsed: list[float] = []

    def write(i: int) -> None:
        nonlocal busy, ok
        c = sqlite3.connect(tmp, timeout=0.05)
        c.execute("PRAGMA journal_mode=WAL")
        t0 = time.perf_counter()
        try:
            c.execute("INSERT INTO notes (id, body) VALUES (?, ?)", (f"n-{i}", f"body {i}"))
            c.commit()
            with lock:
                ok += 1
        except sqlite3.OperationalError as exc:
            if "locked" in str(exc).lower() or "busy" in str(exc).lower():
                with lock:
                    busy += 1
            else:
                raise
        finally:
            elapsed.append(time.perf_counter() - t0)
            c.close()

    with ThreadPoolExecutor(max_workers=100) as pool:
        futs = [pool.submit(write, i) for i in range(100)]
        for fut in as_completed(futs):
            fut.result()

    print(f"sqlite WAL 100 writers timeout=0.05s: ok={ok} busy={busy}")
    print("diagnosis: SQLite serializes writers; 100 agents need Postgres MVCC, not a node-local funnel.")
    return 0 if (ok + busy) == 100 else 1


if __name__ == "__main__":
    raise SystemExit(main())
