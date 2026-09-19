---
id: homebase-cycle-20260914-010-autotune-judge-vs-streaming
title: "Cycle 10: autotuner must not own the judge; Nanite/USD purpose is not score"
type: inbox
status: captured
created: 2026-09-14
updated: 2026-09-14
harnesses: [hermes]
domains: [physics, computer-science, simulation]
confidence: medium
tags: [homebase, digital-twin, autotuning, streaming, research-cycle]
---

# Cycle 10 — scientific autotuning vs held-out judge; USD/Nanite streaming vs sim tick

## Question
Does a **program autotuner** (search over configurations) or a **view-dependent mesh streamer** (Nanite clusters / USD payloads+purpose) become a scoring or physics kernel, or must **measurement/acceptance stay a separate writer** from **search** and from **camera/working-set**?

## Hypothesis
**H (tested):** OpenTuner’s architecture already **splits SearchDriver (DesiredResults) from user-defined Measurement (Results)**. That is the charter “never let candidate edit the judge.” Nanite/USD **Purpose/Visibility/Payload load** are **working-set / render traversal** contracts, sibling to cycle 9 animation cull — not rally authority.

**Avoid:** Re-citing FMI, CCD, DTDL, jobs/SoA, Modelica/Ptolemy, QSS, UE Animation Budget. Do not promote H3. Do not treat bot-check pages as evidence.

## Host
Measured 2026-09-14 ~17:39 CDT: load **4.53 / 6.80 / 6.82**, Mem 23 Gi, **~5.7 Gi available**, swap ~34 Gi used, 20 logical CPUs. Tape gate **loadavg-1m < 4 and Mem available > 8 Gi** **failed** (1m 4.53; Mem 5.7 Gi) → **experiment not executed**. QMD: 0 collections; no index mutation. No GPU, no installs, no kb_store ingest, no DSN read.

## Primary sources retrieved

Retrieved (full documents, not snippets-only):

- Ansel et al., **OpenTuner: An Extensible Framework for Program Autotuning**, PACT’14, ACM 978-1-4503-2809-8/14/08, DOI 10.1145/2628071.2628092. PDF HTTP 200 from `https://commit.csail.mit.edu/papers/2014/ansel-pact14-opentuner.pdf` (redirect from groups.csail.mit.edu; 476488 bytes). Site: https://opentuner.org/ (HTTP 200).
- Unreal Engine **5.8** *Nanite Virtualized Geometry*: https://dev.epicgames.com/documentation/en-us/unreal-engine/nanite-virtualized-geometry-in-unreal-engine (HTTP 200; title matches; not Cloudflare interstitial).
- Pixar **USD 26.08** glossary: https://openusd.org/release/glossary.html (HTTP 200; *USD Terms and Concepts*).

**Discarded / unused this cycle:** HLA 1516 URLs (still wrong-standard class, cycles 7–9). No OpenTuner GitHub clone (would be an install/download). PDF not copied into the vault (size vs cycle artifact budget; text extracted locally then discarded).

### OpenTuner (PACT 2014)

Figure 2: **Search techniques + SearchDriver + ConfigurationManipulator** read Results and **write DesiredResults**; **MeasurementDriver + user-defined measurement function** read DesiredResults and **write Results**; they communicate **exclusively through a results database**. Usage: implement `manipulator()` (search space) and `run(desired_result, input, limit)` (fitness) on `MeasurementInterface`; example returns `Result(time=run_result['time'])` after `call_program` compile+run (Figure 3 GCC flags).

Abstract/intro: **multi-objective** tradeoff among **performance, accuracy, energy, memory**, and QoS targets. Ensembles of search techniques get **larger testing budgets** when they perform well.

GCC experiment note: authors **allowed `-ffast-math`**, which **can change rounding or NaN behavior**, and “have small impacts on program results”; they also “observe speedups with these flags removed.” The paper’s **Figure 5 / §4** reports configuration-space sizes and speedups; it does **not** describe a **held-out test set** or a judge that the searcher cannot rewrite.

### Nanite (UE 5.8)

Virtualized geometry: import analyzes meshes into **hierarchical clusters**; at render time clusters **swap on the fly at varying LOD based on the camera view** and stream **only visible detail**. Own rendering pass **bypasses traditional draw calls**. SSD recommended because it **relies on streaming mesh data from disk on demand**.

**Not currently supported** (docs): view-specific min screen radius / distance culling; forward rendering; VR stereo; MSAA; lighting channels; **ray-tracing against Nanite meshes** uses the **Fallback Mesh by default**. WPO displacement is limited (per-cluster GPU cull). Frame budgets “no longer constrained by polycounts” is a **render** claim, not contact localization.

### USD 26.08 glossary

**Payload:** composition arc like a Reference, but if the stage opens with `UsdStage::InitialLoadSet::LoadNone`, payload arcs are **recorded but not traversed** so clients build a **working set**. Payloads are **weaker than references**.

**Purpose** (`UsdGeomImageable`): client-driven **visibility categories** as gates on scenegraph traversal (`default` / `render` / `proxy` / `guide`). **Visibility:** `inherited` vs `invisible` — **pruning invisibility** of the subtree for **rendering**.

## Support / refute

- **Supported:** Autotuning frameworks already treat **search** and **measurement** as different writers (OpenTuner Figure 2). Homebase must keep **acceptance predicates / held-out tapes** on the measurement side; search must not edit fixtures or the judge (charter + skill optimizer acceptance).
- **Supported:** `-ffast-math` in the published GCC tuner is an existence proof that **the measurement function can silently relax numerical truth** unless correctness is an explicit gate, not an optional “small impact.”
- **Supported:** Nanite camera-LOD streaming and USD Purpose/Payload load are **observer/working-set** contracts — same Pareto axis as cycle 9 animation cull. They must not supply the **authoritative court mesh** for scoring/contact.
- **Not supported:** OpenTuner (or any autotuner) as a custom sim kernel; Nanite as physics; USD Payload as Property restore (cycle 4); HLA TM.
- **Refuted this cycle:** That load/RAM allowed the net/rally tape.

## Fact vs interpretation

- **Fact:** OpenTuner search vs measurement split; `Result(time=…)`; multi-objective accuracy/energy/memory; `-ffast-math` allowed; Nanite camera cluster swap + Fallback Mesh for RT; USD Payload LoadNone + Purpose categories; host load/RAM.
- **Interpretation:** A Homebase autotune loop should return **invalid** (or infinite cost) if held-out scoring/contact predicates fail, **before** ranking time; streamed/proxy geometry is display-only.
- **Not fact:** Measured OpenTuner wall time here; Nanite vs Chaos collision mesh identity on Homebase.

## Benchmark provenance

**not executed** (loadavg-1m 4.53; Mem available ~5.7 Gi). No `evidence/cycle-010-*`. OpenTuner paper’s 2.8× / GCC numbers are **authors’ 2014 machines**, not this host.

## Decision

Keep charter H1–H3. Add Pareto axes: **(search vs measurement/judge)** and **(streamed/purpose geometry vs authoritative collision/score mesh)**. Do **not** promote H3. Do **not** let an autotuner rewrite held-out tests. Do **not** let Nanite/USD visibility or payload unload change rally outcomes.

## Limitations

Literature/docs only. OpenTuner paper has no held-out split. Nanite page has no collision/Chaos section in the extracted body. USD glossary is terms, not a runtime benchmark. HLA still open.

## Next angle

Cycle 11: **net/rally tape** (segment-plane vs discrete vs TOI) **if** loadavg-1m < 4 **and** Mem available > 8 Gi; else **FMI/DTDL snapshot round-trip spec** (still unmeasured) or **Chaos/Jolt collision mesh vs render mesh** primary docs if non-bot. Cycle 12 is the next six-cycle Pareto synthesis (cycles 7–12).
