#!/usr/bin/env bash
# Copy the fx-9860GIII Python runtime to a Casio USB volume, verify hashes, unmount.
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

py_files=(
  "${SCRIPT_DIR}/formler.py"
  "${SCRIPT_DIR}/formmain.py"
  "${SCRIPT_DIR}/form_ui.py"
  "${SCRIPT_DIR}/form_mek.py"
  "${SCRIPT_DIR}/form_vag.py"
  "${SCRIPT_DIR}/form_el.py"
  "${SCRIPT_DIR}/form_ter.py"
  "${SCRIPT_DIR}/form_mod.py"
  "${SCRIPT_DIR}/form_kon.py"
  "${SCRIPT_DIR}/formkemi.py"
)
for f in "${py_files[@]}"; do
  if [[ ! -f "$f" ]]; then
    echo "Missing calculator runtime file: $f" >&2
    exit 1
  fi
done

MP=""
DEV=""
if command -v blkid >/dev/null 2>&1; then
  mapfile -t casio_devs < <(
    {
      blkid -o device -t LABEL_FATBOOT=CASIO 2>/dev/null || true
      blkid -o device -t LABEL=CASIO 2>/dev/null || true
    } | awk 'NF && !seen[$0]++'
  )
  if [[ ${#casio_devs[@]} -gt 1 ]]; then
    echo "Multiple CASIO-labelled devices found; refusing to guess:" >&2
    printf '  %s\n' "${casio_devs[@]}" >&2
    exit 1
  elif [[ ${#casio_devs[@]} -eq 1 ]]; then
    DEV="${casio_devs[0]}"
  fi
fi
if [[ -z "$DEV" ]] && command -v lsblk >/dev/null 2>&1; then
  mapfile -t calc_devs < <(
    lsblk --pairs --paths --output NAME,PKNAME,FSTYPE,RM,MODEL 2>/dev/null | awk '
      function field(key, re, v) {
        re = key "=\"[^\"]*\""
        if (match($0, re)) {
          v = substr($0, RSTART + length(key) + 2, RLENGTH - length(key) - 3)
          return v
        }
        return ""
      }
      {
        name = field("NAME")
        pkname = field("PKNAME")
        fstype = field("FSTYPE")
        rm = field("RM")
        model = field("MODEL")
        names[++n] = name
        pknames[n] = pkname
        fstypes[n] = fstype
        rms[n] = rm
        models[name] = model
      }
      END {
        for (i = 1; i <= n; i++) {
          parent = pknames[i] ? pknames[i] : names[i]
          if (fstypes[i] == "vfat" && rms[i] == "1" && models[parent] ~ /Calculator/) {
            print names[i]
          }
        }
      }
    '
  )
  if [[ ${#calc_devs[@]} -gt 1 ]]; then
    echo "Multiple removable calculator vfat partitions found; refusing to guess:" >&2
    printf '  %s\n' "${calc_devs[@]}" >&2
    exit 1
  elif [[ ${#calc_devs[@]} -eq 1 ]]; then
    DEV="${calc_devs[0]}"
  fi
fi

if [[ -n "$DEV" ]] && command -v findmnt >/dev/null 2>&1; then
  MP="$(findmnt -n -o TARGET "$DEV" 2>/dev/null || true)"
  if [[ -z "$MP" ]] && command -v udisksctl >/dev/null 2>&1; then
    echo "Mounting $DEV..."
    udisksctl mount -b "$DEV"
    MP="$(findmnt -n -o TARGET "$DEV" 2>/dev/null || true)"
  fi
fi
if [[ -z "$MP" ]]; then
  for cand in /media/*/*/ /run/media/*/*/; do
    if [[ -d "$cand" ]] && findmnt "$cand" >/dev/null 2>&1; then
      srcdev="$(findmnt -rn -o SOURCE -T "$cand" 2>/dev/null || true)"
      if [[ -n "$srcdev" ]]; then
        fat="$(blkid -o value -s LABEL_FATBOOT "$srcdev" 2>/dev/null | tr -d '\n')"
        lab="$(blkid -o value -s LABEL "$srcdev" 2>/dev/null | tr -d '\n')"
        if [[ "$fat" == "CASIO" || "$lab" == "CASIO" ]]; then
          DEV="$srcdev"
          MP="${cand%/}"
          break
        fi
      fi
    fi
  done
fi

if [[ -z "$MP" || ! -d "$MP" ]]; then
  echo "No CASIO USB volume found. Put the calculator in USB/storage mode, then retry." >&2
  if command -v lsblk >/dev/null 2>&1; then
    lsblk -rpo NAME,LABEL,FSTYPE,RM,MOUNTPOINTS,MODEL >&2
  fi
  exit 1
fi

opts="$(findmnt -n -o OPTIONS -T "$MP" 2>/dev/null || true)"
if [[ ",$opts," != *,rw,* ]]; then
  echo "CASIO volume is not mounted read-write: $MP ($opts)" >&2
  exit 1
fi

echo "Target: $MP"
cp -v "${py_files[@]}" "$MP"/
sync

for f in "${py_files[@]}"; do
  b=$(basename "$f")
  echo "--- $b"
  src_hash="$(sha256sum "$f" | awk '{print $1}')"
  dst_hash="$(sha256sum "$MP/$b" | awk '{print $1}')"
  if [[ "$src_hash" != "$dst_hash" ]]; then
    echo "Hash mismatch for $b" >&2
    exit 1
  fi
  echo "$src_hash  $b"
done
sync

if [[ -n "${DEV:-}" ]] && command -v udisksctl >/dev/null 2>&1; then
  udisksctl unmount -b "$DEV" && echo "Unmounted $DEV"
elif [[ "$(id -u)" -eq 0 ]] && [[ -n "${DEV:-}" ]]; then
  umount "$MP" && echo "Unmounted $MP"
else
  echo "Unmount manually if needed: $MP (device was ${DEV:-unknown})." >&2
fi
