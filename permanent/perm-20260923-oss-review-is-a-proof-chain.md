---
id: perm-20260923-oss-review-is-a-proof-chain
title: "OSS review is a proof chain, not a comment-generation task"
type: permanent
status: active
created: 2026-09-23
updated: 2026-09-23
harnesses: []
domains: [software-engineering]
confidence: high
tags: [permanent, oss, review, invariants, verification]
---

# OSS review is a proof chain, not a comment-generation task

## Idea (atomic)

A high-quality OSS review should compress evidence into a proof chain:

1. **Observable:** establish what the current target revision actually does.
2. **Owner + invariant:** identify the module, lifecycle, or contract that owns the behavior.
3. **Consequence:** state the concrete failure or preserved property.
4. **Smallest proof:** produce the narrowest test, counterexample, trace, or measurement that can falsify the claim.
5. **Smallest ownership-correct action:** prefer the minimal fix, review comment, or follow-up that repairs the invariant without widening scope.
6. **Composition recheck:** before posting, re-read current tip and nearby issues/PRs so the claim still holds when changes compose.

The review is incomplete if it jumps from suspicious code directly to a redesign without proving the intermediate invariant.

## Why it matters for our harnesses

Fast contribution loops create a failure mode where analysis volume outruns evidence quality. The durable correction is to preserve distinctions that affect correctness:

- desired state vs implemented state vs observed state vs verified outcome
- execution vs verification
- semantic correctness vs optimization evidence
- authored behavior vs behavior introduced by composition
- resource creation vs resource lifetime and cleanup
- successful retry vs correctness under retry/restart/partial failure
- current-main behavior vs stale issue text

A positive review can be useful when it names the invariant that is already preserved. A negative review should carry a falsifiable counterexample or clearly mark the gap as unknown.

When evidence is unavailable, say **NOT TESTED** or **unknown** rather than manufacturing confidence. Stop expanding the review when additional analysis is no longer changing the decision.

## Public OSS evidence

### libuv #5283

Reviewing the FSEvents allocation cleanup required checking the actual Core Foundation ownership contract rather than reasoning from the age of the code. The useful conclusion was narrow: the ownership rule supported the cleanup; a larger redesign was a separate question.

The same thread also reinforced that repository-specific AI disclosure and contributor-responsibility rules are part of the contribution contract.

- https://github.com/libuv/libuv/pull/5283

### MCAP #1841

The MCAP zstd work makes the proof-chain distinction unusually explicit. Its multi-chunk regression proves correctness of the new lifetime plumbing, but the test intentionally does **not** prove that context reuse occurs. Reuse is a separate mechanism claim backed by before/after process evidence.

- https://github.com/foxglove/mcap/pull/1841

## Review checklist

Before posting:

- pin the target revision
- reproduce or trace the observable
- identify the owner and invariant
- search for counterexamples and overlapping work
- test the failure/resource lifecycle, not only the happy path
- separate correctness claims from performance claims
- state what was tested and what remains unknown
- recheck current tip/comments immediately before mutation
- keep the final comment shorter than the investigation that produced it

## Related

- [[permanent/perm-20260914-landing-evidence-over-state-labels]]
- PR #19: OSS contribution-policy intelligence
