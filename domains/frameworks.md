---
id: domain-frameworks
title: frameworks
type: moc
status: active
created: 2026-09-09
updated: 2026-09-12
tags: [moc, domain]
---

# frameworks

Map of content for [[atlas/home]].

## Secret action portal (compose, do not invent)

Secretless + ssh-agent + XDG portal + Cedar/Biscuit + OpenBao/BWS custody + trusted browser.
HTTP wrap: Infisical Agent Proxy / HASP. Field PII: Skyflow/VGS. Bank: Plaid. Hermes vault already covers login/payment/address.

- [[literature/lit-20260910-trustworthy-secret-brokers]]
- [[literature/lit-20260910-agent-http-inject-brokers]]
- [[literature/lit-20260910-pii-tokenization-vaults]]
- [[permanent/perm-20260910-build-action-portal-not-password-manager]]
- [[permanent/perm-20260910-identity-fields-are-not-documents]]

## Coding scaffolds (replace the loop, do not wrap it)

mini-swe-agent, OpenHands SDK, OpenDev slots, Live-SWE-agent. No universal sidecar for OMP/Hermes.

- [[literature/lit-20260910-oss-coding-plugins]]
- [[permanent/perm-20260910-no-universal-harness-plugin]]
- [[permanent/perm-20260910-scaffold-tool-shape-dominates]]

## Harness evolution (frozen worker + evolver)

Evo-Bench / GSME: a second model edits the executable harness around a frozen policy. Not a plugin wrapping OMP.

- [[literature/lit-20260910-evo-bench-harness-evolution]]
- [[literature/lit-20260910-gsme-self-evolving-harness]]
- [[permanent/perm-20260910-evolver-lifts-frozen-policy]]

## Machine store (100-writer)

Postgres CAS + markdown projection (Cognee 1.0 shape, not a Cognee vendor). Graphiti is a later retrieval overlay. Host: PC 0 over Tailscale. Neon is fallback. PAIR/keel stay their own planes.

- [[literature/lit-20260910-agent-memory-postgres]]
- [[literature/lit-20260910-agent-kb-concurrency]]
- [[literature/lit-20260910-kb-hosting-postgres]]
- [[literature/lit-20260910-kb-mesh-pair-keel]]
- [[permanent/perm-20260910-git-vault-fails-at-100-writers]]
- [[permanent/perm-20260910-postgres-is-the-operational-kb]]
- [[permanent/perm-20260910-postgres-cas-plus-markdown-projection]]
- [[permanent/perm-20260910-vault-to-sota-is-dsn]]
- [[permanent/perm-20260910-host-kb-on-pc0-tailnet]]
- [[permanent/perm-20260910-host-on-neon-pooled-postgres]]

## Orchestration IR

Agent orchestration is a typed dynamic graph \(O_t\), not a static DAG or a named badge. Public IR: [kvnloo/aodl](https://github.com/kvnloo/aodl). C(RAID) is a named hybrid over that IR ([[permanent/perm-20260910-craid-is-named-hybrid]]); Blueprint is the product goal.

- [[permanent/perm-20260817-orchestration-typed-dynamic-graph]]
- [[permanent/perm-20260817-intent-plan-observed]]
- [[permanent/perm-20260817-aodl-ir-first]]
- [[permanent/perm-20260817-no-aodl-repo]]
- [[permanent/perm-20260910-craid-is-named-hybrid]]
- Sources: [[literature/lit-20260817-aodl-voice-transcript]] · [[literature/lit-20260817-hotl-01-issue-88589]] · [[literature/lit-20260817-hotl-02-spec]] · [[literature/lit-20260910-craid-blueprint]]
- Fly recovery student = existing kinds as a **port**, not HOTL 0.3. [[permanent/perm-20260912-fly-specialist-is-an-aodl-port]] · [[literature/lit-20260912-aodl-fly-specialist-port-sketch]] · [[permanent/perm-20260912-p0-is-verified-hermes-recovery]]

Market/auction routing lives under [[domains/tokenomics]] as policy \(\Pi_t\), not as a separate topology.
