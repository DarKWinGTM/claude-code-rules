# Phase Lineage and Subphase Selection Refinement Patch

## 0) Document Control

> **Current Version:** 1.0
> **Status:** Completed
> **Target Design:** [../design/design.md](../design/design.md) v9.83
> **Session:** d42465eb-30a7-4bc8-b9d6-03e52306e9a5
> **Full history:** [../changelog/changelog.md](../changelog/changelog.md)

---

## 1) Context

P076-02 refines phase identity selection after the user identified a recurring RULES behavior problem: when follow-up work needs a phase file, the assistant tends to open the next major phase by default instead of checking whether the work continues an existing phase family and should be a subphase such as `076-02`.

พูดง่าย ๆ: phase ใหม่ไม่ได้แปลว่า major ใหม่เสมอไป. ถ้างานต่อเนื่องจาก family เดิม ต้องมีหลักเกณฑ์ให้พิจารณา current phase, subphase, new major, หรือ ask-now ก่อน.

This is a refinement patch under the existing `076` design-to-phase execution synthesis family. It does not add a new active runtime rule. The active runtime install count remains 43.

---

## 2) Analysis

Risk level: Medium

Dependencies:
- `phase-implementation.md` owns phase identity semantics and is the correct owner for major-vs-subphase selection.
- `artifact-initiation-control.md` owns startup posture only; phase `create now` must not imply a new major phase.
- `todo-standards.md` owns live task-list shaping; it must not silently allocate phase identity.
- `project-documentation-standards.md` owns repository documentation roles and lineage visibility; it must not replace phase identity semantics.
- `execution-continuity-and-mode-selection.md` owns continue/stop behavior; execution momentum must not allocate a new major phase.

Review concerns:
- Do not force subphases for unrelated work.
- Do not preserve old family lineage when nesting would overload or mislead that family.
- Do not treat completed phase status as an automatic lineage break.
- Do not let task creation, startup artifact creation, or execution continuation become hidden phase identity allocation.
- Do not increase the active runtime rule count.

---

## 3) Change Items

### PLS-001 — Phase identity owner refinement

- **Target artifact:** `../phase-implementation.md`
- **Change type:** additive refinement / replacement of implicit major-first behavior

**Before**
```text
`phase-implementation.md` defines the `NNN` and `NNN-NN` grammar and design-to-phase synthesis, but it does not explicitly require checked lineage before opening a new major phase.
```

**After**
```text
`phase-implementation.md` v2.26 adds a major-vs-subphase lineage gate: before opening a new major phase, inspect checked phase lineage and choose current-phase update, existing-family subphase, new major phase, or ask-now/recorded lineage basis. Subphase-fit and major-phase-fit signals are explicit, completed status does not automatically break lineage, and new concern wording does not automatically justify a new major phase.
```

### PLS-002 — Startup posture boundary

- **Target artifacts:** `../artifact-initiation-control.md`, `../design/artifact-initiation-control.design.md`, `../changelog/artifact-initiation-control.changelog.md`
- **Change type:** companion sync

**Before**
```text
Startup phase posture can resolve to `create now`, but the adjacent startup owner does not clearly state that creation still needs phase identity selection.
```

**After**
```text
`artifact-initiation-control` v1.7 states that phase `create now` delegates identity selection to `phase-implementation.md`, where the result may be current phase update, existing-family subphase, new major phase, or ask-now lineage handling.
```

### PLS-003 — Task-list and documentation boundary

- **Target artifacts:** `../todo-standards.md`, `../project-documentation-standards.md`, their design files, and their changelogs
- **Change type:** companion sync

**Before**
```text
Task-list shaping and repository documentation can reveal phase-shaped work, but the boundary against implicit new-major allocation is not explicit enough across both adjacent owners.
```

**After**
```text
`todo-standards` v2.21 and `project-documentation-standards` v2.32 keep live tasks and governed records aligned to current phase/family context while deferring current-phase-vs-subphase-vs-new-major selection to `phase-implementation.md`.
```

### PLS-004 — Execution-continuity lineage boundary

- **Target artifacts:** `../execution-continuity-and-mode-selection.md`, `../design/execution-continuity-and-mode-selection.design.md`, `../changelog/execution-continuity-and-mode-selection.changelog.md`
- **Change type:** companion sync

**Before**
```text
Execution continuity keeps next work moving and routes broad slices through worker routing, but phase-shaped continuation could still be overread as momentum to open a fresh major phase.
```

**After**
```text
`execution-continuity-and-mode-selection` v1.10 adds a phase-lineage continuity boundary: phase-shaped follow-up work applies `phase-implementation.md` lineage handling before any new major phase is opened.
```

### PLS-005 — Master governed record sync

- **Target artifacts:** `../design/design.md`, `../changelog/changelog.md`, `../README.md`, `../TODO.md`, `../phase/SUMMARY.md`
- **Change type:** governed sync

**Before**
```text
Master records describe v9.82/P083 as the current release and do not yet record P076-02/v9.83 phase-lineage refinement.
```

**After**
```text
Master records describe v9.83 with the active runtime count still 43, because P076-02 refines existing phase/startup/task/documentation/execution-continuity owners rather than adding a new runtime rule.
```

### PLS-006 — P076-02 phase record and release boundary

- **Target artifact:** `../phase/phase-076-02-major-vs-subphase-lineage-selection.md`
- **Change type:** additive phase record

**Before**
```text
No P076-02 child phase record exists for major-vs-subphase lineage selection.
```

**After**
```text
A P076-02 phase record tracks owner-chain refinement, master governed sync, runtime install/parity, git push, and GitHub release `v9.83` gates.
```

---

## 4) Verification

- [x] `phase-implementation` runtime/design/changelog updated and audited at v2.26.
- [x] `artifact-initiation-control` runtime/design/changelog updated and audited at v1.7.
- [x] `project-documentation-standards` runtime/design/changelog updated and audited at v2.32.
- [x] `todo-standards` runtime/design/changelog updated and audited at v2.21.
- [x] `execution-continuity-and-mode-selection` runtime/design/changelog updated and audited at v1.10.
- [x] Master records, README, TODO, phase, and patch describe P076-02/v9.83 consistently.
- [x] README Bash and PowerShell install arrays remain exactly 43 active runtime files.
- [x] Runtime install parity is verified for the 43 active runtime rule files.
- [x] Source/runtime release artifacts are pushed and GitHub release `v9.83` is created.

---

## 5) Rollback Approach

If P076-02 proves too broad:
- narrow the lineage gate while preserving the explicit no-forced-subphase boundary
- keep `phase-implementation.md` as the phase identity owner
- keep adjacent owners deferring phase identity selection instead of allocating phase identity themselves
- preserve valid new-major phase creation for genuinely separate rollout families
- revert master v9.83 records only through a governed rollback
- keep active runtime count at 43 unless a separate governed wave changes the runtime install set
