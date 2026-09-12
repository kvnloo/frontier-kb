---
id: inbox-cursor-aodl-papers-20260911
title: "AODL-adjacent papers (58 arXiv ids, Jina-read primaries)"
type: inbox
status: draft
created: 2026-09-11
updated: 2026-09-11
node: cursor
harnesses: [cursor, hermes, omp, grok, codex, claude]
domains: [frameworks, mathematics, cs, information-theory]
tags: [inbox, aodl, literature, arxiv]
---

# Primaries that share AODL's structure under other names

## Context

Pulled abstracts for 58 arXiv ids from DuckDuckGo hits; Jina-read the ones that actually change the language (not enterprise surveys).

Highest leverage (fact vs interpretation in the AODL capture):

| arXiv | Claim (one sentence) | AODL object |
|---|---|---|
| [2604.11767](https://arxiv.org/abs/2604.11767) | $\lambda_A$: typed agent calculus; 94.1% of 835 GitHub configs structurally incomplete; five frameworks embed as fragments | intra-node semantics; bounded `fix_n` |
| [2605.03143](https://arxiv.org/abs/2605.03143) | Pact: choreography + choices/utilities/nature $\mapsto$ a game (why an agent follows a protocol) | `message` + auction $\Pi_t$ |
| [2603.06007](https://arxiv.org/abs/2603.06007) | MASFactory: NL $\to$ editable graph spec $\to$ executable; control/message/state flows | intent vs plan; data vs control |
| [2602.16873](https://arxiv.org/abs/2602.16873) | AdaptOrch: after model-quality convergence, topology dominates model choice | search over $\Pi_t$ |
| [2602.07072](https://arxiv.org/abs/2602.07072) | AgentSpawn: runtime spawn + memory slice + coherence | bounded graph mutation |
| [2605.01879](https://arxiv.org/abs/2605.01879) | Sheaf-theoretic planning: local histories glue; obstruction $\mapsto$ abduction | three objects as sheaves |
| [2510.18893](https://arxiv.org/abs/2510.18893) | CodeCRDT: observation-driven coordination; character merge $\neq$ semantic merge | `observation` + verifier |
| [2512.24601](https://arxiv.org/abs/2512.24601) | RLM: prompt is an environment object; recursive slices beat dump/compaction | token-slice hypothesis |
| [2608.09096](https://arxiv.org/abs/2608.09096) | Evo-Bench: evolver edits harness $H_t$ under budget; early saturation | architecture search |
| [2606.19812](https://arxiv.org/abs/2606.19812) | HOTL legal: trajectory collapse; calibrated escalation | `humanGate` + evidence |
| [2606.08919](https://arxiv.org/abs/2606.08919) | Oversight inverted-U: more escalation can be less safe | human-attention budget in $\Gamma_t$ |
| [2510.24205](https://arxiv.org/abs/2510.24205) | CoMPSeT: compare MPST dialects; global type $\to$ local projection | optional session-type profile |
| [2606.04990](https://arxiv.org/abs/2606.04990) | Survey: traces $\to$ trust / provenance for LLM agents | event log / PROV |
| [2604.25850](https://arxiv.org/abs/2604.25850) | Agentic harness engineering from observability | compile AODL $\to$ harness, not reverse |
| [2607.08032](https://arxiv.org/abs/2607.08032) | Rate-distortion view of memory compaction | slice vs dump |
| [2511.13646](https://arxiv.org/abs/2511.13646) | Live-SWE-agent: on-the-fly scaffold evolution | $H_t$ mutation at runtime |
| [2511.03690](https://arxiv.org/abs/2511.03690) | OpenHands SDK: composable production agent foundation | compiler profile / adapter |
| [2505.19591](https://arxiv.org/abs/2505.19591) | Evolving orchestration (NeurIPS 2025) | dynamic $\Pi_t$, still needs bounds |

Full id list (newest first) is in the AODL capture. Do not treat [2601.13671](https://arxiv.org/abs/2601.13671) as a formal semantics; it is a survey that correctly splits MCP vs A2A vs control plane.

## Next action

Promote selected rows to `literature/` with `sources:` pointing at arXiv html. Do not mint a second IR.

## Links

- https://github.com/kvnloo/aodl/blob/main/docs/research-craid-20260911.md
- [[permanent/perm-20260817-orchestration-typed-dynamic-graph]]
- [[literature/lit-20260817-hotl-02-spec]]
