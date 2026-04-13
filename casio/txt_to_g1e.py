#!/usr/bin/env python3
"""Convert TXT formula files to Casio fx-9860GIII .g2e eActivity files.

Format reverse-engineered from a working FYS.g2e file on the calculator.
"""

import struct
import sys
from pathlib import Path


def _pad4(data: bytes) -> bytes:
    r = len(data) % 4
    return data + b"\x00" * ((4 - r) % 4)


def _invert(data: bytes) -> bytes:
    return bytes(~b & 0xFF for b in data)


def build_text_line(text: str) -> bytes:
    raw = _pad4(text.encode("ascii", errors="replace"))
    return struct.pack(">BxH", 0x81, len(raw)) + raw


def build_heading_line(text: str) -> bytes:
    raw = _pad4(text.encode("ascii", errors="replace"))
    return struct.pack(">BxH", 0x07, len(raw)) + raw


def build_g2e(title: str, lines_data: list[bytes]) -> bytes:
    line_count = len(lines_data)
    all_lines = b"".join(lines_data)

    content_header = bytearray(8)
    content_header[0:8] = struct.pack(">II", 0, len(all_lines) + 8 + 16 + 12)

    eact_tag = b"@EACT\x00\x00\x00"
    name_raw = title.encode("ascii", errors="replace")[:8].ljust(8, b"\x00")

    sub_header = bytearray(16)
    sub_header[0:3] = b"\x00\x00\x00"
    sub_header[3] = 0x01
    sub_header[4:8] = struct.pack(">I", len(all_lines) + 16 + 12)
    sub_header[8:16] = name_raw

    line_index = bytearray(12)
    line_index[0:4] = struct.pack(">I", 4 + len(all_lines))
    line_index[4:8] = struct.pack(">I", len(all_lines))
    line_index[8] = 0xD4
    line_index[9] = 0x00
    line_index[10:12] = struct.pack(">H", line_count)

    content = eact_tag + sub_header + line_index + all_lines

    setup = bytearray(0x48)
    total_content_size = len(content)
    struct.pack_into(">I", setup, 0x00, 0)
    struct.pack_into(">I", setup, 0x04, total_content_size + 0x48)

    setup[0x08] = 0x00
    setup[0x09] = 0x01
    setup[0x0A] = 0x02
    setup[0x0B] = 0x00
    setup[0x0C] = 0x03
    setup[0x0D] = 0x60
    setup[0x0E] = 0x02
    setup[0x0F] = 0x00

    setup[0x16] = 0x14
    setup[0x17] = 0x2A
    setup[0x18] = 0x3F
    setup[0x19] = 0x02
    setup[0x1A] = 0xC0

    setup[0x1E] = 0x28
    setup[0x1F] = 0x30

    setup[0x24] = 0x01
    setup[0x25] = 0x02
    setup[0x26] = 0x01
    setup[0x27] = 0x01
    setup[0x28] = 0x01
    setup[0x29] = 0x03
    setup[0x2A] = 0x01
    setup[0x2B] = 0x01
    for i in range(0x2C, 0x36):
        setup[i] = 0x01

    body = bytes(setup) + content
    total_size = 0x20 + len(body)

    struct.pack_into(">I", setup, 0x00, total_size)
    body = bytes(setup) + content
    total_size = 0x20 + len(body)

    header = bytearray(0x20)
    header[0:8] = b"USBPower"
    header[8] = 0x49
    header[9:14] = b"\x00\x10\x00\x10\x00"
    lsb = total_size & 0xFF
    header[14] = (lsb + 0x41) & 0xFF
    header[15] = 0x01
    struct.pack_into(">I", header, 0x10, total_size)
    header[0x14] = (lsb + 0xB8) & 0xFF
    header[0x1E] = 0xFF
    header[0x1F] = 0xFF

    return _invert(bytes(header)) + body


def txt_to_g2e(txt_path: Path, title: str) -> bytes:
    text = txt_path.read_text(encoding="utf-8")
    lines = []
    for line in text.split("\n"):
        line = line.rstrip()
        if not line:
            continue
        if line.startswith("===") or (line.startswith("--- ") and line.endswith(" ---")):
            lines.append(build_heading_line(line))
        else:
            lines.append(build_text_line(line))
    return build_g2e(title, lines)


FILES = {
    "MEKANIK": "MEKANIK",
    "VAGOR": "VAGOR",
    "ELMAGN": "ELMAGN",
    "TERMO": "TERMO",
    "MODERN": "MODERN",
    "KONST": "KONST",
}


def main():
    script_dir = Path(__file__).parent
    out_dir = script_dir / "g1e"
    out_dir.mkdir(exist_ok=True)

    calc_dir = Path("/media/maxandersson/disk")
    calc_connected = calc_dir.exists() and (calc_dir / "FYS.g2e").exists()

    print("Converting TXT -> G2E (v2):")
    for basename, title in FILES.items():
        txt_path = script_dir / f"{basename}.txt"
        if not txt_path.exists():
            print(f"  SKIP {basename}.txt")
            continue
        data = txt_to_g2e(txt_path, title)
        local_path = out_dir / f"{basename}.g2e"
        local_path.write_bytes(data)
        print(f"  {local_path.name} ({len(data)} bytes)")

        if calc_connected:
            (calc_dir / f"{basename}.g2e").write_bytes(data)
            print(f"    -> copied to calculator")

    if calc_connected:
        print("\nFiles on calculator. Safely eject, then open e-ACT.")
    else:
        print("\nCalculator not detected. Copy .g2e files manually.")


if __name__ == "__main__":
    main()
