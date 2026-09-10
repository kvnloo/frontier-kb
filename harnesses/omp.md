---
id: harness-omp
title: OMP (oh-my-pi)
type: harness
status: active
created: 2026-09-09
updated: 2026-09-10
urls:
  - https://github.com/can1357/oh-my-pi
  - https://omp.sh/
  - https://github.com/can1357/oh-my-pi/issues/11399
  - https://github.com/can1357/oh-my-pi/issues/10027
  - https://github.com/can1357/oh-my-pi/issues/10828
capabilities:
  - secret-obfuscation-placeholders
  - auth-broker-gateway
  - auth-gateway-provider-inject
  - Subagents, LSP, DAP, plan mode, hindsight memory, hashline edits, stream rules
  - Multi-model (60+ providers), Rust core, persistent Python/Bun worker
  - First-class task fan-out into isolated worktrees, reviewer model
  - Native terminal TUI with MCP/http/stdio/sse extensibility
gaps_vs_peers:
  - obfuscation-not-noninterference
  - plaintext-auth-credentials
  - restore-in-tool-args
  - system-schema-unwalked
  - No built-in agent crew orchestration (firstmate/crush cover this)
  - No cross-platform messaging gateway (hermes covers Telegram/Discord)
  - Lacks secondmate persistent multi-client workspace (crush serve does multi-client)
omp_actionable: true
confidence: high
tags: [harness]
---
# OMP

Snapshot: Most capable agent surface shipped; fork of Pi. ~80k Rust core lines.
Strengths: LSP/DAP wired in; real debugger; time-traveling stream rules; subagent fan-out.
Gaps: No persistent multi-agent crew management; no messaging gateway (hermes does this); multi-client workspace is missing vs crush serve.
Sources: https://github.com/can1357/oh-my-pi, https://omp.sh/

Oh My Pi. Three secret paths, not one pile: prompt obfuscation, sqlite provider credentials, auth-gateway inject.

## Secrets (accepted vs SOTA)

**Prompt filter** (`docs/secrets.md`, off by default): `secrets/index.ts:buildSecretObfuscator` collects env names matching KEY|SECRET|TOKEN|… (≥8 chars), `~/.omp/agent/secrets.yml` + `<cwd>/.omp/secrets.yml`, then builtin `SENSITIVE_TOKEN_RE`. `message-transform.ts:obfuscateProviderContext` rewrites conversation messages only. **System prompt and tool schemas are unwalked.** Images skipped. Restore is `deobfuscateToolArguments` — JSON-walk of model-authored tool args only (`sdk.ts:transformToolCallArguments`, `agent-session.ts` toolCall). `deobfuscateSessionContext` restores assistant/branch/compaction only; user/tool-result stay literal. Local tools see plaintext args. Leak if a secret lives in system/tools schema.

**Provider custody:** `sqlite-credential-store.ts:serializeCredential` / `deserializeCredential` write `api_key`/`oauth` as JSON into `auth_credentials.data`. File mode 0600, no decrypt. `AuthCredentialStore` is already pluggable (`auth-storage.ts`): `SqliteAuthCredentialStore` vs `RemoteAuthCredentialStore` (refresh → `REMOTE_REFRESH_SENTINEL`; mutations throw).

**HTTP inject already in tree for model keys:** `auth-gateway/server.ts` foreign-wire → `streamSimple` credential inject. Clients never see the access token. The only AES-GCM artifact is `auth-broker-snapshot.enc`. Tokens-off-laptop = broker + gateway. Infisical wrap does **not** replace that.

Custody leaf (ours, open): [#11399](https://github.com/can1357/oh-my-pi/issues/11399) — optional at-rest wrap of the sqlite `data` blob via serialize/deserialize + wrap-key. Keep CAS/leases/ranking in SQLite. Do **not** expand it into Infisical-as-`AuthCredentialStore` (OAuth rows mutate ~60s with lease fencing; vault APIs are static). Leak: [#10027](https://github.com/can1357/oh-my-pi/issues/10027). PII NER: [#10828](https://github.com/can1357/oh-my-pi/issues/10828).

**Compose, not vendor:** Infisical/HASP sit as a sibling process wrap for **tool-facing** GitHub/AWS keys (the restore hole), or as extra inject at `AuthGatewayBootOptions.storage` + `streamSimple`. Static keys already via `auth.broker.token` / config `!command` / env.

**Ethos (CONTRIBUTING):** do **not** open an issue for work you are about to PR — robomp will pick it up. Major architecture: Discord first. Every PR needs one human sentence + live verification.

[[permanent/perm-20260910-obfuscation-is-not-noninterference]] · Linear [PER-1324](https://linear.app/0ism/issue/PER-1324) (github_writes=0 until Todo)

## Snapshot

Typed task fan-out, MCP, browser/computer tools. robomp auto-implements actionable issues.

## Strengths

Obfuscation exists and is tested. Auth-gateway already injects **provider** tokens. #11399 is the right custody leaf.

## Gaps (leapfrog targets)

Restore-in-tool-args is the Hermes `--apply` equivalent for `GITHUB_TOKEN`. Document wrap for tool credentials; stop teaching restore-as-success. No identity/document store — compose Skyflow/Plaid if needed. Discord-first.

## Sources

- https://github.com/can1357/oh-my-pi/blob/main/docs/secrets.md
- [[literature/lit-20260910-trustworthy-secret-brokers]]
- [[literature/lit-20260910-agent-http-inject-brokers]]
- [[permanent/perm-20260910-identity-fields-are-not-documents]]
