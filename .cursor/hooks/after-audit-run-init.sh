#!/usr/bin/env bash
# afterShellExecution: open Live Workbench when audit-run-init.sh finishes.
set -euo pipefail

input="$(cat)"
command="$(echo "$input" | python3 -c "import sys,json; print(json.load(sys.stdin).get('command',''))" 2>/dev/null || echo "")"
output="$(echo "$input" | python3 -c "import sys,json; print(json.load(sys.stdin).get('output',''))" 2>/dev/null || echo "")"

if ! echo "$command" | grep -q 'audit-run-init'; then
  exit 0
fi

STATE=""
RUN_DIR=""
while IFS= read -r line; do
  case "$line" in
    STATE_URL=*) ;;
    RUN_DIR=*)
      RUN_DIR="${line#RUN_DIR=}"
      STATE="validation/artifacts/$(basename "$RUN_DIR")/run-state.json"
      ;;
  esac
done <<< "$output"

if [[ -z "$STATE" && -n "$RUN_DIR" ]]; then
  STATE="validation/artifacts/$(basename "$RUN_DIR")/run-state.json"
fi

if [[ -z "$STATE" ]]; then
  STATE="validation/golden/audit-run.example.json"
fi

ROOT="$(cd "$(dirname "$0")/../.." && pwd)"
if [[ -n "$RUN_DIR" ]]; then
  python3 - "$ROOT/.cursor/last-audit-run.json" "$STATE" "$RUN_DIR" <<'PY' 2>/dev/null || true
import json, sys, datetime
cache, state, run_dir = sys.argv[1], sys.argv[2], sys.argv[3]
with open(cache, "w") as f:
    json.dump({
        "statePath": state,
        "runDir": run_dir,
        "openedAt": datetime.datetime.utcnow().isoformat() + "Z"
    }, f, indent=2)
PY
fi

"$(dirname "$0")/open-live-workbench.sh" "$STATE" >/dev/null 2>&1 || true
exit 0
