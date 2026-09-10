---
id: perm-20260910-hermes-secrets-are-env-injection
title: "Hermes secrets are env injection, not an action portal"
type: permanent
status: active
created: 2026-09-10
updated: 2026-09-10
harnesses: [hermes]
domains: [tool-use]
confidence: high
tags: [permanent, hermes, secrets]
---

# Hermes secrets are env injection, not an action portal

## Idea (atomic)

Hermes' accepted secret stack (docs, in-tree) is:

- Bitwarden Secrets Manager via `bws` (bundled, auto-install, `os.environ` at startup, override-by-default)
- 1Password via `op://`
- Command helper: any CLI that prints `KEY=VALUE` (`secret-tool`, KeePassXC, `pass`)
- Plugin `SecretSource` for everything else (Infisical, Vault, OS keystores). Bundled set is closed on purpose.

The bootstrap token lives in `.env`. Every other key is fetched and **injected into the process environment**. `hermes secrets bitwarden sync --apply` is the honest name for the current API.

That matches SOTA **custody**. It fails SOTA **mediation**: the agent, tools, cron, and child processes see plaintext. Desktop keychain encryption is opt-in and still serves values to the app.

## Why it matters for our harnesses

zer0 already selected this stack (BWS + `secret-tool`). Do not replace Bitwarden. Put an action portal **in front** of it. Origin posted: [#107698](https://github.com/NousResearch/hermes-agent/issues/107698) (docs), [#107700](https://github.com/NousResearch/hermes-agent/issues/107700) (handles/wrap). Linear [PER-1323](https://linear.app/0ism/issue/PER-1323). Distinct from privilege/sudo broker [PER-110](https://linear.app/0ism/issue/PER-110) and from the vault fill that already landed (#106480).

## Related

- [[literature/lit-20260910-trustworthy-secret-brokers]]
- [[permanent/perm-20260910-custody-is-not-confinement]]
- [[harnesses/hermes]]
