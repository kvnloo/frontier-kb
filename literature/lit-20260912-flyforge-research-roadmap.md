---
id: lit-20260912-flyforge-research-roadmap
title: "FlyForge research roadmap: P0 Hermes recovery before distillation"
type: literature
status: active
created: 2026-09-12
updated: 2026-09-12
sources: ["https://chatgpt.com/share/6aa4e9ce-e88c-83ea-bf45-0e9496a1ad6f?ogimg=plain", "https://github.com/kvnloo/aodl/blob/main/docs/network.md", "https://artificialscientific.com/papers/flies-are-all-you-need"]
harnesses: [cursor, hermes, omp, pi]
domains: [ai-ml, neuroscience, frameworks, physics, cs]
confidence: high
tags: [literature, fly, roadmap, p0, aodl]
---

# FlyForge research roadmap: P0 Hermes recovery before distillation

## Claim (one sentence)

The critical path is **lock a verified Hermes recovery contract, then run a control table (MLP/GRU, direct-input, degree-preserving rewire, fixed reservoir, motif student) under joules-per-verified-success** — distill, grow, and “fly-Qwen” search come after that table exists.

## Evidence

This note compiles the ChatGPT share ([[literature/lit-20260912-chatgpt-flyforge-share]]), the 10-agent genuine-apps loop ([[literature/lit-20260912-connectome-genuine-apps]]), and the AODL network ([kvnloo/aodl `docs/network.md`](https://github.com/kvnloo/aodl/blob/main/docs/network.md)). The **runner** is `apps/evolution-lab` ([[literature/lit-20260912-chatgpt-evolution-lab-share]]). No Tinker or MaleCNS SGD has been run.

### What the idea is (and is not)

| Is | Is not |
| --- | --- |
| Biological circuitry as an **architectural prior** | A fly that replaces Qwen3.8-27B |
| Trainable student on a **bounded action contract** | SWE-bench / TB2.1 scoring of MaleCNS |
| Hybrid allowed if **counted** (encoder + specialist + Qwen fallback) | “Same English prompt” as a fair test |
| Motif distillation (EMD, loom, MB hash) as the likely winner | Upload / digital patient / 166k LIF worker swap |
| fly-inspired after reorganization | Faithful simulated fly brain after RigL |

Two distinct “fly version of Qwen” projects (share §6):

1. **Qwen-distilled controller** — copies verified *actions*. First experiment.
2. **Qwen-distilled language model** — must run without Qwen at inference; tokenizer/readout dominate (fly-hf: 50.6M of 52.8M params in the readout). Parallel, non-blocking.

### Efficiency accounting (mandatory)

Deployment cost = encoding + policy execution + decoding + runtime overhead + fallback. For graphs, edge-steps × recurrent updates per decision are part of execution. Neuron count vs 27B is not a ratio. Biological ~0.12–0.26 μW CNS power and GPU LIF watts are different objects ([[permanent/perm-20260912-emulation-inverts-biological-efficiency]]).

Primary metric ([[permanent/perm-20260912-joules-per-verified-success]]):

\[
\text{Joules per verified success} = \frac{\text{energy of all evaluation attempts}}{\text{verified successful episodes}}
\]

Numerator includes failures. Hosted-model joules stay **unknown** unless measured. Training/teacher cost is a separate ledger from deployment. Frontier is relative to the **declared candidate set**, not a global optimum. Search points 10K, 100K, 1M, 10M, 32M, 100M, 300M, 1B are **not** predicted optima.

NeuroBench’s algorithm-level vs system-level split is the methodological parent (share §2).

### Same-task definition

Every system gets the same **available information**, **permitted history**, **action contract**, and **external verifier**.

- **Track A — shared-feature:** identical numerical fields (tool status, elapsed time, remaining budget, last N actions). Isolates the controller. Language models receive those fields explicitly, not a screenshot they must parse.
- **Track B — end-to-end:** raw observations; each pays for its encoder. A VLM that consumes screenshots is a different deployed object than a fly-motif + compact encoder.

Task suite (proposed, not measured):

| Task | Why |
| --- | --- |
| **Hermes recovery / escalation (P0)** | Always-on niche; typed events; outcome is observable; secrets stay out |
| Delayed-cue memory | Tests whether recurrence is doing work |
| Looming / motion deadline | Matches EMD/LPLC2, FlyVis, Opteran |
| Constrained language-to-action | Bridge toward a Qwen-distilled specialist |

Free-form conversation is a separate evaluation. Do not mix it into the recovery score.

Target (register before testing): ≥95% of reference-controller verified success, ≤50% deployment cost, **zero additional hard-policy violations**. Non-inferiority margin is part of the lock, not a vibe.

### Architecture matrix (every P1 table)

| Branch | What may learn | Question |
| --- | --- | --- |
| MLP with the same history | weights | Is recurrence even needed? |
| Compact GRU / sequence baseline | weights | Does a small conventional RNN already win? |
| Direct-input adapter | same param budget, no graph | FLM lesson: this often eats the gain |
| Degree-preserving rewired graph | readout + optional dynamics; **refit** | Is it this wiring or any sparse graph? |
| Fixed MaleCNS / FlyWire reservoir | I/O + readout only | Inherited graph as features? |
| Type-tied recurrent graph | shared cell-type gains (FlyVis-style) | Does biological tying help sample efficiency? |
| Trainable / reorganized graph | selected weights + connectivity (FlyGM / RigL) | Anatomy as init? |
| Motif-distilled student | EMD / loom / MB-hash / 3-neuron CPG | Can we drop the anatomy? |

Matched training budgets apply **among students**. A pretrained generalist (Qwen3.8-27B, DeepSeek-V4.1-Flash, SmolVLM2-500M, LFM2.5-VL-1.6B) is a **deployed product** comparator, not an equal-lifetime-training control. Qwen3.8 is a hybrid Gated DeltaNet/attention model; the comparison is not “bio recurrence vs dense attention.”

### Phases

**P0 — Lock the contract (do this first; no graph SGD yet)**

1. Freeze the action enum (example: `retry`, `restart_sandbox`, `escalate_qwen`, `noop`, `page_human`).
2. Freeze the event schema: sanitized operational fields only. Classification `sanitized`. No credentials, no screenshot-of-secrets ([[permanent/perm-20260910-screenshots-bypass-vault-redaction]], Keel L0).
3. Write the external verifier (eventual task completion, no extra policy hits).
4. Collect or synthesize a locked episode set. Split train / val / confirm **before** students.
5. Run the **reference** (current Hermes/Qwen recovery policy) and a **small GRU** on Track A. Log failures.
6. Emit JSONL the dashboard can import. Empty charts until then are honest.

Exit: a failing unit test if a student sees a secret-bearing field; a passing GRU baseline log.

**P1 — Control table on Track A**

Fit every row of the matrix that can run locally. Teacher = already-served Qwen. Students stay small. Do not buy hardware as a prerequisite. A 27B at 4-bit is ~13.5 GB weights **before** runtime; do not assume the full multimodal Qwen fits in 12 GB.

Kill criterion: if GRU and direct-input dominate the fly reservoir on val, **do not** spend a cycle on MaleCNS SGD. Pivot to motif students (already the genuine-apps consensus).

**P2 — Distill verified decisions**

Teacher trajectories + **outcomes**, not plausible prose. Distribution-match when logprobs exist; otherwise hard labels. Tokenizer index matching across vocabs is not a distillation loss (share §6).

**P3 — Student states (DAgger) + bounded RL**

Train on states the student actually visits. Forgetting tests when adding tasks. Learning-during-test is a separately declared regime.

**P4 — Grow / reorganize**

RigL as non-biological prune/regrow. Net2Net-style expansion only with an explicit function-preservation check; guarantees do not transfer to arbitrary recurrent connectomes. After substantial rewrite, call the model **fly-inspired** ([[permanent/perm-20260912-anatomy-is-init-not-a-faithful-brain]]).

**P5 — Explain with interventions**

Lesion recurrent subcircuits ↔ delayed-cue. Perturb activity ↔ recovery. Retrain on rewires. Profile time and memory traffic (the real energy). Representational geometry ([[literature/lit-20260912-digital-sphinx]]) if behavior is ambiguous.

**P6 — Freeze and confirm**

Independent seeds, locked confirm split, unseen operational failures. Report unsuccessful configs. Only then consider Connectome-to-Function ([[literature/lit-20260912-connectome-to-function]]).

### Parallel tracks (do not block P0)

| Track | Owner | Status |
| --- | --- | --- |
| Motif distillation (EMD, loom, FlyHash) | frontier-kb claims; later a specialist port | Already the 10-agent consensus |
| Native LM (`fly-hf` vs matched non-connectome) | audit `trust_remote_code` before run | Parallel |
| Lab compiler (NeuronBridge → split-GAL4) | Drosophila labs | Not factory-first code |
| fly-wirehead / Stonkfly / Xenova | I/O remap + PAM current; choreographed swipe | Negative control / interface reference |
| PER-944 Xenova WebGPU | Linear Backlog | Browser viewer, not the student |

Viral apps (DOOMFLY, Flyhard, Tello, Stonkfly, fly-wirehead): useful as **pinout** references. Not evidence of learned preference, profitable trading, or Qwen-beating efficiency.

### Repo join (AODL network + this work)

| Repo | Owns in this program | Does not own |
| --- | --- | --- |
| [kvnloo/aodl](https://github.com/kvnloo/aodl) | \(\mathcal{O}_t\), ports, budgets \(\Gamma_t\), harness ids; proposed `fly-specialist-port` example | scheduler, training loop, MaleCNS arrays |
| [kvnloo/frontier-kb](https://github.com/kvnloo/frontier-kb) | claims, protocol, Pareto logs (this note) | runtime |
| [kvnloo/dash](https://github.com/kvnloo/dash) | orchestra pane **decodes** the graph; thesis-intent PR #38 | a second IR |
| [kvnloo/hermes-keel](https://github.com/kvnloo/hermes-keel) | L0: default router cannot do project work; controller never holds secrets | AODL schema |
| [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) | recovery events, Kanban, gateway; HOTL proposed at #88589 | fly student weights |
| [kvnloo/humanity-vault](https://github.com/kvnloo/humanity-vault) | teaching surface for the cluster | claims of truth |
| [kvnloo/fly-wirehead](https://github.com/kvnloo/fly-wirehead) | MaleCNS LIF playback, photoreceptor pinout, PAM11 20 mV, KC→MBON plasticity **assay** | learning result, Pareto claim |
| [kvnloo/verified-oss-loop](https://github.com/kvnloo/verified-oss-loop) | claim leases / evidence receipts when a Pareto point is asserted | schema |
| [kvnloo/blueprint](https://github.com/kvnloo/blueprint) / evolve / solarpunk | C(RAID) product loop; digital-twin **cores** | this fly graph (solarpunk twin ≠ MaleCNS upload) |

AODL kinds already allowed: `task`, `executor`, `model`, `tool`, `service`, `memory`, `stateStore`, `humanGate`, `environment`, `artifact`, `verifier`. **No `consciousness` kind.** Kardashev changes `constraints.budgets` (tokens, joules, spawn), not kinds. Fail-closed: image/video payload into a text-only specialist is invalid unless a vision child is bound ([[inbox/cursor/inbox-cursor-aodl-thesis-intent-20260912]]).

Proposed P0 graph (sketch, not yet an `examples/valid` file in aodl):

```text
environment:events  --OperationalEvent(sanitized)-->  executor:specialist
        --> tool:recovery_action --> verifier:outcome
        --unfamiliar--> model:qwen38_27b  (higher Γ)
        --policy hit--> humanGate
```

Qwen remains the language/tool worker ([[permanent/perm-20260912-fly-snn-is-sensorimotor-worker-not-svlm]]). The specialist is a **port**, not a planner swap ([[permanent/perm-20260912-fly-specialist-is-an-aodl-port]]).

### Reject list (carried forward)

- MaleCNS SGD as first code; SWE-bench as first score.
- FLM-style chat demo without direct-input.
- Relabel-without-refit as a topology control.
- Eon upload / 91% as embodied accuracy.
- Virtual patient / tau HTS.
- FlyWire@Loihi as green AI without joules.
- Inventing a second AODL spec in Dash or fly-wirehead.

## Fact vs interpretation

- Fact: FLM’s direct-input wins on language NLL; Costi’s topology+weights help chaotic forecasting; FlyGM trains a graph policy with rewire/MLP controls; Sphinx shows walking is not fidelity; fly-hf’s readout dominates params.
- Interpretation: P0 is a **harness** experiment (Hermes + AODL ports + verifier), not a neuroscience upload and not a 27B midpoint hunt. The 10-agent motif consensus is the likely P1 winner; the control table is how we would notice if we were wrong.
- HOLD: the 95%/50% product target is unregistered. CoS mints any Linear HITL; PER-944 stays a viewer.

## Links

- [[literature/lit-20260912-chatgpt-flyforge-share]]
- [[literature/lit-20260912-flm-and-fly-hf-language-reservoirs]]
- [[literature/lit-20260912-costi-connectome-reservoir]]
- [[literature/lit-20260912-digital-sphinx]]
- [[literature/lit-20260912-flygm-graph-policy]]
- [[literature/lit-20260912-connectome-to-function]]
- [[literature/lit-20260912-connectome-genuine-apps]]
- [[permanent/perm-20260912-p0-is-verified-hermes-recovery]]
- [[permanent/perm-20260912-direct-input-control-is-mandatory]]
- [[permanent/perm-20260912-joules-per-verified-success]]
- [[permanent/perm-20260912-fly-specialist-is-an-aodl-port]]
- [[permanent/perm-20260912-anatomy-is-init-not-a-faithful-brain]]
- [[inbox/cursor/inbox-cursor-flyforge-roadmap-20260912]]
- [[harnesses/hermes]]
