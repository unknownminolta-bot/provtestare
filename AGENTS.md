# AGENTS.md

## Cursor Cloud specific instructions

### Overview

Provtestare is a single-process Flask (Python 3.12) quiz app with no database or external service dependencies. All question data lives in Python modules and a JSON file. The optional Gemini AI tutor requires `GEMINI_API_KEY` but all quiz/scoring functionality works without it.

### Running the app

```bash
cd /workspace
source .venv/bin/activate
python app.py
```

The dev server starts on port **5111** (configurable via `PORT` env var). No database, Redis, or other backing services are needed.

### Linting

```bash
.venv/bin/flake8 app.py scorer.py hp_scorer.py --max-line-length=120
```

Pre-existing E402 (imports after `load_dotenv()`) and one F841 are known; do not treat them as regressions.

### Tests

The only automated test is the Casio formula audit test:

```bash
cd casio && ../.venv/bin/python test_formula_audit.py
```

Exit code 0 = pass (no stdout output on success).

### Gotchas

- `python3.12-venv` must be installed at the system level (`sudo apt-get install -y python3.12-venv`) before creating the virtualenv. The update script handles this.
- The app uses `load_dotenv()` before importing question modules, so the E402 lint warnings are intentional.
- KaTeX math rendering requires CDN access (internet); offline testing will show raw LaTeX in the browser but the app still functions.
