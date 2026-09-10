---
id: harness-hermes
title: Hermes Agent
type: harness
status: active
created: 2026-09-09
updated: 2026-09-10
urls:
  - https://github.com/NousResearch/hermes-agent
  - https://hermes-agent.nousresearch.com/
  - https://github.com/NousResearch/hermes-agent/blob/main/website/docs/user-guide/secrets/index.md
  - https://github.com/NousResearch/hermes-agent/issues/107698
  - https://github.com/NousResearch/hermes-agent/issues/107700
  - https://github.com/NousResearch/hermes-agent/issues/107704
  - https://github.com/NousResearch/hermes-agent/issues/107705
capabilities:
  - bitwarden-secrets-manager
  - onepassword
  - command-helper-secret-tool
  - browser-vault-login-payment-address
  - Built-in learning loop: skills from experience, FTS5 session search, agent-curated memory
  - Messaging gateway: Telegram, Discord, Slack, WhatsApp, Signal, Email
  - Multi-backend compute: local, Docker, SSH, Singularity, Modal, Daytona, Vercel Sandbox
  - Nous Portal provider bundle; cron scheduler; subagents
gaps_vs_peers:
  - env-injection-not-action-portal
  - no-identity-kind
  - no-document-portal
  - screenshot-not-redacted
  - No native DAP debugger support (omp/crush lead here)
  - Rust-less (Python/uv) heavier resource profile than omp
  - Subagent worktree isolation less explicit than firstmate/crush
omp_actionable: true
confidence: high
tags: [harness]
---
# Hermes Agent

Snapshot: Self-improving agent with closed learning loop; built by Nous Research.
Strengths: Messaging gateway across platforms; run anywhere compute backends; scheduled automations; skill creation from experience.
Gaps: Python/uv stack heavier than omp Rust core; no real DAP integration; crew worktree isolation less explicit than crush/firstmate.
Sources: https://github.com/NousResearch/hermes-agent, https://hermes-agent.nousresearch.com/

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

## Orchestration IR (proposal only)

Hermes has execution primitives (Kanban, runs, leases, review, goal/judge) but no machine-readable topology vocabulary. HOTL 0.1/0.2 is the proposed IR at [kvnloo/aodl](https://github.com/kvnloo/aodl); **not merged**, no second scheduler.

- Catalog id `hermes`: [harnesses/catalog.json](https://github.com/kvnloo/aodl/blob/main/harnesses/catalog.json)
- [[literature/lit-20260817-hotl-01-issue-88589]] — upstream [issue #88589](https://github.com/NousResearch/hermes-agent/issues/88589)
- [[literature/lit-20260817-hotl-02-spec]]
- [[permanent/perm-20260817-intent-plan-observed]]
- [[permanent/perm-20260817-no-aodl-repo]]

Starmap/learning graph is a time-axis **projection** of memory, not orchestration edge semantics.

## Keel

- [[literature/lit-20260910-keel-level0-evidence-surface]]
