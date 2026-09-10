---
id: lit-20260817-hotl-02-spec
title: "HOTL/AODL 0.2 research specification"
type: literature
status: active
created: 2026-09-10
updated: 2026-09-10
sources: ["groot:/workspace/hermes-home/kanban/boards/zer0-company/attachments/t_83991e68/hotl-0.2-report.md", "https://github.com/NousResearch/hermes-agent/issues/88589"]
harnesses: [hermes, omp]
domains: [frameworks, mathematics, tokenomics, cs]
confidence: high
tags: [literature, hotl, aodl, ir]
---

# HOTL/AODL 0.2 research specification

## Claim (one sentence)

HOTL should be a **specification/IR + validator**, not a second scheduler: keep desired topology, compiled plan, observed runtime, authority, evidence, and human approval distinct.

## Evidence

- Package (groot, 2026-08-17 14:23 local): `hotl-0.2-report.md`, `hotl-0.2.schema.json`, `hotl-0.2.ebnf`, `architecture.mermaid`. README mentions `examples/` and `tests/validate.py` that were **not** written into the attachment dir.
- Wire id: `hotl-0.2`. `HOTL` kept for continuity; **AODL** is a possible future public name (collides with “agent-oriented”).
- Formal object: \(O_t=(V_t,E_t,S_t,\Pi_t,\Gamma_t)\) is the **observed** graph at logical time t. Document = `intentGraph` + `policies` + `constraints` + `provenance`. Compiler emits immutable `plan`. Runtime emits append-only `eventLog` + `observedGraph`.
- Transition \(C \xrightarrow{a} C'\) only if schema/type, policy, capability ceiling, budget reservation, and event nonce pass. Unbounded recursion is invalid.
- Market is **policy**, not topology: announce → bid → award → execute → verify → settle. Autonomous payment unsupported.
- Literature audit (hypothesis, not measured): 60–80% of machinery already exists (Petri/BPMN/CWL/actors/FIPA/OPA/PROV/LangGraph/MCP/A2A). Genuinely new candidate: conservative cross-runtime ontology tying ports, authority, dynamic mutation, evidence, and human gates.
- Hermes adapter: compile to Kanban task IDs + Keel gates; project events back to observed \(O_t\); fail closed on unsupported semantics.
- Starmap/learning graph is a **projection** (radius = time), not an event ledger. Reuse layout; do not conflate memory edges with orchestration edges.

## Fact vs interpretation

- Fact: 0.2 is docs-only; no runtime, no second ledger, no git repo.
- Interpretation: \(\theta = \theta_{\text{base}}+A_{\text{identity}}+A_{\text{factory}}\) is an architecture hypothesis, not a learned-model equation. Token-efficiency of graph slices vs full dump is a benchmark, not a theorem.

## Links

- [[permanent/perm-20260817-orchestration-typed-dynamic-graph]]
- [[permanent/perm-20260817-intent-plan-observed]]
- [[permanent/perm-20260817-aodl-ir-first]]
- [[permanent/perm-20260817-market-is-allocation-policy]]
- Parent issue: [[literature/lit-20260817-hotl-01-issue-88589]]
