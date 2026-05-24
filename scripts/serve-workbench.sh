#!/usr/bin/env bash
# Start http.server from agentskills-audit-collection root (fixes 404 on golden/artifacts).
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
PORT="${ASW_LIVE_PORT:-8765}"
PIDFILE="$ROOT/.cursor/.audit-http-server.pid"

cd "$ROOT"

if command -v lsof >/dev/null 2>&1; then
  OLD="$(lsof -ti :"$PORT" 2>/dev/null || true)"
  if [[ -n "$OLD" ]]; then
    echo "Stopping existing process on port $PORT (pid $OLD)…" >&2
    kill "$OLD" 2>/dev/null || true
    sleep 0.3
  fi
fi

nohup python3 -m http.server "$PORT" >/dev/null 2>&1 &
echo $! > "$PIDFILE"
sleep 0.5

probe() {
  curl -fsS -o /dev/null -w "%{http_code}" "$1" 2>/dev/null || echo "000"
}

echo "Serving from: $ROOT" >&2
echo "Port: $PORT" >&2

CODES=(
  "http://127.0.0.1:${PORT}/workbench/live/data/barrierlens-run-state.json"
  "http://127.0.0.1:${PORT}/validation/golden/barrierlens-run-state.json"
  "http://127.0.0.1:${PORT}/agentskills-audit-collection/workbench/live/data/barrierlens-run-state.json"
)

OK_URL=""
for u in "${CODES[@]}"; do
  code="$(probe "$u")"
  echo "  [$code] $u" >&2
  if [[ "$code" == "200" && -z "$OK_URL" ]]; then
    OK_URL="$u"
  fi
done

if [[ -z "$OK_URL" ]]; then
  echo "ERROR: run-state probe failed. Check you are in agentskills-audit-collection." >&2
  exit 1
fi

LIVE="http://127.0.0.1:${PORT}/workbench/live/?barrierlens=1"
REPORT="http://127.0.0.1:${PORT}/reports/barrierlens-audit.html"

echo "" >&2
echo "Open Live:  $LIVE" >&2
echo "Open Report: $REPORT" >&2

case "$(uname -s)" in
  Darwin) open "$LIVE" 2>/dev/null || true ;;
  Linux) command -v xdg-open >/dev/null && xdg-open "$LIVE" || true ;;
esac
