#!/usr/bin/env bash
set -euo pipefail

root="${1:-$HOME/src/latency-wave4}"
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

clone https://github.com/frameprobe/frameprobe.git frameprobe
clone https://github.com/OSRTT/OSLTT.git OSLTT
clone https://github.com/Nixola/VRRTest.git VRRTest
clone https://github.com/netborg-afps/dxvk-low-latency.git dxvk-low-latency
clone https://gitlab.freedesktop.org/emersion/drm_info.git drm_info
clone https://gitlab.freedesktop.org/emersion/libdisplay-info.git libdisplay-info

echo "prepared under $root"
