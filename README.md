# Provtestare

**[provtestare.onrender.com](https://provtestare.onrender.com)** -- klicka och kör direkt.

Flask-baserad övningsapp for svenska högskolekurser i fysik, matematik och kemi. Inkluderar en svart tavla (rityta) med AI-handledare via Gemini, plus ett verktygskit för Casio fx-9860 formelsamlingar.

[![Deploy to Render](https://render.com/images/deploy-to-render-button.svg)](https://render.com/deploy?repo=https://github.com/unknownminolta-bot/provtestare)

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

### Alt 1: Publik länk (enklast — rekommenderas)

Appen kan hostas gratis på Render. Klicka knappen ovan eller gå till:

```
https://render.com/deploy?repo=https://github.com/unknownminolta-bot/provtestare
```

1. Skapa ett gratis Render-konto
2. Klicka "Deploy" — appen byggs automatiskt
3. Du får en publik URL typ `https://provtestare-xxxx.onrender.com`
4. Skicka länken till kursarna

Obs: Gratis-planen sover efter 15 min inaktivitet (30s kallstart vid nästa besök). All quiz-funktionalitet fungerar utan API-nyckel — AI-handledaren kräver `GEMINI_API_KEY` i Render-miljövariabler.

**Alternativa plattformar:** Railway (`railway.app`) och Fly.io (`fly.io`) fungerar också med samma `Procfile`.

### Alt 2: LAN-delning

Kör `./start.sh` — appen startar på `0.0.0.0:5111` och skriptet visar din LAN-IP. Kursare ansluter till `http://<din-ip>:5111` på samma nätverk (t.ex. eduroam).

### Alt 3: Docker

```bash
docker compose up --build
```

### Alt 4: Zipfil

Zippa och skicka. Mottagaren kör:

```bash
unzip provtestare.zip && cd exam-tester
./setup.sh && ./start.sh
```

Kräver Python 3.10+ och internetanslutning (KaTeX CDN).

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
