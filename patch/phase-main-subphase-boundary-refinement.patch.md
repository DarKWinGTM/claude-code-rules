# Phase Main/Subphase Boundary Refinement Patch

## 0) Document Control

> **Current Version:** 1.0
> **Status:** Completed
> **Target Design:** [../design/design.md](../design/design.md) v9.95
> **Session:** d42465eb-30a7-4bc8-b9d6-03e52306e9a5
> **Full history:** [../changelog/changelog.md](../changelog/changelog.md)

---

## 1) Context

P076-04 refines phase identity selection after the user identified that the existing lineage-first criteria can over-nest future work under one old major phase. The concrete evidence came from NodeClaw task/phase behavior, where many new or separately gated slices continued to appear as `P055-xx` subphases.

พูดง่าย ๆ: P076-02 fixed “เปิด major ใหม่ง่ายเกินไป”; P076-04 fixes the mirror problem, “ติดอยู่ใน major เดิมนานเกินไป”.

This is a refinement patch under the existing `076` phase identity family. It does not add a new active runtime rule. The active runtime install count remains 46.

---

## 2) Analysis

Risk level: Medium.

Dependencies:
- `phase-implementation.md` owns phase identity semantics and is the correct owner for bounded-phase and umbrella-escape doctrine.
- `design/phase-implementation.design.md` owns the target-state rationale for the phase identity decision model.
- `changelog/phase-implementation.changelog.md` owns the `phase-implementation` version/history record.
- Master records (`design/design.md`, `changelog/changelog.md`, `README.md`, `TODO.md`, `phase/SUMMARY.md`) must describe v9.95 consistently.

Review concerns:
- Do not replace lineage-first selection with major-first selection.
- Do not force new main phases when a subphase genuinely continues the same bounded execution gate.
- Do not treat broad same-domain evidence as sufficient for subphase selection when output/gate/release/rollback boundaries diverge.
- Do not edit NodeClaw phase files; NodeClaw is evidence for RULES behavior only.
- Do not increase the active runtime rule count.

---

## 3) Change Items

### PMSB-001 — Bounded-phase doctrine

- **Target artifacts:** `../phase-implementation.md`, `../design/phase-implementation.design.md`, `../changelog/phase-implementation.changelog.md`
- **Change type:** additive refinement / decision-model tightening

**Before**
```text
`phase-implementation.md` v2.31 requires lineage inspection before opening a new major phase and lists subphase-fit signals such as same objective, policy domain, rule owner chain, design target, patch surface, dependency, or completed parent/sibling history.
```

**After**
```text
`phase-implementation` v2.32 keeps lineage-first selection but states that lineage is evidence, not a prison. A subphase should continue the same bounded execution gate, target output, verification gate, dependency chain, or rollback boundary. Same product area, same owner chain, or same historical phase family is insufficient by itself when the new work has its own capability, output, verification gate, release boundary, or rollback boundary.
```

### PMSB-002 — Phase saturation and umbrella escape signals

- **Target artifacts:** `../phase-implementation.md`, `../design/phase-implementation.design.md`
- **Change type:** additive refinement

**Before**
```text
Major-phase-fit signals mention materially different objective/basis/design/rollback and overloaded nesting, but the rule does not make phase saturation or umbrella-phase escape operational enough for recurring phase-family drift.
```

**After**
```text
The phase owner includes phase saturation / umbrella escape signals: many sibling subphases no longer share one clear gate, the parent label becomes a program bucket, future work needs independent closeout, verification, release, or rollback, or readers cannot tell why the work remains inside the old family without reading historical context. Those signals push toward a new main phase or an ask-now lineage decision.
```

### PMSB-003 — Same-domain-is-not-enough boundary

- **Target artifact:** `../phase-implementation.md`
- **Change type:** clarification

**Before**
```text
Subphase-fit signals include broad relation terms that can be overread as enough to keep work under an old phase family.
```

**After**
```text
The runtime rule explicitly says same product area, same broad domain, same owner chain, or same historical label does not by itself justify a subphase. The checked relationship must preserve the current phase's bounded goal/output/gate meaning.
```

### PMSB-004 — Master governed record sync

- **Target artifacts:** `../design/design.md`, `../changelog/changelog.md`, `../README.md`, `../TODO.md`, `../phase/SUMMARY.md`
- **Change type:** governed sync

**Before**
```text
Master records describe v9.94/P086 as the current release and do not yet record P076-04 bounded main/subphase boundary refinement.
```

**After**
```text
Master records describe v9.95/P076-04 with the active runtime count still 46, because P076-04 refines the existing `phase-implementation` runtime owner rather than adding a new active runtime rule.
```

### PMSB-005 — P076-04 phase record and release boundary

- **Target artifact:** `../phase/phase-076-04-main-subphase-boundary-refinement.md`
- **Change type:** additive phase record

**Before**
```text
No P076-04 child phase record exists for main/subphase boundary refinement.
```

**After**
```text
A P076-04 phase record tracks the bounded-phase doctrine, master governed sync, runtime install/parity/body-sufficiency checks, git push, and GitHub release `v9.95` gates.
```

---

## 4) Verification

- [x] `phase-implementation` runtime/design/changelog updated and audited at v2.32.
- [x] Master records, README, TODO, phase, and patch describe P076-04/v9.95 consistently.
- [x] README Bash and PowerShell install arrays remain exactly 46 active runtime files.
- [x] Runtime install parity is verified for the 46 active runtime rule files.
- [x] Active runtime body sufficiency is verified for the 46 active runtime rule files.
- [x] Source/runtime release artifacts are pushed and GitHub release `v9.95` is created.

---

## 5) Rollback Approach

If P076-04 over-corrects toward unnecessary new main phases:
- narrow phase-saturation and umbrella-escape wording while preserving the same-domain-is-not-enough boundary
- keep P076-02 lineage-first behavior intact
- keep valid subphase continuity for work that continues the same bounded goal/output/gate
- revert master v9.95 records only through a governed rollback
- keep active runtime count at 46 unless a separate governed wave changes the runtime install set
