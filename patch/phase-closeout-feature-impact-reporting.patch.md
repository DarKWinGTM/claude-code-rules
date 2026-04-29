# Phase Closeout Feature Impact Reporting Patch

## 0) Document Control

> **Current Version:** 1.0
> **Status:** Completed
> **Target Design:** [../design/design.md](../design/design.md) v9.74
> **Session:** d42465eb-30a7-4bc8-b9d6-03e52306e9a5
> **Full history:** [../changelog/changelog.md](../changelog/changelog.md)

---

## 1) Context

P075 responds to a closeout-quality gap: phase completion reports can become too audit-like when they list checked files and task IDs but do not explain what the phase actually developed, improved, enabled, or changed for the user/system.

พูดง่าย ๆ: ปิด phase แล้วต้องบอกด้วยว่า phase นี้ส่งมอบอะไร เพิ่ม/ปรับปรุงอะไร และผลกระทบคืออะไร ไม่ใช่รายงานแค่ audit scope.

This patch separates the two work types:

### Runtime active rule changes

These are behavior/semantic rule changes:
- `response-closing-and-action-framing.md`
- `phase-implementation.md`
- `answer-presentation.md`
- `accurate-communication.md`
- `explanation-quality.md`

### Development docs / governed record sync only

These are companion record updates only, not runtime-rule improvement targets:
- paired `design/*.design.md`
- paired `changelog/*.changelog.md`
- `design/design.md`
- `changelog/changelog.md`
- `README.md`
- `TODO.md`
- `phase/SUMMARY.md`
- `phase/phase-075-01-phase-closeout-feature-impact-reporting.md`
- this patch file

---

## 2) Analysis

Risk level: Medium

Dependencies:
- P031 already added easy-to-picture phase/progress explanation guidance.
- P062 split closing/action framing out of `accurate-communication.md` into `response-closing-and-action-framing.md`.
- P073/P074 preserved the 41-file active runtime install boundary.

Review concerns:
- Do not make every simple completion response long or templated.
- Do not weaken verification-honest wording; feature/impact claims still need checked basis or bounded inference wording.
- Do not turn README/TODO/phase/patch/design/changelog sync into runtime-rule targets.
- Do not change the 41-file active runtime install list.

---

## 3) Change Items

### PCFI-001 — `response-closing-and-action-framing.md` phase-backed closeout owner

- **Target artifact:** `../response-closing-and-action-framing.md`
- **Target locations:** `## Rule Statement`, `## Core Principles`, `## Preferred Shapes`, anti-patterns, quality metrics
- **Change type:** additive

**Before**
```text
The chain owns concise synthesis, next-action framing, recommendation-with-reason wording, alternative preservation, closed-topic summary handling, and advisory proposal framing.
```

**After**
```text
The chain also owns phase-backed closeout synthesis: when closing phase-backed work, report what the phase delivered, the feature/improvement changed, user/system impact, verification basis, and next phase state when relevant before or alongside audit scope.
```

**Preserved behavior**
- Endings stay concise and high-signal.
- Future-work proposals remain advisory unless selected.
- Execution-mode decisions still defer to `execution-continuity-and-mode-selection.md`.

### PCFI-002 — `phase-implementation.md` closeout/reporting contract

- **Target artifact:** `../phase-implementation.md`
- **Target locations:** purpose/authority boundary, child phase field contract, verification/rollback contract, verification checklist
- **Change type:** additive + metadata alignment

**Before**
```text
Phase files define objective, action checklist, affected artifacts, TODO/changelog coordination, verification, exit criteria, rollback notes, and next possible phases.
```

**After**
```text
Phase closeout should also state what the phase delivered, which feature/improvement changed, what user/system impact it has, what verification supports it, and whether a next phase is not started, draft, selected, or active.
```

**Preserved behavior**
- `/phase` remains a live execution synthesis layer, not design authority.
- Patch linkage and current-phase-first task behavior remain intact.
- Shared-board/plugin coordination mechanics remain outside Main RULES doctrine.

### PCFI-003 — `answer-presentation.md` compact phase closeout pattern

- **Target artifact:** `../answer-presentation.md`
- **Target locations:** specialized compact patterns, trigger model, preferred output shapes, anti-patterns
- **Change type:** additive

**Before**
```text
Phase/progress explanations use a short plain-language opening plus concise grouping.
```

**After**
```text
Phase-backed closeout uses a compact pattern such as: `What this phase delivered`, `Feature / Improvement`, `Impact`, `Verification`, and `Next phase state` when those fields improve clarity.
```

**Preserved behavior**
- Simple answers stay compact.
- Sectioning is used only when it improves comprehension.
- Tables remain light and optional.

### PCFI-004 — `accurate-communication.md` feature/impact wording honesty

- **Target artifact:** `../accurate-communication.md`
- **Target locations:** core principles, phase/progress framing, decision checklist, anti-patterns, quality metrics
- **Change type:** additive

**Before**
```text
Phase/progress reporting should start with a short plain-language line that helps the reader picture what the phase is doing.
```

**After**
```text
Phase closeout reporting should explain what changed and what impact it has before or alongside checked-scope/audit detail, while keeping delivery, testing, and fixed/stable claims aligned to the verification actually performed.
```

**Preserved behavior**
- Claim-state wording stays evidence-aligned.
- Scoped non-findings remain scoped.
- Technical snapshot wording still defers to `technical-snapshot-communication.md`.

### PCFI-005 — `explanation-quality.md` phase-closeout explanation flow

- **Target artifact:** `../explanation-quality.md`
- **Target locations:** core requirements, phase/progress explanation guidance, trigger model, preferred examples, anti-patterns
- **Change type:** additive

**Before**
```text
Phase/progress explanations start with an easy-to-picture line and keep governance detail after the orientation.
```

**After**
```text
Phase closeout explanations should make the delivered feature/improvement and its practical user/system meaning visible before deeper governance detail, file lists, or task IDs.
```

**Preserved behavior**
- Explanations remain concise and practical.
- Dense technical detail can still appear after the user-facing meaning is clear.
- Safe continuation still proceeds when no real stop gate exists.

### PCFI-006 — Paired design/changelog sync

- **Target artifacts:** paired design/changelog files for the five touched runtime owners
- **Change type:** companion sync only

**Before**
```text
Companion records do not yet describe phase-backed feature/impact closeout reporting.
```

**After**
```text
Companion records describe the same target state and version history for phase-backed closeout reporting.
```

### PCFI-007 — Master records, phase summary, README, TODO, and runtime install sync

- **Target artifacts:** `../design/design.md`, `../changelog/changelog.md`, `../README.md`, `../TODO.md`, `../phase/SUMMARY.md`, `../phase/phase-075-01-phase-closeout-feature-impact-reporting.md`, this patch file
- **Change type:** companion sync only

**Before**
```text
Master records are synchronized through P074-02 and do not yet record P075 phase closeout reporting behavior.
```

**After**
```text
Master records record P075 as a narrow runtime closeout-reporting improvement, preserve the 41-file active runtime install scope, and verify source/runtime parity after installing only active runtime rules.
```

---

## 4) Verification

- [x] Runtime rule changes are limited to the five listed active runtime owners.
- [x] Development docs/governed record changes are clearly companion sync only.
- [x] Phase closeout behavior requires feature/improvement/impact/verification/next-phase-state visibility without forcing long templates for trivial work.
- [x] README active runtime install list remains 41 files.
- [x] Runtime install copies only the 41 active runtime rule files.
- [x] Source/runtime parity passes for the active runtime install set.
- [x] No plugin/project-owned runtime destination files are touched.

---

## 5) Rollback Approach

If P075 proves too broad:
- revert only the five closeout-reporting runtime owner changes and their companion record entries
- preserve the existing P031 phase/progress explanation guidance unless separately challenged
- preserve P073/P074 active runtime install and shared runtime destination boundaries
- do not delete or manage destination/runtime files outside the current source-owned install set as part of rollback
