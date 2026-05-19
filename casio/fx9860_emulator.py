#!/usr/bin/env python3
"""fx-9860GIII text-mode emulator for Python-mode scripts.

The fx-9860GIII LCD is 128x64 px. Python print/input text mode uses a
fixed 6x8 px mini-font, so one screen is 21 columns x 8 rows. This emulator
captures every exported page from formler_calc.py, simulates EXE prompts, and
fails if any logical screen exceeds 21x8 or contains non-ASCII characters.
"""

from __future__ import annotations

import argparse
import builtins
import io
import sys
import textwrap
from contextlib import redirect_stdout
from dataclasses import dataclass, field
from pathlib import Path
from typing import Callable, Iterable, Sequence

SCRIPT_DIR = Path(__file__).parent
SCREEN_COLS = 21
SCREEN_ROWS = 8


@dataclass
class Page:
    label: str
    body: str
    overflow: list[str] = field(default_factory=list)
    bad_chars: set[str] = field(default_factory=set)


def split_into_lines(text: str) -> list[str]:
    out: list[str] = []
    for raw in text.splitlines():
        if raw == "":
            out.append("")
            continue
        if len(raw) <= SCREEN_COLS:
            out.append(raw)
            continue
        out.extend(textwrap.wrap(raw, width=SCREEN_COLS, drop_whitespace=False) or [""])
    return out


def logical_screens(body: str) -> list[list[str]]:
    screens: list[list[str]] = []
    current: list[str] = []
    for raw in body.splitlines():
        current.extend(split_into_lines(raw))
        if "[EXE]" in raw:
            screens.append(current)
            current = []
    if current:
        screens.append(current)
    return screens or [[]]


def diagnose(label: str, body: str) -> Page:
    overflow: list[str] = []
    for idx, screen in enumerate(logical_screens(body), start=1):
        if len(screen) > SCREEN_ROWS:
            overflow.append(f"screen {idx}: {len(screen)} rows")
        overflow.extend(ln for ln in screen if len(ln) > SCREEN_COLS)
    bad = {c for c in body if not c.isspace() and (ord(c) < 0x20 or ord(c) > 0x7E)}
    return Page(label=label, body=body, overflow=overflow, bad_chars=bad)


def frame(lines: Sequence[str]) -> str:
    border = "+" + "-" * SCREEN_COLS + "+"
    rows = list(lines[:SCREEN_ROWS])
    while len(rows) < SCREEN_ROWS:
        rows.append("")
    body = "\n".join("|" + (row[:SCREEN_COLS]).ljust(SCREEN_COLS) + "|" for row in rows)
    return border + "\n" + body + "\n" + border


def render_page(page: Page) -> str:
    screens = logical_screens(page.body)
    out = [f"== {page.label} =="]
    out.append(frame(screens[0] if screens else []))
    if len(screens) > 1:
        out.append(f"  note: {len(screens)} skarmar/promptar")
    if page.overflow:
        out.append("  OVERFLOW:")
        for ln in page.overflow:
            out.append(f"    {ln!r}")
    if page.bad_chars:
        chars = ", ".join(f"{c!r}=U+{ord(c):04X}" for c in sorted(page.bad_chars))
        out.append(f"  NON-ASCII: {chars}")
    return "\n".join(out)


def capture_pages(pages: Iterable[Callable[[], None] | tuple[str, str]]) -> list[Page]:
    rendered: list[Page] = []
    for entry in pages:
        if isinstance(entry, tuple):
            label, body = entry
        else:
            buf = io.StringIO()
            old_input = builtins.input
            def fake_input(prompt: str = "") -> str:
                if prompt:
                    print(prompt)
                raise EOFError
            try:
                builtins.input = fake_input
                with redirect_stdout(buf):
                    entry()
            finally:
                builtins.input = old_input
            label = getattr(entry, "__name__", "page")
            body = buf.getvalue()
        rendered.append(diagnose(label, body))
    return rendered


def emulate_module(module_path: Path) -> int:
    sys.path.insert(0, str(module_path.parent))
    name = module_path.stem
    if name in sys.modules:
        del sys.modules[name]
    module = __import__(name)
    pages_fn = getattr(module, "all_pages", None)
    if pages_fn is None:
        print(f"{module_path}: missing all_pages()")
        return 1
    pages = capture_pages(pages_fn())
    failures = 0
    for page in pages:
        print(render_page(page))
        print()
        if page.overflow or page.bad_chars:
            failures += 1
    print(f"\nResultat: {failures}/{len(pages)} sidor med fel")
    return 0 if failures == 0 else 2


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "module",
        nargs="?",
        default=str(SCRIPT_DIR / "formler_calc.py"),
        help="Path to calculator-side Python module that exports all_pages().",
    )
    args = parser.parse_args(argv)
    return emulate_module(Path(args.module))


if __name__ == "__main__":
    raise SystemExit(main())
