---
id: perm-20260923-performance-claims-need-separate-correctness-and-causality
title: "Performance claims need separate correctness and causality evidence"
type: permanent
status: active
created: 2026-09-23
updated: 2026-09-23
harnesses: []
domains: [software-engineering, statistics]
confidence: high
tags: [permanent, performance, measurement, causality, verification]
---

# Performance claims need separate correctness and causality evidence

## Idea (atomic)

A green regression test can prove that a new implementation still behaves correctly while proving nothing about whether the intended optimization mechanism actually happened.

Treat these as separate proof obligations:

1. **Correctness:** output/state semantics remain valid.
2. **Mechanism:** the code path or resource reuse claimed by the optimization actually occurred.
3. **Causality:** the measured change is attributable to the treatment rather than build drift, workload drift, warmup, queueing, or noise.
4. **Impact:** the mechanism changes a metric users or operators care about.

Evidence strength should scale with claim blast radius. A local cleanup needs less proof than a cross-platform architecture or latency claim.

## Why it matters for our harnesses

Agent systems make it easy to produce instrumentation and easy to overinterpret it. Useful measurement needs boundaries:

- pin control and candidate revisions
- verify built-artifact identity when runtime behavior is expected to differ
- separate setup, queue, service, stall, provider, action, verify, and total time where those phases matter
- report distributions/tails instead of one favorable sample
- use paired A/B or ABAB designs when noise or warmup can dominate
- preserve the exact workload and configuration across treatments
- test extreme values and lifecycle boundaries when timing arithmetic or scheduling semantics are involved
- use real workloads when synthetic tests cannot exercise the claimed mechanism
- keep correctness tests even when the performance mechanism requires a different measurement surface

If the measurement cannot distinguish the candidate from the control, the correct result is **unknown**, not “probably faster.”

## Public OSS evidence

### MCAP #1841

The zstd context-reuse PR separates correctness from mechanism evidence well.

Its multi-chunk test verifies that reused-encoder lifetime plumbing does not corrupt output. The author explicitly notes that the test would still pass if reuse were removed, so it is not used as proof of reuse.

The mechanism/impact evidence instead compares the same real workload before and after: process creation drops from 447 `clone3` calls to 3 while the decoded output remains equivalent; the reported wall-clock run also improves from about 23.1 s to 21.6 s.

- https://github.com/foxglove/mcap/pull/1841

## Evidence ladder

For optimization claims, prefer the cheapest level that can actually falsify the claim:

1. static ownership/lifetime trace
2. deterministic focused regression for semantic safety
3. mechanism-specific counters/traces
4. paired microbenchmark
5. repeated A/B or ABAB benchmark
6. representative end-to-end workload
7. production/field evidence with confounders documented

Higher is not automatically better. A lower-level mechanism counter can be more causal than a noisy end-to-end benchmark. Use multiple levels when correctness and impact live on different surfaces.

## Anti-patterns

- treating added telemetry as proof of improvement
- using a correctness test as proof that reuse/caching/offload happened
- comparing different binaries, model versions, prompts, configs, or datasets
- reporting only the best run
- optimizing mean latency while hiding tail regressions
- claiming savings from projections without reconciling physical/provider usage
- rerunning until green without explaining the variance

## Related

- [[permanent/perm-20260914-landing-evidence-over-state-labels]]
- PR #19: exact treatment identity and falsifiable verification
