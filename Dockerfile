FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app.py scorer.py hp_scorer.py hp_pdf_parser.py hp_generator.py questions_*.py ./
COPY data/hp_imported_questions.json data/
COPY templates/ templates/
COPY static/ static/

EXPOSE 8080

CMD ["gunicorn", "--bind", "0.0.0.0:8080", "--workers", "2", "--threads", "4", "--timeout", "120", "app:app"]
