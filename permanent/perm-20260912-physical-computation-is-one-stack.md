---
id: perm-20260912-physical-computation-is-one-stack
title: "Physical computation is one stack: Landauer → spikes → notes → tokens"
type: permanent
status: active
created: 2026-09-12
updated: 2026-09-12
harnesses: [cursor, omp, hermes]
domains: [physics, information-theory, neuroscience, ai-ml, cs, learning-acceleration]
confidence: high
tags: [permanent, toe, landauer, vault]
---

# Physical computation is one stack: Landauer → spikes → notes → tokens

## Idea (atomic)

There is one stack, not two magics (biology vs silicon). **Irreversible computation costs energy** (Landauer). Brains pay in ATP-per-spike and therefore evolved **sparse, local, event-driven** codes (Attwell–Laughlin). Transformers pay in watts-per-token and therefore evolved **dense, batched, global** codes. Frontier-KB already implemented the brain policy in software: notes are neurons, wikilinks are synapses, retrieve/search are spikes, idle edges decay, noise is pruned. The 2026 fly meme is the same diagram at cell resolution. Qwen3.8-27B is a different layer: a cultural-language cortex trained in tokens. Kardashev (AODL inbox) changes **budgets** (joules, tokens, spawn), not kinds.

```
physics:     kT ln2 per erased bit
biology:     ~0.25 μW fly CNS; sparse spikes; mushroom-body adapter
emulation:   MaleCNS LIF on CPU/GPU (efficiency inverted)
vault:       notes / synapses / synapse_loop / humanity-vault
harness:     frozen worker + evolver + SoL-Pi compact
language:    Qwen3.8-27B SVLM worker (tokens, tools, GUI)
```

Same conservation law: **signal that does not change a weight is exposure, not encoding**. Sung/Huberman on the human side; Hebb + sleep-SHY on the fly side; `synapse_loop.py` on the vault side.

## Why it matters for our harnesses

When someone says "the fly will replace the 27B," they are mixing layers. Route **language and SWE** to the SVLM. Route **durable claims** to the vault. Route **closed-loop visuo-motor** (if ever) to a connectome or a distilled motif on the right substrate. Do not add a `consciousness` kind.

## Related

- [[literature/lit-20260912-fly-connectome-task-meme]]
- [[literature/lit-20260912-biology-vs-silicon-energy]]
- [[literature/lit-20260912-qwen38-27b-vs-fly-snn]]
- [[permanent/perm-20260911-kb-is-a-brain-prune-and-potentiate]]
- [[permanent/perm-20260911-encoding-beats-exposure]]
- [[permanent/perm-20260911-plasticity-needs-alert-then-rest]]
- [[permanent/perm-20260910-small-models-are-workers-or-specialists]]
- [[permanent/perm-20260817-market-is-allocation-policy]]
- [[inbox/cursor/inbox-cursor-aodl-thesis-intent-20260912]]
- [[domains/physics]]
