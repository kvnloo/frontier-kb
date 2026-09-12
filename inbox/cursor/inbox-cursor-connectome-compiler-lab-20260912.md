---
id: inbox-cursor-connectome-compiler-lab-20260912
title: "Connectome as compiler: fru/dsx → split-GAL4 → optogenetics workflows that save months"
type: inbox
status: draft
created: 2026-09-12
updated: 2026-09-12
node: cursor
harnesses: [cursor]
domains: [neuroscience]
tags: [inbox, fly, malecns, fruitless, doublesex, split-gal4, neuronbridge, optogenetics]
confidence: high
sources: ["https://www.cell.com/cell/fulltext/S0092-8674(26)00942-6", "https://male-cns.janelia.org/", "https://neuronbridge.janelia.org", "https://splitgal4.janelia.org"]
---

# Connectome as compiler: fru/dsx → split-GAL4 → optogenetics (labs, today)

## Claim

In *Drosophila*, **fruitless/doublesex compile sex into wiring**. The 2024–2026 connectomes are the compiled binary. **split-GAL4 is the debugger**; **NeuronBridge is the linker** from EM cell types to genetic addresses; **optogenetics is the runtime test**. A lab that starts from MaleCNS/FlyWire/BANC plus existing FlyLight lines can skip months of GAL4 screening and avoid testing the wrong sex, the wrong neck, or a 2-synapse edge.

## Compiler model (what to tell a fly lab)

| Layer | What it is | Do not confuse with |
| --- | --- | --- |
| Source | sex-determination cascade → male/female *fru*/*dsx* isoforms | a private "courtship brain" |
| Compile | alternative splicing + hemilineage programs → cell number, morphology, synapses | transcriptome-only labels |
| Binary | MaleCNS / FlyWire / BANC / MANC / FANC / L1 larva graphs | LIF meme models (Shiu is a *prior*, not the fly) |
| Linker | NeuronBridge color-depth MIP + PPPM | eyeballing confocal vs EM by hand |
| Injector | split-GAL4 / split-LexA (AD ∩ DBD) | pan-*fru*-GAL4 (thousands of cells) |
| Runtime | CsChrimson / GtACR1 / GCaMP in both sexes | one sex, one intensity, one assay |

MaleCNS Cell 2026: sex-specific/dimorphic types are concentrated in **higher centers**; sensory and motor periphery are largely isomorphic. Dimorphic neurons **reroute** shared sensory streams (changeover switches). Male-specific synapses form **hotspots**. Most but not all dimorphism is *fru*/*dsx*: ~89% of male-specific and ~61% of dimorphic central-brain neurons are *fru+*/*dsx+*; **11% of sex-specific and 39% of dimorphic neurons are fru−/dsx−**. Screening only *fru* reagents misses those.

## Which volume (wrong volume wastes a year)

| Question | Volume | Portal |
| --- | --- | --- |
| Male brain **and** VNC, intact neck, *fru*/*dsx* + dimorphism | **MaleCNS v1.0** (166,700 neurons, 11,710 types; Cell 2026) | [male-cns.janelia.org](https://male-cns.janelia.org/) · [neuPrint `male-cns:v1.0`](https://neuprint.janelia.org) · [Dimorphism Explorer](https://male-cns.janelia.org/build/dimorphism_overview/) · [Cell Type Explorer](https://reiserlab.github.io/celltype-explorer-drosophila-male-cns/) |
| Female whole brain | FlyWire FAFB v783 (~139k neurons) | [codex.flywire.ai](https://codex.flywire.ai/) |
| Female brain **and** cord | **BANC** (Nature 2026) | [codex.flywire.ai/banc](https://codex.flywire.ai/banc) · [banc.community](https://banc.community) |
| Male VNC only | MANC | [Janelia MANC](https://www.janelia.org/project-team/flyem/manc-connectome) |
| Female VNC | FANC | Azevedo et al. Nature 2024 |
| Larva (L1 female CNS) | L1EM / Winding 2023 | [VFB EM docs](https://www.virtualflybrain.org/docs/data/em/) |
| Type-name Rosetta stone | MaleCNS (`flywireType`, `mancType`, `hemibrainType`) | [downloads](https://male-cns.janelia.org/download/) |

HOLD: Codex still listed **MCNS v0.9** in 2026; **neuPrint `male-cns:v1.0`** (released 2026-06-08) is the paper snapshot. NeuronBridge MaleCNS matches landed **2025-11-07**.

---

## Workflow 1 — Overnight: gene/behavior → nodes → existing drivers

**Saves:** 3–12 months of "which GAL4 labels my neuron?"

1. Name the behavior and the **sex** (courtship song, receptivity, aggression, feeding, walking). Pick the volume above.
2. Open **Dimorphism Explorer** (male vs FlyWire female) or Codex `gene==Fruitless` / `Doublesex` (female). Filter by hemilineage (`ALv1`, `DL2_ventral`, `SMPpv1`, …) not just type name.
3. Classify every candidate as **isomorphic / dimorphic / male-specific / female-specific**. Peripheral sensory/motor is usually isomorphic; the interesting switch is often 1–2 hops into a higher center (LH, PVLP, SMP, pC1/P1, vpoEN).
4. Pull **upstream sensory** and **downstream DNs/MNs** in neuPrint (`fetch_adjacencies`). Drop edges that fail Workflow 5's reliability cut.
5. Search **NeuronBridge** with the MaleCNS / FlyWire / MANC body ID → **Color Depth Search**. Prefer an existing **split-GAL4** hit over Gen1 GAL4.
6. Confirm the line at [splitgal4.janelia.org](https://splitgal4.janelia.org). Order from **BDSC** ("Order from Bloomington"). If no button: `flybank@janelia.hhmi.org`.
7. Cross to **UAS-CsChrimson-mVenus** (BDSC 55134 / Janelia 50416) and a **GtACR1** silencer. Image the expression in **both sexes** before behavior. FlyLight protocols: [janelia.org/project-team/flylight/protocols](https://www.janelia.org/project-team/flylight/protocols).

Worked example already in the literature: MaleCNS identifies a **vpoEN changeover switch** (isomorphic morphology; female output → vpoDN/DNp37; male output → P1_6a). Do not spend a year asking "is vpoEN male-specific?" — it is not. Test **downstream partners**, both sexes.

LoVP92 is the only male-specific visual projection neuron ("love-spot"): isomorphic VPNs become *functionally* dimorphic via co-convergence. If the behavior is visual courtship, start here rather than screening optic-lobe GAL4s.

DNb07 ⊣ DNp63 (inhibitory axon–axon) share olfactory/visual flow; **split-GAL4 reagents already exist** (Zung et al. 2025 DN catalogue). That is a paper-ready hypothesis with stocks on the shelf.

## Workflow 2 — EM cell → existing split (do not build a line)

**Saves:** 2–6 months of hemidriver crossing.

Practical walkthrough (Kyle Thieringer, used in labs now): [notes.kylethieringer.com/lore/how-to-find-genetic-drivers-for-candidate-neurons](https://notes.kylethieringer.com/lore/how-to-find-genetic-drivers-for-candidate-neurons)

1. NeuronBridge search by **dataset-native ID** (MaleCNS, FlyWire, MANC, hemibrain). Click **Color Depth Search Results** for the matching library.
2. Rank: (a) published split-GAL4 with sparse MCFO, (b) SS line that already exists, (c) two Gen1 hits you could split.
3. Open the hit: EM left, LM middle/right. Require morphology match of the **distinctive arbors**, not just soma position.
4. Stock: search BDSC by SS#### / R##X##. Meissner et al. eLife 2025: **3,060 adult + 1,373 larval** curated splits from >77,000 combinations. Janelia already paid that cost.

Collections to search **before** designing a new split:

- Whole CNS: Meissner et al. eLife 2025 · [splitgal4.janelia.org](https://splitgal4.janelia.org)
- Descending neurons: Zung, Namiki, Meissner et al. 2025 bioRxiv [10.1101/2025.02.22.639679](https://doi.org/10.1101/2025.02.22.639679) — Stürner Nature 2025 matched **51% of DN types to LM driver lines**
- Mushroom body / learning: Shuai et al. eLife 2025, 800+ splits, ~300 types, including refined sugar reward **SS87269** · [elifesciences.org/articles/94168](https://elifesciences.org/articles/94168)
- SEZ / feeding: Sterne et al. eLife 2021, 277 lines, 138 types · [elifesciences.org/articles/71679](https://elifesciences.org/articles/71679) — this is the set Shiu actually activated
- Larva: Meissner larval set; raw stacks [raw.larval.flylight.virtualflybrain.org](https://raw.larval.flylight.virtualflybrain.org/)

## Workflow 3 — Design a new split (only if Workflow 2 is empty)

**Saves:** vs. screening a Gen1 library; still ~2–3 months of genetics, not a year of anatomy.

R client: [natverse.org/neuronbridger](https://natverse.org/neuronbridger/) · vignette [design_split_gal4](https://natverse.org/neuronbridger/articles/design_split_gal4.html)

```r
# hemibrain/FlyWire/MANC body id → ranked GAL4/LexA
ns <- neuronbridge_search(target_id, threshold = 2000)
# predict intersection of two hemidrivers
potential.split <- neuronbridge_predict_split(
  line1 = "R58G03", line2 = "R71D08",
  threshold1 = 2000, threshold2 = 2000)
```

Fewer surviving predicted cells = sparser line. Then: order AD and DBD hemidrivers from BDSC → make stable split → image CsChrimson-mVenus + nc82 → only then behavior.

MaleCNS / FlyWire meshes must be in **JRC2018U_HR** (brain) or **JRC2018VNCU_HR** (VNC) for CDM search. Paper: Clements et al. BMC Bioinformatics 2024 [10.1186/s12859-024-05732-7](https://bmcbioinformatics.biomedcentral.com/articles/10.1186/s12859-024-05732-7). Method: Otsuna color-depth MIP.

Reverse direction (published line → EM cell): [match_em_to_line](https://natverse.org/neuronbridger/articles/match_em_to_line.html) (AstA-SEZ / SS32423 example).

## Workflow 4 — Graph designs the optogenetic experiment

**Saves:** activating 40 cell types when 5 would falsify the model.

### 4a. Rank nodes, do not screen neuropils

- **Direct edges:** neuPrint / Codex / `malecns` R ([natverse.org/malecns](https://natverse.org/malecns/)) / `neuprint-python`.
- **Indirect influence (multi-hop):** BANC influence metric — Bates, Phelps, Kim, Yang et al. Nature 2026; code [ConnectomeInfluenceCalculator](https://github.com/DrugowitschLab/ConnectomeInfluenceCalculator) · R [natverse/influencer](https://github.com/natverse/influencer/). Tutorial already compares **ORN → pC1 in BANC vs MaleCNS**: [fly_connectome_data_tutorial](https://github.com/sjcabs/fly_connectome_data_tutorial/blob/main/R/04_indirect_connectivity.Rmd).
- **In silico activation/silence:** Shiu et al. Nature 2024 LIF on FlyWire. Activate at 10/50/200 Hz, read identified MNs. Code: [github.com/philshiu/Drosophila_brain_model](https://github.com/philshiu/Drosophila_brain_model). **106 SEZ splits → 11 predicted to drive MN9/proboscis; 10/11 confirmed; 4/95 false negatives at 50 Hz.** That is a month of behavior instead of a year of SEZ screening.

HOLD: Shiu is **female FlyWire**, identical LIF cells, no gap junctions/peptides. Transfer to MaleCNS is unvalidated (see [[literature/lit-20260912-shiu-huang-malecns-physiology]]). Use it to **rank**, then test.

### 4b. The Lillvis triple (courtship song, generalizable)

Lillvis et al. Current Biology 2024 used MANC + 58 new splits covering ≥40 VNC types (17/22 *fru+*/*dsx+* song types) and three assays **per line**:

1. **GtACR1 silence** during courtship (necessity)
2. **CsChrimson activate** in isolated males (sufficiency)
3. **CsChrimson during courtship** (can it retune ongoing song)

Intensities 0.3–42 μW/mm². Nested pulse ⊂ sine architecture. Companion physiology: Shiozaki et al. Nat Neurosci 2024.

Do not run only (2). Sufficiency without necessity is how labs publish the wrong node.

### 4c. Command-like DNs are networks

Braun et al. Nature 2024: DNp09 / aDN2 / MDN **recruit other DNs**. Activating DNp09 and concluding "this cell is walking" is incomplete — the connectome says you co-activated DNa02/DNb02. If the behavior is flexible, **silence the downstream DN set** (split-LexA + GAL4) rather than building a story around one cell.

### 4d. Effector recipe (lab bench)

- **Activate:** CsChrimson, all-trans-retinal in food, dark-reared, 627–660 nm. BDSC 55134.
- **Silence (acute):** GtACR1, green light.
- **Image:** GCaMP6s/7f; for DNs, neck-connective 2P as in Braun 2024.
- Always **two independent splits** for the same type when claiming a Cell/Nature result.

## Workflow 5 — Comparative male / female / larva *before* claiming dimorphism

**Saves:** a year of "we discovered a male-only neuron" that is isomorphic in FlyWire, or a "novel type" that is a hemibrain split.

1. Match the type in **MaleCNS** (names are the consensus atlas; ~97.5% matched; MaleCNS revised ~4% of FlyWire types).
2. Overlay female meshes (Neuroglancer on the MaleCNS site includes FlyWire meshes transformed into male space).
3. Apply **Schlegel et al. Nature 2024** reliability: conservation of a type–type edge rises with synapse count. Weak ≥1-synapse edges are often technical or idiosyncratic. Lab rule used across 2024–2026 papers: **require ≥5 synapses and presence in both hemispheres (and, for dimorphism, a consistent MaleCNS vs FlyWire/BANC difference)**.
4. Check *fru*/*dsx* **confidence flags**. MaleCNS annotated 4,505 *fru* (2,695 high-confidence) and 407 *dsx* (332 high-confidence) by co-registering LM clones — **not RNA-seq**. VNC *fru*/*dsx* is not exhaustive.
5. If the neuron is a DN/AN, read **Stürner et al. Nature 2025** before tracing: dimorphic DNa12 (aSP22, male courtship), song ANs from hemilineage 08B, female DNp13 (ovipositor).
6. Larval homology: L1 connectome (Winding, Pedigo et al. Science 2023) + larval splits. Adult dimorphism is often a **remodeling of a shared larval hemilineage**, not a new adult cell. Truman/Zlatic lineage maps + MaleCNS `trumanHl` / `itoLeeHl` fields.

Deutsch et al. 2025 (female FlyWire *fru*/*dsx*, ~98 types / ~1700 cells; Codex labels; [github.com/deutschlab/sexual-dimorphism-paper](https://github.com/deutschlab/sexual-dimorphism-paper)): *fru*/*dsx* cells are interconnected but **not a private network** — most synapses are to isomorphic partners. That is why activating pan-*fru* is uninterpretable.

Cambridge thesis (Beckett; MaleCNS chapter) already did the gold-standard close: **LHAV2b2** as a courtship brake (DA1 + VL2a excitatory vs VA1v inhibitory). GCaMP: PAA on VL2a is close-range. **GtACR1 of LHAV2b2 → increased male–male courtship.** That is the template: connectome prediction → existing/new split → one imaging + one silencing experiment.

## Workflow 6 — Intact-neck sensorimotor (only MaleCNS or BANC)

FAFB and MANC are **physically cut at the neck**. For any claim of the form "this brain cell drives that muscle," you need MaleCNS (male) or BANC (female). Cheong/Marin/Takemura MANC papers (eLife 2024) still matter for VNC internals; Stürner 2025 is the bridge; MaleCNS/BANC are the finished necks.

## Months you still spend (honest)

Genetics + behavior still take calendar time. What the graph **eliminates**: (1) screening 100 Gen1 GAL4s, (2) building a split that already exists, (3) testing 90 cell types Shiu/influence already call negative, (4) discovering "dimorphism" that is a dataset mismatch, (5) treating pan-*fru* as a cell type.

---

## Papers 2024–2026 (Cell / Nature + the reagents you actually click)

### Cell / Nature (core)

| Paper | Why a lab opens it | URL |
| --- | --- | --- |
| Berg, Beckett, Marin, Jefferis, Rubin et al. **Cell** 2026 189:5504–5526.e15. Sexual dimorphism in the complete *Drosophila* male CNS connectome | The male CNS + male–female comparison + *fru*/*dsx* | [Cell](https://www.cell.com/cell/fulltext/S0092-8674(26)00942-6) · [DOI](https://doi.org/10.1016/j.cell.2026.08.015) · [PMC preprint](https://pmc.ncbi.nlm.nih.gov/articles/PMC12636603/) · [bioRxiv](https://www.biorxiv.org/content/10.1101/2025.10.09.680999) |
| Dorkenwald et al. **Nature** 2024. Neuronal wiring diagram of an adult brain | FlyWire female brain | [10.1038/s41586-024-07558-y](https://www.nature.com/articles/s41586-024-07558-y) |
| Schlegel et al. **Nature** 2024. Whole-brain annotation and multi-connectome cell typing | Type atlas + which edges are reliable | [10.1038/s41586-024-07686-5](https://www.nature.com/articles/s41586-024-07686-5) |
| Shiu et al. **Nature** 2024. Connectome-constrained LIF predicts feeding/grooming | In silico screen → 91% match to split-GAL4/CsChrimson | [10.1038/s41586-024-07763-9](https://www.nature.com/articles/s41586-024-07763-9) |
| Huang, Luo et al. **Nature** 2024. MB dopamine STM/LTM | Plasticity is KC×DAN×MBON, not whole-graph SGD | [10.1038/s41586-024-07819-w](https://www.nature.com/articles/s41586-024-07819-w) |
| Bates, Phelps, Kim, Yang et al. **Nature** 2026. Distributed control circuits across a brain-and-cord connectome | BANC female CNS; influence scores | [10.1038/s41586-026-10735-w](https://www.nature.com/articles/s41586-026-10735-w) · preprint [10.1101/2025.07.31.667571](https://www.biorxiv.org/content/10.1101/2025.07.31.667571) |
| Stürner et al. **Nature** 2025. Comparative connectomics of DNs and ANs | Sex-dimorphic neck neurons + 51% DN↔driver match | [10.1038/s41586-025-08925-z](https://www.nature.com/articles/s41586-025-08925-z) |
| Azevedo et al. **Nature** 2024. Female VNC (FANC) | Female cord; MN atlas | [10.1038/s41586-024-07389-x](https://www.nature.com/articles/s41586-024-07389-x) |
| Lesser et al. **Nature** 2024. Leg/wing premotor synaptic architecture | Premotor logic | [10.1038/s41586-024-07600-z](https://www.nature.com/articles/s41586-024-07600-z) |
| Braun, Hurtak, Ramdya et al. **Nature** 2024. Descending networks transform command signals | DNp09 recruits a DN population; all-optical test | [10.1038/s41586-024-07523-9](https://www.nature.com/articles/s41586-024-07523-9) |

### Reagents + matching (the "today" stack)

| Paper | URL |
| --- | --- |
| Meissner et al. **eLife** 2025. Split-GAL4 driver line resource (3060 adult / 1373 larva) | [elifesciences.org/articles/98405](https://elifesciences.org/articles/98405) · [10.7554/eLife.98405](https://doi.org/10.7554/eLife.98405) |
| Clements et al. **BMC Bioinformatics** 2024. NeuronBridge | [10.1186/s12859-024-05732-7](https://bmcbioinformatics.biomedcentral.com/articles/10.1186/s12859-024-05732-7) |
| Shuai et al. **eLife** 2025. Driver lines for associative learning | [elifesciences.org/articles/94168](https://elifesciences.org/articles/94168) |
| Zung et al. 2025. Updated DN split-GAL4 catalogue | [10.1101/2025.02.22.639679](https://doi.org/10.1101/2025.02.22.639679) |
| Deutsch et al. 2025. Sexually dimorphic neurons in FlyWire | [10.1101/2025.06.10.658788](https://www.biorxiv.org/content/10.1101/2025.06.10.658788v2) · Codex `gene==Fruitless` |

### MANC / song / larva

| Paper | URL |
| --- | --- |
| Takemura et al. **eLife** 2024. MANC connectome | [10.7554/eLife.97769](https://doi.org/10.7554/eLife.97769) |
| Cheong et al. **eLife** 2024. DN → MN in MANC | [10.7554/eLife.96084](https://doi.org/10.7554/eLife.96084) |
| Marin et al. **eLife** 2024. MANC annotation | [10.7554/eLife.97766](https://doi.org/10.7554/eLife.97766) |
| Lillvis et al. **Curr Biol** 2024. Nested song circuits + 58 splits | [10.1016/j.cub.2024.01.015](https://www.cell.com/current-biology/fulltext/S0960-9822(24)00015-0) |
| Shiozaki et al. **Nat Neurosci** 2024. Nested song activity | [10.1038/s41593-024-01738-9](https://www.nature.com/articles/s41593-024-01738-9) |
| Winding, Pedigo et al. **Science** 2023. Larval CNS connectome (still the larval map) | [10.1126/science.add9330](https://www.science.org/doi/10.1126/science.add9330) |

## Tool URLs (bookmark bar)

- MaleCNS hub: https://male-cns.janelia.org/
- Dimorphism Explorer: https://male-cns.janelia.org/build/dimorphism_overview/
- Cell Type Explorer: https://reiserlab.github.io/celltype-explorer-drosophila-male-cns/
- neuPrint: https://neuprint.janelia.org (dataset `male-cns:v1.0`)
- NeuronBridge: https://neuronbridge.janelia.org
- Split-GAL4: https://splitgal4.janelia.org
- FlyLight collection: https://www.janelia.org/open-science/fly-light-split-gal4-driver-collection
- Codex: https://codex.flywire.ai/ · BANC: https://codex.flywire.ai/banc
- VFB: https://www.virtualflybrain.org/
- BDSC orders: https://bdsc.indiana.edu/
- Janelia MANC: https://www.janelia.org/project-team/flyem/male-cns-connectome
- `malecns` R: https://natverse.org/malecns/
- neuronbridger: https://natverse.org/neuronbridger/
- Shiu model: https://github.com/philshiu/Drosophila_brain_model
- Influence: https://github.com/DrugowitschLab/ConnectomeInfluenceCalculator

## Fact vs interpretation

- Fact: MaleCNS v1.0 + FlyWire + BANC + MANC/FANC + L1 now cover male/female adult CNS and larva at EM resolution; NeuronBridge indexes MaleCNS since 2025-11-07; 3060 adult splits are orderable.
- Fact: Shiu's unbiased SEZ optogenetic screen matched LIF predictions at >90%; Lillvis/Braun/Beckett-style experiments are the 2024–2026 template.
- Interpretation: "the connectome is a compiler from genes to behavior" is a **lab planning metaphor**. *fru*/*dsx* specify dimorphic wiring; they do not encode the behavior. Behavior still requires neuromodulation, experience (MB), and population DNs.
- HOLD: Do not treat fly-wirehead/Stonkfly LIF demos as experimental design. Use Shiu on FlyWire IDs, then MaleCNS anatomy, then real splits.

## Next action

Promote to `literature/lit-20260912-connectome-compiler-lab-workflows` after CoS review. Link from [[domains/neuroscience]] and [[literature/lit-20260912-shiu-huang-malecns-physiology]].

## Links

- [[literature/lit-20260912-shiu-huang-malecns-physiology]]
- [[literature/lit-20260912-fly-connectome-task-meme]]
- [[permanent/perm-20260912-connectome-is-wiring-not-a-trainable-llm]]
- [[permanent/perm-20260912-mushroom-body-is-the-only-plastic-specialist]]
- [[inbox/cursor/inbox-cursor-fly-connectome-wave-20260912]]
