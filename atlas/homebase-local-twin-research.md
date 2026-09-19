---
id: homebase-local-twin-research
title: "Homebase local digital twin kernel research program"
type: atlas
status: active
created: 2026-09-14
updated: 2026-09-14
harnesses: [hermes]
domains: [physics, computer-science, simulation]
confidence: medium
tags: [homebase, digital-twin, autoresearch]
---

# Homebase local digital twin research

## User objective
Run the whole facility digital twin and playable multi-sport simulation on the user's PC. Research beyond conventional game-engine selection, including a custom simulation kernel and autoresearch-driven optimization across the development pipeline. Custom kernel necessity is a hypothesis, not an established conclusion. Local game execution is required; local-only research inference has not been specified.

## Verified starting evidence
Canonical product: /mnt/zer0models/workspace/zer0/products/homebase-pickleball. Dedicated worktree: /workspace/wt/homebase-engine-2026. Not pickleball-palace-builder, not GrowTwin.

Audit reports preserved in [[inbox/chiefstaff-homebase/branches]], [[inbox/chiefstaff-homebase/runtime]], [[inbox/chiefstaff-homebase/architecture-research]]. Original evidence and harnesses remain in /workspace/wt/homebase-engine-2026/docs/engine-audit/.

- 209 refs, 105 distinct commits, one committed src/engine tree. GitNexus indexed 13/100 integration groups and two dirty snapshots; 87 integration combinations not graph-indexed. All discovered engine/test variants covered. One remote fetch failed; cached refs included.
- RK4 gravity/drag is live. Default spin/Magnus is disconnected. Automated exhibition, not athlete-controlled gameplay. No authoritative multiplayer transport established.
- Executed defects: net serve can credit server; NVZ athlete identity mismatch; net collision changes under equivalent court rotation; inconsistent optional rally scoring.
- Engine tests: 1,170 passed. Full suite: 2,320 passed, two failed, one unhandled error. Engine typecheck/build passed; lint failed. Green isolated tests do not establish physical-event-to-score correctness.
- Microbenchmarks: median 1.304 microseconds/free-flight RK4 step; roughly 4,236 headless rules games/s excludes physics/rendering. Browser roughly 13.34 FPS used software rendering, not GPU performance.
- No production code migration or official 2026 rulebook conformance pass completed.

## Host snapshot, not a permanent budget
2026-09-14: i9-10900KF, 10 cores/20 threads; RTX 3080 Ti, 12,288 MiB VRAM; 23 GiB usable RAM, about 5.9 GiB available, 28 GiB swap occupied. /workspace about 122 GiB free. Re-measure before experiments. Do not stop other workloads or infer active swapping from occupancy alone.

## Competing hypotheses
1. Mature runtime with simulation LOD, selective updates, streaming and sport modules is sufficient.
2. Game-owned native headless simulation kernel plus a thin runtime adapter improves locality, reproducibility and multi-sport reuse enough to justify ownership.
3. A broader custom runtime/renderer is necessary. Require evidence that targeted changes and existing runtimes cannot meet the budget before promoting this costly path.

Do not conflate OS kernel, GPU compute kernel, game-loop scheduler, physics solver, domain simulation, and developer optimization harness.

Cycle 1 synthesis ([[inbox/chiefstaff-homebase/cycle-20260914-001-multirate-fmi]]): FMI 3.0 (2022-05-10) names ME / Co-Simulation / Scheduled Execution, clocks with importer-owned priorities, `fmi3DoStep` early return, Intermediate Update, and full FMU state get/set. That is a **contract** for multi-rate communication points and snapshots, not a measured Homebase kernel. Unreal 5.8 tick groups (Pre/During/PostPhysics, min interval) are **frame-phase** ordering; DuringPhysics may complete after the group. Score/energy conservation at rate change is **unmeasured** (host load precluded the 120s experiment).

Cycle 2 synthesis ([[inbox/chiefstaff-homebase/cycle-20260914-002-ccd-event-order]]): Jolt Discrete tunnels thin colliders; LinearCast CastShape **time-steals** and still misses **rotational** sweeps. Box2D TOI is tunnel-prevention (esp. vs statics) and may miss final-position hits. PhysX CCD default one pass **drops time after first TOI**; trigger shapes skip CCD; multi-pass can multi-bounce in one step. Engine CCD ≠ authoritative sport event log. Contact localization unmeasured on Homebase (load ~9).

Cycle 4 synthesis ([[inbox/chiefstaff-homebase/cycle-20260914-004-dtdl-snapshot-vs-telemetry]]): DTDL v3 Properties have backing storage and sync metadata; Telemetry is an emitted stream without that restore contract. Components are by-value (no independent identity); Relationships are by-reference DTMIs. FMI complete FMU state remains an opaque blob (cycle 1), not a typed ops graph. DDS 1.4 is pub/sub QoS, not snapshots. Unreal Replay docs were a bot-check stub this cycle and are not evidence. Snapshot round-trip unmeasured (load ~11).

Cycle 5 synthesis ([[inbox/chiefstaff-homebase/cycle-20260914-005-jobs-soa-locality]]): Unity 6.6 jobs (work stealing, ParallelFor over NativeArray), UE 5.8 Tasks (DAG on TaskGraph workers), and Godot WorkerThreadPool (group tasks + wait; array size frozen) are **schedulers**, not scoring or Property restore. Executed CPython AABB bench (N=4000, seed 20260914): SoA median **0.371 s** vs AoS **0.517 s**; 2-thread private **0.377 s** (GIL); overlap counts **7580** and held-out **1868** agreed. Layout ≠ kernel replacement.

Cycle 6 Pareto ([[inbox/chiefstaff-homebase/cycle-20260914-006-pareto-synthesis]]): Keep H1–H3. Live splits: FMI **contract** vs tick groups; CCD ≠ scoring oracle; Property restore ≠ Telemetry ≠ opaque blobs; jobs ≠ SoA queries ≠ serial rules writers; scoreboard independence **rejected**. Do not promote custom runtime until a pinned held-out tape fails H1/H2. Conservation/CCD/Property round-trips remain **unmeasured**. Cycle 7: net segment-plane vs discrete vs TOI if loadavg-1m < 4.

Cycle 7 synthesis ([[inbox/chiefstaff-homebase/cycle-20260914-007-des-vs-ode]]): Modelica 3.6 requires **sample/hold** between continuous plant and clocked partitions; `when` bodies are not evaluated during continuous integration. Ptolemy II assigns **DE vs continuous-time** to distinct hierarchical **directors**, not one stepper. DEVS is timed-event vocabulary (Wikipedia secondary). Net/rally tape **not executed** (load 5.59/12.03/15.42; Mem ~6.2 Gi available). Keep H1–H3; DES ops vs ODE court is a contract split, not a kernel bake-off.

Cycle 8 synthesis ([[inbox/chiefstaff-homebase/cycle-20260914-008-qss-vs-timestep]]): Kofman & Junco 2001: QSS is **state quantization with hysteresis**, exactly DEVS; Lipschitz **Theorem 6** convergence as quantum → 0. Dual of time-step ODE, not a scoring oracle. retQSS maps particle–mesh **state-events** to **time-events**. IEEE 1516.1 HTML served **IEEE 1302-2019** (discarded). Tape **not executed** (Mem ~6.4 Gi < 8 Gi). Keep H1–H3.

Cycle 9 synthesis ([[inbox/chiefstaff-homebase/cycle-20260914-009-anim-lod-vs-authority]]): UE 5.8 Animation Budget Allocator **throttles skeletal ticking** to a **game-thread ms budget** (lower rate, interpolate, stop tick). Unity 6 **Cull Completely** disables animation when renderers are not visible; **Animate Physics** couples Animator to FixedUpdate. glTF 2.0 samplers interpolate **LINEAR/STEP/CUBICSPLINE** between keys — not RK4/TOI. HLA 1516 TM still unverified. Tape **not executed** (load 10.64; Mem ~5.9 Gi). Keep H1–H3; visibility must not write score.

Cycle 10 synthesis ([[inbox/chiefstaff-homebase/cycle-20260914-010-autotune-judge-vs-streaming]]): OpenTuner (PACT 2014) **SearchDriver writes DesiredResults; user Measurement writes Results** via a results DB — search must not own the judge. Published GCC tuner **allowed `-ffast-math`** (FP change). UE 5.8 Nanite **camera-view cluster streaming**; ray tracing uses **Fallback Mesh** by default. USD 26.08 **Payload LoadNone** working set; **Purpose/Visibility** are render traversal gates. Tape **not executed** (load 4.53; Mem ~5.7 Gi). Keep H1–H3.

Cycle 11 synthesis ([[inbox/chiefstaff-homebase/cycle-20260914-011-collision-vs-render-mesh]]): UE 5.8 **Simple vs Complex Collision** — hulls/primitives vs **trimesh**; **UseComplexAsSimple cannot simulate** that body (static collider vs other simple dynamics). Jolt **MeshShape mostly static**, **HeightField static**, MeshShape **needs supplied inertia**. Collision Complexity is **not** Nanite cluster streaming (cycle 10). Tape **not executed** (load 10.74; Mem ~6.2 Gi). Keep H1–H3; pin authored collision off render LOD.

Cycle 12 Pareto ([[inbox/chiefstaff-homebase/cycle-20260914-012-pareto-synthesis]]): Keep H1–H3. Live splits after 7–11: DES ops ≠ ODE court; QSS ≠ scoring; anim LOD/cull ≠ authority; SearchDriver ≠ judge; streamed/Purpose mesh ≠ authored collision; simple/complex ≠ Nanite. Cycle 5 SoA AABB remains the only executed bench. Conservation/CCD/Property RT **unmeasured**. Cycle 13: net tape if loadavg-1m < 4 and Mem > 8 Gi; else dissipative work/energy or FMI get/set (not HLA HTML).

## Research angles
- Multi-rate simulation, event-driven/discrete-event facility operations, sleeping entities, spatial partitioning and fidelity transitions with state conservation.
- Data-oriented layout, jobs/task scheduling, incremental computation, cache locality, SIMD, allocation control; ECS only if earned.
- Sports contact/flight/possession, continuous collision, calibrated parameters, temporal rules and authoritative event ordering.
- Local digital twin state, provenance, coordinate/asset semantics, offline persistence, optional telemetry reconciliation and uncertainty. Never publish facility addresses/coordinates.
- Render streaming, visibility, animation LOD, instancing, GPU/CPU budgets and asset-build iteration.
- Native runtimes, mature OSS simulation/co-simulation libraries, game research papers, commercial production talks, and existing local autoresearch tools. Verify licenses and actual shipped/buildable status.
- Autoresearch methodology: constrained Pareto optimization, held-out scenes/seeds, paired repeated measurements, uncertainty, anti-Goodhart tests, reproducible manifests.

## First-principles complexity extension

User-requested bounded cycle: [[inbox/chiefstaff-homebase/first-principles-complexity-charter]]. Ask what can be removed or derived while preserving causal correctness and human outcomes. Compare current bridges, single-owner session with thin adapters, runtime-native ownership, and broader event/ECS machinery; do not presume a universal kernel wins. Use sequential mathematical, physical, causal, informational, perceptual, maintenance, epistemic and human-benefit lenses, followed by an adversarial pass. First concrete discriminator is whether removing scoreboard projection changes domain lifecycle. Subsequent cycles choose one unresolved simplification hypothesis, not repeated philosophical essays. Existing resource, evidence and no-production-promotion constraints remain in force.

## Acceptance and workflow
Research is ongoing, not a promise to invent a superior engine. Each cycle selects one unresolved question, gathers primary evidence or runs a small experiment, and records support/refutation, limitations and next action. Keep a candidate matrix and decision.tsv. Pivot on plateau rather than repeating searches.

A performance win requires unchanged correctness/calibration constraints, comparable target-hardware measurements, repeated samples, and a relevant workload. Do not optimize FPS by silently reducing facility occupancy, physical fidelity, input responsiveness or visual quality. Keep a Pareto frontier, not one universal score. Separate training/calibration, validation and held-out workloads; do not let optimizer rewrite acceptance tests.

Near-term exit gate: reproducible baseline scenarios and resource budgets, evidence-backed candidate comparison, and at least one verified improvement or reproducible disqualification. If reached, select the next unresolved angle rather than declaring the whole program solved. Publish a synthesis after each six substantive cycles. Do not merge or deploy automatically.

## Resource and write policy
One serial research worker, every two hours. Small CPU experiments only initially, at most two workers/threads and 120 seconds per experiment, under 1 GiB incremental memory and 200 MiB new artifacts per cycle. Prefer timeouts and enforced process limits where available. No GPU training, large model downloads, engine installs/builds, paid services or external publication without separate authorization. Under memory pressure perform source research only. Never kill other workloads.

Write only this atlas and inbox/chiefstaff-homebase/ for this program; prototypes may live in the dedicated engine worktree's research sandbox without editing production sources. Preserve existing dirty work. No commits/pushes/merges. Source access failures are blockers, not permission to fabricate results. Scheduler output is local, not chat delivery.
