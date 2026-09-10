---
id: lit-20260910-sandbox-harness-split
title: Sandbox / harness↔compute split
type: literature
status: draft
created: 2026-09-10
updated: 2026-09-10
sources:
  - https://openai.github.io/openai-agents-python/sandbox/guide/
  - https://github.com/can1357/oh-my-pi
  - https://github.com/NousResearch/hermes-agent
harnesses: [omp, hermes, opencode, claude-code]
domains: []
confidence: medium
tags: [literature, sandbox, compute, harness]
---
# Sandbox / harness↔compute split

## Claim (one sentence)
The sandbox is the compute plane and the harness is the orchestration plane; separating them (OpenAI Agents SDK sandbox guide, omp's persistent Python/Bun worker, Hermes' compute backends) is the clean architecture for future harnesses.

## Evidence
- OpenAI Agents SDK sandbox guide documents sandboxing as a distinct compute layer.
- omp README: "persistent Python and a Bun worker, and either kernel can call back into the agent's own tools — read, search, task — over a loopback bridge."
- Hermes README: "Seven terminal backends — local, Docker, SSH, Singularity, Modal, Daytona, and Vercel Sandbox" with serverless persistence.
- Claude Computer Use tool similarly separates desktop automation from the agent model.

## Fact vs interpretation
- Fact: all four products separate agent logic from compute/sandbox.
- Interpretation: the harness↔compute split is the durable pattern; harnesses should expose sandbox manifests and treat compute as a pluggable plane.

## Links
- https://openai.github.io/openai-agents-python/sandbox/guide/
- https://github.com/can1357/oh-my-pi
- https://github.com/NousResearch/hermes-agent
