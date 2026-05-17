# Observed Shape, Extracted Doctrine, and Selected Target Form Separation Patch

> **Current Version:** 1.0
> **Session:** 1f1873d2-0feb-485f-a5ff-d383254590dd
> **Status:** Active / In Progress
> **Target Design:** [design/design.md](../design/design.md) v10.11
> **Full history:** [changelog/changelog.md](../changelog/changelog.md)

---

## Context

This is the governed patch record for `v10.11 / P103`.

It packages a wording/evidence refinement wave so AI must keep observed project shape, extracted doctrine, and selected target form separate when using checked examples to justify governance or normalization choices.

---

## Analysis

The released `v10.10 / P102` wave made chain-shape selection explicit, but it still left one attribution/wording gap open.

The first issue is epistemic: the assistant can still talk about a selected RULES target form as if it were literally the observed structure of a checked project or example, even when the example only grounds a recommendation.

The second issue is procedural: current owner surfaces still need an explicit equivalence-basis field so observed source shape, extracted doctrine, and selected target form do not collapse into one unsupported claim during sync, review, or later reuse.

---

## Change Items

### 1) Observed shape / extracted doctrine / selected target separation

- **Target artifact:** `document-governance.md`, `phase-todo-artifact.md`, `worker-routing-and-context.md`
- **Change type:** additive refinement
- **Current state:** chain-shape doctrine exists, but observed example shape and selected target form can still be described too loosely as if they were the same thing.
- **Target state:** RULES explicitly separates observed project shape, extracted doctrine, selected target form, and equivalence-claim basis.
- **Review point:** keep this as wording/evidence refinement only; do not reopen P102 chain-shape selection itself.

### 2) Integrity and read/report wording expansion

- **Target artifact:** `document-integrity.md`, `safe-io.md`
- **Change type:** additive refinement
- **Current state:** integrity and read-order doctrine verifies structure, but it does not yet force explicit wording separation between observed example shape and selected target form.
- **Target state:** integrity and safe-read/report wording explicitly prevent example-pattern overclaiming unless checked equivalence evidence exists.
- **Review point:** preserve existing parent-first reading and no-drift structure checks while adding wording/evidence precision.

### 3) Companion chains and release surfaces

- **Target artifact:** touched owner design/changelog companions plus `README.md`, `design/design.md`, `changelog/changelog.md`, `TODO.md`, `phase/SUMMARY.md`, P103 phase record, and this patch
- **Change type:** release synchronization
- **Current state:** master surfaces identify `v10.10 / P102` as the current released wave with no active phase open.
- **Target state:** master surfaces identify `v10.11 / P103` as the active observed-shape/extracted-doctrine/selected-target wave until release verification passes.
- **Review point:** keep runtime install count at 18 and keep the `plugin/` tree reference-only and out of release scope.

---

## Verification

Required checks before release closeout:
- README Bash and PowerShell install arrays contain exactly the same 18 active runtime files.
- All 18 active source runtime files exist and have substantive bodies.
- Touched owner files keep resolvable design and changelog metadata links.
- The five target owners explicitly separate observed project shape, extracted doctrine, and selected target form.
- `docs_analysis` explicitly records equivalence-claim basis when a checked example is used.
- No touched owner implies that a selected RULES target form is literally the observed project pattern without checked equivalence proof.
- Current P102 chain-shape doctrine remains intact.
- `TODO.md` and `phase/SUMMARY.md` remain compact current entrypoints with reachable `history/` / `done/` references.
- Runtime install copies only README-listed active root runtime rules.
- Source/runtime parity and source/destination body sufficiency pass for 18/18 files.
- `shared-task-list-path-coordination.md` remains observed-only and outside the source-owned install set.
- The untracked `plugin/` tree remains outside staged release scope.
- Git diff has no whitespace errors.
- GitHub release `v10.11` must be created and verified before closeout wording claims release completion.

---

## Implementation Status

P103 is active and not yet released.

Phase/patch startup, touched doctrine-owner wording, companion/master-surface sync, local validation, runtime install, and 18/18 parity/body-sufficiency checks are complete from the released `v10.10 / P102` baseline. Push, GitHub release creation, and closeout verification are still pending.

---

## Rollback Approach

If P103 is reversed after release, restore the prior `v10.10 / P102` source state through a governed rollback release while keeping the compact 18-rule runtime install scope unchanged unless an explicit rollback gate selects another install action.

Do not treat the untracked `plugin/` tree, runtime destination extras, or existing history/done/archive surfaces as cleanup targets during rollback.
