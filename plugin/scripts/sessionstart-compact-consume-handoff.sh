#!/usr/bin/env bash
set -euo pipefail

INPUT=$(cat)

source "${CLAUDE_PLUGIN_ROOT}/scripts/compact-handoff-common.sh"

prune_compact_state

status_line=""
compact_root="$(compact_data_dir 2>/dev/null || true)"
review_index_path="$(index_path 2>/dev/null || true)"
directive_text=""
directive_mode="fallback-review-required"
objective_status="needs-recheck"
carry_count="0"
recheck_count="0"
review_target="index.json"
review_dir=""
precompact_file=""
carry_forward_file=""
proof_file=""
resume_session_id=""
source_session_id=""
carry_forward_json=""

if source_session_id="$(resolve_matching_pending_source_session "$INPUT" 2>/dev/null)"; then
  if [ -n "$source_session_id" ] && carry_forward_json="$(load_selected_carry_forward "$source_session_id" 2>/dev/null)"; then
    delete_pending_for_session "$source_session_id"
    record_sessionstart_proof "$source_session_id" "$INPUT" "consumed" "exact_session_id_match" >/dev/null

    resume_session_id="$(SESSIONSTART_INPUT_JSON="$INPUT" python3 - <<'PY'
import json,os
try:
    data=json.loads(os.environ.get('SESSIONSTART_INPUT_JSON', '{}'))
except Exception:
    data={}
print(data.get('session_id') or '')
PY
)"
    mark_session_consumed_in_index "$source_session_id" "$resume_session_id"
    rewrite_index

    review_dir="$(session_dir_path "$source_session_id" 2>/dev/null || true)"
    precompact_file="$(precompact_context_path "$source_session_id" 2>/dev/null || true)"
    carry_forward_file="$(carry_forward_selected_path "$source_session_id" 2>/dev/null || true)"
    proof_file="$(sessionstart_proof_path "$source_session_id" 2>/dev/null || true)"
    review_target="sessions/${source_session_id}/"

    parsed_state="$(CARRY_FORWARD_JSON="$carry_forward_json" python3 - <<'PY'
import json,os
payload=json.loads(os.environ.get('CARRY_FORWARD_JSON', '{}'))
inject=payload.get('inject', {})
objective_state = 'available' if inject.get('activeObjective') else 'needs-recheck'
carry_count = len(inject.get('selectedCarryForwardItems') or [])
recheck_count = len(inject.get('needsRecheckItems') or [])
print(json.dumps({
    'objectiveStatus': objective_state,
    'carryCount': carry_count,
    'recheckCount': recheck_count,
}, ensure_ascii=False))
PY
)"

    objective_status="$(PARSED_STATE_JSON="$parsed_state" python3 - <<'PY'
import json,os
print(json.loads(os.environ['PARSED_STATE_JSON']).get('objectiveStatus', 'needs-recheck'))
PY
)"
    carry_count="$(PARSED_STATE_JSON="$parsed_state" python3 - <<'PY'
import json,os
print(json.loads(os.environ['PARSED_STATE_JSON']).get('carryCount', 0))
PY
)"
    recheck_count="$(PARSED_STATE_JSON="$parsed_state" python3 - <<'PY'
import json,os
print(json.loads(os.environ['PARSED_STATE_JSON']).get('recheckCount', 0))
PY
)"

    status_line="[rules-compact-extension] review-required session=${source_session_id} objective=${objective_status} carry=${carry_count} recheck=${recheck_count} reviewRoot=${compact_root} review=${review_target}"
    directive_mode="exact-session-review-required"

    directive_text="$(SOURCE_SESSION_ID="$source_session_id" REVIEW_DIR="$review_dir" PRECOMPACT_FILE="$precompact_file" CARRY_FORWARD_FILE="$carry_forward_file" PROOF_FILE="$proof_file" OBJECTIVE_STATUS="$objective_status" python3 - <<'PY'
import os
source_session_id=os.environ.get('SOURCE_SESSION_ID', '')
review_dir=os.environ.get('REVIEW_DIR', '')
precompact_file=os.environ.get('PRECOMPACT_FILE', '')
carry_forward_file=os.environ.get('CARRY_FORWARD_FILE', '')
proof_file=os.environ.get('PROOF_FILE', '')
objective_status=os.environ.get('OBJECTIVE_STATUS', 'needs-recheck')
parts = [
    f"Review required before continuation for source session {source_session_id}.",
    "Use the stored session files below as references instead of treating carried-forward detail as settled truth.",
]
if review_dir:
    parts.append(f"Review directory: {review_dir}")
files = [path for path in (precompact_file, carry_forward_file, proof_file) if path]
if files:
    parts.append("Review files:\n- " + "\n- ".join(files))
parts.append(f"Objective status: {objective_status}")
parts.append("Review discipline: read the stored files when needed before continuing; do not rely on an injected replay of old context.")
print("\n\n".join(parts))
PY
)"
  fi
fi

if [ -z "$status_line" ]; then
  status_line="[rules-compact-extension] review-required no-exact-session-match objective=needs-recheck carry=0 recheck=0 reviewRoot=${compact_root} review=index.json"
  directive_text="$(COMPACT_ROOT="$compact_root" REVIEW_INDEX_PATH="$review_index_path" python3 - <<'PY'
import os
compact_root=os.environ.get('COMPACT_ROOT', '')
review_index_path=os.environ.get('REVIEW_INDEX_PATH', '')
parts = [
    "Review required before continuation.",
    "No exact pending source session match was resolved for this compact resume.",
    "Use the compact index below as the reference source and re-anchor from verified local context.",
]
if compact_root:
    parts.append(f"Review root: {compact_root}")
if review_index_path:
    parts.append("Review file:\n- " + review_index_path)
parts.append("Objective status: needs-recheck")
parts.append("Review discipline: do not treat any carried-forward detail as settled truth until the correct source session is re-established.")
print("\n\n".join(parts))
PY
)"
fi

record_sessionstart_directive "$source_session_id" "$resume_session_id" "$status_line" "$directive_text" "$directive_mode" "$objective_status" "$carry_count" "$recheck_count" "$compact_root" "$review_target" "$review_dir" "$precompact_file" "$carry_forward_file" "$proof_file" >/dev/null

python3 - "$status_line" "$directive_text" <<'PY'
import json
import sys

status_line = sys.argv[1]
directive_text = sys.argv[2]

output = {
    "hookSpecificOutput": {
        "hookEventName": "SessionStart",
        "additionalContext": directive_text,
    }
}
if status_line:
    output["systemMessage"] = status_line

print(json.dumps(output))
PY
