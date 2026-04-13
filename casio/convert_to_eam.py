#!/usr/bin/env python3
"""Convert TXT formula files to .eam files for eAct Maker (planet-casio.com).

Open the .eam file in https://tools.planet-casio.com/EactMaker/
then click the format dropdown and export as G1E.
Transfer the .g1e to calculator via USB.
"""

import os
import sys
from pathlib import Path

SCRIPT_DIR = Path(__file__).parent

FILES = {
    "MEKANIK": "Mekanik",
    "VAGOR": "Vagor & Optik",
    "ELMAGN": "El & Magnetism",
    "TERMO": "Termofysik",
    "MODERN": "Modern Fysik",
    "KONST": "Konstanter",
}


def txt_to_eam(txt_path: Path, title: str, output_path: Path):
    content = txt_path.read_text(encoding="utf-8")
    eam_data = f"g1e\x1e{title}\x1e\x1e{content}"
    output_path.write_text(eam_data, encoding="utf-8")
    print(f"  {output_path.name} ({len(content)} chars)")


def main():
    out_dir = SCRIPT_DIR / "eam"
    out_dir.mkdir(exist_ok=True)

    print("Converting TXT -> EAM:")
    for basename, title in FILES.items():
        txt_path = SCRIPT_DIR / f"{basename}.txt"
        if not txt_path.exists():
            print(f"  SKIP {basename}.txt (not found)")
            continue
        eam_path = out_dir / f"{basename}.g1e.eam"
        txt_to_eam(txt_path, title, eam_path)

    print(f"\nDone. EAM files in: {out_dir}")
    print("\nNext steps:")
    print("1. Open https://tools.planet-casio.com/EactMaker/")
    print("2. Click 'Load', select a .eam file")
    print("3. Set format to 'G1E'")
    print("4. Click 'Save' to download the .g1e")
    print("5. Transfer .g1e to calculator via USB")


if __name__ == "__main__":
    main()
