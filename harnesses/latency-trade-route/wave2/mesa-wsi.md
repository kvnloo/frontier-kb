# Mesa WSI — present timing validation

## Why now

Mesa 26.1/26.2 materially expanded `VK_EXT_present_timing` support, including Wayland and X11/XWayland paths. The 26.2 work also includes fixes around clock domains, causal present timing, VRR/FRR detection and adaptive sleep pullback.

This is a new measurement surface worth validating independently.

## Goal

Determine whether application-visible timing can be used as a trustworthy display timestamp for the wider latency lab.

## Matrix

On hardware/backends available later:

- Wayland
- X11
- XWayland
- fixed refresh
- VRR
- FIFO / FIFO-relaxed / latest-ready where supported
- Mesa 26.1 vs 26.2/current

## Per-frame record

- requested target time
- returned time domain
- GPU-done timestamp
- queue-done timestamp if exposed
- actual present timestamp
- earliest present timestamp
- refresh estimate
- present ID

Cross-correlate with:

- DRM vblank/pageflip tracepoints
- compositor presentation feedback
- an external photodiode/high-speed-camera measurement if available

## Invariants

A timing result is useful only if:

- it is causal;
- frame IDs do not alias;
- the clock domain is documented/correlatable;
- fixed-refresh intervals cluster at integer refresh periods;
- VRR intervals track actual flips rather than nominal mode refresh.

## Output

Produce a backend trust table:

| backend | actual present | queue done | clock domain | dropped-frame signal | external error |
| --- | --- | --- | --- | --- | --- |

This table becomes shared infrastructure for DXVK, vkd3d-proton, wgpu and LatencyFleX experiments.
