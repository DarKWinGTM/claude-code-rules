#!/usr/bin/env bash
set -euo pipefail

script_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd -P)"
source_repo="$(cd "$script_dir/.." && pwd -P)"
installer="$script_dir/setup-claude-code-rules.sh"
tmp_root="$(mktemp -d)"
trap 'rm -rf "$tmp_root"' EXIT

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
  anti-mockup.md anti-sycophancy.md context-load-and-document-density-control.md
  custom-agent-selection-priority.md dan-safe-normalization.md development-verification-and-debug-strategy.md
  document-changelog-control.md document-consistency.md document-design-control.md document-patch-control.md
  emergency-protocol.md evidence-grounded-burden-of-proof.md execution-continuity-and-mode-selection.md
  explanation-quality.md flow-diagram-no-frame.md functional-intent-verification.md
  goal-set-review-and-priority-balance.md governed-document-rollover-control.md high-signal-communication.md
  maintainable-code-structure-and-decomposition.md native-worker-agent-routing-and-context-control.md
  natural-professional-communication.md no-variable-guessing.md operational-failure-handling.md
  phase-implementation.md project-documentation-standards.md recovery-contract.md refusal-classification.md
  refusal-minimization.md response-closing-and-action-framing.md runtime-topology-control.md safe-file-reading.md
  safe-terminal-output.md strict-file-hygiene.md tactical-strategic-programming.md
  technical-snapshot-communication.md todo-standards.md unified-version-control-system.md zero-hallucination.md
  answer-presentation.md artifact-initiation-control.md
)

fail() {
  printf 'FAIL: %s\n' "$1" >&2
  exit 1
}

assert_file() {
  [ -f "$1" ] || fail "expected file: $1"
}

assert_absent() {
  [ ! -e "$1" ] || fail "expected absent path: $1"
}

assert_equal() {
  [ "$1" = "$2" ] || fail "$3 (expected $1, got $2)"
}

hash_file() {
  sha256sum "$1" | awk '{print $1}'
}

blob_file() {
  git hash-object -- "$1"
}

tree_hash() {
  local root="$1"
  (
    cd "$root"
    find . -type f -print0 | sort -z | xargs -0 sha256sum | sha256sum | awk '{print $1}'
  )
}

tree_state_hash() {
  local root="$1"
  (
    cd "$root"
    {
      find . -mindepth 1 -printf '%y\t%p\t%l\n' | LC_ALL=C sort
      find . -type f -print0 | LC_ALL=C sort -z | xargs -0 sha256sum
    } | sha256sum | awk '{print $1}'
  )
}

write_manifest_line() {
  local manifest="$1"
  local file="$2"
  local snapshot="$3"
  printf '%s\t%s\t%s\n' "$file" "$(hash_file "$snapshot")" "$(blob_file "$snapshot")" >> "$manifest"
}

write_historical_file() {
  local file="$1"
  local target="$2"
  local commit=""
  local item
  while IFS= read -r item; do
    if git -C "$source_repo" cat-file -e "$item:$file" 2>/dev/null; then
      commit="$item"
      break
    fi
  done < <(git -C "$source_repo" rev-list --all -- "$file")
  [ -n "$commit" ] || fail "no historical blob found for $file"
  git -C "$source_repo" show "$commit:$file" > "$target"
}

verify_payload() {
  local project="$1"
  local expected_source="$2"
  local rules_dir="$project/.claude/rules"
  local manifest="$rules_dir/.claude-code-rules-manifest.tsv"
  local index=0 file manifest_file
  assert_file "$manifest"
  mapfile -t manifest_files < <(cut -f1 "$manifest")
  assert_equal "${#active_rule_files[@]}" "${#manifest_files[@]}" 'manifest file count mismatch'
  for file in "${active_rule_files[@]}"; do
    manifest_file="${manifest_files[$index]}"
    assert_equal "$file" "$manifest_file" "manifest order mismatch at index $index"
    assert_file "$rules_dir/$file"
    assert_equal "$(hash_file "$expected_source/$file")" "$(hash_file "$rules_dir/$file")" "payload mismatch for $file"
    [ "$(wc -c < "$rules_dir/$file")" -gt 500 ] || fail "body-sufficiency check failed for $file"
    index=$((index + 1))
  done
}

project="$tmp_root/project"
rules_dir="$project/.claude/rules"
mkdir -p "$rules_dir/.claude-code-rules-legacy-backup/nested"
printf 'opaque prior quarantine\n' > "$rules_dir/.claude-code-rules-legacy-backup/nested/former.md"

write_historical_file anti-mockup.md "$rules_dir/anti-mockup.md"
printf 'obsolete owned snapshot\n' > "$rules_dir/obsolete-owned.md"
printf 'modified original snapshot\n' > "$tmp_root/modified-original.md"
cp "$tmp_root/modified-original.md" "$rules_dir/modified-owned.md"
printf 'modified by another owner\n' >> "$rules_dir/modified-owned.md"
printf 'unmatched same-name sentinel\n' > "$rules_dir/unmatched-sentinel.md"
printf 'unrelated runtime rule\n' > "$rules_dir/shared-task-list-path-coordination.md"
unrelated_hash="$(hash_file "$rules_dir/shared-task-list-path-coordination.md")"
modified_hash="$(hash_file "$rules_dir/modified-owned.md")"
unmatched_hash="$(hash_file "$rules_dir/unmatched-sentinel.md")"

manifest="$rules_dir/.claude-code-rules-manifest.tsv"
write_manifest_line "$manifest" obsolete-owned.md "$rules_dir/obsolete-owned.md"
write_manifest_line "$manifest" modified-owned.md "$tmp_root/modified-original.md"

"$installer" --project-root "$project" --source-repo "$source_repo" > "$tmp_root/first-install.out"
verify_payload "$project" "$source_repo"

mapfile -t quarantine_runs < <(find "$project/.claude/quarantine/claude-code-rules" -mindepth 1 -maxdepth 1 -type d -print)
assert_equal 1 "${#quarantine_runs[@]}" 'expected one quarantine run'
quarantine_run="${quarantine_runs[0]}"
assert_file "$quarantine_run/anti-mockup.md"
assert_file "$quarantine_run/obsolete-owned.md"
assert_file "$quarantine_run/prior-in-tree-quarantine/nested/former.md"
assert_absent "$rules_dir/anti-mockup.md"
assert_absent "$rules_dir/obsolete-owned.md"
assert_absent "$rules_dir/.claude-code-rules-legacy-backup"
assert_equal "$modified_hash" "$(hash_file "$rules_dir/modified-owned.md")" 'modified manifest-owned file changed'
assert_equal "$unmatched_hash" "$(hash_file "$rules_dir/unmatched-sentinel.md")" 'unmatched file changed'
assert_equal "$unrelated_hash" "$(hash_file "$rules_dir/shared-task-list-path-coordination.md")" 'unrelated file changed'
for file in "${retired_rule_candidates[@]}"; do
  assert_absent "$rules_dir/$file"
done

printf 'poison that must never be read\n' > "$quarantine_run/poison.md"
quarantine_hash="$(tree_hash "$project/.claude/quarantine/claude-code-rules")"
mv "$project/.claude/quarantine/claude-code-rules" "$project/.claude/quarantine/claude-code-rules-offline"
"$installer" --project-root "$project" --source-repo "$source_repo" > "$tmp_root/rerun.out"
verify_payload "$project" "$source_repo"
assert_absent "$project/.claude/quarantine/claude-code-rules"
assert_equal "$quarantine_hash" "$(tree_hash "$project/.claude/quarantine/claude-code-rules-offline")" 'offline quarantine changed during reinstall'
assert_equal "$unrelated_hash" "$(hash_file "$rules_dir/shared-task-list-path-coordination.md")" 'unrelated file changed on rerun'

"$installer" --project-root "$project" --source-repo "$source_repo" > "$tmp_root/idempotent.out"
verify_payload "$project" "$source_repo"
assert_absent "$project/.claude/quarantine/claude-code-rules"

known_good="$tmp_root/known-good-v10.57"
git clone --quiet --no-local "$source_repo" "$known_good"
git -C "$known_good" checkout --quiet v10.57
"$installer" --project-root "$project" --source-repo "$known_good" > "$tmp_root/restoration.out"
verify_payload "$project" "$known_good"
assert_absent "$project/.claude/quarantine/claude-code-rules"
assert_equal "$quarantine_hash" "$(tree_hash "$project/.claude/quarantine/claude-code-rules-offline")" 'controlled restoration touched quarantine'
assert_equal "$unrelated_hash" "$(hash_file "$rules_dir/shared-task-list-path-coordination.md")" 'controlled restoration changed unrelated file'

traversal_project="$tmp_root/traversal-project"
mkdir -p "$traversal_project/.claude/rules"
printf 'escape sentinel\n' > "$traversal_project/escape.md"
printf '../../escape.md\t%s\t%s\n' "$(hash_file "$traversal_project/escape.md")" "$(blob_file "$traversal_project/escape.md")" > "$traversal_project/.claude/rules/.claude-code-rules-manifest.tsv"
if "$installer" --project-root "$traversal_project" --source-repo "$source_repo" > "$tmp_root/traversal.out" 2>&1; then
  fail 'path-traversal manifest unexpectedly succeeded'
fi
assert_file "$traversal_project/escape.md"
assert_absent "$traversal_project/.claude/rules/accurate-communication.md"

collision_project="$tmp_root/collision-project"
mkdir -p "$collision_project/.claude/rules"
printf 'other-owner active-name collision\n' > "$collision_project/.claude/rules/accurate-communication.md"
collision_hash="$(hash_file "$collision_project/.claude/rules/accurate-communication.md")"
if "$installer" --project-root "$collision_project" --source-repo "$source_repo" > "$tmp_root/collision.out" 2>&1; then
  fail 'unowned active-name collision unexpectedly succeeded'
fi
assert_equal "$collision_hash" "$(hash_file "$collision_project/.claude/rules/accurate-communication.md")" 'active-name collision was overwritten'
assert_absent "$collision_project/.claude/rules/.claude-code-rules-manifest.tsv"

duplicate_active_project="$tmp_root/duplicate-active-project"
mkdir -p "$duplicate_active_project/.claude/rules"
duplicate_active_manifest="$duplicate_active_project/.claude/rules/.claude-code-rules-manifest.tsv"
printf 'accurate-communication.md\t%s\t%s\n' "$(hash_file "$source_repo/accurate-communication.md")" "$(blob_file "$source_repo/accurate-communication.md")" > "$duplicate_active_manifest"
printf 'accurate-communication.md\t%s\t%s\n' "$(hash_file "$source_repo/action-safety.md")" "$(blob_file "$source_repo/action-safety.md")" >> "$duplicate_active_manifest"
if "$installer" --project-root "$duplicate_active_project" --source-repo "$source_repo" > "$tmp_root/duplicate-active.out" 2>&1; then
  fail 'duplicate active manifest record unexpectedly succeeded'
fi
assert_absent "$duplicate_active_project/.claude/rules/accurate-communication.md"

duplicate_obsolete_project="$tmp_root/duplicate-obsolete-project"
mkdir -p "$duplicate_obsolete_project/.claude/rules"
printf 'duplicate obsolete sentinel\n' > "$duplicate_obsolete_project/.claude/rules/obsolete-owned.md"
duplicate_obsolete_hash="$(hash_file "$duplicate_obsolete_project/.claude/rules/obsolete-owned.md")"
duplicate_obsolete_manifest="$duplicate_obsolete_project/.claude/rules/.claude-code-rules-manifest.tsv"
write_manifest_line "$duplicate_obsolete_manifest" obsolete-owned.md "$duplicate_obsolete_project/.claude/rules/obsolete-owned.md"
write_manifest_line "$duplicate_obsolete_manifest" obsolete-owned.md "$duplicate_obsolete_project/.claude/rules/obsolete-owned.md"
if "$installer" --project-root "$duplicate_obsolete_project" --source-repo "$source_repo" > "$tmp_root/duplicate-obsolete.out" 2>&1; then
  fail 'duplicate obsolete manifest record unexpectedly succeeded'
fi
assert_equal "$duplicate_obsolete_hash" "$(hash_file "$duplicate_obsolete_project/.claude/rules/obsolete-owned.md")" 'duplicate obsolete preflight mutated target'
assert_absent "$duplicate_obsolete_project/.claude/quarantine/claude-code-rules"

manifest_link_project="$tmp_root/manifest-link-project"
mkdir -p "$manifest_link_project/.claude/rules"
printf 'external manifest sentinel\n' > "$tmp_root/external-manifest.tsv"
external_manifest_hash="$(hash_file "$tmp_root/external-manifest.tsv")"
ln -s "$tmp_root/external-manifest.tsv" "$manifest_link_project/.claude/rules/.claude-code-rules-manifest.tsv"
if "$installer" --project-root "$manifest_link_project" --source-repo "$source_repo" > "$tmp_root/manifest-link.out" 2>&1; then
  fail 'manifest symlink unexpectedly succeeded'
fi
[ -L "$manifest_link_project/.claude/rules/.claude-code-rules-manifest.tsv" ] || fail 'manifest symlink was replaced'
assert_equal "$external_manifest_hash" "$(hash_file "$tmp_root/external-manifest.tsv")" 'manifest symlink target was modified'
assert_absent "$manifest_link_project/.claude/rules/accurate-communication.md"

broken_manifest_link_project="$tmp_root/broken-manifest-link-project"
mkdir -p "$broken_manifest_link_project/.claude/rules"
ln -s "$tmp_root/missing-manifest.tsv" "$broken_manifest_link_project/.claude/rules/.claude-code-rules-manifest.tsv"
if "$installer" --project-root "$broken_manifest_link_project" --source-repo "$source_repo" > "$tmp_root/broken-manifest-link.out" 2>&1; then
  fail 'broken manifest symlink unexpectedly succeeded'
fi
[ -L "$broken_manifest_link_project/.claude/rules/.claude-code-rules-manifest.tsv" ] || fail 'broken manifest symlink was replaced'

active_link_project="$tmp_root/active-link-project"
mkdir -p "$active_link_project/.claude/rules"
printf 'external active target sentinel\n' > "$tmp_root/external-active.md"
external_active_hash="$(hash_file "$tmp_root/external-active.md")"
ln -s "$tmp_root/external-active.md" "$active_link_project/.claude/rules/accurate-communication.md"
if "$installer" --project-root "$active_link_project" --source-repo "$source_repo" > "$tmp_root/active-link.out" 2>&1; then
  fail 'active-target symlink unexpectedly succeeded'
fi
[ -L "$active_link_project/.claude/rules/accurate-communication.md" ] || fail 'active-target symlink was replaced'
assert_equal "$external_active_hash" "$(hash_file "$tmp_root/external-active.md")" 'active-target symlink destination was modified'

broken_active_link_project="$tmp_root/broken-active-link-project"
mkdir -p "$broken_active_link_project/.claude/rules"
ln -s "$tmp_root/missing-active.md" "$broken_active_link_project/.claude/rules/accurate-communication.md"
if "$installer" --project-root "$broken_active_link_project" --source-repo "$source_repo" > "$tmp_root/broken-active-link.out" 2>&1; then
  fail 'broken active-target symlink unexpectedly succeeded'
fi
[ -L "$broken_active_link_project/.claude/rules/accurate-communication.md" ] || fail 'broken active-target symlink was replaced'

preflight_project="$tmp_root/preflight-project"
mkdir -p "$preflight_project/.claude/rules/.claude-code-rules-legacy-backup/nested"
printf 'opaque preflight quarantine\n' > "$preflight_project/.claude/rules/.claude-code-rules-legacy-backup/nested/former.md"
mkdir -p "$preflight_project/.claude/rules/obsolete-directory"
printf 'obsolete-directory\t%s\t%s\n' "$(printf '0%.0s' {1..64})" "$(printf '0%.0s' {1..40})" > "$preflight_project/.claude/rules/.claude-code-rules-manifest.tsv"
preflight_hash="$(tree_state_hash "$preflight_project")"
if "$installer" --project-root "$preflight_project" --source-repo "$source_repo" > "$tmp_root/preflight.out" 2>&1; then
  fail 'invalid later manifest target unexpectedly succeeded'
fi
assert_equal "$preflight_hash" "$(tree_state_hash "$preflight_project")" 'failed deterministic preflight mutated project tree'
assert_absent "$preflight_project/.claude/quarantine/claude-code-rules"

claude_link_project="$tmp_root/claude-link-project"
claude_link_external="$tmp_root/claude-link-external"
mkdir -p "$claude_link_project" "$claude_link_external/rules"
printf 'external claude sentinel\n' > "$claude_link_external/sentinel.md"
claude_link_hash="$(tree_state_hash "$claude_link_external")"
ln -s "$claude_link_external" "$claude_link_project/.claude"
if "$installer" --project-root "$claude_link_project" --source-repo "$source_repo" > "$tmp_root/claude-link.out" 2>&1; then
  fail 'symlinked .claude ancestor unexpectedly succeeded'
fi
[ -L "$claude_link_project/.claude" ] || fail 'symlinked .claude ancestor was replaced'
assert_equal "$claude_link_hash" "$(tree_state_hash "$claude_link_external")" 'symlinked .claude ancestor mutated external tree'

rules_link_project="$tmp_root/rules-link-project"
rules_link_external="$tmp_root/rules-link-external"
mkdir -p "$rules_link_project/.claude" "$rules_link_external"
printf 'external rules sentinel\n' > "$rules_link_external/sentinel.md"
rules_link_hash="$(tree_state_hash "$rules_link_external")"
ln -s "$rules_link_external" "$rules_link_project/.claude/rules"
if "$installer" --project-root "$rules_link_project" --source-repo "$source_repo" > "$tmp_root/rules-link.out" 2>&1; then
  fail 'symlinked rules directory unexpectedly succeeded'
fi
[ -L "$rules_link_project/.claude/rules" ] || fail 'symlinked rules directory was replaced'
assert_equal "$rules_link_hash" "$(tree_state_hash "$rules_link_external")" 'symlinked rules directory mutated external tree'

quarantine_parent_link_project="$tmp_root/quarantine-parent-link-project"
quarantine_parent_external="$tmp_root/quarantine-parent-external"
mkdir -p "$quarantine_parent_link_project/.claude/rules" "$quarantine_parent_external"
write_historical_file anti-mockup.md "$quarantine_parent_link_project/.claude/rules/anti-mockup.md"
printf 'external quarantine parent sentinel\n' > "$quarantine_parent_external/sentinel.md"
quarantine_parent_hash="$(tree_state_hash "$quarantine_parent_external")"
ln -s "$quarantine_parent_external" "$quarantine_parent_link_project/.claude/quarantine"
if "$installer" --project-root "$quarantine_parent_link_project" --source-repo "$source_repo" > "$tmp_root/quarantine-parent-link.out" 2>&1; then
  fail 'symlinked quarantine parent unexpectedly succeeded'
fi
assert_file "$quarantine_parent_link_project/.claude/rules/anti-mockup.md"
assert_equal "$quarantine_parent_hash" "$(tree_state_hash "$quarantine_parent_external")" 'symlinked quarantine parent mutated external tree'

quarantine_root_link_project="$tmp_root/quarantine-root-link-project"
quarantine_root_external="$tmp_root/quarantine-root-external"
mkdir -p "$quarantine_root_link_project/.claude/rules" "$quarantine_root_link_project/.claude/quarantine" "$quarantine_root_external"
write_historical_file anti-mockup.md "$quarantine_root_link_project/.claude/rules/anti-mockup.md"
printf 'external quarantine root sentinel\n' > "$quarantine_root_external/sentinel.md"
quarantine_root_hash="$(tree_state_hash "$quarantine_root_external")"
ln -s "$quarantine_root_external" "$quarantine_root_link_project/.claude/quarantine/claude-code-rules"
if "$installer" --project-root "$quarantine_root_link_project" --source-repo "$source_repo" > "$tmp_root/quarantine-root-link.out" 2>&1; then
  fail 'symlinked quarantine root unexpectedly succeeded'
fi
assert_file "$quarantine_root_link_project/.claude/rules/anti-mockup.md"
assert_equal "$quarantine_root_hash" "$(tree_state_hash "$quarantine_root_external")" 'symlinked quarantine root mutated external tree'

printf 'Bash installer fixtures: PASS\n'
