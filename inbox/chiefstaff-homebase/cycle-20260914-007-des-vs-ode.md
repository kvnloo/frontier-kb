---
id: homebase-cycle-20260914-007-des-vs-ode
title: "Cycle 7: discrete-event facility ops vs ODE court (literature; tape deferred)"
type: inbox
status: captured
created: 2026-09-14
updated: 2026-09-14
harnesses: [hermes]
domains: [physics, computer-science, simulation]
confidence: medium
tags: [homebase, digital-twin, des, ode, hybrid, research-cycle]
---

# Cycle 7 — DES facility operations vs ODE court physics

## Question
Must **facility operations** (booking, occupancy, HVAC/setpoints, session start/stop) run as a **discrete-event** clock domain, separate from **ODE/DAE court physics**, or is one engine tick group enough?

## Hypothesis
**H (tested):** Heterogeneous models of computation — discrete-event (timed events, no work between events) vs continuous-time (integrator / state events) — are **not interchangeable**. Crossing them without explicit **sample/hold** (or a director boundary) is a modeling error in primary specs. This does **not** by itself require a custom Homebase kernel (charter H1–H3 remain competing).

**Avoid:** Re-citing FMI 3.0 clocks vs Unreal tick groups (cycle 1); CCD brands (cycle 2); DTDL Property vs Telemetry (cycle 4); job APIs (cycle 5).

## Host
Measured 2026-09-14 ~11:25 CDT: load **5.59 / 12.03 / 15.42**; Mem 23 Gi, ~6.2 Gi available, swap 26 Gi used. Cycle 6 gate was **loadavg-1m < 4 and Mem available > 8 Gi** for the net/rally tape. **Not met → experiment not executed.** QMD: 0 collections; no index mutation.

## Primary sources retrieved

Retrieved (full pages, not snippets-only):
- Modelica Language Specification 3.6 ch. 16: https://specification.modelica.org/maint/3.6/synchronous-language-elements.html
- Modelica 3.6 ch. 8 Equations (state/time events, `when`, `noEvent`): https://specification.modelica.org/maint/3.6/equations.html
- Ptolemy II home (directors / MoC): https://ptolemy.berkeley.edu/ptolemyII/index.htm
- DEVS summary (secondary; formalism name only): https://en.wikipedia.org/api/rest_v1/page/summary/DEVS

**IEEE 1516 HLA time management:** `https://standards.ieee.org/ieee/1516/7343/` resolved to unrelated **IEEE C57.168-2023** HTML; **discarded** (wrong document). arXiv API returned empty bodies this cycle.

### Modelica 3.6 — clocks vs continuous plant
Ch. 16: synchronous clocked semantics exist so a **continuous plant** and a **sampled controller** connect only via **`sample`** (continuous → clocked) and **`hold`** (clocked → continuous). Clocked variables “can only be directly accessed when the associated clock is active”; mixing clocks in one equation requires explicit casts. `Clock(3)` sets a sampling interval. This is a **compiler-checked partition**, not a game-loop comment.

Ch. 8: `when`-bodies are **not** evaluated during continuous integration; relations inside `when`/`noEvent` do not induce state or time events. `smooth`/`noEvent` exist specifically to **avoid state-event iteration** when continuity is guaranteed. Non-discrete-time `when` conditions are specified as errors.

### Ptolemy II — directors, not one kernel
Ptolemy II (Java framework; v11.0 dated 2018-06-19 on the retrieved page): model semantics come from a **director** implementing a model of computation. Directors include **discrete-events (DE)** and **continuous-time**, plus PN, SDF, SR. “Each level of the hierarchy in a model can have its own director, and distinct directors can be composed hierarchically.” Continuous-time + state machines → **hybrid systems** (HyVisual). Interoperability is via **actor abstract semantics**, not a single ODE stepper.

### DEVS (secondary)
Wikipedia extract (2026-08-14 revision): DEVS is a **timed event** modular/hierarchical formalism covering discrete-event, continuous (ODE-described), and hybrid systems. Use as **vocabulary**, not a shipping Homebase dependency. ASU ACIMS `/devs/` returned **404**.

## Support / refute
- **Supported:** Facility-scale **ops** (sparse events: court assigned, session ends, HVAC setpoint) match **DE / clocked / when** domains; in-play ball flight matches **continuous / ODE** with **state events** at contacts. Crossing without `sample`/`hold` or a director boundary is ill-typed in Modelica and unowned in Ptolemy.
- **Supported:** This is a **scheduler/domain split**, same family as cycle 1 FMI communication points — but **DES vs ODE**, not ME vs tick groups.
- **Not supported:** Need to rewrite Homebase in Modelica, Ptolemy, or DEVS. Need a custom renderer. One tick group is “wrong” as implementation — only **insufficient as the contract**.
- **Refuted for this cycle:** That idle-host net tape would run (loadavg-1m 5.59 ≥ 4).

## Fact vs interpretation
- **Fact:** Quoted Modelica 3.6 sample/hold and `when`/state-event rules; Ptolemy II director list and hierarchical composition.
- **Interpretation:** Homebase should keep **ops event queue** and **physics stepper** as separate clocks with explicit conversion, even if both sit inside Unity/UE/custom.
- **Not fact:** HLA time management; arXiv QSS papers; measured conservation across DES↔ODE.

## Benchmark provenance
**not executed** (host gate). No artifact under `evidence/cycle-007-*`.

## Decision
Keep charter H1–H3. Treat **DES ops vs ODE court** as a live Pareto axis: cheap path = engine timers + physics tick with **explicit** conversion; mid path = owned event calendar + RK4/CCD domain; costly path = Ptolemy/Modelica-like multi-director runtime. **Do not** promote H3. **Next:** execute cycle-6 **net/rally tape** when loadavg-1m < 4 and Mem available > 8 Gi; else **HLA 1516 time-management from a verified PDF** or **QSS/quantized-state** primary if HTTP works.

## Limitations
- Wikipedia DEVS is secondary.
- Ptolemy landing page, not the design-doc PDF.
- Modelica is DAE/control-oriented; sports contact/scoring not specified there.
- FMI 3.0 not re-fetched (cycle 1).
- Load still elevated; 15-min load 15.42.

## Dedup
Does not re-fetch FMI/CCD/DTDL/jobs. Does not claim scoreboard independence. Does not run AABB again.

## URLs
- https://specification.modelica.org/maint/3.6/synchronous-language-elements.html
- https://specification.modelica.org/maint/3.6/equations.html
- https://ptolemy.berkeley.edu/ptolemyII/index.htm
- https://en.wikipedia.org/api/rest_v1/page/summary/DEVS (secondary)
- Discarded: https://standards.ieee.org/ieee/1516/7343/ (wrong IEEE page)
