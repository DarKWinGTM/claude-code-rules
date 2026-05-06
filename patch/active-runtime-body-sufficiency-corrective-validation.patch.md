# Active Runtime Body Sufficiency Corrective Validation Patch

## 0) Document Control

> **Current Version:** 1.0
> **Status:** Completed
> **Target Design:** [../design/design.md](../design/design.md) v9.88, [../design/unified-version-control-system.design.md](../design/unified-version-control-system.design.md) v1.3
> **Session:** d42465eb-30a7-4bc8-b9d6-03e52306e9a5
> **Full history:** [../changelog/changelog.md](../changelog/changelog.md)

---

## 1) Context

P073-10 repairs a runtime materialization drift: 10 active root runtime files are listed in the README active install arrays and master active runtime inventory, but each contains only metadata/header content. Runtime install parity therefore succeeded while installed active behavior was missing.

พูดง่าย ๆ: source กับ runtime เหมือนกันจริง แต่ทั้งคู่เป็น stub ที่ไม่มี body จึงต้องเพิ่ม validation ว่า active runtime file ต้องมี contract จริงด้วย.

---

## 2) Analysis

Risk level: High for governance integrity, Medium for text-only implementation.

Dependencies:
- `unified-version-control-system.md` owns controller-level version/rule-chain sufficiency semantics.
- `project-documentation-standards.md` owns runtime install scope and governed artifact role boundaries.
- `document-consistency.md` owns cross-file sync and parity/no-drift claim checks.
- `document-design-control.md` keeps design target-state authority separate from runtime body authority.
- `document-changelog-control.md` keeps version/history authority.
- `phase-implementation.md`, `document-patch-control.md`, and `todo-standards.md` own governed execution records.

Review concerns:
- Do not remove active runtime files that master records still classify as active unless stronger checked authority proves removal.
- Do not restore stale v1.1 bodies blindly.
- Do not let design files replace root runtime behavior.
- Do not increase active runtime count.
- Do not delete observed-only destination runtime extras.
- Do not claim runtime parity is sufficient unless body sufficiency also passes.

---

## 3) Change Items

### P07310-001 — Materialize metadata-only active runtime bodies

- **Target artifacts:** `../anti-mockup.md`, `../dan-safe-normalization.md`, `../emergency-protocol.md`, `../flow-diagram-no-frame.md`, `../recovery-contract.md`, `../refusal-classification.md`, `../refusal-minimization.md`, `../safe-file-reading.md`, `../safe-terminal-output.md`, `../unified-version-control-system.md`
- **Change type:** replacement / corrective materialization

**Before**
```text
Each target root runtime file contains only title/version/design/session metadata, lacks Full history, and has no substantive runtime behavior contract despite being README-listed active runtime content.
```

**After**
```text
Each target root runtime file contains canonical metadata including Full history plus a concise substantive runtime body with rule statement, operational contract, boundaries/triggers where relevant, verification expectations, and integration links.
```

### P07310-002 — Sync repaired rule design/changelog companions

- **Target artifacts:** `../design/<rule>.design.md`, `../changelog/<rule>.changelog.md` for the 10 repaired rule chains
- **Change type:** companion sync

**Before**
```text
Design and changelog files describe active target-state or prior runtime updates, but the root runtime files do not materialize those contracts.
```

**After**
```text
Each companion design/changelog chain is version-aligned with the restored runtime body and records the metadata-only stub repair without turning design into runtime authority.
```

### P07310-003 — Add active runtime body-sufficiency validation doctrine

- **Target artifacts:** `../unified-version-control-system.md`, `../design/unified-version-control-system.design.md`, `../changelog/unified-version-control-system.changelog.md`, `../project-documentation-standards.md`, `../design/project-documentation-standards.design.md`, `../changelog/project-documentation-standards.changelog.md`, `../document-consistency.md`, `../design/document-consistency.design.md`, `../changelog/document-consistency.changelog.md`
- **Change type:** additive refinement

**Before**
```text
Runtime install/parity doctrine distinguishes active root runtime files from design/changelog/TODO/phase/patch surfaces, but does not explicitly reject metadata-only active root files or require substantive runtime bodies before parity/no-drift claims.
```

**After**
```text
Runtime sufficiency doctrine states that README-listed active runtime files require canonical metadata, Full history, and substantive runtime behavior bodies; design-only or metadata-only roots cannot satisfy active runtime install/parity claims.
```

### P07310-004 — Master records and release sync

- **Target artifacts:** `../design/design.md`, `../changelog/changelog.md`, `../README.md`, `../TODO.md`, `../phase/SUMMARY.md`, `../phase/phase-073-10-active-runtime-body-sufficiency-corrective-validation.md`
- **Change type:** governed sync

**Before**
```text
Master records describe v9.87 with 44 active runtime rules and runtime parity, but body-sufficiency is not part of the verified release gate.
```

**After**
```text
Master records describe v9.88 with unchanged 44 active runtime rules, record P073-10 as the active runtime body-sufficiency repair, add metadata-only stub prevention to release verification, and close only after source/runtime parity and body-sufficiency checks pass.
```

### P07310-005 — Runtime install and validation

- **Target artifacts:** `/home/node/.claude/rules/` destination active runtime copies
- **Change type:** controlled install / verification

**Before**
```text
Destination active runtime copies match the source stubs for the 10 affected files, so parity passes while runtime behavior is missing.
```

**After**
```text
Only README-listed active runtime files are installed; source/runtime parity passes for 44/44 files; no README-listed active runtime file is metadata-only; destination extras remain observed-only and untouched.
```

---

## 4) Verification

- [x] The 10 affected active runtime files have canonical metadata including `Full history`.
- [x] The 10 affected active runtime files have substantive runtime bodies.
- [x] Repaired rule/design/changelog versions align.
- [x] Body-sufficiency validation doctrine is added to controller/governance owners.
- [x] Master records describe v9.88 and unchanged active runtime count 44 consistently.
- [x] README Bash and PowerShell install arrays include exactly 44 active runtime files.
- [x] Source body-sufficiency audit passes for all 44 active runtime files.
- [x] Runtime install parity is verified 44/44.
- [x] Runtime body-sufficiency audit passes after install.
- [x] Source/runtime release artifacts are pushed and GitHub release `v9.88` is created.

---

## 5) Closeout Summary

This patch completed the active runtime body-sufficiency repair for the unchanged 44-file active runtime install set. The corrected source roots now carry substantive runtime bodies, the restored chains are version-aligned, and runtime install/parity plus body-sufficiency verification passed for all README-listed active runtime files.

Destination markdown files outside the source-owned active runtime set remain observed-only and untouched.

---

## 6) Rollback Approach

If the corrective materialization is wrong:
- revert the v9.88 commit
- reinstall the prior v9.87 44-rule runtime set only under explicit rollback gate
- keep destination extras observed-only and do not delete them
- preserve source/runtime body-sufficiency validation if the rollback only affects a specific restored body and the validation doctrine remains correct
- delete or correct GitHub release/tag only with explicit user approval
