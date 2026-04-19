#!/usr/bin/env python3
"""Audit calculator formula sources and EAM output for known bad patterns."""

from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass
from pathlib import Path

from normalize_eam_subscripts import lint as lint_subscripts


@dataclass(frozen=True)
class Issue:
    category: str
    line_no: int
    message: str
    line: str


SOURCE_PATTERNS: tuple[tuple[str, re.Pattern[str], str], ...] = (
    (
        "legacy-transition-index",
        re.compile(r"\bE[nN][12]\b"),
        "Use explicit level notation like `E(n1)`/`E(n2)` instead of chained `En1` tokens.",
    ),
    (
        "legacy-half-life",
        re.compile(r"\bT_(?:half|h)\b"),
        "Use one canonical half-life name in source text, e.g. `T_halv`.",
    ),
    (
        "legacy-half-thickness",
        re.compile(r"\bd_(?:half|h)\b"),
        "Use one canonical half-thickness name in source text, e.g. `d_halv`.",
    ),
    (
        "legacy-schwarzschild",
        re.compile(r"\br_?Sch\b|\brSch\b"),
        "Prefer the shorter canonical source name `r_S` for Schwarzschild radius.",
    ),
    (
        "legacy-refraction-angle",
        re.compile(r"\bab\b|\bvb\b|\bag\b"),
        "Use `ar`/`vr` for refraction and `ak` for critical angle to match the render-safe convention.",
    ),
    (
        "legacy-medel",
        re.compile(r"\bv_medel\b"),
        "Use the shorter canonical source name `v_m`.",
    ),
)

EAM_PATTERNS: tuple[tuple[str, re.Pattern[str], str], ...] = (
    (
        "ambiguous-subscript",
        re.compile(r"\\submi;"),
        "Ambiguous `\\submi;` token detected. Use an explicit render-safe semantic subscript such as `\\subm;`, `\\submax;`, `\\submin;`, `\\subhal;`, `\\subrms;`, or `\\subres;`.",
    ),
    (
        "compound-level-index",
        re.compile(r"E\\subn;\\subs\d+;"),
        "Compound level indices should not be emitted as chained subscripts. Use an explicit form such as `E(n\\subs1;)`.",
    ),
    (
        "merged-trig-token",
        re.compile(r"(?<!\\)([A-Za-z])(?:sin|cos|tan)\("),
        "Merged function token detected. Insert explicit multiplication before trig functions.",
    ),
)


def audit_text(text: str, scope: str) -> list[Issue]:
    issues: list[Issue] = []
    patterns = SOURCE_PATTERNS if scope == "source" else EAM_PATTERNS
    for line_no, line in enumerate(text.splitlines(), start=1):
        for category, pattern, message in patterns:
            if pattern.search(line):
                issues.append(Issue(category, line_no, message, line))

    if scope == "eam":
        for line_no, line in enumerate(text.splitlines(), start=1):
            for problem in lint_subscripts(line):
                issues.append(Issue("unsupported-subscript", line_no, problem, line))

    return issues


def detect_scope(path: Path) -> str:
    if path.suffix == ".txt":
        return "source"
    return "eam"


def iter_repo_files(root: Path) -> list[Path]:
    candidates: list[Path] = []
    for pattern in ("*.txt", "*.eam"):
        candidates.extend(root.rglob(pattern))
    for name in ("FORMLER.py", "generate_eam_g2e.py"):
        candidate = root / name
        if candidate.exists():
            candidates.append(candidate)
    filtered: list[Path] = []
    for path in sorted(set(candidates)):
        parts = set(path.parts)
        if "__pycache__" in parts or "backups" in parts:
            continue
        if "eam" in parts:
            continue
        if path.name.startswith("test_"):
            continue
        filtered.append(path)
    return filtered


def audit_path(path: Path) -> list[Issue]:
    scope = detect_scope(path)
    text = path.read_text(encoding="utf-8")
    return audit_text(text, scope)


def main(argv: list[str] | None = None) -> int:
    argv = argv or sys.argv
    parser = argparse.ArgumentParser()
    parser.add_argument("paths", nargs="*", help="Files or directories to audit")
    parser.add_argument(
        "--tree",
        metavar="DIR",
        help="Audit the calculator repo tree for known formula issues.",
    )
    args = parser.parse_args(argv[1:])

    paths: list[Path] = [Path(p) for p in args.paths]
    if args.tree:
        paths.extend(iter_repo_files(Path(args.tree)))
    if not paths:
        print("No input paths.")
        return 1

    exit_code = 0
    for path in paths:
        path = path.expanduser()
        if path.is_dir():
            for child in iter_repo_files(path):
                issues = audit_path(child)
                for issue in issues:
                    print(
                        f"{child}:{issue.line_no}: [{issue.category}] {issue.message}\n"
                        f"  {issue.line}"
                    )
                if issues:
                    exit_code = 1
            continue

        issues = audit_path(path)
        for issue in issues:
            print(
                f"{path}:{issue.line_no}: [{issue.category}] {issue.message}\n"
                f"  {issue.line}"
            )
        if issues:
            exit_code = 1

    if exit_code == 0:
        print("OK")
    return exit_code


if __name__ == "__main__":
    raise SystemExit(main())
