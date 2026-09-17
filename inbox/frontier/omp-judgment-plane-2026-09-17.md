---
id: inbox-frontier-omp-judgment-plane-2026-09-17
title: "OMP v18.2.2–18.2.4 — judgment + caret delegation"
type: inbox
status: draft
created: 2026-09-17
updated: 2026-09-17
node: frontier
harnesses: [omp]
domains: [ai-ml, frameworks, tool-use]
tags: [inbox, frontier, omp, judgment]
---

# OMP judgment plane

## Context

- **v18.2.4:** `Judge` / `TypeSafeJudge` / `TextJudge`; `providers.judgmentProvider` ∈ {auto,typesafe,llm}; unified thinking-level / unexpected-stop / AI-staging judgments; live `composer.tokenRate`
- **v18.2.3:** `^` model-tag → session agents `m1`/`m2`…; **breaking** async `resolveModelHeaders()`
- **v18.2.2:** Bedrock `baseUrl`; gateway session isolation; Anthropic `stop_reason: tool_use`

Does **not** reopen OMP-1..7.

## Next action

Productize judgment plane; note async header migration landmine. Align with Firstmate typesafe Choice pattern.

## Links

- https://github.com/can1357/oh-my-pi/releases/tag/v18.2.4
- https://github.com/can1357/oh-my-pi/releases/tag/v18.2.3
- https://github.com/can1357/oh-my-pi/releases/tag/v18.2.2
