#!/usr/bin/env python3
r"""Normalize Eact Maker letter subscripts to Unicode Latin subscript letters.

Policy (strict pass):
  - Keep numeric subscripts: \\subs0;, \\subs1;, ... (\\subs + digits + ;)
  - \\subs; alone (no digit) means subscript letter s -> \\u209b (e.g. W = F\\subs;s)
  - \\sub<lowercase letters>; -> one Unicode subscript char per letter when ALL are
    supported (a,e,h,i,j,k,l,m,n,o,p,r,s,t,u,v,x). Otherwise keep the full token.
  - \\sub<...>; uppercase letters are converted "where possible" by mapping to their
    lowercase subscript equivalent (A->ₐ, N->ₙ, etc). Unsupported uppercase letters
    keep the full token.
  - Lowercase letters b,c,d,f,g,q,w,y,z: no standard Latin subscript -> keep token.

Usage:
  python normalize_eam_subscripts.py              # lint tokens on stdin
  python normalize_eam_subscripts.py --lint FILE
  python normalize_eam_subscripts.py --apply FILE   # rewrite FILE in place

Semantic notation audits such as banned `\submi;` patterns and merged trig
tokens live in `formula_audit.py`.
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

# LATIN SUBSCRIPT SMALL LETTER * (and modifier letters where Unicode assigns them)
LOWER_SUB = {
    "a": "\u2090",
    "e": "\u2091",
    "o": "\u2092",
    "x": "\u2093",
    "h": "\u2095",
    "k": "\u2096",
    "l": "\u2097",
    "m": "\u2098",
    "n": "\u2099",
    "p": "\u209a",
    "s": "\u209b",
    "t": "\u209c",
    "i": "\u1d62",
    "r": "\u1d63",
    "u": "\u1d64",
    "v": "\u1d65",
    "j": "\u2c7c",
}

UNSUPPORTED_LOWER = frozenset("bcdfgqwyz")
# Convert uppercase to lowercase where a Latin subscript lowercase glyph exists.
UPPER_TO_LOWER = {
    "A": "a",
    "E": "e",
    "H": "h",
    "I": "i",
    "J": "j",
    "K": "k",
    "L": "l",
    "M": "m",
    "N": "n",
    "O": "o",
    "P": "p",
    "R": "r",
    "S": "s",
    "T": "t",
    "U": "u",
    "V": "v",
    "X": "x",
}

# \\subs0;, \\subs12; — digits only after "subs"
RE_SUBS_NUM = re.compile(r"\\subs\d+;")
# \\submi;, \\subs; (same as \\sub + "s" + ";") — letters only before ;
RE_SUB_LETTERS = re.compile(r"\\sub([A-Za-z]+);")

# Unicode subscript digits U+2080..U+2089 (fx-9860GIII shows raw \\subs1; / \\subn; if not converted)
_SUB_DIGITS = "₀₁₂₃₄₅₆₇₈₉"
RE_SUBS_DIGITS_ONLY = re.compile(r"\\subs(\d+);")

# g1e: Latin subscript Unicode letters are often dropped on the device; use ASCII "_tag" instead.
RE_UNDERSCORE_BEFORE_FRAC = re.compile(r"(_[a-z]+)(\\frac)")
RE_AMBIGUOUS_AFTER_S_SUB = re.compile(r"([a-zA-Z])_s([a-zA-Z])")


def _replace_sub_letters(m: re.Match[str]) -> str:
    body = m.group(1)
    mapped: list[str] = []
    for c in body:
        if c.isupper():
            lc = UPPER_TO_LOWER.get(c)
            if lc is None:
                return m.group(0)
            mapped.append(lc)
            continue
        if c in UNSUPPORTED_LOWER:
            return m.group(0)
        mapped.append(c)
    return "".join(LOWER_SUB[c] for c in mapped)


def _replace_subs_digits(m: re.Match[str]) -> str:
    return "".join(_SUB_DIGITS[int(d)] for d in m.group(1))


def _ascii_sub_body(body: str) -> str:
    out: list[str] = []
    for c in body:
        if c.isupper():
            out.append(UPPER_TO_LOWER.get(c, c.lower()))
        else:
            out.append(c)
    return "".join(out)


def _replace_sub_letters_ascii(m: re.Match[str]) -> str:
    return "_" + _ascii_sub_body(m.group(1))


def normalize_eam_text(text: str) -> str:
    # \\subs<digits>; is never matched: after \\sub the [A-Za-z]+ cannot include digits.
    return RE_SUB_LETTERS.sub(_replace_sub_letters, text)


def normalize_calculator_export(text: str) -> str:
    """Normalize Eact markup for fx-9860GIII .g1e (raw \\sub...; shows literally; Unicode Latin
    subscript letters are often invisible; use Unicode subscript digits + ASCII _tag for letters).

    Order: \\subs<digits>; -> ₀₉, then \\sub<letters>; -> _letters (ASCII), then spacing fixes.
    """
    out = RE_SUBS_DIGITS_ONLY.sub(_replace_subs_digits, text)
    out = RE_SUB_LETTERS.sub(_replace_sub_letters_ascii, out)
    out = RE_AMBIGUOUS_AFTER_S_SUB.sub(r"\1_s \2", out)
    out = RE_UNDERSCORE_BEFORE_FRAC.sub(r"\1 \2", out)
    return out


def lint(text: str) -> list[str]:
    issues: list[str] = []
    for m in RE_SUB_LETTERS.finditer(text):
        tok = m.group(0)
        body = m.group(1)
        upper_bad = [c for c in body if c.isupper() and c not in UPPER_TO_LOWER]
        lower_bad = [c for c in body if c.islower() and c in UNSUPPORTED_LOWER]
        if upper_bad or lower_bad:
            issues.append(
                f"kept (unsupported upper={upper_bad!r}, lower={lower_bad!r}): {tok}"
            )
    return issues


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--lint", metavar="FILE", help="list bare \\subs; and kept letter tokens")
    ap.add_argument("--apply", metavar="FILE", help="normalize file in place")
    args = ap.parse_args()

    if args.lint:
        p = Path(args.lint)
        t = p.read_text(encoding="utf-8")
        for line in lint(t):
            print(line)
        return

    if args.apply:
        p = Path(args.apply)
        t = p.read_text(encoding="utf-8")
        n = normalize_eam_text(t)
        if n != t:
            p.write_text(n, encoding="utf-8")
            print(f"Updated {p}")
        else:
            print(f"No changes {p}")
        return

    data = sys.stdin.read()
    print(normalize_eam_text(data), end="")


if __name__ == "__main__":
    main()
