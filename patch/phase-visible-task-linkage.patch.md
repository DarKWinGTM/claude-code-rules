# Phase-Visible Task Linkage Patch

## 0) Document Control

> **Current Version:** 1.0
> **Status:** Completed
> **Target Design:** [../design/design.md](../design/design.md) v9.85
> **Session:** d42465eb-30a7-4bc8-b9d6-03e52306e9a5
> **Full history:** [../changelog/changelog.md](../changelog/changelog.md)

---

## 1) Context

P076-03 refines phase-backed live task-list behavior after the user identified a practical RULES gap: after phase planning is complete and execution starts, Claude Code built-in task-list entries can still be created as generic tasks without visibly referencing the active phase.

พูดง่าย ๆ: Rules เดิมบอกให้ task list “ตาม phase” แต่ไม่ได้บังคับให้ task แต่ละอัน “เห็น phase” ใน subject หรือ description.

This is a refinement patch under the existing `076` design-to-phase execution synthesis family. It does not add a new active runtime rule. The active runtime install count remains 43.

---

## 2) Analysis

Risk level: Medium.

Dependencies:
- `phase-implementation.md` owns phase semantics, phase identity, and the core live task-list linkage contract.
- `todo-standards.md` owns built-in task-list live tracking behavior and task update discipline.
- `artifact-initiation-control.md` owns startup live-task posture and must initialize phase-backed live tasks with visible linkage.
- `project-documentation-standards.md` owns repository document-role boundaries and must keep task lists from becoming phase authority.
- `execution-continuity-and-mode-selection.md` owns next-work continuation and must prevent continuation-created tasks from losing phase context.

Review concerns:
- Do not make the built-in task list the authority for phase semantics.
- Do not force one exact subject grammar when another active title grammar or shared-board rule applies.
- Do not make phase-linkage overhead mandatory for trivial non-phase tasks.
- Do not widen the active runtime rule count.
- Do not touch plugin/shared-board task grammar or observed-only runtime destination extras.

---

## 3) Change Items

### PVTL-001 — Phase owner visible-link contract

- **Target artifacts:** `../phase-implementation.md`, `../design/phase-implementation.design.md`, `../changelog/phase-implementation.changelog.md`
- **Change type:** additive refinement / replacement of preference-only wording

**Before**
```text
`phase-implementation.md` says the built-in task list should mirror current phase execution slices and that current phase ID in task subjects is useful when it improves clarity.
```

**After**
```text
`phase-implementation` v2.27 requires Claude Code built-in task entries to visibly link to active or clearly implied phase context when phase-backed work is non-trivial. The link may appear in the subject or description; `P<phase-id>` is preferred when no stronger title grammar blocks it, and `phase_ref` or equivalent description linkage is required when subject linkage would conflict with another title grammar.
```

### PVTL-002 — Live task-list tracking owner sync

- **Target artifacts:** `../todo-standards.md`, `../design/todo-standards.design.md`, `../changelog/todo-standards.changelog.md`
- **Change type:** companion sync

**Before**
```text
`todo-standards` requires task creation to align with active/implied phase context and prefers phase IDs in subjects when useful, but visible linkage is not a required post-create condition.
```

**After**
```text
`todo-standards` v2.22 requires phase-backed or clearly phase-shaped live task entries to visibly expose phase ID/name/family or implied-stage context in subject or description, and to update entries immediately if a created/extended task lacks that visible linkage.
```

### PVTL-003 — Startup task initialization sync

- **Target artifacts:** `../artifact-initiation-control.md`, `../design/artifact-initiation-control.design.md`, `../changelog/artifact-initiation-control.changelog.md`
- **Change type:** companion sync

**Before**
```text
Startup live task-list initialization is expected for active phase work, but the startup owner does not state that initialized tasks must show phase linkage.
```

**After**
```text
`artifact-initiation-control` v1.8 states that when live task-list initialization happens under active or clearly implied phase context, the initial task entries should be phase-linked from the start rather than becoming generic live-tracking tasks.
```

### PVTL-004 — Documentation and continuation boundary sync

- **Target artifacts:** `../project-documentation-standards.md`, `../execution-continuity-and-mode-selection.md`, and their companion design/changelog files
- **Change type:** companion sync

**Before**
```text
Repository role boundaries correctly say the built-in task list is live tracking and not phase authority, while execution continuity discovers work from task/phase/TODO/design surfaces. Neither owner explicitly blocks phase-hidden task entries during phase-shaped continuation.
```

**After**
```text
`project-documentation-standards` v2.33 keeps the task list non-authoritative while requiring visible pointers back to active/implied phase context for phase-backed work. `execution-continuity-and-mode-selection` v1.11 requires continuation-created or continuation-extended task entries to preserve visible phase linkage instead of becoming generic next-work tasks.
```

### PVTL-005 — Master governed record sync

- **Target artifacts:** `../design/design.md`, `../changelog/changelog.md`, `../README.md`, `../TODO.md`, `../phase/SUMMARY.md`
- **Change type:** governed sync

**Before**
```text
Master records describe v9.84/P073-09 as the current release and P076-02 as the latest phase-family refinement for phase lineage. They do not yet record P076-03 phase-visible task linkage.
```

**After**
```text
Master records describe v9.85/P076-03 with the active runtime count still 43, because P076-03 refines existing phase/startup/task/documentation/execution-continuity owners rather than adding a runtime rule.
```

### PVTL-006 — P076-03 phase record and release boundary

- **Target artifact:** `../phase/phase-076-03-phase-visible-task-linkage.md`
- **Change type:** additive phase record

**Before**
```text
No P076-03 child phase record exists for phase-visible task linkage.
```

**After**
```text
A P076-03 phase record tracks owner-chain refinement, master governed sync, runtime install/parity, git push, and GitHub release `v9.85` gates.
```

---

## 4) Verification

- [x] `phase-implementation` runtime/design/changelog updated and audited at v2.27.
- [x] `artifact-initiation-control` runtime/design/changelog updated and audited at v1.8.
- [x] `project-documentation-standards` runtime/design/changelog updated and audited at v2.33.
- [x] `todo-standards` runtime/design/changelog updated and audited at v2.22.
- [x] `execution-continuity-and-mode-selection` runtime/design/changelog updated and audited at v1.11.
- [x] Master records, README, TODO, phase, and patch describe P076-03/v9.85 consistently.
- [x] README Bash and PowerShell install arrays remain exactly 43 active runtime files.
- [x] Runtime install parity is verified for the 43 active runtime rule files.
- [x] Source/runtime release artifacts are pushed and GitHub release `v9.85` is created.

---

## 5) Rollback Approach

If P076-03 proves too rigid:
- narrow the visible-linkage contract while preserving that silent internal phase alignment is insufficient for phase-backed non-trivial task entries
- keep `phase-implementation.md` as the phase identity and task-linkage owner
- keep `todo-standards.md` as the live task-list mechanics owner
- preserve subject-or-description flexibility and `phase_ref` fallback when stronger title grammar applies
- keep built-in task lists as live execution pointers, not phase authority
- revert master v9.85 records only through a governed rollback
- keep active runtime count at 43 unless a separate governed wave changes the runtime install set
