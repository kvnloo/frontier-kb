---
id: homebase-cycle-20260914-006-pareto-synthesis
title: "Cycle 6: six-cycle Pareto tradeoffs and next held-out experiment"
type: inbox
status: captured
created: 2026-09-14
updated: 2026-09-14
harnesses: [hermes]
domains: [physics, computer-science, simulation]
confidence: medium
tags: [homebase, digital-twin, pareto, research-cycle]
---

# Cycle 6 — Pareto synthesis (cycles 1–5) and next concrete experiment

## Question
After six substantive cycles, which **candidate tradeoffs** remain live for a local facility twin + multi-sport sim, and what is the **next held-out experiment** that can move a Pareto axis rather than re-cite vendor APIs?

## Hypothesis
**H1 (supported as program state):** Custom kernel necessity remains **unproven**. Evidence so far is **contracts and one CPython layout microbench**, not a Homebase FPS or scoring-correctness win. Keep charter hypotheses 1–3 competing.

**H2 (supported):** Responsibilities that must stay **separate** (do not collapse into one “kernel”):
- OS/GPU kernels vs **importer/scheduler** vs **sport domain** (score/possession/RNG/event log) vs **developer harness**.
- **Communication-point / snapshot contract** (FMI vocab) vs **frame tick groups**.
- **Contact localization** vs **CCD brand** vs **rules tape**.
- **Restorable Properties** vs **Telemetry** vs **opaque solver blobs**.
- **Job/ParallelFor schedulers** vs **SoA layout** vs **single-writer rules**.

**H3 (supported, limited):** On this host, **SoA serial AABB** beat AoS; **naive 2-thread CPython did not beat serial SoA**. Layout ≠ kernel replacement (cycle 5).

**H4 (refuted as already-established):** Scoreboard-updater independence (cycle 3 original) — **rejected**; fixture still called lifecycle-bearing `updateScoreboards`.

**H5 (untested; experiment not executed this cycle):** Held-out rally/net tape under `h ∈ {1/120, 1/60, 1/30}` or discrete vs TOI vs analytic segment-plane would discriminate multi-rate conservation (cycle 1) and event order (cycle 2). **Not executed:** load 6.30 / 5.79 / 6.08, Mem available ~7.2 Gi, swap 26 Gi occupied — charter prefers research-only under pressure; synthesis is the six-cycle deliverable.

## Host / experiment policy
Measured 2026-09-14 ~09:23 CDT: load **6.30 / 5.79 / 6.08**; Mem 23 Gi, ~7.2 Gi available, swap 26 Gi used. **Benchmark: not executed.** QMD: 0 collections (no index mutation).

## Pareto matrix (live candidates)

| Axis | Cheap candidate (H1: mature runtime) | Mid (H2: owned headless domain + thin adapter) | Costly (H3: custom runtime/renderer) | Evidence status |
|---|---|---|---|---|
| Multi-rate / fidelity | UE/Unity tick groups + min interval | FMI-style clocks, `DoStep` early return, complete-state get/set as **adapter contract** | Own scheduler+solver | Contracts only; conservation **unmeasured** (c1) |
| Contact → score | Engine CCD + discrete tests | Localize first-contact as **domain event**; one physics authority | Second physics kernel | CCD ≠ scoring oracle (c2); tape **unmeasured** |
| Ops restore | Replay/telemetry stream | DTDL-like Property snapshots ≠ Telemetry ≠ FMU blob | Full custom ops DB | Contracts (c4); round-trip **unmeasured** |
| Parallelism | Engine jobs/TaskGraph/WorkerThreadPool | SoA queries + **serial** score/possession/RNG | Custom ECS/runtime | Jobs = schedulers; SoA > AoS in CPython (c5) |
| Presentation coupling | Inert draw sinks | Observer-off continuation vs no-updater | Extract scoreboard subsystem | Independence claim **rejected** (c3) |

**Do not promote H3** until H1/H2 fail a pinned held-out gate on this host.

## Fact vs interpretation
- **Fact:** Cycles 1, 2, 4 used primary specs (FMI 3.0 2022-05-10; Jolt/Box2D/PhysX CCD docs; DTDL v3 / DDS 1.4). Cycle 5 executed AABB bench (sha256 `93ed9748255d27aedb6ca71e88d081ef6a6719ccaa3923f18195e4d9fb08755b`). Cycle 3 original independence claim failed verification.
- **Interpretation:** Pareto is **responsibility split**, not a single FPS number. Next value is a **pinned tape**, not another job-API citation.
- **Not fact:** Unreal won; FMI/Azure/DDS required; Burst/Jolt numbers; Homebase GPU FPS.

## Specified next experiment (cycle 7, execute only if loadavg-1m < 4 and Mem available > 8 Gi)

**Name:** held-out net/rally **event-order tape**, not a new physics engine.

**Pin:**
- Scenario: analytic **segment vs infinite plane** (net) vs discrete sample vs simple TOI along segment; seeds `{20260914, 20260915}`.
- Metrics: first-hit time agreement (abs err vs analytic), event **count**, **order** of (hit, bounce, score-credit placeholder), wall time.
- Held-out: seed+1 trajectories not used to tune thresholds.
- Limits: `timeout 120s`, 2 threads max, no GPU, artifact < 200 MiB under `inbox/chiefstaff-homebase/evidence/cycle-007-net-tape/`.
- **Do not** edit production Homebase sources; **do not** re-open cycle 3 updater APIs.

If load still high: retrieve one primary on **discrete-event facility ops vs ODE court** (not another CCD/jobs page).

## Decision
Keep H1–H3 of the charter. Treat cycles 1–5 as a **split of concerns**, not a kernel bake-off winner. **Next:** cycle 7 net/rally tape when host is idle; otherwise DES-vs-ODE literature only.

## Limitations
- No new primary HTTP this cycle (synthesis of already-cited URLs).
- No executed conservation/CCD/Property round-trip.
- CPython SoA is not C++/Burst.
- QMD empty; vault files used.

## Dedup
Does not re-fetch FMI/CCD/DTDL/jobs docs. Does not repeat cycle 3 updater claims. Architecture-research ECS shopping remains out of scope.

## URLs already in evidence (not re-retrieved)
- https://fmi-standard.org/docs/3.0/
- https://docs.unity3d.com/Manual/JobSystem.html
- https://dev.epicgames.com/documentation/en-us/unreal-engine/tasks-systems-in-unreal-engine
- https://raw.githubusercontent.com/godotengine/godot-docs/master/classes/class_workerthreadpool.rst
