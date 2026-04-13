#!/usr/bin/env python3
"""Exam Knowledge Tester – Flask app."""

import json
import random
from flask import Flask, render_template, request, jsonify, session

from questions_physics import FYXF04_QUESTIONS, FYSIK12_QUESTIONS
from questions_math import MAXF02_QUESTIONS
from scorer import score_answers, generate_diagnostic

app = Flask(__name__)
app.secret_key = "exam-tester-local-only-key"

ALL_QUESTIONS = FYXF04_QUESTIONS + FYSIK12_QUESTIONS + MAXF02_QUESTIONS

EXAM_SETS = {
    "fyxf04": FYXF04_QUESTIONS,
    "maxf02": MAXF02_QUESTIONS,
    "fysik12": FYSIK12_QUESTIONS,
    "full": ALL_QUESTIONS,
}

EXAM_LABELS = {
    "fyxf04": "FYXF04 – Fysik 4",
    "maxf02": "MAXF02 – Matematik 3c/4",
    "fysik12": "Fysik 1+2 (Mat-Fys provet)",
    "full": "Full Diagnostic (all 55)",
}


@app.route("/")
def index():
    return render_template("index.html", exam_labels=EXAM_LABELS)


@app.route("/api/start", methods=["POST"])
def start_quiz():
    data = request.get_json()
    exam_mode = data.get("mode", "full")
    questions = list(EXAM_SETS.get(exam_mode, ALL_QUESTIONS))
    random.shuffle(questions)

    safe_questions = []
    for q in questions:
        safe_questions.append({
            "id": q["id"],
            "exam": q["exam"],
            "topic_display": q.get("topic_display", q["topic"]),
            "points": q["points"],
            "no_calculator": q.get("no_calculator", False),
            "question": q["question"],
            "answer_type": q["answer_type"],
            "choices": q.get("choices"),
            "unit": q.get("unit", ""),
        })

    session["exam_mode"] = exam_mode
    session["question_ids"] = [q["id"] for q in questions]

    return jsonify({"questions": safe_questions, "total": len(safe_questions)})


@app.route("/api/submit", methods=["POST"])
def submit_quiz():
    data = request.get_json()
    user_answers = data.get("answers", {})
    time_per_question = data.get("times", {})

    question_ids = session.get("question_ids", [])
    exam_mode = session.get("exam_mode", "full")

    q_lookup = {q["id"]: q for q in ALL_QUESTIONS}
    questions_in_order = [q_lookup[qid] for qid in question_ids if qid in q_lookup]

    scored = score_answers(questions_in_order, user_answers)
    diagnostic = generate_diagnostic(scored, questions_in_order)

    solutions = {}
    for q in questions_in_order:
        solutions[q["id"]] = {
            "correct_answer": str(q["correct_answer"]),
            "solution": q.get("solution", ""),
            "unit": q.get("unit", ""),
        }

    return jsonify({
        "scored": scored,
        "diagnostic": diagnostic,
        "solutions": solutions,
        "times": time_per_question,
    })


if __name__ == "__main__":
    app.run(debug=True, port=5111)
