# Maintainable Helper and Comment Discipline Refinement Patch

## 0) Document Control

> **Current Version:** 1.0
> **Status:** Completed
> **Target Design:** [../design/design.md](../design/design.md) v9.82
> **Session:** d42465eb-30a7-4bc8-b9d6-03e52306e9a5
> **Full history:** [../changelog/changelog.md](../changelog/changelog.md)

---

## 1) Context

P083 refines the existing `maintainable-code-structure-and-decomposition.md` owner after the user identified a nuance in the P082 maintainability rule: avoiding God functions and God files must not drift into helper-function inflation, and source code should carry useful comments when purpose, process, constraints, side effects, or business rules are otherwise hard to understand.

พูดง่าย ๆ: rule เดิมบอกให้แยก responsibility ให้ดี; P083 เพิ่มว่าอย่าแตก helper จนเกินจำเป็น และ comment ต้องช่วยให้เข้าใจ code จริง ไม่ใช่ comment ทุกบรรทัดหรือ comment ซ้ำ syntax.

This is a refinement patch, not a new active runtime rule. The active runtime install count remains 43.

---

## 2) Analysis

Risk level: Medium

Dependencies:
- `maintainable-code-structure-and-decomposition.md` owns coding-time responsibility, decomposition, helper necessity, source-code comment discipline, and anti-overengineering posture.
- `tactical-strategic-programming.md` remains convergence owner and should not absorb helper/comment rules.
- `explanation-quality.md` and `accurate-communication.md` govern assistant response explanations and evidence wording, not source-code comment policy.
- `project-documentation-standards.md` owns durable governed docs; inline comments must not replace governed design/spec authority.

Review concerns:
- Do not weaken God-function/God-file avoidance while discouraging trivial helpers.
- Do not create a comment-every-line doctrine.
- Do not make comments a replacement for clear names, clear structure, or governed docs.
- Do not invent explanatory source comments for unverified behavior.
- Do not add a new active runtime rule or increase the active runtime count.

---

## 3) Change Items

### MHC-001 — Runtime owner refinement

- **Target artifact:** `../maintainable-code-structure-and-decomposition.md`
- **Change type:** replacement / additive refinement

**Before**
```text
The maintainable code structure owner covers responsibility boundaries, code-smell-triggered decomposition, smallest useful decomposition, wrong abstraction avoidance, explicit dependency/state boundaries, behavior-preserving refactor, and tactical structure-debt convergence, but does not explicitly guard against helper-function inflation or define source-code comment discipline.
```

**After**
```text
The owner is updated to v1.1 with helper-function necessity guidance, explicit guardrails against helpers for obvious expressions/trivial assignments/pass-through wrappers, helper decision gates, source-code comment decision gates, comment spam/stale comment smell triggers, and integration boundaries separating source-code comments from assistant explanations and durable governed docs.
```

### MHC-002 — Design and chain changelog sync

- **Target artifacts:** `../design/maintainable-code-structure-and-decomposition.design.md`, `../changelog/maintainable-code-structure-and-decomposition.changelog.md`
- **Change type:** companion sync

**Before**
```text
The chain design and changelog describe v1.0 as the P082 owner creation state.
```

**After**
```text
The chain design and changelog describe v1.1 as the helper-function necessity and source-code comment discipline refinement while preserving P082's principle-based maintainability owner model.
```

### MHC-003 — Master governed record sync

- **Target artifacts:** `../design/design.md`, `../changelog/changelog.md`, `../README.md`, `../TODO.md`, `../phase/SUMMARY.md`
- **Change type:** governed sync

**Before**
```text
Master records describe v9.81 with 43 active runtime rules and P082 as the latest maintainable code structure owner addition.
```

**After**
```text
Master records describe v9.82 with the active runtime count still 43, because P083 refines `maintainable-code-structure-and-decomposition.md` to v1.1 rather than adding a new runtime rule.
```

### MHC-004 — P083 phase record and release boundary

- **Target artifact:** `../phase/phase-083-01-maintainable-helper-comment-discipline-refinement.md`
- **Change type:** additive phase record

**Before**
```text
No P083 phase record exists for the helper/comment refinement.
```

**After**
```text
A P083 phase record tracks triad refinement, master governed sync, runtime install/parity, git push, and GitHub release `v9.82` gates.
```

---

## 4) Verification

- [x] Maintainable code structure runtime/design/changelog triad updated and audited at v1.1.
- [x] Master records, README, TODO, phase, and patch describe P083/v9.82 consistently.
- [x] README Bash and PowerShell install arrays remain exactly 43 active runtime files.
- [x] Golden semantic anchors pass for God-function/file protection, no helper for trivial expression, helper extraction when concept/process/test/boundary value exists, comment usefulness, no comment spam, stale-comment cleanup, and source-code comment versus governed-doc boundary.
- [x] Runtime install parity is verified for the 43 active runtime rule files.
- [x] Source/runtime release artifacts are pushed and GitHub release `v9.82` is created.

---

## 5) Rollback Approach

If P083 proves too broad:
- narrow helper-function guidance while preserving the principle that helpers must earn their indirection cost
- narrow comment guidance to purpose/process/constraint/side-effect/business-rule cases only
- preserve the no-comment-spam and stale-comment cleanup boundaries
- preserve P082 maintainability, God function/file, wrong-abstraction, and behavior-preserving refactor guidance
- revert master v9.82 records only through a governed rollback
- keep active runtime count at 43 unless a separate governed wave changes the runtime install set
