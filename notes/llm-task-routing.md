---
id: note-20260909-llm-task-routing
title: LLM Task Routing Pattern Catalog
type: permanent
status: draft
created: 2026-09-09
updated: 2026-09-09
harnesses: [omp, hermes, opencode, cursor, codex]
domains: [ai-ml, frameworks]
confidence: medium
tags: [permanent, routing, free-pool, benchmarks]
---

# LLM Task Routing Pattern Catalog

## Problem Statement

Intelligent task→model routing must balance capability, cost, and availability. The core challenge: prefer **free pools** (OpenCode Zen free Muse Spark tier, OpenRouter free endpoints, Nous Research free tier, Vercel AI SDK free-tier models) before consuming paid OAuth weekly caps (xAI API, Codex subscriptions, Cursor Pro quotas).

**FACT:** OpenCode Zen offers free Muse Spark tier access. ([opencode.zen](https://opencode.zen) free tier)

**THIN:** Specific webdev performance ranks for Muse Spark models are not publicly documented. Capability assertions require benchmark validation.

## Ranked OSS Router Implementations

Listed by sophistication and real-time benchmark integration:

1. **mcp-bench-router** — DesignArena realtime consumer ([DesignArena API](https://designarena.io/api)), end-to-end bench-aware routing **FACT**
2. **LiteLLM `auto_router`** — fallback chains, latency tracking ([LiteLLM docs](https://docs.litellm.ai/docs/routing))
3. **OMP roles/fallbackChains** — declarative role-based routing ([OMP routing](https://github.com/openmp/omp))
4. **Hermes OpenRouter routers** — wrapper abstractions for OR free tiers
5. **RouteLLM** — learned routing for cost/quality trade-offs ([RouteLLM GitHub](https://github.com/lm-sys/routellm))
6. **LLMRouter** — rule-based multi-provider routing
7. **semantic-router** — intent-based semantic routing ([semantic-router](https://github.com/aurelio-labs/semantic-router))
8. **vllm semantic-router** — VLLM integration layer
9. **automix** — mixture-of-models orchestration

**Observability:** ClawTrace + AgentTrace provide token/cost postmortem analysis.

## DesignArena Benchmark Integration

**FACT:** DesignArena publishes real-time model Elo rankings for web development tasks via public API: `https://designarena.io/api/leaderboard`

**FACT:** Only `mcp-bench-router` consumes DesignArena rankings end-to-end for routing decisions.

**INTERPRETATION:** Other routers (LiteLLM, OMP, Hermes) lack native DesignArena integration; manual config mappings required.

## Routing Decision Levers

1. **Latency budgets** — TTFT, token throughput SLOs
2. **Quota tracking** — weekly caps per provider (Cursor Pro, xAI API)
3. **Capability filters** — tool-use support (function calling), context window, modality
4. **Task type classification** — webdev, data science, sysadmin, research
5. **Tool availability** — local tool execution (MCP servers, filesystem access)
6. **Personal evals** — user-specific preference/performance history

## Proposed Free-Pool-First Policy

**INTERPRETATION:** Optimal routing order for cost efficiency:

1. **Task classification** — infer domain/complexity from prompt
2. **Free pool intersection** — filter `free ∩ capable` models
3. **DesignArena ranking** — for webdev tasks, prefer highest Elo among free pool
4. **Latency/quota secondary** — break ties by availability
5. **Paid fallback last** — consume OAuth quotas only when free pools exhausted

**THIN:** This policy is proposed but not implemented in any production harness. Requires validation through A/B testing.

## Zer0 Factory Mapping (On Hold)

**INTERPRETATION:** Natural home for free-pool-first routing:

- `skills/route-model` — skill invoked before task delegation
- Done sidecar service — background quota/cost tracking
- Integration with `domains/tokenomics.md` postmortem analysis
- AgentTrace / ClawTrace pairing for audit trails

**Status:** Held pending OMP foundational work.

## Proposed Implementation Leaves

1. **OMP #5018-adjacent** — free-pool-first routing PR (GitHub issue reference needed)
2. **mcp-bench-router `preferFree` flag** — factory method for free-tier-first instances
   - **THIN:** This is a planned feature, not yet implemented
   - Would expose `createRouter({ preferFree: true, fallbackToPaid: true })`

## Current Gaps

**FACT:** None of OMP, Hermes, OpenCode Zen, or Cursor combine:
- DesignArena real-time Elo integration
- Free-pool-first cost policy
- Transparent quota tracking

**INTERPRETATION:** Building this requires:
- DesignArena API polling infra
- Multi-provider credential management (OR, Nous, Vercel, xAI, Cursor)
- Task→domain classifier (lightweight prompt analysis or learned)
- Observability hooks (ClawTrace/AgentTrace)

## Why It Matters for Our Harnesses

Intelligent routing directly reduces operational costs while maintaining quality:
- Cursor Pro quota conservation → fewer monthly overages
- xAI API weekly cap management → predictable billing
- Free-tier maximization → zero marginal cost for routine tasks
- Benchmark-aware selection → quality floor enforcement

## Related

- [[domains/tokenomics]] — cost attribution and postmortem analysis
- [[domains/frameworks]] — router implementation patterns
- [[harnesses/omp]] — role-based routing foundation
- [[harnesses/cursor]] — quota management and fallback chains
- [[harnesses/opencode]] — free Muse Spark tier access
