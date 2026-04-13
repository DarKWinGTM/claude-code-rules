#!/usr/bin/env bash
set -euo pipefail

INPUT=$(cat)

source "${CLAUDE_PLUGIN_ROOT}/scripts/compact-handoff-common.sh"

prune_compact_state

session_state_json="$(create_session_state_from_input "$INPUT")"
write_precompact_session_files "$session_state_json" >/dev/null || exit 0
