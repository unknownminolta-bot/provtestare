#!/usr/bin/env bash
set -e

cd "$(dirname "$0")"

CLOUDFLARED="$HOME/.local/bin/cloudflared"
PORT=${PORT:-5111}

if [ ! -x "$CLOUDFLARED" ]; then
    echo "Installerar cloudflared..."
    mkdir -p "$HOME/.local/bin"
    curl -fsSL https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-amd64 \
        -o "$CLOUDFLARED"
    chmod +x "$CLOUDFLARED"
fi

echo "╔══════════════════════════════════════════╗"
echo "║  PROVTESTARE — Publik tunnel             ║"
echo "╚══════════════════════════════════════════╝"
echo ""
echo "  Startar tunnel till localhost:$PORT..."
echo "  Den publika URL:en visas nedan."
echo "  Ctrl+C för att stänga."
echo ""

"$CLOUDFLARED" tunnel --url "http://localhost:$PORT"
