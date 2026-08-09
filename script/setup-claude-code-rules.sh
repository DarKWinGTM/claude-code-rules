#!/usr/bin/env bash
set -euo pipefail

usage() {
  cat <<'EOF'
Usage:
  setup-claude-code-rules.sh [--project-root <path>] [--source-repo <path>] [--repo-url <url>] [--ref <git-ref>]

Installs the current active Claude Code runtime rules into <project-root>/.claude/rules/
using owner-aware manifest cleanup and execution-disconnected quarantine.
EOF
}

project_root="${PWD}"
source_repo=""
repo_url="https://github.com/DarKWinGTM/claude-code-rules.git"
ref=""
cloned_repo_dir=""
staging_dir=""
quarantine_run_dir=""
quarantine_root_preexisting=0
mutation_started=0
commit_succeeded=0
rolling_back=0
manifest_backed_up=0
manifest_installed=0

manifest_files=()
manifest_sha256s=()
manifest_blobs=()
planned_quarantine_labels=()
planned_quarantine_sources=()
planned_quarantine_names=()
quarantine_moved_sources=()
quarantine_moved_destinations=()
active_backup_files=()
active_installed_files=()

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
      printf 'Unknown argument: %s\n' "$1" >&2
      usage >&2
      exit 1
      ;;
  esac
done

if [ ! -d "$project_root" ]; then
  printf 'Project root does not exist: %s\n' "$project_root" >&2
  exit 1
fi
project_root="$(cd "$project_root" && pwd -P)"

rollback_install() {
  local index file source destination
  [ "$rolling_back" -eq 0 ] || return 0
  rolling_back=1

  if [ "$manifest_installed" -eq 1 ] && { [ -e "$manifest_path" ] || [ -L "$manifest_path" ]; }; then
    rm -f -- "$manifest_path" || true
  fi
  if [ "$manifest_backed_up" -eq 1 ] && [ -f "$staging_dir/manifest-backup.tsv" ]; then
    mv -- "$staging_dir/manifest-backup.tsv" "$manifest_path" || true
  fi

  for ((index=${#active_installed_files[@]}-1; index>=0; index--)); do
    file="${active_installed_files[$index]}"
    rm -f -- "$rules_dir/$file" || true
  done
  for ((index=${#active_backup_files[@]}-1; index>=0; index--)); do
    file="${active_backup_files[$index]}"
    if [ -f "$staging_dir/active-backup/$file" ]; then
      mv -- "$staging_dir/active-backup/$file" "$rules_dir/$file" || true
    fi
  done

  for ((index=${#quarantine_moved_sources[@]}-1; index>=0; index--)); do
    source="${quarantine_moved_sources[$index]}"
    destination="${quarantine_moved_destinations[$index]}"
    if [ -e "$destination" ] || [ -L "$destination" ]; then
      if [ ! -e "$source" ] && [ ! -L "$source" ]; then
        mv -- "$destination" "$source" || true
      else
        printf 'Rollback could not restore quarantine source because it now exists: %s\n' "$source" >&2
      fi
    fi
  done

  if [ -n "$quarantine_run_dir" ] && [ -d "$quarantine_run_dir" ]; then
    rmdir "$quarantine_run_dir" 2>/dev/null || true
  fi
  if [ "$quarantine_root_preexisting" -eq 0 ] && [ -d "$quarantine_root" ]; then
    rmdir "$quarantine_root" 2>/dev/null || true
  fi
}

cleanup() {
  local status=$?
  trap - EXIT
  if [ "$mutation_started" -eq 1 ] && [ "$commit_succeeded" -eq 0 ]; then
    rollback_install || status=1
  fi
  if [ -n "$staging_dir" ] && [ -d "$staging_dir" ]; then
    rm -rf -- "$staging_dir"
  fi
  if [ -n "$cloned_repo_dir" ] && [ -d "$cloned_repo_dir" ]; then
    rm -rf -- "$cloned_repo_dir"
  fi
  exit "$status"
}
trap cleanup EXIT

if [ -n "$source_repo" ]; then
  if [ ! -d "$source_repo" ]; then
    printf 'Source repo does not exist: %s\n' "$source_repo" >&2
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
  printf 'Source repo does not look like claude-code-rules: %s\n' "$source_repo" >&2
  exit 1
fi

claude_dir="$project_root/.claude"
rules_dir="$claude_dir/rules"
manifest_path="$rules_dir/.claude-code-rules-manifest.tsv"
quarantine_parent="$claude_dir/quarantine"
quarantine_root="$quarantine_parent/claude-code-rules"
prior_in_tree_quarantine="$rules_dir/.claude-code-rules-legacy-backup"

assert_managed_directory() {
  local path="$1"
  local label="$2"
  local resolved
  if [ -L "$path" ]; then
    printf '%s must not be a symbolic link: %s\n' "$label" "$path" >&2
    return 1
  fi
  if [ -e "$path" ] && [ ! -d "$path" ]; then
    printf '%s is not a directory: %s\n' "$label" "$path" >&2
    return 1
  fi
  [ -d "$path" ] || return 0
  resolved="$(cd "$path" && pwd -P)"
  case "$resolved" in
    "$project_root"|"$project_root"/*) ;;
    *)
      printf '%s resolves outside the project root: %s -> %s\n' "$label" "$path" "$resolved" >&2
      return 1
      ;;
  esac
}

assert_managed_directory "$claude_dir" 'Claude directory'
assert_managed_directory "$rules_dir" 'Rules directory'
mkdir -p "$rules_dir"
assert_managed_directory "$claude_dir" 'Claude directory'
assert_managed_directory "$rules_dir" 'Rules directory'

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
  goal-authoring-and-route-support.md
  external-verification-and-source-trust.md
  memory-governance-and-session-boundary.md
  phase-todo-artifact.md
  portable-implementation-and-hardcoding-control.md
  refusal-and-recovery.md
  safe-io.md
  worker-routing-and-context.md
)

retired_rule_candidates=(
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
    printf 'No SHA-256 tool available.\n' >&2
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

is_safe_rule_filename() {
  local file="$1"
  case "$file" in
    ""|"."|".."|*/*|*\\*) return 1 ;;
  esac
  return 0
}

validate_hash_field() {
  local value="$1"
  local label="$2"
  local line_number="$3"
  [ -z "$value" ] && return 0
  if [[ ! "$value" =~ ^[0-9a-fA-F]{40}$ && ! "$value" =~ ^[0-9a-fA-F]{64}$ ]]; then
    printf 'Invalid %s in manifest line %s.\n' "$label" "$line_number" >&2
    return 1
  fi
}

manifest_contains_file() {
  local needle="$1"
  local file
  for file in "${manifest_files[@]}"; do
    [ "$file" = "$needle" ] && return 0
  done
  return 1
}

validate_manifest() {
  local line_number=0 file recorded_sha256 recorded_blob
  if [ -L "$manifest_path" ]; then
    printf 'Manifest path must not be a symbolic link: %s\n' "$manifest_path" >&2
    return 1
  fi
  if [ -e "$manifest_path" ] && [ ! -f "$manifest_path" ]; then
    printf 'Manifest path is not a regular file: %s\n' "$manifest_path" >&2
    return 1
  fi
  [ -f "$manifest_path" ] || return 0

  while IFS=$'\t' read -r file recorded_sha256 recorded_blob || [ -n "${file:-}${recorded_sha256:-}${recorded_blob:-}" ]; do
    line_number=$((line_number + 1))
    recorded_blob="${recorded_blob%$'\r'}"
    [ -n "$file" ] || continue
    if ! is_safe_rule_filename "$file"; then
      printf 'Unsafe filename in manifest line %s: %s\n' "$line_number" "$file" >&2
      return 1
    fi
    if manifest_contains_file "$file"; then
      printf 'Duplicate filename in manifest line %s: %s\n' "$line_number" "$file" >&2
      return 1
    fi
    validate_hash_field "$recorded_sha256" 'SHA-256' "$line_number"
    validate_hash_field "$recorded_blob" 'Git blob hash' "$line_number"
    manifest_files+=("$file")
    manifest_sha256s+=("$recorded_sha256")
    manifest_blobs+=("$recorded_blob")
  done < "$manifest_path"
}

manifest_record_found=0
manifest_recorded_sha256=""
manifest_recorded_blob=""
load_manifest_record() {
  local needle="$1"
  local index
  manifest_record_found=0
  manifest_recorded_sha256=""
  manifest_recorded_blob=""
  for ((index=0; index<${#manifest_files[@]}; index++)); do
    if [ "${manifest_files[$index]}" = "$needle" ]; then
      manifest_record_found=1
      manifest_recorded_sha256="${manifest_sha256s[$index]}"
      manifest_recorded_blob="${manifest_blobs[$index]}"
      return 0
    fi
  done
}

matches_recorded_snapshot() {
  local target="$1"
  local recorded_sha256="$2"
  local recorded_blob="$3"
  local current_sha256 current_blob
  current_sha256="$(hash_file "$target")"
  current_blob="$(git_blob_hash "$target")"
  if [ -n "$recorded_blob" ]; then
    [ "$current_blob" = "$recorded_blob" ]
  elif [ -n "$recorded_sha256" ]; then
    [ "$current_sha256" = "$recorded_sha256" ]
  else
    return 1
  fi
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

planned_source_exists() {
  local needle="$1"
  local source
  for source in "${planned_quarantine_sources[@]}"; do
    [ "$source" = "$needle" ] && return 0
  done
  return 1
}

planned_name_exists() {
  local needle="$1"
  local name
  for name in "${planned_quarantine_names[@]}"; do
    [ "$name" = "$needle" ] && return 0
  done
  return 1
}

add_quarantine_plan() {
  local label="$1"
  local source="$2"
  local destination_name="$3"
  if planned_source_exists "$source"; then
    return 0
  fi
  if planned_name_exists "$destination_name"; then
    printf 'Duplicate quarantine destination name: %s\n' "$destination_name" >&2
    return 1
  fi
  planned_quarantine_labels+=("$label")
  planned_quarantine_sources+=("$source")
  planned_quarantine_names+=("$destination_name")
}

active_target_is_owned() {
  local file="$1"
  local source_path="$source_repo/$file"
  local target="$rules_dir/$file"
  local current_blob

  if [ -L "$source_path" ] || [ ! -f "$source_path" ]; then
    printf 'Active source rule must be a regular non-symlink file: %s\n' "$source_path" >&2
    return 1
  fi
  if [ -L "$target" ]; then
    printf 'Active rule target must not be a symbolic link: %s\n' "$target" >&2
    return 1
  fi
  if [ -e "$target" ] && [ ! -f "$target" ]; then
    printf 'Active rule target is not a regular file: %s\n' "$target" >&2
    return 1
  fi
  [ -f "$target" ] || return 0
  if [ "$(hash_file "$target")" = "$(hash_file "$source_path")" ]; then
    return 0
  fi
  load_manifest_record "$file"
  if [ "$manifest_record_found" -eq 1 ] && matches_recorded_snapshot "$target" "$manifest_recorded_sha256" "$manifest_recorded_blob"; then
    return 0
  fi
  current_blob="$(git_blob_hash "$target")"
  if repo_has_historical_blob "$file" "$current_blob"; then
    return 0
  fi
  printf 'Refusing to overwrite modified or unowned active rule target: %s\n' "$target" >&2
  return 1
}

ensure_quarantine_run() {
  if [ -z "$quarantine_run_dir" ]; then
    assert_managed_directory "$claude_dir" 'Claude directory'
    assert_managed_directory "$quarantine_parent" 'Quarantine parent'
    assert_managed_directory "$quarantine_root" 'Quarantine root'
    if [ -d "$quarantine_root" ]; then
      quarantine_root_preexisting=1
    else
      quarantine_root_preexisting=0
      mkdir -p "$quarantine_root"
    fi
    assert_managed_directory "$quarantine_parent" 'Quarantine parent'
    assert_managed_directory "$quarantine_root" 'Quarantine root'
    quarantine_run_dir="$(mktemp -d "$quarantine_root/run-$(date +%Y%m%d-%H%M%S)-XXXXXX")"
    assert_managed_directory "$quarantine_run_dir" 'Quarantine run directory'
  fi
}

validate_manifest

for file in "${active_rule_files[@]}"; do
  active_target_is_owned "$file"
done

if [ -L "$prior_in_tree_quarantine" ]; then
  printf 'Prior in-tree quarantine path must not be a symbolic link: %s\n' "$prior_in_tree_quarantine" >&2
  exit 1
fi
if [ -e "$prior_in_tree_quarantine" ]; then
  if [ ! -d "$prior_in_tree_quarantine" ]; then
    printf 'Prior in-tree quarantine path is not a directory: %s\n' "$prior_in_tree_quarantine" >&2
    exit 1
  fi
  add_quarantine_plan 'prior in-tree quarantine directory' "$prior_in_tree_quarantine" 'prior-in-tree-quarantine'
fi

for ((index=0; index<${#manifest_files[@]}; index++)); do
  file="${manifest_files[$index]}"
  is_active_rule "$file" && continue
  target="$rules_dir/$file"
  if [ -L "$target" ]; then
    printf 'Manifest-owned target must not be a symbolic link: %s\n' "$target" >&2
    exit 1
  fi
  if [ -e "$target" ] && [ ! -f "$target" ]; then
    printf 'Manifest-owned target is not a regular file: %s\n' "$target" >&2
    exit 1
  fi
  if [ -f "$target" ]; then
    if matches_recorded_snapshot "$target" "${manifest_sha256s[$index]}" "${manifest_blobs[$index]}"; then
      add_quarantine_plan "obsolete manifest-owned rule $file" "$target" "$file"
    else
      printf 'Skipping manifest quarantine for %s because it no longer matches the previous claude-code-rules install snapshot.\n' "$file" >&2
    fi
  fi
done

for file in "${retired_rule_candidates[@]}"; do
  is_active_rule "$file" && continue
  target="$rules_dir/$file"
  planned_source_exists "$target" && continue
  if [ -L "$target" ]; then
    printf 'Retired rule candidate must not be a symbolic link: %s\n' "$target" >&2
    exit 1
  fi
  if [ -e "$target" ] && [ ! -f "$target" ]; then
    printf 'Retired rule candidate is not a regular file: %s\n' "$target" >&2
    exit 1
  fi
  if [ -f "$target" ]; then
    current_blob="$(git_blob_hash "$target")"
    if repo_has_historical_blob "$file" "$current_blob"; then
      add_quarantine_plan "retired historical rule $file" "$target" "$file"
    fi
  fi
done

assert_managed_directory "$claude_dir" 'Claude directory'
assert_managed_directory "$rules_dir" 'Rules directory'
staging_dir="$(mktemp -d "$claude_dir/.claude-code-rules-stage-XXXXXX")"
assert_managed_directory "$staging_dir" 'Staging directory'
staged_manifest="$staging_dir/.claude-code-rules-manifest.tsv"
mkdir -p "$staging_dir/active-backup"
for file in "${active_rule_files[@]}"; do
  cp -- "$source_repo/$file" "$staging_dir/$file"
  printf '%s\t%s\t%s\n' "$file" "$(hash_file "$staging_dir/$file")" "$(git_blob_hash "$staging_dir/$file")" >> "$staged_manifest"
done

mutation_started=1

if [ "${#planned_quarantine_sources[@]}" -gt 0 ]; then
  ensure_quarantine_run
  for ((index=0; index<${#planned_quarantine_sources[@]}; index++)); do
    source="${planned_quarantine_sources[$index]}"
    destination="$quarantine_run_dir/${planned_quarantine_names[$index]}"
    if [ -L "$source" ] || [ ! -e "$source" ]; then
      printf 'Quarantine source changed after preflight: %s\n' "$source" >&2
      exit 1
    fi
    if [ -e "$destination" ] || [ -L "$destination" ]; then
      printf 'Quarantine destination already exists for %s: %s\n' "${planned_quarantine_labels[$index]}" "$destination" >&2
      exit 1
    fi
    mv -- "$source" "$destination"
    quarantine_moved_sources+=("$source")
    quarantine_moved_destinations+=("$destination")
    printf 'Quarantined claude-code-rules %s -> %s\n' "${planned_quarantine_labels[$index]}" "$destination" >&2
  done
fi

for file in "${active_rule_files[@]}"; do
  active_target_is_owned "$file"
  target="$rules_dir/$file"
  if [ -f "$target" ]; then
    mv -- "$target" "$staging_dir/active-backup/$file"
    active_backup_files+=("$file")
  fi
  mv -- "$staging_dir/$file" "$target"
  active_installed_files+=("$file")
done

if [ -L "$manifest_path" ]; then
  printf 'Manifest path changed to a symbolic link before replacement: %s\n' "$manifest_path" >&2
  exit 1
fi
if [ -e "$manifest_path" ] && [ ! -f "$manifest_path" ]; then
  printf 'Manifest path changed to a non-regular file before replacement: %s\n' "$manifest_path" >&2
  exit 1
fi
if [ -f "$manifest_path" ]; then
  mv -- "$manifest_path" "$staging_dir/manifest-backup.tsv"
  manifest_backed_up=1
fi
mv -- "$staged_manifest" "$manifest_path"
manifest_installed=1

commit_succeeded=1
rm -rf -- "$staging_dir"
staging_dir=""

printf 'Installed %s active Claude Code rules into %s\n' "${#active_rule_files[@]}" "$rules_dir"
printf 'Manifest: %s\n' "$manifest_path"
if [ -n "$quarantine_run_dir" ]; then
  printf 'Quarantine: %s\n' "$quarantine_run_dir"
fi
