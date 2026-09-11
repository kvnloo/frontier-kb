---
id: perm-20260911-anti-slop-is-smallest-complete
title: "Anti-slop is the smallest complete change that matches the existing tree"
type: permanent
status: active
created: 2026-09-11
updated: 2026-09-11
harnesses: [cursor, hermes, omp]
domains: [frameworks, skills]
confidence: high
tags: [permanent, anti-slop, coding-patterns, verified-oss-loop]
---

# Anti-slop is smallest complete

## Idea (atomic)

Quality from coding agents is the smallest complete diff that matches local style: one concern, fail-then-pass that asserts behavior, names from the domain, comments that explain why, sibling surfaces checked, dead helpers deleted. Anti-patterns are narrating comments, speculative abstractions, drive-by format churn, tests that echo implementation, catch-all except, unasked README, extra deps, duplicate AGENTS.md/CLAUDE.md, indexer-injected second H1s, and TODOs instead of finishing the claim.

## Why it matters for our harnesses

Greptile on LiteLLM #40744 objected to a test that only compared duplicated static JSON — that is slop, not coverage. Factory workers should shrink until a reviewer can name the issue in the first screen. Do not add a second loop or a manifesto in AGENTS.md; point at `skills/anti-slop`.

## Related

- [[literature/lit-20260911-agent-onboarding-tools]]
- [[permanent/perm-20260911-orient-before-edit]]
- [[permanent/perm-20260911-bots-advise-humans-merge]]
