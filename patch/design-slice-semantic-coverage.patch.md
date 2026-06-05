# Design-Slice Semantic Coverage Patch

> **Current Version:** 1.0
> **Session:** 1f1873d2-0feb-485f-a5ff-d383254590dd
> **Status:** Complete / Released
> **Target Design:** [../design/phase-todo-artifact.design.md](../design/phase-todo-artifact.design.md) v1.27
> **Full history:** [../changelog/changelog.md](../changelog/changelog.md)

---

## Context

This is the governed patch record for the P140 wave.

It packages one bounded doctrine refinement: when a governed design slice is selected for implementation, phase/task/verification execution must account for the selected semantic slice instead of stopping at the visible headline feature or happy-path action alone.

---

## Analysis

Before this wave:
- design already remained target-state truth
- phase already derived execution from design truth
- goal/task shaping already preferred outcome/output/gate over raw command buckets

The remaining gap was semantic coverage:
- selected design behavior could still narrow into only the visible action
- invariants, failure modes, durability/recovery expectations, or dependency semantics could still drop out of the active execution slice without explicit status
- closeout wording could still sound complete while part of the selected design contract remained silently uncovered

The better posture is:
- extract implementation-relevant obligations from the selected governed design slice
- keep phase/task surfaces compact without copying the whole design body
- require explicit status for selected semantic items before closeout
- make continuation/verification logic follow the full selected semantic slice rather than only the headline output

---

## Change Items

### 1) Phase/task semantic coverage owner hardening

- **Target artifacts:** `phase-todo-artifact.md`, `design/phase-todo-artifact.design.md`, `changelog/phase-todo-artifact.changelog.md`
- **Change type:** active doctrine refinement
- **Current state:** phase/task execution already derives from design truth, but selected semantic obligations can still disappear behind a visible feature headline.
- **Target state:** selected governed design slices now require semantic-item extraction and explicit status coverage before phase/task closeout.
- **Review point:** phase stays execution synthesis and does not become a second design authority.

### 2) Execution/continuation gate hardening

- **Target artifacts:** `execution-and-goal-frame.md`, `design/execution-and-goal-frame.design.md`, `changelog/execution-and-goal-frame.changelog.md`
- **Change type:** active doctrine refinement
- **Current state:** continuation already prefers goal/output/gate, but execution can still stop at the visible action while selected design obligations remain uncovered.
- **Target state:** selected design-slice obligation coverage now drives execution readiness, continuation, and completion boundaries.
- **Review point:** headline-output-only closeout is no longer sufficient when selected invariants, failure modes, or dependency semantics remain unclassified.

### 3) Release-surface sync

- **Target artifacts:** `TODO.md`, `phase/SUMMARY.md`, `phase/phase-140-design-slice-semantic-coverage.md`, `patch/design-slice-semantic-coverage.patch.md`, `changelog/changelog.md`, and `changelog/changelog/v10.48-released-design-slice-semantic-coverage.changelog.md`
- **Change type:** release synchronization
- **Current state:** the latest released baseline is still `v10.47 / P139`; P140 exists only as a selected goal and route plan.
- **Target state:** current-state and release-history surfaces align to one promoted `v10.48 / P140` baseline after verification/publish closeout.
- **Review point:** release wording must follow actual install/parity/branch/tag/release evidence rather than anticipatory success wording.

---

## Verification

Required checks before release closeout:
- selected design slices now require semantic coverage before phase/task closeout
- selected semantic items receive explicit status classification as `implemented`, `verified`, `deferred`, `blocked`, `not applicable`, or `out of scope`
- execution and closeout can no longer stop at a visible headline output while selected invariants, failure modes, or dependency semantics remain silently uncovered
- touched design/changelog/TODO/phase/patch/master-changelog/detail surfaces align to `v10.48 / P140`
- touched runtime owners are installed/updated and verified for source/runtime parity + body sufficiency
- `git diff --check` passes
- the selected scope is pushed to `master`, tagged, and GitHub release verification passes

---

## Implementation Status

P140 is completed.

The touched runtime owners now require selected design-slice semantic coverage before phase/task closeout, the companion design/changelog/TODO/phase/patch/master-changelog/detail surfaces are aligned to `v10.48 / P140`, touched runtime-owner install/update verification passed with source/runtime parity + body sufficiency in checked scope, `git diff --check` passed, and push/update to `master`, tag `v10.48`, and GitHub release verification passed.
