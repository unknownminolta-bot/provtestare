#!/usr/bin/env bash
set -e

cd "$(dirname "$0")"

if [ ! -d ".venv" ]; then
    echo "Kör ./setup.sh först"
    exit 1
fi

PORT=${PORT:-5111}
LOCAL_IP=$(hostname -I 2>/dev/null | awk '{print $1}' || echo "localhost")

echo "╔══════════════════════════════════════╗"
echo "║       PROVTESTARE — Startar          ║"
echo "╚══════════════════════════════════════╝"
echo ""
echo "  Lokal:  http://localhost:$PORT"
echo "  LAN:    http://$LOCAL_IP:$PORT"
echo ""

export HOST=0.0.0.0
export PORT=$PORT

.venv/bin/python3 app.py
