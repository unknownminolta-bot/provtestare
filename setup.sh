#!/usr/bin/env bash
set -e

echo "╔══════════════════════════════════════╗"
echo "║       PROVTESTARE — Installation     ║"
echo "╚══════════════════════════════════════╝"
echo ""

if ! command -v python3 &>/dev/null; then
    echo "❌ Python 3 krävs men hittades inte."
    echo "   Installera: https://www.python.org/downloads/"
    exit 1
fi

PY_VER=$(python3 -c "import sys; print(f'{sys.version_info.major}.{sys.version_info.minor}')")
echo "✓ Python $PY_VER hittad"

if [ ! -d ".venv" ]; then
    echo "→ Skapar virtuell miljö..."
    python3 -m venv .venv
fi

echo "→ Installerar beroenden..."
.venv/bin/pip install -q -r requirements.txt

if [ ! -f ".env" ]; then
    echo ""
    echo "ℹ  Ingen .env-fil hittad."
    echo "   Appen fungerar utan AI-handledare."
    echo "   För AI-stöd, skapa .env med:"
    echo "     GEMINI_API_KEY=din-nyckel"
    echo ""
fi

LOCAL_IP=$(hostname -I 2>/dev/null | awk '{print $1}' || echo "localhost")
PORT=${PORT:-5111}

echo ""
echo "✓ Installation klar!"
echo ""
echo "╔══════════════════════════════════════╗"
echo "║  Starta med:                         ║"
echo "║    ./start.sh                        ║"
echo "║                                      ║"
echo "║  Lokal:  http://localhost:$PORT       ║"
echo "║  LAN:    http://$LOCAL_IP:$PORT  ║"
echo "╚══════════════════════════════════════╝"
