#!/usr/bin/env bash
set -euo pipefail

INPUT=$(cat)
DATA_DIR="${CLAUDE_PLUGIN_DATA:-}"

if [ -z "$DATA_DIR" ]; then
  exit 0
fi

mkdir -p "$DATA_DIR/compact"
printf '%s\n' "$INPUT" > "$DATA_DIR/compact/last-precompact.json"
