#!/usr/bin/env bash
set -euo pipefail

root="${1:-$HOME/src/latency-wave5}"
mkdir -p "$root"

clone() {
  local url="$1"
  local dir="$2"
  if [[ -d "$root/$dir/.git" ]]; then
    git -C "$root/$dir" fetch --all --prune
  else
    git clone --filter=blob:none "$url" "$root/$dir"
  fi
}

clone https://github.com/libretro/RetroArch.git RetroArch
clone https://github.com/psychopy/psychopy.git psychopy
clone https://github.com/EyeTrackVR/EyeTrackVR.git EyeTrackVR
clone https://github.com/pupil-labs/pupil.git pupil
clone https://github.com/optiscaler/OptiScaler.git OptiScaler
clone https://github.com/NVIDIA-RTX/Streamline.git Streamline
clone https://github.com/GPUOpen-LibrariesAndSDKs/FidelityFX-SDK.git FidelityFX-SDK

echo "prepared under $root"
