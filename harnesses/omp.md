---
id: harness-omp
title: OMP (oh-my-pi)
type: harness
status: active
created: 2026-09-09
updated: 2026-09-11
urls:
  - https://github.com/can1357/oh-my-pi
  - https://omp.sh/
  - https://github.com/can1357/oh-my-pi/issues/11399
  - https://github.com/can1357/oh-my-pi/issues/10027
  - https://github.com/can1357/oh-my-pi/issues/10828
  - https://github.com/NVlabs/SoL-Pi
capabilities:
  - secret-obfuscation-placeholders
  - auth-broker-gateway
  - auth-gateway-provider-inject
  - Subagents, LSP, DAP, plan mode, hindsight memory, hashline edits, stream rules
  - Multi-model (60+ providers), Rust core, persistent Python/Bun worker
  - First-class task fan-out into isolated worktrees, reviewer model
  - Native terminal TUI with MCP/http/stdio/sse extensibility
  - Legacy Pi extension load (pi.extensions + earendil-works shim)
gaps_vs_peers:
  - obfuscation-not-noninterference
  - plaintext-auth-credentials
  - restore-in-tool-args
  - system-schema-unwalked
  - No built-in agent crew orchestration (firstmate/crush cover this)
  - No cross-platform messaging gateway (hermes covers Telegram/Discord)
  - Lacks secondmate persistent multi-client workspace (crush serve does multi-client)
  - SoL-Pi Online Context Compact likely no-ops (no agent_settled)
  - Stock SoL-Pi factory fails without findCutPoint (OMP 18.1.17 shim)
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

## SoL-Pi (NVIDIA efficiency extension)

Do **not** merge SoL-Pi into omp core (`github_writes=0` on `can1357/oh-my-pi`). Load it as a plugin:

```bash
omp install github:NVlabs/SoL-Pi
# or: omp plugin link /path/to/SoL-Pi
# live smoke used: omp plugin install /path/to/SoL-Pi
```

`pi.extensions` + `@earendil-works/*` rewrite (`legacy-pi-coding-agent-shim`, #7094 edit/write factories) is the path. Live smoke (2026-09-11): `omp plugin install` listed `sol-pi` v0.1.0; `omp plugin doctor` reports the package ok. The stock `src/sol-pi/index.ts` entry still statically imports OCC/`findCutPoint`; OMP 18.1.17's shim does not export that symbol, so the default factory fails even when `onlineContextCompact` is false. Phase 0 is a thin wrapper that imports only Action Fusion + ObservationPack.

Conservative config (no extra model, no abort/continue):

```json
{
  "version": 1,
  "actionFusion": true,
  "observationPack": true,
  "evidencePreservingReducer": false,
  "onlineContextCompact": false
}
```

Write it to `.omp/sol-pi.json` or `~/.omp/agent/sol-pi.json` (`CONFIG_DIR_NAME` is `.omp`). Action Fusion wraps OMP's `edit`/`write` (hashline preserved if those factories are the real tools). ObservationPack needs the `context` event — OMP has it. EPR is the same secret/log-exfil caution as Pi. OCC: OMP has `compact()` / `session_before_tree` / `session_stop` but **not** `agent_settled`; NVIDIA says OCC then starts no boundary compaction. Adapter later; Discord-first if core events are required.

[[literature/lit-20260911-sol-pi-harness-efficiency]] · [[permanent/perm-20260911-omp-can-load-sol-pi-via-legacy-shim]]

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
