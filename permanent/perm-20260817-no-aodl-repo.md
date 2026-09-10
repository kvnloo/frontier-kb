---
id: perm-20260817-no-aodl-repo
title: "AODL is published as kvnloo/aodl from HOTL 0.2"
type: permanent
status: active
created: 2026-09-10
updated: 2026-09-10
harnesses: [hermes]
domains: [frameworks]
confidence: high
tags: [permanent, aodl, provenance]
---

# AODL is published as kvnloo/aodl from HOTL 0.2

## Idea (atomic)

The formal language is now at **[kvnloo/aodl](https://github.com/kvnloo/aodl)** (`726335e`). It starts from HOTL 0.2 IR/schema/validator, not a new DSL.

Still true:

1. ChatGPT voice thread is not fully recovered and is **not** in the public repo
2. Hermes paste `118824` remains private
3. HOTL 0.1 + 0.2 docs originated on groot (`t_7432ab2d`, `t_83991e68`)
4. Upstream issue remains [NousResearch/hermes-agent#88589](https://github.com/NousResearch/hermes-agent/issues/88589) — do not file a duplicate

`kvnloo/flow` is a Ratatui swarm TUI. zerOS `AgentCoreLanguage.jsx` + `docs/research/2026-07-13-agent-orchestration-topologies.md` are **badge UI**, not the calculus. Desktop `ao` is a different product.

## Why it matters for our harnesses

Do not invent a second spec. Extend `kvnloo/aodl` + #88589. Dash should not grow a parallel orchestration language.

## Related

- [[literature/lit-20260817-aodl-voice-transcript]]
- [[literature/lit-20260817-hotl-02-spec]]
- [[harnesses/hermes]]
