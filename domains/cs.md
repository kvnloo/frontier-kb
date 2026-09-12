---
id: domain-cs
title: cs
type: moc
status: active
created: 2026-09-09
updated: 2026-09-12
tags: [moc, domain]
---

# cs

Map of content for [[atlas/home]].

## Privilege separation / capabilities

Protected-subsystem + complete mediation (Saltzer/Schroeder). XDG portal, ssh-agent, Capsicum, Secretless as reusable brokers.

- [[literature/lit-20260910-trustworthy-secret-brokers]]
- [[literature/lit-20260910-agent-http-inject-brokers]]
- [[literature/lit-20260910-pii-tokenization-vaults]]
- [[permanent/perm-20260910-build-action-portal-not-password-manager]]
- [[permanent/perm-20260910-custody-is-not-confinement]]
- [[permanent/perm-20260910-identity-fields-are-not-documents]]
- [[permanent/perm-20260910-screenshots-bypass-vault-redaction]]

## Concurrent knowledge store

Git is the review log. Postgres CAS is the 100-writer ledger. Host on PC 0 over Tailscale; Neon is fallback.

- [[literature/lit-20260910-agent-kb-concurrency]]
- [[literature/lit-20260910-agent-memory-postgres]]
- [[literature/lit-20260910-kb-hosting-postgres]]
- [[permanent/perm-20260910-git-vault-fails-at-100-writers]]
- [[permanent/perm-20260910-postgres-cas-plus-markdown-projection]]
- [[permanent/perm-20260910-postgres-is-the-operational-kb]]
- [[permanent/perm-20260910-vault-to-sota-is-dsn]]
- [[permanent/perm-20260910-host-kb-on-pc0-tailnet]]
- [[permanent/perm-20260910-host-on-neon-pooled-postgres]]

## Process / graph models

Orchestration as a typed dynamic graph and IR (not a pretty DSL). Audit Petri nets, BPMN, CWL, actors, FIPA Contract Net before inventing a calculus.

- [[permanent/perm-20260817-orchestration-typed-dynamic-graph]]
- [[permanent/perm-20260817-aodl-ir-first]]
- [[literature/lit-20260817-hotl-02-spec]]

## Sparse graphs vs dense mats

Connectome SNN = CSR + LIF + labels. Transformer = dense matmul + tokens. Freeze-backbone / train-adapter is the shared CS move (mushroom body, LoRA, evolver-around-frozen-worker). [[permanent/perm-20260912-mushroom-body-is-the-only-plastic-specialist]] · [[permanent/perm-20260912-optimize-fly-via-mb-pinout-substrate]]
