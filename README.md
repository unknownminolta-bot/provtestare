# Provtestare

Flask-baserad övningsapp för svenska högskolekurser i fysik, matematik och kemi, plus ett verktygskit för Casio fx-9860 formelsamlingar.

## Provmoduler

| Läge | Slug | Beskrivning | Frågor |
|------|------|-------------|--------|
| KEXF01 | `kexf01` | Kemi 1 — Tekniskt basår (omtenta) | 30 |
| FYXF04 | `fyxf04` | Fysik 4 | 21 |
| MAXF02 | `maxf02` | Matematik 3c/4 | 20 |
| Fysik 1+2 | `fysik12` | Fysik 1+2 (Mat-Fys-provet) | 14 |
| Fullständig diagnostik | `full` | Alla frågor | 85 |

Frågorna är flerval, numeriska (med toleransbaserad bedömning), eller fritext. Poängräknaren ger ämnesvis diagnostik, beredskapsvärden och studieprioriteter.

## Snabbstart

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python app.py
```

Öppna http://localhost:5111 i webbläsaren.

### AI-förklaringar (valfritt)

Appen har en "Förklara"-knapp som via Gemini ger konceptförklaringar utan att avslöja svaret. Skapa en `.env`-fil i projektroten:

```
GEMINI_API_KEY=din-nyckel-här
```

Utan nyckel fungerar appen som vanligt — knappen visar ett tydligt felmeddelande. Modellen kan ändras med `GEMINI_MODEL` (standard: `gemini-2.5-flash`).

## Casio fx-9860 formelverktyg

Katalogen `casio/` innehåller formelsamlingar och konverterare för Casio fx-9860GIII:

- **`*.txt`** — Formelsamlingar per ämne (Mekanik, Vågor, Elmagn, Termo, Modern, Konstanter)
- **`FORMLER.py`** — Interaktiv Python-meny för att bläddra formler direkt på räknaren
- **`convert_to_eam.py`** — Konverterar `.txt` till `.eam`-format
- **`txt_to_g1e.py`** — Konverterar `.txt` till `.g1e`-filer (USB-överföring)
- **`generate_eam_g2e.py`** — Genererar `.g2e` eActivity-filer med inbäddade formler

## Projektstruktur

```
app.py                   Flask-app (port 5111)
scorer.py                Poängräknare och diagnostikgenerator
questions_physics.py     FYXF04 + Fysik 1+2 frågebanker
questions_math.py        MAXF02 frågebank
questions_chemistry.py   KEXF01 frågebank
templates/index.html     Webb-UI
static/style.css         Stilmall
requirements.txt         Python-beroenden
docs/                    Provschema-utkast
casio/                   Räknarverktyg
```
