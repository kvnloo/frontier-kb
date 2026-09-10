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

The report's acceptance test is differential: two same-shape canaries, record **everything** the agent VM can observe, classifier cannot tell which secret was used beyond authorized output \(O\). Grep-for-plaintext is not that test.

At-rest encryption of `auth_credentials` (OMP #11399) is custody. Necessary. Not the portal.

## Why it matters for our harnesses

OMP leapfrog vs Hermes is not "better redaction." It is refusing agent-owned browser sessions and secret-return RPCs. Origin draft: [PER-1324](https://linear.app/0ism/issue/PER-1324). Keep #11399 / [PER-1216](https://linear.app/0ism/issue/PER-1216) as the custody leaf.

## Related

- [[literature/lit-20260910-trustworthy-secret-brokers]]
- [[permanent/perm-20260910-build-action-portal-not-password-manager]]
- [[harnesses/omp]]
