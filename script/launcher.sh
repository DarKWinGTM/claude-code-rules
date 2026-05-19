#!/usr/bin/env bash
set -euo pipefail

usage() {
  cat <<'EOF'
Usage:
  launcher.sh [--project-root <path>]

Primary operator path for Claude Code project-local RULES install.
- Run from a cloned RULES repo.
- Dispatches to script/setup-claude-code-rules.sh.
- Installs into <project-root>/.claude/rules/.

If --project-root is omitted:
- when run outside the RULES repo root, the current directory is used
- when run from the RULES repo root, an explicit --project-root is required
EOF
}

script_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd -P)"
repo_root="$(cd "$script_dir/.." && pwd -P)"
helper="$repo_root/script/setup-claude-code-rules.sh"
project_root=""

while [ "$#" -gt 0 ]; do
  case "$1" in
    --project-root)
      project_root="$2"
      shift 2
      ;;
    -h|--help)
      usage
      exit 0
      ;;
    *)
      echo "Unknown argument: $1" >&2
      usage >&2
      exit 1
      ;;
  esac
done

if [ ! -x "$helper" ]; then
  echo "Helper script is missing or not executable: $helper" >&2
  exit 1
fi

if [ -z "$project_root" ]; then
  current_dir="$(pwd -P)"
  if [ "$current_dir" = "$repo_root" ]; then
    echo "When running launcher from the RULES repo root, pass --project-root <target-project>." >&2
    exit 1
  fi
  project_root="$current_dir"
fi

exec "$helper" --project-root "$project_root" --source-repo "$repo_root"
