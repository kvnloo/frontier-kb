---
id: homebase-cycle-20260914-005-jobs-soa-locality
title: "Cycle 5: job schedulers vs SoA locality vs shared-score writers"
type: inbox
status: captured
created: 2026-09-14
updated: 2026-09-14
harnesses: [hermes]
domains: [computer-science, simulation]
confidence: medium
tags: [homebase, digital-twin, jobs, data-locality, research-cycle]
---

# Cycle 5 — jobs/task graphs do not replace partitioned domain writes

## Question
Can engine **job / ParallelFor / worker-pool** APIs be treated as a facility-twin kernel (or a reason to replace the runtime), or must **data layout, exclusive writes, and reduction** be measured independently of the scheduler brand?

## Hypothesis
**H1 (supported as vendor contract, not a Homebase FPS claim):** Unity 6.6 documents a native job system with **worker threads sized to CPU cores**, **work stealing**, **ParallelFor** over a `NativeArray` (`IJobParallelFor.Execute(int index)` once per element), optional Burst, and a **safety system**. Jobs are scheduled work units, not sport authority or Property restore.[1][2]

**H2 (supported as vendor contract):** Unreal Engine 5.8 **Tasks System** is a job manager over the same backend as **TaskGraph**: launch callable, wait/result, **DAG prerequisites**, nested tasks (parent incomplete until nested complete), pipes, task events, priorities. It does not define contact identity, scoring, or DTDL Properties.[3]

**H3 (supported as vendor contract):** Godot `WorkerThreadPool` allocates startup worker threads; **group tasks** run a Callable many times (e.g. arena enemies). Official sample **waits for group completion** before dependent code; docs require the iterated array **size remain constant** during the parallel section; cheap tasks can **hurt** performance.[4]

**H4 (executed microbenchmark, limited):** On this host, **SoA AABB pair tests beat AoS** (~0.371 s vs ~0.517 s median, N=4000, CPython 3.11, 5 samples after warmup). **Two threads with private counts did not beat serial SoA** (median 0.377 s) — GIL-bound. All four methods agreed on **7580** overlaps; held-out N=4500 seed+1 agreed on **1868**. Layout mattered more than naive threading **in this interpreter**. This is **not** Burst/C++/Jolt, not Homebase physics, not a kernel win.[5]

**H5 (nearby-wrong, refuted as sufficient):** “Add a job system / ECS and the twin scales” — schedulers still need **partitioned writes**. A shared locked counter did not help here; Unity/Godot/UE all require the caller to own data races. Parallel overlap tests ≠ parallel score/possession/RNG updates (cycles 2–4).

## Host / experiment policy
Measured 2026-09-14 ~07:19–07:25 CDT: load **~1.83 / 3.79 / 4.59** during bench (earlier cycle start load ~3.16 / 4.97 / 5.05); Mem 23 Gi, ~7.4 Gi available. Experiment **executed** under 120 s, 2 threads, RSS ~17→20 MiB.

## Evidence (primary)

### Unity 6.6 job system
- URL: https://docs.unity3d.com/Manual/JobSystem.html [1]
- URL: https://docs.unity3d.com/Manual/JobSystemOverview.html [2]
- URL: https://docs.unity3d.com/Manual/JobSystemParallelForJobs.html [2]
- Retrieved 2026-09-14. Built from job ID 75330297, 2026-09-13. Worker threads vs main thread; work stealing; ParallelFor batches `Execute` per index on `NativeArray`; Burst recommended; ECS optional pairing.

### Unreal Engine 5.8 Tasks System
- URL: https://dev.epicgames.com/documentation/en-us/unreal-engine/tasks-systems-in-unreal-engine [3]
- DAG of dependent tasks; same scheduler/workers as TaskGraph; `Launch` + `FTask` / `TTask<ResultType>`; priorities high/normal/background; nested tasks; pipes.

### Godot WorkerThreadPool (engine docs RST)
- URL: https://raw.githubusercontent.com/godotengine/godot-docs/master/classes/class_workerthreadpool.rst [4]
- Generated from `doc/classes/WorkerThreadPool.xml`. Group vs regular tasks; `wait_for_group_task_completion`; constant element count during parallel section.

### Local bench
- Path: `inbox/chiefstaff-homebase/evidence/cycle-005-jobs/bench.json`
- sha256: `93ed9748255d27aedb6ca71e88d081ef6a6719ccaa3923f18195e4d9fb08755b`
- Scenario: synthetic AABB naive pairs; seed 20260914; not a contact/scoring oracle.

| method | median_s | overlap_count |
|---|---|---|
| aos_serial | 0.5165 | 7580 |
| soa_serial | 0.3706 | 7580 |
| soa_2thread_private | 0.3770 | 7580 |
| soa_2thread_locked | 0.3797 | 7580 |

Held-out N=4500: soa_serial 0.494 s, soa_2thread 0.463 s, aos 0.642 s; count 1868 all agree.

## Fact vs interpretation
- **Fact:** Unity/UE/Godot document job DAGs or ParallelFor over arrays, plus wait/completion barriers.[1][3][4]
- **Fact:** This cycle's SoA serial beat AoS; 2 CPython threads did not beat SoA serial; counts matched including held-out.[5]
- **Interpretation:** Measure **broadphase layout** separately from **rules/score writers** and from **draw**. Do not replace an engine to obtain a thread pool. Do not treat GIL Python as evidence that C++ jobs cannot scale.
- **Not fact:** Homebase FPS; Burst/SIMD numbers; that ECS is required; custom kernel necessity.

## Decision
Keep hypotheses 1–3 of the charter. **Job APIs are schedulers**, not restore graphs (cycle 4) and not scoring oracles (cycle 2). Prefer **SoA/partitioned reductions for independent queries**; keep **serial (or single-writer) rule/possession/RNG**. No engine replacement on this evidence.

## Limitations
- CPython GIL; 2-thread result is expected non-scaling, not a C++ disproof.
- Naive O(N²) pairs, not sweep-and-prune / BVH.
- Locked path had few contended hits (7580 vs ~8e6 tests), so lock cost was under-stressed.
- No GPU, no installs, no production edits.
- QMD had **0 collections** this host; search used vault files + HTTP primaries.

## Next angle
Cycle 6 should **synthesize Pareto** (cycles 1–5) plus one concrete next experiment: **held-out rally/net tape** (h={1/120,1/60,1/30} or discrete vs TOI vs segment-plane) **or** a **C-level/ctypes** 2-thread SoA overlap without GIL if load allows. Do not re-run cycle 3 updater claims.

## Dedup
Does not repeat FMI clocks (1), CCD/TOI (2), scoreboard verification (3), or DTDL Property vs Telemetry (4). Architecture-research listed EnTT/Flecs as optional ECS — this cycle tests **jobs vs layout vs shared writers**, not ECS shopping.
