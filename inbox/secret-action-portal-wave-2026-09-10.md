---
id: inbox-secret-action-portal-wave-20260910
title: Secret action portal wave (2026-09-10)
type: inbox
status: draft
created: 2026-09-10
updated: 2026-09-10
harnesses: [hermes, omp, o8, grok, codex, claude, pi, fx]
tags: [inbox, secrets, broker]
---

# Secret action portal wave

CoS mint 2026-09-10 from deep-research report. Follow-up research same day: wrap products + Hermes vault kinds + identity vs documents.

Parent: [PER-1321](https://linear.app/0ism/issue/PER-1321)

1. [PER-1322](https://linear.app/0ism/issue/PER-1322) frontier-kb ingest
2. [PER-1323](https://linear.app/0ism/issue/PER-1323) Hermes env-inject — origin posted: [#107698](https://github.com/NousResearch/hermes-agent/issues/107698) docs, [#107700](https://github.com/NousResearch/hermes-agent/issues/107700) handles/wrap, [#107704](https://github.com/NousResearch/hermes-agent/issues/107704) identity kind, [#107705](https://github.com/NousResearch/hermes-agent/issues/107705) documents-not-vault.
3. [PER-1324](https://linear.app/0ism/issue/PER-1324) OMP: obfuscation is not a broker. **Do not post an issue we intend to PR** (CONTRIBUTING: robomp pickup). Discord-first. #11399 stays custody (serialize/deserialize wrap, not Infisical-as-store). Auth-gateway already injects **model** keys (`auth-gateway/server.ts` → `streamSimple`). Restore-in-tool-args is the tool-key hole. Groq map 2026-09-10 confirmed file:symbol. Draft: `inbox/omp-portal-discord-2026-09-10.md`.
4. [PER-1325](https://linear.app/0ism/issue/PER-1325) zer0: BWS + secret-tool stay custody
5. [PER-1326](https://linear.app/0ism/issue/PER-1326) other harnesses (no spray)
6. [PER-1327](https://linear.app/0ism/issue/PER-1327) prototype `agent-portal.sock` — only if wrap+Skyflow cannot hit a destination

New notes: [[literature/lit-20260910-agent-http-inject-brokers]] · [[literature/lit-20260910-pii-tokenization-vaults]] · [[permanent/perm-20260910-hermes-vault-is-login-payment-address]] · [[permanent/perm-20260910-identity-fields-are-not-documents]] · [[permanent/perm-20260910-screenshots-bypass-vault-redaction]]

Raw report: [[inbox/20260910-deep-research-secret-brokers]]
Processed: [[literature/lit-20260910-trustworthy-secret-brokers]]
