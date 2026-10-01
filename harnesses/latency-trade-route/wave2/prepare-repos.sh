#!/usr/bin/env bash
set -euo pipefail

root="${1:-$HOME/src/latency-wave2}"
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

clone https://github.com/gfx-rs/wgpu.git wgpu
clone https://github.com/HansKristian-Work/vkd3d-proton.git vkd3d-proton
clone https://github.com/alvr-org/ALVR.git ALVR
clone https://gitlab.freedesktop.org/mesa/mesa.git mesa
clone https://gitlab.freedesktop.org/monado/monado.git monado

echo "prepared under $root"
