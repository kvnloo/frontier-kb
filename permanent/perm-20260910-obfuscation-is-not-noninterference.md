---
id: perm-20260910-obfuscation-is-not-noninterference
title: "Obfuscation is not noninterference"
type: permanent
status: active
created: 2026-09-10
updated: 2026-09-10
harnesses: [omp]
domains: [information-theory, tool-use]
confidence: high
tags: [permanent, omp, secrets]
---

# Obfuscation is not noninterference

## Idea (atomic)

Replacing provider-visible secret bytes with `$$HASH$$` and restoring them in tool arguments is a prompt filter. A fully malicious agent still sees restored values at execution, owns CDP/Playwright, and can distinguish canary secrets \(s_0,s_1\) through tool results, screenshots, diffs, errors, and timing.

File:symbol (verified 2026-09-10): `secrets/index.ts:buildSecretObfuscator`; `obfuscator.ts:SecretObfuscator`; `message-transform.ts:obfuscateProviderContext` (messages only — **system prompt and tool schemas unwalked**); `deobfuscateToolArguments` JSON-walk of model-authored args; `sdk.ts:transformToolCallArguments`; `deobfuscateSessionContext` restores assistant/branch/compaction only. Images skipped. Thinking/signatures stay byte-identical.

The report's acceptance test is differential: two same-shape canaries, record **everything** the agent VM can observe, classifier cannot tell which secret was used beyond authorized output \(O\). Grep-for-plaintext is not that test.

At-rest encryption of `auth_credentials` (OMP #11399) is custody at `sqlite-credential-store.ts:serializeCredential|deserializeCredential`. Necessary. Not the portal. Do not replace SQLite with Infisical: OAuth rows mutate ~60s with lease fencing. Restore-in-tool-args is the Hermes `--apply` equivalent for **tool** keys. Provider keys already inject at `auth-gateway/server.ts` via `streamSimple`. CONTRIBUTING: do not file an issue for a PR you are about to open (robomp pickup); Discord-first for architecture.

## Why it matters for our harnesses

OMP leapfrog vs Hermes is not "better redaction." It is refusing agent-owned browser sessions and secret-return RPCs, and not restoring `GITHUB_TOKEN` into local tool args. Origin draft: [PER-1324](https://linear.app/0ism/issue/PER-1324) — **github_writes=0 until Todo**. Keep #11399 / [PER-1216](https://linear.app/0ism/issue/PER-1216) as the custody leaf. Leak already filed: #10027 (edit diff).

## Related

- [[literature/lit-20260910-trustworthy-secret-brokers]]
- [[literature/lit-20260910-agent-http-inject-brokers]]
- [[permanent/perm-20260910-build-action-portal-not-password-manager]]
- [[harnesses/omp]]
