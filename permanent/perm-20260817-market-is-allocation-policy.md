---
id: perm-20260817-market-is-allocation-policy
title: "A marketplace is an allocation policy inside O_t, not a separate product"
type: permanent
status: active
created: 2026-09-10
updated: 2026-09-10
harnesses: [hermes, grok, omp, codex]
domains: [tokenomics, frameworks]
confidence: high
tags: [permanent, tokenomics, marketplace]
---

# A marketplace is an allocation policy inside O_t, not a separate product

## Idea (atomic)

Static routing is `controller → Claude Code`. A supervisor fans out to Codex / OMP / Hermes. A market is the same graph with different \(\Pi_t\):

\[
T \xrightarrow{\text{auction}} \{A_i\} \quad A_i \xrightarrow{\text{bid}(p,c,t,q)} T \quad T \xrightarrow{\text{award}} A_k
\]

Phases: announce → bid → award → execute → verify → settle. Bid fields: price, cost, time, quality/confidence, capabilities, terms. Trust, escrow, and payment boundaries are explicit. **Autonomous finance is unsupported.**

This is the compression of Factorio → software factory → agent marketplace: one controller learns policies over dynamic resource-constrained graphs; Factorio, software, orchestration, and company ops are instantiations.

## Why it matters for our harnesses

Dash “connect-all” / grok-bot / cheap Groq-Cerebras routing is an **allocation policy**, not a new topology. Tokenomics notes should treat routing and budgets as \(\Gamma_t\) / \(\Pi_t\), not as a separate ledger. HOTL 0.2 forbids hidden payment and undeclared privileged capability.

## Related

- [[permanent/perm-20260817-orchestration-typed-dynamic-graph]]
- [[domains/tokenomics]]
- [[literature/lit-20260817-hotl-02-spec]]
