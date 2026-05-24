#!/usr/bin/env bash
# Start workbench server from agentskills-audit-collection root (handles URL prefix 404).
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
PORT="${ASW_LIVE_PORT:-8765}"
PIDFILE="$ROOT/.cursor/.audit-http-server.pid"

if command -v lsof >/dev/null 2>&1; then
  OLD="$(lsof -ti :"$PORT" 2>/dev/null || true)"
  if [[ -n "$OLD" ]]; then
    echo "Stopping existing process on port $PORT (pid $OLD)…" >&2
    kill "$OLD" 2>/dev/null || true
    sleep 0.4
  fi
fi

mkdir -p "$ROOT/.cursor"
nohup python3 "$ROOT/scripts/serve-workbench.py" --port "$PORT" >/tmp/asw-workbench-${PORT}.log 2>&1 &
echo $! > "$PIDFILE"
sleep 0.6

if ! curl -fsS "http://127.0.0.1:${PORT}/workbench/live/data/barrierlens-run-state.json" >/dev/null; then
  echo "ERROR: server did not start. Log: /tmp/asw-workbench-${PORT}.log" >&2
  tail -20 "/tmp/asw-workbench-${PORT}.log" >&2 || true
  exit 1
fi

LIVE="http://127.0.0.1:${PORT}/workbench/live/?barrierlens=1"
echo "OK — Open: $LIVE" >&2

case "$(uname -s)" in
  Darwin) open "$LIVE" 2>/dev/null || true ;;
  Linux) command -v xdg-open >/dev/null && xdg-open "$LIVE" || true ;;
esac
