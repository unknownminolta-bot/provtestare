#!/usr/bin/env python3
"""Provtestare – Flask-app för tentamensförberedelse."""

import base64
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
app.secret_key = os.environ.get("SECRET_KEY", "exam-tester-local-only-key")

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


@app.route("/")
def index():
    return render_template("index.html", exam_labels=EXAM_LABELS)


@app.route("/api/status")
def api_status():
    return jsonify({
        "ai_available": bool(os.environ.get("GEMINI_API_KEY")),
        "total_questions": len(ALL_QUESTIONS),
    })


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


_BLACKBOARD_SYSTEM_PROMPT = (
    "Du är en pedagogisk handledare för en svensk högskolestudent som övar inför tentamen.\n"
    "Studenten har ritat/skrivit uträkningar på en digital svart tavla (mörk bakgrund, ljusa streck).\n\n"
    "Regler:\n"
    "1. Tolka studentens handskrivna arbete i bilden — identifiera ekvationer, uträkningar och resonemang.\n"
    "2. Om studenten har gjort räknefel eller logiska fel, peka ut dem tydligt och förklara varför.\n"
    "3. Ge vägledning mot rätt lösningsgång utan att avslöja det exakta svaret direkt.\n"
    "4. Om studenten ställer en specifik fråga i textmeddelandet, besvara den.\n"
    "5. Svara på svenska. Var tydlig och pedagogisk.\n"
    "6. Skriv formler med vanlig text (t.ex. F = ma, E = mc²). Undvik markdown-formatering.\n"
    "7. Om bilden är tom eller oläslig, be studenten skriva tydligare."
)


@app.route("/api/blackboard-ask", methods=["POST"])
def blackboard_ask():
    data = request.get_json()
    image_b64 = data.get("image", "")
    user_text = data.get("text", "")
    qid = data.get("question_id", "")

    if not image_b64:
        return jsonify({"error": "Ingen bild skickades."}), 400

    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        return jsonify({"error": "Ingen API-nyckel konfigurerad. Sätt GEMINI_API_KEY i .env-filen."}), 503

    try:
        from google import genai
        from google.genai import types
    except ImportError:
        return jsonify({"error": "google-genai ej installerat. Kör: pip install google-genai"}), 503

    q_lookup = {q["id"]: q for q in ALL_QUESTIONS}
    q = q_lookup.get(qid)

    prompt_parts = [_BLACKBOARD_SYSTEM_PROMPT, "\n\n"]
    if q:
        prompt_parts.append(
            f"Aktuell fråga ({q.get('topic_display', q.get('topic', ''))}): {q['question']}\n"
        )
        if q.get("unit"):
            prompt_parts.append(f"Svaret ska ges i enheten: {q['unit']}\n")
    if user_text:
        prompt_parts.append(f"\nStudentens fråga: {user_text}\n")
    prompt_parts.append(
        "\nAnalysera bilden av studentens arbete ovan och ge pedagogisk vägledning."
    )

    image_bytes = base64.b64decode(image_b64)
    text_prompt = "".join(prompt_parts)

    client = genai.Client(api_key=api_key)
    model_name = os.environ.get("GEMINI_MODEL", "gemini-2.5-flash")

    contents = [
        types.Part.from_bytes(data=image_bytes, mime_type="image/png"),
        text_prompt,
    ]

    def generate():
        try:
            for chunk in client.models.generate_content_stream(
                model=model_name, contents=contents
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
    host = os.environ.get("HOST", "127.0.0.1")
    port = int(os.environ.get("PORT", "5111"))
    debug = os.environ.get("FLASK_DEBUG", "1") == "1"
    app.run(host=host, port=port, debug=debug)
