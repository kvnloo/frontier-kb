---
id: perm-20260910-custody-is-not-confinement
title: "Custody is not confinement"
type: permanent
status: active
created: 2026-09-10
updated: 2026-09-10
harnesses: [hermes, omp]
domains: [cs, information-theory]
confidence: high
tags: [permanent, secrets, custody, noninterference]
---

# Custody is not confinement

## Idea (atomic)

\[
\text{custody} \neq \text{authorization} \neq \text{information flow}
\]

OpenBao / Bitwarden Secrets Manager / `secret-tool` excel at storing, rotating, and leasing material. They do not confine what an agent may *do* once a value is in process memory, an authenticated socket, or a browser profile.

Secretless Broker is the exhibit: the client can be perfectly secretless and still receive a powerful authenticated channel. `ssh-agent` is explicit that `SSH_AUTH_SOCK` is itself valuable authority.

Threshold sharding is a custody primitive. After reconstruction, secret sharing says nothing about the broker RPC. Destination restriction is part of noninterference: `send_secret(handle, attacker.com)` is `read_secret`.

## Why it matters for our harnesses

zer0's BWS + `secret-tool` path is the right custody backend. Keep it. Do not treat `hermes secrets bitwarden sync --apply` or `bws secret get` as the broker. PER-254 stays (enable BWS). PER-1325 is the policy: custody only.

## Related

- [[literature/lit-20260910-trustworthy-secret-brokers]]
- [[permanent/perm-20260910-build-action-portal-not-password-manager]]
- [[permanent/perm-20260910-hermes-secrets-are-env-injection]]
