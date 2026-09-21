---
id: lit-20260919-sol-pi-recursive-efficient-improvement
title: "SoL-Pi recursive efficient improvement — literature reconciliation"
type: literature
status: draft
created: 2026-09-19
updated: 2026-09-21
sources: ["https://arxiv.org/abs/2609.20519", "https://github.com/NVlabs/SoL-Pi"]
harnesses: [pi, omp]
domains: [frameworks, tool-use, tokenomics, ai-ml]
confidence: medium
tags: [literature, sol-pi, nvidia, autoresearch]
---

# SoL-Pi recursive efficient improvement (lit reconciliation)

Link: arXiv:2609.20519 (SoL-Pi)
Author: SoL-Pi / NVlabs
Date read: 2026-09-19
Status: Literature reconciliation (not operational state)

## Thesis (from paper)

Harness is trainable. Freeze worker/model behavior during each experiment.
Mutate scaffold. Credit only externally verified improvements.

Broad-to-deep auto-research: broad mechanism families → cheap falsification → deeper mutation within surviving family → paired evaluation → promotion gate.

## Four surviving mechanisms (mapped to z0 repos)

1. Tool ABI efficiency (action-fusion / tool-shape) → OMP extension / tool layer
2. Exact evidence plane + verifiable reduction → RLM / cognitive-state
3. Context economics / cache-read-write pricing → RLM controller / tokenomics
4. Recursive efficient improvement (measured, not assumed) → Evolution Lab (RFC 2)

## Capability floor (explicit)

Compounding NOT demonstrated by paper; hypothesized only.
Measured only by: verified_success, provider_turns/verified_success, tokens/verified_success, cost/verified_success, wall_time/verified_success, joules/verified_success where measurable.

## Held-out evaluation (explicit)

Every promotion requires sealed battery (G5) before live canary (G6).
No autonomous merge (P0 stops at gate calibration + seed candidates + open eval).

## Mapping to z0 repositories

- OMP: execution semantics, extension surface, tool ABI (Action Fusion belongs here)
- RLM: provider projection, exact evidence plane, verified reduction (RFC 79 updated)
- z0intelligence: bounded live decisions / policy / decision receipts
- Evolution Lab: experiment generation, candidate lineages, archive, gates (RFC 2 new)
- Tokenomics: experiment identity / verified outcomes / token/cache/cost/latency accounting
- AGY: research + implementation workers (not routing authority)
- live-runtime: attestation / rollback / canary (current core 51f8a20 + AGY a1686ce verified)
- Braid: asynchronous reconciliation (NOT required for P0)
- AODL: contracts / authority / budget (NOT scheduler)
- AgentTrace: trajectory / candidate / activation (for observation, not control)
- frontier-kb: public memory (this file lives here, not operational state)

## Explicit statement of current evidence status

- Broad-to-deep methodology: documented by paper; NOT yet executed by z0 experiment loop
- Recursive efficient improvement: HYPOTHESIS ONLY; no measured loop yet
- Action Fusion: smoke PASS (SoL-Pi source bd00588); NOT globally adopted (no promotion gate met)
- RLM Phase II: RFC #79 updated; ATTENTION: no autonomous merge; agent_settled lifecycle preserved
- AGY: loaded (a1686ce) but SHADOW only (per user's rule); no routing authority
- Jev (TypeSafe / OpenJev / NanoJev / vLLM): loaded but shadow/log; no consumption of routing decisions
- Shadow delay: measured ~30-200ms sequential per turn; no frontier-avoidance evidence

## Corrections applied to frontier-kb (this session, 2026-09-19)

1. Stale claim removed: "missing findCutPoint blocks fingerprinting" → corrected (findCutPoint present via z0int-bridge; fingerprints verified for agy-executor / z0-live-runtime)
2. OCC/state mismatch claim updated: migration requires core reload + AGY attestation; session state preserved; no full restart required
3. Published literature link: arXiv:2609.20519 (read from SoL-Pi repo bd00588, not from upstream paper copy — paper's own source is authoritative for mechanism descriptions)
4. Distinction preserved: tool-shape efficiency ≠ task-level verified efficiency; metrics must include verification + fallback/retry
5. Cash / savings: NOT measured; shadow writes do not prove skipped frontier; only receipt with skipped_provider tag can prove it

## Cross-references

- Older note: `literature/lit-20260910-evo-bench-harness-evolution.md` (existing harness-evolver mechanism)
- RFC 79 update: `/tmp/omp-jev-probe/frontier-kb-reconciliation.md` (section 5)
- RFC 2 (Harness Pretraining): `/tmp/omp-jev-probe/frontier-kb-reconciliation.md` (section 6)
- Action Fusion experiment issue: `/tmp/omp-jev-probe/frontier-kb-reconciliation.md` (section 7)