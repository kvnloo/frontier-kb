---
id: homebase-cycle-20260914-004-dtdl-snapshot-vs-telemetry
title: "Cycle 4: DTDL Property/Telemetry vs complete-state snapshots"
type: inbox
status: captured
created: 2026-09-14
updated: 2026-09-14
harnesses: [hermes]
domains: [computer-science, simulation]
confidence: medium
tags: [homebase, digital-twin, dtdl, snapshot, provenance, research-cycle]
---

# Cycle 4 — operational graph vs complete simulation state

## Question
Must a local facility twin keep **typed, restorable Properties** (identity, possession, score, clock, pending contacts, RNG/event sequence) **separate from Telemetry streams and from an opaque physics snapshot**, or can one JSON graph / one FMU blob serve both operations and playable sport?

## Hypothesis
**H1 (supported as DTDL v3 language claim, unmeasured on Homebase):** A Property is **read-only or read/write state with backing storage and synchronization metadata** between the twin and its store; Telemetry is **emitted data** (sensor stream, occupancy stream, alert) without that backing-store contract. Restoring a match from Telemetry logs is not specified by DTDL as equivalent to restoring Properties.[1][2]

**H2 (supported as DTDL composition claim):** A **Component** includes another Interface **by value** (no independent twin identity; v3 forbids nested Components). A **Relationship** is a **by-reference** link whose validity does **not** require the target Interface to be present. Court occupancy as a nested component vs athlete/court identity as graph edges are different restoration problems.[1][2]

**H3 (supported as contrast with cycle 1, not a kernel win):** FMI 3.0 names **getting and setting the complete FMU state** as an opaque capability of an FMU, distinct from getting individual variables. That blob is **not** a typed operations graph (no DTMI, no Property vs Telemetry split). DTDL is **not** a multi-rate communication-point API. Neither document is a sport scoring kernel.[3][1]

**H4 (nearby-wrong, refuted as sufficient):** OMG DDS 1.4 is **data-centric pub/sub** (APIs + QoS for delivering information to matching consumers). It does not define complete-state round trips, sport event identity, or fidelity promotion. Pub/sub ≠ snapshot restoration.[4]

**Not claimed:** Azure Digital Twins as a required cloud; Unreal Replay (docs fetch returned a bot-check stub this cycle — **not evidence**); ISO 23247 (HTTP 403); any FPS number; custom kernel required.

## Host / experiment policy
Measured 2026-09-14 ~05:13 CDT: load averages **11.42 / 6.45 / 5.47**; Mem 23 Gi total, ~7.1 Gi available, swap ~26 Gi used. Charter: under pressure, **research only**. Benchmarks: **not executed**.

## Evidence (primary)

### DTDL Version 3 Language Description
- URL: https://raw.githubusercontent.com/Azure/opendigitaltwins-dtdl/master/DTDL/v3/DTDL.v3.md [1]
- Retrieved 2026-09-14; document length 53034 bytes. Context specifier `dtmi:dtdl:context;3`.
- Metamodel: Interface, Command, Component, Property, Relationship, Telemetry.
- Interface `@id` is a DTMI; contents limited (100,000 elements in hierarchy); Interface text limited to 1 MiByte.
- Telemetry: data **emitted** by a twin (regular sensor stream, computed occupancy stream, occasional alert). Example serializes as `"temp": 42.5` — a payload, not a stored Property.
- Property: **read-only and read/write state**; explicitly includes **synchronization of that state** between distributed components and a **backing store**. Sync metadata exists for every Property and is **not** in the model definition.
- Relationship `target` datatype is DTMI (**by reference**). Component `schema` is Interface (**by value**); cycles forbidden; DTDL v3 Component cannot contain another Component.
- Commands describe operations with optional request/response (e.g. reboot) — not physics steps.

### Azure Digital Twins model overview (product mapping of DTDL)
- URL: https://learn.microsoft.com/en-us/azure/digital-twins/concepts-models [2]
- Models are nouns; twins are instances. Contents: Property (state, backing storage, readable anytime), Relationship (graph, may have properties), Component (integral, **does not need a separate identity**, not independently created/deleted/rearranged).
- DTDL also used by IoT Plug and Play; not exclusive to Azure Digital Twins.
- Supports mixing v2/v3 with extend/component direction restrictions.

### FMI 3.0 (already used in cycle 1; cited only for contrast)
- URL: https://fmi-standard.org/docs/3.0/ [3]
- ToC includes **2.2.7.4 Getting and Setting the Complete FMU State**, distinct from 2.2.7.2 variable get/set, plus Super State **FMU State Settable**. Not re-argued here.

### OMG DDS 1.4 About page
- URL: https://www.omg.org/spec/DDS/About-DDS/ [4]
- Specification Version 1.4; publicationDate 2015-03-30. DCPS model: APIs and communication semantics/QoS for producers to matching consumers. Purpose quoted: efficient delivery of the right information to the right place at the right time. **Not** a complete-state or scoring contract.

## Fact vs interpretation
- **Fact:** DTDL separates Property (stored, synchronized) from Telemetry (emitted).[1]
- **Fact:** Component vs Relationship is by-value identity-less inclusion vs by-reference graph link.[1][2]
- **Fact:** FMI complete FMU state is a different, opaque restore API.[3]
- **Interpretation:** Homebase should treat **match operational Properties** (identity, possession, pending contacts, rule/clock/RNG, committed event IDs) as restorable independently of **render/mesh LOD** and independently of **contact telemetry**. An opaque physics snapshot may exist **in addition**, not as a substitute for the typed graph. Do not put facility geographic coordinates in that graph.
- **Not fact:** That adopting DTDL JSON-LD in production is required; that DDS QoS or Azure graph hosting would restore a rally.

## Decision
Keep charter hypotheses 1–3. **Do not** collapse telemetry logs, physics blobs, and operational identity into one restore path. Prefer a **held-out snapshot round-trip** later: serialize Properties + event IDs + RNG + pending contacts; drop Telemetry and draw state; restore; check next-serve legality and score identity. Still no second physics authority (cycle 2) and no treating FMI as a kernel win (cycle 1). Cycle 3's rejected updater-independence claim is **not** reused.

## Limitations
- Host load precluded the 120s experiment; no Homebase measurements.
- Unreal Replay documentation fetch was a ~19-character bot-check page — discarded.
- ISO 23247 landing page returned 403 — not cited.
- Azure product page is vendor mapping of DTDL, not an independent standard body; language source of truth is the GitHub DTDL v3 document.[1]
- No arXiv this cycle. No GPU, no installs, no production edits.

## Next angle
When load < ~4 and available RAM > ~8 GiB: **held-out rally/net tape** (cycles 1–2) **or** snapshot round-trip of Properties vs Telemetry-stripped restore. Else: **data locality / jobs** (broadphase vs rules vs draw work independently) without engine replacement. Do not re-run cycle 3 independence claims without a pinned on/off command tape.

## Dedup
Does not repeat FMI clocks/tick groups (cycle 1), CCD/TOI (cycle 2), or scoreboard-updater verification (cycle 3). Architecture-research already recommends persisting seed/tick/commands/keyframes; this cycle adds the **Property vs Telemetry vs opaque FMU** distinction those schemas did not cite.

## Validation and publication boundary
Real frontmatter newlines. Markdown-only vault write; no `kb_store` ingest, no DSN read, no commit/push, no cron change, no G1/M1 acceptance.
