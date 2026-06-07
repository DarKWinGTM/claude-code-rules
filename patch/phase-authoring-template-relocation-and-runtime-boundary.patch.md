# Phase Authoring Template Relocation and Runtime Boundary Patch

> **Current Version:** 1.0
> **Session:** 1f1873d2-0feb-485f-a5ff-d383254590dd
> **Status:** Complete / Released
> **Target Design:** [../design/document-governance.design.md](../design/document-governance.design.md) v1.15
> **Full history:** [../changelog/changelog.md](../changelog/changelog.md)

---

## Context

This is the governed patch record for the P142 wave.

It packages one bounded repository-boundary clarification: the phase authoring template should live under `template/` as a support-only scaffold instead of sitting in the root active product RULES surface where it reads like an active runtime Rule.

---

## Analysis

Before this wave:
- the file was named `phase-implementation-template.md`
- it lived in the root RULES surface beside active runtime Rule files
- active docs described it as a helper, but its placement still made readers think it might be a real Rule
- the real phase doctrine already lived in `phase-todo-artifact.md` plus governed `phase/` surfaces

The better posture is:
- keep the template available and reusable
- move it into a dedicated template support directory
- rename it so the file itself says “authoring template” instead of “phase implementation”
- keep runtime phase authority explicit and separate

---

## Change Items

### 1) Template relocation and rename

- **Target artifacts:** `phase-implementation-template.md` → `template/phase-authoring-template.md`
- **Change type:** relocation / naming clarification
- **Current state:** root placement and old name make the file look like an active Rule.
- **Target state:** the template lives under `template/` and clearly reads as a support-only authoring scaffold.
- **Review point:** the file remains reusable without reading like installed runtime authority.

### 2) Current-state classification cleanup

- **Target artifacts:** `README.md`, `document-governance.md`, `diagram/STRUCTURE.md`, and touched active design docs that classify repository roles
- **Change type:** active current-state clarification
- **Current state:** root-level wording and old path references create ambiguity about what is a Rule versus what is support material.
- **Target state:** current-state docs classify the relocated template consistently as support-only / non-runtime / non-authority and keep phase doctrine authority with `phase-todo-artifact.md` plus governed `phase/` surfaces.
- **Review point:** active docs should not leave root-placement ambiguity behind.

### 3) Current-state and release sync

- **Target artifacts:** `TODO.md`, `phase/SUMMARY.md`, `phase/phase-142-phase-authoring-template-relocation-and-runtime-boundary.md`, `patch/phase-authoring-template-relocation-and-runtime-boundary.patch.md`, `changelog/changelog.md`, and `changelog/changelog/v10.50-released-phase-authoring-template-relocation-and-runtime-boundary.changelog.md`
- **Change type:** execution/release synchronization
- **Current state:** the latest released baseline is still `v10.49 / P141`; P142 exists only as the selected goal and route plan.
- **Target state:** current-state and release-history surfaces align to one promoted `v10.50 / P142` baseline after verification/publish closeout.
- **Review point:** release wording must follow actual verification and publish evidence.

---

## Verification

Required checks before release closeout:
- `template/phase-authoring-template.md` exists and the old root template path is gone
- checked active references no longer make the relocated template read like an active Rule
- active phase doctrine location is explicit: `phase-todo-artifact.md` plus governed `phase/` surfaces
- runtime install scope remains correct and does not absorb the template into the active payload
- touched design/changelog/TODO/phase/patch/master-changelog/detail surfaces align to `v10.50 / P142`
- touched runtime owners are installed/updated and verified for source/runtime parity + body sufficiency
- `git diff --check` passes
- the selected scope is pushed to `master`, tagged, and GitHub release verification passes

---

## Rollback Approach

If the relocation proves too disruptive, restore the old path only temporarily while keeping the support-only classification explicit; do not promote the template into runtime as a shortcut. Any longer-term rollback should still preserve the separation between runtime phase authority and support scaffolding.

---

## Implementation Status

P142 is completed.

The template relocation and active-reference cleanup are in place in checked scope, touched design/changelog/TODO/phase/patch/master-changelog/detail surfaces are aligned to `v10.50 / P142`, runtime/install-scope verification plus source/runtime parity and body sufficiency passed for the touched runtime owner, `git diff --check` passed, and push to `master`, tag `v10.50`, and GitHub release verification passed. Release URL: https://github.com/DarKWinGTM/claude-code-rules/releases/tag/v10.50
