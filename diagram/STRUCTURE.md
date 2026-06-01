# RULES Diagram Structure

> **Status:** Active bootstrap structure surface / In Progress
> **Current Doctrine Basis:** [../docs/superpowers/specs/2026-06-01-rules-diagram-companion-pattern-design.md](../docs/superpowers/specs/2026-06-01-rules-diagram-companion-pattern-design.md)
> **Design Alignment:** [../design/document-governance.design.md](../design/document-governance.design.md)
> **Session:** 1f1873d2-0feb-485f-a5ff-d383254590dd

---

## Purpose

This file is the top-level visual entrypoint for RULES.

พูดง่าย ๆ: `design/` ยังเป็น textual truth, แต่ `diagram/STRUCTURE.md` คือภาพรวมที่ช่วยให้เห็นความสัมพันธ์ของระบบทั้งก้อนในมุม visual-first โดยไม่ต้องแตกตาม text shard อัตโนมัติ.

---

## Whole-repo relationship map

```text
RULES/
  README.md
    → current front page / onboarding / current-state overview

  root runtime rules (*.md)
    → active runtime behavior contract

  design/
    → textual target-state truth

  diagram/
    → visual synthesis lane
    → STRUCTURE.md = whole-repo visual anchor
    → <subject>.design.md = integrated subject diagrams when needed

  changelog/
    → version/history authority

  TODO.md
    → compact durable execution index

  phase/
    → live staged execution

  patch/
    → before/after review artifacts

  plugin/
    → optional support/implementation surfaces only

  docs/superpowers/
    → supporting spec/plan artifacts for design and implementation waves
```

---

## Authority boundaries

- `design/` owns semantic truth and target-state meaning.
- `diagram/` owns visual synthesis and relationship explanation.
- If text and diagram differ, `design/` wins semantically.
- `changelog/`, `TODO.md`, `phase/`, and `patch/` may track diagram work, but they do not own diagram meaning.
- governed-docs preview/manifest/report output stays support-only and must not become source truth.

---

## Current bootstrap posture

This correction wave opens the diagram lane with the global anchor first.

Current checked posture:
- `diagram/STRUCTURE.md` is now the required whole-repo visual anchor.
- No subject-level RULES diagram chain is selected as the default next diagram body yet.
- Future subject diagrams should start as one integrated document per subject and split only after a real visual-complexity trigger appears.

---

## Subject-diagram rule

When a RULES subject needs governed visual explanation:
- start with `diagram/<subject>.design.md`
- keep it bodyful and integrated by default
- split into `diagram/<subject>/<NN>-<slice>.design.md` only when the diagram itself becomes too broad or separates into genuinely different visual questions

What is **not** enough reason to split:
- matching design shards for symmetry alone
- making plugin implementation easier
- forcing one diagram file per text heading

---

## Current follow-up direction

The current sync wave still needs to:
- align active owner docs so `diagram/` is recognized as a first-class governed visual lane
- keep inline answer/phase-local text-diagram guidance separate from repository diagram-lane doctrine
- preserve plugin behavior as downstream support only before any later implementation returns
