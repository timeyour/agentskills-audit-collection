#!/usr/bin/env bash
# beforeSubmitPrompt: open Live Workbench when user starts an /audit-style request.
set -euo pipefail

input="$(cat)"
prompt="$(echo "$input" | python3 -c "import sys,json; print(json.load(sys.stdin).get('prompt',''))" 2>/dev/null || echo "")"

# Match /audit, live audit, audit workbench (EN + 审计)
if ! echo "$prompt" | python3 -c "
import sys,re
p=sys.stdin.read()
pat=r'(?i)(/audit\b|use\s+/audit|live\s+audit|audit\s+workbench|审计|交付验收|run-state\.json)'
sys.exit(0 if re.search(pat,p) else 1)
" 2>/dev/null; then
  echo '{"continue": true}'
  exit 0
fi

ROOT="$(cd "$(dirname "$0")/../.." && pwd)"
STATE="validation/golden/audit-run.example.json"

# Prefer last real run from init script
if [[ -f "$ROOT/.cursor/last-audit-run.json" ]]; then
  STATE="$(python3 -c "import json; print(json.load(open('$ROOT/.cursor/last-audit-run.json')).get('statePath','$STATE'))" 2>/dev/null || echo "$STATE")"
fi

"$(dirname "$0")/open-live-workbench.sh" "$STATE" >/dev/null 2>&1 || true

echo "$(python3 - <<PY
import json
msg = (
  'Live Workbench opened in browser (http://127.0.0.1:8765/workbench/live/). '
  'While running /audit: run ./scripts/audit-run-init.sh <url>, then update '
  'validation/artifacts/<runId>/run-state.json per .claude/skills/audit/references/live-run-protocol.md'
)
print(json.dumps({'continue': True, 'user_message': msg}))
PY
)"
exit 0
