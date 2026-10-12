---
id: inbox-20261012-math372-digital-twins
title: "Math372 wave 3: digital twins, numerical contracts, and shared-operator compute"
type: inbox
status: draft
created: 2026-10-12
updated: 2026-10-12
node: chatgpt
harnesses: []
domains: [cs]
tags: [inbox, mathematics, digital-twins, scientific-computing]
---

<!-- oss-factory:v1
{"id":"20261012-math372-wave3","kind":"result","project":"frontier-kb","from":"chatgpt","to":["factory"],"status":"done","civ":{"city_id":"oss:frontier-kb"},"parent_id":"math372-42","branch":"study/math372-digital-twin-wave3-20261012","dedupe_key":"frontier-kb/math372/wave3-digital-twins"}
-->

# Math372 wave 3 — LIMITED, not runtime promotion

Parent: [research program #42](https://github.com/kvnloo/frontier-kb/issues/42).

## Decision

Put reusable numerical components beneath digital twins. Optimize **time to a scientifically valid scenario at fixed accuracy**, not theorem count or isolated asymptotics. Keep conventional optimization gains separate from new mathematical claims.

## Executed: family 325 meets an actual numerical path

[OpenAI's 325 scope](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/docs/325.md) includes rational functions with poles outside the closure of the numerical range. That gives a concrete research connection to [OpenMC's CRAM depletion method](https://github.com/openmc-dev/openmc/blob/aa4afc41eb5421fb77351da863bca150be106a5e/openmc/deplete/cram.py): bound the error in a rational matrix-exponential approximation before considering adaptive order/substeps.

The included local source snapshot matches Git blob `3594ffbe8419aebd533d675631ead9001744510c` exactly. Extracting the unchanged numerical-method AST and CRAM16 coefficients gives **12/12 exact parity checks** against the standalone adapter. Compatibility bindings replace only imports and the method's substep validators; full OpenMC integration was not run.

The finite research prototype adds an exact-rational outer rectangle for the numerical range of the stored real matrix, checks both poles and conjugate poles, and uses the holomorphic IPF continuation. Extending `2*real(alpha/(z-theta))` naively to complex z is not holomorphic. A nilpotent 2x2 test also demonstrates why eigenvalues alone cannot certify nonnormal matrix-function error.

**18 domain screens: 6 require a tighter enclosure because the outer rectangle contains poles.** This is inconclusive about the actual numerical range, not evidence of invalid physics or an invalid CRAM algorithm. All 18 remain ineligible for automatic promotion: a rigorous uniform scalar-error bound, numerical-roundoff treatment, and local Lean recheck are still missing.

## Conventional control: same-operator batching

Synthetic closed one-way transfer chains: 64/256/1024 states; 1/8/32 initial vectors; seeds 17/29/43; 11 alternating-order timing pairs per case. CPU only, one BLAS thread, NumPy 2.3.5 / SciPy 1.17.0. Timed calls include preparation, copying, allocations, factorization and solves.

| Shared vectors | Cases | Median speed ratio across cases | Range |
|---|---:|---:|---:|
| 1 | 9 | 1.01x | 0.90–1.11x |
| 8 | 9 | 6.90x | 5.71–7.51x |
| 32 | 9 | 11.15x | 7.02–24.81x |

Maximum absolute difference against SciPy expm_multiply on those 27 cases: **2.037953139577553e-14**. Block-versus-column difference: **0**. Maximum closed-chain mass error: **3.219646771412954e-15**.

These are isolated adapted-kernel measurements, **not OpenMC end-to-end speedups, a new CRAM algorithm, a GPU result, or a gain caused by family 325**. The production numerical method already supports multiple RHS columns in the tested shapes. The possible contribution is aggregation at a supported caller, only when the operator/timestep/precision/substeps are exactly shared.

[Minimal pinned-source batching reproducer](reproduce_math372_wave3.py). The complete research packet, raw timing pairs, domain-screen implementation, source snapshot and tests were delivered as a conversation artifact; they are not all hosted in this note.

## Preserved negative result

A separate fixture (32 states, rate=4, seed=8, identity RHS) returns **-2.6358201516364696e-13** in both paths; the unchanged pinned method reproduces it. The dense reference is nonnegative. Maximum reference error is **2.583905372923346e-12**. This rejects the experiment's strict positivity floor of -5e-14. No clipping or tolerance relaxation was applied.

**21 tests pass; 1 expected-failure positivity test remains; 12 source-parity checks pass.** This synthetic requirement is not asserted to be an established upstream bug. A norm bound does not imply entrywise positivity.

## Prioritized follow-on waves — proposed, not executed

| Priority | Families | Useful transfer | First admission gate |
|---|---|---|---|
| 1 | 325 | Shared scientific matrix-function error checks; OpenMC now, evaluate reusable SciPy/SLEPc/PETSc seams | Pole-free domain, useful uniform error bound, roundoff and actual workload evidence |
| 2 | 115 | Admissible traffic/resource scenario ensembles with fixed observed totals | Exact small-instance oracle; uniform feasible tables are not a realistic demand model; bounded-cell counting is not automatically bounded-cell sampling |
| 3 | 125; later 089/174 | GEV park/service siting and network-planning experiments | Genuine metric; directed travel, capacities, fairness and electrical flows require separate contracts |
| 4 | 374 | Sensitivity tests for digital-twin transport/assimilation | Uniform continuous source on a compact convex body and quadratic transport; not generic point-cloud registration |
| 5 | 107/130 | Finite GPU matrix/FFT building blocks | Executable crossover versus tuned kernels at fixed precision, shape and memory |
| 6 | 362/364 | Compatible kinetic/plasma/gas simulation validation | Exact PDE/model fit; continuum smoothness is not numerical stability or all-species physics |

Proposed architecture: versioned observations/geometry -> candidate scenarios -> shared numerical kernels -> bounded CPU/GPU execution -> independently checked outcomes -> scene/planning UI. Start locally; distribute only after measurement justifies movement/scheduling overhead. No new scheduler or project registry is introduced.

## Next action

First measure whether a real supported OpenMC workflow contains enough exactly identical operators to benefit from aggregation. Include memory, grouping and communication costs; compare against existing caller behavior. In parallel, qualify the full family-325 error-bound chain before any adaptive solver change. Keep the prior Kerdoios quota-accounting owner separate. No upstream issue/PR or default-branch merge is authorized by this note.

## Credit and sources

Preserve [Emiel Lorist and Felix Schwenninger's August 2026 proof](https://arxiv.org/abs/2608.03841), [Michel Crouzeix and Cesar Palencia's 2017 bound](https://arxiv.org/abs/1702.00668), and OpenAI's later complete-inequality/formalization artifacts. Do not assign exclusive priority to OpenAI for the scalar result. CRAM belongs to Maria Pusa, Antti Isotalo/Maria Pusa's substep work, and OpenMC contributors. SciPy's reference credits Awad H. Al-Mohy and Nicholas J. Higham.

[Release corrections](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/history.md) · [115](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/docs/115.md) · [125](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/docs/125.md) · [374](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/docs/374.md) · [107](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/docs/107.md) · [130](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/docs/130.md).
