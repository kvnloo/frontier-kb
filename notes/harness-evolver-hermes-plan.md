---
id: harness-evolver-hermes-plan
title: "Harness Evolver — Hermes architecture plan (phased, gated, kill-criteria'd)"
type: permanent
status: draft
created: 2026-09-14
updated: 2026-09-14
harnesses: [hermes]
domains: [ai-ml, frameworks]
confidence: high
tags: [harness-evolver, rsi, architecture-plan, hermes]
---

# Harness Evolver — Hermes architecture plan

Concrete build of the generalized loop in [[permanent/perm-20260914-harness-evolver]] as a Hermes subsystem. Read that note first for the adapter interface, credit gates, and evidence base; this note is the Hermes-specific instantiation: where it lives, what it reuses, the phased rollout, and what kills each phase.

## Placement: a new top-level `evolver/` package, offline from the hot path

The evolver is an **offline diagnose–edit–eval loop around the agent loop, never a sidecar in the hot path**. New top-level directory in `NousResearch/hermes-agent`:

```
evolver/
  archive.py     # pathology-keyed failure archive: (task, trace, failure_class)
  proposer.py    # evolver worker: strong model → diff-scoped patch proposals
  gates.py       # validity → activation → credit (paired 2σ, pre-registered)
  champions.py   # MAP-Elites champion archive per pathology niche
  rollout.py     # PR/merge-queue emission + one-command rollback
  adapter.py     # the Hermes adapter implementing the 5-slot interface
```

Nothing in `agent/` changes to host it. Trace capture hooks in at the factory boundary via a JSONL contract (`fix_results/` already emits per-run records), not via repo surgery.

## The Hermes adapter (5 slots filled)

- **Evolvable surface (declared, versioned):** Phase 1: `agent/system_prompt.py` text, `agent/prompt_builder.py` assembly order, tool schemas/descriptions under `tools/`, retry/fallback policy in `model_config.gateway_runtime`. **Forbidden, always:** `evolver/gates.py`, the sealed battery, credentials/secret scope machinery, billing.
- **Open battery:** `evals/toolperf_abeval` trap tasks (evolver may see all of these) + the pathology archive.
- **Sealed battery:** abeval traps **plus a held-out slice of recent real GitHub issues**, frozen per quarter, curated by a human, evolver-blind. Never the agent's own evals — trusting-trust rots the bar.
- **Trace stream:** every factory fix-run (`~/workspace/hermes` lanes: task, trajectory, fail/pass, failure class), every background-reviewer skill-write that later scores zero use, every abeval trap failure → `(task, trace, failure_class)` into `archive.py`.
- **Rollout gate:** credited patch → PR against the repo with gate evidence attached (validity log, activation replay, credit numbers, rollback command) → human merge (Kevin). Bots advise, humans merge.

## What we already own (~80% of the substrate)

- **Factory harness** (`~/workspace/hermes/`): lanes, worktrees, `fix_results/`, red-on-base/green discipline — the trace source and the replay rig.
- **Trap battery** (`evals/toolperf_abeval/ab_eval.py`): genuine two-arm A/B on error-inducing tasks — needs sealing + wiring as the credit gate, not rebuilding.
- **Trajectory emission** (`mini_swe_runner.py`, `batch_runner.py`, `trajectory_compressor.py`): produced today with no consumer — becomes the evolver's training signal.
- **Cadence substrate** (`cron/scheduler.py` + `tools/cronjob_tools.py`): the evolver runs as a scheduled job, tool-accessible, no new infra.
- **Background reviewer** (`agent/background_review.py`): the failure stream for Phase 3's skill-promotion loop.

## Phased rollout

### Phase 0 — Calibrate the gates (weeks 1–2). Kill: calibration fails.
Build `archive.py` schema + trace capture from factory runs. Seal v1 battery. Then run the three gates on **human-authored patches** (recent real fix PRs): the gates must separate known-good from known-bad. Declare the Phase-1 evolvable surface. If the gates can't tell them apart, the methodology is broken — do not proceed to any evolver.

### Phase 1 — Prompt + retry-policy evolver (weeks 3–6). Kill: 20 generations, zero credited patches.
`proposer.py`: strong model diagnoses top pathologies, emits minimal diff-scoped patches. `gates.py` enforces validity → activation → credit; `champions.py` banks per-niche winners; `rollout.py` opens evidence-attached PRs. First credited patch is the program's proof-of-life; widen nothing until it lands.

### Phase 2 — Tool-shape evolver (after first credit). Kill: credited patches fail transfer.
Evolve tool schemas/descriptions/ABI — the ~20-point lever. Blast radius is bigger, so credited patches go through **canary rollout** (N% of runs) before the human merge gate. Transfer test on held-out task families is the kill criterion: lift that evaporates off-battery is overfit, not improvement.

### Phase 3 — Close the memory write-loop (after Phase 2 transfers). Kill: no Δ on long-horizon recall evals.
Reuse the credit methodology for the three memory gaps: eval-gated skill promotion (draft index → trap-battery self-test → live index), curator consolidation switched on **with measured retention** (not hope), holographic trust + a consolidation half. The evolver's gates become the memory loop's measurement spine.

## Metrics

- Primary: **Δ sealed-battery pass rate per generation** (2σ paired, pre-registered).
- Compounding signature: **$/credited patch must fall** as the archive grows.
- Transfer: credited patches must hold ≥80% lift on held-out task families.
- Learning health: prune rate on the champion archive (dead niches get pruned, per the KB's synaptic-homeostasis design).

## Cost budget

Cap spend per generation. Cheap/free models run validity + activation replays; the strong model is spent only on diagnosis + proposal. Track and publish $/credited patch per generation.

## Safety boundaries (architectural, not hoped-for)

Offline loop; never touches the hot path. Credit gate, evaluator, sealed battery, credentials, and billing are outside the evolvable surface **by declaration** (`adapter.py` enforces it — the proposer cannot emit diffs outside the surface). Human merge gate on every deployment. One-command rollback, versioned surface.

## Related

- [[permanent/perm-20260914-harness-evolver]] — the generalized, harness-agnostic version (adapter interface, results table, per-harness applicability)
- [[harnesses/hermes]] — Hermes harness note
- [[literature/lit-20260910-gsme-self-evolving-harness]]
- [[literature/lit-20260910-evo-bench-harness-evolution]]
- [[permanent/perm-20260910-evolver-lifts-frozen-policy]]
- [[permanent/perm-20260910-measure-the-learning-loop]]
- [[permanent/perm-20260911-kb-is-a-brain-prune-and-potentiate]]
