#!/usr/bin/env python3
"""Capture KEXF01 quiz screenshots via browser-bridge bb.py (same stack as MCP)."""

from __future__ import annotations

import json
import re
import subprocess
import time
from datetime import datetime, timezone
from pathlib import Path

BB = (
    "/home/maxandersson/browser-bridge/.venv/bin/python3",
    "/home/maxandersson/browser-bridge/bb.py",
)
OUT_DIR = Path("/home/maxandersson/exam-tester/artifacts/live-captures/kexf01")
SEARCH_TERMS = [
    "a) ",
    "b) ",
    "c) ",
    "d) ",
    "Beräkna",
    "Bestäm",
    "Vilket",
    "Hur ",
    "Förklara",
    "Skriv",
    "Visa",
    "Tabellen",
    "figuren",
    "Givet",
    "En lösning",
    "Vid jämvikt",
    "koncentrationen",
    "lösningen",
    "reaktion",
    "jämvikt",
    "elektronegativitet",
    "bindning",
    "atom",
    "gasen",
    "trycket",
    "temperaturen",
]


def bb(*args: str, timeout: float = 120) -> str:
    r = subprocess.run(
        [BB[0], BB[1], *args],
        capture_output=True,
        text=True,
        timeout=timeout,
    )
    return ((r.stdout or "") + (r.stderr or "")).strip()


def extract_qtext_from_search_output(output: str) -> str:
    for line in output.splitlines():
        m = re.match(r"\s*\d+\.\s+\[div#q-text\.question-text\]\s*(.*)$", line)
        if m:
            return m.group(1).strip()
    return ""


def read_question_text(tab: str) -> str:
    for term in SEARCH_TERMS:
        out = bb("search", tab, term, timeout=60)
        text = extract_qtext_from_search_output(out)
        if text:
            return text
    return ""


def read_counter(tab: str, expected: int) -> str:
    out = bb("search", tab, f"{expected} / 30", timeout=60)
    m = re.search(rf"({expected}\s*/\s*30)", out)
    return m.group(1) if m else ""


def click_skip(tab: str) -> None:
    bb("click", tab, "--text", "Hoppa över", timeout=30)


def main() -> int:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    for p in OUT_DIR.glob("q*.png"):
        p.unlink(missing_ok=True)
    (OUT_DIR / "results.png").unlink(missing_ok=True)
    (OUT_DIR / "manifest.json").unlink(missing_ok=True)

    run_id = str(int(time.time()))
    tab = f"mcp_run={run_id}"
    url = f"https://provtestare.onrender.com/?{tab}"

    warnings: list[str] = []
    questions: list[dict] = []

    bb("go", url, timeout=120)
    time.sleep(35)

    start_out = bb("click", tab, "--text", "KEXF01 — Kemi 1", timeout=30)
    if "ERROR" in start_out or "TimeoutError" in start_out:
        warnings.append(f"start: KEXF01 card click failed: {start_out[:500]}")
        print(json.dumps({"captured": 0, "warnings": warnings}, ensure_ascii=False, indent=2))
        return 1

    time.sleep(1.0)

    prev_qtext = ""
    for order in range(1, 31):
        time.sleep(0.55)
        counter_ok = read_counter(tab, order)
        if not counter_ok:
            warnings.append(f"q{order:02d}: expected counter {order} / 30 not found in page search")

        path = OUT_DIR / f"q{order:02d}.png"
        try:
            bb("screenshot", tab, "--output", str(path), timeout=60)
            if not (path.exists() and path.stat().st_size > 400):
                warnings.append(f"q{order:02d}: screenshot missing or very small")
        except Exception as e:
            warnings.append(f"q{order:02d}: screenshot error: {e}")

        qtext = read_question_text(tab)
        if not qtext:
            warnings.append(f"q{order:02d}: question text not extracted")
            qtext = ""
        if prev_qtext and qtext == prev_qtext:
            warnings.append(f"q{order:02d}: question text unchanged vs previous (possible stuck UI)")

        preview = qtext.replace("\n", " ").strip()[:80]
        questions.append(
            {
                "order": order,
                "filename": path.name,
                "question_text_preview": preview or "(empty)",
            }
        )

        click_skip(tab)
        time.sleep(0.85)
        if order < 30:
            nqt = read_question_text(tab)
            if nqt == qtext:
                warnings.append(f"q{order:02d}: question unchanged after skip; clicking skip again")
                click_skip(tab)
                time.sleep(0.75)
        prev_qtext = qtext

    results_path = OUT_DIR / "results.png"
    time.sleep(0.8)
    try:
        bb("screenshot", tab, "--output", str(results_path), timeout=60)
        if not (results_path.exists() and results_path.stat().st_size > 400):
            warnings.append("results.png: missing or very small")
    except Exception as e:
        warnings.append(f"results screenshot: {e}")

    q_shots = sum(
        1
        for i in range(1, 31)
        if (OUT_DIR / f"q{i:02d}.png").exists()
        and (OUT_DIR / f"q{i:02d}.png").stat().st_size > 400
    )
    res_ok = results_path.exists() and results_path.stat().st_size > 400
    total_disk = q_shots + (1 if res_ok else 0)

    manifest = {
        "run_timestamp": datetime.now(timezone.utc).isoformat(),
        "subject": "kexf01",
        "total_captured": total_disk,
        "questions": questions,
    }
    (OUT_DIR / "manifest.json").write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    print(
        json.dumps(
            {"captured": total_disk, "question_pngs": q_shots, "warnings": warnings},
            ensure_ascii=False,
            indent=2,
        ),
        flush=True,
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
