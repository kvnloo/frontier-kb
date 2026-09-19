---
id: homebase-cycle-20260914-001-multirate-fmi
title: "Cycle 1: multi-rate twins vs FMI 3.0 and engine tick groups"
type: inbox
status: captured
created: 2026-09-14
updated: 2026-09-14
confidence: medium
tags: [homebase, digital-twin, multi-rate, fmi, research-cycle]
---

# Cycle 1 — multi-rate simulation and correctness-preserving fidelity transitions

## Question
Can a local facility digital twin plus playable multi-sport sim keep **score/physics invariants** across **rate changes** (ops DES vs court ODE vs display interpolation) without a full custom engine, by treating the **scheduler** as a first-class importer and **state snapshots** as the fidelity-transition API?

## Hypothesis
**H1 (supported in part):** Separate (1) discrete-event facility operations, (2) fixed-communication-step sport physics, (3) display interpolation. FMI 3.0 already names the contracts: Model Exchange vs Co-Simulation vs Scheduled Execution, clocks/partitions, `fmi3DoStep` early return, Intermediate Update Mode, and get/set of complete FMU state. A game-engine **tick group** is a **frame-phase** ordering, not a conservation-preserving multi-rate protocol.

**H2 (untested):** Adopting FMI-style communication points for pickleball RK4 + rules events would reduce scoring defects vs a single variable `dt` game loop. Not executed this cycle.

**H3 (not claimed):** Unreal already won; a custom kernel is required. Both remain unproven.

## Host / experiment policy
Measured 2026-09-14 ~00:35 CDT: load averages 13.59 / 14.28 / 17.39; Mem 23 Gi total, ~5.4 Gi available, swap occupied. Charter: under pressure, **research only**. Benchmarks: **not executed**.

## Evidence (primary)

### FMI 3.0 specification (Modelica Association)
- URL: https://fmi-standard.org/docs/3.0/
- Version header retrieved: **Functional Mock-up Interface Specification version 3.0, 2022-05-10**.
- Site: https://fmi-standard.org/ — FMI is a free standard (ZIP of XML + binaries/C); claimed support by 280+ tools; current complete package listed as **3.0.2** on the homepage (spec page fetched was 3.0).
- Interface types (ToC + “What is new”): **Model Exchange (ME)**, **Co-Simulation (CS)**, **Scheduled Execution (SE)**.
- CS additions vs 2.0 (spec “What is new”): early return from `fmi3DoStep`, Event Mode, Intermediate Update Mode, clocks/clocked variables; async CS from 2.0 **removed**.
- Notation: CS/SE communication points \(t_i\), step \(h_i = t_{i+1}-t_i\).
- Clocks: Clock Types, model partitions and clocked variables, clocks API (ToC 2.2.8).
- FMU state: “Getting and Setting the Complete FMU State” (ToC 2.2.7.4) — candidate **fidelity-transition snapshot**, not a guarantee of energy/score conservation.
- SE 5.1.1 (verbatim extract): importer must schedule partitions by activation time and **Clock `priority` (mandatory for SE)**; same-time ticks need a defined sequence; priorities are **local to an FMU**; importer must derive order across connected FMUs from local priorities and I/O; **periodic clocks: rate-monotonic scheduling recommended**.
- Smoothness/continuity of CS inputs (ToC 4.1.1) is specified; **no “conservation of energy/score” keyword** in the retrieved HTML (`conservation` / `multi-rate` string search: not present). FMI does **not** by itself prove pickleball rally correctness.

### Unreal Engine 5.8 actor ticking (Epic)
- URL: https://dev.epicgames.com/documentation/en-us/unreal-engine/actor-ticking-in-unreal-engine
- Page description: “Explanation of the ticking system used to update Actors each frame.”
- Actors/components tick once per frame unless a **minimum ticking interval** is set; groups: **TG_PrePhysics**, **TG_DuringPhysics** (physics may finish **during or after** this group), **TG_PostPhysics**, **TG_PostUpdateWork**.
- Multiple `FTickFunction`s and `AddPrerequisite` exist.
- This is **intra-frame phasing + optional skip interval**, not FMI communication-point semantics. **DuringPhysics** explicitly allows physics completion **after** the group — a source of off-by-one vs rules events if scoring reads transforms mid-group.

### Existing local audit (not re-run)
Charter: RK4 live; Magnus disconnected; net-serve credit, NVZ identity, rotation-dependent net collision. 1,170 engine tests green ≠ physical-event-to-score correctness. Architecture-research already lists engines; **this cycle does not repeat that matrix**.

## Fact vs interpretation
- **Fact:** FMI 3.0 publishes ME/CS/SE, clocks, early return, intermediate updates, FMU state snapshots (2022-05-10 spec text retrieved).
- **Fact:** UE 5.8 documents tick groups and min intervals, with DuringPhysics overlapping the physics solver.
- **Interpretation:** A Homebase **scheduler** should own communication points and event localization; the **sport domain** should expose snapshot + event-return; the **runtime** should interpolate for display only. That mapping is a design claim, not a measured win.
- **Not fact:** FMI import of the current TypeScript kernel, or that SE is cheaper than a thin C++ domain layer.

## Competing next experiments (when load/RAM allow; max 120s, 2 threads, 1 GiB, no GPU)
1. **Held-out rally tape:** replay N recorded contact times at physics `h` ∈ {1/120, 1/60, 1/30} vs event-localized (early-return analog). Metrics: score identity vs baseline tape, energy drift of free-flight RK4, wall time. Do not change acceptance tests.
2. **Two-clock toy:** periodic court ODE clock + Poisson facility HVAC/booking events; assert no double-credit of a net event when ops clock is 1 Hz and physics is 120 Hz.
3. **Snapshot round-trip:** serialize analog of FMU state at rate change; restore; compare bit-stable or ε-ball on position/velocity (not FPS).

## Decision
Keep **three hypotheses of the charter**. Promote **scheduler vs domain vs renderer** as the unit of comparison, not “Unreal vs custom kernel.” FMI 3.0 is a **contract vocabulary** for multi-rate + snapshots; UE tick groups are **not** that contract. **Do not** wrap the live pickleball kernel in FMI this cycle (no installs).

## Limitations
- arXiv API 429; Godot physics-interpolation URL 404/not fetched; later curl blocked — Godot not cited.
- Spec HTML ToC-heavy; some section bodies collapsed; homepage 3.0.2 vs fetched 3.0 page.
- No CPU experiment; no conservation numbers.
- FMI license/tool chain not compiled.

## Next angle
When host load < ~4 and available RAM > ~8 GiB: experiment 1 (held-out rally tape, score identity vs `h`). Else: **authoritative event ordering / continuous collision vs discrete net tests** from primary physics sources, still no GPU.

## Dedup
Does not repeat architecture-research engine table. Cycle 0 decision.tsv only posed “is custom kernel necessary?”
