# Phase Implementation Template

Use this helper when you want to draft a **readable, process-heavy phased implementation plan** before or while creating the real governed patch document in `patches/*.patch.md`.

This file is intentionally written as normal markdown.
It is a **helper**, not a governed chain.

---

## Purpose

This template helps you write a phase plan that is:
- easy to read in normal markdown
- explicit about what each phase is doing
- traceable back to the design
- clear about TODO and changelog companion work
- structured enough for day-to-day execution tracking
- detailed enough for review, handoff, and governance checkpoints

The semantic rule is `phase-implementation.md`.
The live governed plan instance belongs in `patches/*.patch.md`.

---

## When to use this

Use this template when:
- the work has multiple real stages
- one stage produces outputs needed by a later stage
- verification gates matter between stages
- migration or rollout order matters
- rollback or containment boundaries matter
- you need to show how execution maps back to the design
- TODO and changelog coordination should be visible while planning
- multiple people, systems, or document chains are involved and need a clear operating view

Do **not** use this template when the task is so small that a normal implementation checklist is enough.

---

## Operating model

Use the repository roles like this:

- `phase-implementation.md`
  - semantic rule for phase behavior
  - defines what a valid phase should contain

- `patches/*.patch.md`
  - the real governed execution-plan file
  - the place where the live authoritative plan should exist

- `design/*.design.md`
  - the design source of truth for intended behavior
  - each phase should cite the exact design details it is implementing, validating, or synchronizing

- `TODO.md`
  - execution tracking only
  - should reflect active work driven by the patch

- `changelog/*.changelog.md`
  - history only
  - should capture synchronized or released outcomes, not replace the plan

A strong phase plan keeps all of these visible without mixing their roles.

---

## Enterprise quick-start checklist

Before you draft the real plan, confirm this:

- [ ] This work genuinely needs phases instead of a simple linear plan
- [ ] I know the governing design file or files
- [ ] I know the exact design sections or requirements that matter
- [ ] I know what the final governed patch file path will be
- [ ] I know what active TODO work should move during execution
- [ ] I know what changelog impact should be recorded later
- [ ] I know the main verification gates and rollback boundaries
- [ ] I know the high-risk transitions between phases
- [ ] I know who owns the execution of each major phase
- [ ] I know who or what must review or approve phase completion, if approvals matter

If most of these are unclear, discovery should happen before writing a full phase plan.

---

## Execution control board

In a real patch, it is useful to keep one short control board near the top.
This is the high-signal operating view for humans scanning the plan.

Recommended fields:
- overall plan status
- plan health
- current active phase
- current blocker
- next checkpoint
- target patch file path
- target design file path
- execution owner
- reviewer or approver
- risk level
- last verification checkpoint
- last approval checkpoint when approvals matter

This section is not a substitute for deeper phase sections.
It is just the executive summary of the current state.

---

## What a strong phase plan should show

A strong phase plan usually makes all of these clear:

### 1) Overall plan context
- current state
- target state
- why phased execution is useful here

### 2) Phase tracking
- phase name or ID
- current status
- dependencies
- outputs
- key gate or checkpoint

### 3) Design traceability
- exactly which design sections or requirements are being executed in each phase
- not just "follow design" in general

### 4) Execution detail
- concrete action points
- what is intentionally out of scope
- what files or systems are affected
- what evidence should exist when the phase is done

### 5) Companion tracking
- what TODO movement is expected
- what changelog movement is expected
- when those companion updates should happen

### 6) Safety and governance
- verification gates
- exit criteria
- rollback or containment notes
- escalation or blocker handling when needed
- owner / reviewer / approver visibility when governance sign-off matters
- explicit decision gates before high-impact transitions

---

## Suggested status model

Use any simple status set you want, but keep it explicit and consistent.

Recommended **phase statuses**:
- `Pending`
- `In Progress`
- `Blocked`
- `Completed`
- `Deferred`

Recommended **action-point statuses** inside a phase:
- `[ ]` not started
- `[x]` completed
- `[-]` intentionally skipped or not applicable

Recommended **plan-level health labels** if useful:
- `On Track`
- `At Risk`
- `Off Track`

---

## Recommended phase map columns

For an enterprise/process-heavy patch, this table is usually useful:

| Phase | Status | Objective | Design Reference | Depends On | Deliverables | TODO Impact | Changelog Impact | Gate |
|------|--------|-----------|------------------|------------|--------------|-------------|------------------|------|
| P1 | Pending | <objective> | `<design section>` | none | <outputs> | <todo note> | <history note> | <gate> |
| P2 | Pending | <objective> | `<design section>` | P1 | <outputs> | <todo note> | <history note> | <gate> |

Use fewer columns only if readability improves.
Do not remove design traceability, TODO impact, or changelog impact unless they are truly not relevant.

---

## Required phase detail blocks

For each phase, try to keep the same shape so the plan stays easy to operate.

### 1) Status
Show the current phase status clearly.

### 2) Design references
Cite the exact design details being implemented or validated.

Good examples:
- `design/payment-flow.design.md` → section 4.2
- `design/api-gateway.design.md` → "Request validation" subsection
- `design/design.md` → active runtime inventory update requirement

Weak example:
- "follow the design"

### 3) Objective
State what this phase must achieve.

### 4) Why this phase exists
Explain why it is separated from the others.

### 5) Entry conditions / prerequisites
State what must already be true before this phase starts.

### 6) Action points
Use concrete checkable work items.
These are the operational heart of the phase.

### 7) Deliverables / outputs
State what must exist when the phase is done.
This can be files, updated docs, runtime artifacts, test results, approvals, or synced metadata.

### 8) Ownership and approvals
State who drives the phase and who must review or approve it when sign-off matters.

Useful fields:
- owner
- reviewer
- approver
- approval condition

### 9) Decision gate
If the next transition is high-impact, state the explicit gate.

Examples:
- do not proceed until runtime/design/changelog versions align
- do not install runtime copies until repo files are final
- do not close rollout until drift search passes

### 10) Out of scope
Protect the phase from silent scope creep.

### 11) Affected artifacts
List the files, systems, chains, or services touched by this phase.

### 12) TODO coordination
State how TODO should move during or after the phase.

Examples:
- open new active tasks before phase start
- mark rollout task complete only after verification passes
- keep deferred work visible but outside current execution scope

### 13) Changelog coordination
State what history should be recorded later.

Examples:
- add a synchronized rollout entry after the governed chain aligns
- record runtime installation only after installed copy verification passes
- keep historical correction wording explicit when cleaning legacy references

### 14) Verification / evidence
State what proof is required.

Examples:
- drift search passes
- versions match
- installed runtime copy matches repo version
- affected links resolve
- test command or search result confirms expected state

### 15) Exit criteria
State what must be true before the phase is considered complete.

### 16) Sign-off record
If formal review matters, show the decision explicitly.

Suggested fields:
- decision
- decided by
- decision date
- decision notes

### 17) Risks / rollback notes
State failure boundaries and what to do if the phase goes wrong.

### 18) Escalation path
If the phase becomes blocked or at-risk, state who or what should be escalated.

### 19) Next possible phases
Show where execution goes next.

---

## Governance review checklist

Use this at the end of a phase review or before changing phase status to `Completed`.

- [ ] Phase status reflects reality
- [ ] Design references still point to the correct intended behavior
- [ ] Action points reflect the real remaining work
- [ ] Deliverables are explicit and observable
- [ ] Owner / reviewer / approver expectations are still clear
- [ ] TODO coordination still matches execution state
- [ ] Changelog coordination still matches what should be recorded later
- [ ] Verification evidence is specific enough to justify the decision
- [ ] Exit criteria are satisfied or clearly not yet satisfied
- [ ] Sign-off requirements are satisfied when needed
- [ ] Rollback or containment notes are still valid
- [ ] Escalation path is clear if the phase becomes blocked
- [ ] Next phase is clear

---

## Minimal realistic example

Below is a small example that still reads like normal markdown.

---

### Example: Create first-class phase rule and realign helper usage

## Context

The repository currently supports phase behavior indirectly through patch-control, but there is no dedicated rule chain for phase semantics.
The helper template also looks too much like a governed file.

The target state is:
- a first-class `phase-implementation.md` rule
- patch files remain the live governed plans
- the root helper becomes readable normal markdown

## Execution control board

- Overall status: In Progress
- Plan health: On Track
- Current active phase: P2
- Current blocker: none
- Next checkpoint: finish governance realignment and verify drift search
- Governing patch path: `patches/phase-implementation-rollout.patch.md`
- Target design path: `design/phase-implementation.design.md`
- Execution owner: documentation maintainer
- Reviewer / approver: governance reviewer
- Risk level: Medium
- Last verification checkpoint: new phase chain created and linked
- Last approval checkpoint: not required yet

## Phase map

| Phase | Status | Objective | Design Reference | Depends On | Deliverables | TODO Impact | Changelog Impact | Gate |
|------|--------|-----------|------------------|------------|--------------|-------------|------------------|------|
| P1 | Completed | Create phase rule chain | `design/phase-implementation.design.md` sections 1-6 | none | rule/design/changelog baseline | keep rollout open | record chain creation | chain exists |
| P2 | In Progress | Realign governance docs | `design/document-patch-control.design.md` section 8 | P1 | updated role model | keep rollout open | record authority split | drift review |
| P3 | Pending | Rewrite helper and install runtime copies | `design/design.md` phase-planning contract | P2 | readable helper + installed rules | close rollout on success | record rollout closure | installed-copy match |

## P2 — Realign governance docs

**Status**
- In Progress

**Design references**
- `design/document-patch-control.design.md` section 8
- `design/project-documentation-standards.design.md` section 6

**Objective**
- Move semantic phase authority into the new rule while keeping patches as the governed plan instances.

**Why this phase exists**
- The repository needs a clear authority split before the helper is finalized and runtime installation is closed.

**Entry conditions / prerequisites**
- The new `phase-implementation` chain already exists.

**Action points**
- [x] Refocus patch-control wording
- [ ] Update project-documentation standards wording
- [ ] Update master design and master changelog references
- [ ] Run drift search for stale authority language

**Deliverables / outputs**
- updated runtime/design/changelog authority wording
- aligned repository role model
- drift-check evidence

**Ownership and approvals**
- Owner: documentation maintainer
- Reviewer: governance reviewer
- Approver: repository maintainer when rollout wording changes the active model
- Approval condition: all affected governance docs align and drift search passes

**Decision gate**
- Do not proceed to helper finalization until authority wording is aligned across patch-control, project-documentation standards, and master design.

**Out of scope**
- final runtime installation

**Affected artifacts**
- `document-patch-control.md`
- `project-documentation-standards.md`
- `design/design.md`
- related changelog files

**TODO coordination**
- Keep the rollout task open until authority-model updates are synchronized and verified.

**Changelog coordination**
- Add one synchronized rollout entry after the rule, governance docs, and master docs all align.

**Verification / evidence**
- No active doc still claims patch-control is the only phase-semantics authority.
- Patch docs still remain the governed execution-plan artifacts.
- Active references point to `phase-implementation.md` for semantics.

**Exit criteria**
- Governance docs clearly distinguish semantic rule, governed patch, helper, TODO, and changelog roles.

**Sign-off record**
- Decision: Pending
- Decided by: governance reviewer
- Decision date: <set when approved>
- Decision notes: finalize after drift review passes

**Risks / rollback notes**
- Risk: one file keeps stale wording and reintroduces authority confusion.
- Containment: run a drift search before closing the phase.

**Escalation path**
- If drift remains unresolved, escalate to the owner of the affected governance chain before moving to the next phase.

**Next possible phases**
- P3 helper rewrite and runtime installation

---

## Common mistakes

Avoid these mistakes when using phases:
- turning this helper into a pseudo-governed document
- using a fake `Phase 1 → 5` flow even when the project does not need it
- forgetting to cite the design sections that justify a phase
- writing phases with no status or no action checklist
- writing phases with vague objectives but no observable outputs
- treating TODO as the full plan instead of the execution tracker
- treating changelog as the plan instead of the history record
- forgetting verification evidence, exit criteria, or rollback notes

---

## Copyable skeleton

Copy the block below into a real patch file and replace the placeholders.

```markdown
# <Patch Title>

## Execution control board

- Overall status: <Pending / In Progress / Blocked / Completed / Deferred>
- Plan health: <On Track / At Risk / Off Track>
- Current active phase: <phase id>
- Current blocker: <none / blocker summary>
- Next checkpoint: <what should happen next>
- Governing patch path: `patches/<context>.patch.md`
- Target design path: `<design file path>`
- Execution owner: <owner>
- Reviewer / approver: <reviewer or approver>
- Risk level: <Low / Medium / High>
- Last verification checkpoint: <latest verified checkpoint>
- Last approval checkpoint: <latest approval or not required>

## Context

Describe:
- current state
- target state
- why phased execution is useful here
- why a simple linear plan is not enough

## Governing references

- Target design: `<design file>`
- Phase rule: `phase-implementation.md`
- TODO companion: `TODO.md`
- Changelog companion: `<relevant changelog file>`

## Phase map

| Phase | Status | Objective | Design Reference | Depends On | Deliverables | TODO Impact | Changelog Impact | Gate |
|------|--------|-----------|------------------|------------|--------------|-------------|------------------|------|
| P1 | Pending | <objective> | `<design section>` | none | <outputs> | <todo note> | <history note> | <gate> |
| P2 | Pending | <objective> | `<design section>` | P1 | <outputs> | <todo note> | <history note> | <gate> |

## <Phase ID> — <Phase Name>

**Status**
- <Pending / In Progress / Blocked / Completed / Deferred>

**Design references**
- `<design file>` → `<section / anchor / requirement summary>`

**Objective**
- <what this phase must achieve>

**Why this phase exists**
- <why this is separated from the others>

**Entry conditions / prerequisites**
- <what must already be true>

**Action points**
- [ ] <first concrete action>
- [ ] <second concrete action>
- [ ] <third concrete action>

**Deliverables / outputs**
- <file / artifact / result>
- <file / artifact / result>

**Ownership and approvals**
- Owner: <owner>
- Reviewer: <reviewer>
- Approver: <approver or not required>
- Approval condition: <what must be true for approval>

**Decision gate**
- <what must be satisfied before moving beyond this phase>

**Out of scope**
- <what this phase intentionally does not do>

**Affected artifacts**
- `<file / service / document>`
- `<file / service / document>`

**TODO coordination**
- <what TODO items should be opened, updated, or closed during this phase>

**Changelog coordination**
- <what changelog entry should be added when this phase or rollout completes>

**Verification / evidence**
- <phase-level checks>
- <phase-level proof>

**Exit criteria**
- <what must be true before leaving this phase>

**Sign-off record**
- Decision: <Pending / Approved / Rework Required / Not Required>
- Decided by: <name / role>
- Decision date: <date>
- Decision notes: <notes>

**Risks / rollback notes**
- Risk: <risk>
- Rollback / containment: <what to do if this phase fails>

**Escalation path**
- <who or what to escalate to if blocked>

**Next possible phases**
- <next phase>
- <optional alternate next phase>

## Cross-phase coordination

Explain:
- which outputs from one phase are required by another
- which phases can proceed in parallel
- which verification gates block later work
- which TODO/changelog changes happen only after specific phases finish
- what escalation path exists if the plan becomes blocked

## Final verification

- [ ] Phase order matches project reality
- [ ] Each phase has a clear status
- [ ] Each phase cites the relevant design details
- [ ] Action points are concrete and trackable
- [ ] Deliverables are explicit
- [ ] TODO coordination is explicit
- [ ] Changelog coordination is explicit
- [ ] Verification and exit criteria are clear
- [ ] Rollback or containment notes exist where needed
```

---

## Final reminder

If this plan becomes the real live plan, move it into `patches/*.patch.md`.

Keep this helper readable.
Keep the patch authoritative.
Keep the design references explicit.
Keep TODO and changelog visible as companion artifacts.
