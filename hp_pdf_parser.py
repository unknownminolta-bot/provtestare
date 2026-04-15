"""Import and parse Hogskoleprovet PDFs from studera.nu."""

from __future__ import annotations

import json
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Any
from urllib.parse import urljoin

import fitz  # pymupdf
import requests

BASE = "https://www.studera.nu"
FPN_BASE = "https://www.studera.nu/hogskoleprov/fpn/"
DATA_DIR = Path(__file__).with_name("data")
PDF_DIR = DATA_DIR / "hp_pdfs"
DTK_DIR = Path(__file__).with_name("static") / "hp" / "dtk" / "imported"
OUT_JSON = DATA_DIR / "hp_imported_questions.json"

SECTIONS = ("xyz", "kva", "nog", "dtk", "ord", "las", "mek", "elf")
CHOICE_RE = re.compile(r"^\s*([A-E])(?:[\)\.\-:]?\s*(.*))\s*$")
QUESTION_RE = re.compile(r"^\s*(\d{1,2})[\.\)]\s+(.+)\s*$")


@dataclass
class ParsedItem:
    id: str
    section: str
    exam_date: str
    provpass: int
    question: str
    choices: list[str]
    correct_answer: str
    passage_id: str | None = None
    diagram_id: str | None = None
    diagram_path: str | None = None
    solution: str = ""
    difficulty: str = "medium"
    points: int = 1

    def to_dict(self) -> dict[str, Any]:
        return self.__dict__.copy()


def _slug_year_season(year: int, season: str) -> str:
    return f"{year}-{season}"


def _candidate_exam_pages(year: int, season: str) -> list[str]:
    # studera.nu naming differs by year; try several known patterns.
    key = f"{year}-{season}"
    return [
        f"{FPN_BASE}provfragor-och-facit-{ 'varen' if season == 'vt' else 'hosten' }-{year}/",
        f"{FPN_BASE}provfragor-facit-och-normering-{ 'varen' if season == 'vt' else 'hosten' }-{year}/",
        f"{FPN_BASE}facit-provfragor-och-normering-{ 'varen' if season == 'vt' else 'hosten' }-{year}/",
        # Some pages use explicit dates:
        f"{FPN_BASE}provfragor-och-facit-{ 'varen' if season == 'vt' else 'hosten' }-{year}-12-mars/" if key == "2022-vt" else "",
    ]


def _fetch(url: str, timeout: int = 30) -> str:
    r = requests.get(url, timeout=timeout)
    if r.status_code >= 400:
        raise RuntimeError(f"HTTP {r.status_code} for {url}")
    return r.text


def _extract_pdf_links(html: str) -> list[str]:
    links = re.findall(r'href="([^"]+\.pdf)"', html, flags=re.IGNORECASE)
    out: list[str] = []
    for href in links:
        if href.startswith("http"):
            out.append(href)
        else:
            out.append(urljoin(BASE, href))
    # de-duplicate while preserving order
    dedup: list[str] = []
    seen: set[str] = set()
    for link in out:
        if link in seen:
            continue
        seen.add(link)
        dedup.append(link)
    return dedup


def discover_exam_pdfs(year: int, season: str) -> list[str]:
    pages = [p for p in _candidate_exam_pages(year, season) if p]
    for page in pages:
        try:
            html = _fetch(page)
            pdfs = _extract_pdf_links(html)
            if pdfs:
                return pdfs
        except Exception:
            continue
    # Fallback: crawl the historical index page and find matching exam pages.
    try:
        hist_html = _fetch("https://www.studera.nu/hogskoleprov/om/forbereda/tidigare/")
        page_links = re.findall(r'href="([^"]+/fpn/[^"]+)"', hist_html, flags=re.IGNORECASE)
        season_word = "varen" if season == "vt" else "hosten"
        for rel in page_links:
            full = rel if rel.startswith("http") else urljoin(BASE, rel)
            low = full.lower()
            if str(year) not in low or season_word not in low:
                continue
            try:
                html = _fetch(full)
                pdfs = _extract_pdf_links(html)
                if pdfs:
                    return pdfs
            except Exception:
                continue
    except Exception:
        pass
    return []


def _ensure_dirs() -> None:
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    PDF_DIR.mkdir(parents=True, exist_ok=True)
    DTK_DIR.mkdir(parents=True, exist_ok=True)


def _download_pdf(url: str, dst: Path) -> Path:
    if dst.exists() and dst.stat().st_size > 0:
        return dst
    r = requests.get(url, timeout=60)
    r.raise_for_status()
    dst.write_bytes(r.content)
    return dst


def _pdf_text(doc: fitz.Document) -> str:
    parts: list[str] = []
    for page in doc:
        parts.append(page.get_text("text"))
    return "\n".join(parts)


def _detect_section(pdf_name: str, text: str) -> str:
    n = pdf_name.lower()
    if "kvant" in n:
        # Mixed quantitative pass, section inferred per question keyword in parser.
        return "quant-mixed"
    if "verb" in n:
        return "verbal-mixed"
    for sec in SECTIONS:
        if sec in n or re.search(rf"\b{sec.upper()}\b", text):
            return sec
    return "unknown"


def _infer_section_from_question(text: str) -> str:
    t = text.lower()
    if "kvantitet i" in t and "kvantitet ii" in t:
        return "kva"
    if "(1)" in t and "(2)" in t and "tillracklig information" in t:
        return "nog"
    if any(token in t for token in ("diagram", "tabell", "karta")):
        return "dtk"
    if "välj det alternativ som ligger närmast betydelsen" in t or "synonym" in t:
        return "ord"
    return "xyz"


def _section_from_index(sec_hint: str, qnum: int) -> str:
    if sec_hint == "quant-mixed":
        if 1 <= qnum <= 12:
            return "xyz"
        if 13 <= qnum <= 22:
            return "kva"
        if 23 <= qnum <= 28:
            return "nog"
        return "dtk"
    if sec_hint == "verbal-mixed":
        # Common order in verbal: ORD, LAS, MEK, ELF. Some PDFs omit ELF.
        if 1 <= qnum <= 10:
            return "ord"
        if 11 <= qnum <= 20:
            return "ord"
        if 21 <= qnum <= 30:
            return "las"
        if 31 <= qnum <= 40:
            return "mek"
        return "elf"
    return sec_hint


def _split_question_blocks(text: str) -> list[tuple[int, str]]:
    lines = [ln.rstrip() for ln in text.splitlines() if ln.strip()]
    blocks: list[tuple[int, str]] = []
    cur_num: int | None = None
    cur_lines: list[str] = []
    for ln in lines:
        m = QUESTION_RE.match(ln)
        if m:
            if cur_num is not None:
                blocks.append((cur_num, "\n".join(cur_lines)))
            cur_num = int(m.group(1))
            cur_lines = [m.group(2).strip()]
        elif cur_num is not None:
            cur_lines.append(ln.strip())
    if cur_num is not None:
        blocks.append((cur_num, "\n".join(cur_lines)))
    return blocks


def _extract_choices(block: str) -> tuple[str, list[str]]:
    lines = block.splitlines()
    stem_lines: list[str] = []
    choices: list[str] = []
    collecting_choices = False
    for ln in lines:
        cm = CHOICE_RE.match(ln)
        if cm and (collecting_choices or len(ln.strip()) <= 6 or ln.strip().startswith(tuple("ABCDE"))):
            collecting_choices = True
            option_text = cm.group(2).strip()
            choices.append(f"{cm.group(1)}) {option_text}".rstrip())
        elif collecting_choices and choices and ln.strip():
            # Continue multiline choice text for latest choice
            if QUESTION_RE.match(ln):
                break
            choices[-1] = (choices[-1] + " " + ln.strip()).strip()
        else:
            stem_lines.append(ln)
    # Drop empty choice placeholders like "A)".
    choices = [c for c in choices if len(c.strip()) > 2]
    stem = " ".join(stem_lines).strip()
    return stem, choices


def _extract_dtk_images(doc: fitz.Document, exam_slug: str, provpass: int) -> list[str]:
    image_ids: list[str] = []
    max_images = 20
    for idx, page in enumerate(doc):
        if len(image_ids) >= max_images:
            break
        imgs = page.get_images(full=True)
        for j, img in enumerate(imgs):
            if len(image_ids) >= max_images:
                break
            try:
                xref = img[0]
                pix = fitz.Pixmap(doc, xref)
                out_name = f"{exam_slug}_pp{provpass}_p{idx+1}_{j+1}.png"
                out_path = DTK_DIR / out_name
                if pix.colorspace is None:
                    continue
                if pix.alpha or pix.colorspace.n not in (1, 3):
                    pix = fitz.Pixmap(fitz.csRGB, pix)
                # Heuristic: ignore tiny glyph sprites/icons; keep likely chart assets.
                if pix.width < 300 or pix.height < 180:
                    continue
                pix.save(out_path)
                image_ids.append(str(out_path.relative_to(Path(__file__).with_name("static"))))
            except Exception:
                continue
    return image_ids


def _parse_pdf_questions(
    pdf_path: Path,
    exam_slug: str,
    provpass: int,
    answer_key: dict[int, str] | None = None,
) -> list[dict[str, Any]]:
    answer_key = answer_key or {}
    with fitz.open(pdf_path) as doc:
        text = _pdf_text(doc)
        sec_hint = _detect_section(pdf_path.name, text)
        blocks = _split_question_blocks(text)
        dtk_images = _extract_dtk_images(doc, exam_slug, provpass) if sec_hint in {"dtk", "quant-mixed"} else []

    out: list[dict[str, Any]] = []
    img_cursor = 0
    for qnum, block in blocks:
        stem, choices = _extract_choices(block)
        if len(choices) < 4:
            continue
        section = _section_from_index(sec_hint, qnum)
        if section in {"unknown", "quant-mixed", "verbal-mixed"}:
            section = _infer_section_from_question(stem)
            if section == "xyz" and sec_hint == "verbal-mixed":
                section = "mek"
        correct = answer_key.get(qnum, "")
        qid = f"hp_{exam_slug}_{section}_{qnum:02d}"
        item = ParsedItem(
            id=qid,
            section=section,
            exam_date=exam_slug,
            provpass=provpass,
            question=stem,
            choices=choices[:5],
            correct_answer=correct or "A",
        )
        if section == "dtk" and dtk_images:
            item.diagram_id = f"{qid}_diagram"
            if img_cursor < len(dtk_images):
                item.diagram_path = dtk_images[img_cursor]
                img_cursor += 1
        out.append(item.to_dict())
    return out


def _parse_answer_key_from_text(text: str) -> dict[int, str]:
    # Simple parser for rows like "1 A 2 C 3 D ..."
    pairs = re.findall(r"(\d{1,2})\s*([A-E])", text)
    out: dict[int, str] = {}
    for qn, ans in pairs:
        qni = int(qn)
        if 1 <= qni <= 80:
            out[qni] = ans
    return out


def _parse_answer_key_pdf(pdf_path: Path) -> dict[int, str]:
    try:
        with fitz.open(pdf_path) as doc:
            text = _pdf_text(doc)
        return _parse_answer_key_from_text(text)
    except Exception:
        return {}


def _guess_provpass_from_name(name: str) -> int:
    m = re.search(r"provpass[-_ ]?(\d)", name.lower())
    if m:
        return int(m.group(1))
    return 2


def import_all_exams(years: list[int] | None = None) -> dict[str, Any]:
    _ensure_dirs()
    if years is None:
        years = list(range(2013, 2026))

    imported: list[dict[str, Any]] = []
    discovered_pages = 0
    downloaded_pdfs = 0
    failures: list[str] = []

    for year in years:
        for season in ("vt", "ht"):
            exam_slug = _slug_year_season(year, season)
            pdf_links = discover_exam_pdfs(year, season)
            if not pdf_links:
                failures.append(f"{exam_slug}: no pdf links discovered")
                continue
            discovered_pages += 1

            answer_keys: dict[int, str] = {}
            question_pdfs: list[Path] = []
            for url in pdf_links:
                name = url.split("/")[-1]
                local = PDF_DIR / f"{exam_slug}_{name}"
                try:
                    _download_pdf(url, local)
                    downloaded_pdfs += 1
                except Exception as exc:
                    failures.append(f"{exam_slug}: download fail {url} ({exc})")
                    continue
                lower = name.lower()
                if "facit" in lower:
                    answer_keys.update(_parse_answer_key_pdf(local))
                elif "provpass" in lower:
                    question_pdfs.append(local)

            for qpdf in question_pdfs:
                try:
                    provpass = _guess_provpass_from_name(qpdf.name)
                    parsed = _parse_pdf_questions(qpdf, exam_slug, provpass, answer_keys)
                    imported.extend(parsed)
                except Exception as exc:
                    failures.append(f"{exam_slug}: parse fail {qpdf.name} ({exc})")

    # Deduplicate by id and keep first occurrence.
    unique: dict[str, dict[str, Any]] = {}
    for q in imported:
        qid = str(q.get("id", ""))
        if qid and qid not in unique:
            unique[qid] = q

    OUT_JSON.write_text(json.dumps(list(unique.values()), ensure_ascii=False, indent=2), encoding="utf-8")
    return {
        "status": "ok",
        "years": years,
        "discovered_exam_pages": discovered_pages,
        "downloaded_pdfs": downloaded_pdfs,
        "imported_questions": len(unique),
        "output": str(OUT_JSON),
        "failures": failures[:200],
    }

