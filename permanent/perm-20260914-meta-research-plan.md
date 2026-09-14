---
id: perm-20260914-meta-research-plan
title: "Meta research plan: sweeping every source for Harness Evolver SOTA"
type: permanent
status: draft
created: 2026-09-14
updated: 2026-09-14
harnesses: [omp, hermes, codex, claude, cursor, opencode]
domains: [ai-ml, frameworks]
confidence: medium
tags: [permanent, meta-research, research-plan, evolver, rsi, methodology]
---

# Meta research plan: sweeping every source for Harness Evolver SOTA

## Mission

One repeatable operation that answers, from **every source class**, the same question: *what is the newest evidence about self-improving agent scaffolds, and what does it imply for the [[permanent/perm-20260914-harness-evolver|Harness Evolver]] architecture?* The sweep feeds [[notes/harness-evolver-hermes-plan]] (Hermes instantiation) with concrete mechanisms, not vibes.

## Source classes

### 1. arXiv (cs.AI / cs.CL / cs.LG / cs.SE)
- **Method:** `GET https://export.arxiv.org/api/query?search_query=all:<terms>&sortBy=submittedDate&sortOrder=descending` (no auth; 3s politeness delay between calls).
- **Query terms:** `"self-improving agent"`, `"self-evolving agent"`, `"recursive self-improvement" agent`, `"agent scaffold evolution"`, `"harness" "self-improvement" LLM`.
- **Cadence:** one-shot deep sweep per plan iteration + weekly recurring watch on new submissions.
- **Cost:** $0. **Failure mode observed 2026-09-14:** 429/timeout from shared egress IP — mitigate with single consolidated query + longer backoff; see §First sweep.
- **Stub:** `python scripts/sweep_arxiv.py --since 2026-01-01` (to be added under `frontier-kb/scripts/`).

### 2. Semantic Scholar API (fallback for papers)
- **Method:** `GET https://api.semanticscholar.org/graph/v1/paper/search?query=<q>&fields=title,abstract,url,year,authors,citationCount,externalIds&sort=publicationDate:desc` (anonymous = low quota; API key optional via `S2_API_KEY`).
- **Cadence:** one-shot when arXiv is throttled.
- **Cost:** $0. **Failure mode observed 2026-09-14:** 429 anonymous — shared IP throttled; needs key for recurring use.

### 3. Papers-with-Code trending
- **Method:** browse + scrape `https://paperswithcode.com/` trending / agent task leaderboards (no stable public API; use `browser.search` targeted queries).
- **Query terms:** "LLM agents", "self-improvement", SOTA tables on SWE-bench / tau-bench / Terminal-Bench.
- **Cadence:** monthly (leaderboards move slowly).

### 4. GitHub trending + search API (new harness/evolver repos)
- **Method:** `GET https://api.github.com/search/repositories?q=<q>+in:name,description,readme&sort=updated&order=desc&per_page=15` (unauthenticated = 10 req/min; fine).
- **Query terms:** `self-improving agent harness`, `agent scaffold evolution`, `self-evolving LLM agent`, `recursive self-improvement agent`.
- **Cadence:** weekly recurring (new repos ship fast).
- **Cost:** $0.

### 5. X/Twitter researcher posts
- **Method:** no direct X API; use `browser.search` with `site:x.com` queries + social.search (Instagram/Threads/Facebook) for researcher threads that cross-post.
- **Query terms:** "self-improving agents", "harness evolution", "RLM", "continual harness".
- **Cadence:** per-sweep (X indexing lags).
- **Cost:** $0. Coverage is best-effort — treat as a supplement, never the primary.

### 6. Hacker News API (Algolia)
- **Method:** `GET https://hn.algolia.com/api/v1/search?query=<q>&tags=story&hitsPerPage=12` (no auth).
- **Query terms:** `self-improving agent`, `agent scaffold evolution`, `recursive self-improvement`, `evolving prompts`.
- **Cadence:** weekly recurring. High signal-to-noise for launches (Prime Agent, HyperAgents, Meta-Agent all surfaced here).
- **Cost:** $0.

### 7. Frontier-lab engineering blogs
- **Method:** `browser.search` + direct fetch: Anthropic (`anthropic.com/research`, `/institute`), OpenAI engineering, DeepMind blog, Nous Research blog, PrimeIntellect blog, Sakana AI, Weco.
- **Cadence:** per-sweep + watch via RSS/manual check.
- **Cost:** $0.

### 8. Newsletters (Import AI, The Batch, TLDR AI)
- **Method:** `browser.search` for newsletter archives on target terms; subscribe-free web archives.
- **Cadence:** per-sweep.

### 9. Reddit (r/MachineLearning, r/LocalLLaMA)
- **Method:** `browser.search` `site:reddit.com` on target terms; subreddit search pages fetched directly.
- **Cadence:** per-sweep. Good for failure reports and replication attempts.

### 10. YouTube talks
- **Method:** `browser.search` for conference talks / course playlists (e.g. Stanford CS329A "Self-Improving AI Agents" 2026-08).
- **Cadence:** per-sweep; transcribe only talks that make a concrete architectural claim.

### 11. Conference proceedings (ICLR / ICML / NeurIPS)
- **Method:** `browser.search` + openreview.net search API (`https://api.openreview.net/notes/search`) for agent self-improvement papers.
- **Cadence:** per-conference cycle + per-sweep for 2026 proceedings.

### 12. Our own 8-free-model swarm (already running)
- **Method:** `~/workspace/hermes/research_sota_free.py` — 8 parallel free-model research prompts through the OpenRouter proxy; outputs in `~/workspace/hermes/research_sota_free_results/<model>.md`.
- **Angles:** scaffold-evolution SOTA, credit assignment stats, tool-shape evolution, memory consolidation, harness adapter design, self-play/adversarial, $/credited-improvement metrics, safety/rollback gates.
- **Cadence:** per plan iteration. **Cost:** $0.

### 13. frontier-kb literature re-mining
- **Method:** grep + read `literature/` and `permanent/` for evolver-adjacent notes (GSME, Evo-Bench, DGM, GEPA, Voyager) before declaring anything "new".
- **Cadence:** every sweep (cheap, prevents rediscovery).

### 14. hermes-maintainer contention data
- **Method:** `~/workspace/hermes-maintainer/` contention scans + PR-issue links — what rival builders are actually shipping to `NousResearch/hermes-agent` (fixes land within minutes; the watch sees them first).
- **Cadence:** continuous (15m watch already runs).

## Output schema (every finding)

```yaml
finding: <one-line mechanism or result>
architectural_implication: <what changes in the evolver plan — concrete>
confidence: high | medium | low
source_url: <primary URL>
novelty: new | confirms | contradicts   # vs perm-20260914-harness-evolver
```

## Dedup rule

Key findings on normalized `(mechanism, source_domain)`. arXiv paper == HN thread about it == blog post about it → one finding, three URLs. GitHub repos dedup by `owner/name`. The swarm's 8 model outputs dedup against each other AND against the API sweep before touching the KB.

## Refresh / kill criteria

- **Sweep "done enough":** all $0 API sources queried, GitHub+HN results triaged, swarm outputs synthesized, ≥3 independent source classes agree on any claim promoted to `confidence: high`.
- **Plan refresh cadence:** re-sweep when any of (a) a new harness-evolver launch (GitHub/HN), (b) quarterly sealed-battery rotation, (c) a phase kill criterion fires.
- **Stop signal:** two consecutive sweeps with zero `novelty: new` findings at `confidence >= medium` → drop to quarterly cadence.

## Repeatable operation checklist

1. [ ] Run `scripts/sweep_arxiv.py`, `scripts/sweep_github.py`, `scripts/sweep_hn.py` (single-query, polite delays)
2. [ ] Run the 8-free-model swarm (`~/workspace/hermes/research_sota_free.py`)
3. [ ] Fetch top-5 hits per source (blog posts, repo READMEs, paper abstracts)
4. [ ] Re-mine frontier-kb `literature/` + `permanent/` for prior art
5. [ ] Fill one output-schema record per finding; dedup
6. [ ] Write findings into this note's "Sweep results" log below; promote `high`-confidence ones into `perm-20260914-harness-evolver` / `notes/harness-evolver-hermes-plan`
7. [ ] `python scripts/validate-schema.py`, commit, push

## First sweep results (2026-09-14)

arXiv: **failed** (429 + timeouts, shared egress IP). Semantic Scholar: **failed** (429 anonymous). GitHub + HN: **succeeded** (98 records). Three highest-signal findings below; all `novelty: new` vs the plan except where noted.

### Finding 1 — PrimeIntellect "Prime Agent": production self-improving harness (HIGH)
- **What:** Launched Aug 2026, 20.7k stars. Two abstractions: **RLM** (context as a variable; subagent delegation as function calls inside a persistent IPython REPL — the model writes "language model programs as actions over its own context") and **Continual Harness**, formalized as **H = (ρ, G, K, M)** — prompts, sub-agents, skills, memory — each exposing the same CRUD surface the agent itself can call mid-trajectory. `/refine` pipeline: reads the agent's own trajectory, applies the *smallest relevant CRUD edit*; **each refinement records its trigger and the outcome it produced** (evidence-backed, not arbitrary); plan/apply split (background planning, fast atomic apply at turn boundary); the **base system prompt is immutable**; rollback by refinement ID.
- **Architectural implication:** The plan's 5-slot adapter gets its evolvable surface formalized as CRUD over (ρ, G, K, M) — adopt this formalism verbatim. Borrow the plan/apply split for `rollout.py` (propose in background, atomic apply) and make every champion in `champions.py` store (trigger, outcome, rollback-id) the way `/refine` does. Their "immutable base prompt" is our "forbidden surface" idea, independently validated in production.
- **Confidence:** high. **Source:** https://www.primeintellect.ai/blog/prime-agent (HN: 254 pts)

### Finding 2 — canvas-org "Meta-Agent": two-loop continual harness optimization with measured gains (HIGH)
- **What:** Research prototype (Essam Sleiman, Canvas). **Fast loop:** run harness → experience store (task traces + outcomes) → diagnose → hypothesis → candidate harnesses → validate → select; keeps **wins AND failures** so the next proposer sees what already failed. **Slow loop (experimental):** a second agent periodically reviews proposer traces and updates the **versioned proposer instructions** — the loop improves the optimizer itself. Frozen Claude Haiku 4.5 agent: **66.7% → 86.7% on tau-bench v3 airline** (judge-guided, best at epoch 5). Harness interface boundary: *"the benchmark adapter owns task selection, labels, and scoring; the harness owns the decision procedure"* — this is our 5-slot adapter's boundary, stated cleanly. Limitations they admit: transfer unmeasured, skill evolution can learn brittle heuristics, **cost should be reported alongside performance**.
- **Architectural implication:** Add the slow loop as an explicit Phase-2b: version the proposer instructions (`proposer_instructions/` in their layout) and measure whether proposers improve across benchmarks — Meta-Agent's stated open question is our transfer experiment. Adopt their per-candidate evidence layout (`harness.py`, `proposal_notes.json`, `scores.json`, per-task traces) as the `experience/` dir format. Their "report cost alongside performance" becomes a hard rule in our metrics: every credited patch ships with $/Δ.
- **Confidence:** high. **Source:** https://github.com/canvas-org/meta-agent (HN: 234 pts via HyperAgents thread context; repo README)

### Finding 3 — AxisMeru "pravrudhi": independent implementation of nearly our exact architecture (HIGH)
- **What:** Apache-2.0 RSI engine: run "a budgeted night" over your own model and harness. **Harness track = fixed model, mutable scaffold** (our Phase 2, already built). Sealed pools are **kernel-owned**; a **noise-floor study is required before any night** (our Phase 0 calibration, mandatory). The evaluator kernel (`pravrudhi_kernel/`) **has no model client and no network access; it is the only writer of evidence** — the trust boundary enforced by *dependency direction*, not declaration. Candidates disposed of by **sequential test**; hash-chained ledger with `replay --verify`; human inbox sign-off (`pravrudhi inbox` → accept/reject); export with provenance. Even the external-proof tier enters the ledger by hash only.
- **Architectural implication:** Strengthen the plan's safety boundary: the credit gate/evaluator must be a separate package the evolver **cannot import** (dependency direction), not merely a "declared forbidden" surface. Make the noise-floor study a hard prerequisite (gate the first night on it). Adopt sequential testing for candidate disposal and the hash-chained ledger for champion provenance. Pravrudhi is the closest thing to a reference implementation — study its `paper/` dir before writing `evolver/gates.py`.
- **Confidence:** high. **Source:** https://github.com/AxisMeru/pravrudhi

### Supporting signals (medium)
- **Anthropic, "When AI builds itself" (2026-06-04, HN 534 pts / 704 comments):** 8× code/engineer/day since 2024; >80% of merged code Claude-authored; automated Claude reviewer would have caught ~1/3 of past incident bugs — lab-grade evidence that automated review gates work. Their framing ("closing the loop"; the remaining gap is *judgement in choosing goals*) is why the **human merge gate stays** in our plan. https://www.anthropic.com/institute/recursive-self-improvement
- **Warp builds self-improving agents on Claude (2026-08-29):** production deployment of self-improving agents on a closed harness — the "wrapper-layer only" variant from our plan's closed-harness section, confirmed shippable. https://claude.com/blog/how-warp-builds-self-improving-agents-on-claude
- **Sakana AI RSI Lab (2026-06-05):** dedicated lab; watch for publications. https://sakana.ai/rsi-lab/
- **Weco AIDE² "First Evidence of Recursive Self-Improvement" (2026-07-15):** claimed RSI evidence on coding — read before Phase 0. https://www.weco.ai/blog/first-evidence-of-recursive-self-improvement
- **Meta^N: Recursive Self-Improvement Through Emergent Depth (arXiv 2608.24735, 2026-09-13):** 1-day-old; fetch when arXiv egress recovers.
- **Technology Review (2026-09-13):** "AI recursive self-improvement might not come so quickly after all" — the counter-case; read before committing Phase 2 budget. https://www.technologyreview.com/2026/08/18/1142188/ai-recursive-self-improvement/

### Source failures logged
- arXiv API: 429/timeout (shared IP). Retry with single consolidated query + 60s backoff, or from host 0.
- Semantic Scholar: 429 anonymous. Needs `S2_API_KEY` for recurring use.

## Related
- [[permanent/perm-20260914-harness-evolver]] — the generalized loop this plan feeds
- [[notes/harness-evolver-hermes-plan]] — the Hermes instantiation
- [[literature/lit-20260910-gsme-self-evolving-harness]]
- [[literature/lit-20260910-evo-bench-harness-evolution]]
