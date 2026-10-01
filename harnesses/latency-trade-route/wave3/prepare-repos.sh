#!/usr/bin/env bash
set -euo pipefail

root="${1:-$HOME/src/latency-wave3}"
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

clone https://github.com/libsdl-org/SDL.git SDL
clone https://github.com/godotengine/godot.git godot
clone https://github.com/hyprwm/Hyprland.git Hyprland
clone https://github.com/hyprwm/aquamarine.git aquamarine
clone https://github.com/flightlessmango/MangoHud.git MangoHud
clone https://github.com/torvalds/linux.git linux
clone https://github.com/glfw/glfw.git glfw

echo "prepared under $root"
