---
id: harness-hermes
title: Hermes Agent
type: harness
status: active
created: 2026-09-09
updated: 2026-09-12
urls:
  - https://github.com/NousResearch/hermes-agent
  - https://hermes-agent.nousresearch.com/
  - https://github.com/NousResearch/hermes-agent/blob/main/website/docs/user-guide/secrets/index.md
  - https://github.com/NousResearch/hermes-agent/issues/107698
  - https://github.com/NousResearch/hermes-agent/issues/107700
  - https://github.com/NousResearch/hermes-agent/issues/107704
  - https://github.com/NousResearch/hermes-agent/issues/107705
  - https://github.com/NVlabs/SoL-Pi
  - https://hermes-agent.nousresearch.com/docs/developer-guide/plugins
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
  - No Pi ExtensionAPI; SoL-Pi TS package will not load
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

## SoL-Pi (port, do not import)

SoL-Pi is a TypeScript Pi extension. Hermes integration is a **standalone Python plugin** (`~/.hermes/plugins/sol-pi/`, `register(ctx)`), not a PR into `hermes-agent` (`github_writes=0`) and not `pip install` of the npm package. A thin Hermes↔Pi plugin ABI is not thin — share policy across two host ports. Hermes Agent Plugins v1.0.0 is not Pi ExtensionAPI. See [[permanent/perm-20260911-hermes-pi-plugin-adapter-is-host-port-not-abi]].

| Mechanism | Hermes seam | Trap |
| --- | --- | --- |
| Action Fusion | `register_tool` wrapping file tools + optional `terminal` `then_run` | Tool names are not Pi `edit`/`write` |
| ObservationPack | session archive + `obs_recall` + **request-time** rewrite | `transform_tool_result` mutates stored history; SoL-Pi does not. Prefer context-engine `select_context` **composed** with the default compressor |
| EPR | `transform_tool_result` + auxiliary reducer model | Quote-verify against archive; skip likely-secret; fail open |
| OCC | plan-boundary around built-in compressor | Only one `ContextEngine` may register; do not clobber `ContextCompressor` |

[[literature/lit-20260911-sol-pi-harness-efficiency]] · [[permanent/perm-20260911-hermes-sol-pi-is-a-python-plugin-port]] · [[permanent/perm-20260911-observationpack-is-projection-not-history-rewrite]]

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

## FlyForge P0 (recovery specialist, not a planner swap)

Research program (not implemented in this vault): typed operational events → bounded recovery action → external verifier. Qwen3.8-27B remains the language worker and escalation model. A GRU/motif/reservoir student is an AODL **executor** port. Keel L0 still forbids the default router from doing project work; the specialist must not see secret-bearing payloads.

Local runner: [kvnloo/evolution-lab](https://github.com/kvnloo/evolution-lab) (JSONL archive, ΔHV, learned-only front). Tinker is a declared backend that currently refuses.

- [[literature/lit-20260912-flyforge-research-roadmap]]
- [[permanent/perm-20260912-p0-is-verified-hermes-recovery]]
- [[permanent/perm-20260912-fly-specialist-is-an-aodl-port]]
- Linear [PER-944](https://linear.app/0ism/issue/PER-944) stays a WebGPU viewer, not this controller.

## Keel

- [[literature/lit-20260910-keel-level0-evidence-surface]]
