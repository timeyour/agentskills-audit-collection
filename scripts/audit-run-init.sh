#!/usr/bin/env bash
# Initialize a live audit run directory for workbench/live polling.
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
URL="${1:-}"
if [[ -z "$URL" ]]; then
  echo "Usage: $0 <target-url>" >&2
  exit 1
fi

RUN_ID="$(date -u +%Y%m%dT%H%M%SZ)-$$"
RUN_DIR="$ROOT/validation/artifacts/$RUN_ID"
mkdir -p "$RUN_DIR"

cat > "$RUN_DIR/run-state.json" <<EOF
{
  "runVersion": "0.1.0",
  "runId": "$RUN_ID",
  "target": { "url": "$URL", "label": "$URL" },
  "workflow": { "id": "audit-default-v1", "label": "Standard website delivery audit" },
  "progress": { "current": 1, "total": 9, "label": "1/9 — Intake & permissions" },
  "currentStageId": "intake",
  "currentStepId": "target",
  "activeAnnotation": "初始化审计：确认目标与权限边界",
  "status": "running",
  "stages": [
    {"id":"intake","label":"Intake & permissions","order":1,"status":"in_progress","skill":"audit","steps":[
      {"id":"target","label":"Confirm target URL","status":"in_progress"},
      {"id":"permission","label":"Set permission boundary","status":"pending"}
    ]},
    {"id":"surface-discovery","label":"Web surface map","order":2,"status":"pending","skill":"audit","steps":[{"id":"routes","label":"List routes & CTAs","status":"pending"}]},
    {"id":"source-pass","label":"Source evidence","order":3,"status":"pending","skill":"audit","steps":[{"id":"claims","label":"Collect claims","status":"pending"}]},
    {"id":"feature-inventory","label":"Feature inventory","order":4,"status":"pending","skill":"audit","steps":[{"id":"inventory","label":"Build feature table","status":"pending"}]},
    {"id":"live-functional","label":"Live functional test","order":5,"status":"pending","skill":"flow-test","steps":[
      {"id":"homepage-load","label":"Homepage load","status":"pending"},
      {"id":"cta-primary","label":"Primary CTA","status":"pending"},
      {"id":"lead-form","label":"Lead form","status":"pending"}
    ]},
    {"id":"visual-qa","label":"Visual QA","order":6,"status":"pending","skill":"visual-qa","steps":[{"id":"viewport-desktop","label":"Desktop viewport","status":"pending"}]},
    {"id":"deploy-check","label":"Deployment readiness","order":7,"status":"pending","skill":"deploy-check","steps":[{"id":"env-deps","label":"Env & deps","status":"pending"}]},
    {"id":"synthesis","label":"Report synthesis","order":8,"status":"pending","skill":"audit","steps":[{"id":"issue-cards","label":"Issue cards","status":"pending"}]},
    {"id":"accept-five","label":"Five-pass (optional)","order":9,"status":"pending","skill":"accept-five","steps":[{"id":"pass-1","label":"Baseline pass","status":"pending"}]}
  ],
  "findingsPreview": [],
  "eventsPath": "validation/artifacts/$RUN_ID/run-events.ndjson",
  "reportPath": null,
  "updatedAt": "$(date -u +%Y-%m-%dT%H:%M:%SZ)"
}
EOF

echo '{"ts":"'"$(date -u +%Y-%m-%dT%H:%M:%SZ)"'","type":"run_started","runId":"'"$RUN_ID"'","targetUrl":"'"$URL"'"}' > "$RUN_DIR/run-events.ndjson"

echo "RUN_ID=$RUN_ID"
echo "RUN_DIR=$RUN_DIR"
echo "STATE_URL=workbench/live/?state=validation/artifacts/$RUN_ID/run-state.json"
echo "STATE_HTTP_URL=http://127.0.0.1:8765/validation/artifacts/$RUN_ID/run-state.json"
echo "BROWSER_EXT=Load browser-extension/ unpacked; paste STATE_HTTP_URL in extension popup"
echo "REPORT_PATH=validation/artifacts/$RUN_ID/audit-report.json"
echo "Start server: python3 -m http.server 8765  # then open the STATE_URL path"
echo "After audit: python3 scripts/audit_report_merge_run.py --run-dir validation/artifacts/$RUN_ID --merge-preview"
