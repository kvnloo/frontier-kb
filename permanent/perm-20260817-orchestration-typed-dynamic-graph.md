---
id: perm-20260817-orchestration-typed-dynamic-graph
title: "Orchestration is a typed dynamic graph, not a static DAG"
type: permanent
status: active
created: 2026-09-10
updated: 2026-09-10
harnesses: [hermes, omp, grok, codex]
domains: [frameworks, mathematics, cs]
confidence: high
tags: [permanent, aodl, hotl]
---

# Orchestration is a typed dynamic graph, not a static DAG

## Idea (atomic)

An orchestration at logical time \(t\) is

\[
\mathcal{O}_t = (V_t, E_t, S_t, \Pi_t, \Gamma_t)
\]

- \(V_t\): agents, models, tools, humans, memories, environments, tasks, artifacts
- \(E_t\): typed relations (delegate, message, critique, verify, depend, observe, control, award)
- \(S_t\): runtime state
- \(\Pi_t\): routing / execution / allocation policy
- \(\Gamma_t\): goals, constraints, budgets, verification

The system evolves \(\mathcal{O}_0 \rightarrow \cdots \rightarrow \mathcal{O}_T\). Spawning a debugger after a coder fails, or a second reviewer after reject, is a **graph mutation**, not a different English topology name. A conventional workflow language encodes `A → B → C`. This object must encode who may create whom, who may communicate, what crosses an edge, when topology may change, what completion means, and how success is established.

## Why it matters for our harnesses

Dash, Hermes Kanban, OMP `task`, and grok-bot all currently describe **nodes** (harness CLIs, profiles, bots) without a comparable description of **topology**. “Swarm” on a badge is not a computational structure. HOTL 0.2 is the attempt to make this IR; Dash’s Bots pane is a projection of observed \(V\), not \(\mathcal{O}_t\).

## Related

- [[literature/lit-20260817-aodl-voice-transcript]]
- [[literature/lit-20260817-hotl-02-spec]]
- [[permanent/perm-20260817-intent-plan-observed]]
- [[permanent/perm-20260817-market-is-allocation-policy]]
- [[harnesses/hermes]]
- [[domains/frameworks]]
