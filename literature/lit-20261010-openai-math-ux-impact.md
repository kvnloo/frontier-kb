---
id: lit-20261010-openai-math-ux-impact
title: "OpenAI mathematics 372: UX-first OSS transfer triage"
type: literature
status: draft
created: 2026-10-10
updated: 2026-10-10
sources: ["https://github.com/openai/math/commit/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb", "https://github.com/openai/math/blob/main/history.md", "https://github.com/kvnloo/ctx/blob/main/README.md", "https://github.com/kvnloo/kerdoios/blob/main/ROADMAP.md"]
harnesses: [omp, hermes]
domains: [cs]
confidence: medium
tags: [literature, mathematics, algorithms, ux, benchmarks]
---

# OpenAI mathematics 372: UX-first OSS transfer triage

## Claim (one sentence)

Use a paper only when its algorithm can improve a **measured, high-value, complete end-user journey** while preserving the target repo's correctness, performance and maintenance ethos.

## Evidence

- Source snapshot: [openai/math @ `fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb`](https://github.com/openai/math/commit/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb), 372 result families, 719 manuscripts; 300 top-line manuscripts have stated Lean formalization coverage (~42%) as of October 7. Read [withdrawals/corrections](https://github.com/openai/math/blob/main/history.md) before reusing an argument.
- Formal theorem ≠ executable fast kernel ≠ measured user win; for example [#107](https://github.com/openai/math/blob/main/lean/docs/107.md) is an arithmetic-operation upper bound, and [#130](https://github.com/openai/math/blob/main/lean/docs/130.md) is exact complex-arithmetic FFT with extremely small asymptotic saving.
- [ctx](https://github.com/kvnloo/ctx/blob/main/README.md) is fundamentally BM25, semantic, provenance, and graph lookup. There is currently no evidence that family [#121](https://github.com/openai/math/blob/main/lean/docs/121.md) edit distance is on its UX-critical path.
- [Kerdoios](https://github.com/kvnloo/kerdoios/blob/main/ROADMAP.md) operates a hard-constrained, heterogeneous Pareto compute portfolio. Its latency/cost/privacy matrix is not automatically a metric k-median instance; family [#125](https://github.com/openai/math/blob/main/lean/docs/125.md) requires a metric.
- Current-status checks (2026-10-10): [PyTorch #187094](https://github.com/pytorch/pytorch/issues/187094) remains open but needs GB300 reproduction; [PyTorch #195629](https://github.com/pytorch/pytorch/issues/195629), [CUA #4416](https://github.com/trycua/cua/issues/4416), and [Newton #4320](https://github.com/newton-physics/newton/issues/4320) are closed; do not duplicate others' work.

## Repo-specific UX contract

- **PyTorch:** training step and tokens/sec, VRAM, numerical parity by dtype/shape/device.
- **CUA:** time to verified desktop task, p95, focus/cancellation safety.
- **OMP/Hermes:** time to useful completed work, provider turns/cost, streaming/cached-prefix integrity, no phantom completion.
- **ctx:** time to cited relevant evidence; recall/precision, index/update p95, provenance.
- **Newton:** time to first *valid* simulation step; steps/sec, contact and gradient correctness.
- **OpenUSD:** time to first meaningful scene, frame p95, scene/undo semantics.
- **PyPSA/OpenMC:** time to scientifically valid solution at fixed gap or uncertainty.
- **Kerdoios/z0:** cost/latency per independent verified success; never bypass hard filters.

## First-fit decisions

| Family | Candidate | Decision | Cheap disqualifier |
|---|---|---|---|
| #107 / #130 | PyTorch GEMM / FFT | Research-only despite high UX ceiling | No practical executable crossover + numerical parity |
| #110 | Kerdoios model migration | Assumptions-first | Movement is nonmetric / request model fails |
| #125 | Kerdoios k-median | Demote | Provider costs and constraints do not yield a metric |
| #121 | ctx edit similarity | Demote | Edit distance not on a hot user path |
| #120 | graph matching specialist | Qualify | No large unweighted general matching hot path |
| #174 | graph preprocessing | Hold | No cut-sparse spanning-tree role in real solver |
| #124 | six-lane agent factory | Not applicable | Only three identical machines and unit-time jobs |

## Fact vs interpretation

**Facts:** Stated formalization scopes and upstream issue status are source-specific; closed fixes are not available work. Source-reported performance numbers are not our reproduced measurements.

**Interpretation:** Rank potential by user-journey criticality and achievable full-task improvement, but a hypothetical upper bound is not a verified impact. For latency, if component fraction `f` runs `s` times faster, maximum whole-task reduction under Amdahl is `f(1 - 1/s)`. Require independent end-to-end tests before promotion.

No math-derived runtime patch or performance improvement has been qualified or shipped in this wave. Negative results are valid outcomes. Preserve original researchers, diagnosis authors, human reviewers, and test contributors as a provenance chain.

## Next gates

1. Measure existing P0 UX path with supported target hardware and actual workload.
2. Verify paper revision, exact Lean theorem scope, and algorithm constructivity.
3. Attempt cheapest counterexample/feasibility experiment.
4. Compare unchanged baseline, simple control and challenger on complete user journey.
5. Publish frozen receipts via existing Evolution Lab → Tokenomics → z0evals; upstream PR only after maintainer-aligned independent review.

## First observed UX leverage (existing measurements, not this wave's benchmark)

Kerdoios's [local-cognition placement profile](https://github.com/kvnloo/kerdoios/blob/main/docs/local-cognition-placement.md) reports **360 tokens/s on llama.cpp vs 10.5 tokens/s on Ollama** for the same FunctionGemma weights/runtime context on its profiled GPU (~34x backend effect). It also reports cold-load costs of **46–306 ms** and short decisions of **124–1275 ms** for five measured models. Reusing a resident small model can therefore matter to an interactive turn; **the existing runtime selection / reuse path is a higher-confidence UX target than immediately implementing #125 metric k-median**. These figures are source-reported prior measurements, not rebenchmarked here and not generalized to a whole agent task. The #110 theorem's metric/adversary preconditions still require proof of fit.

**Next discriminating experiment:** use existing serving receipts to measure the frequency and E2E p95 contribution of `reuse/load/evict`, preserving equal verified outcomes and no extra policy violations. Compare current planner with a simple no-thrash control; pursue #110 only if true metric-server applicability and additional benefits survive. Do not add another placement engine.
