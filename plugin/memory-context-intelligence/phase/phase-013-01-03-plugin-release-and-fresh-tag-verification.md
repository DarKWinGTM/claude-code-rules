# Phase 013-01-03 — Plugin Release and Fresh-Tag Verification

> **Parent Phase:** [phase-013-01-deterministic-standalone-additional-stage-emission.md](phase-013-01-deterministic-standalone-additional-stage-emission.md)
> **Summary File:** [SUMMARY.md](SUMMARY.md)
> **Current Version:** 0.1.78
> **Status:** Clean release candidate verified; explicit external-action confirmation pending
> **Target Design:** [../design/design.md](../design/design.md) v0.1.78
> **Patch Reference:** [../patch/deterministic-standalone-additional-stage-emission.patch.md](../patch/deterministic-standalone-additional-stage-emission.patch.md)
> **Session:** 48a3ef9b-50cf-4574-8f00-4f6b6e28f76e (2026-08-09)

---

## Objective

Stages the verified plugin delta from the v0.9.29 tag in a clean temporary clone, then owns the approval-gated push, tag, GitHub Release, and fresh-tag verification.

## Inherited boundaries

- Initial analysis remains read-only and advisory.
- One selected topic maps to one artifact.
- Existing additional-stage files are preserved; no overwrite path is active.
- Main RULES and Phases 017-018 remain unchanged.
- Completion wording is limited to direct verification evidence.

## Entry evidence

The release child is unblocked by checked local implementation evidence:
- package/governed versions align at `0.9.30` / `0.1.78`
- post-version focused manifest/skill checks passed: `20 passed`
- post-version full source suite passed: `132 passed`
- controlled temporary-HOME/additional-root smoke passed for independent artifacts, collision byte preservation, traversal/symlink refusal, and checked Main RULES digest equality
- `claude plugin validate` passed

This entry evidence does not authorize push, tag, or GitHub Release.

## Clean release candidate record

Verified before the external-action gate:
- clean clone base: `memory-context-intelligence--v0.9.29` at `a70970c2e5496c3a46d9d5a3d7b83c30a6ed5dd1`
- dedicated local branch: `mci-release-v0.9.30`
- candidate scope: exactly 37 allowlisted plugin paths, with zero unexpected paths and zero deletions
- focused clean-clone suite: `113 passed`
- full clean-clone suite: `132 passed`
- clean-clone `claude plugin validate`: PASS
- remote preflight: branch absent, tag absent, and GitHub Release not found in checked scope

A local candidate commit exists for the approval gate. Its final SHA is reported directly with the confirmation request because any pre-gate documentation amendment changes that SHA. Remote parity remains unverified until the approved push/tag/release sequence completes.

---

### Task 10: Stage a clean plugin-only release candidate from the v0.9.29 tag

**Files:**
- Release source: `/home/node/workplace/AWCLOUD/TEMPLATE/RULES/plugin/memory-context-intelligence/`
- Temporary clean clone: generated under `/tmp`
- Base: `memory-context-intelligence--v0.9.29` (`a70970c`)
- Branch: `mci-release-v0.9.30`

**Release allowlist:**

```text
plugin/memory-context-intelligence/.claude-plugin/plugin.json
plugin/memory-context-intelligence/README.md
plugin/memory-context-intelligence/bin/memory-context-intelligence
plugin/memory-context-intelligence/changelog/changelog.md
plugin/memory-context-intelligence/changelog/v0.1.78-deterministic-standalone-additional-stage-emission.changelog.md
plugin/memory-context-intelligence/design/02-topic-list-and-choice-flow.design.md
plugin/memory-context-intelligence/design/05-additional-staging-and-promotion.design.md
plugin/memory-context-intelligence/design/08-memory-evidence-source-model.design.md
plugin/memory-context-intelligence/design/design.md
plugin/memory-context-intelligence/lib/candidate_packet.py
plugin/memory-context-intelligence/lib/historical_replay.py
plugin/memory-context-intelligence/lib/live_trial.py
plugin/memory-context-intelligence/lib/orchestration.py
plugin/memory-context-intelligence/lib/presentation.py
plugin/memory-context-intelligence/lib/readiness.py
plugin/memory-context-intelligence/lib/signals.py
plugin/memory-context-intelligence/patch/deterministic-standalone-additional-stage-emission.patch.md
plugin/memory-context-intelligence/phase/SUMMARY.md
plugin/memory-context-intelligence/phase/history/2026-08-09-pre-rollover-SUMMARY.md
plugin/memory-context-intelligence/phase/history/2026-08-09.md
plugin/memory-context-intelligence/phase/phase-013-candidate-packet-builder-and-additional-emitter.md
plugin/memory-context-intelligence/phase/phase-013-01-deterministic-standalone-additional-stage-emission.md
plugin/memory-context-intelligence/phase/phase-013-01-01-evidence-normalization-and-standalone-rendering.md
plugin/memory-context-intelligence/phase/phase-013-01-02-atomic-emission-runtime-verification-and-version-sync.md
plugin/memory-context-intelligence/phase/phase-013-01-03-plugin-release-and-fresh-tag-verification.md
plugin/memory-context-intelligence/skills/analysis/SKILL.md
plugin/memory-context-intelligence/tests/test_analysis_skill_contract.py
plugin/memory-context-intelligence/tests/test_candidate_packet.py
plugin/memory-context-intelligence/tests/test_candidate_packet_cli.py
plugin/memory-context-intelligence/tests/test_historical_replay.py
plugin/memory-context-intelligence/tests/test_intake.py
plugin/memory-context-intelligence/tests/test_live_trial.py
plugin/memory-context-intelligence/tests/test_orchestration.py
plugin/memory-context-intelligence/tests/test_plugin_manifest.py
plugin/memory-context-intelligence/tests/test_presentation.py
plugin/memory-context-intelligence/tests/test_readiness.py
plugin/memory-context-intelligence/tests/test_signals.py
```

Run `tests/test_analysis_surface.py` as an unchanged regression check, but do not copy it or `lib/analysis_surface.py`. Do not copy `lib/config_policy.py`, `lib/intake.py`, init-skill files, image/preview/index assets, root `TODO.md`, Main RULES, or other plugins; those are already represented by the v0.9.29 base or outside this release delta.

- [ ] **Step 1: Create a clean temporary clone from the existing release tag**

```bash
REPO_URL="https://github.com/DarKWinGTM/claude-code-rules.git"
SOURCE_ROOT="/home/node/workplace/AWCLOUD/TEMPLATE/RULES"
RELEASE_ROOT="$(mktemp -d /tmp/mci-v0.9.30-release.XXXXXX)"
git clone "$REPO_URL" "$RELEASE_ROOT"
git -C "$RELEASE_ROOT" switch -c mci-release-v0.9.30 memory-context-intelligence--v0.9.29
```

Expected: clean branch based at `a70970c`.

- [ ] **Step 2: Copy exactly the release allowlist**

Create an allowlist file under `/tmp`, then stream only those paths:

```bash
ALLOWLIST_FILE="$(mktemp /tmp/mci-v0.9.30-allowlist.XXXXXX)"
python3 - "$ALLOWLIST_FILE" <<'PY'
from pathlib import Path
import sys

paths = """plugin/memory-context-intelligence/.claude-plugin/plugin.json
plugin/memory-context-intelligence/README.md
plugin/memory-context-intelligence/bin/memory-context-intelligence
plugin/memory-context-intelligence/changelog/changelog.md
plugin/memory-context-intelligence/changelog/v0.1.78-deterministic-standalone-additional-stage-emission.changelog.md
plugin/memory-context-intelligence/design/02-topic-list-and-choice-flow.design.md
plugin/memory-context-intelligence/design/05-additional-staging-and-promotion.design.md
plugin/memory-context-intelligence/design/08-memory-evidence-source-model.design.md
plugin/memory-context-intelligence/design/design.md
plugin/memory-context-intelligence/lib/candidate_packet.py
plugin/memory-context-intelligence/lib/historical_replay.py
plugin/memory-context-intelligence/lib/live_trial.py
plugin/memory-context-intelligence/lib/orchestration.py
plugin/memory-context-intelligence/lib/presentation.py
plugin/memory-context-intelligence/lib/readiness.py
plugin/memory-context-intelligence/lib/signals.py
plugin/memory-context-intelligence/patch/deterministic-standalone-additional-stage-emission.patch.md
plugin/memory-context-intelligence/phase/SUMMARY.md
plugin/memory-context-intelligence/phase/history/2026-08-09-pre-rollover-SUMMARY.md
plugin/memory-context-intelligence/phase/history/2026-08-09.md
plugin/memory-context-intelligence/phase/phase-013-candidate-packet-builder-and-additional-emitter.md
plugin/memory-context-intelligence/phase/phase-013-01-deterministic-standalone-additional-stage-emission.md
plugin/memory-context-intelligence/phase/phase-013-01-01-evidence-normalization-and-standalone-rendering.md
plugin/memory-context-intelligence/phase/phase-013-01-02-atomic-emission-runtime-verification-and-version-sync.md
plugin/memory-context-intelligence/phase/phase-013-01-03-plugin-release-and-fresh-tag-verification.md
plugin/memory-context-intelligence/skills/analysis/SKILL.md
plugin/memory-context-intelligence/tests/test_analysis_skill_contract.py
plugin/memory-context-intelligence/tests/test_candidate_packet.py
plugin/memory-context-intelligence/tests/test_candidate_packet_cli.py
plugin/memory-context-intelligence/tests/test_historical_replay.py
plugin/memory-context-intelligence/tests/test_intake.py
plugin/memory-context-intelligence/tests/test_live_trial.py
plugin/memory-context-intelligence/tests/test_orchestration.py
plugin/memory-context-intelligence/tests/test_plugin_manifest.py
plugin/memory-context-intelligence/tests/test_presentation.py
plugin/memory-context-intelligence/tests/test_readiness.py
plugin/memory-context-intelligence/tests/test_signals.py""".splitlines()
Path(sys.argv[1]).write_text("\n".join(paths) + "\n", encoding="utf-8")
PY
tar -C "$SOURCE_ROOT" -cf - -T "$ALLOWLIST_FILE" | tar -C "$RELEASE_ROOT" -xf -
```

If any listed source path is missing, stop before staging.

- [ ] **Step 3: Verify candidate scope before staging**

```bash
git -C "$RELEASE_ROOT" status --short
git -C "$RELEASE_ROOT" diff --check
git -C "$RELEASE_ROOT" diff --name-only
```

Expected: every changed path is in the exact plugin allowlist; no root RULES, root TODO, other plugin, deletion, or unexpected generated asset appears.

- [ ] **Step 4: Run focused and full tests in the release clone**

```bash
cd "$RELEASE_ROOT/plugin/memory-context-intelligence"
python3 -m pytest -q \
  tests/test_candidate_packet.py \
  tests/test_candidate_packet_cli.py \
  tests/test_signals.py \
  tests/test_orchestration.py \
  tests/test_presentation.py \
  tests/test_analysis_skill_contract.py \
  tests/test_historical_replay.py \
  tests/test_live_trial.py \
  tests/test_readiness.py \
  tests/test_plugin_manifest.py
python3 -m pytest -q tests
```

Expected: PASS from the clean release candidate.

- [ ] **Step 5: Stage exact files and inspect staged scope**

```bash
git -C "$RELEASE_ROOT" add --pathspec-from-file="$ALLOWLIST_FILE"
git -C "$RELEASE_ROOT" diff --cached --check
git -C "$RELEASE_ROOT" diff --cached --name-status
```

Compare staged paths programmatically with the allowlist. Expected: exact set equality after excluding allowlisted files that are byte-identical to the base tag. No unrelated path is staged.

- [ ] **Step 6: Commit the release candidate**

```bash
git -C "$RELEASE_ROOT" commit -m "$(cat <<'EOF'
feat: add deterministic standalone trial emission

Co-Authored-By: Claude <noreply@anthropic.com>
EOF
)"
```

Record the commit SHA. Do not push yet.

---

### Task 11: Push, tag, release, and verify v0.9.30

**External action gate:** Before Step 2, present the exact repository, branch, commit SHA, tag, release title, staged path count, and test results. Obtain explicit action-and-scope confirmation for push + tag + GitHub Release.

- [ ] **Step 1: Verify local release candidate one final time**

```bash
git -C "$RELEASE_ROOT" status --short --branch
git -C "$RELEASE_ROOT" show --stat --oneline HEAD
cd "$RELEASE_ROOT/plugin/memory-context-intelligence"
python3 -m pytest -q tests
```

Expected: clean release clone and full suite PASS.

- [ ] **Step 2: Push the dedicated plugin branch after confirmation**

```bash
git -C "$RELEASE_ROOT" push -u origin mci-release-v0.9.30
```

Verify:

```bash
git -C "$RELEASE_ROOT" ls-remote --heads origin mci-release-v0.9.30
```

Expected: remote branch SHA equals local release commit SHA.

- [ ] **Step 3: Create and push the annotated package tag**

```bash
git -C "$RELEASE_ROOT" tag -a memory-context-intelligence--v0.9.30 \
  -m "memory-context-intelligence v0.9.30"
git -C "$RELEASE_ROOT" push origin memory-context-intelligence--v0.9.30
```

Verify the peeled annotated tag resolves to the release commit.

- [ ] **Step 4: Create the GitHub Release**

```bash
gh release create memory-context-intelligence--v0.9.30 \
  --repo DarKWinGTM/claude-code-rules \
  --title "memory-context-intelligence v0.9.30" \
  --notes "$(cat <<'EOF'
## memory-context-intelligence v0.9.30

- Keeps the initial analysis response read-only and advisory.
- Adds deterministic explicit post-selection additional-stage handling.
- Emits one rich standalone trial rule per selected topic.
- Normalizes evidence without temporary memory/transcript/path-line dependencies.
- Preflights the full selected set and refuses collisions without overwrite.
- Strengthens additional-root namespace, traversal, and symlink containment.
- Keeps Main RULES promotion separate and unapproved.

Verification: focused tests, full plugin suite, controlled temporary-HOME/additional-root smoke, and clean release-clone tests passed in the recorded release scope.
EOF
)"
```

- [ ] **Step 5: Verify release identity and fresh tag behavior**

```bash
gh release view memory-context-intelligence--v0.9.30 \
  --repo DarKWinGTM/claude-code-rules \
  --json url,tagName,name,isDraft,isPrerelease,targetCommitish
VERIFY_ROOT="$(mktemp -d /tmp/mci-v0.9.30-verify.XXXXXX)"
git clone --depth 1 --branch memory-context-intelligence--v0.9.30 \
  "$REPO_URL" "$VERIFY_ROOT"
cd "$VERIFY_ROOT/plugin/memory-context-intelligence"
python3 -m pytest -q tests
```

Expected:
- release is neither draft nor prerelease
- tag/name match `memory-context-intelligence--v0.9.30` / `memory-context-intelligence v0.9.30`
- fresh tagged clone reports manifest version `0.9.30`
- full plugin suite passes
- tag tree contains only the intended plugin delta relative to v0.9.29

- [ ] **Step 6: Record post-release verification without moving the tag**

After live verification, update the local source phase summary, this phase, changelog shard, and patch with:
- branch/commit/tag
- GitHub Release URL
- fresh-tag test command/result
- checked release scope and limits

If these post-release evidence updates are pushed, use a separate plugin-doc-only commit on `mci-release-v0.9.30`; do not move or recreate the published tag. Root `TODO.md` closeout stays outside the plugin release commit because the root working tree contains unrelated active work.

---

## Completion gate

Phase 013-01 can close only when:
- baseline date-fixture failures are corrected and distinguished from feature behavior
- selected signal/topic entailment is explicit and trace-linked
- initial presentation and ordinary choose remain unselected for additional creation
- explicit later selection records additional-trial true and Main RULES promotion false
- rich standalone schema and forbidden-dependency validation pass
- multi-topic batch preflight happens before the first write
- collision, duplicate, path, namespace, traversal, and symlink tests pass
- no active overwrite parameter/CLI/help/report path remains
- replay remains no-write; trial/readiness use the shared rich validator
- temporary smoke proves independent files, zero-write collision behavior, byte preservation, and Main RULES digest equality
- focused and full package suites pass in both source and clean release clone
- README/manifest/package version align to `0.1.78` / `0.9.30`
- exact plugin-only staged scope is verified
- branch, tag, GitHub Release, and fresh tagged-clone parity are verified after explicit external-action confirmation
- every selected design obligation is marked verified, deferred, blocked, not applicable, or out of scope

## Verification record fields

At execution closeout, record observed values for every field below; do not prefill them from planned or worker-reported results:

- baseline command and result
- RED tests and their missing-mechanism failures
- focused GREEN commands and results
- temporary smoke results for single/batch/collision/symlink/Main RULES digest checks
- full source-suite command and result
- clean release-clone suite command and result
- release commit SHA and exact staged scope
- verified remote branch SHA
- annotated tag and peeled commit
- GitHub Release URL and status
- fresh-tag clone command and result
- checked coverage and explicit exclusions
- evidence-calibrated confidence statement

## Rollback / containment

Before external release:
- revert only Phase 013-01 source/governed changes in the clean release candidate
- do not modify or remove existing runtime additional-stage artifacts
- do not reset or clean the main RULES working tree

After branch push but before tag/release:
- push a corrective commit or delete only the dedicated unreleased branch after explicit confirmation

After published tag/release:
- do not force-move the tag or silently replace the release
- publish a corrective plugin version if runtime behavior is wrong
- release deletion/tag deletion requires separate destructive confirmation and is not the default rollback

Main RULES bodies, unrelated RULES changes, other plugins, the fifteen existing additional-stage artifacts, and Phases 017-018 remain protected throughout.
