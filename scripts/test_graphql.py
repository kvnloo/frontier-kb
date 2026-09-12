#!/usr/bin/env python3
"""GraphQL + synapse loop against Postgres (CI store job)."""
from __future__ import annotations

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from graphql_server import execute  # noqa: E402
from kb_store import apply_schema, connect, ingest  # noqa: E402
from synapse_loop import fire, run_loop, seed_synapses  # noqa: E402


def main() -> int:
    conn = connect()
    apply_schema(conn)
    ingest(conn, "gql-test")
    seed_synapses(conn, "gql-test")
    fire(conn, "perm-20260911-encoding-beats-exposure", "gql-test", "agent")
    loop = run_loop(conn, "gql-test", apply_prune=False)

    payload = execute(
        conn,
        """
        query BrainHome {
          cycle { phase ultradianMinutes protocol { id source title } }
          cluster(id: LEARNING_ACCELERATION) { title notes { id title distilled weight retrievalDue } }
          clusterAodl: cluster(id: AODL_THESIS) { title notes { id } }
          clusterRadar: cluster(id: HARNESS_RADAR) { title notes { id } }
          llmFrontier { id title distilled }
          brain { neurons synapses meanWeight }
          note(id: "perm-20260911-encoding-beats-exposure") {
            id title distilled weight retrievalDue
            synapses { dst weight }
          }
        }
        """,
    )
    errors = payload.get("errors") or []
    data = payload.get("data") or {}
    problems: list[str] = []
    if errors:
        problems.append(str(errors))
    cluster = (data.get("cluster") or {}).get("notes") or []
    if len(cluster) < 8:
        problems.append(f"learning cluster too small: {len(cluster)}")
    if len((data.get("clusterAodl") or {}).get("notes") or []) < 6:
        problems.append("AODL_THESIS cluster too small")
    if len((data.get("clusterRadar") or {}).get("notes") or []) < 6:
        problems.append("HARNESS_RADAR cluster too small")
    if not (data.get("llmFrontier") or []):
        problems.append("llmFrontier empty")
    brain = data.get("brain") or {}
    if int(brain.get("neurons") or 0) < 10:
        problems.append("brain neurons too small")
    if int(brain.get("synapses") or 0) < 1:
        problems.append("no synapses")
    note = data.get("note") or {}
    distilled = note.get("distilled") or ""
    if "not learned" not in distilled.lower() and "exposure without encoding" not in distilled.lower():
        problems.append(f"distill failed: {distilled[:120]}")
    if not (data.get("cycle") or {}).get("protocol"):
        problems.append("cycle protocol missing")

    mut = execute(
        conn,
        """
        mutation Fire {
          fire(noteId: "perm-20260911-kb-is-a-brain-prune-and-potentiate", actor: "gql-test", kind: agent) {
            id weight
          }
        }
        """,
    )
    if mut.get("errors"):
        problems.append(f"mutation {mut['errors']}")
    fired = ((mut.get("data") or {}).get("fire") or {}).get("weight")
    if fired is None:
        problems.append("fire weight missing")

    report = {
        "ok": not problems,
        "loop": {"decayed": loop.get("decayed"), "proposals": len(loop.get("proposals") or [])},
        "neurons": brain.get("neurons"),
        "synapses": brain.get("synapses"),
        "cluster": len(cluster),
        "problems": problems,
    }
    print(json.dumps(report))
    return 0 if report["ok"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
