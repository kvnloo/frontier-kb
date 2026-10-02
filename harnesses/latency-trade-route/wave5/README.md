# E2E latency trade route — wave 5

Status: **triaged and staged, not executed**

Wave 5 adds the human/perceptual layer:

```text
photon
 -> retinal/visual integration
 -> target perception
 -> decision
 -> motor response
```

This wave does **not** assume lower software latency always improves performance.

## Lanes

1. RetroArch — runahead / frame delay / BFI as a temporal-rendering laboratory
2. PsychoPy — calibrated human-response and motion-clarity tasks
3. Frame generation — rendered-vs-generated frame freshness and queue growth
4. Eye tracking / foveation — gaze age at shading and at photon
5. Photon ↔ human metric contract — speed/accuracy and motion-clarity tradeoffs

## Core outcomes

Report separately:

- physical input-to-photon
- photon t10 / t50 / t90
- response-time distribution
- accuracy/error rate
- motion-discrimination threshold
- gaze age
- frame-generation queue age

Do not collapse these into one score.

## Safety

High-contrast flicker/BFI/strobe experiments can be uncomfortable and may be unsafe for people with photosensitive seizure risk. Keep netplay/BFI tests out of this wave, begin with non-flicker baselines, and stop any visual test if symptoms occur.

## Promotion

None. This wave builds experimental evidence only.
