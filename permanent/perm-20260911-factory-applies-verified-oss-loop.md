---
id: perm-20260911-factory-applies-verified-oss-loop
title: "OSS factory HITL columns are the Verified OSS Loop, not a second scheduler"
type: permanent
status: active
created: 2026-09-11
updated: 2026-09-11
harnesses: [cursor, hermes, omp]
domains: [frameworks, skills]
confidence: high
tags: [permanent, oss-factory, hitl, verified-oss-loop]
---

# Factory HITL columns are the Verified OSS Loop

## Idea (atomic)

`kvnloo/oss-factory` Linear columns (Triage → Backlog → Todo → In Progress → Ready to Review → Maintainer Review → Done) are the same loop as `kvnloo/verified-oss-loop` SPEC (research → claimable → claim lease → isolated work → receipt → independent review → human merge). Traction formula is an *outcome view*. It must not set claim priority or authorize merge. `github_writes=0` until Todo is the factory's origin-write gate and is compatible with workers-never-merge.

## Why it matters for our harnesses

When optimizing **opted-in** `kvnloo/*` repos, run `oss-onboard --with-automation` and stop. When contributing to origin OSS, follow *their* bots and templates; do not paste loop labels onto kubernetes/litellm/HA. CoS should keep HITL.md pointing at the kit so new factory workers cannot invent a third process.

## Related

- [[literature/lit-20260911-oss-quality-bot-stacks]]
- [[permanent/perm-20260911-bots-advise-humans-merge]]
- https://github.com/kvnloo/verified-oss-loop/blob/main/docs/factory.md
- https://github.com/kvnloo/oss-factory
