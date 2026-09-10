---
id: lit-20260910-keel-level0-evidence-surface
title: "Keel Level-0 evidence/capability surface (hermes-keel)"
type: literature
status: draft
created: 2026-09-10
updated: 2026-09-10
sources: ["https://github.com/kvnloo/hermes-keel", "https://github.com/kvnloo/hermes-keel/blob/main/docs/level-0-evidence.md", "https://github.com/kvnloo/hermes-keel/blob/main/keel-level.json", "https://kvnloo.github.io/hermes-keel/"]
harnesses: [hermes]
domains: [frameworks, tool-use]
confidence: high
tags: [literature, keel, level-0, evidence]
---

# Keel Level-0 evidence/capability surface (hermes-keel)

## Claim (one sentence)

Hermes Keel Level 0 is a constitutional/bootstrap spec that makes one invariant mechanically testable: the Telegram-facing default router cannot execute project work directly — proven via capability receipts + sealed nonce evidence, not model refusal prose.

## Evidence

- Repo kvnloo/hermes-keel states Level 0 only; no installable plugin / general execution backend yet.
- Machine card keel-level.json: level 0, state authorized, orderedActions (provision canary-worker, strip default capabilities, restart default gateway, verify inventory, router escape test, stop), forbidden product/FM/GPU/extra workers, promotion requires Captain for Level 1.
- Evidence pack evidence/level-0/t_c8dc8afb: PASS for Level 0 only; causal chain router to Kanban task to canary claim to nonce artifact to deterministic verify_level0.py.
- Capability closure: router inventory had no terminal/shell/code/project/delegation/git/browser/MCP escape; canary inventory did — boundary after canonical dispatch only.
- Invariant ladder Level 0..10 documented; only Level 0 authorized today.

## Fact vs interpretation

- Fact: Level 0 PASS + verifier script + capability inventory closure are repo artifacts.
- Interpretation: Right surface to expose to Hermes OSS as capability receipts / authorize fail-close without enabling keel.service or production mesh.poll.
- HOLD: do not start keel.service / production_enabled; github_writes=0 on origin NousResearch/hermes-agent until authorized.

## Links

- Spec source: https://github.com/kvnloo/hermes-keel
