#!/usr/bin/env bash
# install_daemon.sh — Installeer de Certificaid embedding-daemon als macOS LaunchAgent
# Zie ADR-018 voor architectuurbeslissing.
#
# Gebruik:
#   bash tools/extractie/install_daemon.sh           # installeren
#   bash tools/extractie/install_daemon.sh --stop    # stoppen + verwijderen
#   bash tools/extractie/install_daemon.sh --status  # status opvragen

set -euo pipefail

LABEL="com.certificaid.embedding-daemon"
PLIST_DIR="$HOME/Library/LaunchAgents"
PLIST_PATH="$PLIST_DIR/$LABEL.plist"
LOG_DIR="$HOME/Library/Logs"
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(cd "$SCRIPT_DIR/../.." && pwd)"
DAEMON_SCRIPT="$SCRIPT_DIR/embedding_daemon.py"
PYTHON="$(which python3)"
PORT=8765

# ---------------------------------------------------------------------------
# Hulpfuncties
# ---------------------------------------------------------------------------

daemon_status() {
    if launchctl list | grep -q "$LABEL" 2>/dev/null; then
        echo "✓ LaunchAgent actief ($LABEL)"
    else
        echo "✗ LaunchAgent niet actief"
    fi
    echo ""
    echo "Health-check:"
    curl -s --max-time 2 "http://127.0.0.1:$PORT/health" 2>/dev/null \
        | python3 -m json.tool 2>/dev/null \
        || echo "  (daemon niet bereikbaar op poort $PORT)"
}

stop_daemon() {
    echo "→ Stoppen en verwijderen …"
    launchctl unload -w "$PLIST_PATH" 2>/dev/null || true
    rm -f "$PLIST_PATH"
    echo "✓ LaunchAgent verwijderd"
}

# ---------------------------------------------------------------------------
# Argument-verwerking
# ---------------------------------------------------------------------------

if [[ "${1:-}" == "--status" ]]; then
    daemon_status
    exit 0
fi

if [[ "${1:-}" == "--stop" ]]; then
    if [[ -f "$PLIST_PATH" ]]; then
        stop_daemon
    else
        echo "LaunchAgent-plist niet gevonden: $PLIST_PATH"
    fi
    exit 0
fi

# ---------------------------------------------------------------------------
# Controleer vereisten
# ---------------------------------------------------------------------------

echo "→ Vereisten controleren …"

if [[ ! -f "$DAEMON_SCRIPT" ]]; then
    echo "✗ Daemon-script niet gevonden: $DAEMON_SCRIPT"
    exit 1
fi

if ! "$PYTHON" -c "import fastapi, uvicorn" 2>/dev/null; then
    echo "→ fastapi en uvicorn installeren …"
    "$PYTHON" -m pip install "fastapi>=0.111.0" "uvicorn[standard]>=0.29.0"
fi

if ! "$PYTHON" -c "import chromadb, sentence_transformers" 2>/dev/null; then
    echo "✗ chromadb of sentence-transformers niet geïnstalleerd."
    echo "  Installeer via: pip install -r $PROJECT_ROOT/requirements.txt"
    exit 1
fi

# ---------------------------------------------------------------------------
# Plist schrijven
# ---------------------------------------------------------------------------

mkdir -p "$PLIST_DIR" "$LOG_DIR"

cat > "$PLIST_PATH" << PLIST
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN"
    "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>Label</key>
    <string>$LABEL</string>

    <key>ProgramArguments</key>
    <array>
        <string>$PYTHON</string>
        <string>$DAEMON_SCRIPT</string>
        <string>--port</string>
        <string>$PORT</string>
    </array>

    <key>WorkingDirectory</key>
    <string>$PROJECT_ROOT</string>

    <key>RunAtLoad</key>
    <true/>

    <key>KeepAlive</key>
    <true/>

    <key>StandardOutPath</key>
    <string>$LOG_DIR/certificaid-embedding-daemon.log</string>

    <key>StandardErrorPath</key>
    <string>$LOG_DIR/certificaid-embedding-daemon.err.log</string>

    <!-- Herstart pas na 10 seconden bij crash -->
    <key>ThrottleInterval</key>
    <integer>10</integer>
</dict>
</plist>
PLIST

echo "✓ Plist geschreven: $PLIST_PATH"

# ---------------------------------------------------------------------------
# Verwijder eventuele vorige instantie
# ---------------------------------------------------------------------------

launchctl unload "$PLIST_PATH" 2>/dev/null || true

# ---------------------------------------------------------------------------
# Laden
# ---------------------------------------------------------------------------

launchctl load -w "$PLIST_PATH"
echo "✓ LaunchAgent geladen (start bij login, herstart bij crash)"
echo ""
echo "Logs:"
echo "  stdout: $LOG_DIR/certificaid-embedding-daemon.log"
echo "  stderr: $LOG_DIR/certificaid-embedding-daemon.err.log"
echo ""
echo "Wacht ~20s op model-load, dan:"
echo "  curl http://127.0.0.1:$PORT/health"
echo ""
echo "Stoppen: bash tools/extractie/install_daemon.sh --stop"
