# Design-to-Phase Execution Synthesis Patch

## 0) Document Control

> **Current Version:** 1.0
> **Status:** Completed
> **Target Design:** [../design/design.md](../design/design.md) v9.75
> **Session:** d42465eb-30a7-4bc8-b9d6-03e52306e9a5
> **Full history:** [../changelog/changelog.md](../changelog/changelog.md)

---

## 1) Context

P076 responds to a workflow gap: when governed design is already clear enough for staged execution, the assistant can still wait for a separate user command to turn that design into phase files and live tasks.

พูดง่าย ๆ: ถ้า design พร้อมแล้ว AI ควรถอด design ออกมาเป็น phase plan และเริ่มเดินงานตาม phase ได้เลย ไม่ต้องรอให้ผู้ใช้สั่งแยกทุกขั้น.

This patch keeps the change narrow:
- `phase-implementation.md` owns the design-to-phase execution synthesis behavior.
- `artifact-initiation-control.md` gets only a startup bridge sentence so clear staged design resolves phase posture early.
- TODO/task/execution/communication rules are not rewritten because their existing ownership is already sufficient.

---

## 2) Analysis

Risk level: Medium

Dependencies:
- `document-design-control.md` already owns design as active target-state truth.
- `phase-implementation.md` already owns `/phase`, source-input synthesis, child phase structure, and live phase/task linkage.
- `artifact-initiation-control.md` already owns startup artifact posture.
- `todo-standards.md` already owns live task-list behavior.
- `execution-continuity-and-mode-selection.md` already owns continue-vs-stop behavior.

Review concerns:
- Do not make every design doc force phase planning.
- Do not let phase replace design as target-state truth.
- Do not duplicate TODO/live task mechanics or execution-continuity stop gates.
- Do not weaken startup ambiguity handling; ask when design or rollout choice is genuinely unresolved.

---

## 3) Change Items

### DTPES-001 — `phase-implementation.md` design-to-phase synthesis bridge

- **Target artifact:** `../phase-implementation.md`
- **Target location:** `Phase Workspace Contract` / `Source-input synthesis`
- **Change type:** additive

**Before**
```text
`/phase` is a live execution synthesis layer, not source of truth. It may consume design target-state input and governed patch review input when relevant.
```

**After**
```text
When governed design is sufficiently clear for staged execution, `/phase` should actively derive or update the phase execution order from normalized design truth, create or update phase summary/child phase files, initialize current-phase live tasks when non-trivial work begins, and continue phase-by-phase unless a real stop gate exists.
```

**Preserved behavior**
- Phase remains a live execution synthesis layer, not design authority.
- Staged execution remains required; trivial work does not force phase overhead.
- Real ambiguity, missing access, destructive/high-impact action, or materially different rollout choices still stop for clarification/confirmation.

### DTPES-002 — `phase-implementation.design.md` target-state sync

- **Target artifact:** `../design/phase-implementation.design.md`
- **Target locations:** goal, scope/startup bridge, summary/child model, verification checklist
- **Change type:** additive

**After**
```text
The design records that sufficiently clear governed design can drive phase creation/update and phase-by-phase execution synthesis while preserving design as target-state truth.
```

### DTPES-003 — `phase-implementation.changelog.md` version sync

- **Target artifact:** `../changelog/phase-implementation.changelog.md`
- **Change type:** additive version entry

**After**
```text
Record v2.24 for design-to-phase execution synthesis.
```

### DTPES-004 — `artifact-initiation-control.md` startup bridge

- **Target artifact:** `../artifact-initiation-control.md`
- **Target locations:** resolve-set guidance, trigger matrix, artifact resolution contract
- **Change type:** additive narrow bridge

**After**
```text
If governed design is already sufficiently clear and staged execution is warranted, phase posture should resolve to `use existing` or `create now` rather than lingering as implicit planning.
```

**Preserved behavior**
- Ambiguous phase need still asks now.
- Trivial isolated work still bypasses heavy artifact setup.
- `not required` still does not imply deletion/disposal authority.

### DTPES-005 — `artifact-initiation-control.design.md` and changelog sync

- **Target artifacts:** `../design/artifact-initiation-control.design.md`, `../changelog/artifact-initiation-control.changelog.md`
- **Change type:** companion sync only

**After**
```text
Record the same clear-design-to-phase-posture bridge at startup without taking over phase semantics.
```

### DTPES-006 — Master records and runtime install sync

- **Target artifacts:** `../design/design.md`, `../changelog/changelog.md`, `../README.md`, `../TODO.md`, `../phase/SUMMARY.md`, `../phase/phase-076-01-design-to-phase-execution-synthesis.md`, this patch file
- **Change type:** companion sync only

**After**
```text
Master records show P076 as a narrow design-to-phase execution synthesis refinement and runtime install/parity remains limited to the 41 README-listed active runtime rules.
```

---

## 4) Verification

- [x] Runtime rule changes are limited to `phase-implementation.md` and `artifact-initiation-control.md`.
- [x] Design-to-phase synthesis is conditional on sufficiently clear governed design and staged execution being warranted.
- [x] Phase remains execution synthesis only and does not replace design as target-state truth.
- [x] Existing TODO/live task-list and execution-continuity owners are not duplicated.
- [x] Ambiguity, missing access, destructive/high-impact action, and materially different rollout choices remain real stop gates.
- [x] README active runtime install list remains 41 files.
- [x] Runtime install copies only the 41 active runtime rule files.
- [x] Source/runtime parity passes for the active runtime install set.
- [x] No plugin/project-owned runtime destination files are touched.

---

## 5) Rollback Approach

If P076 proves too broad:
- remove or narrow only the design-to-phase synthesis bridge in `phase-implementation.md`
- remove the companion startup bridge sentence from `artifact-initiation-control.md` if it causes phase posture overreach
- preserve existing phase/source-input synthesis, startup artifact posture, live task-list, and execution-continuity behavior
- do not change the 41-file active runtime install boundary or delete/manage destination files outside the current source-owned install set
