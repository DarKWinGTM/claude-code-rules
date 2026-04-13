#!/usr/bin/env bash
set -euo pipefail

cat >/dev/null

source "${CLAUDE_PLUGIN_ROOT}/scripts/compact-handoff-common.sh"

prune_compact_state
