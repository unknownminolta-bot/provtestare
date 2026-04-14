# Provtestare

Flask-baserad övningsapp for svenska högskolekurser i fysik, matematik och kemi. Inkluderar en svart tavla (rityta) med AI-handledare via Gemini, plus ett verktygskit för Casio fx-9860 formelsamlingar.

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
chmod +x setup.sh start.sh
./setup.sh
./start.sh
```

Alternativt manuellt:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python app.py
```

Öppna http://localhost:5111 i webbläsaren.

## Dela med kursare

### Alt 1: LAN-delning (enklast)

Kör `./start.sh` — appen startar på `0.0.0.0:5111` och skriptet visar din LAN-IP. Dina kursare ansluter till `http://<din-ip>:5111` från sina enheter på samma nätverk (t.ex. eduroam).

### Alt 2: Docker

```bash
docker compose up --build
```

Appen körs på port 8080 med gunicorn (produktionsserver).

### Alt 3: Skicka zipfilen

Zippa och skicka. Mottagaren kör:

```bash
unzip provtestare.zip && cd exam-tester
chmod +x setup.sh start.sh
./setup.sh
./start.sh
```

Kräver Python 3.10+ och internetanslutning (för KaTeX-rendering via CDN).

## AI-handledare (valfritt)

Appen har en svart tavla där du kan rita uträkningar och fråga Gemini om hjälp. Skapa en `.env`-fil i projektroten:

```
GEMINI_API_KEY=din-nyckel-här
```

Utan nyckel fungerar appen fullt ut — alla frågor, poängsättning och diagnostik fungerar. Bara AI-handledaren (svarta tavlan) kräver nyckeln. Modellen kan ändras med `GEMINI_MODEL` (standard: `gemini-2.5-flash`).

## Webbläsarstöd

| Webbläsare | Status |
|------------|--------|
| Chrome / Edge (senaste) | Full support |
| Firefox (senaste) | Full support |
| Safari 14+ / iOS Safari | Full support |
| Äldre mobila webbläsare | Grundfunktioner OK, rityta kan ha begränsningar |

Appen fungerar på mobil men är optimerad för laptop/desktop.

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
templates/index.html     Webb-UI + svarta tavlan
static/style.css         Stilmall
setup.sh                 Installationsskript
start.sh                 Startskript (LAN-delning)
Dockerfile               Docker-image
docker-compose.yml       Docker Compose
requirements.txt         Python-beroenden
docs/                    Provschema-utkast
casio/                   Räknarverktyg
```
