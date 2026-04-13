#!/usr/bin/env bash
set -euo pipefail

COMPACT_STATE_TTL_SECONDS=3600

compact_data_dir() {
  if [ -z "${CLAUDE_PLUGIN_DATA:-}" ]; then
    return 1
  fi

  printf '%s/compact\n' "$CLAUDE_PLUGIN_DATA"
}

ensure_compact_data_dir() {
  local compact_dir
  compact_dir="$(compact_data_dir)" || return 1
  mkdir -p "$compact_dir"
  printf '%s\n' "$compact_dir"
}

sessions_root_dir() {
  local compact_dir
  compact_dir="$(compact_data_dir)" || return 1
  printf '%s/sessions\n' "$compact_dir"
}

ensure_sessions_root_dir() {
  local sessions_dir
  sessions_dir="$(sessions_root_dir)" || return 1
  mkdir -p "$sessions_dir"
  printf '%s\n' "$sessions_dir"
}

session_dir_path() {
  local session_id="$1"
  local sessions_dir
  sessions_dir="$(sessions_root_dir)" || return 1
  printf '%s/%s\n' "$sessions_dir" "$session_id"
}

ensure_session_dir() {
  local session_id="$1"
  local session_dir
  session_dir="$(session_dir_path "$session_id")" || return 1
  mkdir -p "$session_dir"
  printf '%s\n' "$session_dir"
}

pending_path() {
  local session_id="$1"
  local session_dir
  session_dir="$(session_dir_path "$session_id")" || return 1
  printf '%s/pending.json\n' "$session_dir"
}

precompact_context_path() {
  local session_id="$1"
  local session_dir
  session_dir="$(session_dir_path "$session_id")" || return 1
  printf '%s/precompact-context.json\n' "$session_dir"
}

carry_forward_selected_path() {
  local session_id="$1"
  local session_dir
  session_dir="$(session_dir_path "$session_id")" || return 1
  printf '%s/carry-forward-selected.json\n' "$session_dir"
}

sessionstart_proof_path() {
  local session_id="$1"
  local session_dir
  session_dir="$(session_dir_path "$session_id")" || return 1
  printf '%s/sessionstart-proof.json\n' "$session_dir"
}

sessionstart_directive_path() {
  local session_id="$1"
  local session_dir
  session_dir="$(session_dir_path "$session_id")" || return 1
  printf '%s/sessionstart-directive.json\n' "$session_dir"
}

index_path() {
  local compact_dir
  compact_dir="$(compact_data_dir)" || return 1
  printf '%s/index.json\n' "$compact_dir"
}

remove_legacy_compact_files() {
  local compact_dir
  compact_dir="$(compact_data_dir)" || return 0

  rm -f \
    "$compact_dir/active-handoff.json" \
    "$compact_dir/last-sessionstart-consumed.json" \
    "$compact_dir/last-precompact.json" \
    "$compact_dir/last-postcompact.json" \
    "$compact_dir/last-sessionstart-compact.json"
}

iso_now_utc() {
  python3 - <<'PY'
import datetime as dt
print(dt.datetime.now(dt.timezone.utc).isoformat().replace('+00:00', 'Z'))
PY
}

iso_plus_ttl_utc() {
  python3 - "$COMPACT_STATE_TTL_SECONDS" <<'PY'
import datetime as dt
import sys
seconds = int(sys.argv[1])
print((dt.datetime.now(dt.timezone.utc) + dt.timedelta(seconds=seconds)).isoformat().replace('+00:00', 'Z'))
PY
}

transcript_path_for_session() {
  local session_id="$1"
  printf '/home/node/.claude/projects/-home-node-workplace-AWCLOUD-CLAUDE/%s.jsonl\n' "$session_id"
}

extract_precompact_context() {
  local session_id="$1"
  local transcript_path
  transcript_path="$(transcript_path_for_session "$session_id")"

  python3 - "$session_id" "$transcript_path" <<'PY'
import json
import pathlib
import sys

session_id = sys.argv[1]
transcript_path = pathlib.Path(sys.argv[2])

result = {
    "activeObjective": None,
    "governingBasis": None,
    "activeFrame": None,
    "selectedCarryForwardItems": [],
    "needsRecheckItems": [],
}

if not transcript_path.exists():
    print(json.dumps(result, ensure_ascii=False))
    raise SystemExit(0)

reject_prefixes = (
    "Base directory for this skill:",
    "Plan file referenced",
    "Skills restored",
    "SessionStart:compact says:",
    "[Request interrupted by user]",
)
reject_substrings = (
    "tool_result",
    "hookSpecificOutput",
    "memsearch",
    "frontend-review",
    ".claude/plugins/cache/",
)

text_candidates = []
for line in transcript_path.read_text(encoding="utf-8").splitlines():
    try:
        obj = json.loads(line)
    except Exception:
        continue
    if obj.get("sessionId") != session_id:
        continue
    if obj.get("type") != "user":
        continue
    message = obj.get("message", {})
    content = message.get("content", [])
    if not isinstance(content, list):
        continue
    for block in content:
        if not isinstance(block, dict):
            continue
        if block.get("type") != "text":
            continue
        text = (block.get("text") or "").strip()
        if not text:
            continue
        if text.startswith(reject_prefixes):
            continue
        lowered = text.lower()
        if any(token.lower() in lowered for token in reject_substrings):
            continue
        if len(text) < 12:
            continue
        text_candidates.append(text)

if text_candidates:
    latest = text_candidates[-1][:400]
    result["activeObjective"] = latest
    result["selectedCarryForwardItems"].append(latest)
else:
    result["needsRecheckItems"].append(
        "Current objective could not be extracted cleanly from the pre-compact transcript and should be rechecked."
    )

print(json.dumps(result, ensure_ascii=False))
PY
}

write_json_file() {
  local target_path="$1"
  local json_payload="$2"
  JSON_PAYLOAD="$json_payload" python3 - "$target_path" <<'PY'
import json
import os
import pathlib
import sys
payload = json.loads(os.environ.get('JSON_PAYLOAD', '{}'))
path = pathlib.Path(sys.argv[1])
path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
PY
}

create_session_state_from_input() {
  local input="$1"

  RAW_INPUT="$input" python3 - "$COMPACT_STATE_TTL_SECONDS" <<'PY'
import datetime as dt
import json
import os
import sys

raw = os.environ.get("RAW_INPUT", "")
ttl_seconds = int(sys.argv[1])
now = dt.datetime.now(dt.timezone.utc)
expires = now + dt.timedelta(seconds=ttl_seconds)

try:
    event = json.loads(raw) if raw.strip() else {}
except Exception:
    event = {}

payload = {
    "sourceSessionId": event.get("session_id"),
    "trigger": event.get("trigger"),
    "createdAt": now.isoformat().replace("+00:00", "Z"),
    "expiresAt": expires.isoformat().replace("+00:00", "Z"),
    "cwd": event.get("cwd"),
}
print(json.dumps(payload, ensure_ascii=False))
PY
}

write_precompact_session_files() {
  local session_state_json="$1"
  local source_session_id

  source_session_id="$(SESSION_STATE_JSON="$session_state_json" python3 - <<'PY'
import json,os
payload=json.loads(os.environ.get('SESSION_STATE_JSON', '{}'))
print(payload.get('sourceSessionId') or '')
PY
)"

  if [ -z "$source_session_id" ]; then
    return 1
  fi

  ensure_compact_data_dir >/dev/null || return 0
  ensure_sessions_root_dir >/dev/null || return 0
  ensure_session_dir "$source_session_id" >/dev/null || return 0

  local precompact_context_json
  precompact_context_json="$(python3 - "$source_session_id" <<'PY'
import json
import sys
from subprocess import check_output
session_id = sys.argv[1]
PY
)"

  precompact_context_json="$(extract_precompact_context "$source_session_id")"

  local pending_json
  pending_json="$(SESSION_STATE_JSON="$session_state_json" python3 - <<'PY'
import json,os
payload=json.loads(os.environ.get('SESSION_STATE_JSON', '{}'))
out={
  'schema': 'claude-code-rules/pending@1',
  'sourceSessionId': payload.get('sourceSessionId'),
  'createdAt': payload.get('createdAt'),
  'pendingUntil': payload.get('expiresAt'),
  'trigger': payload.get('trigger'),
  'cwd': payload.get('cwd'),
}
print(json.dumps(out, ensure_ascii=False))
PY
)"

  local transcript_path
  transcript_path="$(transcript_path_for_session "$source_session_id")"

  local precompact_json
  precompact_json="$(PRECOMPACT_CONTEXT_JSON="$precompact_context_json" python3 - "$source_session_id" "$transcript_path" <<'PY'
import json,os,sys
session_id=sys.argv[1]
transcript_path=sys.argv[2]
ctx=json.loads(os.environ.get('PRECOMPACT_CONTEXT_JSON', '{}'))
out={
  'schema': 'claude-code-rules/precompact-context@1',
  'sourceSessionId': session_id,
  'transcriptPath': transcript_path,
  'activeObjective': ctx.get('activeObjective'),
  'governingBasis': ctx.get('governingBasis'),
  'activeFrame': ctx.get('activeFrame'),
  'selectedCarryForwardItems': ctx.get('selectedCarryForwardItems', []),
  'needsRecheckItems': ctx.get('needsRecheckItems', []),
}
print(json.dumps(out, ensure_ascii=False))
PY
)"

  local carry_forward_json
  carry_forward_json="$(PRECOMPACT_JSON="$precompact_json" python3 - <<'PY'
import json,os
ctx=json.loads(os.environ.get('PRECOMPACT_JSON', '{}'))
out={
  'schema': 'claude-code-rules/carry-forward-selected@1',
  'sourceSessionId': ctx.get('sourceSessionId'),
  'derivedFrom': 'precompact-context.json',
  'inject': {
    'activeObjective': ctx.get('activeObjective'),
    'governingBasis': ctx.get('governingBasis'),
    'activeFrame': ctx.get('activeFrame'),
    'selectedCarryForwardItems': ctx.get('selectedCarryForwardItems', []),
    'needsRecheckItems': ctx.get('needsRecheckItems', []),
  }
}
print(json.dumps(out, ensure_ascii=False))
PY
)"

  write_json_file "$(pending_path "$source_session_id")" "$pending_json"
  write_json_file "$(precompact_context_path "$source_session_id")" "$precompact_json"
  write_json_file "$(carry_forward_selected_path "$source_session_id")" "$carry_forward_json"

  rewrite_index
  printf '%s\n' "$source_session_id"
}

mark_session_consumed_in_index() {
  local source_session_id="$1"
  local resume_session_id="$2"
  local consumed_at
  consumed_at="$(iso_now_utc)"
  local cleanup_after
  cleanup_after="$(iso_plus_ttl_utc)"

  python3 - "$(index_path)" "$source_session_id" "$resume_session_id" "$consumed_at" "$cleanup_after" <<'PY'
import json
import pathlib
import sys
path = pathlib.Path(sys.argv[1])
source_session_id = sys.argv[2]
resume_session_id = sys.argv[3]
consumed_at = sys.argv[4]
cleanup_after = sys.argv[5]
index = {'sessions': []}
if path.exists():
    try:
        index = json.loads(path.read_text(encoding='utf-8'))
    except Exception:
        index = {'sessions': []}
entries = []
for entry in index.get('sessions', []):
    if entry.get('sourceSessionId') == source_session_id:
        entry['state'] = 'consumed'
        entry['resumeSessionId'] = resume_session_id or None
        entry['consumedAt'] = consumed_at
        entry['cleanupAfter'] = cleanup_after
    entries.append(entry)
path.write_text(json.dumps({'sessions': entries}, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
PY
}

record_sessionstart_proof() {
  local source_session_id="$1"
  local sessionstart_input="$2"
  local status="$3"
  local reason="$4"

  ensure_compact_data_dir >/dev/null || return 0
  ensure_sessions_root_dir >/dev/null || return 0
  ensure_session_dir "$source_session_id" >/dev/null || return 0

  local proof_path
  proof_path="$(sessionstart_proof_path "$source_session_id")"

  SESSIONSTART_INPUT="$sessionstart_input" python3 - "$proof_path" "$COMPACT_STATE_TTL_SECONDS" "$source_session_id" "$status" "$reason" <<'PY'
import datetime as dt
import json
import os
import pathlib
import sys

path = pathlib.Path(sys.argv[1])
ttl_seconds = int(sys.argv[2])
source_session_id = sys.argv[3]
status = sys.argv[4]
reason = sys.argv[5]
now = dt.datetime.now(dt.timezone.utc)
expires = now + dt.timedelta(seconds=ttl_seconds)

try:
    sessionstart_event = json.loads(os.environ.get('SESSIONSTART_INPUT', '') or '{}')
except Exception:
    sessionstart_event = {}

proof = {
    'schema': 'claude-code-rules/sessionstart-proof@1',
    'sourceSessionId': source_session_id,
    'consumedAt': now.isoformat().replace('+00:00', 'Z'),
    'expiresAt': expires.isoformat().replace('+00:00', 'Z'),
    'hookEventName': 'SessionStart',
    'sessionStartSessionId': sessionstart_event.get('session_id'),
    'source': sessionstart_event.get('source'),
    'outputChannels': ['systemMessage', 'hookSpecificOutput.additionalContext'] if status == 'consumed' else ['hookSpecificOutput.additionalContext'],
    'status': status,
    'reason': reason,
}

path.write_text(json.dumps(proof, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
PY
}

record_sessionstart_directive() {
  local source_session_id="$1"
  local resume_session_id="$2"
  local status_line="$3"
  local directive_text="$4"
  local directive_mode="$5"
  local objective_status="$6"
  local carry_count="$7"
  local recheck_count="$8"
  local review_root="$9"
  local review_target="${10}"
  local review_dir="${11}"
  local precompact_file="${12}"
  local carry_forward_file="${13}"
  local proof_file="${14}"

  ensure_compact_data_dir >/dev/null || return 0
  ensure_sessions_root_dir >/dev/null || return 0
  ensure_session_dir "$source_session_id" >/dev/null || return 0

  local directive_path
  directive_path="$(sessionstart_directive_path "$source_session_id")"

  DIRECTIVE_TEXT="$directive_text" STATUS_LINE="$status_line" python3 - "$directive_path" "$COMPACT_STATE_TTL_SECONDS" "$source_session_id" "$resume_session_id" "$directive_mode" "$objective_status" "$carry_count" "$recheck_count" "$review_root" "$review_target" "$review_dir" "$precompact_file" "$carry_forward_file" "$proof_file" <<'PY'
import datetime as dt
import json
import os
import pathlib
import sys

path = pathlib.Path(sys.argv[1])
ttl_seconds = int(sys.argv[2])
source_session_id = sys.argv[3]
resume_session_id = sys.argv[4] or None
directive_mode = sys.argv[5]
objective_status = sys.argv[6]
carry_count = int(sys.argv[7])
recheck_count = int(sys.argv[8])
review_root = sys.argv[9]
review_target = sys.argv[10]
review_dir = sys.argv[11]
precompact_file = sys.argv[12]
carry_forward_file = sys.argv[13]
proof_file = sys.argv[14]
now = dt.datetime.now(dt.timezone.utc)
expires = now + dt.timedelta(seconds=ttl_seconds)
directive_text = os.environ.get('DIRECTIVE_TEXT', '')
status_line = os.environ.get('STATUS_LINE', '')
review_files = [item for item in (precompact_file, carry_forward_file, proof_file) if item]

directive = {
    'schema': 'claude-code-rules/sessionstart-directive@1',
    'sourceSessionId': source_session_id,
    'resumeSessionId': resume_session_id,
    'generatedAt': now.isoformat().replace('+00:00', 'Z'),
    'expiresAt': expires.isoformat().replace('+00:00', 'Z'),
    'directiveMode': directive_mode,
    'reviewRequired': True,
    'objectiveStatus': objective_status,
    'carryCount': carry_count,
    'recheckCount': recheck_count,
    'reviewRoot': review_root or None,
    'reviewTarget': review_target or None,
    'reviewSourceDirectory': review_dir or None,
    'reviewFiles': review_files,
    'systemMessage': status_line or None,
    'directiveText': directive_text,
}

path.write_text(json.dumps(directive, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
PY
}

rewrite_index() {
  local compact_dir
  compact_dir="$(ensure_compact_data_dir)" || return 0
  local sessions_dir
  sessions_dir="$(ensure_sessions_root_dir)" || return 0
  local index_file
  index_file="$(index_path)" || return 0

  python3 - "$sessions_dir" "$index_file" <<'PY'
import json
import pathlib
import sys

sessions_dir = pathlib.Path(sys.argv[1])
index_file = pathlib.Path(sys.argv[2])
entries = []

for session_dir in sorted(sessions_dir.iterdir()) if sessions_dir.exists() else []:
    if not session_dir.is_dir():
        continue
    pending = session_dir / 'pending.json'
    proof = session_dir / 'sessionstart-proof.json'
    entry = {
        'sourceSessionId': session_dir.name,
        'state': 'cleanable',
        'hasPending': pending.exists(),
        'hasCarryForward': (session_dir / 'carry-forward-selected.json').exists(),
        'hasProof': proof.exists(),
        'hasDirective': (session_dir / 'sessionstart-directive.json').exists(),
    }
    if pending.exists():
        try:
            data = json.loads(pending.read_text(encoding='utf-8'))
            entry['state'] = 'pending'
            entry['createdAt'] = data.get('createdAt')
            entry['pendingUntil'] = data.get('pendingUntil')
            entry['trigger'] = data.get('trigger')
            entry['cwd'] = data.get('cwd')
        except Exception:
            entry['state'] = 'cleanable'
    elif proof.exists():
        try:
            data = json.loads(proof.read_text(encoding='utf-8'))
            entry['state'] = data.get('status') or 'consumed'
            entry['consumedAt'] = data.get('consumedAt')
            entry['cleanupAfter'] = data.get('expiresAt')
            entry['resumeSessionId'] = data.get('sessionStartSessionId')
        except Exception:
            entry['state'] = 'cleanable'
    entries.append(entry)

index_file.write_text(json.dumps({'sessions': entries}, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
PY
}

prune_expired_session_dirs() {
  local sessions_dir
  sessions_dir="$(sessions_root_dir)" || return 0
  if [ ! -d "$sessions_dir" ]; then
    return 0
  fi

  python3 - "$sessions_dir" <<'PY'
import datetime as dt
import json
import pathlib
import shutil
import sys

sessions_dir = pathlib.Path(sys.argv[1])
now = dt.datetime.now(dt.timezone.utc)

for session_dir in sessions_dir.iterdir():
    if not session_dir.is_dir():
        continue

    pending = session_dir / 'pending.json'
    proof = session_dir / 'sessionstart-proof.json'

    expired = False
    if pending.exists():
        try:
            data = json.loads(pending.read_text(encoding='utf-8'))
            ts = data.get('pendingUntil')
            expired = not ts or dt.datetime.fromisoformat(ts.replace('Z', '+00:00')) <= now
        except Exception:
            expired = True
    elif proof.exists():
        try:
            data = json.loads(proof.read_text(encoding='utf-8'))
            ts = data.get('expiresAt')
            expired = not ts or dt.datetime.fromisoformat(ts.replace('Z', '+00:00')) <= now
        except Exception:
            expired = True
    else:
        expired = True

    if expired:
        shutil.rmtree(session_dir, ignore_errors=True)
PY
}

prune_compact_state() {
  remove_legacy_compact_files
  prune_expired_session_dirs
  rewrite_index
}

resolve_matching_pending_source_session() {
  local input="$1"
  local index_file
  index_file="$(index_path)" || return 1
  if [ ! -f "$index_file" ]; then
    return 1
  fi

  SESSIONSTART_INPUT="$input" python3 - "$index_file" <<'PY'
import json
import os
import pathlib
import sys

path = pathlib.Path(sys.argv[1])
try:
    index = json.loads(path.read_text(encoding='utf-8'))
except Exception:
    raise SystemExit(1)

try:
    sessionstart_event = json.loads(os.environ.get('SESSIONSTART_INPUT', '') or '{}')
except Exception:
    sessionstart_event = {}

session_id = sessionstart_event.get('session_id')
source = sessionstart_event.get('source')
if not session_id or source != 'compact':
    raise SystemExit(1)

pending = [
    entry for entry in index.get('sessions', [])
    if entry.get('state') == 'pending' and entry.get('sourceSessionId') == session_id
]
if len(pending) != 1:
    raise SystemExit(1)

print(session_id)
PY
}

load_selected_carry_forward() {
  local source_session_id="$1"
  local file
  file="$(carry_forward_selected_path "$source_session_id")" || return 1
  if [ ! -f "$file" ]; then
    return 1
  fi
  cat "$file"
}

delete_pending_for_session() {
  local source_session_id="$1"
  local file
  file="$(pending_path "$source_session_id")" || return 0
  rm -f "$file"
}
