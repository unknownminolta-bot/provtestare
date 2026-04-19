#!/usr/bin/env python3
"""Regression checks for formula audit and generator conventions."""

from pathlib import Path

from formula_audit import audit_text
from generate_eam_g2e import SECTIONS, build_eam, parse_formats
from normalize_eam_subscripts import normalize_calculator_export


ROOT = Path(__file__).parent


def assert_no_issues(label: str, text: str, scope: str) -> None:
    issues = audit_text(text, scope)
    assert not issues, f"{label} unexpectedly failed audit: {issues}"


def main() -> None:
    # Legacy patterns should be caught.
    assert audit_text("E = |En1 - En2|", "source")
    assert audit_text("lambda = ln2/T_half", "source")
    assert audit_text(r"E = |E\subn;\subs1; - E\subn;\subs2;|", "eam")
    assert audit_text(r"n\lambda; = dsin(\alpha;\subn;)", "eam")
    assert audit_text(r"\lambda;\submi; = \frac{hc}{eU}", "eam")

    # Generated sections should be clean.
    for name, section in SECTIONS.items():
        assert_no_issues(name, section["content"], "eam")

    # Source text should also be free of the known legacy patterns.
    for name in ("MEKANIK", "VAGOR", "ELMAGN", "TERMO", "MODERN", "KONST"):
        text = (ROOT / f"{name}.txt").read_text(encoding="utf-8")
        assert_no_issues(f"{name}.txt", text, "source")

    modern = SECTIONS["MODERN"]["content"]
    assert r"\lambda;\submax;T = a" in modern
    assert r"T\subhal;" in modern
    assert r"E = |E(n\subs1;) \minus; E(n\subs2;)|" in modern
    assert r"\lambda;\submin; = \frac{hc}{eU}" in modern
    assert r"r\subs; = \frac{2Gm}{c^{2}}" in modern

    vagor = SECTIONS["VAGOR"]["content"]
    assert r"d\times;sin(\alpha;\subn;)" in vagor
    assert r"n\submax; = \frac{d}{\lambda;}" in vagor
    assert r"sin(\alpha;\subk;)" in vagor

    mekanik = SECTIONS["MEKANIK"]["content"]
    assert r"F\subres; = ma" in mekanik
    assert r"\eta; = \frac{E\subn;}{E\subt;} = \frac{P\subn;}{P\subt;}" in mekanik

    elmagn = SECTIONS["ELMAGN"]["content"]
    assert r"\Sigma;I\subi; = \Sigma;I\subu;" in elmagn
    assert r"u = u\submax;sin(\omega;t)" in elmagn

    assert build_eam("TEST", "body", "g1e").startswith("g1e\x1e")
    # g1e path must not leave raw Eact subscript tokens (device shows them verbatim).
    g1e_body = build_eam("T", r"v\subs0; = \Sigma;I\subi;", "g1e").split("\x1e", 3)[3]
    assert "\\sub" not in g1e_body and "\\subs" not in g1e_body
    assert "₀" in g1e_body and "_i" in g1e_body
    assert "\\sub" not in normalize_calculator_export(r"\epsilon;\subs0;\epsilon;\subr;A")
    assert "₀" in normalize_calculator_export(r"\epsilon;\subs0;\epsilon;\subr;A")
    assert "_r" in normalize_calculator_export(r"\epsilon;\subs0;\epsilon;\subr;A")
    assert parse_formats("both") == ["g2e", "g1e"]
    assert parse_formats("g2e,g1e") == ["g2e", "g1e"]

    # Edge (agent 8): Doppler — ASCII subscripts + space before \frac
    dop = r"f\subo; = f\subk;\frac{v+v\subo;}{v\minus;v\subk;}"
    dop_out = normalize_calculator_export(dop)
    assert "\\sub" not in dop_out
    assert "f_o" in dop_out and "f_k" in dop_out and "v_o" in dop_out and "v_k" in dop_out
    assert r"f_k \frac" in dop_out

    # Edge: F\subs;s (subscript s) + distance s → F_s s
    w_line = normalize_calculator_export(r"W = F\subs;s")
    assert "F_s s" in w_line
    assert "\\sub" not in w_line

    # Multi-char subscript
    assert "_res" in normalize_calculator_export(r"F\subres; = ma")
    assert "_max" in normalize_calculator_export(r"n\submax; = x")


if __name__ == "__main__":
    main()
