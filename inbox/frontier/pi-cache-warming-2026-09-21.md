---
id: inbox-frontier-pi-cache-warming-2026-09-21
title: "pi 0.86 — cost-gated prompt cache warming"
type: inbox
status: draft
created: 2026-09-21
updated: 2026-09-21
node: frontier
harnesses: [pi]
domains: [ai-ml, frameworks, tokenomics]
tags: [inbox, frontier, pi, cache]
---

# pi cost-gated cache warming

## Context

### FACT
- **v0.86.0:** prompt cache warming modes `off|streaming|idle`; refresh = 1-token @ **90% cache lifetime**; gate expected savings ≥ **$0.05**; idle≤30m / active≤60m; stop on model switch / compaction / branch.
- Transcript-backed system/tool section diffs (#9548); `/bug` redacted diagnostics; offline Radius catalog; per-model compaction budgets; `user_bash` fail-closed.
- **v0.86.1:** Meta Muse provider (`/login meta` / `META_API_KEY`); Node compile-cache launch speed.

### INTERPRETATION
- Clearest Anthropic cache-warm peer steal this window (complements OMP #12431 recall-stable head). Multi-harness pattern now: OMP cache-head + pi warmer + Prime fhcache-candidate.

## Next action

Steal contract into Hermes/OMP Anthropic sessions (research/port). Compare savings gate vs raw keepalive.

## Links

- https://github.com/earendil-works/pi/releases/tag/v0.86.0
- https://github.com/earendil-works/pi/releases/tag/v0.86.1
