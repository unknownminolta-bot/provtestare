"""Gemini-backed HP practice question generator."""

from __future__ import annotations

import json
import os
from typing import Any

from questions_hp import KVA_FIXED_CHOICES, NOG_FIXED_CHOICES, HP_SECTIONS


def _section_prompt(section: str) -> str:
    section = section.lower().strip()
    base = (
        "Du skapar frågor i svensk högskoleprovsstil.\n"
        "Krav:\n"
        "- Svara ENDAST med JSON-array.\n"
        "- Varje objekt ska innehålla: question, choices, correct_answer, solution, difficulty.\n"
        "- correct_answer ska vara en bokstav (A-E).\n"
        "- choices ska redan vara formaterade som 'A) ...', 'B) ...' osv.\n"
        "- difficulty: easy, medium, hard.\n"
        "- Undvik identiska distraktorer.\n"
    )
    if section == "xyz":
        return base + "Skapa matematiska problemlösningsfrågor (XYZ), 4 alternativ (A-D)."
    if section == "kva":
        return (
            base
            + "Skapa KVA-frågor med två kvantiteter. Inkludera kvantitet I/II i question-texten. "
            "Alternativen måste vara exakt KVA-standard."
        )
    if section == "nog":
        return (
            base
            + "Skapa NOG-frågor med en huvudfråga och två påståenden (1) och (2). "
            "Alternativen måste vara exakt NOG-standard."
        )
    if section == "dtk":
        return base + "Skapa DTK-frågor med tabell/diagrambeskrivning i text (utan bild), 4 alternativ (A-D)."
    if section == "ord":
        return base + "Skapa ORD-frågor (ordförståelse), 5 alternativ (A-E)."
    if section == "las":
        return base + "Skapa LAS-frågor med kort svensk passage i question-texten och 4 alternativ."
    if section == "mek":
        return base + "Skapa MEK-frågor (meningskomplettering), 4 alternativ (A-D)."
    if section == "elf":
        return base + "Skapa ELF-frågor med kort engelsk passage i question-texten och 4 alternativ."
    raise ValueError(f"Unsupported section: {section}")


def _fallback_question(section: str, idx: int) -> dict[str, Any]:
    # Conservative fallback when AI is unavailable or malformed.
    if section == "ord":
        return {
            "id": f"hp_generated_{section}_{idx:03d}",
            "section": section,
            "exam_date": "generated",
            "provpass": 2,
            "question": "Välj synonym till ordet: \"kortfattad\".",
            "choices": ["A) utförlig", "B) lakonisk", "C) osäker", "D) tydlig", "E) tillfällig"],
            "correct_answer": "B",
            "solution": "Lakonisk betyder kortfattad.",
            "difficulty": "easy",
            "points": 1,
        }
    if section == "kva":
        return {
            "id": f"hp_generated_{section}_{idx:03d}",
            "section": section,
            "exam_date": "generated",
            "provpass": 2,
            "question": "Kvantitet I: 3^2\nKvantitet II: 8",
            "choices": list(KVA_FIXED_CHOICES),
            "correct_answer": "A",
            "solution": "9 > 8.",
            "difficulty": "easy",
            "points": 1,
        }
    if section == "nog":
        return {
            "id": f"hp_generated_{section}_{idx:03d}",
            "section": section,
            "exam_date": "generated",
            "provpass": 2,
            "question": "Hur gammal är personen X?",
            "choices": list(NOG_FIXED_CHOICES),
            "correct_answer": "C",
            "solution": "Båda påståenden krävs.",
            "difficulty": "medium",
            "points": 1,
            "nog_statement_1": "X är 3 år äldre än Y.",
            "nog_statement_2": "Y är 20 år.",
        }
    return {
        "id": f"hp_generated_{section}_{idx:03d}",
        "section": section,
        "exam_date": "generated",
        "provpass": 2,
        "question": "Genererad övningsfråga.",
        "choices": ["A) Alternativ 1", "B) Alternativ 2", "C) Alternativ 3", "D) Alternativ 4"],
        "correct_answer": "A",
        "solution": "Förklaring saknas i fallback.",
        "difficulty": "easy",
        "points": 1,
    }


def _normalize_choices(section: str, choices: list[str]) -> list[str]:
    if section == "kva":
        return list(KVA_FIXED_CHOICES)
    if section == "nog":
        return list(NOG_FIXED_CHOICES)
    return choices


def generate_hp_questions(section: str, count: int = 10) -> list[dict[str, Any]]:
    section = (section or "").strip().lower()
    if section not in HP_SECTIONS:
        raise ValueError(f"Unsupported section: {section}")
    count = max(1, min(50, int(count)))

    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        return [_fallback_question(section, i + 1) for i in range(count)]

    prompt = _section_prompt(section)
    content = (
        f"Skapa {count} frågor för sektionen {section.upper()}.\n"
        "Returnera strikt JSON-array utan markdown."
    )
    try:
        from google import genai

        client = genai.Client(api_key=api_key)
        model_name = os.environ.get("GEMINI_MODEL", "gemini-2.5-flash")
        response = client.models.generate_content(model=model_name, contents=[prompt, content])
        text = response.text or "[]"
        text = text.strip()
        if text.startswith("```"):
            text = text.strip("`")
            text = text.replace("json", "", 1).strip()
        parsed = json.loads(text)
        if not isinstance(parsed, list):
            raise ValueError("Generator response is not a JSON array.")
    except Exception:
        return [_fallback_question(section, i + 1) for i in range(count)]

    output: list[dict[str, Any]] = []
    for idx, obj in enumerate(parsed[:count], start=1):
        if not isinstance(obj, dict):
            output.append(_fallback_question(section, idx))
            continue
        choices = obj.get("choices") or []
        if not isinstance(choices, list) or not choices:
            output.append(_fallback_question(section, idx))
            continue
        choices = [str(c) for c in choices]
        normalized = {
            "id": f"hp_generated_{section}_{idx:03d}",
            "section": section,
            "exam_date": "generated",
            "provpass": 2,
            "question": str(obj.get("question", "")).strip() or "Genererad övningsfråga.",
            "choices": _normalize_choices(section, choices),
            "correct_answer": str(obj.get("correct_answer", "A")).strip()[:1].upper() or "A",
            "solution": str(obj.get("solution", "")).strip(),
            "difficulty": str(obj.get("difficulty", "medium")).strip().lower(),
            "points": 1,
        }
        output.append(normalized)

    while len(output) < count:
        output.append(_fallback_question(section, len(output) + 1))
    return output
