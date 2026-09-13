---
id: lit-20260912-optic-lobe-visual-front-end
title: "Drosophila optic lobe is a ~800-pixel multi-task visual front-end, not a tiny CNN"
type: literature
status: active
created: 2026-09-12
updated: 2026-09-12
sources:
  - "https://www.nature.com/articles/s41586-025-08746-0"
  - "https://www.nature.com/articles/s41586-024-07981-1"
  - "https://www.nature.com/articles/s41586-024-07939-3"
  - "https://www.nature.com/articles/s41586-024-07558-y"
  - "https://codex.flywire.ai/?dataset=maol"
  - "https://www.janelia.org/project-team/flyem/optic-lobe"
  - "https://doi.org/10.1038/nature24626"
  - "https://doi.org/10.1038/s41593-024-01640-4"
  - "https://www.jneurosci.org/content/35/19/7587"
  - "https://www.pnas.org/doi/10.1073/pnas.1219068110"
  - "https://doi.org/10.1126/scirobotics.adi0591"
  - "https://doi.org/10.1109/icra48891.2023.10161258"
  - "https://doi.org/10.1371/journal.pbio.0050116"
  - "https://doi.org/10.1038/236"
harnesses: [cursor]
domains: [neuroscience, ai-ml, physics]
confidence: high
tags: [literature, fly, optic-lobe, motion, loom, color, connectome, compound-eye]
---

# Drosophila optic lobe is a ~800-pixel multi-task visual front-end, not a tiny CNN

## Claim (one sentence)

The fruit-fly optic lobe is a **retinotopic, identified, multi-task feature bank** (~50k neurons / ~800 columns per eye) that compresses photoreceptors into ~4,500 visual-projection channels for motion, loom, color, figure-ground, and collision; what is uniquely useful versus a tiny CNN is the **copyable algorithms and ethological bottleneck**, not emulating 50k cells on a GPU.

## Evidence

### Connectomes (2024–2026)

| Dataset | Animal / region | Scale | Paper / portal |
| --- | --- | --- | --- |
| FlyWire FAFB v783 | Female adult brain | 139,255 neurons, 54.5M chemical synapses | Dorkenwald et al. Nature 2024 https://www.nature.com/articles/s41586-024-07558-y |
| FlyWire optic-lobe parts list | Female right OL intrinsic | ~38,500 intrinsic neurons → **227 types**; +3,900 VPNs, 250 VCNs, ~4,700 photoreceptors | Matsliah, Yu et al. Nature 2024 https://www.nature.com/articles/s41586-024-07981-1 |
| MAOL / optic-lobe:v1.1 | Male right OL (FlyEM FIB-SEM; first proofread region of MaleCNS) | Codex: **52,445 neurons, 6,484,936 connections**; Nern: ~**53,000 neurons, 732 types**; ~4,500 VPNs / 352 types | Nern, Loesche, Takemura et al. Nature 2025 https://www.nature.com/articles/s41586-025-08746-0 ; https://www.janelia.org/project-team/flyem/optic-lobe ; https://codex.flywire.ai/?dataset=maol |
| MaleCNS / MCNS | Male whole CNS (includes both OLs + VNC) | 166,694–166,700 neurons | Codex MCNS v0.9; Cell 2026 |

Nern et al.: 60 cell types account for >50% of synapses and ~75% of neurons. VPNs compress “nearly 50,000 local neurons” into ~4,500 cells (~3,000 LC/LPC/LLPC/LPLC + ~500 MeTu). About half of types were newly named; split-GAL4 lines are matched to the catalogue. Data: neuPrint `optic-lobe:v1.1`; Neuroglancer `gs://flyem-optic-lobe/v1.1/`. Code: https://github.com/reiserlab/male-drosophila-visual-system-connectome-code

Follow-ons: Hoeller, Zhao, Nern, Romani, Reiser, bioRxiv 2025-12-22, “The organization of visual pathways in the Drosophila brain” https://doi.org/10.64898/2025.12.22.696097 ; brainwide VPN/VCN/bilateral analysis of FAFB, bioRxiv 2026-02-03 https://doi.org/10.64898/2026.02.02.700492

### Identified algorithms (what the lobe actually computes)

**Motion (Hassenstein–Reichardt / Barlow–Levick hybrid).** T4 (ON) and T5 (OFF) are the first direction-selective cells; four subtypes map onto four lobula-plate layers (front-to-back, back-to-front, up, down). Connectomes show spatially offset excitatory vs inhibitory inputs on T4/T5 dendrites (Mi1/Tm3/Mi9/Mi4/C3/CT1 for T4; Tm1/2/4/9/CT1 for T5) — a three-arm detector that contains both HR correlation and BL veto as subsets (Shinomiya et al. eLife 2019; Takemura et al. 2017). Downstream: HS/VS LPTCs integrate wide-field optic flow; LPi neurons implement motion opponency (Mauss / Borst; Nature Neuroscience 2023). Columnar GABAergic C2/C3 feedback is required for direction selectivity (2025 preprint).

**Loom / collision.** LPLC2 is an ultra-selective looming detector: cross-shaped dendrites read all four T4/T5 layers so **outward radial motion excites, inward motion inhibits** (Klapoetke, Nern, Reiser, Card, Nature 2017 https://doi.org/10.1038/nature24626). Population tiles visual space and synapses onto giant-fiber descending neurons that drive jump takeoff. LC4 supplies angular **velocity**; LPLC2 supplies a Gaussian **size** component; their sum on GF predicts spike timing and short vs long takeoff (Ache et al. Current Biology 2019). LC6/LC16 also loom-tuned; LPLC1 supports back-to-front slowing.

**Color (R7/R8).** Inner photoreceptors: pale/yellow R7 (Rh3 UV / Rh4 UV) and R8 (Rh5 blue / Rh6 green). Color opponency begins at R7/R8 terminals. Tm5a/b (R7), Tm5c (R8), Tm20 are hue-selective; **recurrent Tm lateral connections are required** — silencing recurrence broadens tuning (Christenson, Sanz Diez, Abbott, Behnia, Nature Neuroscience 2024 https://doi.org/10.1038/s41593-024-01640-4). Matsliah cluster analysis adds Tm5d/e/f as a hypothetical color subsystem. Longden et al. Nat Commun 2023: ON vs OFF motion pathways have different spectral sensitivities, aiding detection of approaching colored objects.

**Figure–ground.** LC12 responds to a figure’s leading edge and is suppressed by ground motion; LC9 and LC10a cluster figure-like stimuli (including figure opposite ground) away from ground alone (Aptekar / Frye, J Neurosci 2015 https://www.jneurosci.org/content/35/19/7587). LC10 also small-object / courtship tracking.

**Collision avoidance as a robot primitive.** The same T4/T5 → LPTC / VPN stack implements: (1) translational optic-flow balance (wall avoidance), (2) expansion/divergence (head-on collision), (3) loom (predator/obstacle), (4) figure tracking. This is the Franceschini / Serres / Ruffier / de Croon insect-to-robot lineage, now pin-addressable in the connectome.

### Connectome-constrained CNNs (flyvis)

Lappalainen, Tschopp, Turaga, Macke et al. Nature 2024 https://www.nature.com/articles/s41586-024-07939-3

- Architecture: 64 motion-pathway cell types, tiled over **721 hexagonal columns** → **45,669 neurons, 1,513,231 synapses**.
- Free parameters: **734** (65 τ, 65 Vrest, 604 unitary synapse scales). Signs and synapse counts are frozen from the connectome.
- Task: optic-flow estimation (Sintel), **no neural recordings in the loss**. Ensemble of 50 models. Recovers ON/OFF split and T4/T5 direction selectivity vs 26 physiology papers.
- Code: https://github.com/TuragaLab/flyvis — `NumberOfParams(free=734, fixed=2959)`.
- Interpretation: sparsity + type-homogeneous weights make connectivity **identifiable**. A dense CNN with 45k units would have millions of free weights. **No FLOPs or wattage reported** for flyvis inference.

### What is uniquely useful vs a tiny CNN

A TinyML CNN (NanoFlowNet: 170,881 params, 5.5–9.3 FPS on GAP8; PULP-Frontnet 64–86 mW; MCU-class models in the milliwatt–tens-of-milliwatt band) already does **one** vision task (dense flow, detection) on a conventional camera. The optic lobe is not a better ImageNet classifier.

Uniquely useful **if you steal the algorithms / sensor co-design**, not if you emulate the graph:

1. **Multi-task from ~800 pixels.** One retina feeds parallel, named channels: 4-direction ON/OFF motion, loom, small object, figure-ground, hue, wide-field flow — without a new head per task. A tiny CNN is typically single-task; adding loom+color+figure is more data and more params.
2. **Geometry is the filter.** LPLC2’s cross dendrites *are* radial-motion opponency. T4’s three-arm dendrite *is* the EMD. Hard to get that from 170k learned conv weights without lots of examples or NAS.
3. **Identified bottleneck.** ~50k local cells → ~4,500 VPNs already routed to motor programs (jump, turn, courtship). A CNN last layer is generic; you still train a policy.
4. **Parameter count after architecture is known.** flyvis: 45k neurons, **734** free params. That is the scientific object: a **constrained mechanistic net**, not a bigger CNN.
5. **Sensor match.** ~4–5° interommatidial angle, panoramic FOV, high temporal bandwidth, local gain control. EMDs are cheap at that sampling; CNNs assume a high-res camera + ADC + DRAM.
6. **Recurrence for hue, not feedforward RGB.** Tiny CNNs do not implement Tm recurrence unless you add it.
7. **Where the tiny CNN wins.** Semantic texture, learned robustness, existing cameras/MCUs, ImageNet-like tasks. **Emulating 50k LIF cells on CPU/GPU is worse than MobileNet** (see [[literature/lit-20260912-biology-vs-silicon-energy]]): the nanowatt advantage lives in analog/neuromorphic substrate, not in a von Neumann replay of MaleCNS.

### Measured compute / energy

**Living fly (biology, not silicon):**

- Whole CNS: **~0.12 μW** (Laughlin-style O2 budget) to **~0.26 μW** (explanted-brain calorimetry). [[literature/lit-20260912-biology-vs-silicon-energy]]
- Photoreceptors dominate visual cost. Blowfly R1–6: **7.5×10⁹ ATP/s**, ~1000 bit/s → **7×10⁶ ATP/bit** (Laughlin, de Ruyter van Steveninck, Anderson, Nat Neurosci 1998 https://doi.org/10.1038/236). *D. melanogaster* R1–6: ~**200 bit/s** daylight, ~10× cheaper per bit than blowfly (Niven, Anderson, Laughlin, PLoS Biol 2007 https://doi.org/10.1371/journal.pbio.0050116). ATP hydrolysis ~8×10⁻²⁰ J: **~10–50 pW per Drosophila photoreceptor**; ~4800 R1–6 cells → **order 10² nW for the retina**, a large fraction of the whole CNS budget. Downstream LMCs are ~10³–10⁴× cheaper per cell than photoreceptors (Laughlin 1998).
- Implication: the fly spends visual energy at the **sensor**; computation after that is cheap analog. A camera+CNN spends it on ADC, buses, and dense matmul.

**Artificial compound eyes / insect robots (silicon):**

| System | Specs | Power | URL |
| --- | --- | --- | --- |
| CurvACE (Floreano / EPFL LIS, 2013) | 630 ommatidia, 180°×60° FOV, 1.75 g, 1950 fps, local adaptation | **0.9 W max** | https://www.pnas.org/doi/10.1073/pnas.1219068110 ; https://www.epfl.ch/labs/lis/research/completed/curvace/ |
| Franceschini Robot-fly (1992) | 118 pixels / 116 analog EMDs, 11 kg, pole avoidance | analog, no published mW | https://royalsocietypublishing.org/doi/10.1098/rstb.1992.0106 |
| Zhou et al. pinhole compound eye (HKUST, Science Robotics 2024) | 140° / binocular 220° FOV, perovskite nanowire, drone tracking | not reported in abstracts | https://doi.org/10.1126/scirobotics.adi8666 |
| Fibre ACE (Light Sci Appl 2024) | 271 fibres, 180° FOV, 31.3 kHz | not reported | https://doi.org/10.1038/s41377-024-01580-5 |
| Spherical ACE (Nature Communications 2026) | 294° FOV, **self-powered** event pixels, 8 ns response | 0 V bias (sensor) | https://www.nature.com/articles/s41467-026-73745-2 |
| de Croon et al. Loihi drone (Sci Robotics 2024) | 5-layer SNN, 28,800 neurons, event camera, 200 Hz | **0.94 W idle + 7–12 mW** for the net | https://doi.org/10.1126/scirobotics.adi0591 |
| NanoFlowNet (tiny CNN baseline) | 170,881 params, GAP8, Crazyflie 34 g, 5.5–9.3 FPS | GAP8 optical-flow class **~25 mW @ 50 MHz** (related RISC-V paper, not NanoFlowNet’s own joules) | https://doi.org/10.1109/icra48891.2023.10161258 |
| Adaptive-SpikeNet vs ANN | event optical flow | **~10×** energy vs similar-size ANN (analytical) | https://www.nature.com/articles/s44172-025-00492-5 |

**Gap:** there is **no apples-to-apples milliwatt paper** that runs the MAOL/flyvis graph vs NanoFlowNet on the same MCU for the same collision task. Closest silicon numbers are CurvACE (0.9 W sensor), Loihi (7–12 mW net), GAP8 CNNs (tens of mW). Biology is **10⁵–10⁸×** below those, and **does not transfer** to CPU emulation.

### Labs

- **HHMI Janelia FlyEM / Reiser / Rubin / Turaga:** MAOL, Nern inventory, flyvis, split-GAL4, optic-lobe neuPrint.
- **Princeton / Seung / Murthy FlyWire Consortium:** FAFB female brain + Matsliah OL parts list; Codex.
- **Janelia / Columbia Card lab:** loom, giant fiber, LC activation → behavior (Wu et al. eLife 2016).
- **MPI / Borst lab:** T4/T5, LPi, LPTCs, motion opponency.
- **Columbia Behnia + Abbott:** R7/R8 hue, recurrence.
- **UCLA Frye:** figure-ground LC9/10/12.
- **Yale Clark / Janelia Strother:** ON motion, C2/C3.
- **Cambridge Laughlin / Niven:** photoreceptor joules.
- **EPFL Floreano LIS:** CurvACE.
- **Aix-Marseille Franceschini / Serres / Ruffier:** analog EMD robots.
- **TU Delft de Croon:** neuromorphic / NanoFlowNet drones.
- **HKUST Fan:** 2024 pinhole compound eye.
- **Google Research Connectomics:** FIB-SEM / segmentation (MaleCNS, MAOL).

## Fact vs interpretation

- Fact: two complete adult optic-lobe connectomes exist (female FlyWire 2024; male MAOL 2025) plus a connectome-constrained 734-parameter optic-flow net that matches T4/T5 physiology.
- Fact: identified cells implement HR-like motion, radial-opponency loom, recurrent hue, and figure-ground, and compress to a few thousand VPN channels.
- Fact: living visual energy is nanowatts (photoreceptor-dominated); published compound-eye cameras are 0.9 W class; tiny CNNs on GAP8 are tens of milliwatts.
- Interpretation: the optic lobe is a **better recipe for a front-end** (EMD + loom geometry + VPN bottleneck + compound-eye sampling) than it is a drop-in replacement for MobileNet.
- HOLD: no published joule-matched “MAOL vs TinyML CNN” collision benchmark. CurvACE watts are the sensor, not the fly algorithm.

## Links

- [[literature/lit-20260912-biology-vs-silicon-energy]]
- [[literature/lit-20260912-shiu-huang-malecns-physiology]]
- [[permanent/perm-20260912-emulation-inverts-biological-efficiency]]
- [[permanent/perm-20260912-fly-snn-is-sensorimotor-worker-not-svlm]]
- [[domains/neuroscience]]
