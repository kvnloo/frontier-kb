---
id: lit-20260910-agent-http-inject-brokers
title: "Coding-agent HTTP inject brokers (Infisical Agent Proxy, HASP, OneCLI)"
type: literature
status: active
created: 2026-09-10
updated: 2026-09-10
sources: ["https://infisical.com/docs/documentation/platform/agent-proxy/local-agent-proxy", "https://github.com/gethasp/hasp", "https://github.com/onecli/onecli"]
harnesses: [hermes, omp]
domains: [cs, frameworks, tool-use]
confidence: high
tags: [literature, secrets, broker, wrap]
---

# Coding-agent HTTP inject brokers

## Claim (one sentence)

The 2026 product that already does destination-bound **API-key** inject is a process wrap (Infisical Agent Proxy, HASP), not a new vault and not an in-tree SecretSource.

## Evidence

- **Infisical Agent Proxy**: `infisical secrets agent-proxy run -- claude` (or `-- hermes` / `-- omp`). Sandbox (bubblewrap/seatbelt), scrub env, only egress is a local MITM that rewrites headers / substitutes placeholders for allowlisted hosts.
- **HASP** (https://github.com/gethasp/hasp): local encrypted vault, `hasp_run` / `hasp_inject`, first-class Hermes profile. Grants: once / session / window. Built for provider keys, not SSN.
- **OneCLI**: heavier HTTP/WebSocket gateway + body transform + approvals.
- **OMP already injects model provider keys in-tree:** `packages/ai/src/auth-gateway/server.ts` foreign-wire → `streamSimple`. Clients never see the access token. Infisical/HASP compose as a **sibling** wrap for tool-facing GitHub/AWS keys (the `deobfuscateToolArguments` hole), not as a new `AuthCredentialStore`. #11399 stays field-encrypt of the sqlite blob.
- Hermes #22791 closed Infisical-as-in-tree-vault not-planned. Same placement: wrap outside core.

## Fact vs interpretation

Fact: wrap products exist so the model never holds the GitHub/AWS token. OMP's auth-gateway already does that for **model** credentials.
Interpretation: Infisical/HASP are Phase 1 wrap for Hermes env-apply and OMP restore-in-tool-args for **tool** credentials. They are not identity/document portals and they do not replace OMP auth-broker.

## Links

- Hermes origin: https://github.com/NousResearch/hermes-agent/issues/107698 (docs), https://github.com/NousResearch/hermes-agent/issues/107700 (handles/wrap)
- [[permanent/perm-20260910-build-action-portal-not-password-manager]]
- [[harnesses/hermes]] · [[harnesses/omp]]
