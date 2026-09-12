---
id: inbox-cursor-aodl-formalism-20260911
title: "Push AODL as a mathematical language without a new kind"
type: inbox
status: draft
created: 2026-09-11
updated: 2026-09-11
node: cursor
harnesses: [cursor]
domains: [mathematics, physics, cs, information-theory, neuroscience]
tags: [inbox, aodl, formalism, sheaf, session-types]
---

# Formalize orchestration as language, not as a new product

## Context

AODL already has $\mathcal{O}_t=(V_t,E_t,S_t,\Pi_t,\Gamma_t)$ and intent $\neq$ plan $\neq$ observed. The 2026-09-11 pass says: add **readings and compiler profiles**, not schema kinds, until a Hermes dry-run exists.

Proposed composition (interpretation, not 0.3):

- **Intra-node:** $\lambda_A$ (oracle + bounded fix). Missing terminate / unbounded spawn is already fail-closed.
- **Inter-node:** HOTL graph. `message` edges may later carry a global type (MPST / Pact). Duality failure is $\bot$.
- **Geometry:** intent/plan/observed as three sheaves on a time site; gluing = merge receipts; obstruction = fail closed. Do not JSON-encode a topos.
- **Stats/control:** $\Pi_t$ is a policy on a typed graph MDP. AdaptOrch: topology dominates once models converge.
- **Info theory:** rate = tokens; distortion = missed deps / stale state. RLM = $\mathcal{O}_t$ lives outside the window.
- **Consciousness/philosophy (discipline):** blackboard $\neq$ IIT; active inference $\approx$ $\Gamma_t$; Keel L0 is collective intentionality ("router is not the project"). Density of a drawing is not $\Phi$.

Push order: compiler dry-run, human-attention budget in $\Gamma_t$, spawn coherence + verifier, architecture search over **valid documents**, then optional session-type profile.

## Next action

Do not change `schema/hotl-0.2.schema.json` from this note. If a construct lands later: one valid fixture and one invalid fixture.

## Links

- https://github.com/kvnloo/aodl/blob/main/docs/research-craid-20260911.md
- [[permanent/perm-20260817-intent-plan-observed]]
- [[permanent/perm-20260817-aodl-ir-first]]
- [[permanent/perm-20260910-craid-is-named-hybrid]]
- https://arxiv.org/abs/2604.11767
- https://arxiv.org/abs/2605.03143
- https://arxiv.org/abs/2605.01879
