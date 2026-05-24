#!/usr/bin/env bash
# Open Live Workbench — must serve from agentskills-audit-collection repo root.
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
PORT="${ASW_LIVE_PORT:-8765}"
STATE="${1:-validation/golden/audit-run.example.json}"

# Default: BarrierLens golden (always in repo) unless local artifact exists
if [[ "$#" -eq 0 ]]; then
  if [[ -f "$ROOT/validation/artifacts/20260524T055013Z-9936/run-state.json" ]]; then
    STATE="validation/artifacts/20260524T055013Z-9936/run-state.json"
  else
    STATE="validation/golden/barrierlens-run-state.json"
  fi
fi

exec "$ROOT/.cursor/hooks/open-live-workbench.sh" "$STATE"
