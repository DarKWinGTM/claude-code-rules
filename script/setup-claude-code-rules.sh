#!/usr/bin/env bash
set -euo pipefail

usage() {
  cat <<'EOF'
Usage:
  setup-claude-code-rules.sh [--project-root <path>] [--source-repo <path>] [--repo-url <url>] [--ref <git-ref>]

Installs the current active Claude Code runtime rules into <project-root>/.claude/rules/
using owner-aware manifest cleanup.
EOF
}

project_root="${PWD}"
source_repo=""
repo_url="https://github.com/DarKWinGTM/claude-code-rules.git"
ref=""
cloned_repo_dir=""
legacy_backup_run_dir=""

while [ "$#" -gt 0 ]; do
  case "$1" in
    --project-root)
      project_root="$2"
      shift 2
      ;;
    --source-repo)
      source_repo="$2"
      shift 2
      ;;
    --repo-url)
      repo_url="$2"
      shift 2
      ;;
    --ref)
      ref="$2"
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

if [ ! -d "$project_root" ]; then
  echo "Project root does not exist: $project_root" >&2
  exit 1
fi
project_root="$(cd "$project_root" && pwd -P)"

cleanup() {
  if [ -n "$cloned_repo_dir" ] && [ -d "$cloned_repo_dir" ]; then
    rm -rf "$cloned_repo_dir"
  fi
}
trap cleanup EXIT

if [ -n "$source_repo" ]; then
  if [ ! -d "$source_repo" ]; then
    echo "Source repo does not exist: $source_repo" >&2
    exit 1
  fi
  source_repo="$(cd "$source_repo" && pwd -P)"
else
  if [ -n "${BASH_SOURCE[0]:-}" ] && [ -f "${BASH_SOURCE[0]}" ]; then
    script_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd -P)"
    candidate_repo="$(cd "$script_dir/.." && pwd -P)"
    if [ -f "$candidate_repo/README.md" ] && [ -f "$candidate_repo/accurate-communication.md" ]; then
      source_repo="$candidate_repo"
    fi
  fi

  if [ -z "$source_repo" ]; then
    cloned_repo_dir="$(mktemp -d)"
    git clone "$repo_url" "$cloned_repo_dir/claude-code-rules" >/dev/null
    source_repo="$cloned_repo_dir/claude-code-rules"
    if [ -n "$ref" ]; then
      git -C "$source_repo" checkout "$ref" >/dev/null
    fi
  fi
fi

if [ ! -f "$source_repo/README.md" ] || [ ! -f "$source_repo/accurate-communication.md" ]; then
  echo "Source repo does not look like claude-code-rules: $source_repo" >&2
  exit 1
fi

rules_dir="$project_root/.claude/rules"
mkdir -p "$rules_dir"

manifest_path="$rules_dir/.claude-code-rules-manifest.tsv"
legacy_backup_root="$rules_dir/.claude-code-rules-legacy-backup"

active_rule_files=(
  accurate-communication.md
  action-safety.md
  audience-surface-disclosure-control.md
  authority-and-scope.md
  coding-discipline.md
  communication-register.md
  document-governance.md
  document-integrity.md
  evidence-discipline.md
  execution-and-goal-frame.md
  explanation-and-presentation.md
  external-verification-and-source-trust.md
  memory-governance-and-session-boundary.md
  phase-todo-artifact.md
  portable-implementation-and-hardcoding-control.md
  refusal-and-recovery.md
  safe-io.md
  worker-routing-and-context.md
)

legacy_candidate_files=(
  anti-mockup.md
  anti-sycophancy.md
  context-load-and-document-density-control.md
  custom-agent-selection-priority.md
  dan-safe-normalization.md
  development-verification-and-debug-strategy.md
  document-changelog-control.md
  document-consistency.md
  document-design-control.md
  document-patch-control.md
  emergency-protocol.md
  evidence-grounded-burden-of-proof.md
  execution-continuity-and-mode-selection.md
  explanation-quality.md
  flow-diagram-no-frame.md
  functional-intent-verification.md
  goal-set-review-and-priority-balance.md
  governed-document-rollover-control.md
  high-signal-communication.md
  maintainable-code-structure-and-decomposition.md
  native-worker-agent-routing-and-context-control.md
  natural-professional-communication.md
  no-variable-guessing.md
  operational-failure-handling.md
  phase-implementation.md
  project-documentation-standards.md
  recovery-contract.md
  refusal-classification.md
  refusal-minimization.md
  response-closing-and-action-framing.md
  runtime-topology-control.md
  safe-file-reading.md
  safe-terminal-output.md
  strict-file-hygiene.md
  tactical-strategic-programming.md
  technical-snapshot-communication.md
  todo-standards.md
  unified-version-control-system.md
  zero-hallucination.md
  answer-presentation.md
  artifact-initiation-control.md
)

hash_file() {
  if command -v sha256sum >/dev/null 2>&1; then
    sha256sum "$1" | awk '{print $1}'
  elif command -v shasum >/dev/null 2>&1; then
    shasum -a 256 "$1" | awk '{print $1}'
  elif command -v openssl >/dev/null 2>&1; then
    openssl dgst -sha256 "$1" | awk '{print $NF}'
  else
    echo "No SHA-256 tool available." >&2
    return 1
  fi
}

git_blob_hash() {
  git hash-object -- "$1" 2>/dev/null || true
}

is_active_rule() {
  local needle="$1"
  local item
  for item in "${active_rule_files[@]}"; do
    if [ "$item" = "$needle" ]; then
      return 0
    fi
  done
  return 1
}

ensure_legacy_backup_dir() {
  if [ -z "$legacy_backup_run_dir" ]; then
    legacy_backup_run_dir="$legacy_backup_root/$(date +%Y%m%d-%H%M%S)"
    mkdir -p "$legacy_backup_run_dir"
  fi
}

quarantine_legacy_file() {
  local file="$1"
  local target="$2"
  ensure_legacy_backup_dir
  mv "$target" "$legacy_backup_run_dir/$file"
  printf 'Quarantined legacy claude-code-rules file %s -> %s\n' "$file" "$legacy_backup_run_dir/$file" >&2
}

repo_has_historical_blob() {
  local file="$1"
  local current_blob="$2"
  local commit historical_blob
  [ -n "$current_blob" ] || return 1
  while IFS= read -r commit; do
    historical_blob="$(git -C "$source_repo" rev-parse "$commit:$file" 2>/dev/null || true)"
    if [ -n "$historical_blob" ] && [ "$historical_blob" = "$current_blob" ]; then
      return 0
    fi
  done < <(git -C "$source_repo" rev-list --all -- "$file" 2>/dev/null)
  return 1
}

if [ -f "$manifest_path" ]; then
  while IFS=$'\t' read -r file recorded_sha256 recorded_blob; do
    [ -n "$file" ] || continue
    if is_active_rule "$file"; then
      continue
    fi
    target="$rules_dir/$file"
    if [ -f "$target" ]; then
      current_sha256="$(hash_file "$target" || true)"
      current_blob="$(git_blob_hash "$target")"
      manifest_match=0
      if [ -n "$recorded_blob" ]; then
        [ "$current_blob" = "$recorded_blob" ] && manifest_match=1
      elif [ -n "$recorded_sha256" ]; then
        [ "$current_sha256" = "$recorded_sha256" ] && manifest_match=1
      fi
      if [ "$manifest_match" -eq 1 ]; then
        rm -f "$target"
      else
        printf 'Skipping manifest cleanup for %s because it no longer matches the previous claude-code-rules install snapshot.\n' "$file" >&2
      fi
    fi
  done < "$manifest_path"
fi

for file in "${legacy_candidate_files[@]}"; do
  if is_active_rule "$file"; then
    continue
  fi
  target="$rules_dir/$file"
  if [ -f "$target" ]; then
    current_blob="$(git_blob_hash "$target")"
    if repo_has_historical_blob "$file" "$current_blob"; then
      quarantine_legacy_file "$file" "$target"
    fi
  fi
done

tmp_manifest="$(mktemp)"
trap 'rm -f "$tmp_manifest"; cleanup' EXIT

for file in "${active_rule_files[@]}"; do
  cp "$source_repo/$file" "$rules_dir/$file"
  printf '%s\t%s\t%s\n' "$file" "$(hash_file "$rules_dir/$file")" "$(git_blob_hash "$rules_dir/$file")" >> "$tmp_manifest"
done

mv "$tmp_manifest" "$manifest_path"
trap cleanup EXIT

printf 'Installed %s active Claude Code rules into %s\n' "${#active_rule_files[@]}" "$rules_dir"
printf 'Manifest: %s\n' "$manifest_path"
