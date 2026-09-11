---
id: perm-20260911-bots-advise-humans-merge
title: "Quality bots advise; authorized humans (or maintainer-configured merge automation) merge"
type: permanent
status: active
created: 2026-09-11
updated: 2026-09-11
harnesses: [cursor, hermes, omp]
domains: [frameworks, skills]
confidence: high
tags: [permanent, oss, merge-authority, greptile]
---

# Quality bots advise; authorized humans merge

## Idea (atomic)

An AI review confidence score, Codecov patch %, CodSpeed "no perf change", Scorecard SARIF, and a complete evidence receipt are **SPEC review/evidence**. They are not merge. Kubernetes Tide is the exception that proves the rule: it merges only because maintainers configured `/lgtm`+`/approve` as *their* authorized path. A coding agent, cloud worker, or a bot the implementer controls must not hold that bit.

## Why it matters for our harnesses

Factory and Cursor/Hermes/OMP workers will see Greptile on LiteLLM and try to copy "must be 4/5 to merge". Keep it as "must be 4/5 before *asking* a maintainer". Verified OSS Loop §5 vs §6. Do not stack four AI commenters. Do not copy LiteLLM's whole Actions tree into a spec repo.

## Related

- [[literature/lit-20260911-oss-quality-bot-stacks]]
- [[permanent/perm-20260911-factory-applies-verified-oss-loop]]
- https://github.com/kvnloo/verified-oss-loop
