---
id: perm-20260910-build-action-portal-not-password-manager
title: "Build a privileged action portal, not an AI password manager"
type: permanent
status: active
created: 2026-09-10
updated: 2026-09-10
harnesses: [hermes, omp, o8, grok, codex, claude, pi, fx]
domains: [cs, tool-use, frameworks]
confidence: high
tags: [permanent, secrets, broker, portal]
---

# Build a privileged action portal, not an AI password manager

## Idea (atomic)

The LLM should never call `get_secret("chase_password")`. Nothing in the agent-accessible RPC schema should be able to represent plaintext secret material. It requests `authenticate`, `sign_structured`, `submit_private_field`, or `request(route, credential_capability)`. The trusted component performs the action and returns a constrained result.

There is intentionally no `read_secret`, `decrypt_for_caller`, `export_cookie`, `raw_sign`, `eval_js`, or `arbitrary_authenticated_request`.

## Why it matters for our harnesses

Hermes and OMP already have vaults and redaction. Both still give the agent the effect of possessing the secret: env injection, restored tool args, agent-owned browser. The leapfrog is the portal API, composed from Secretless + ssh-agent + XDG portal + Cedar, not a second password manager.

Linear: [PER-1321](https://linear.app/0ism/issue/PER-1321) parent. Prototype leaf [PER-1327](https://linear.app/0ism/issue/PER-1327).

## Related

- [[literature/lit-20260910-trustworthy-secret-brokers]]
- [[permanent/perm-20260910-custody-is-not-confinement]]
- [[harnesses/hermes]]
- [[harnesses/omp]]
