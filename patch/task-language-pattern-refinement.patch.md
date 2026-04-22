# Task Language Pattern Refinement Patch

## 0) Document Control

> **Current Version:** 1.0
> **Status:** Completed
> **Target Design:** [../design/todo-standards.design.md](../design/todo-standards.design.md) v2.19
> **Session:** a9bec472-1706-4019-8cfd-5ba988a71662
> **Full history:** [../changelog/changelog.md](../changelog/changelog.md)

---

## 1) Context

This patch captures the bounded refinement wave that makes Task List wording follow the actual active session language pattern more explicitly.

Why this matters:
- current wording already says task language should align naturally with the active session language/register
- but that wording is still loose enough that the runtime can drift back into detached generic wording
- the user wants task wording to follow the language that is actually being used in the session, without forcing Thai-only output or any fixed Thai/English ratio
- technical labels should remain in technical form when translating them would make the wording less natural

---

## 2) Analysis

Risk level: Medium

Dependencies:
- `../todo-standards.md`
- `../phase-implementation.md`
- `../design/design.md`
- `../README.md`
- `../TODO.md`
- `../phase/SUMMARY.md`
- `../changelog/changelog.md`

Review concern:
- make the language rule more explicit without turning it into a rigid monolingual policy
- preserve flexibility for naturally mixed Thai+English task wording and preserve technical labels when forced translation would reduce clarity

---

## 3) Change Items

### Change Item 1
- **Target location:** `todo-standards`
- **Change type:** additive

**Before**
```text
Task wording should align naturally with the active session language/register, but the wording was still loose enough that runtime behavior could fall back into generic detached phrasing.
```

**After**
```text
Task wording should follow the actual active session language pattern, use Thai-led wording by default when the session is primarily Thai, preserve naturally mixed Thai+English wording when that is how the session is actually being used, and keep technical labels in technical form when forced translation would reduce clarity.
```

### Change Item 2
- **Target location:** `phase-implementation`
- **Change type:** additive

**Before**
```text
Phase-linked task wording should align naturally with the active session language/register, but the rule did not yet spell out how Thai-led or naturally mixed wording should be handled in practice.
```

**After**
```text
Phase-linked task wording should follow the actual active session language pattern, keep Thai-led wording by default when the session is primarily Thai, preserve naturally mixed Thai+English wording when that is the real session pattern, and avoid forced translation of technical labels when that would read less naturally.
```

### Change Item 3
- **Target location:** master/history surfaces
- **Change type:** additive

**Before**
```text
Master/design/history surfaces did not yet record this bounded task-language-pattern refinement wave.
```

**After**
```text
Master/history surfaces now record the task-language-pattern refinement coherently and make it visible that task wording should follow actual session usage rather than a forced monolingual or fixed-ratio policy.
```

---

## 4) Verification

- [x] `todo-standards` now explicitly says task wording should follow the actual active session language pattern
- [x] `phase-implementation` now explicitly says phase-linked task wording should follow the actual active session language pattern
- [x] Thai-led default wording is explicit when the session is primarily Thai
- [x] naturally mixed Thai+English wording remains allowed when that matches the real session pattern
- [x] technical labels may remain untranslated when forced translation would reduce clarity
- [x] touched master/history surfaces record the wave coherently

---

## 5) Rollback Approach

If the refinement proves too broad:
- preserve the rule that task wording should still follow session language rather than detached generic wording
- narrow the new examples/default-language wording before removing it entirely
- do not roll back into a state where task wording is treated like generic system output rather than the language actually being used in the session
