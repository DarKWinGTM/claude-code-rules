# Deterministic standalone additional-stage emission patch

> **Current Version:** 0.1.78
> **Session:** 48a3ef9b-50cf-4574-8f00-4f6b6e28f76e (2026-08-09)
> **Status:** implemented and verified in local source/test/smoke scope; external release pending
> **Target Design:** [../design/05-additional-staging-and-promotion.design.md](../design/05-additional-staging-and-promotion.design.md)
> **Full history:** [../changelog/changelog.md](../changelog/changelog.md)

---

## Context

The plugin already presents advisory Topic cards and already has one-topic packet/emission guards. The missing source contract begins after the user reviews those cards and explicitly selects one or several topics for additional-stage execution.

Current packet emission is too thin for standalone doctrine, retains raw evidence anchors in packet state, supports an active overwrite flag, and does not provide one atomic full-set preflight/write path for a selected multi-topic batch. The approved v0.1.78 design keeps initial analysis read-only while making the later explicit follow-up deterministic and additional-stage-first.

## Analysis

### Before

- the analysis surface presents advisory Topic cards and stops correctly without writing
- the follow-up text points generally toward proposals or goal drafts rather than the governed additional-stage preset
- selected state does not explicitly separate additional-stage authorization from Main RULES promotion authorization
- the renderer emits a thin artifact whose meaning can depend on packet-local/raw evidence context
- internal packet reports may carry trace/source anchors directly into rendering inputs
- multi-topic carry-forward is rejected as one combined packet, but there is no deterministic independent per-topic batch preflight/write transaction
- `--allow-overwrite` remains an active CLI/runtime path
- destination checks do not yet prove the full selected namespace and symlink containment contract required by v0.1.78

### After

- initial `/memory-context-intelligence:analysis` behavior remains read-only and advisory
- explicit later user selection activates the governed additional-stage preset without asking internal routing questions
- selection state explicitly records additional-stage approval and denies Main RULES promotion approval
- every selected topic is normalized, entailment-checked, packetized, and rendered independently
- emitted artifacts contain the complete rich standalone doctrine schema
- forbidden transient evidence dependencies fail validation before emission
- all selected destinations are derived and preflighted before any write
- any collision rejects the entire selected set and preserves all existing bytes
- the deterministic workflow exposes no active overwrite option
- writes remain contained under `<additional-root>/memory-context-intelligence/`, including traversal and symlink-escape checks

## Change items

### 1. Post-presentation assistant contract — replacement

**Targets:**
- `skills/analysis/SKILL.md`
- `lib/presentation.py`
- focused analysis-skill and presentation tests

**Before:** topic selection remains advisory but the next-action bridge does not encode the deterministic additional-stage follow-up or the separate promotion state.

**After:** first-response analysis still performs no write; explicit later selection is represented as additional-stage-only authorization with deterministic defaults and no Main RULES promotion approval.

### 2. Candidate normalization and entailment — additive

**Targets:**
- `lib/candidate_packet.py`
- focused candidate-packet tests

**Before:** packet evidence may preserve raw trace/source anchors without a required standalone semantic normalization gate.

**After:** internal raw evidence remains available for audit, while emission consumes a normalized standalone evidence model and rejects unrelated, context-only, incomplete, or forbidden-reference output according to the approved entailment state.

### 3. Rich standalone renderer — replacement

**Targets:**
- `lib/candidate_packet.py`
- `tests/test_candidate_packet.py`

**Before:** rendered additional material contains a thin summary, counts, owner mapping, and lifecycle sections.

**After:** rendered material includes title/trial metadata, one selected topic, intended Main RULES owner and integration anchors, `Main RULES mutation: Not performed`, candidate summary, core principle, operating clauses, before/after behavior, normalized evidence basis, owner reasoning, trial-first rationale, risks, success criteria, rollback notes, stop gates, leader verification needs, and promotion boundary.

### 4. Atomic multi-topic batch emission — additive

**Targets:**
- `lib/candidate_packet.py`
- `bin/memory-context-intelligence`
- focused CLI/candidate-packet tests

**Before:** one combined multi-topic packet is rejected, but selected topics do not have one independent-packet batch transaction that preflights every destination before writing.

**After:** the batch path builds one packet/report/destination per topic, validates the whole set, rejects duplicate destinations or any existing destination, and only then writes every new file.

### 5. Collision, overwrite, and containment hardening — replacement

**Targets:**
- `lib/candidate_packet.py`
- `lib/live_trial.py`
- `lib/readiness.py`
- `bin/memory-context-intelligence`
- candidate-packet/live-trial/readiness tests

**Before:** the emitter accepts an `allow_overwrite` parameter and CLI flag, and root checks do not fully express namespace-plus-symlink containment for the selected workflow.

**After:** the deterministic selected-topic path has no active overwrite option, resolves only under an additional-stage root plus `memory-context-intelligence/`, refuses root/path/symlink escape, and keeps live-trial/readiness evidence aligned with collision-safe standalone emission.

### 6. Governed and package-facing synchronization — replacement

**Targets:**
- `phase/phase-013-01-deterministic-standalone-additional-stage-emission.md`
- `phase/phase-013-01-01-evidence-normalization-and-standalone-rendering.md`
- `phase/phase-013-01-02-atomic-emission-runtime-verification-and-version-sync.md`
- `phase/phase-013-01-03-plugin-release-and-fresh-tag-verification.md`
- `phase/phase-013-candidate-packet-builder-and-additional-emitter.md`
- `phase/SUMMARY.md` and `phase/history/2026-08-09*.md`
- `changelog/changelog.md` and the v0.1.78 shard
- root `TODO.md`
- `README.md`
- `.claude-plugin/plugin.json`
- manifest/version tests when the runtime implementation lands

**Before:** governed design is at v0.1.78 while runtime/package surfaces still describe the v0.1.77 / package 0.9.29 baseline.

**After:** implementation and verification evidence align the plugin-governed chain to v0.1.78 and package version 0.9.30 without changing Main RULES or reopening Phases 017-018.

### 7. Plugin-only Git and release closeout — additive

**Targets:**
- canonical repository `/home/node/workplace/AWCLOUD/TEMPLATE/RULES`
- one dedicated plugin release branch derived from the verified repository baseline
- exact plugin/governed allowlist from this wave
- plugin package tag for `0.9.30`
- GitHub repository `DarKWinGTM/claude-code-rules`

**Before:** v0.1.78 design/planning and local implementation may exist only in the extensively modified working tree, with no published package-version proof.

**After:** only the verified plugin wave is committed and pushed; unrelated RULES and other-plugin changes remain outside the commit; the plugin package tag and GitHub Release identify version `0.9.30`; fresh remote/tag/release inspection proves parity with the locally tested allowlist.

The current repository has extensive unrelated modified and untracked files. Release preparation must therefore use an exact allowlist and inspect the staged diff before commit. A clean-working-tree claim is neither expected nor required, but unrelated paths in the release commit are forbidden.

## Verification

Use `new_focused_test` as the selected verification route.

Required sequence:
1. capture the current focused-test and full-suite baseline without upgrading worker-reported results into proof
2. add focused failing tests for state separation, rich schema, entailment/normalization, forbidden references, independent batch preflight, collision preservation, no-overwrite CLI behavior, and root/path/symlink containment
3. run each focused test file to confirm RED for the intended missing mechanism
4. implement the smallest source changes that satisfy the approved design
5. rerun focused tests to GREEN
6. run a controlled temporary-HOME/additional-root smoke flow covering single-topic creation, multi-topic split, collision-before-write, byte preservation, and Main RULES unchanged evidence
7. run the full plugin test suite and classify any date-sensitive fixture failures from fresh output rather than historical worker reports
8. sync README/manifest/changelog/phase/TODO only to the strongest evidence reached

Observed verification results:
- focused RED tests failed on the intended missing state, renderer, batch, collision, containment, and consumer-alignment mechanisms before implementation
- focused GREEN implementation checks passed across signals/orchestration, candidate packet/CLI, presentation/skill, replay/live-trial/readiness, and intake scopes
- controlled temporary-HOME/additional-root smoke passed for two independent artifacts, collision-before-write with byte preservation, traversal rejection, symlink rejection, and checked Main RULES digest equality
- pre-version-bump full suite: `132 passed`
- post-version manifest/skill checks: `20 passed`
- post-version full suite: `132 passed`
- package validation: `claude plugin validate` passed

Covers: local plugin source behavior, package metadata, rich standalone rendering, selection/promotion separation, batch preflight, collision preservation, exclusive writes, containment, and local package structure.

Does not cover: marketplace installation, remote branch/tag parity, GitHub Release publication, fresh-tag execution, or stability over time.

No `fixed`, `runtime/live-verified`, `stable`, or release-ready claim is made beyond this checked scope.

## Rollback approach

Rollback source and governed v0.1.78 changes as one bounded plugin-local wave while preserving:
- all pre-existing files under `~/.claude/rules/additional/memory-context-intelligence/`
- the twelve already-created standalone trial artifacts
- the three earlier preserved trial artifacts
- Main RULES bodies
- deferred Phases 017-018
- unrelated root TODO and RULES work

Do not delete or overwrite emitted trial files as part of rollback without separate explicit destructive authorization. If a newly created test artifact under a controlled temporary root must be removed, keep that cleanup limited to the temporary test scope.
