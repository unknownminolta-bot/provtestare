"""
Scoring engine and diagnostic report generator for exam practice.
"""

from __future__ import annotations

import math
import re
from typing import Any


def _normalize_text(value: str) -> str:
    s = value.strip().lower()
    s = re.sub(r"\s+", " ", s)
    return s


def _parse_float(raw: str) -> float | None:
    if raw is None:
        return None
    s = str(raw).strip()
    if not s:
        return None
    try:
        return float(s)
    except ValueError:
        return None


def _question_points(question: dict[str, Any]) -> int:
    p = question.get("points")
    if p is None:
        return 1
    try:
        return int(p)
    except (TypeError, ValueError):
        return 1


def _check_numeric(user_raw: str, correct_raw: Any, tolerance: Any) -> bool:
    user_val = _parse_float(user_raw)
    if user_val is None:
        return False
    correct_val = _parse_float(str(correct_raw).strip()) if correct_raw is not None else None
    if correct_val is None:
        return False
    if math.isnan(user_val) or math.isnan(correct_val):
        return False
    try:
        tol = float(tolerance) if tolerance is not None else 0.0
    except (TypeError, ValueError):
        tol = 0.0
    if tol < 0:
        tol = 0.0
    ref = abs(correct_val)
    if ref < 1e-15:
        return abs(user_val - correct_val) <= tol
    return abs(user_val - correct_val) <= tol * ref


def _check_text(user_raw: str, correct_raw: Any) -> bool:
    u = _normalize_text(str(user_raw) if user_raw is not None else "")
    c = _normalize_text(str(correct_raw) if correct_raw is not None else "")
    return u == c


def _check_multiple_choice(user_raw: str, correct_raw: Any) -> bool:
    u = str(user_raw).strip().casefold() if user_raw is not None else ""
    c = str(correct_raw).strip().casefold() if correct_raw is not None else ""
    if not u or not c:
        return False
    return u[0] == c[0]


def _answer_correct(question: dict[str, Any], user_answer: str) -> bool:
    answer_type = (question.get("answer_type") or "text").strip().lower()
    correct = question.get("correct_answer")

    if answer_type == "numeric":
        return _check_numeric(user_answer, correct, question.get("tolerance"))
    if answer_type == "multiple_choice":
        return _check_multiple_choice(user_answer, correct)
    return _check_text(user_answer, correct)


def _question_id(q: dict[str, Any]) -> str:
    if "id" in q and q["id"] is not None:
        return str(q["id"])
    if "question_id" in q and q["question_id"] is not None:
        return str(q["question_id"])
    return ""


def score_answers(questions: list[dict], user_answers: dict) -> dict:
    """
    Score user answers against correct answers.

    Args:
        questions: list of question dicts (each has id, correct_answer, answer_type, tolerance, etc.)
        user_answers: dict mapping question_id -> user's answer string

    Returns dict with:
        - "total_correct": int
        - "total_questions": int
        - "total_points_earned": int
        - "total_points_possible": int
        - "per_question": list of dicts with {id, correct, user_answer, correct_answer, points, topic, topic_display}
    """
    per_question: list[dict[str, Any]] = []
    total_correct = 0
    total_points_earned = 0
    total_points_possible = 0

    for q in questions:
        qid = _question_id(q)
        max_pts = _question_points(q)
        total_points_possible += max_pts

        user_raw = user_answers.get(qid, "")
        if user_raw is None:
            user_raw = ""
        user_str = str(user_raw)

        ok = _answer_correct(q, user_str) if qid else False
        earned = max_pts if ok else 0
        if ok:
            total_correct += 1
        total_points_earned += earned

        topic = q.get("topic") or ""
        topic_display = q.get("topic_display")
        if topic_display is None or topic_display == "":
            topic_display = str(topic) if topic else ""

        per_question.append(
            {
                "id": qid,
                "correct": ok,
                "user_answer": user_str,
                "correct_answer": q.get("correct_answer"),
                "points": earned,
                "topic": str(topic),
                "topic_display": str(topic_display),
            }
        )

    return {
        "total_correct": total_correct,
        "total_questions": len(questions),
        "total_points_earned": total_points_earned,
        "total_points_possible": total_points_possible,
        "per_question": per_question,
    }


def _safe_percentage(earned: float, possible: float) -> float:
    if possible <= 0:
        return 0.0
    return round(100.0 * earned / possible, 2)


def _topic_status(pct: float) -> str:
    if pct >= 80.0:
        return "strong"
    if pct >= 50.0:
        return "review"
    return "weak"


def _exam_name(q: dict[str, Any]) -> str:
    for key in ("exam", "exam_name", "exam_title"):
        v = q.get(key)
        if v is not None and str(v).strip():
            return str(v).strip()
    return "Unknown"


def _exam_frequency(q: dict[str, Any]) -> float:
    raw = q.get("exam_frequency")
    if raw is None:
        return 0.0
    try:
        return float(raw)
    except (TypeError, ValueError):
        return 0.0


def generate_diagnostic(scored_results: dict, questions: list[dict]) -> dict:
    """
    Generate a diagnostic report from scored results.

    Returns dict with:
        - "exam_scores": dict mapping exam name -> {earned, possible, percentage}
        - "topic_scores": dict mapping topic -> {earned, possible, percentage, exam_frequency, status}
          where status is "strong" (>=80%), "review" (50-79%), or "weak" (<50%)
        - "critical_misses": list of topics with exam_frequency >= 0.8 and status "weak"
        - "readiness": dict mapping exam name -> percentage (weighted by exam_frequency)
        - "study_priorities": list of {topic, topic_display, exam, priority_score, reason}
          sorted by priority_score descending
          priority_score = exam_frequency * (1 - topic_percentage)
    """
    qmap = {_question_id(q): q for q in questions}

    exam_agg: dict[str, dict[str, float]] = {}
    readiness_num: dict[str, float] = {}
    readiness_den: dict[str, float] = {}

    topic_agg: dict[str, dict[str, float]] = {}
    topic_freq: dict[str, float] = {}
    topic_display_pick: dict[str, str] = {}
    topic_exam_weight: dict[str, dict[str, float]] = {}

    per_question = scored_results.get("per_question") or []

    for row in per_question:
        qid = row.get("id", "")
        q = qmap.get(qid, {})
        max_pts = _question_points(q)
        earned = float(row.get("points") or 0)
        exam = _exam_name(q)
        freq = _exam_frequency(q)
        topic = str(q.get("topic") or row.get("topic") or "unknown")

        ea = exam_agg.setdefault(exam, {"earned": 0.0, "possible": 0.0})
        ea["earned"] += earned
        ea["possible"] += float(max_pts)

        w = freq if freq > 0 else 1.0
        readiness_num[exam] = readiness_num.get(exam, 0.0) + earned * w
        readiness_den[exam] = readiness_den.get(exam, 0.0) + float(max_pts) * w

        td = q.get("topic_display") or row.get("topic_display") or topic
        topic_display_pick.setdefault(topic, str(td))

        ta = topic_agg.setdefault(topic, {"earned": 0.0, "possible": 0.0})
        ta["earned"] += earned
        ta["possible"] += float(max_pts)

        topic_freq[topic] = max(topic_freq.get(topic, 0.0), freq)

        tex = topic_exam_weight.setdefault(topic, {})
        tex[exam] = tex.get(exam, 0.0) + freq

    exam_scores: dict[str, dict[str, Any]] = {}
    for exam, vals in exam_agg.items():
        earned, possible = vals["earned"], vals["possible"]
        exam_scores[exam] = {
            "earned": int(earned) if earned == int(earned) else earned,
            "possible": int(possible) if possible == int(possible) else possible,
            "percentage": _safe_percentage(earned, possible),
        }

    readiness: dict[str, float] = {}
    for exam, num in readiness_num.items():
        den = readiness_den.get(exam, 0.0)
        readiness[exam] = _safe_percentage(num, den) if den > 0 else 0.0

    topic_scores: dict[str, dict[str, Any]] = {}
    for topic, vals in topic_agg.items():
        earned, possible = vals["earned"], vals["possible"]
        pct = _safe_percentage(earned, possible)
        freq = topic_freq.get(topic, 0.0)
        topic_scores[topic] = {
            "earned": int(earned) if earned == int(earned) else earned,
            "possible": int(possible) if possible == int(possible) else possible,
            "percentage": pct,
            "exam_frequency": freq,
            "status": _topic_status(pct),
        }

    critical_misses: list[str] = []
    for topic, info in topic_scores.items():
        if float(info["exam_frequency"]) >= 0.8 and info["status"] == "weak":
            critical_misses.append(topic)

    study_priorities: list[dict[str, Any]] = []
    for topic, info in topic_scores.items():
        freq = float(info["exam_frequency"])
        ratio = (float(info["percentage"]) / 100.0) if info["possible"] else 0.0
        priority_score = freq * (1.0 - ratio)

        exam_weights = topic_exam_weight.get(topic, {})
        if exam_weights:
            primary_exam = max(exam_weights.items(), key=lambda kv: kv[1])[0]
        else:
            primary_exam = "Unknown"

        pct = float(info["percentage"])
        status = str(info["status"])
        reason = (
            f"Topic appears often on exams (frequency {freq:.0%}) and your score is {pct:.0f}% ({status})."
            if freq >= 0.5
            else f"Score is {pct:.0f}% ({status}); improving this topic still helps overall readiness."
        )

        study_priorities.append(
            {
                "topic": topic,
                "topic_display": topic_display_pick.get(topic, topic),
                "exam": primary_exam,
                "priority_score": round(priority_score, 4),
                "reason": reason,
            }
        )

    study_priorities.sort(key=lambda x: x["priority_score"], reverse=True)

    return {
        "exam_scores": exam_scores,
        "topic_scores": topic_scores,
        "critical_misses": critical_misses,
        "readiness": readiness,
        "study_priorities": study_priorities,
    }
