#!/usr/bin/env bash
# Shared helper: ensure static server + open Live Workbench in browser.
set -euo pipefail

# Repo root: agentskills-audit-collection/
ROOT="$(cd "$(dirname "$0")/../.." && pwd)"
PORT="${ASW_LIVE_PORT:-8765}"
STATE_PATH="${1:-validation/golden/audit-run.example.json}"
CACHE="$ROOT/.cursor/last-audit-run.json"
PIDFILE="$ROOT/.cursor/.audit-http-server.pid"

mkdir -p "$ROOT/.cursor"

# Persist last opened state for /audit prompts without init script
if [[ "$STATE_PATH" != "validation/golden/audit-run.example.json" ]]; then
  python3 - "$CACHE" "$STATE_PATH" <<'PY' 2>/dev/null || true
import json, sys, datetime
cache, path = sys.argv[1], sys.argv[2]
data = {"statePath": path, "openedAt": datetime.datetime.utcnow().isoformat() + "Z"}
with open(cache, "w") as f:
    json.dump(data, f, indent=2)
PY
fi

server_running() {
  if command -v curl >/dev/null 2>&1; then
    curl -fsS "http://127.0.0.1:${PORT}/" >/dev/null 2>&1
    return $?
  fi
  if [[ -f "$PIDFILE" ]]; then
    local pid
    pid="$(cat "$PIDFILE" 2>/dev/null || true)"
    [[ -n "$pid" ]] && kill -0 "$pid" 2>/dev/null
    return $?
  fi
  return 1
}

start_server() {
  if server_running; then
    return 0
  fi
  (cd "$ROOT" && nohup python3 -m http.server "$PORT" >/dev/null 2>&1 & echo $! > "$PIDFILE")
  sleep 0.4
}

open_url() {
  local url="http://127.0.0.1:${PORT}/workbench/live/?state=${STATE_PATH}"
  case "$(uname -s)" in
    Darwin) open "$url" 2>/dev/null || true ;;
    Linux)
      if command -v xdg-open >/dev/null 2>&1; then xdg-open "$url" 2>/dev/null || true; fi
      ;;
    MINGW*|MSYS*|CYGWIN*) start "$url" 2>/dev/null || true ;;
  esac
  echo "Opened: $url" >&2
}

start_server
open_url
