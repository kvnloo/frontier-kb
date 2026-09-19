---
id: homebase-cycle-20260914-012-pareto-synthesis
title: "Cycle 12: Pareto synthesis of cycles 7–12 and next held-out experiment"
type: inbox
status: captured
created: 2026-09-14
updated: 2026-09-14
harnesses: [hermes]
domains: [physics, computer-science, simulation]
confidence: medium
tags: [homebase, digital-twin, pareto, research-cycle]
---

# Cycle 12 — Pareto synthesis (cycles 7–11) and next concrete experiment

## Question
After six more substantive cycles (7–11 plus this synthesis), which **candidate tradeoffs** remain live for a local facility twin + multi-sport sim, and what is the **next held-out experiment** that can move a Pareto axis rather than re-cite vendor APIs?

## Hypothesis
**H1 (supported as program state):** Custom kernel necessity remains **unproven**. Cycles 7–11 are **contracts and docs**, not a Homebase FPS or scoring-correctness win. Keep charter hypotheses 1–3 competing.

**H2 (supported):** Additional responsibility splits (do not collapse into one “kernel”):
- **DES / clocked ops** vs **continuous-time court ODE** (Modelica sample/hold; Ptolemy directors) — not one tick group.
- **QSS / state quantization** vs **uniform dt RK4** — dual of time-step, not a scoring oracle.
- **Animation LOD / cull / key interpolation** vs **authoritative contact/score**.
- **SearchDriver / autotune** vs **frozen Measurement/judge**; **streamed render working set** vs **authored collision**.
- **Simple vs complex collision** vs **Nanite/USD render mesh**; Jolt **MeshShape/HeightField static**.

**H3 (unchanged, limited):** Cycle 5 CPython SoA AABB remains the only executed microbench in this program. Cycles 7–11: **experiment not executed**.

**H4 (still rejected):** Scoreboard-updater independence (cycle 3 original).

**H5 (untested; not executed this cycle):** Held-out net/rally tape (analytic segment-plane vs discrete vs TOI). Gate **loadavg-1m < 4 and Mem available > 8 Gi** **failed** (load **5.47 / 8.96 / 9.29**, MemAvailable **~5.6 Gi**).

## Host / experiment policy
Measured 2026-09-14 ~21:46 CDT: load **5.47 / 8.96 / 9.29**; Mem 23 Gi, ~5.6 Gi available, swap 36 Gi used of 151 Gi. **Benchmark: not executed.** QMD: 0 collections (no index mutation). No GPU, no installs, no kb_store ingest, no DSN read, no production edits.

## Pareto matrix (cycles 7–11, stacked on cycle 6)

| Axis | Cheap (H1 mature runtime) | Mid (H2 headless domain + adapter) | Costly (H3 custom runtime) | Evidence status |
|---|---|---|---|---|
| Ops vs court time | Engine tick + timers | Modelica sample/hold; Ptolemy DE vs CT directors | Own hybrid kernel | Contracts (c7); tape **unmeasured** |
| Integrator | Fixed dt RK4 (live Homebase) | QSS/LIQSS/retQSS as **optional** solver | Replace scoring with DEVS | Dual of dt, not score (c8) |
| Animation | Engine budget/cull | Anim off scoring path; interpolate presentation | Custom anim kernel | UE budget + Unity Cull Completely (c9) |
| Autotune / streaming | Engine Nanite/USD load | Search ≠ judge; Purpose/Visibility ≠ collision | Autotune Collision Complexity | OpenTuner split; USD LoadNone (c10) |
| Collision vs render | Authored simple/complex | Pin collision off Nanite clusters | Second mesh authority | UE 5.8 flags; Jolt MeshShape static (c11) |
| Multi-rate / CCD / restore / jobs | (cycle 6 rows still live) | FMI / domain event / Property / SoA serial | Custom | Conservation/CCD/Property RT **still unmeasured** |

**Do not promote H3** until H1/H2 fail a pinned held-out gate on this host.

## Fact vs interpretation
- **Fact:** Cycles 7–11 retrieved primary or official docs (Modelica 3.6, Ptolemy directors, Kofman&Junco 2001, UE 5.8 anim budget / Nanite / simple-vs-complex, Unity Cull Completely, OpenTuner PACT 2014, USD 26.08, Jolt Doxygen). HLA 1516 HTML repeatedly served the **wrong document** (IEEE 1302) — discarded. Jolt architecture HTML and whitepaper **404**.
- **Interpretation:** Second six-cycle block is still **split of concerns**. Next value is the **pinned net tape**, not HLA retries or another mesh page.
- **Not fact:** Unreal won; QSS faster on Homebase; Nanite writes Chaos; MeshShape is a scoring log.

## Specified next experiment (cycle 13, execute only if loadavg-1m < 4 and Mem available > 8 Gi)

**Name:** held-out net/rally **event-order tape** (unchanged from cycle 6; still the discriminating experiment).

**Pin:**
- Scenario: analytic **segment vs infinite plane** (net) vs discrete sample vs simple TOI along segment; seeds `{20260914, 20260915}`.
- Metrics: first-hit time agreement (abs err vs analytic), event **count**, **order** of (hit, bounce, score-credit placeholder), wall time.
- Held-out: seed+1 trajectories not used to tune thresholds.
- Limits: `timeout 120s`, 2 threads max, no GPU, artifact < 200 MiB under `inbox/chiefstaff-homebase/evidence/cycle-013-net-tape/`.
- **Do not** edit production Homebase sources; **do not** re-open cycle 3 updater APIs; **do not** autotune Collision Complexity.

If load still high: one **new** primary — **energy/work balance for dissipative bounce** (cycle 1 conservation still unmeasured) **or** FMI 3.0 get/set FMU state round-trip **spec** (not Azure), **not** another HLA HTML fetch.

## Decision
Keep H1–H3 of the charter. Treat cycles 7–11 as **further splits**, not a kernel winner. **Next:** cycle 13 net/rally tape when host is idle; otherwise dissipative conservation or FMI snapshot contract (not HLA HTML).

## Limitations
- No new primary HTTP this cycle (synthesis).
- No executed conservation/CCD/Property round-trip since cycle 5 AABB.
- Host still under pressure; swap occupied.
- QMD empty; vault files used.

## Dedup
Does not re-fetch FMI/CCD/DTDL/jobs/QSS/anim/Nanite/simple-vs-complex. Does not repeat cycle 3 updater claims. Does not treat IEEE 1302 as HLA 1516.

## URLs already in evidence (not re-retrieved)
- https://specification.modelica.org/maint/3.6/synchronous-language-elements.html
- https://ptolemy.berkeley.edu/publications/papers/08/OverviewPtolemyII/
- https://www.fceia.unr.edu.ar/dsf/PDF/KofmanJunco.pdf
- https://dev.epicgames.com/documentation/en-us/unreal-engine/animation-budget-allocator-in-unreal-engine
- https://docs.unity3d.com/Manual/class-Animator.html
- https://opentuner.org/
- https://dev.epicgames.com/documentation/en-us/unreal-engine/simple-versus-complex-collision-in-unreal-engine
- https://jrouwe.github.io/JoltPhysics/
