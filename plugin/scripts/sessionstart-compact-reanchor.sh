#!/usr/bin/env bash
set -euo pipefail

INPUT=$(cat)
DATA_DIR="${CLAUDE_PLUGIN_DATA:-}"

if [ -n "$DATA_DIR" ]; then
  mkdir -p "$DATA_DIR/compact"
  printf '%s\n' "$INPUT" > "$DATA_DIR/compact/last-sessionstart-compact.json"
fi

python3 - <<'PY'
import json
message = (
    "Post-compact reminder from rules-compact-extension: re-anchor to the active objective before continuing. "
    "Preserve the latest user-selected governing basis and active frame. "
    "Treat compressed carry-forward detail as needs-recheck when exact wording, exact payloads, or exact checked scope materially matter. "
    "Continue directly only after separating carried-forward facts from needs-recheck details."
)
print(json.dumps({
    "hookSpecificOutput": {
        "hookEventName": "SessionStart",
        "additionalContext": message,
    }
}))
PY
