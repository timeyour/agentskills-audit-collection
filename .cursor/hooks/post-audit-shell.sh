#!/usr/bin/env bash
# postToolUse (Shell): remind agent to sync run-state after audit-run-init.
set -euo pipefail

input="$(cat)"
command="$(echo "$input" | python3 -c "
import sys,json
d=json.load(sys.stdin)
ti=d.get('tool_input') or {}
if isinstance(ti,str):
    import json as j
    ti=j.loads(ti) if ti.startswith('{') else {'command':ti}
print(ti.get('command',''))
" 2>/dev/null || echo "")"

if ! echo "$command" | grep -qE 'audit-run-init|audit-run-emit'; then
  echo '{}'
  exit 0
fi

echo "$(python3 - <<'PY'
import json
print(json.dumps({
  "additional_context": (
    "Live Audit: update validation/artifacts/<runId>/run-state.json after each stage "
    "(activeAnnotation + step status). Append run-events.ndjson. "
    "User watches workbench/live/ — keep chat Progress Updates in sync. "
    "See .claude/skills/audit/references/live-run-protocol.md"
  )
}))
PY
)"
exit 0
