# DXVK low-latency — external validation

Reference implementation:
https://github.com/netborg-afps/dxvk-low-latency

This fork documents a VRR low-latency mode using `VK_EXT_present_timing`.

## Question

Does timing-aware pacing reduce **input-to-photon**, or only produce nicer present intervals?

## Compare

- upstream DXVK baseline
- upstream current present-timing work
- dxvk-low-latency default
- dxvk-low-latency VRR mode
- `VK_NV_low_latency2` path where applicable

## Workload

Use one deterministic D3D11 scene where a synthetic mouse movement produces a large luminance change under the photodiode.

## Capture

- physical HID event time
- application frame ID
- input sample time if exposed
- DXVK frame begin
- queue submit
- target present time
- actual present time
- DRM first-pixel time
- photon time

## Score

Primary:

```text
input_to_photon p50/p95/p99
```

Secondary:

- missed deadlines
- cadence error
- GPU utilization
- FPS

A pacing method wins only if it improves photon-age without an unacceptable miss-rate increase.
