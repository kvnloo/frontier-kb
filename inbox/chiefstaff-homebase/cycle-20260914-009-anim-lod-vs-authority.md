---
id: homebase-cycle-20260914-009-anim-lod-vs-authority
title: "Cycle 9: animation LOD/culling vs rally authority; HLA still unverified"
type: inbox
status: captured
created: 2026-09-14
updated: 2026-09-14
harnesses: [hermes]
domains: [physics, computer-science, simulation]
confidence: medium
tags: [homebase, digital-twin, animation, rendering, research-cycle]
---

# Cycle 9 — animation budget / culling / interpolation vs domain authority

## Question
Can **animation LOD, visibility culling, and keyframe interpolation** (render/streaming angle) be treated as the same class of contract as FMI clocks (c1), CCD (c2), Property vs Telemetry (c4), jobs (c5), DES vs ODE (c7), and QSS (c8) — i.e. a **presentation/solver schedule** that must **not** write score, possession, or first-contact?

## Hypothesis
**H (tested):** Engine animation systems explicitly **throttle or skip** skeletal/animator updates based on **visibility and CPU budget**. That is **perceptual quality under a millisecond budget**, not rally truth. glTF interpolation is **how to fill frames between keys**, not a physics integrator.

**Avoid:** Re-citing FMI, Jolt/Box2D/PhysX CCD, DTDL, jobs/SoA, Modelica/Ptolemy, QSS papers. Do not treat Unreal bot-check pages as evidence (cycle 4). Do not promote H3.

## Host
Measured 2026-09-14 ~15:35 CDT: load **10.64 / 9.55 / 7.99**, Mem 23 Gi, **~5.9 Gi available**, swap ~34 Gi used, 20 logical CPUs. Cycle 8 tape gate **loadavg-1m < 4 and Mem available > 8 Gi** **failed** → **experiment not executed**. QMD: 0 collections; no index mutation. No GPU. No HLA PDF this cycle (prior IEEE 1516 HTML served 1302-2019).

## Primary sources retrieved

Retrieved (full HTML specs/docs, not snippets-only):

- Unreal Engine **5.8** *Animation Budget Allocator*: https://dev.epicgames.com/documentation/en-us/unreal-engine/animation-budget-allocator-in-unreal-engine (HTTP 200, title matches; not a Cloudflare interstitial).
- Unity **6.0 (6000.0)** *Animator component*: https://docs.unity3d.com/6000.0/Documentation/Manual/class-Animator.html
- Khronos **glTF 2.0** specification: https://registry.khronos.org/glTF/specs/2.0/glTF-2.0.html (animation objects + Appendix C interpolation).

**Discarded / blocked:**

- IEEE 1516 / 1516.1 HTML and SISO download URLs (404 / wrong-standard class, cycles 7–8).
- Pitch HLA tutorial URL redirected to **onearc.com** marketing HTML — not HLA TM.
- OpenRTI GitLab raw README **403**.
- Godot AnimationTree page retrieved but did not contain `process_callback` / animation-cull contract in the extracted body; **not used**.

### Unreal 5.8 Animation Budget Allocator

Plugin **constrains computation time** for animation on specified skeletal meshes by **dynamically throttling Skeletal Mesh Component ticking**. Fixed budget in **milliseconds of game-thread work**, adjustable **per-platform**. If over budget: stop ticking individual skeletal meshes (favor **Leader Pose Component**); **lower animation update rate**; **choose whether to Interpolate between updates**. Significance favors **closest / most significant** meshes. Requires `SkeletalMeshComponentBudgeted`, Auto Calculate Significance, Enable Animation Budget. Toggle `a.Budget.Enabled`. Debug overlay `a.Budget.Debug.Enabled`.

This is **game-thread animation CPU**, not contact localization or scoring.

### Unity 6 Animator

**Update Mode:** Normal (sync with `Update`, timescale); **Animate Physics** (sync with `FixedUpdate` / physics); Unscaled Time (ignore timescale, e.g. GUI). **Culling Mode:** Always Animate; **Cull Update Transforms** (retarget, IK, and transform writes **disabled when renderers are not visible**); **Cull Completely** (**animation completely disabled** when renderers are not visible). **Apply Root Motion:** animation vs script owns position/rotation.

If a **physics-coupled** athlete used **Cull Completely** while off-camera, **transform/animation would freeze** while the court sim continued — or worse, if root motion were treated as authority, **off-screen athletes would stop contributing**. Visibility must not decide rally outcomes (charter + kernel-experiments: rendering visibility must not decide authoritative outcomes).

### glTF 2.0 animation (normative)

An animation is **channels + samplers**. Sampler interpolation: **LINEAR**, **STEP**, **CUBICSPLINE**. Inputs relative to **t = 0** at the start of the parent animation. Different channels of the same animation **MUST NOT** share the same target. CUBICSPLINE output count **MUST** be **3×** input (in/out tangents + values). Appendix C: how to compute property values **between keyframes**. Implementation note: **non-linear time inputs** (Maya/3ds Max time warps) are **not directly represented**.

This is **asset playback interpolation**, not RK4 / QSS / TOI.

## Support / refute

- **Supported:** Animation budget/culling/interpolation are **presentation contracts** on the same Pareto axis as render streaming / visibility (charter angle). They optimize **perceived quality under CPU ms**, not score.
- **Supported:** Unity **Cull Completely** and UE **stop ticking** are explicit **observer-dependent** skips — the observer-removal counterfactual from cycle 3 / kernel-experiments: suppressing draw must not change domain continuation; here the engine **does** skip animation when not visible unless Always Animate / budget-exempt.
- **Supported:** Animate Physics vs Normal is a **clock coupling** (FixedUpdate vs Update), sibling to Modelica sample/hold (c7) and FMI communication points (c1), still **not** a custom kernel.
- **Not supported:** Homebase must implement UE Budget Allocator; glTF CUBICSPLINE is a physics solver; HLA time management (still unverified).
- **Refuted this cycle:** That load/RAM allowed the net/rally tape. That Pitch/SISO/OpenRTI URLs yield HLA 1516.1 TM this cycle.

## Fact vs interpretation

- **Fact:** Quoted UE throttle behaviors; Unity Update/Culling/Root Motion enums; glTF sampler interpolation MUST rules; host load/RAM; discarded HLA URLs.
- **Interpretation:** Authoritative athlete/ball pose for **rules** should not be the **interpolated, culled, budgeted skeletal pose**. Display can interpolate between **authoritative snapshots**.
- **Not fact:** Measured FPS or contact error under culling; Homebase using these plugins.

## Benchmark provenance

**not executed** (loadavg-1m 10.64; Mem available ~5.9 Gi). No `evidence/cycle-009-*`.

## Decision

Keep charter H1–H3. Add Pareto axis: **animation LOD/cull/interpolate vs authoritative pose**. Do **not** promote H3. Do **not** let visibility or animation budget write score/possession/contact. Prefer **Always Animate / unculled** (or a separate sim skeleton) for any pose that feeds rules; use budget/cull only on **spectators / distant cosmetic meshes**.

## Limitations

Literature/docs only. Unity page mixes a **Normal** vector glossary injection into Update Mode text; Update Mode meaning still taken from the following sentences (Update vs FixedUpdate vs unscaled). Godot cull not evidenced. HLA still open.

## Next angle

Cycle 10: **net/rally tape** (segment-plane vs discrete vs TOI) **if** loadavg-1m < 4 **and** Mem available > 8 Gi; else **scientific autotuning / held-out gates** (never let candidate edit the judge) or **USD/Nanite streaming vs sim tick** if those docs are non-bot.
