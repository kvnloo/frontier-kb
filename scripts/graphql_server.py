#!/usr/bin/env python3
"""GraphQL brain API for humanity-vault. Stdlib HTTP + graphql-core."""
from __future__ import annotations

import json
import os
import sys
from datetime import datetime, timezone
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import parse_qs, urlparse

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(Path(__file__).resolve().parent))

from graphql import graphql_sync  # noqa: E402
from graphql.type import (  # noqa: E402
    GraphQLArgument,
    GraphQLBoolean,
    GraphQLEnumType,
    GraphQLField,
    GraphQLFloat,
    GraphQLID,
    GraphQLInt,
    GraphQLList,
    GraphQLNonNull,
    GraphQLObjectType,
    GraphQLSchema,
    GraphQLString,
)

from kb_store import apply_schema, connect, get_note, search_notes  # noqa: E402
from synapse_loop import (  # noqa: E402
    AODL_THESIS_IDS,
    HARNESS_RADAR_IDS,
    LEARNING_IDS,
    LLM_FRONTIER_IDS,
    RETRIEVAL_INTERVALS,
    brain_snapshot,
    fire as fire_note,
    retrieval_due,
    run_loop,
    seed_synapses,
    strengthen as strengthen_edge,
    utcnow,
)

PROTOCOL = [
    {
        "id": "move",
        "source": "patrick",
        "title": "Move",
        "why": "BDNF and metabolic state are prerequisites, not extras.",
        "durationMinutes": 12,
    },
    {
        "id": "alert",
        "source": "huberman",
        "title": "Alert",
        "why": "Plasticity needs a tagged, focused bout — not background tabs.",
        "durationMinutes": 3,
    },
    {
        "id": "encode",
        "source": "sung",
        "title": "Encode",
        "why": "Group, compare, distill. Do not highlight the vault.",
        "durationMinutes": 25,
    },
    {
        "id": "retrieve",
        "source": "sung",
        "title": "Retrieve",
        "why": "Regenerate the claim without the page. Familiarity is a trap.",
        "durationMinutes": 12,
    },
    {
        "id": "rest",
        "source": "huberman",
        "title": "Rest (NSDR)",
        "why": "Consolidation happens after the bout. Gate the next encode.",
        "durationMinutes": 10,
    },
    {
        "id": "measure",
        "source": "johnson",
        "title": "Measure",
        "why": "Hit-rate, synapse weight, idle-days. Effort is not a biomarker.",
        "durationMinutes": 4,
    },
    {
        "id": "prune",
        "source": "johnson",
        "title": "Prune",
        "why": "Unused edges are noise. Review candidates; never silent-delete.",
        "durationMinutes": 6,
    },
]


def _iso(value):
    if value is None:
        return None
    if hasattr(value, "isoformat"):
        return value.isoformat()
    return str(value)


def _distill(body: str) -> str:
    if not body:
        return ""
    for heading in ("## Idea (atomic)", "## Claim (one sentence)", "## Idea"):
        if heading in body:
            chunk = body.split(heading, 1)[1]
            chunk = chunk.split("##", 1)[0].strip()
            return " ".join(chunk.split())
    for line in body.splitlines():
        line = line.strip()
        if line and not line.startswith("#") and not line.startswith("-"):
            return line
    return ""


def _tags(frontmatter) -> list[str]:
    raw = (frontmatter or {}).get("tags") or "[]"
    if isinstance(raw, list):
        return [str(x).strip() for x in raw]
    text = str(raw).strip().strip("[]")
    if not text:
        return []
    return [p.strip().strip("'\"") for p in text.split(",") if p.strip()]


def _domains(frontmatter) -> list[str]:
    raw = (frontmatter or {}).get("domains") or "[]"
    if isinstance(raw, list):
        return [str(x).strip() for x in raw]
    text = str(raw).strip().strip("[]")
    if not text:
        return []
    return [p.strip().strip("'\"") for p in text.split(",") if p.strip()]


def _hydrate(conn, row: dict) -> dict:
    with conn.cursor() as cur:
        cur.execute(
            """
            SELECT COALESCE(AVG(weight), 0) AS weight,
                   COALESCE(SUM(fires), 0) AS fires,
                   MAX(last_fired) AS last_fired
              FROM synapses
             WHERE src = %s OR dst = %s
            """,
            (row["id"], row["id"]),
        )
        syn = cur.fetchone()
    last = syn["last_fired"]
    fires = int(syn["fires"] or 0)
    fm = row.get("frontmatter") or {}
    return {
        "id": row["id"],
        "path": row.get("path"),
        "title": row["title"],
        "type": row.get("type") or "note",
        "status": row.get("status") or "draft",
        "body": row.get("body") or "",
        "distilled": _distill(row.get("body") or ""),
        "tags": _tags(fm),
        "domains": _domains(fm),
        "created": _iso(row.get("created_at") or row.get("created")),
        "updated": _iso(row.get("updated_at") or row.get("updated")),
        "weight": float(syn["weight"] or 0),
        "lastFired": _iso(last),
        "retrievalDue": retrieval_due(last, utcnow(), fires),
        "_fires": fires,
    }


def _synapses(conn, note_id: str, limit: int) -> list[dict]:
    with conn.cursor() as cur:
        cur.execute(
            """
            SELECT src, dst, rel, weight, fires, last_fired
              FROM synapses
             WHERE src = %s OR dst = %s
          ORDER BY weight DESC
             LIMIT %s
            """,
            (note_id, note_id, limit),
        )
        return [
            {
                "src": r["src"],
                "dst": r["dst"],
                "rel": r["rel"],
                "weight": float(r["weight"]),
                "fires": int(r["fires"]),
                "lastFired": _iso(r["last_fired"]),
            }
            for r in cur.fetchall()
        ]


def _load_note(conn, note_id: str) -> dict | None:
    row = get_note(conn, note_id)
    if not row:
        return None
    return _hydrate(conn, row)


CYCLE_PHASES = ("MOVE", "ALERT", "ENCODE", "RETRIEVE", "INTERLEAVE", "REST", "SLEEP", "MEASURE", "PRUNE")


def _cycle(conn, phase: str | None = None) -> dict:
    if phase is None:
        with conn.cursor() as cur:
            cur.execute("SELECT phase FROM cycles ORDER BY id DESC LIMIT 1")
            row = cur.fetchone()
        phase = (row["phase"] if row else "ENCODE").upper()
    if phase not in CYCLE_PHASES:
        phase = "ENCODE"
    return {
        "phase": phase,
        "ultradianMinutes": 90,
        "nextRestInMinutes": 20 if phase in {"ENCODE", "RETRIEVE", "INTERLEAVE"} else 0,
        "protocol": PROTOCOL,
    }


def build_schema(conn) -> GraphQLSchema:
    note_type_enum = GraphQLEnumType("NoteType", {k: k for k in ("literature", "permanent", "harness", "moc", "inbox", "note")})
    status_enum = GraphQLEnumType("NoteStatus", {k: k for k in ("draft", "active", "pruned", "archived")})
    actor_enum = GraphQLEnumType("ActorKind", {"human": "human", "agent": "agent"})
    phase_enum = GraphQLEnumType("CyclePhase", {k: k for k in CYCLE_PHASES})
    cluster_enum = GraphQLEnumType(
        "ClusterId",
        {
            "LEARNING_ACCELERATION": "LEARNING_ACCELERATION",
            "LLM_FRONTIER": "LLM_FRONTIER",
            "HARNESS_RADAR": "HARNESS_RADAR",
            "AODL_THESIS": "AODL_THESIS",
        },
    )

    synapse_type = GraphQLObjectType(
        "Synapse",
        lambda: {
            "src": GraphQLField(GraphQLNonNull(GraphQLID)),
            "dst": GraphQLField(GraphQLNonNull(GraphQLID)),
            "rel": GraphQLField(GraphQLNonNull(GraphQLString)),
            "weight": GraphQLField(GraphQLNonNull(GraphQLFloat)),
            "fires": GraphQLField(GraphQLNonNull(GraphQLInt)),
            "lastFired": GraphQLField(GraphQLString),
        },
    )

    protocol_type = GraphQLObjectType(
        "ProtocolStep",
        {
            "id": GraphQLField(GraphQLNonNull(GraphQLID)),
            "source": GraphQLField(GraphQLNonNull(GraphQLString)),
            "title": GraphQLField(GraphQLNonNull(GraphQLString)),
            "why": GraphQLField(GraphQLNonNull(GraphQLString)),
            "durationMinutes": GraphQLField(GraphQLInt),
        },
    )

    cycle_type = GraphQLObjectType(
        "LearningCycle",
        {
            "phase": GraphQLField(GraphQLNonNull(phase_enum)),
            "ultradianMinutes": GraphQLField(GraphQLNonNull(GraphQLInt)),
            "nextRestInMinutes": GraphQLField(GraphQLInt),
            "protocol": GraphQLField(GraphQLNonNull(GraphQLList(GraphQLNonNull(protocol_type)))),
        },
    )

    def synapses_resolver(note, info, limit=12):
        return _synapses(conn, note["id"], limit)

    note_type = GraphQLObjectType(
        "Note",
        lambda: {
            "id": GraphQLField(GraphQLNonNull(GraphQLID)),
            "path": GraphQLField(GraphQLString),
            "title": GraphQLField(GraphQLNonNull(GraphQLString)),
            "type": GraphQLField(GraphQLNonNull(note_type_enum), resolve=lambda n, _i: n.get("type") or "note"),
            "status": GraphQLField(GraphQLNonNull(status_enum), resolve=lambda n, _i: n.get("status") or "draft"),
            "body": GraphQLField(GraphQLString),
            "distilled": GraphQLField(GraphQLString),
            "tags": GraphQLField(GraphQLNonNull(GraphQLList(GraphQLNonNull(GraphQLString)))),
            "domains": GraphQLField(GraphQLNonNull(GraphQLList(GraphQLNonNull(GraphQLString)))),
            "created": GraphQLField(GraphQLString),
            "updated": GraphQLField(GraphQLString),
            "weight": GraphQLField(GraphQLNonNull(GraphQLFloat)),
            "lastFired": GraphQLField(GraphQLString),
            "retrievalDue": GraphQLField(GraphQLNonNull(GraphQLBoolean)),
            "synapses": GraphQLField(
                GraphQLNonNull(GraphQLList(GraphQLNonNull(synapse_type))),
                args={"limit": GraphQLArgument(GraphQLInt, default_value=12)},
                resolve=synapses_resolver,
            ),
        },
    )

    cluster_type = GraphQLObjectType(
        "Cluster",
        {
            "id": GraphQLField(GraphQLNonNull(cluster_enum)),
            "title": GraphQLField(GraphQLNonNull(GraphQLString)),
            "notes": GraphQLField(GraphQLNonNull(GraphQLList(GraphQLNonNull(note_type)))),
        },
    )

    brain_type = GraphQLObjectType(
        "BrainSnapshot",
        {
            "neurons": GraphQLField(GraphQLNonNull(GraphQLInt)),
            "synapses": GraphQLField(GraphQLNonNull(GraphQLInt)),
            "meanWeight": GraphQLField(GraphQLNonNull(GraphQLFloat)),
            "pruneCandidates": GraphQLField(GraphQLNonNull(GraphQLInt)),
            "lastLoopAt": GraphQLField(GraphQLString),
            "nodes": GraphQLField(GraphQLNonNull(GraphQLList(GraphQLNonNull(note_type)))),
            "edges": GraphQLField(GraphQLNonNull(GraphQLList(GraphQLNonNull(synapse_type)))),
        },
    )

    def resolve_note(_root, _info, id):  # noqa: A002
        return _load_note(conn, id)

    def resolve_search(_root, _info, q, limit=20):
        rows = search_notes(conn, q, limit)
        out = []
        for row in rows:
            full = get_note(conn, row["id"])
            if full:
                out.append(_hydrate(conn, full))
        return out

    def resolve_cluster(_root, _info, id):  # noqa: A002
        titles = {
            "LEARNING_ACCELERATION": "Human learning acceleration",
            "LLM_FRONTIER": "LLM frontier teaching track",
            "HARNESS_RADAR": "Harness radar",
            "AODL_THESIS": "AODL contract",
        }
        ids = {
            "LEARNING_ACCELERATION": LEARNING_IDS,
            "LLM_FRONTIER": LLM_FRONTIER_IDS,
            "HARNESS_RADAR": HARNESS_RADAR_IDS,
            "AODL_THESIS": AODL_THESIS_IDS,
        }[id]
        notes = []
        for nid in ids:
            note = _load_note(conn, nid)
            if note:
                notes.append(note)
        return {"id": id, "title": titles[id], "notes": notes}

    def resolve_brain(_root, _info):
        snap = brain_snapshot(conn)
        nodes = []
        for n in snap["nodes"]:
            full = _load_note(conn, n["id"])
            if full:
                nodes.append(full)
        edges = [
            {
                "src": e["src"],
                "dst": e["dst"],
                "rel": e["rel"],
                "weight": float(e["weight"]),
                "fires": int(e["fires"]),
                "lastFired": _iso(e["last_fired"]),
            }
            for e in snap["edges"]
        ]
        return {**snap, "nodes": nodes, "edges": edges}

    def resolve_due(_root, _info, limit=8):
        with conn.cursor() as cur:
            cur.execute(
                """
                SELECT n.id, MAX(s.last_fired) AS last_fired, COALESCE(SUM(s.fires), 0) AS fires
                  FROM notes n
                  LEFT JOIN synapses s ON s.src = n.id OR s.dst = n.id
                 WHERE n.type = 'permanent' AND n.status NOT IN ('pruned', 'archived')
              GROUP BY n.id
              ORDER BY n.updated_at DESC
                 LIMIT 40
                """
            )
            rows = list(cur.fetchall())
        now = utcnow()
        due = []
        for row in rows:
            if retrieval_due(row["last_fired"], now, int(row["fires"] or 0)):
                note = _load_note(conn, row["id"])
                if note:
                    due.append(note)
            if len(due) >= limit:
                break
        return due

    def resolve_prune(_root, _info, limit=20):
        report = run_loop(conn, writer="graphql", apply_prune=False)
        notes = []
        for item in report["proposals"][:limit]:
            note = _load_note(conn, item["id"])
            if note:
                notes.append(note)
        return notes

    def resolve_llm(_root, _info):
        notes = []
        for nid in LLM_FRONTIER_IDS:
            note = _load_note(conn, nid)
            if note:
                notes.append(note)
        return notes

    def mut_fire(_root, _info, noteId, actor, kind="human"):
        fire_note(conn, noteId, actor, kind)
        return _load_note(conn, noteId)

    def mut_retrieve(_root, _info, noteId, recalled, actor):
        from synapse_loop import retrieve as retrieve_note

        retrieve_note(conn, noteId, recalled, actor)
        return _load_note(conn, noteId)

    def mut_prune(_root, _info, noteId, actor):
        with conn.cursor() as cur:
            cur.execute(
                """
                UPDATE notes SET status = 'pruned', updated_at = now(), version = version + 1
                 WHERE id = %s
             RETURNING id
                """,
                (noteId,),
            )
            if cur.fetchone():
                cur.execute(
                    """
                    INSERT INTO prune_log (note_id, reason, weight, idle_days, actor)
                    VALUES (%s, 'human-review', 0, 0, %s)
                    """,
                    (noteId, actor),
                )
                cur.execute(
                    """
                    INSERT INTO usage_events (note_id, actor, kind, op, detail)
                    VALUES (%s, %s, 'human', 'prune', 'graphql')
                    """,
                    (noteId, actor),
                )
        conn.commit()
        return _load_note(conn, noteId)

    def mut_strengthen(_root, _info, src, dst, actor):
        return strengthen_edge(conn, src, dst, actor)

    def mut_cycle(_root, _info, phase, actor=None):
        with conn.cursor() as cur:
            cur.execute("INSERT INTO cycles (phase, actor) VALUES (%s, %s)", (phase, actor or "human"))
        conn.commit()
        return _cycle(conn, phase)

    query = GraphQLObjectType(
        "Query",
        {
            "note": GraphQLField(note_type, args={"id": GraphQLArgument(GraphQLNonNull(GraphQLID))}, resolve=resolve_note),
            "search": GraphQLField(
                GraphQLNonNull(GraphQLList(GraphQLNonNull(note_type))),
                args={"q": GraphQLArgument(GraphQLNonNull(GraphQLString)), "limit": GraphQLArgument(GraphQLInt, default_value=20)},
                resolve=resolve_search,
            ),
            "cluster": GraphQLField(
                cluster_type,
                args={"id": GraphQLArgument(GraphQLNonNull(cluster_enum))},
                resolve=resolve_cluster,
            ),
            "brain": GraphQLField(GraphQLNonNull(brain_type), resolve=resolve_brain),
            "dueRetrievals": GraphQLField(
                GraphQLNonNull(GraphQLList(GraphQLNonNull(note_type))),
                args={"limit": GraphQLArgument(GraphQLInt, default_value=8)},
                resolve=resolve_due,
            ),
            "pruneCandidates": GraphQLField(
                GraphQLNonNull(GraphQLList(GraphQLNonNull(note_type))),
                args={"limit": GraphQLArgument(GraphQLInt, default_value=20)},
                resolve=resolve_prune,
            ),
            "cycle": GraphQLField(GraphQLNonNull(cycle_type), resolve=lambda *_: _cycle(conn)),
            "llmFrontier": GraphQLField(GraphQLNonNull(GraphQLList(GraphQLNonNull(note_type))), resolve=resolve_llm),
        },
    )

    mutation = GraphQLObjectType(
        "Mutation",
        {
            "fire": GraphQLField(
                note_type,
                args={
                    "noteId": GraphQLArgument(GraphQLNonNull(GraphQLID)),
                    "actor": GraphQLArgument(GraphQLNonNull(GraphQLString)),
                    "kind": GraphQLArgument(actor_enum, default_value="human"),
                },
                resolve=mut_fire,
            ),
            "retrieve": GraphQLField(
                note_type,
                args={
                    "noteId": GraphQLArgument(GraphQLNonNull(GraphQLID)),
                    "recalled": GraphQLArgument(GraphQLNonNull(GraphQLBoolean)),
                    "actor": GraphQLArgument(GraphQLNonNull(GraphQLString)),
                },
                resolve=mut_retrieve,
            ),
            "prune": GraphQLField(
                note_type,
                args={
                    "noteId": GraphQLArgument(GraphQLNonNull(GraphQLID)),
                    "actor": GraphQLArgument(GraphQLNonNull(GraphQLString)),
                },
                resolve=mut_prune,
            ),
            "strengthen": GraphQLField(
                synapse_type,
                args={
                    "src": GraphQLArgument(GraphQLNonNull(GraphQLID)),
                    "dst": GraphQLArgument(GraphQLNonNull(GraphQLID)),
                    "actor": GraphQLArgument(GraphQLNonNull(GraphQLString)),
                },
                resolve=mut_strengthen,
            ),
            "startCycle": GraphQLField(
                GraphQLNonNull(cycle_type),
                args={
                    "phase": GraphQLArgument(GraphQLNonNull(phase_enum)),
                    "actor": GraphQLArgument(GraphQLString),
                },
                resolve=mut_cycle,
            ),
        },
    )

    return GraphQLSchema(query=query, mutation=mutation)


def execute(conn, query: str, variables=None):
    schema = build_schema(conn)
    result = graphql_sync(schema, query, variable_values=variables or {})
    payload = {"data": result.data}
    if result.errors:
        payload["errors"] = [{"message": str(e)} for e in result.errors]
    return payload


class Handler(BaseHTTPRequestHandler):
    conn = None
    seeded = False

    def log_message(self, fmt, *args):  # noqa: A003
        sys.stderr.write("%s - %s\n" % (self.address_string(), fmt % args))

    def _send(self, code: int, payload):
        body = json.dumps(payload).encode("utf-8")
        self.send_response(code)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Headers", "content-type")
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        self.wfile.write(body)

    def do_OPTIONS(self):  # noqa: N802
        self.send_response(204)
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Headers", "content-type")
        self.send_header("Access-Control-Allow-Methods", "GET,POST,OPTIONS")
        self.end_headers()

    def do_GET(self):  # noqa: N802
        parsed = urlparse(self.path)
        if parsed.path in ("/health", "/"):
            self._send(200, {"ok": True, "service": "humanity-vault-graphql"})
            return
        if parsed.path != "/graphql":
            self._send(404, {"ok": False, "error": "not_found"})
            return
        qs = parse_qs(parsed.query)
        query = (qs.get("query") or [""])[0]
        self._run(query, None)

    def do_POST(self):  # noqa: N802
        length = int(self.headers.get("Content-Length") or "0")
        raw = self.rfile.read(length) if length else b"{}"
        try:
            payload = json.loads(raw.decode("utf-8") or "{}")
        except json.JSONDecodeError:
            self._send(400, {"errors": [{"message": "invalid json"}]})
            return
        self._run(payload.get("query") or "", payload.get("variables"))

    def _run(self, query: str, variables):
        if not query:
            self._send(400, {"errors": [{"message": "missing query"}]})
            return
        if not Handler.seeded:
            seed_synapses(self.conn, "graphql-boot")
            Handler.seeded = True
        self._send(200, execute(self.conn, query, variables))


def main() -> int:
    host = os.environ.get("GRAPHQL_HOST", "127.0.0.1")
    port = int(os.environ.get("GRAPHQL_PORT", "8787"))
    conn = connect()
    apply_schema(conn)
    Handler.conn = conn
    server = ThreadingHTTPServer((host, port), Handler)
    print(json.dumps({"ok": True, "listen": f"http://{host}:{port}/graphql"}))
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        return 0
    finally:
        conn.close()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
