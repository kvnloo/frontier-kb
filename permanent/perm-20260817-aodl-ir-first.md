---
id: perm-20260817-aodl-ir-first
title: "AODL is an IR; pretty DSL comes later"
type: permanent
status: active
created: 2026-09-10
updated: 2026-09-10
harnesses: [hermes, omp]
domains: [frameworks, mathematics]
confidence: high
tags: [permanent, aodl, ir]
---

# AODL is an IR; pretty DSL comes later

## Idea (atomic)

Do not start by inventing a pretty DSL. Pipeline:

```text
AODL/HOTL source → parser → typed IR → static validator → runtime → event/state log
```

Readable syntax is sugar. Every authority, data, budget, and policy field stays explicit in IR. First milestone that proves generality: the **same primitives** express ReAct and RLM. If those need special cases in the runtime, the calculus is not general enough. Architecture search is then search over programs in this IR, not over hardcoded `planner(); coder(); reviewer()`.

ReAct, planner-executor, debate, swarm, hierarchical agents, and tree search become **instances of one state-transition system**, not separate products.

## Why it matters for our harnesses

OMP/Hermes/Dash currently special-case each topology in prompts and UI badges. A shared IR would let Dash’s orchestra pane decode a graph instead of painting a named glyph, and would let an optimizer mutate architecture without rewriting harness adapters.

Prior art likely covers 60–80% (Petri, BPMN, CWL, actors, FIPA Contract Net, OPA, PROV). The missing piece is the agent-specific ontology + interchange, not “a graph.”

## Related

- [[permanent/perm-20260817-orchestration-typed-dynamic-graph]]
- [[literature/lit-20260817-hotl-02-spec]]
- [[permanent/perm-20260817-no-aodl-repo]]
