#!/usr/bin/env python3
"""Provtestare – Flask-app för tentamensförberedelse."""

import json
import os
import random

from dotenv import load_dotenv
from flask import Flask, Response, render_template, request, jsonify, session, stream_with_context

load_dotenv()

from questions_physics import FYXF04_QUESTIONS, FYSIK12_QUESTIONS
from questions_math import MAXF02_QUESTIONS
from questions_chemistry import KEXF01_QUESTIONS
from scorer import score_answers, generate_diagnostic

app = Flask(__name__)
app.secret_key = "exam-tester-local-only-key"

ALL_QUESTIONS = (
    FYXF04_QUESTIONS + FYSIK12_QUESTIONS + MAXF02_QUESTIONS + KEXF01_QUESTIONS
)

EXAM_SETS = {
    "kexf01": KEXF01_QUESTIONS,
    "fyxf04": FYXF04_QUESTIONS,
    "maxf02": MAXF02_QUESTIONS,
    "fysik12": FYSIK12_QUESTIONS,
    "full": ALL_QUESTIONS,
}

EXAM_LABELS = {
    "kexf01": "KEXF01 — Kemi 1 (omtenta)",
    "fyxf04": "FYXF04 — Fysik 4",
    "maxf02": "MAXF02 — Matematik 3c/4",
    "fysik12": "Fysik 1+2 (Mat-Fys-provet)",
    "full": f"Fullständig diagnostik (alla {len(ALL_QUESTIONS)})",
}


_TUTOR_SYSTEM_PROMPT = (
    "Du är en pedagogisk handledare för en svensk högskolestudent som övar inför tentamen.\n\n"
    "Regler:\n"
    "1. Förklara det relevanta konceptet, teorin eller formeln som krävs för denna typ av uppgift.\n"
    "2. Beskriv en steg-för-steg-metod (lösningsgång) utan att avslöja det specifika svaret.\n"
    "3. Svara på svenska. Var kortfattad — högst ~150 ord.\n"
    "4. Skriv formler inline med vanlig text, t.ex. pH = -log[H⁺]. Använd inte markdown.\n"
    "5. Om frågan gäller namngivning eller definitioner, förklara den bakomliggande principen "
    "och ge liknande exempel — inte svaret på just denna fråga.\n"
    "6. Avsluta med en kort uppmaning att studenten ska tillämpa metoden själv."
)


def _build_tutor_prompt(q: dict) -> str:
    parts = [
        f"Ämne: {q.get('topic_display', q.get('topic', 'Okänt'))}",
        f"Provkod: {q.get('exam', '')}",
        f"Fråga: {q['question']}",
    ]
    if q.get("unit"):
        parts.append(f"Svaret ges i enheten: {q['unit']}")
    if q["answer_type"] == "multiple_choice" and q.get("choices"):
        opts = [f"  {chr(65 + i)}) {c}" for i, c in enumerate(q["choices"])]
        parts.append("Svarsalternativ:\n" + "\n".join(opts))
    parts.append(
        "\nFörklara det underliggande konceptet och ge en lösningsgång "
        "för denna typ av uppgift."
    )
    return "\n".join(parts)


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


@app.route("/api/explain", methods=["POST"])
def explain_question():
    data = request.get_json()
    qid = data.get("question_id", "")

    q_lookup = {q["id"]: q for q in ALL_QUESTIONS}
    q = q_lookup.get(qid)
    if not q:
        return jsonify({"error": "Frågan hittades inte."}), 404

    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        return jsonify({"error": "Ingen API-nyckel konfigurerad. Sätt GEMINI_API_KEY i .env-filen."}), 503

    try:
        from google import genai
    except ImportError:
        return jsonify({"error": "google-genai ej installerat. Kör: pip install google-genai"}), 503

    client = genai.Client(api_key=api_key)
    model_name = os.environ.get("GEMINI_MODEL", "gemini-2.5-flash")
    prompt = _TUTOR_SYSTEM_PROMPT + "\n\n" + _build_tutor_prompt(q)

    def generate():
        try:
            for chunk in client.models.generate_content_stream(
                model=model_name, contents=prompt
            ):
                if chunk.text:
                    yield f"data: {json.dumps({'text': chunk.text})}\n\n"
        except Exception as e:
            yield f"data: {json.dumps({'error': str(e)})}\n\n"
        yield "data: [DONE]\n\n"

    return Response(
        stream_with_context(generate()),
        content_type="text/event-stream",
        headers={"Cache-Control": "no-cache", "X-Accel-Buffering": "no"},
    )


if __name__ == "__main__":
    app.run(debug=True, port=5111)
