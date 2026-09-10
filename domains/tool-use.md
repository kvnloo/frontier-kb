---
id: domain-tool-use
title: tool-use
type: moc
status: active
created: 2026-09-09
updated: 2026-09-10
tags: [moc, domain]
---

# tool-use

Map of content for [[atlas/home]].

## Secret-bearing tools

Agent-facing tools must not return secrets or own CDP. Typed action RPC: `authenticate`, `sign_structured`, `submit_private_field`.

- [[permanent/perm-20260910-build-action-portal-not-password-manager]]
- [[permanent/perm-20260910-hermes-secrets-are-env-injection]]
- [[permanent/perm-20260910-obfuscation-is-not-noninterference]]
- [[permanent/perm-20260910-hermes-vault-is-login-payment-address]]
- [[permanent/perm-20260910-identity-fields-are-not-documents]]
- [[permanent/perm-20260910-screenshots-bypass-vault-redaction]]

## Specialist retrieval and editor ABI

SWE-grep pattern: typed file+line hand-off. `str_replace` vs bash can move 27B SWE-bench by ~20 points.

- [[literature/lit-20260910-swe-grep]]
- [[permanent/perm-20260910-specialist-subagent-handoff]]
- [[permanent/perm-20260910-scaffold-tool-shape-dominates]]
