# Exam Knowledge Tester

Flask-based practice exam app for Swedish university physics and math courses, plus a Casio fx-9860 formula sheet toolchain.

## Exam modules

| Mode | Slug | Description |
|------|------|-------------|
| FYXF04 | `fyxf04` | Fysik 4 (Chalmers/LiU) |
| MAXF02 | `maxf02` | Matematik 3c/4 |
| Fysik 1+2 | `fysik12` | Fysik 1+2 (Mat-Fys provet) |
| Full Diagnostic | `full` | All 55 questions |

Questions are multiple-choice or numeric with tolerance-based grading. The scorer produces per-topic diagnostics and point breakdowns.

## Quick start

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python app.py
```

Open http://localhost:5111 in your browser.

## Casio fx-9860 formula tools

The `casio/` directory contains formula sheets and converters for the Casio fx-9860GIII calculator:

- **`*.txt`** — Plain-text formula sheets per topic (Mekanik, Vagor, Elmagn, Termo, Modern, Konstanter)
- **`FORMLER.py`** — Interactive Python menu for browsing formulas directly on the calculator
- **`convert_to_eam.py`** — Converts `.txt` sheets to `.eam` format for [eAct Maker](https://tools.planet-casio.com/EactMaker/)
- **`txt_to_g1e.py`** — Converts `.txt` sheets to `.g1e` files (transfer via USB)
- **`generate_eam_g2e.py`** — Generates `.g2e` eActivity files with embedded formulas

To regenerate the binary outputs:

```bash
cd casio
python convert_to_eam.py    # -> eam/
python txt_to_g1e.py         # -> g1e/
python generate_eam_g2e.py   # -> eam_g2e/, g2e_out/
```

## Project structure

```
app.py                  Flask application (port 5111)
scorer.py               Scoring engine and diagnostic reports
questions_physics.py    FYXF04 + Fysik 1+2 question banks
questions_math.py       MAXF02 question bank
templates/index.html    Web UI
static/style.css        Styles
requirements.txt        Python dependencies
docs/                   Exam scheduling drafts
casio/                  Calculator formula tools
```
