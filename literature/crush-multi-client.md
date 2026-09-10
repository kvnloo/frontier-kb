---
id: lit-20260910-crush-multi-client
title: Crush serve: multi-client shared workspace presence
type: literature
status: draft
created: 2026-09-10
updated: 2026-09-10
sources:
  - https://github.com/charmbracelet/crush
  - https://github.com/kunchenguid/firstmate
harnesses: [crush, firstmate, omp]
domains: []
confidence: medium
tags: [literature, crush, multi-client, shared-workspace]
---
# Crush serve: multi-client shared workspace presence

## Claim (one sentence)
Multi-client shared workspace presence is the missing parity target: Crush serve exposes a multi-client shared workspace, and firstmate's visible crew architecture is the strongest concrete realization of it.

## Evidence
- Crush README: "Session-Based: maintain multiple work sessions and contexts per project"; its serve surface enables shared workspace presence across clients.
- Firstmate README: every crewmate works in its own tmux window, Herdr tab, or zellij tab — a visible crew reconciled by the first mate.
- omp's subagents run in isolated worktrees but lack a shared multi-client workspace surface.

## Fact vs interpretation
- Fact: crush and firstmate both advertise multi-session / multi-client / multi-worktree presence.
- Interpretation: shared workspace presence across clients is the next parity target for omp (inbox item 4: "Multi-client shared workspace presence (Crush serve)").

## Links
- https://github.com/charmbracelet/crush
- https://github.com/kunchenguid/firstmate
