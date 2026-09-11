"""Humanity's Vault — synaptic homeostasis for frontier-kb.

Notes are neurons. Wikilinks seed synapses. Human/agent usage spikes
potentiate (saturating Hebbian). Idle edges decay (SHY analog). Below
threshold, notes.status becomes 'pruned' — never DELETE.
"""
from __future__ import annotations

import argparse
import json
import os
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
HALF_LIFE_DAYS = 14.0
WEIGHT_CAP = 8.0
SEED_WEIGHT = 1.0
PRUNE_WEIGHT = 0.08
PRUNE_IDLE_DAYS = 21.0
INBOX_IDLE_DAYS = 7.0
PRUNE_MAX_FIRES = 2
RETRIEVAL_INTERVALS = (1, 3, 7, 14, 30)
PROTECTED_TYPES = frozenset({"moc"})
LEARNING_IDS = (
    "domain-learning-acceleration",
    "domain-neuroscience",
    "lit-20260911-justin-sung-higher-order-encoding",
    "lit-20260911-huberman-plasticity-alert-rest",
    "lit-20260911-bryan-johnson-measure-dont-guess",
    "lit-20260911-rhonda-patrick-bdnf-exercise",
    "lit-20260911-synaptic-pruning-as-kb-policy",
    "lit-20260911-synaptic-homeostasis-sleep-shy",
    "lit-20260911-llm-frontier-teaching-surface",
    "perm-20260911-encoding-beats-exposure",
    "perm-20260911-plasticity-needs-alert-then-rest",
    "perm-20260911-measure-the-learning-loop",
    "perm-20260911-bdnf-is-a-learning-prerequisite",
    "perm-20260911-kb-is-a-brain-prune-and-potentiate",
    "perm-20260911-human-agent-synergy-is-the-loop",
    "perm-20260911-distill-then-retrieve-llm-frontier",
)
LLM_FRONTIER_IDS = (
    "perm-20260911-distill-then-retrieve-llm-frontier",
    "lit-20260911-llm-frontier-teaching-surface",
    "perm-20260910-swe-2-is-a-posttrained-model",
    "perm-20260910-scaffold-tool-shape-dominates",
    "perm-20260910-small-models-are-workers-or-specialists",
    "perm-20260910-postgres-is-the-operational-kb",
    "perm-20260910-no-universal-harness-plugin",
    "lit-20260910-context-triad",
)


def utcnow() -> datetime:
    return datetime.now(timezone.utc)


def decay_weight(weight: float, days_idle: float, half_life: float = HALF_LIFE_DAYS) -> float:
    if days_idle <= 0 or weight <= 0:
        return max(0.0, weight)
    return weight * (0.5 ** (days_idle / half_life))


def hebbian_strengthen(weight: float, amount: float = 0.18, cap: float = WEIGHT_CAP) -> float:
    return min(cap, weight + amount * (1.0 - (weight / cap)))


def retrieval_due(last_fired: datetime | None, now: datetime, fires: int) -> bool:
    if last_fired is None:
        return True
    idx = min(max(fires, 0), len(RETRIEVAL_INTERVALS) - 1)
    idle = (now - last_fired).total_seconds() / 86400.0
    return idle >= RETRIEVAL_INTERVALS[idx]


def should_prune(
    *,
    note_type: str,
    status: str,
    weight: float,
    days_idle: float,
    fires: int,
) -> bool:
    if status in {"pruned", "archived"}:
        return False
    if note_type in PROTECTED_TYPES:
        return False
    if note_type == "permanent" and (fires >= 3 or weight >= 0.5):
        return False
    idle_limit = INBOX_IDLE_DAYS if note_type == "inbox" else PRUNE_IDLE_DAYS
    return days_idle >= idle_limit and weight < PRUNE_WEIGHT and fires < PRUNE_MAX_FIRES


def _connect():
    sys.path.insert(0, str(Path(__file__).resolve().parent))
    from kb_store import apply_schema, connect  # noqa: WPS433

    conn = connect()
    apply_schema(conn)
    return conn


def seed_synapses(conn, writer: str = "synapse-seed") -> dict:
    """Create synapses from wikilinks. Existing weights are left intact."""
    inserted = skipped = 0
    with conn.cursor() as cur:
        cur.execute("SELECT src, dst, rel FROM links")
        rows = list(cur.fetchall())
        for row in rows:
            src, dst, rel = row["src"], row["dst"], row["rel"]
            cur.execute(
                """
                INSERT INTO synapses (src, dst, rel, weight, fires, created_at, updated_at)
                VALUES (%s, %s, %s, %s, 0, now(), now())
                ON CONFLICT (src, dst, rel) DO NOTHING
                """,
                (src, dst, rel, SEED_WEIGHT),
            )
            if cur.rowcount:
                inserted += 1
            else:
                skipped += 1
        cur.execute(
            """
            INSERT INTO usage_events (note_id, actor, kind, op, detail)
            VALUES (NULL, %s, 'agent', 'seed', %s)
            """,
            (writer, f"inserted={inserted} skipped={skipped}"),
        )
    conn.commit()
    return {"ok": True, "inserted": inserted, "skipped": skipped, "links": len(rows)}


def _note_weight(cur, note_id: str) -> tuple[float, int, datetime | None]:
    cur.execute(
        """
        SELECT COALESCE(AVG(weight), 0) AS w,
               COALESCE(SUM(fires), 0) AS f,
               MAX(last_fired) AS last_fired
          FROM synapses
         WHERE src = %s OR dst = %s
        """,
        (note_id, note_id),
    )
    row = cur.fetchone()
    return float(row["w"] or 0), int(row["f"] or 0), row["last_fired"]


def fire(conn, note_id: str, actor: str, kind: str = "human", op: str = "fire") -> dict:
    now = utcnow()
    with conn.cursor() as cur:
        cur.execute("SELECT id, type, status FROM notes WHERE id = %s", (note_id,))
        note = cur.fetchone()
        if not note:
            return {"ok": False, "error": "not_found", "id": note_id}
        cur.execute(
            """
            UPDATE synapses
               SET weight = LEAST(%s, weight + 0.18 * (1.0 - weight / %s)),
                   fires = fires + 1,
                   last_fired = %s,
                   updated_at = now()
             WHERE src = %s OR dst = %s
            """,
            (WEIGHT_CAP, WEIGHT_CAP, now, note_id, note_id),
        )
        touched = cur.rowcount
        cur.execute(
            """
            INSERT INTO usage_events (note_id, actor, kind, op, detail)
            VALUES (%s, %s, %s, %s, %s)
            """,
            (note_id, actor, kind, op, f"touched={touched}"),
        )
        weight, fires, last_fired = _note_weight(cur, note_id)
    conn.commit()
    return {
        "ok": True,
        "id": note_id,
        "touched": touched,
        "weight": weight,
        "fires": fires,
        "lastFired": last_fired.isoformat() if last_fired else None,
    }


def retrieve(conn, note_id: str, recalled: bool, actor: str, kind: str = "human") -> dict:
    op = "retrieve_hit" if recalled else "retrieve_miss"
    result = fire(conn, note_id, actor, kind, op=op)
    if not recalled and result.get("ok"):
        with conn.cursor() as cur:
            cur.execute(
                """
                UPDATE synapses
                   SET weight = weight * 0.92, updated_at = now()
                 WHERE src = %s OR dst = %s
                """,
                (note_id, note_id),
            )
        conn.commit()
        result["recalled"] = False
    else:
        result["recalled"] = recalled
    return result


def strengthen(conn, src: str, dst: str, actor: str, kind: str = "human") -> dict:
    if src == dst:
        return {"ok": False, "error": "self_synapse"}
    with conn.cursor() as cur:
        cur.execute(
            """
            INSERT INTO synapses (src, dst, rel, weight, fires, last_fired, created_at, updated_at)
            VALUES (%s, %s, 'coactivation', 1.15, 1, now(), now(), now())
            ON CONFLICT (src, dst, rel) DO UPDATE
               SET weight = LEAST(%s, synapses.weight + 0.22 * (1.0 - synapses.weight / %s)),
                   fires = synapses.fires + 1,
                   last_fired = now(),
                   updated_at = now()
         RETURNING src, dst, rel, weight, fires, last_fired
            """,
            (src, dst, WEIGHT_CAP, WEIGHT_CAP),
        )
        row = cur.fetchone()
        cur.execute(
            """
            INSERT INTO usage_events (note_id, actor, kind, op, detail)
            VALUES (%s, %s, %s, 'strengthen', %s)
            """,
            (src, actor, kind, dst),
        )
    conn.commit()
    return {"ok": True, **{k: (v.isoformat() if hasattr(v, "isoformat") else v) for k, v in row.items()}}


def run_loop(conn, writer: str = "synapse-loop", apply_prune: bool = False) -> dict:
    """Nightly homeostasis: decay idle synapses, propose (or apply) prunes."""
    now = utcnow()
    decayed = 0
    proposals: list[dict] = []
    applied = 0
    with conn.cursor() as cur:
        cur.execute("SELECT src, dst, rel, weight, fires, last_fired, created_at FROM synapses")
        edges = list(cur.fetchall())
        for edge in edges:
            last = edge["last_fired"] or edge["created_at"]
            if last.tzinfo is None:
                last = last.replace(tzinfo=timezone.utc)
            idle = (now - last).total_seconds() / 86400.0
            new_w = decay_weight(float(edge["weight"]), idle)
            if abs(new_w - float(edge["weight"])) > 1e-9:
                cur.execute(
                    """
                    UPDATE synapses SET weight = %s, updated_at = now()
                     WHERE src = %s AND dst = %s AND rel = %s
                    """,
                    (new_w, edge["src"], edge["dst"], edge["rel"]),
                )
                decayed += 1

        cur.execute(
            """
            SELECT n.id, n.type, n.status, n.title,
                   COALESCE(AVG(s.weight), 0) AS weight,
                   COALESCE(SUM(s.fires), 0) AS fires,
                   MAX(s.last_fired) AS last_fired,
                   n.updated_at
              FROM notes n
              LEFT JOIN synapses s ON s.src = n.id OR s.dst = n.id
             WHERE n.status NOT IN ('pruned', 'archived')
          GROUP BY n.id, n.type, n.status, n.title, n.updated_at
            """
        )
        for note in cur.fetchall():
            last = note["last_fired"] or note["updated_at"]
            if last is None:
                idle = 999
            else:
                if last.tzinfo is None:
                    last = last.replace(tzinfo=timezone.utc)
                idle = (now - last).total_seconds() / 86400.0
            if should_prune(
                note_type=note["type"],
                status=note["status"],
                weight=float(note["weight"] or 0),
                days_idle=idle,
                fires=int(note["fires"] or 0),
            ):
                item = {
                    "id": note["id"],
                    "title": note["title"],
                    "type": note["type"],
                    "weight": float(note["weight"] or 0),
                    "idleDays": idle,
                    "fires": int(note["fires"] or 0),
                }
                proposals.append(item)
                if apply_prune:
                    cur.execute(
                        """
                        UPDATE notes SET status = 'pruned', updated_at = now(), version = version + 1
                         WHERE id = %s
                        """,
                        (note["id"],),
                    )
                    cur.execute(
                        """
                        INSERT INTO prune_log (note_id, reason, weight, idle_days, actor)
                        VALUES (%s, 'homeostasis', %s, %s, %s)
                        """,
                        (note["id"], item["weight"], idle, writer),
                    )
                    applied += 1

        cur.execute(
            """
            INSERT INTO usage_events (note_id, actor, kind, op, detail)
            VALUES (NULL, %s, 'agent', 'loop', %s)
            """,
            (writer, json.dumps({"decayed": decayed, "proposals": len(proposals), "applied": applied})),
        )
    conn.commit()
    return {
        "ok": True,
        "decayed": decayed,
        "proposals": proposals,
        "applied": applied,
        "apply": apply_prune,
        "at": now.isoformat(),
    }


def brain_snapshot(conn, node_limit: int = 80) -> dict:
    with conn.cursor() as cur:
        cur.execute("SELECT COUNT(*) AS n FROM notes WHERE status <> 'pruned'")
        neurons = int(cur.fetchone()["n"])
        cur.execute("SELECT COUNT(*) AS n, COALESCE(AVG(weight), 0) AS w FROM synapses")
        syn = cur.fetchone()
        cur.execute("SELECT COUNT(*) AS n FROM notes WHERE status = 'pruned'")
        pruned = int(cur.fetchone()["n"])
        cur.execute("SELECT MAX(at) AS last FROM usage_events WHERE op IN ('loop', 'seed')")
        last = cur.fetchone()["last"]
        cur.execute(
            """
            SELECT n.id, n.title, n.type, n.status,
                   COALESCE(AVG(s.weight), 0) AS weight,
                   MAX(s.last_fired) AS last_fired
              FROM notes n
              LEFT JOIN synapses s ON s.src = n.id OR s.dst = n.id
             WHERE n.status <> 'pruned'
          GROUP BY n.id, n.title, n.type, n.status
          ORDER BY weight DESC, n.updated_at DESC
             LIMIT %s
            """,
            (node_limit,),
        )
        nodes = list(cur.fetchall())
        ids = [n["id"] for n in nodes]
        edges = []
        if ids:
            cur.execute(
                """
                SELECT src, dst, rel, weight, fires, last_fired
                  FROM synapses
                 WHERE src = ANY(%s) AND dst = ANY(%s)
              ORDER BY weight DESC
                 LIMIT 400
                """,
                (ids, ids),
            )
            edges = list(cur.fetchall())
    return {
        "neurons": neurons,
        "synapses": int(syn["n"]),
        "meanWeight": float(syn["w"] or 0),
        "pruneCandidates": pruned,
        "lastLoopAt": last.isoformat() if last else None,
        "nodes": nodes,
        "edges": edges,
    }


def dump(obj):
    def conv(v):
        if hasattr(v, "isoformat"):
            return v.isoformat()
        if isinstance(v, dict):
            return {k: conv(x) for k, x in v.items()}
        if isinstance(v, list):
            return [conv(x) for x in v]
        return v

    print(json.dumps(conv(obj), default=str))


def main() -> int:
    parser = argparse.ArgumentParser(description="frontier-kb synaptic loop")
    sub = parser.add_subparsers(dest="cmd", required=True)
    sub.add_parser("seed")
    loop_p = sub.add_parser("loop")
    loop_p.add_argument("--apply", action="store_true", help="apply prunes (default: dry-run)")
    fire_p = sub.add_parser("fire")
    fire_p.add_argument("--id", required=True)
    fire_p.add_argument("--actor", default=os.environ.get("KB_WRITER", "cli"))
    fire_p.add_argument("--kind", default="human", choices=("human", "agent"))
    ret_p = sub.add_parser("retrieve")
    ret_p.add_argument("--id", required=True)
    ret_p.add_argument("--recalled", action="store_true")
    ret_p.add_argument("--actor", default=os.environ.get("KB_WRITER", "cli"))
    str_p = sub.add_parser("strengthen")
    str_p.add_argument("--src", required=True)
    str_p.add_argument("--dst", required=True)
    str_p.add_argument("--actor", default=os.environ.get("KB_WRITER", "cli"))
    sub.add_parser("snapshot")
    args = parser.parse_args()
    writer = os.environ.get("KB_WRITER", "synapse-loop")

    try:
        conn = _connect()
    except Exception as exc:  # noqa: BLE001
        dump({"ok": False, "error": "connect", "detail": str(exc)})
        return 2

    try:
        if args.cmd == "seed":
            dump(seed_synapses(conn, writer))
        elif args.cmd == "loop":
            dump(run_loop(conn, writer, apply_prune=args.apply))
        elif args.cmd == "fire":
            dump(fire(conn, args.id, args.actor, args.kind))
        elif args.cmd == "retrieve":
            dump(retrieve(conn, args.id, args.recalled, args.actor))
        elif args.cmd == "strengthen":
            dump(strengthen(conn, args.src, args.dst, args.actor))
        elif args.cmd == "snapshot":
            dump(brain_snapshot(conn))
        return 0
    finally:
        conn.close()


if __name__ == "__main__":
    raise SystemExit(main())
