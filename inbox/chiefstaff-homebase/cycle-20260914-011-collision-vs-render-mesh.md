---
id: homebase-cycle-20260914-011-collision-vs-render-mesh
title: "Cycle 11: Chaos simple/complex collision ≠ Nanite render mesh; Jolt MeshShape is static"
type: inbox
status: captured
created: 2026-09-14
updated: 2026-09-14
harnesses: [hermes]
domains: [physics, computer-science, simulation]
confidence: medium
tags: [homebase, digital-twin, collision, mesh, research-cycle]
---

# Cycle 11 — collision geometry vs render/streaming mesh

## Question
Does Unreal **simple vs complex collision** (and Jolt **MeshShape / HeightFieldShape**) share identity with **Nanite/USD render working-set** (cycle 10), or must **simulation collision** stay a **separate authored shape** from **camera-streamed triangles**?

## Hypothesis
**H (tested):** UE 5.8 already ships **two collision representations** (primitives/hulls vs trimesh) selected by **query kind and Collision Complexity flags**, independent of Nanite cluster streaming. Jolt **MeshShape** is **mostly static** and **HeightFieldShape requires static bodies**. Render LOD cannot be the scoring net.

**Avoid:** Re-citing FMI clocks, DTDL Property, OpenTuner SearchDriver, animation budget, QSS. Do not promote H3. No bot-check pages.

## Host
Measured 2026-09-14 ~19:43 CDT: load **10.74 / 6.25 / 5.92**, MemTotal 23.3 Gi, **MemAvailable ~6.2 Gi**, SwapFree ~117 Gi of ~152 Gi, 2/4001 processes. Tape gate **loadavg-1m < 4 and Mem available > 8 Gi** **failed** → **experiment not executed**. QMD: 0 collections; no index mutation. No GPU, no installs, no kb_store ingest, no DSN read.

## Primary sources retrieved

Retrieved (full documents, not snippets-only):

- Unreal Engine **5.8** *Simple versus Complex Collision*: https://dev.epicgames.com/documentation/en-us/unreal-engine/simple-versus-complex-collision-in-unreal-engine (HTTP 200; title matches 5.8).
- Unreal Engine **5.8** *Collision in Unreal Engine*: https://dev.epicgames.com/documentation/en-us/unreal-engine/collision-in-unreal-engine (HTTP 200; hub/essentials only — used as navigation, not as collision-flag evidence).
- Jolt Physics architecture (Doxygen): https://jrouwe.github.io/JoltPhysics/ (HTTP 200, 163245 bytes). Architecture page `md_Docs_2Architecture.html` **404**; whitepaper URL `https://jrouwe.nl/jolt/JoltPhysicsWhitePaper.pdf` **404** — discarded.

### UE 5.8 simple vs complex

Simple collision = **cubes, spheres, capsules, convex hulls**. Complex = **the trimesh of a given object**. Default: engine **creates both**, then the **physics solver** uses the matching shape for **scene queries and collision tests** depending on **complex vs simple query**.

Collision Complexity (Static Mesh Editor, Collision category):

- **Project Default:** simple requests → simple shapes; complex requests → complex (project physics settings).
- **Simple And Complex:** simple shapes for **regular scene queries and collision tests**; **complex (per poly)** for **complex scene queries**.
- **Use Simple Collision As Complex:** complex queries still hit **simple** shapes; **ignores the trimesh**; **saves memory** (no baked trimesh) and can improve performance.
- **Use Complex Collision As Simple:** simple queries hit **complex** shapes; **ignores simple collision**; **trimesh used for physics simulation collision**. **You cannot simulate the object** under UseComplexAsSimple; you **can collide other simulated (simple) objects against it**. Chair example: simple hull lets a pawn **slide off a covering angled surface**; UseComplexAsSimple lets the pawn **land on the seat**.

Docs do **not** state that Nanite clusters, Fallback Mesh, or USD Purpose are this trimesh. Cycle 10 Nanite page used **Fallback Mesh for ray tracing**, a **render** path.

### Jolt architecture

Bodies: **static / dynamic / kinematic**. Shapes include **ConvexHullShape**, **TriangleShape** (single triangle; use MeshShape for many), **MeshShape** — “triangles… **mostly used for static geometry**,” **HeightFieldShape** — “Any body that uses this shape **needs to be static**.” Mass/inertia: MeshShape **cannot compute its own mass and inertia** (must be supplied). Per-triangle friction/restitution is an **example**, not a scoring event log.

## Support / refute

- **Supported:** Collision and render already split in shipped engines: **query flag + Collision Complexity** choose **hull vs trimesh**; Nanite (cycle 10) chooses **camera clusters**. A Homebase net/court must **pin which collision representation** is authoritative; visibility/stream LOD must not swap it.
- **Supported:** UseComplexAsSimple **forbids simulating that body** — trimesh-as-simple is a **static collider** pattern, sibling to Jolt MeshShape/HeightField **static** constraint. Dynamic balls/athletes stay **simple/convex**.
- **Supported:** Use Simple As Complex is an explicit **memory/perf** trade that **drops the trimesh** — Goodhart risk if a tuner picks it to save RAM while net contact needs per-poly.
- **Not supported:** Chaos/Jolt as a custom Homebase kernel; Nanite Fallback Mesh as Chaos collision (docs silent); HLA TM.
- **Refuted this cycle:** That load/RAM allowed the net/rally tape.

## Fact vs interpretation

- **Fact:** UE 5.8 four Collision Complexity modes; UseComplexAsSimple cannot simulate the object; Jolt MeshShape mostly static, HeightField static, MeshShape needs supplied inertia; host load/RAM.
- **Interpretation:** Authoritative pickleball net/court should be a **pinned simple or complex collision asset**, not Nanite LOD. Scoring events stay domain-localized (cycle 2 CCD ≠ oracle).
- **Not fact:** Measured TOI vs segment-plane on Homebase; Chaos vs Nanite mesh identity in a cooked Homebase build.

## Benchmark provenance

**not executed** (loadavg-1m 10.74; Mem available ~6.2 Gi). No `evidence/cycle-011-*`.

## Decision

Keep charter H1–H3. Extend cycle 10 Pareto: **(authored collision simple/complex vs streamed render mesh)** and **(static trimesh colliders vs dynamic simple bodies)**. Do **not** promote H3. Do **not** let Collision Complexity or Nanite streaming be an autotune knob that changes held-out contact (cycle 10 judge split).

## Limitations

Literature/docs only. Collision hub page had almost no body. Jolt architecture HTML 404; used Doxygen index. No Godot/PhysX re-read this cycle (cycle 2 already covered PhysX CCD). HLA still open.

## Next angle

Cycle 12: **six-cycle Pareto synthesis (7–12)** plus tape gate: **net/rally tape** if loadavg-1m < 4 and Mem available > 8 Gi; else keep synthesis-only and name the next unmeasured axis (conservation at rate change, Property snapshot RT, or HLA TM if a real PDF).
