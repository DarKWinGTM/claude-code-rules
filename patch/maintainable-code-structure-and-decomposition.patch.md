# Maintainable Code Structure and Decomposition Patch

## 0) Document Control

> **Current Version:** 1.0
> **Status:** In Progress
> **Target Design:** [../design/design.md](../design/design.md) v9.81
> **Session:** d42465eb-30a7-4bc8-b9d6-03e52306e9a5
> **Full history:** [../changelog/changelog.md](../changelog/changelog.md)

---

## 1) Context

P082 adds a first-class coding-structure rule after the user identified a gap: the existing tactical/strategic doctrine allows fast tactical work with convergence, but it does not directly teach AI how to structure code during implementation so it avoids unnecessary God functions, God files, hidden dependencies, and poor decomposition.

พูดง่าย ๆ: กฎใหม่นี้ไม่ได้บังคับ pattern ตายตัว แต่สอน AI ให้คิดเรื่อง responsibility, maintainability, code smell, และ smallest useful decomposition ระหว่างเขียนโค้ดจริง.

This is a source/governance/runtime-install patch. It adds one new active runtime rule, integrates the adjacent tactical/strategic boundary, updates master governance records, installs the active rule set, and prepares v9.81.

---

## 2) Analysis

Risk level: Medium

Dependencies:
- `tactical-strategic-programming.md` owns tactical entry, strategic target, convergence path, and strategic closure.
- `maintainable-code-structure-and-decomposition.md` will own coding-time responsibility boundaries, smell-triggered decomposition, and anti-overengineering posture.
- README install arrays must remain the canonical active runtime install set.
- Runtime install must copy only README-listed active runtime rule files.

Review concerns:
- Do not turn maintainability into fixed line-count policing.
- Do not force Clean Architecture, MVC, service/repository, or any project-agnostic template.
- Do not split cohesive code merely because it is long.
- Do not create speculative abstractions or DRY-by-appearance wrong abstractions.
- Do not let `tactical-strategic-programming.md` become the owner of coding-time decomposition.
- Do not claim runtime parity until the 43-rule install/audit gate passes.

---

## 3) Change Items

### MCS-001 — New maintainable code structure owner

- **Target artifact:** `../maintainable-code-structure-and-decomposition.md`
- **Target design:** `../design/maintainable-code-structure-and-decomposition.design.md`
- **Target changelog:** `../changelog/maintainable-code-structure-and-decomposition.changelog.md`
- **Change type:** additive

**Before**
```text
No first-class active runtime rule owns coding-time responsibility decomposition, God function/file avoidance, code-smell-triggered structure decisions, smallest-useful decomposition, or wrong-abstraction guardrails.
```

**After**
```text
A first-class active runtime rule owns maintainable code structure and decomposition with principle-based guidance: maintainability as future changeability, responsibility by reason to change, code smells as triggers not verdicts, smallest useful decomposition, explicit dependency/state boundaries, wrong-abstraction avoidance, behavior-preserving refactor posture, and verification-honest reporting.
```

### MCS-002 — Tactical/strategic integration boundary

- **Target artifacts:** `../tactical-strategic-programming.md`, `../design/tactical-strategic-programming.design.md`, `../changelog/tactical-strategic-programming.changelog.md`
- **Change type:** additive / boundary clarification

**Before**
```text
Tactical-strategic-programming owns tactical entry and strategic convergence, but it does not explicitly defer coding-time responsibility and decomposition quality to a dedicated owner.
```

**After**
```text
Tactical-strategic-programming points to maintainable-code-structure-and-decomposition for code responsibility quality inside tactical or strategic implementation. Tactical fixes may stay fast, but material structure debt should have a convergence path and should not silently worsen God-function or God-file drift.
```

### MCS-003 — Master record sync

- **Target artifacts:** `../design/design.md`, `../changelog/changelog.md`, `../README.md`, `../TODO.md`, `../phase/SUMMARY.md`
- **Change type:** companion sync

**Before**
```text
Master records describe v9.80 with 42 active runtime rules and P081 as the latest worker-routing refinement.
```

**After**
```text
Master records describe v9.81 with 43 active runtime rules and P082 as the maintainable code structure and decomposition owner addition, including README Bash/PowerShell install arrays and phase/TODO/changelog records.
```

### MCS-004 — P082 phase record

- **Target artifact:** `../phase/phase-082-01-maintainable-code-structure-and-decomposition.md`
- **Change type:** additive

**Before**
```text
No P082 phase record exists.
```

**After**
```text
A P082 phase record tracks the new rule triad, tactical/strategic integration, governed sync, runtime install, parity verification, push, and release gates.
```

### MCS-005 — Runtime install and release boundary

- **Target artifacts:** README-listed active runtime rule files and `/home/node/.claude/rules/` deployed copies
- **Change type:** install / verification

**Before**
```text
The active runtime install set contains 42 source-owned runtime rule files from v9.80.
```

**After**
```text
The active runtime install set contains 43 source-owned runtime rule files after adding `maintainable-code-structure-and-decomposition.md`, copying only README-listed active runtime rules, and verifying source/runtime hash parity for v9.81.
```

---

## 4) Verification

- [x] Maintainable code structure runtime/design/changelog created at v1.0.
- [x] Tactical-strategic runtime/design/changelog updated to v1.3 with clear integration boundary.
- [x] Master records, README, TODO, phase, and patch describe P082/v9.81 consistently.
- [x] README Bash and PowerShell install arrays include exactly 43 active runtime files.
- [x] Golden scenarios pass: God function/file trigger, cohesive long function no forced split, wrong-abstraction avoidance, tactical fix with convergence path, behavior-preserving refactor, and verification-honest reporting.
- [x] Runtime install parity is verified for the 43 active runtime rule files.
- [ ] Source/runtime release artifacts are pushed and GitHub release `v9.81` is created.

---

## 5) Rollback Approach

If P082 proves too broad:
- narrow the smell-trigger wording so it remains advisory and analysis-first
- keep the no-line-count / no-template-doctrine boundary
- preserve tactical-strategic integration only as a deferral to code-structure ownership
- revert the master v9.81 docs only through a separate governed rollback
- remove the new active rule from README install arrays only under an explicit rollback wave
- do not delete destination/runtime files outside the source-owned install set as part of rollback without explicit destructive authorization
