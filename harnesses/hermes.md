---
id: harness-hermes
title: hermes
type: harness
status: active
created: 2026-09-09
updated: 2026-09-10
urls: ["https://github.com/NousResearch/hermes-agent", "https://github.com/NousResearch/hermes-agent/blob/main/website/docs/user-guide/secrets/index.md", "https://github.com/NousResearch/hermes-agent/issues/107698", "https://github.com/NousResearch/hermes-agent/issues/107700", "https://github.com/NousResearch/hermes-agent/issues/107704", "https://github.com/NousResearch/hermes-agent/issues/107705"]
capabilities: ["bitwarden-secrets-manager", "onepassword", "command-helper-secret-tool", "browser-vault-login-payment-address"]
gaps_vs_peers: ["env-injection-not-action-portal", "no-identity-kind", "no-document-portal", "screenshot-not-redacted"]
omp_actionable: false
confidence: high
tags: [harness]
---

# hermes

Nous Hermes Agent. Two secret systems, not one pile.

## Secrets (accepted vs SOTA)

**Sources (custody):** Bitwarden SM (`bws` → `os.environ`), 1Password, command helper. Plugin `SecretSource`. Bundled set closed (#22791).

**Vault (browser fill):** #106480 / #107585. Kinds: login / payment / address. Origin-bound, password-blind, supervisor CDP. No SSN/file kind.

**Origin we filed:** [#107698](https://github.com/NousResearch/hermes-agent/issues/107698) docs `--apply` warning. [#107700](https://github.com/NousResearch/hermes-agent/issues/107700) handles for tool credentials + wrap (Infisical/HASP), not vendored. [#107704](https://github.com/NousResearch/hermes-agent/issues/107704) identity field kind + vision freeze. [#107705](https://github.com/NousResearch/hermes-agent/issues/107705) documents are not vault items.

SOTA gap left: those four issues are still open. Vault kinds remain login/payment/address until #107704 lands. Someone already asked to be assigned on #107700.

[[permanent/perm-20260910-hermes-secrets-are-env-injection]] · [[permanent/perm-20260910-hermes-vault-is-login-payment-address]] · Linear [PER-1323](https://linear.app/0ism/issue/PER-1323)

## Snapshot

Kanban scheduler, gateway/peer A2A. Privilege/sudo broker is a separate lane (PR #63066 / PER-110).

## Strengths

Vault fill is the OpenInstinct port. Sources compose and refuse to overwrite bootstrap tokens. Teknium issue shape: Overview → gap today → Current State (files) → phased plan + gates → what this is not.

## Gaps (leapfrog targets)

Stop applying tool secrets into untrusted children. Identity kind + vision freeze. Documents via Skyflow/VGS wrap, not `hermes vault add`. Plaid (#12324) for bank, not Playwright.

## Sources

- https://github.com/NousResearch/hermes-agent/blob/main/website/docs/user-guide/secrets/index.md
- [[literature/lit-20260910-trustworthy-secret-brokers]]
- [[literature/lit-20260910-agent-http-inject-brokers]]
- [[literature/lit-20260910-pii-tokenization-vaults]]
