---
id: inbox-omp-portal-ethos-20260910
title: OMP portal path (Discord-first, do not robomp-bait)
type: inbox
status: draft
created: 2026-09-10
updated: 2026-09-10
harnesses: [omp]
tags: [inbox, omp, secrets]
---

# OMP portal path

PER-1324 github_writes=0 until Todo. CONTRIBUTING (oh-my-pi):

- Major architecture: **Discord before implementation**. A GitHub issue is not a substitute.
- **Do not open an issue for work you are about to submit** — robomp treats actionable issues as work to pick up.
- PRs need one human sentence + live verification. bun check is not enough.

## Existing origin (ours)

- #11399 at-rest `auth_credentials` — **custody**. robomp already confirmed the code cites. Do not expand.
- #10027 placeholder restored into edit diff + JSONL — **leak**. Keep as the leak leaf.
- #10828 PAW PII plugin — NER, not brokerage.

## Hermes analog already posted

#107698 docs, #107700 handles/wrap, #107704 identity kind, #107705 documents-not-vault.

## Recommended OMP move (do not post until Discord + PER-1324 Todo)

1. Discord: restore-in-tool-args is Hermes `--apply` for **tool** keys. Provider keys already inject at auth-gateway. Wrap Infisical/HASP as sibling for GitHub/AWS. Do not vendor. Do not new vault. Do not expand #11399.
2. Smallest PR if we implement ourselves: **docs wrap recipe** in `docs/secrets.md` + do not restore tool-facing names (or fix #10027 so diffs stay placeholders). No issue if we are about to PR that.
3. Problem-only issue (only if we will NOT implement): "obfuscation is not a broker" as a tracking note — high robomp-bait risk. Prefer Discord.

Draft Discord (not posted):

> `secrets.enabled` hides env/`secrets.yml` values from the provider, then `deobfuscateToolArguments` puts them back before tools run (`packages/coding-agent/src/secrets/message-transform.ts`). That's a prompt filter: system prompt and tool schemas are not walked; local tools see plaintext. #11399 is at-rest wrap of `auth_credentials.data` (`serializeCredential`) — keep it, do not turn it into Infisical-as-store (OAuth rows mutate). Provider keys already inject at `auth-gateway/server.ts` (`streamSimple`); clients never see the access token. The remaining hole is tool-facing GitHub/AWS keys. Document Infisical Agent Proxy / HASP as a process wrap around omp for those, and stop teaching restore-as-success. #10027 is the edit-diff leak of the restored value. Not proposing Skyflow/SSN in core. Not competing with #11399.
