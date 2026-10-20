---
id: atlas-agent-os-evidence-map
title: "Agent OS evidence map: what work is moving out of the model?"
type: atlas
status: draft
created: 2026-09-20
updated: 2026-09-20
domains: [cs, frameworks, ai-ml, systems]
tags: [agent-os, context, scheduling, communication, systems, efficiency]
---

# Agent OS evidence map

## The simple question

**What work are we paying the language model to do that a system could do more cheaply, explicitly, or reliably?**

This map tracks papers, repos, protocols, and production systems that move some responsibility out of free-form model inference and into an explicit mechanism.

It is evidence for a working thesis, not proof of one architecture:

> LLMs should spend their expensive computation on semantic work. State, scheduling, memory, permissions, synchronization, resource accounting, and other systems work should move into cheaper mechanisms whenever those mechanisms preserve verified capability.

The broad corpus is a **systematic evidence map**, not one statistical meta-analysis. Results are only pooled when the tasks, baselines, interventions, and outcomes are comparable.

## How to read each row

Each row answers four questions:

1. **What was the model doing?**
2. **What mechanism takes over?**
3. **What evidence says that helped?**
4. **What stops us from overgeneralizing?**

The final column links the source to one or more working hypotheses:

- **H1 Context externalization**: keep persistent information outside active context and load a task working set.
- **H2 Explicit control flow**: once semantic structure is known, deterministic control should replace repeated model bookkeeping where possible.
- **H3 Text is overused as systems state**: text is useful for semantics and people, but not always the best machine representation.
- **H4 Learned policies must earn complexity**: keep a learned controller only when it beats simpler rules or algorithms.
- **H5 Better models increase systems pressure**: longer and more capable agents make state, concurrency, permissions, and resource management more important.

---

# 1. Context and memory

## Working-set management

| Source | Work moved out of the model | Mechanism | Evidence | Important limit | Thesis |
|---|---|---|---|---|---|
| [MemGPT: Towards LLMs as Operating Systems](https://arxiv.org/abs/2310.08560) (2023) | Keeping all useful history resident in one prompt | Virtual context management across memory tiers | Evaluated on long-document analysis and multi-session chat beyond the underlying context window | The model still participates in memory management. This is not evidence that every paging decision should be deterministic | H1 |
| [Recursive Language Models](https://arxiv.org/abs/2512.24601) (2025) | Reading a huge prompt as one always-resident context | Prompt becomes an external environment that the model programmatically examines and recursively queries | Authors report successful handling of inputs up to two orders of magnitude beyond model context and gains over long-context scaffolds on four tasks | Later work questions whether recursion itself is the key mechanism | H1 |
| [The Y-Combinator for LLMs / λ-RLM](https://arxiv.org/abs/2603.20105) (2026) | Model invents its own recursive control program | Preverified typed combinators handle SPLIT / MAP / REDUCE while the model solves bounded leaves | 29/36 wins over standard RLM; up to +21.9 accuracy points and up to 4.1x lower latency in the reported study | Long-context task family only; formal guarantees rely on its runtime assumptions | H1, H2 |
| [SRLM: Self-Reflective Program Search](https://arxiv.org/abs/2603.15653) (2026) | Fixed recursive decomposition strategy | Uncertainty-aware search over context-interaction programs | Authors report up to 22% improvement over RLM under the same time budget and find recursion is not always the main driver | Control remains partly model-mediated; it is a counterexample to treating recursion as the answer | H1, H4 |
| [Effective context engineering for AI agents](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents) (2025) | Blindly growing the transcript | Just-in-time retrieval, compaction, structured notes, focused subagents | Production guidance treats context as finite and recommends the smallest high-signal working set | Practitioner guidance, not a controlled paper with one comparable effect size | H1, H5 |
| [SoL-Pi](https://nvlabs.github.io/SoL-Pi/) (2026) | Replaying large observations and repeatedly rereading long evidence | ObservationPack, Evidence-Preserving Reducer, Online Context Compact | On authors' EdgeBench evaluation, 45-49% fewer tokens than Pi while retaining about 94% of Pi average score | Terminal-Bench 4 solved 15/63 vs 18/63 for Pi and Codex, so efficiency and capability must be tracked together | H1, H4 |

### Existing local notes

- [[literature/context-triad]]
- [[literature/lit-20260911-sol-pi-harness-efficiency]]
- [[literature/lit-20260919-sol-pi-recursive-efficient-improvement]]

**Synthesis:** the strongest shared idea is not "use recursion" or "use summaries." It is simpler: **the whole history should not be the working set.**

---

# 2. Serving and memory systems

## Classical memory management reappears below the agent layer

| Source | Work moved out of the model/system | Mechanism | Evidence | Important limit | Thesis |
|---|---|---|---|---|---|
| [PagedAttention / vLLM](https://arxiv.org/abs/2309.06180) (2023) | Ad hoc allocation of dynamically growing KV caches | OS-inspired paging and flexible KV-cache sharing | Reported 2-4x throughput over FasterTransformer and Orca at similar latency in evaluated serving workloads | This manages inference memory, not agent semantic context. The analogy should not be stretched into identity | H1 |
| [vLLM](https://github.com/vllm-project/vllm) | Each application reinvents high-throughput model serving | Shared serving runtime, batching, KV management, model execution | Widely used implementation of PagedAttention and related serving techniques | Runtime support/capabilities belong to vLLM, not our own model registry | H1, H5 |

**Synthesis:** classical systems abstractions can transfer to LLM computation without requiring the model to reason about the abstraction itself.

---

# 3. Compilation, scheduling, and concurrency

## Once dependencies are known, stop asking the model what is runnable

| Source | Work moved out of the model | Mechanism | Evidence | Important limit | Thesis |
|---|---|---|---|---|---|
| [LLMCompiler](https://proceedings.mlr.press/v235/kim24y.html) (ICML 2024) | Sequential reason-act scheduling for every function call | Planner emits dependencies; task-fetching unit dispatches ready work; executor runs calls in parallel | Up to 3.7x latency speedup, 6.7x cost savings, and about 9% accuracy gain vs ReAct in reported evaluations | Function-calling benchmarks do not establish a universal scheduler for long-horizon coding agents | H2, H5 |
| [AIOS: LLM Agent Operating System](https://openreview.net/forum?id=L4HHkCDz2x) (COLM 2025) | Every agent individually manages LLM calls, context, memory, storage, tools, and access | Kernel centralizes scheduling and resource management; evaluates FIFO and round-robin scheduling | Authors report up to 2.1x faster agent execution; scheduling ablations show large waiting-time differences | This is one concrete kernel design, not evidence that its exact API is the universal Agent OS | H2, H5 |
| [The Agent Operating System: reference architecture](https://arxiv.org/abs/2608.03214) (2026) | One "orchestrator" informally owns intent, policy, scheduling, routing, memory, and audit | Separates Control & Governance from Runtime & Coordination planes | Provides explicit invariants and responsibility boundaries | Reference architecture, not an empirical efficiency result | H2, H5 |
| [Towards an Agent Operating System: Lessons from Classical and Cloud OS](https://arxiv.org/abs/2607.25076) (2026) | Framework-specific abstractions repeatedly rebuilt | Proposes deriving stable agent abstractions from POSIX/Kubernetes-style platform lessons | Argues the field is in a pre-consolidation experimentation phase | Position paper. It motivates standardization but does not establish which abstractions will win | H2, H5 |
| [Agent Operating Systems: integrating agentic control planes with traditional OSs](https://arxiv.org/abs/2606.01508) (2026) | Agent-specific scheduling, state, policy, and audit remain bolted onto applications | Explicit agent control plane integrated with existing OS primitives | Defines schedulers, context/memory management, capabilities, policy, and observability as system responsibilities | Architectural proposal, not a benchmark demonstrating all pieces are necessary | H2, H5 |

### Existing local notes

- [[literature/durable-workflows]]
- [[literature/lit-20260910-agent-kb-concurrency]]

**Synthesis:** **planning and scheduling are different jobs.** The model may decide what work should exist. A queue, dependency counter, or scheduler can often decide what work is runnable.

---

# 4. Communication and representation

## Text is not the only possible machine bus

| Source | Work moved out of the model | Mechanism | Evidence | Important limit | Thesis |
|---|---|---|---|---|---|
| [Model Context Protocol](https://modelcontextprotocol.io/) | Every model/harness learns bespoke tool and resource integration through prompt conventions | Typed protocol for tools, resources, prompts, and extensions | 2026-07-28 spec moves toward a stateless core and formal extensions such as Tasks | Interoperability standard, not evidence of lower reasoning cost by itself | H2, H3 |
| [Agent2Agent Protocol](https://a2a-protocol.org/latest/) | Custom agent-to-agent discovery and task handoff logic | Agent cards, task lifecycle, structured parts/artifacts, protocol bindings | Stable v1.0 released in 2026 for cross-framework interoperability | Standardizes communication, not the internal scheduler or memory model | H2, H3 |
| [Cache-to-Cache: Direct Semantic Communication Between LLMs](https://proceedings.iclr.cc/paper_files/paper/2026/hash/474ada926b331d78f06d95e8913111cc-Abstract-Conference.html) (ICLR 2026) | Source model renders semantics to intermediate text; target model reconstructs them | Learned projection/fusion between KV caches | Reported 3.1-5.4% average gain over text communication and 2.5x average latency speedup; 6.4-14.2% over individual models | Requires compatible learned cache transfer and does not imply ordinary agents should replace auditable messages with hidden states | H3 |

### Existing local notes

- [[literature/mcp-dual-stack]]

**Synthesis:** natural language is valuable for people and semantics. It should not automatically be the storage format, synchronization primitive, or intermediate representation for every machine interaction.

---

# 5. Harness efficiency and recursive improvement

## Improve the system around the model, not only the model

| Source | Work moved out of the model | Mechanism | Evidence | Important limit | Thesis |
|---|---|---|---|---|---|
| [SoL-Pi: Scaling Auto-Research Loops for Efficient Agent Harnesses](https://nvlabs.github.io/SoL-Pi/) (2026) | Repeated turns and redundant evidence processing remain accepted as harness overhead | Auto-research searched 152 directions; four harness mechanisms survived capability-gated evaluation | Authors report substantial token/cost reduction on EdgeBench and a lower-cost verified frontier in a swarm experiment | Search cost is real, mechanisms interact, and some benchmarks show reduced solve counts | H1, H4, H5 |
| [frontier-kb harness-evolution notes](../literature/lit-20260910-evo-bench-harness-evolution.md) | Treat the harness as fixed | Search over scaffold/mechanism changes under external verification | Local research synthesis feeding Evolution Lab | Our synthesis is not independent evidence and must never be cited as if it were a paper result | H4 |
| [Evolution Lab](https://github.com/kvnloo/evolution-lab) | Assume every learned component deserves production traffic | Frozen controls, Pareto/MAP-Elites search, promotion gates, simple baselines | Our experimental substrate, not evidence for the thesis yet | Must remain a consumer of evidence and a place to falsify claims | H4 |

**Synthesis:** the useful endpoint of self-improvement is not always a better model. A successful learned behavior may expose a simpler rule, data structure, or algorithm and then be compiled downward.

---

# 6. Agent-native host environment

## The cognitive kernel does not replace the physical OS

| Source | Work moved out of the user/agent | Mechanism | Evidence | Important limit | Thesis |
|---|---|---|---|---|---|
| [Omarchy AI manual](https://omarchy.org/manual/ai/) | Manual installation and host integration of coding agents, system skills, usage views, and local models | Coding-agent CLIs as first-class launchers, default-agent surface, shared skills, usage panel, Ollama/LM Studio integration | Concrete shipping host environment built around agent use | Omarchy is a host environment, not evidence that it should own cognitive scheduling, memory, or authority semantics | H5 |

**Synthesis:** an Agent OS can have two complementary layers: an agent-native host environment and a cognitive runtime that manages expensive semantic computation.

---

# 7. What the current evidence does and does not say

## The convergence we can defend

Across otherwise different research lines, a recurring pattern appears:

```text
before:
    model inference manages semantic work
    + systems bookkeeping

after:
    explicit mechanism handles more bookkeeping
    model sees a smaller, bounded semantic problem
```

The mechanisms differ:

- memory paging
- typed recursive combinators
- DAG scheduling
- protocol schemas
- kernel services
- direct cache communication
- evidence handles
- context compaction

The common direction is **responsibility separation**.

## What we cannot claim yet

We do not yet know:

- what fraction of frontier-model tokens are "Agent OS tax"
- whether one universal kernel API is desirable
- whether explicit schedulers beat model scheduling on every agent workload
- how much context paging should be deterministic vs learned
- whether direct latent communication is practical for heterogeneous production agents
- whether the extra complexity of an Agent OS pays for itself on short tasks
- which abstractions belong in a portable ABI rather than one runtime

Those are experiments.

---

# 8. The simplest reader model

A reader should be able to reduce the whole thesis to one sentence:

> **LLMs are good at understanding meaning. Computers are good at keeping track of things. Stop paying the LLM to do both when you can measure that the simpler mechanism works.**

This map exists to test that sentence, not decorate it.

## Next evidence gaps

The next literature wave should prioritize:

- source notes for RLM, λ-RLM, SRLM, MemGPT, PagedAttention, LLMCompiler, AIOS, AOS, C2C, MCP, and A2A
- one strong counterexample for each hypothesis
- comparable experiment groups where a true quantitative meta-analysis is possible
- classical references for scheduling, working sets, event sourcing, MVCC, actors, and durable workflows
- real coding-agent traces that can estimate the proposed Agent OS tax
