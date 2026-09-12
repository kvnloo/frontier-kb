---
id: perm-20260911-observationpack-is-projection-not-history-rewrite
title: "ObservationPack rewrites provider context, not session history"
type: permanent
status: active
created: 2026-09-11
updated: 2026-09-11
harnesses: [pi, omp, hermes]
domains: [frameworks, tokenomics]
confidence: high
tags: [permanent, sol-pi, context]
---

# ObservationPack rewrites provider context, not session history

## Idea (atomic)

SoL-Pi packs large tool results only in the `context` event (messages sent to the provider). The stored session keeps original bytes; `obs_recall` pages the archive. Threshold 10 KiB, `FULL_SENDS = 2`, placeholder `obs_[hex]`, fail-open. Evidence-Preserving Reducer receipts are excluded so verified quotes are not packed again.

## Why it matters for our harnesses

Any OMP/Hermes port that truncates the persisted tool result to save tokens is a different mechanism and will break resume, compaction tails, and "show me the original log." OMP already has a `context` event — use it. Hermes needs `select_context` (or equivalent pre-request rewrite), plus a recall tool, plus an on-disk ledger under the session directory.

## Related

- [[literature/lit-20260911-sol-pi-harness-efficiency]]
- [[permanent/perm-20260911-hermes-sol-pi-is-a-python-plugin-port]]
- [[harnesses/pi]]
