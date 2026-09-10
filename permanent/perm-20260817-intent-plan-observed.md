---
id: perm-20260817-intent-plan-observed
title: "Keep intent, compiled plan, and observed O_t distinct"
type: permanent
status: active
created: 2026-09-10
updated: 2026-09-10
harnesses: [hermes]
domains: [frameworks]
confidence: high
tags: [permanent, hotl]
---

# Keep intent, compiled plan, and observed O_t distinct

## Idea (atomic)

Three objects, never substituted:

```text
Desired graph     what the controller intends
Compiled plan     what a specific runtime can safely support
Observed O_t      what actually exists and is happening now
```

A HOTL document is intent (`intentGraph` + `policies` + `constraints` + `provenance`). A compiler emits an immutable `plan`. A runtime emits an append-only `eventLog` and `observedGraph`. Reverse-projecting Kanban tasks back into a “swarm” drawing is a lie unless the policy was recorded. Unsupported semantics must **fail closed**, not be inferred from a glyph.

## Why it matters for our harnesses

Hermes Starmap radius-as-time is a **projection** of memory, not an orchestration ledger. Dash `/roster` is an observed host/agent list. Neither is the intent graph. Compiling AODL/HOTL into Hermes Kanban must map only dependency + review/goal contracts that already exist; message/auction/mesh stay visualization-only until a runtime contract exists ([[literature/lit-20260817-hotl-01-issue-88589]]).

## Related

- [[permanent/perm-20260817-orchestration-typed-dynamic-graph]]
- [[literature/lit-20260817-hotl-02-spec]]
- [[harnesses/hermes]]
