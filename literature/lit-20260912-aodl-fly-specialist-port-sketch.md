---
id: lit-20260912-aodl-fly-specialist-port-sketch
title: "AODL intent sketch: fly specialist port (not yet aodl/examples)"
type: literature
status: draft
created: 2026-09-12
updated: 2026-09-12
sources: ["https://github.com/kvnloo/aodl/blob/main/examples/valid/pipeline.json", "https://github.com/kvnloo/aodl/blob/main/schema/hotl-0.2.schema.json"]
harnesses: [hermes, cursor]
domains: [frameworks]
confidence: medium
tags: [literature, aodl, fly, sketch]
---

# AODL intent sketch: fly specialist port (not yet aodl/examples)

## Claim (one sentence)

P0 compiles to an HOTL 0.2 document that already validates as a **sequence** with a verifier and an escalation model — using only catalog kinds — so the fly student is a port on \(\mathcal{O}_t\), not a new topology.

## Evidence

This is an **intent sketch** for later `examples/valid/fly-specialist-port.json`. It is not validated by `kvnloo/aodl` CI in this workspace. `provenance.sourceHash` is a placeholder; replace before landing. Node `kind` enum is taken from `schema/hotl-0.2.schema.json`.

```json
{
  "specVersion": "0.2",
  "graphId": "fly-specialist-port",
  "revision": 0,
  "intentGraph": {
    "nodes": [
      {
        "id": "events",
        "kind": "environment",
        "ports": [
          {"id": "out", "direction": "out", "schema": "OperationalEvent", "classification": "sanitized"}
        ],
        "capabilities": ["observe"],
        "authorityCeiling": ["observe"],
        "lifecycle": "declared"
      },
      {
        "id": "specialist",
        "kind": "executor",
        "ports": [
          {"id": "in", "direction": "in", "schema": "OperationalEvent", "classification": "sanitized"},
          {"id": "out", "direction": "out", "schema": "RecoveryAction"}
        ],
        "capabilities": ["execute"],
        "authorityCeiling": ["execute"],
        "lifecycle": "declared"
      },
      {
        "id": "qwen38_27b",
        "kind": "model",
        "ports": [
          {"id": "in", "direction": "in", "schema": "OperationalEvent", "classification": "sanitized"},
          {"id": "out", "direction": "out", "schema": "RecoveryAction"}
        ],
        "capabilities": ["execute"],
        "authorityCeiling": ["execute"],
        "lifecycle": "declared"
      },
      {
        "id": "recovery_action",
        "kind": "tool",
        "ports": [
          {"id": "in", "direction": "in", "schema": "RecoveryAction"},
          {"id": "out", "direction": "out", "schema": "RecoveryAction"}
        ],
        "capabilities": ["execute"],
        "authorityCeiling": ["execute"],
        "lifecycle": "declared"
      },
      {
        "id": "outcome",
        "kind": "verifier",
        "ports": [
          {"id": "in", "direction": "in", "schema": "RecoveryAction"},
          {"id": "out", "direction": "out", "schema": "Task"}
        ],
        "capabilities": ["execute"],
        "authorityCeiling": ["execute"],
        "lifecycle": "declared"
      },
      {
        "id": "captain",
        "kind": "humanGate",
        "ports": [
          {"id": "in", "direction": "in", "schema": "Task"},
          {"id": "out", "direction": "out", "schema": "Task"}
        ],
        "capabilities": ["approve"],
        "authorityCeiling": ["approve"],
        "lifecycle": "declared"
      }
    ],
    "edges": [
      {
        "id": "e-events-specialist",
        "relation": "dependency",
        "from": "events",
        "to": "specialist",
        "fromPort": "out",
        "toPort": "in",
        "delivery": {"order": "ordered", "idempotent": true, "timeoutMs": 5000, "maxRetries": 0},
        "authority": {"grant": ["execute"], "delegationDepth": 0},
        "provenance": {"sourceHash": "REPLACE_BEFORE_AODL_LANDING"}
      },
      {
        "id": "e-specialist-action",
        "relation": "dependency",
        "from": "specialist",
        "to": "recovery_action",
        "fromPort": "out",
        "toPort": "in",
        "delivery": {"order": "ordered", "idempotent": true, "timeoutMs": 5000, "maxRetries": 0},
        "authority": {"grant": ["execute"], "delegationDepth": 0},
        "provenance": {"sourceHash": "REPLACE_BEFORE_AODL_LANDING"}
      },
      {
        "id": "e-action-outcome",
        "relation": "verification",
        "from": "recovery_action",
        "to": "outcome",
        "fromPort": "out",
        "toPort": "in",
        "delivery": {"order": "ordered", "idempotent": true, "timeoutMs": 60000, "maxRetries": 0},
        "authority": {"grant": ["execute"], "delegationDepth": 0},
        "provenance": {"sourceHash": "REPLACE_BEFORE_AODL_LANDING"}
      }
    ]
  },
  "policies": {
    "kinds": ["sequence", "retry"],
    "fanIn": "all",
    "dynamic": {"allowed": false, "maxChildren": 0, "maxDepth": 0}
  },
  "constraints": {
    "budgets": {"tokens": 0, "joules": 0, "spawn": 1},
    "termination": {"on": "verifier.succeeded"}
  },
  "provenance": {
    "source": "frontier-kb-sketch",
    "sourceHash": "REPLACE_BEFORE_AODL_LANDING"
  }
}
```

Escalate-to-Qwen and `humanGate` edges are **policy**, not extra topology kinds. Unfamiliar states raise \(\Gamma_t\) and take the `model` node; hard-policy hits go to `captain`. Secret-bearing schemas are invalid at the specialist `in` port.

Fail-closed codec rule (thesis-intent): an image or video payload without a bound vision child must not compile.

## Fact vs interpretation

- Fact: HOTL 0.2 already has executor/model/tool/verifier/humanGate/environment.
- Interpretation: landing this file in aodl is a later PR on `kvnloo/aodl`, not a Dash rewrite.
- HOLD: `constraints.budgets.joules` may not be in the schema yet. If validation rejects unknown budget keys, keep joules in provenance until the schema grows — do not fork 0.3 for one field.

## Links

- [[permanent/perm-20260912-fly-specialist-is-an-aodl-port]]
- [[literature/lit-20260912-flyforge-research-roadmap]]
- [[literature/lit-20260817-hotl-02-spec]]
