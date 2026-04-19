#!/usr/bin/env bash
# Copy g1e_fixed/*.g1e to a mounted Casio USB volume (vfat LABEL=CASIO), verify hashes, unmount.
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SRC="${SCRIPT_DIR}/g1e_fixed"

if [[ ! -d "$SRC" ]]; then
  echo "Missing ${SRC}" >&2
  exit 1
fi

shopt -s nullglob
g1e=( "${SRC}"/*.g1e )
if [[ ${#g1e[@]} -eq 0 ]]; then
  echo "No .g1e files in ${SRC}. Run: python3 generate_eam_g2e.py --convert --formats both" >&2
  exit 1
fi

MP=""
if command -v findmnt >/dev/null 2>&1; then
  MP="$(findmnt -rn -o TARGET -L CASIO 2>/dev/null | head -1 || true)"
fi
if [[ -z "$MP" ]]; then
  for cand in /media/*/*/ /run/media/*/*/; do
    if [[ -d "$cand" ]] && findmnt "$cand" >/dev/null 2>&1; then
      srcdev="$(findmnt -rn -o SOURCE -T "$cand" 2>/dev/null || true)"
      if [[ -n "$srcdev" ]] && lsblk -o LABEL -nr "$srcdev" 2>/dev/null | grep -qx CASIO; then
        MP="$cand"
        break
      fi
    fi
  done
fi

if [[ -z "$MP" || ! -d "$MP" ]]; then
  echo "No mounted volume with LABEL=CASIO. Plug in the calculator USB, mount the storage partition, then retry." >&2
  echo "Tip: sudo mount /dev/sdX1 /run/media/\$USER/CASIO" >&2
  exit 1
fi

echo "Target: $MP"
cp -v "${SRC}"/*.g1e "$MP"/
sync

for f in "${SRC}"/*.g1e; do
  b=$(basename "$f")
  echo "--- $b"
  sha256sum "$f" "$MP/$b"
done

if [[ "$(id -u)" -eq 0 ]]; then
  umount "$MP" && echo "Unmounted $MP"
else
  echo "Run: sudo umount $(printf '%q' "$MP")"
fi
