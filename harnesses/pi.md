---
id: harness-pi
title: pi
type: harness
status: active
created: 2026-09-09
updated: 2026-09-20
urls:
  - https://github.com/earendil-works/pi
  - https://pi.dev/
  - https://github.com/NVlabs/SoL-Pi
  - https://nvlabs.github.io/SoL-Pi/
capabilities:
  - Minimal tool loop (read/write/edit/bash)
  - Public ExtensionAPI + pi install git:/npm:
  - RPC + session tree + native compaction
  - SoL-Pi opt-in efficiency extension
gaps_vs_peers:
  - No LSP/DAP in core (OMP comparison)
  - No messaging gateway in core (Hermes comparison)
omp_actionable: true
confidence: high
tags: [harness, pi, extensions, sol-pi]
---

# pi

Mario Zechner / Earendil `pi` (`@earendil-works/pi-coding-agent`) is intentionally a minimal coding-agent substrate with a strong extension boundary.

## Snapshot

The architectural rule is more important than the feature inventory: if behavior does not belong in core, it should be an extension. Even new extension hooks are expected to justify their interaction cost.

The repo includes the coding-agent package plus lower-level agent/AI/TUI packages. Public extension events make it a useful substrate for experiments such as SoL-Pi without requiring those mechanisms to be patched permanently into core.

## Extension boundary

Pi is a strong control case for our own harness work because it forces a recurring question: “does this capability require core support, or can the stable extension surface express it?”

That question should be asked before borrowing any Pi idea into OMP/Hermes and before proposing upstream changes to Pi itself.

## Contribution contract

Pi has an unusually explicit social gate:

- New-contributor issues and PRs are auto-closed by default and reviewed later by maintainers.
- A maintainer can grant issue participation with `lgtmi`; only `lgtm` grants the right to submit PRs.
- Do not open a PR before receiving `lgtm`.
- Issues should be short, concrete, in the contributor's own voice, and explain why the problem matters.
- Large-volume automated issue submission can lead to blocking.
- Before an approved PR: `npm run check` and `./test.sh` must pass.
- Contributors do not edit `CHANGELOG.md`; maintainers own changelog entries.

The development rules add important repository-safety constraints: read files fully before broad edits, do not use destructive git operations, do not guess dependency APIs, test modified test files directly, and preserve concurrent work by staging only files changed in the current session.

## Maintainer signals

Recent merged changes are concrete and bounded: stale asynchronous image conversion, skill autocomplete ranking, CJK punctuation in file autocomplete, copy behavior, shell duration formatting, event unsubscription, and eval transcript validation.

The common shape is not “add a new subsystem.” It is “demonstrate one broken or missing contract, identify its narrow owner, and validate the repair.”

## Cross-harness lens

Pi gives us a test for architectural restraint. When another harness adds a built-in subsystem, compare whether Pi can express the same outcome as an extension.

This is especially useful for:

- context reduction / compaction
- model/provider behavior
- session lifecycle hooks
- tool-result transforms
- efficiency mechanisms such as SoL-Pi
- observability hooks

The absence of a feature in Pi should not automatically be treated as a gap. It may be an intentional refusal to move extension behavior into core.

## Contribution strategy

For Pi, the next useful action is not to open many issues. Select one reproducible problem with clear user impact, trace whether it belongs in core or an extension, write a one-screen issue in our own voice, and explicitly offer to implement it. Implementation begins only after upstream `lgtm`.

## Sources

- https://github.com/earendil-works/pi
- https://github.com/earendil-works/pi/blob/main/CONTRIBUTING.md
- https://github.com/earendil-works/pi/blob/main/AGENTS.md
- https://pi.dev/
- [[literature/lit-20260911-sol-pi-harness-efficiency]]
- [[permanent/perm-20260911-sol-pi-is-pi-public-extension-not-core-patch]]
- [[harnesses/omp]]
- [[inbox/oss-harness-contribution-policy-radar-20260920]]
