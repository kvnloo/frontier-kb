---
id: harness-hermes
title: hermes
type: harness
status: active
created: 2026-09-09
updated: 2026-09-10
urls: ["https://github.com/NousResearch/hermes-agent", "https://github.com/NousResearch/hermes-agent/blob/main/website/docs/user-guide/secrets/index.md"]
capabilities: ["bitwarden-secrets-manager", "onepassword", "command-helper-secret-tool"]
gaps_vs_peers: ["env-injection-not-action-portal"]
omp_actionable: false
confidence: high
tags: [harness]
---

# hermes

Nous Hermes Agent. Accepted secret stack is **custody + env injection**, not SOTA mediation.

## Secrets (accepted vs SOTA)

Accepted (in-tree, docs 2026-09-10):

- Bitwarden Secrets Manager (`bws` → `os.environ`, override-by-default)
- 1Password (`op://`)
- Command helper (`secret-tool`, KeePassXC, `pass` → `KEY=VALUE`)
- Plugin `SecretSource` for Infisical/Vault/keystores. Bundled set is closed.

SOTA gap: no agent RPC should return plaintext. Need a privileged action portal in front of these backends.

[[permanent/perm-20260910-hermes-secrets-are-env-injection]] · Linear [PER-1323](https://linear.app/0ism/issue/PER-1323)

## Snapshot

Kanban scheduler, gateway/peer A2A, Telegram router. Privilege/sudo broker is a separate lane (PR #63066 / PER-110).

## Strengths

Vault backends exist, compose, and refuse to overwrite bootstrap tokens. Command helper matches zer0's `secret-tool` path.

## Gaps (leapfrog targets)

Action portal. Trusted browser executor. Destination-bound inject. Differential canary tests. Do not replace Bitwarden.

## Sources

- https://github.com/NousResearch/hermes-agent/blob/main/website/docs/user-guide/secrets/index.md
- [[literature/lit-20260910-trustworthy-secret-brokers]]
