---
id: perm-20260910-screenshots-bypass-vault-redaction
title: "Vault text redaction is not screenshot noninterference"
type: permanent
status: active
created: 2026-09-10
updated: 2026-09-10
harnesses: [hermes, omp]
domains: [information-theory, tool-use]
confidence: high
tags: [permanent, vault, screenshot]
---

# Vault text redaction is not screenshot noninterference

## Idea (atomic)

Hermes `register_vault_redaction_value` (`agent/redact.py`) exact-substring-scrubs later **text** tool results. `browser_vision` / screenshots / DOM dumps are not that function. After `browser_vault_fill`, the value can still sit in the page the model can look at.

OMP has the same class of hole: restore-in-tool-args, then `edit` diffs (#10027) and any browser screenshot of a filled field.

Acceptance test remains differential canaries: classifier over **everything** the agent VM can observe, including images. Grep-for-plaintext is not that test.

## Why it matters for our harnesses

Any identity-kind fill must freeze vision/screenshot (and CDP evaluate that returns `input.value`) on the bound origin until navigation away, or the fill is theater. That gate belongs in the vault-fill issue, not as a separate redact-screenshots product.

## Related

- [[permanent/perm-20260910-obfuscation-is-not-noninterference]]
- [[permanent/perm-20260910-custody-is-not-confinement]]
- [[harnesses/hermes]] · [[harnesses/omp]]
