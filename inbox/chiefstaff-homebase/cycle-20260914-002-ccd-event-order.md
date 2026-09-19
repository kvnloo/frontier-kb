---
id: homebase-cycle-20260914-002-ccd-event-order
title: "Cycle 2: discrete net tests vs CCD/TOI event localization"
type: inbox
status: captured
created: 2026-09-14
updated: 2026-09-14
confidence: medium
tags: [homebase, digital-twin, ccd, toi, contact, research-cycle]
---

# Cycle 2 — continuous collision vs discrete net tests

## Question
Does **authoritative event ordering** for sport contacts (net, NVZ, court lines) require **time-of-impact (TOI) / linear-cast CCD**, or can discrete overlap tests plus rules still be made rotation-invariant without replacing the engine?

## Hypothesis
**H1 (supported as primary-source design claim, unmeasured on Homebase):** Discrete collision at the start/end of a step can **tunnel** through thin nets and can produce **ghost contacts** on joined edges; that is consistent with the existing audit finding that net collision **changes under equivalent court rotation**. Enabling a generic physics CCD flag is **not** the same as emitting a **single localized contact event** the rules layer can score.[1][3][4]

**H2 (supported, refutes “CCD ⇒ correct scoring”):** Jolt **LinearCast** fully **rotates then CastShape**; fast-rotating long objects can still miss. Box2D TOI “might miss collisions that are clear at the final positions” and is scoped mainly to **tunnel prevention vs statics**, not full rotational CCD.[1][3]

**H3 (supported as contract, unmeasured):** PhysX default `ccdMaxPasses = 1` **drops remaining time after first TOI** (“time stealing”, same term in Jolt). Multi-pass CCD can bounce **the same object multiple times in one step**. Trigger shapes are **excluded from CCD** unless emulated. A sport **domain** must own first-contact vs later-contact semantics; leftover `dt` must not silently credit a second net or a serve.[5][1]

**Not claimed:** Unreal/Jolt/PhysX already won; a custom kernel is required; any FPS/throughput number.

## Host / experiment policy
Measured 2026-09-14 ~02:41 CDT: load averages **9.03 / 9.36 / 10.02**; Mem 23 Gi total, ~6.5 Gi available, swap occupied (~25 Gi used). Charter: under pressure, **research only**. Benchmarks: **not executed**.

## Evidence (primary)

### Jolt Physics architecture (LinearCast / time stealing)
- URL: https://jrouwe.github.io/JoltPhysics/ [1]
- Default `EMotionQuality` is **Discrete**: collision at the beginning of the step; if none, integrate by velocity. Fast/small objects **tunnel** through thin objects in one step.
- **LinearCast**: same initial discrete test, then **CastShape** from the new position; on hit, body is **placed back at the collision and stays until the next step** — named **time stealing**. Back-stepping the whole world is documented as too expensive and **not implemented**.
- LinearCast **fully rotates** the object at step start, then casts from that orientation; **rotational tunneling** remains possible.
- **Ghost collisions**: sliding over mesh/box internal edges; inactive vs active edges; `mEnhancedInternalEdgeRemoval` has geometric preconditions (shared edges).

Docs ToC also lists CCD as jobs **Find CCD Contacts / Resolve CCD Contacts** after integrate, and CastShape as a sweep API.[2]

### Box2D 3.1 collision (TOI)
- URL: https://box2d.org/documentation/md_collision.html [3]
- `b2TimeOfImpact()` exists to find when two **moving** shapes collide; **main purpose: tunnel prevention**; used internally so moving objects do not tunnel **through static shapes**.
- Algorithm: initial separating axis; iterate until touch or pass. **May miss collisions that are clear at final positions.** Rotational misses described as typically glancing.
- Fixed-rotation **shape cast** “will not miss any collisions” (translation-only).
- Collision API is usable **outside** the rigid-body solver (distance, TOI, manifolds, dynamic AABB tree).

### Box2D ghost collisions (Erin Catto, 2020-06-21)
- URL: https://box2d.org/posts/2020/06/ghost-collisions/ [4]
- Overlap on joined edges is **inevitable especially with discrete CD**; shortest resolution can **block motion** (sidewalk crack). Chain shapes + Voronoi/ghost-vertex treatment are a **geometry** fix, not a scoring protocol.

### NVIDIA PhysX 5.6 Advanced Collision Detection
- URL: https://nvidia-omniverse.github.io/PhysX/physx/5.6.0/docs/AdvancedCollisionDetection.html [5]
- CCD is **opt-in at three layers**: scene flag `eENABLE_CCD`, pair flag `eDETECT_CCD_CONTACT`, body flag `eENABLE_CCD`. Activates only above per-shape velocity thresholds.
- `ccdMaxPasses` default **1**: advance to **first TOI**, **drop remaining time**. More passes reduce dropped time, raise cost.
- Multi-pass CCD: same pair may bounce **multiple times in one simulation step**; default contact reports keep the **first** impact unless configured otherwise.
- `eTRIGGER_SHAPE` **not included in CCD**; emulate with filter flags if needed.
- Actor pose/velocity in CCD callbacks usually refer to **time of impact**, not post-response velocity.

### Existing local audit (not re-run)
Charter/cycle 1: RK4 live; Magnus disconnected; net-serve credit, NVZ identity, **rotation-dependent net collision**. Architecture-research already lists Jolt as a **dependency candidate with CCD**; this cycle does **not** repeat that matrix. It asks whether **CCD as shipped** is the **event-localization contract** the rules layer needs.

## Fact vs interpretation
- **Fact:** Discrete vs LinearCast/TOI vs ghost-edge behavior is documented by Jolt, Box2D, and PhysX as above.[1][3][5] Ghost-edge blocking on joined colliders is the discrete-CD sidewalk-crack case.[4]
- **Fact:** Default CCD implementations **steal time** or **drop remainder after first TOI**; they are not a complete multi-contact event log for scoring.[1][5]
- **Interpretation:** Homebase should treat **contact localization** (TOI or analytic net plane vs ball path) as a **domain event** with identity, clock, and pending-contact state, independent of renderer and of leftover integrator `dt`.
- **Not fact:** That LinearCast would fix the rotation-dependent net bug; that FMI clocks (cycle 1) imply TOI; that a custom C++ kernel is faster.

## Decision
Keep charter hypotheses 1–3. **Do not** treat engine CCD as a scoring oracle. Prefer a **held-out contact tape**: discrete overlap vs linear-cast/TOI vs analytic segment–net, comparing **event identity and order**, not FPS. A thin **CastShape/TOI** in the sport module can sit on top of Discrete physics without adopting a second physics authority.

## Limitations
- Host load precluded the 120s experiment; no Homebase measurements.
- Jolt docs HTML is ToC-heavy; LinearCast prose taken from architecture page [1], not a compiled sample.
- PhysX page is 5.6.0 docs; Unreal’s Chaos CCD not fetched this cycle (avoid engine-table dup).
- No arXiv (cycle 1 429). No GPU, no installs.

## Next angle
When load < ~4 and available RAM > ~8 GiB: **held-out rally/net tape** at `h` ∈ {1/120, 1/60, 1/30} plus **segment–plane TOI vs discrete AABB**, score/event identity vs baseline. Else: **digital-twin snapshot/provenance** (identity, possession, pending contacts, RNG) without coordinates of the real facility.

## Dedup
Does not repeat architecture-research engine table or cycle 1 FMI/tick-group contract.

## Sources

[1] https://jrouwe.github.io/JoltPhysics
[2] https://jrouwe.github.io/JoltPhysicsDocs/5.4.0/index.html
[3] https://box2d.org/documentation/md_collision.html
[4] https://box2d.org/posts/2020/06/ghost-collisions
[5] https://nvidia-omniverse.github.io/PhysX/physx/5.6.0/docs/AdvancedCollisionDetection.html
