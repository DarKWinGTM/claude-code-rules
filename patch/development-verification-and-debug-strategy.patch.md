# Development Verification and Debug Strategy Patch

## 0) Document Control

> **Current Version:** 1.0
> **Status:** In Progress
> **Target Design:** [../design/design.md](../design/design.md) v9.86
> **Session:** d42465eb-30a7-4bc8-b9d6-03e52306e9a5
> **Full history:** [../changelog/changelog.md](../changelog/changelog.md)

---

## 1) Context

P084-01 adds a first-class RULES owner for coding-time verification strategy. The user wants debug/testing/TestKit behavior to become a flexible, strategic working principle rather than a rigid requirement to create TestingKit artifacts for every coding task.

พูดง่าย ๆ: เป้าหมายคือให้ AI ทำ coding แบบมี proof plan เสมอสำหรับงานที่มี behavior จริง แต่ไม่ทำให้ทุกงานเล็กกลายเป็นพิธีกรรม test หนักเกินไป.

This patch creates a new active runtime rule and integrates adjacent coding, phase, task, documentation, communication, and execution-continuity owners. Active runtime count changes from 43 to 44.

---

## 2) Analysis

Risk level: Medium.

Dependencies:
- `maintainable-code-structure-and-decomposition.md` owns code structure and behavior-preserving refactor posture.
- `accurate-communication.md` owns evidence-strength wording for edited/tested/fixed/stable claims.
- `phase-implementation.md` owns phase-backed closeout and phase execution surfaces.
- `todo-standards.md` owns live task-list visibility.
- `project-documentation-standards.md` owns repository documentation role boundaries.
- `execution-continuity-and-mode-selection.md` owns continuing from implementation into verification when safe.
- `native-worker-agent-routing-and-context-control.md` already owns worker routing for broad/noisy test/log output.

Review concerns:
- Do not make TestKit mandatory for every task.
- Do not over-force live/provider/runtime checks.
- Do not let fake/local tests imply live proof.
- Do not make verification strategy replace project-specific test architecture.
- Keep trivial no-behavior work lightweight.

---

## 3) Change Items

### DVDS-001 — New verification strategy owner

- **Target artifacts:** `../development-verification-and-debug-strategy.md`, `../design/development-verification-and-debug-strategy.design.md`, `../changelog/development-verification-and-debug-strategy.changelog.md`
- **Change type:** additive

**Before**
```text
No first-class RULES owner defines coding-time debug/testing/TestKit verification strategy as a proportionate default for non-trivial coding work.
```

**After**
```text
`development-verification-and-debug-strategy` v1.0 owns coding-time verification strategy, debug path selection, testing depth, TestKit/scenario decisions, and evidence-calibrated coding closeout.
```

### DVDS-002 — Coding/refactor owner integration

- **Target artifacts:** `../maintainable-code-structure-and-decomposition.md`, `../design/maintainable-code-structure-and-decomposition.design.md`, `../changelog/maintainable-code-structure-and-decomposition.changelog.md`
- **Change type:** companion sync

**Before**
```text
Maintainable-code requires behavior preservation and relevant checks, but verification strategy is not delegated to a dedicated owner.
```

**After**
```text
Maintainable-code v1.2 defers debug/testing/TestKit verification strategy to the new owner while preserving its structure/refactor responsibilities.
```

### DVDS-003 — Evidence wording integration

- **Target artifacts:** `../accurate-communication.md`, `../design/accurate-communication.design.md`, `../changelog/accurate-communication.changelog.md`
- **Change type:** companion sync

**Before**
```text
Accurate communication separates edited/tested/fixed states generally, but coding verification strategy and TestKit evidence boundaries are not explicitly tied to a dedicated owner.
```

**After**
```text
Accurate-communication v2.21 integrates coding closeout wording so edited, tested, fake/local verified, live verified, fixed, and stable claims align with the new verification strategy owner.
```

### DVDS-004 — Phase/TODO/documentation/continuity sync

- **Target artifacts:** `../phase-implementation.md`, `../todo-standards.md`, `../project-documentation-standards.md`, `../execution-continuity-and-mode-selection.md`, and companion design/changelog files
- **Change type:** companion sync

**Before**
```text
Phase and task owners can track implementation work, but they do not consistently require visible development verification/TestKit coverage for non-trivial coding phases. Execution continuity can continue work, but does not explicitly continue from implementation into verification.
```

**After**
```text
Phase/task/documentation/continuity owners preserve Development Verification / TestKit Coverage for non-trivial coding work, keep verification slices visible when material, and continue into verification when implementation is done but evidence is still pending.
```

### DVDS-005 — Master records and runtime install

- **Target artifacts:** `../design/design.md`, `../changelog/changelog.md`, `../README.md`, `../TODO.md`, `../phase/SUMMARY.md`
- **Change type:** governed sync

**Before**
```text
Master records describe v9.85 with 43 active runtime rules and no development verification strategy owner.
```

**After**
```text
Master records describe v9.86 with 44 active runtime rules, add the new owner to install arrays and active inventory, and record source/runtime parity after install.
```

---

## 4) Verification

- [x] New rule/design/changelog triad exists and is version-aligned at v1.0.
- [x] Adjacent owner integrations are version-aligned.
- [x] Master records describe v9.86 and active runtime count 44 consistently.
- [x] README Bash and PowerShell install arrays include exactly 44 active runtime files.
- [x] Runtime install parity is verified for the 44 active runtime rule files.
- [ ] Source/runtime release artifacts are pushed and GitHub release `v9.86` is created.

---

## 5) Rollback Approach

If the new verification strategy proves too heavy:
- narrow trigger wording to only higher-risk coding/debug/integration work before removing the owner entirely
- preserve evidence-boundary wording that prevents edit-only fixed claims and fake/local overclaim
- keep TestKit as an option rather than a universal requirement
- remove the new runtime rule from README install arrays and master inventory only through a governed rollback
- reinstall the previous 43-rule runtime set only under a separate explicit rollback gate
