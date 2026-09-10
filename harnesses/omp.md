---
id: harness-omp
title: omp
type: harness
status: active
created: 2026-09-09
updated: 2026-09-10
urls: ["https://github.com/can1357/oh-my-pi", "https://github.com/can1357/oh-my-pi/issues/11399"]
capabilities: ["secret-obfuscation-placeholders"]
gaps_vs_peers: ["obfuscation-not-noninterference", "plaintext-auth-credentials"]
omp_actionable: true
confidence: high
tags: [harness]
---

# omp

Oh My Pi. Secret handling today is provider-visible obfuscation plus plaintext `auth_credentials` in agent.db.

## Secrets (accepted vs SOTA)

Accepted: replace secret values with `$$HASH$$` before the model sees them; restore in tool arguments. Optional at-rest wrap is origin #11399 (open). Agent still owns tools, CDP/Playwright, and restored plaintext at execution.

SOTA gap: obfuscation is a prompt filter. Differential noninterference (canary \(s_0\) vs \(s_1\)) is the test. Action portal, not a better redactor.

[[permanent/perm-20260910-obfuscation-is-not-noninterference]] · Linear [PER-1324](https://linear.app/0ism/issue/PER-1324)

## Snapshot

Coding agent with typed task fan-out, MCP, browser/computer tools.

## Strengths

Obfuscation exists and is tested. #11399 is the right custody leaf.

## Gaps (leapfrog targets)

No secret-return primitive. Broker-owned browser. Destination-bound inject. Do not expand #11399 into the portal.

## Sources

- https://github.com/can1357/oh-my-pi/issues/11399
- [[literature/lit-20260910-trustworthy-secret-brokers]]
