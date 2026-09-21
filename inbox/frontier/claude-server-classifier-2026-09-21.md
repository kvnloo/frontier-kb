---
id: inbox-frontier-claude-server-classifier-2026-09-21
title: "Claude 2.1.278 — server auto-mode classifier + gateway safeguards"
type: inbox
status: draft
created: 2026-09-21
updated: 2026-09-21
node: frontier
harnesses: [claude-code]
domains: [ai-ml, frameworks, tool-use]
tags: [inbox, frontier, claude-code, gateway, auto-mode]
---

# Claude server auto-mode classifier

## Context

### FACT
- **v2.1.278:** auto-mode defaults to **server-side classifier** (no classifier charge) for API / Enterprise / Bedrock / Vertex / Foundry / gateways. `/status` shows Auto mode server row. Opt-out: `CLAUDE_CODE_AUTO_MODE_SERVER=0` (not on direct API).
- Gateways **must** forward `safeguards` / `safeguard_results` unchanged; else notice hold → billed local classifier.
- **v2.1.277:** AGENTS.md when no CLAUDE.md — four `instructionFiles` modes (`claude-md-or-agents-md` default, and/and, claude-only, managed-only); Bedrock/Vertex/Foundry need `@AGENTS.md`. `CLAUDE_GATEWAY_PROXY_IS_EGRESS_BOUNDARY=1` proxy-only SSRF; upstream `headers:` (reserved names refused).

### INTERPRETATION
- Fleet-critical compatibility tax for any Hermes/self-host gateway in front of Claude Code. Pin ≥2.1.278 and verify `/status` Auto mode server=Enabled after upgrade.
- AGENTS.md modes = cross-harness instruction-file convergence (shared with Codex/others).

## Next action

Pin Claude fleets ≥2.1.278; audit gateway protocol for safeguards pass-through; footnote llm-gateway-protocol. No Linear.

## Links

- https://github.com/anthropics/claude-code/releases/tag/v2.1.278
- https://github.com/anthropics/claude-code/releases/tag/v2.1.277
- https://code.claude.com/docs/en/auto-mode-classifier-billing
- https://code.claude.com/docs/en/memory.md
