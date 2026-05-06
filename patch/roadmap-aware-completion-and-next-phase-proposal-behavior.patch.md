# Roadmap-Aware Completion and Next-Phase Proposal Behavior Patch

## 0) Document Control

> **Current Version:** 1.0
> **Status:** In Progress
> **Target Design:** [../design/design.md](../design/design.md) v9.89
> **Session:** d42465eb-30a7-4bc8-b9d6-03e52306e9a5
> **Full history:** [../changelog/changelog.md](../changelog/changelog.md)

---

## 1) Context

P075-02 responds to a closeout and roadmap gap: after all selected work is complete, the assistant can stop without proposing the next meaningful phase even when checked roadmap surfaces show successor work. At the same time, next-step proposals must not become a blocker between selected, safe, unblocked phases.

พูดง่าย ๆ: ทำงานต่อเนื่องก่อนเมื่อทางถัดไปถูกเลือกและปลอดภัย แต่เมื่อจบจริงแล้วควรเสนอ next phase ที่มีหลักฐานรองรับจาก design/phase/TODO แทนที่จะเงียบ.

This patch separates the work types:

### Runtime active rule changes

These are behavior/semantic rule changes:
- `phase-implementation.md`
- `execution-continuity-and-mode-selection.md`
- `response-closing-and-action-framing.md`
- `explanation-quality.md`
- `answer-presentation.md`
- `high-signal-communication.md`
- `native-worker-agent-routing-and-context-control.md`

### Development docs / governed record sync only

These are companion record updates only, not runtime-rule improvement targets:
- paired `design/*.design.md`
- paired `changelog/*.changelog.md`
- `design/design.md`
- `changelog/changelog.md`
- `README.md`
- `TODO.md`
- `phase/SUMMARY.md`
- `phase/phase-075-02-roadmap-aware-completion-and-next-phase-proposal-behavior.md`
- this patch file

---

## 2) Analysis

Risk level: Medium

Dependencies:
- P075-01 established delivery/feature/impact/verification closeout reporting.
- P076 established design-to-phase execution synthesis.
- P076-02 established lineage-first phase identity selection.
- P076-03 established visible phase linkage in non-trivial phase-backed live tasks.
- P081-02 established broad research/design-improvement worker-lane orchestration.
- P073-10 established 44-file active runtime body-sufficiency validation.

Review concerns:
- Do not weaken continuation-first behavior when selected safe work can continue.
- Do not turn advisory next work into automatic execution authority.
- Do not make every simple answer include a roadmap block or deep-dive offer.
- Do not strip required next recommendations through high-signal pruning.
- Do not change the 44-file active runtime install list.
- Do not treat README/TODO/phase/patch/design/changelog as runtime-rule targets.

---

## 3) Change Items

### RCNP-001 — `phase-implementation.md` roadmap and phase-matrix synthesis

- **Target artifact:** `../phase-implementation.md`
- **Target locations:** source-input synthesis, verification/closeout behavior, phase summary responsibilities, trigger/anti-pattern/checklist language
- **Change type:** additive + metadata alignment

**Before**
```text
Phase planning can synthesize current staged execution from design and close a phase with delivery, impact, verification, and next phase state.
```

**After**
```text
When checked design/TODO/phase/implementation evidence supports more than the current slice, phase summary can carry a bounded roadmap or phase matrix with candidate phases, dependencies, gates, deliverables, and status. True closeout can recommend the best-supported next phase or wave with goal, expected output, and gate while preserving advisory status for unselected work.
```

**Preserved behavior**
- `/phase` remains live execution synthesis, not design authority.
- Selected safe continuation is not converted into a proposal pause.
- Draft/proposal roadmap entries do not become active phases by implication.

### RCNP-002 — `execution-continuity-and-mode-selection.md` completion-to-roadmap bridge

- **Target artifact:** `../execution-continuity-and-mode-selection.md`
- **Target locations:** continuous execution, active next-work discovery, legitimate stop gates, trigger model, anti-patterns
- **Change type:** additive + metadata alignment

**Before**
```text
When execution mode remains active and safe next work is discoverable, continue rather than stopping for milestone-only narration.
```

**After**
```text
When the active objective is actually complete, classify successor state: selected and unblocked successor work continues; meaningful unselected successor work is recommended as advisory next work; ambiguous or approval-sensitive successor work asks narrowly; no visible successor is reported as none selected/opened.
```

**Preserved behavior**
- Completion-to-roadmap behavior is closeout-only, not a mid-execution stop ritual.
- Verification pending still continues when safe.
- Broad successor analysis still passes through worker routing when appropriate.

### RCNP-003 — `response-closing-and-action-framing.md` roadmap-aware completion owner

- **Target artifact:** `../response-closing-and-action-framing.md`
- **Target locations:** rule statement, core principles, preferred shapes, anti-patterns, quality metrics
- **Change type:** additive + metadata alignment

**Before**
```text
The closing chain owns concise synthesis, action framing, recommendation-with-reason wording, alternatives, phase-backed closeout synthesis, and advisory proposals.
```

**After**
```text
The closing chain also owns roadmap-aware completion: after true objective completion, first close delivered work, then recommend supported next phase or wave with goal, output, and gate when checked roadmap surfaces show meaningful unselected successor work.
```

**Preserved behavior**
- Recommendations remain advisory unless selected.
- No recommendation block is added when selected safe continuation is already underway.
- No future work is invented when checked scope shows none.

### RCNP-004 — `explanation-quality.md` easy-first completion explanation and optional deep dive

- **Target artifact:** `../explanation-quality.md`
- **Target locations:** core requirements, phase/progress explanation, closing/decision usefulness, compact examples, anti-patterns
- **Change type:** additive + metadata alignment

**Before**
```text
Explanations should be plain-language-first, complete enough for action, and stop before overexplaining.
```

**After**
```text
Easy-first explanations can remain compact while still landing with a supported next roadmap recommendation at true completion and one optional, specific deep-dive offer when more detail may help.
```

**Preserved behavior**
- The answer does not auto-expand into the deep dive.
- Deep-dive offers are omitted when active execution should continue or the answer is already detailed enough.
- Plain-language-first explanation stays evidence-calibrated.

### RCNP-005 — `answer-presentation.md` compact roadmap and deep-dive patterns

- **Target artifact:** `../answer-presentation.md`
- **Target locations:** specialized compact patterns, trigger model, preferred output shapes, canonical examples
- **Change type:** additive + metadata alignment

**Before**
```text
Presentation includes compact phase-backed closeout and advisory proposal layouts.
```

**After**
```text
Presentation adds a compact roadmap-aware completion layout: recommended next, why this next, goal, output, and gate, plus a one-line optional deep-dive offer when useful.
```

**Preserved behavior**
- Headings are used only when they improve scanability.
- Simple answers remain compact.
- The roadmap block does not interrupt selected safe phase progression.

### RCNP-006 — `high-signal-communication.md` pruning boundary

- **Target artifact:** `../high-signal-communication.md`
- **Target locations:** extra-content admission, repetition pruning, never-remove-required-content boundary
- **Change type:** additive + metadata alignment

**Before**
```text
High-signal pruning removes low-value extra content and repeated wording without replacing main owner chains.
```

**After**
```text
High-signal pruning must preserve goal-qualified roadmap recommendations and compact optional deep-dive offers when an active owner requires them, while still removing surplus wording.
```

**Preserved behavior**
- The rule remains supplementary.
- It does not become a new closing or explanation owner.
- It trims only surplus wording, not required content.

### RCNP-007 — `native-worker-agent-routing-and-context-control.md` roadmap/phase-matrix worker routing

- **Target artifact:** `../native-worker-agent-routing-and-context-control.md`
- **Target locations:** worker-scale gate, research orchestration, broad-work triggers, verification checklist
- **Change type:** additive + metadata alignment

**Before**
```text
Broad research, design-improvement, provider/API comparison, source comparison, and source-heavy recommendation work can be mapped into focused worker lanes.
```

**After**
```text
Broad roadmap or phase-matrix analysis can also use focused worker lanes decomposed by phase candidate, dependency, risk area, design axis, or verification gate before the leader absorbs raw design/TODO/phase surfaces.
```

**Preserved behavior**
- One coherent lane is preferred when enough.
- Agent Team workflow remains exceptional.
- Leader verification remains mandatory.

### RCNP-008 — Master records, phase summary, README, TODO, and runtime install sync

- **Target artifacts:** `../design/design.md`, `../changelog/changelog.md`, `../README.md`, `../TODO.md`, `../phase/SUMMARY.md`, `../phase/phase-075-02-roadmap-aware-completion-and-next-phase-proposal-behavior.md`, this patch file
- **Change type:** companion sync only

**Before**
```text
Master records are synchronized through v9.88 / P073-10 and do not yet record P075-02 roadmap-aware completion behavior.
```

**After**
```text
Master records record v9.89 / P075-02 as a narrow continuation of the P075 closeout/reporting family, active runtime count remains 44, and runtime install/parity/body-sufficiency verification runs before release completion claims.
```

---

## 4) Verification

- [x] Runtime rule changes are limited to the seven listed active runtime owners.
- [x] Development docs/governed record changes are companion sync only.
- [x] Roadmap-aware completion preserves selected safe continuation and keeps unselected future work advisory.
- [x] Optional deep-dive offers remain one-line, specific, and non-automatic.
- [x] README active runtime install list remains 44 files.
- [x] Runtime install copies only the 44 active runtime rule files.
- [x] Source/runtime parity and body sufficiency pass for the active runtime install set.
- [x] No plugin/project-owned runtime destination files are touched.
- [ ] Git push and GitHub release `v9.89` are verified.

---

## 5) Rollback Approach

If P075-02 proves too broad:
- narrow or revert only the seven roadmap-aware completion / optional deep-dive / roadmap-worker routing changes and companion record entries
- preserve P075-01 phase-backed delivery/feature/impact closeout reporting unless separately challenged
- preserve P076 design-to-phase synthesis and P076-02 lineage-first phase identity selection
- preserve P081-02 research orchestration and P073-10 active runtime body-sufficiency boundaries
- do not delete or manage destination/runtime files outside the current source-owned active runtime install set as part of rollback
