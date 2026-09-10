---
id: perm-20260910-hermes-vault-is-login-payment-address
title: "Hermes vault is origin-bound login/payment/address fill, not an identity store"
type: permanent
status: active
created: 2026-09-10
updated: 2026-09-10
harnesses: [hermes]
domains: [tool-use]
confidence: high
tags: [permanent, hermes, vault]
---

# Hermes vault is origin-bound login/payment/address fill

## Idea (atomic)

Teknium closed #96970 as "building this as a PR." Landed 2026-09-10:

- #106480 `browser_vault_fill` — password-blind, origin-bound, supervisor CDP only (no argv)
- #107585 TOTP / `browser_vault_enter_code`

Kinds in `agent/vault_store.py`: **login | payment | address**. Payment fill requires human confirm. Model result is `{filled_fields, kind, origin, success}`. Exact secret bytes go to `register_vault_redaction_value` so later **text** browser results cannot echo them.

There is no SSN, tax id, passport, or file kind. `hermes vault add --kind` only offers login/payment/address.

## Why it matters for our harnesses

Do not ask Hermes to invent OpenInstinct. They shipped it. Follow-ups extend the vault contract (new kind + classifier tokens + payment-class confirm) or stay out of tree (wrap / Skyflow). #107698 warns off BWS apply for identity; the vault still has nowhere to put it.

## Related

- [[literature/lit-20260910-pii-tokenization-vaults]]
- [[permanent/perm-20260910-hermes-secrets-are-env-injection]]
- [[harnesses/hermes]]
