---
id: inbox-frontier-harness-release-cluster-2026-09-24
title: "Harness release / DX cluster — 2026-09-24"
type: inbox
status: draft
created: 2026-09-24
updated: 2026-09-24
node: frontier
harnesses: [hermes, omp, claude-code, codex, cursor, prime-intelligence, pi, firstmate, o8]
domains: [frameworks, tool-use, tokenomics]
tags: [inbox, frontier, releases, dx]
---

# Harness release / DX cluster (KB footnote)

## Context

### FACT
- **Hermes v2026.9.24 / v0.21.5** (2026-09-24T10:09:38Z): Desktop plugin SDK (`SandboxedFrame` #120927, `broadcast_plugin_event` #120918); Connectors; temporary `gateway.standalone` (#119680); Windows state.db holders (#121423); compression watermark (#121489); `/review` secret-scope (#117550). Curated notes → **v0.22.0**. https://github.com/NousResearch/hermes-agent/releases/tag/v2026.9.24
- **OMP v18.3.0** (2026-09-24T02:21:31Z): hub→`wait`/`proc://`/`agent://`; ephemeral turns (`ctx.runEphemeralTurn`); Apple Foundation Models; Anthropic `compact-2026-09-04` + cross-cred thinking redaction; `/annotate`; hub deprecation. https://github.com/can1357/oh-my-pi/releases/tag/v18.3.0
- **Claude Code 2.1.281**: gateway Desktop keys + Bedrock `assume_role`/guardrails; MCP URL elicitation; resume/proxy/cache plane. https://github.com/anthropics/claude-code/releases/tag/v2.1.281
- **Cursor Sep 23:** Rollouts + Security Review bots. https://cursor.com/changelog/rollouts-and-security-reviewer · https://cursor.com/blog/rollouts-and-security-reviewer
- **Codex:** GA still **0.156.1**; watch **rust-v0.158.0-alpha.8** Guardian/AgentControl/network-policy. https://github.com/openai/codex/releases/tag/rust-v0.158.0-alpha.8
- **Prime v0.9.6:** `auxiliaryModel` branch+compaction (no session-cache pollution) + incident CLI. https://github.com/PrimeIntellect-ai/prime-agent/releases/tag/v0.9.6
- **SEP-2640** Skills-over-MCP Final (`skills/list`/`get`, `skill://` digests). https://modelcontextprotocol.io/extensions/skills/overview
- Thin: **AEWM** 2609.28416; **SWE-Flux** 2609.28449 (best 37%); **ProCredit** 2609.27532; **FDE-Bench** 2609.27571; pi Chord canonical (consumer still **0.87.1**); Firstmate Claude-away #5488; o8 peer turn budget #2697.

### INTERPRETATION
- Strongest product/DX beat this window is Hermes Desktop SDK + OMP process URI plane + Cursor last-mile bots — not a model event.
- **Hold OMP-1..7** + **keel L0** + **Kevin sleep HOLD (no pin stamps until go)**. Do not build fleets on `gateway.standalone`.

## Next action

Stub fills in this PR. CoS: research steals only until pin go. No Linear.

## Links

- Umbrella: [[inbox/frontier/kb-autoresearch-2026-09-24]]
- Stubs: [[harnesses/hermes]], [[harnesses/omp]], [[harnesses/claude-code]], [[harnesses/codex]], [[harnesses/cursor]], [[harnesses/prime-intelligence]], [[harnesses/pi]]
- Thin lit cluster: [[inbox/frontier/arxiv-agent-eval-cluster-2026-09-24]]
