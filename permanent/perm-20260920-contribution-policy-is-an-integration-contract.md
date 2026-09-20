---
id: perm-20260920-contribution-policy-is-an-integration-contract
title: "Contribution policy is an integration contract"
type: permanent
status: active
created: 2026-09-20
updated: 2026-09-20
harnesses: [fx, pi, nano-rlm, prime-agent, opencode, goose]
domains: [software-engineering, ai-ml]
confidence: high
tags: [permanent, oss, governance, contribution]
---

# Contribution policy is an integration contract

## Idea (atomic)

An automated OSS contributor is not compatible with a repository merely because it can produce a correct patch. It is compatible only when it also satisfies the maintainer's intake, scope, evidence, validation, and communication contract.

Pi requires explicit maintainer approval before PR submission. Goose gates implementation on issue state. Prime Agent starts public contributions in Discussions and restricts code PRs to invited/vouched contributors. OpenCode requires an issue and design review for product features. fx expects focused local evidence followed by an early draft PR. nano-rlm encodes branch, test, and draft-PR behavior directly in AGENTS.md.

These are not superficial etiquette differences. They determine which actions are valid in the contribution state machine.

## Why it matters for our harnesses

`verified-oss-loop` should represent contribution policy as machine-readable preconditions before any upstream write. Candidate generation can be broad; mutation authority must remain repo-specific.

A useful candidate record should therefore include at least:

- upstream repository and policy evidence
- allowed next action: research, issue, discussion, draft PR, invited PR, or no code contribution
- required maintainer state or approval
- required local checks / CI evidence
- communication constraints such as brevity, AI disclosure, or issue templates

This makes policy violations fail closed before GitHub mutation, the same way a runtime capability check should fail before executing an unsupported tool.

## Related

- [[inbox/oss-harness-contribution-policy-radar-20260920]]
- [[harnesses/fx]]
- [[harnesses/pi]]
- [[harnesses/nano-rlm]]
