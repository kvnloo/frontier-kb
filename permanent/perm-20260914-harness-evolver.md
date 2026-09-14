---
id: perm-20260914-harness-evolver
title: "The Harness Evolver: one evolver loop, any harness, via a 5-slot adapter interface"
type: permanent
status: draft
created: 2026-09-14
updated: 2026-09-14
harnesses: [omp, hermes, codex, claude, cursor, opencode]
domains: [ai-ml, frameworks]
confidence: high
tags: [permanent, evolver, rsi, harness-evolution, adapter, credit-gates]
---

# The Harness Evolver: one evolver loop, any harness, via a 5-slot adapter interface

## Idea (atomic)

Recursive self-improvement that compounds lives in the **scaffold, not the weights**: freeze the worker model, let a separate (stronger/different) evolver propose diff-scoped patches to the harness from pathology-keyed failure traces, and credit them through three deterministic gates on a sealed battery. The loop is portable across harnesses because every harness only needs to expose five things: the **evolvable surface** (versioned, diffable artifacts), an **open battery** (evolver may see), a **sealed battery** (evolver-blind, human-curated), a **trace stream** (`task, trace, failure_class`), and a **rollout gate** (deploy + one-command rollback). The same evolver binary then drives OMP, Hermes, Codex, Claude Code, Cursor, and opencode — only the adapter differs.

## The adapter interface

```yaml
adapter:
  scaffold:            # WHAT the evolver may touch — declared, versioned, diffable
    surface: [prompts, tool_schemas, retry_policies, config_defaults]
    forbidden: [credit_gate, evaluator, credentials, billing]  # never evolvable
  batteries:
    open:   # diagnosis + proposal; evolver sees everything here
    sealed: # credit only; human-curated, frozen per quarter, evolver-blind
  traces:              # (task, trace, failure_class) stream into the pathology archive
  rollout:
    deploy: [pr | config_flip | canary_pct]   # how a credited patch ships
    rollback: one_command                      # instant revert, always
    merge_gate: human                          # bots advise, humans merge
```

Sealed vs unsealed is the load-bearing wall: the evolver diagnoses on open traces and proposes against the open battery, but **credit is only ever measured on the sealed battery it cannot see**. Transfer is measured on held-out task *families*, never just held-out instances. Rotate the sealed battery quarterly; a patch that loses its lift on rotation was overfit, not credited — demote it.

## The three credit gates (GSME's, tightened)

1. **Validity** — patch applies cleanly; existing tests/typecheck green. Cheap, deterministic.
2. **Activation** — the patch demonstrably fires in ≥1 replayed failing trace. A patch that never triggers is dead code with a good story.
3. **Credit** — paired A/B on the sealed battery, **2σ significance, pre-registered**. Then the human merge gate.

Add a fourth mechanism, not a gate: a **champion archive per pathology niche** (MAP-Elites flavor). Keep the best patch per failure class even when it loses globally — stepping stones survive for recombination. Losing patches are retained as negative data.

## Phasing (same for every harness; blast radius grows last)

- **Phase 0 — calibrate the gates.** Run the three gates on *human-authored* patches first. If the gates can't distinguish known-good from known-bad, the methodology is broken — fix it before any evolver runs. Kill: calibration fails.
- **Phase 1 — narrow surface.** Evolve prompts + retry policies only. Kill: 20 generations, zero credited patches.
- **Phase 2 — tool shape.** Evolve tool schemas/descriptions/ABI (the ~20-point lever from `perm-20260910-scaffold-tool-shape-dominates`). Bigger blast radius → **canary rollout** (patch ships to N% of runs before the merge gate). Kill: credited patches fail the transfer test.
- **Phase 3 — close the memory write-loop.** Reuse the credit methodology for eval-gated skill promotion, curator consolidation with measured retention, trust-weighted memory. Kill: no Δ on long-horizon recall evals.

## Results table (the evidence base)

| Result | Gain | Why it matters here |
|---|---|---|
| **GSME** (arXiv:2607.13683) — stronger evolver, frozen 27B, pathology-keyed archive, 3 gates | **+9.3pp Terminal-Bench 2 sealed** (36.1→45.4), 86–147% retention | The exact loop shape; transfer survives model swaps |
| **Evo-Bench** (arXiv:2608.09096) — Qwen3.6-27B as evolver, DeepSeek frozen | **+9.7 overall** (held-out) | Evolver need not be frontier-expensive |
| **Darwin Gödel Machine** (ICLR 2026) — agent edits own code, empirical keep-if-better, 80 iters | SWE-bench 20%→50% | Variant archive + empirical gate compounds |
| **Huxley-Gödel Machine** — lineage scored by descendants (clade metric) | Beats prior methods, fewer CPU hours | Score the lineage, not the patch |
| **Voyager** — writes, verifies, reuses executable skills | 3.3× items, milestones up to 15.3× faster | Verify-then-promote is the skill-side twin |

## Cost discipline

Cap spend per generation. Track **$/credited patch** — it must *fall* as the pathology archive grows; that's the compounding signature. Use cheap/free models for validity/activation replays; spend the strong model only on diagnosis + proposal. If $/credited patch rises for 3 consecutive quarters, the surface is exhausted — narrow it or stop.

## Counterarguments, answered

- **Goodhart / battery gaming.** The transfer test + quarterly rotation + human curation is the answer; a patch that evaporates on transfer was never credited. This is why the kill criterion for Phase 2 is transfer failure, not battery score.
- **Shared blind spots (evolver ≈ worker).** Evolver must be stronger or at least *different* from the worker; the pathology archive forces coverage of failure modes the worker can't see. Same-model attacker/defender pairs delude each other — don't do that here.
- **"Just prompt-tuning with extra steps."** Scope is the whole scaffold (tool ABI, retry policies, memory loop), credit is statistical and sealed, and the archive compounds failure-mode *coverage* (MAP-Elites), not one hill-climbed metric.
- **Self-modification safety.** Offline loop, never the hot path; the credit gate, evaluator, and credentials are outside the evolvable surface by declaration; human merge gate; one-command rollback; versioned surface. Containment is architectural, not hoped-for.
- **Diminishing returns.** Expected and priced in: the champion archive banks stepping stones, $/credited patch is tracked, and the kill criteria stop the loop instead of letting it burn money on motion.

## Applicability per harness

- **Hermes / OMP** — full surface: prompts, tool schemas, retry policies, cron config. See [[notes/harness-evolver-hermes-plan]] for the concrete build.
- **opencode** — fully open loop; easiest full-stack target after Hermes. Evolvable surface can include the agent loop itself.
- **Codex / Claude Code / Cursor** — closed cores: the evolvable surface is the *wrapper layer* (injected system prompts, tool/MCP definitions, retry policies), never the vendor core. Credit on your own sealed battery of your own tasks; you still get the compounding, scoped to what you control.

## Non-recommendations (attractive, won't compound)

SFT a small orchestrator (weights don't transfer, harnesses do); inference-time weight RSI on agentic loops (no verifiable per-step reward yet); debate-as-amplifier (bounded by the strongest reasoner); Reflexion alone (plateaus, no cross-task generalization); **agent-written evals** (each generation lowers the bar — the sealed battery stays human-curated, always); swarms without a fitness signal (N× cost, sub-linear gain); naive volume (deliberate-practice literature: volume with coarse feedback plateaus).

## Related

- [[notes/harness-evolver-hermes-plan]] — the concrete Hermes build plan
- [[literature/lit-20260910-gsme-self-evolving-harness]]
- [[literature/lit-20260910-evo-bench-harness-evolution]]
- [[permanent/perm-20260910-evolver-lifts-frozen-policy]]
- [[permanent/perm-20260910-scaffold-tool-shape-dominates]]
- [[permanent/perm-20260910-no-universal-harness-plugin]]
- [[permanent/perm-20260911-bots-advise-humans-merge]]
- [[permanent/perm-20260911-measure-the-learning-loop]]
