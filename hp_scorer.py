"""Scoring for Hogskoleprovet practice modes."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from questions_hp import HP_SECTIONS

QUANT_SECTIONS = ("xyz", "kva", "nog", "dtk")
VERBAL_SECTIONS = ("ord", "las", "mek", "elf")

# Canonical normering anchor points (raw -> normalized score).
# These are used for interpolation and then adjusted per exam season.
_CANONICAL_NORM_ANCHORS = {
    0: 0.00,
    8: 0.20,
    16: 0.40,
    24: 0.60,
    32: 0.80,
    40: 1.00,
    48: 1.20,
    56: 1.40,
    64: 1.60,
    72: 1.80,
    80: 2.00,
}


def _interp_norm(raw_score: int, anchors: dict[int, float]) -> float:
    raw_score = max(0, min(80, int(raw_score)))
    if raw_score in anchors:
        return anchors[raw_score]

    lower = max(k for k in anchors if k < raw_score)
    upper = min(k for k in anchors if k > raw_score)
    lower_v = anchors[lower]
    upper_v = anchors[upper]
    ratio = (raw_score - lower) / (upper - lower)
    return lower_v + (upper_v - lower_v) * ratio


def _build_exam_adjustment(year: int, season: str) -> float:
    # Small deterministic seasonal/year variation to mimic historical normering drift.
    season_bias = 0.015 if season == "ht" else -0.005
    year_bias = ((year - 2013) % 5 - 2) * 0.005
    return season_bias + year_bias


def _build_historical_tables() -> dict[str, dict[str, dict[int, float]]]:
    tables: dict[str, dict[str, dict[int, float]]] = {}
    for year in range(2013, 2026):
        for season in ("vt", "ht"):
            key = f"{year}-{season}"
            adjust = _build_exam_adjustment(year, season)
            quant = {k: min(2.0, max(0.0, v + adjust)) for k, v in _CANONICAL_NORM_ANCHORS.items()}
            verbal = {k: min(2.0, max(0.0, v + adjust * 0.8)) for k, v in _CANONICAL_NORM_ANCHORS.items()}
            tables[key] = {"quant": quant, "verbal": verbal}
    return tables


HP_NORMERING_TABLES = _build_historical_tables()
HP_NORMERING_DEFAULT = "2025-ht"


def _safe_answer(value: Any) -> str:
    if value is None:
        return ""
    return str(value).strip()


def _is_correct(question: dict[str, Any], user_answer: str) -> bool:
    correct = _safe_answer(question.get("correct_answer"))
    user = _safe_answer(user_answer)
    if not correct or not user:
        return False
    # HP uses fixed alternatives; first character matching is practical and robust.
    return correct[:1].casefold() == user[:1].casefold()


@dataclass
class HpScoreResult:
    per_question: list[dict[str, Any]]
    per_section: dict[str, dict[str, Any]]
    quant_raw: int
    verbal_raw: int
    quant_norm: float
    verbal_norm: float
    final_norm: float
    percentile_estimate: float
    total_questions: int
    total_correct: int

    def to_dict(self) -> dict[str, Any]:
        return {
            "per_question": self.per_question,
            "per_section": self.per_section,
            "quant_raw": self.quant_raw,
            "verbal_raw": self.verbal_raw,
            "quant_norm": self.quant_norm,
            "verbal_norm": self.verbal_norm,
            "final_norm": self.final_norm,
            "percentile_estimate": self.percentile_estimate,
            "total_questions": self.total_questions,
            "total_correct": self.total_correct,
        }


def estimate_percentile(score_0_2: float) -> float:
    # Lightweight monotonic mapping for UX feedback.
    s = max(0.0, min(2.0, score_0_2))
    if s <= 0.5:
        return 5 + s * 30
    if s <= 1.0:
        return 20 + (s - 0.5) * 80
    if s <= 1.5:
        return 60 + (s - 1.0) * 60
    return 90 + (s - 1.5) * 20


def score_hp(
    questions: list[dict[str, Any]],
    user_answers: dict[str, Any],
    *,
    normering_key: str | None = None,
) -> dict[str, Any]:
    normering_key = normering_key or HP_NORMERING_DEFAULT
    table = HP_NORMERING_TABLES.get(normering_key, HP_NORMERING_TABLES[HP_NORMERING_DEFAULT])

    per_section: dict[str, dict[str, Any]] = {
        section: {
            "display": HP_SECTIONS[section]["display"],
            "name": HP_SECTIONS[section]["name"],
            "domain": HP_SECTIONS[section]["domain"],
            "correct": 0,
            "total": 0,
        }
        for section in HP_SECTIONS
    }
    per_question: list[dict[str, Any]] = []
    total_correct = 0

    for q in questions:
        qid = str(q.get("id", ""))
        section = str(q.get("section", "")).lower()
        if section not in per_section:
            continue
        user_answer = _safe_answer(user_answers.get(qid, ""))
        ok = _is_correct(q, user_answer)

        per_section[section]["total"] += 1
        if ok:
            per_section[section]["correct"] += 1
            total_correct += 1

        per_question.append(
            {
                "id": qid,
                "section": section,
                "correct": ok,
                "user_answer": user_answer,
                "correct_answer": _safe_answer(q.get("correct_answer")),
                "solution": q.get("solution", ""),
            }
        )

    quant_raw = sum(per_section[s]["correct"] for s in QUANT_SECTIONS)
    verbal_raw = sum(per_section[s]["correct"] for s in VERBAL_SECTIONS)
    quant_norm = round(_interp_norm(quant_raw, table["quant"]), 2)
    verbal_norm = round(_interp_norm(verbal_raw, table["verbal"]), 2)
    final_norm = round((quant_norm + verbal_norm) / 2, 2)
    percentile_estimate = round(estimate_percentile(final_norm), 1)

    result = HpScoreResult(
        per_question=per_question,
        per_section=per_section,
        quant_raw=quant_raw,
        verbal_raw=verbal_raw,
        quant_norm=quant_norm,
        verbal_norm=verbal_norm,
        final_norm=final_norm,
        percentile_estimate=percentile_estimate,
        total_questions=len(questions),
        total_correct=total_correct,
    )
    return result.to_dict()
