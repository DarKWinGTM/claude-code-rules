# Phase 013-01-02 — Atomic Emission, Runtime Verification, and Version Sync

> **Parent Phase:** [phase-013-01-deterministic-standalone-additional-stage-emission.md](phase-013-01-deterministic-standalone-additional-stage-emission.md)
> **Summary File:** [SUMMARY.md](SUMMARY.md)
> **Current Version:** 0.1.78
> **Status:** Completed / verified in local source/test/smoke scope
> **Target Design:** [../design/design.md](../design/design.md) v0.1.78
> **Patch Reference:** [../patch/deterministic-standalone-additional-stage-emission.patch.md](../patch/deterministic-standalone-additional-stage-emission.patch.md)
> **Session:** 48a3ef9b-50cf-4574-8f00-4f6b6e28f76e (2026-08-09)

---

## Objective

Implements full-set preflight, exclusive writes, public follow-up state, replay/trial/readiness alignment, isolated smoke verification, and v0.1.78 / 0.9.30 sync.

## Inherited boundaries

- Initial analysis remains read-only and advisory.
- One selected topic maps to one artifact.
- Existing additional-stage files are preserved; no overwrite path is active.
- Main RULES and Phases 017-018 remain unchanged.
- Completion wording is limited to direct verification evidence.

---

### Task 5: Add atomic multi-topic preflight, exclusive writes, and root/symlink containment

**Files:**
- Modify: `lib/candidate_packet.py:39-92,477-592`
- Create: `tests/test_candidate_packet_cli.py`
- Modify: `tests/test_candidate_packet.py`
- Modify: `bin/memory-context-intelligence:7-52,87-110`

**Interfaces:**

Add:

```python
def preflight_selected_emission(
    packet_reports: list[dict[str, Any]],
    *,
    additional_root: str | None = None,
) -> dict[str, Any]:
    ...


def emit_selected_additional(
    packet_reports: list[dict[str, Any]],
    *,
    additional_root: str | None = None,
    approved_write: bool = False,
) -> dict[str, Any]:
    ...
```

Keep the single-topic wrapper:

```python
def emit_additional(
    packet_report: dict[str, Any],
    *,
    additional_root: str | None = None,
    approved_write: bool = False,
) -> dict[str, Any]:
    return emit_selected_additional(
        [packet_report],
        additional_root=additional_root,
        approved_write=approved_write,
    )["items"][0]
```

Remove `allow_overwrite` from Python signatures, CLI parsers, reports, shell help, and callers.

- [x] **Step 1: Add batch/collision/path RED tests**

Add to `test_candidate_packet.py`:
- `test_selected_batch_writes_one_independent_artifact_per_topic`
- `test_batch_collision_rejects_entire_set_before_first_write_and_preserves_bytes`
- `test_duplicate_batch_destinations_are_rejected_before_write`
- replace `test_overwrite_requires_explicit_allow_overwrite` with `test_existing_destination_is_always_rejected_and_bytes_preserved`
- `test_additional_root_namespace_traversal_and_symlink_escape_fail_closed`

Use `<temp>/rules/additional` as the root, not an arbitrary temp directory. Collision test setup:

```python
sentinel = additional_root / "memory-context-intelligence" / "second.md"
sentinel.parent.mkdir(parents=True)
sentinel.write_bytes(b"existing-sentinel")

with self.assertRaises(candidate_packet.CandidatePacketError):
    candidate_packet.emit_selected_additional(
        [first_packet, second_packet],
        additional_root=str(additional_root),
        approved_write=True,
    )

self.assertFalse((sentinel.parent / "first.md").exists())
self.assertEqual(sentinel.read_bytes(), b"existing-sentinel")
```

- [x] **Step 2: Add CLI RED tests**

Create `test_candidate_packet_cli.py` covering:
- repeatable `emit-selected --packet-report`
- no `--allow-overwrite` in candidate parser help
- no `--allow-overwrite` in shell status/help
- batch collision returns exit code `2`
- collision creates no first file and preserves sentinel bytes

- [x] **Step 3: Confirm RED**

```bash
python3 -m pytest -q tests/test_candidate_packet.py tests/test_candidate_packet_cli.py
```

Expected: FAIL on missing batch API, obsolete overwrite behavior, and weak root contract.

- [x] **Step 4: Implement full-set preflight**

For every packet before any write:
1. require `selected_for_additional_trial is True`
2. require `main_rules_promotion_approved is False`
3. reject packet stop gates
4. render and validate standalone material
5. require root basename `additional`
6. require relative path first segment exactly `memory-context-intelligence`
7. reject duplicate resolved destinations
8. reject every existing destination
9. reject symlink components in the selected root, namespace directory, destination parent chain, and destination
10. resolve/recheck final containment

Return:

```python
{
    "status": "preflight-passed",
    "all_destinations_preflighted": True,
    "selected_for_additional_trial": True,
    "main_rules_promotion_approved": False,
    "items": [
        {
            "destination_path": str,
            "destination_relative_path": str,
            "preview_material": str,
            "standalone_validation": dict,
        }
    ],
}
```

- [x] **Step 5: Implement exclusive batch writes and bounded rollback**

After complete preflight, write each destination with exclusive create mode:

```python
with destination.open("x", encoding="utf-8") as handle:
    handle.write(material)
```

Track only files created by this call. If a later exclusive write fails, remove only those newly created files, never pre-existing files, and re-raise `CandidatePacketError` with the failed destination. Do not add an overwrite compatibility branch.

- [x] **Step 6: Add CLI surfaces**

`packet` adds:
- repeatable `--integration-anchor`
- `--selected-for-additional-trial`

Add internal command:

```text
emit-selected --packet-report <packet.json> [--packet-report <packet-2.json>] --additional-root <...> [--approved-write]
```

Keep `emit` as the one-packet wrapper. Update the shell command map/status text and unknown-command guidance. Do not expose `packet` or `emit-selected` as new public slash commands.

- [x] **Step 7: Run GREEN checks**

```bash
python3 -m pytest -q tests/test_candidate_packet.py tests/test_candidate_packet_cli.py
```

Expected: both files pass with no overwrite path.

---

### Task 6: Make presentation and the analysis skill describe the deterministic later follow-up

**Files:**
- Modify: `lib/presentation.py:664-753,864-910`
- Modify: `skills/analysis/SKILL.md:50-98,117-175`
- Modify: `tests/test_presentation.py`
- Modify: `tests/test_analysis_skill_contract.py`
- Run unchanged regression: `tests/test_analysis_surface.py`

**Interfaces:**
- Every initial topic card and `present` report carries:

```python
"selected_for_additional_trial": False,
"main_rules_promotion_approved": False,
```

- Ordinary `choose` output also carries both flags as false. A chosen topic is selected for analysis follow-up, not approved for file creation.

- [x] **Step 1: Add presentation RED tests**

Add:
- `test_initial_presentation_keeps_trial_and_promotion_unselected`
- `test_next_action_bridge_describes_explicit_additional_trial_follow_up`

Assert the Topic cards and report keep both states false and the action bridge explains that an explicit later request can select Topic N for additional-stage trial creation. It must not promise automatic execution.

- [x] **Step 2: Add skill-contract RED test**

Add `test_analysis_skill_keeps_initial_analysis_read_only_and_requires_explicit_follow_up_selection` asserting that the skill text contains:
- initial analysis remains read-only/advisory
- explicit later selection flips additional-trial selection only
- `main_rules_promotion_approved=False`
- one packet/artifact per selected topic
- full-set preflight before write
- collision refusal and preservation
- no overwrite option
- no internal template/routing/source-sync question when defaults apply
- no Main RULES mutation

- [x] **Step 3: Confirm RED**

```bash
python3 -m pytest -q \
  tests/test_presentation.py \
  tests/test_analysis_skill_contract.py \
  tests/test_analysis_surface.py
```

Expected: new tests fail while existing analysis-surface tests remain green.

- [x] **Step 4: Implement the public wording/state contract**

Replace generic “change proposal or goal draft” next-action wording with explicit later additional-stage trial selection. Add a dedicated post-presentation follow-up subsection to the skill:

```text
user explicitly selects one or several Topic N values and says proceed
→ mark each independent packet selected_for_additional_trial=True
→ keep main_rules_promotion_approved=False
→ normalize and entailment-check each topic
→ perform one emit-selected full-set preflight
→ write only after every destination passes
```

Questions are allowed only for actual ambiguity in topic identity, owner mapping, destination, collision resolution, or another approval/safety boundary.

- [x] **Step 5: Run GREEN checks**

```bash
python3 -m pytest -q \
  tests/test_presentation.py \
  tests/test_analysis_skill_contract.py \
  tests/test_analysis_surface.py
```

Expected: all pass; initial analysis still performs no write.

---

### Task 7: Align replay, live trial, and readiness with the new emitter contract

**Files:**
- Modify: `lib/historical_replay.py`
- Modify: `lib/live_trial.py:41-122,380-418,447-524`
- Modify: `lib/readiness.py:45-109,291-365,493-633`
- Modify: `tests/test_historical_replay.py`
- Modify: `tests/test_live_trial.py`
- Modify: `tests/test_readiness.py`

**Interfaces:**
- Replay: preview only, `selected_for_additional_trial=False`, no write authority.
- Live trial: packet uses `selected_for_additional_trial=True`, promotion false, no overwrite state.
- Readiness: imports/reuses `validate_standalone_artifact`; rich validity and no forbidden dependencies become gates.
- Command map adds `emit-selected` as an internal command.

- [x] **Step 1: Add/replace RED assertions**

Live trial assertions:

```python
self.assertTrue(report["selected_for_additional_trial"])
self.assertFalse(report["main_rules_promotion_approved"])
self.assertTrue(report["emission_checks"]["standalone_artifact_valid"])
self.assertEqual(report["emission_checks"]["forbidden_dependencies"], [])
self.assertNotIn("allow_overwrite", report["emission"])
```

Readiness adds a negative thin-artifact test and requires the rich validator result. Historical replay asserts selection remains false and preview remains no-write.

- [x] **Step 2: Confirm RED**

```bash
python3 -m pytest -q \
  tests/test_historical_replay.py \
  tests/test_live_trial.py \
  tests/test_readiness.py
```

Expected: FAIL on missing selection/promotion/rich-validation fields and obsolete overwrite plumbing.

- [x] **Step 3: Remove overwrite plumbing and reuse the validator**

Delete `--allow-overwrite` from live-trial/readiness parsers and calls. Replace the current two-heading checks with `candidate_packet.validate_standalone_artifact(material)`. A trial/readiness artifact is acceptable only when:
- full rich schema is valid
- forbidden dependency list is empty
- selected-for-trial is true
- Main RULES promotion is false
- Main RULES before/after digest is unchanged when the root is supplied

- [x] **Step 4: Run GREEN checks**

```bash
python3 -m pytest -q \
  tests/test_historical_replay.py \
  tests/test_live_trial.py \
  tests/test_readiness.py
```

Expected: all pass.

---

### Task 8: Run controlled temporary-HOME and additional-root smoke verification

**Files:**
- No persistent source file created.
- Temporary artifacts only under a session-unique `mktemp` directory.

**Interfaces:**
- Uses package-local Python/CLI surfaces.
- Must not touch `/home/node/.claude/rules/additional/memory-context-intelligence/`.

- [x] **Step 1: Prepare an isolated runtime root**

```bash
cd /home/node/workplace/AWCLOUD/TEMPLATE/RULES/plugin/memory-context-intelligence
SMOKE_ROOT="$(mktemp -d /tmp/mci-v0.9.30-smoke.XXXXXX)"
export HOME="${SMOKE_ROOT}/home"
export MCI_ADDITIONAL_ROOT="${SMOKE_ROOT}/rules/additional"
mkdir -p "${HOME}" "${MCI_ADDITIONAL_ROOT}"
```

- [x] **Step 2: Capture Main RULES before digest**

Hash only root Runtime Rule markdown bodies selected by the current source-owned Main RULES scope; persist the digest list under `${SMOKE_ROOT}`, not in the repository.

- [x] **Step 3: Exercise one-topic preview/write and two-topic batch write**

Build two independent packet reports with `--selected-for-additional-trial`, then run:

```bash
bash ./bin/memory-context-intelligence emit-selected \
  --packet-report "${SMOKE_ROOT}/topic-1.json" \
  --packet-report "${SMOKE_ROOT}/topic-2.json" \
  --additional-root "${MCI_ADDITIONAL_ROOT}" \
  --approved-write
```

Assert two distinct files exist under `memory-context-intelligence/`, each body contains one Topic ID, and neither body contains the other Topic ID.

- [x] **Step 4: Exercise collision and byte preservation**

Pre-create the second batch destination with sentinel bytes, choose a new first destination, rerun the batch, and assert:
- command exits `2`
- first destination does not exist
- sentinel SHA-256 is unchanged
- no other destination was created

- [x] **Step 5: Exercise traversal and symlink rejection**

Create a symlink from the selected namespace or destination parent toward an outside directory. Assert the command exits `2` and the outside target remains unchanged.

- [x] **Step 6: Verify Main RULES digest equality**

Recompute the selected Main RULES digest list and compare byte-for-byte. Expected: equal.

- [x] **Step 7: Record evidence limits**

Claim only `temporary local runtime path verified-in-scope`. This smoke does not prove installed plugin runtime, marketplace publication, or stability.

---

### Task 9: Run the full suite and synchronize v0.1.78 / package 0.9.30

**Files:**
- Modify after green runtime evidence: `.claude-plugin/plugin.json`
- Modify after green runtime evidence: `README.md`
- Modify after green runtime evidence: `tests/test_plugin_manifest.py`
- Finalize: `changelog/changelog.md`
- Finalize: `changelog/v0.1.78-deterministic-standalone-additional-stage-emission.changelog.md`
- Finalize: `phase/SUMMARY.md`
- Finalize: this phase file
- Finalize: `patch/deterministic-standalone-additional-stage-emission.patch.md`
- Update local durable index: `/home/node/workplace/AWCLOUD/TEMPLATE/RULES/TODO.md`

- [x] **Step 1: Run the complete package suite before version bump**

```bash
cd /home/node/workplace/AWCLOUD/TEMPLATE/RULES/plugin/memory-context-intelligence
python3 -m pytest -q tests
```

Expected: PASS. If date-sensitive failures remain, report exact failing fixtures and keep implementation/release blocked; do not reuse the historical “6 failures / 4 errors” report as current proof.

- [x] **Step 2: Bump package-facing versions**

Change:
- `.claude-plugin/plugin.json`: `0.9.29 → 0.9.30`
- `README.md`: governed `0.1.77 → 0.1.78`, package `0.9.29 → 0.9.30`, current behavior/status wording
- `tests/test_plugin_manifest.py`: expected manifest version `0.9.30`

README user-facing wording must explain only:
- initial analysis remains read-only
- explicit later Topic selection uses deterministic defaults
- one rich standalone file per topic
- full-set preflight and collision refusal/no overwrite
- Main RULES promotion is separate

Do not expose internal function names or claim release before it happens.

- [x] **Step 3: Finalize governed implementation evidence**

Update the v0.1.78 changelog body, patch verification section, phase summary, and this phase with exact commands/results. Keep release status as `pending external release` until GitHub actions complete. Preserve the pre-rollover summary snapshot and movement links.

- [x] **Step 4: Rerun version and full checks**

```bash
python3 -m pytest -q tests/test_plugin_manifest.py tests/test_analysis_skill_contract.py
python3 -m pytest -q tests
```

Expected: PASS at package 0.9.30.

## Execution result

Completed in the main session.

Verification:
- atomic selected-set preflight, duplicate/existing-destination refusal, exclusive writes, bounded same-call rollback, and additional-root namespace/symlink containment passed focused tests
- presentation and analysis-skill contracts keep initial analysis and ordinary Topic choice unselected while documenting the explicit later trial-creation request
- historical replay remains no-write/unselected; live trial and readiness require trial selection, deny promotion, and reuse the rich standalone validator
- controlled temporary-HOME/additional-root smoke created two independent artifacts, preserved collision bytes, rejected traversal and symlink escape, and kept the checked Main RULES digest unchanged
- pre-version-bump full suite: `132 passed`
- package version synchronized to `0.9.30`; governed version remains `0.1.78`
- post-version manifest/skill checks: `20 passed`
- post-version full suite: `132 passed`
- `claude plugin validate` passed

Covers: local source, tests, controlled smoke, package metadata, and package structural validation.

Does not cover: clean release-clone parity, remote push/tag/release, fresh-tag behavior, marketplace installation, or stability over time.

---
