---
id: lit-20260910-trustworthy-secret-brokers
title: "Trustworthy secret brokers for untrusted AI agents (deep research)"
type: literature
status: active
created: 2026-09-10
updated: 2026-09-10
sources: ["inbox/20260910-deep-research-secret-brokers.md", "https://github.com/cyberark/secretless-broker", "https://github.com/openssh/openssh-portable", "https://github.com/flatpak/xdg-desktop-portal", "https://github.com/cedar-policy/cedar", "https://github.com/openbao/openbao", "https://github.com/spiffe/spire", "https://github.com/NousResearch/hermes-agent/blob/main/website/docs/user-guide/secrets/index.md"]
harnesses: [hermes, omp, o8, grok, codex, claude, pi, fx]
domains: [cs, information-theory, tool-use, frameworks]
confidence: high
tags: [literature, secrets, broker, portal, noninterference]
---

# Trustworthy secret brokers for untrusted AI agents

## Claim (one sentence)

Do not build an AI password manager. Build a privileged action portal: the LLM requests a destination-bound effect, never `get_secret`, and plaintext never has a representation in any agent-accessible interface.

## Evidence

122 OSS/research systems surveyed. Ranked foundations (architectural fit, not popularity):

1. CyberArk Secretless Broker (91) — client never holds the password; still proxies full post-auth traffic
2. OpenSSH `ssh-agent` (90) — non-exportable operations, destination/lifetime/confirmation
3. XDG Desktop Portal (89) — sandboxed caller, validated request, permission store, trusted UI. Existing Secret portal is the *wrong* API because it exports a secret
4. Cedar (86) — analyzable principal/action/resource/context. Broker must attest context, not copy the model's claim
5. Trustee (84) — attest the broker before provisioning. An attested `get_secret()` is still an exfil service
6. OpenBao (83) — leases, dynamic secrets, revocation. Hide plaintext APIs from the agent
7. SPIRE (82) — workload identity, not action policy
8. Biscuit (81) — attenuable capabilities

SOTA composition the report names:

Secretless-style inject + ssh-agent operation APIs + XDG portal mediation + Cedar/Biscuit + SPIRE + OpenBao custody + trusted browser executor + Envoy/mitmproxy egress + optional Trustee/TEE + TPM/FIDO/HSM.

Largest missing OSS piece: semantic browser/form portal. Playwright/CDP, cookies, screenshots, and profile must stay on the trusted side.

Information-flow target is computational noninterference: agent-visible transcripts for secrets \(s_0,s_1\) should be indistinguishable except for explicitly authorized output \(O\). Threshold sharding is custody. Capability mediation is execution. IFC is leakage. Using only the first leaves the hard problem unsolved.

Hermes accepted stack (primary docs, 2026-09-10): Bitwarden Secrets Manager, 1Password, command helper (`secret-tool`, KeePassXC, `pass`). All hydrate `os.environ` at process start. That is OpenBao-class custody plus `get_secret` for the whole environment.

OMP: placeholder obfuscation in provider-visible text, restore in tool args; at-rest `auth_credentials` still plaintext (origin #11399). Prompt filter, not a broker.

## Fact vs interpretation

- Fact: Secretless, ssh-agent, XDG portal, Cedar, OpenBao, SPIRE, Biscuit exist and are maintained (several with 2026 release signals in the source note).
- Fact: Hermes ships BWS / 1Password / command helper as env injectors. Bundled set is closed; Infisical/Vault/keystores are plugins.
- Fact: OMP obfuscation restores secrets before tool execution.
- Interpretation: the valuable new work is a small reference monitor (`agent-portal.sock`) with no secret-return primitive, not a new vault.
- HOLD: github_writes=0 on origin Hermes/OMP until Linear children are Todo. Linear parent [PER-1321](https://linear.app/0ism/issue/PER-1321).

## Links

- Raw capture: [[inbox/20260910-deep-research-secret-brokers]]
- Linear: [PER-1321](https://linear.app/0ism/issue/PER-1321), ingest [PER-1322](https://linear.app/0ism/issue/PER-1322)
- Hermes secrets: https://github.com/NousResearch/hermes-agent/blob/main/website/docs/user-guide/secrets/index.md
- OMP #11399: https://github.com/can1357/oh-my-pi/issues/11399
