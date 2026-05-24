#!/usr/bin/env bash
# Append an NDJSON event and optionally patch activeAnnotation in run-state.json.
# Usage:
#   ./scripts/audit-run-emit.sh <run-dir> <type> [key=value ...]
# Example:
#   ./scripts/audit-run-emit.sh validation/artifacts/20260524T120000Z-1 step_update \
#     stageId=live-functional stepId=cta-primary status=in_progress \
#     annotation='Clicking primary CTA'
set -euo pipefail

RUN_DIR="${1:-}"
EVENT_TYPE="${2:-}"
shift 2 || true

if [[ -z "$RUN_DIR" || -z "$EVENT_TYPE" ]]; then
  echo "Usage: $0 <run-dir> <event-type> [key=value ...]" >&2
  exit 1
fi

TS="$(date -u +%Y-%m-%dT%H:%M:%SZ)"
EVENT_FILE="$RUN_DIR/run-events.ndjson"

# Build JSON object from key=value pairs
JSON="{\"ts\":\"$TS\",\"type\":\"$EVENT_TYPE\""
for kv in "$@"; do
  key="${kv%%=*}"
  val="${kv#*=}"
  # escape quotes in val
  val="${val//\"/\\\"}"
  JSON+=",\"$key\":\"$val\""
done
JSON+="}"

echo "$JSON" >> "$EVENT_FILE"
echo "appended: $EVENT_TYPE"

# If annotation= provided, patch run-state via python if available
ANNOTATION=""
for kv in "$@"; do
  [[ "$kv" == annotation=* ]] && ANNOTATION="${kv#annotation=}"
done

if [[ -n "$ANNOTATION" && -f "$RUN_DIR/run-state.json" ]]; then
  python3 - "$RUN_DIR/run-state.json" "$ANNOTATION" "$TS" <<'PY' 2>/dev/null || true
import json, sys
path, ann, ts = sys.argv[1], sys.argv[2], sys.argv[3]
with open(path) as f:
    s = json.load(f)
s["activeAnnotation"] = ann
s["updatedAt"] = ts
with open(path, "w") as f:
    json.dump(s, f, indent=2, ensure_ascii=False)
    f.write("\n")
PY
fi
