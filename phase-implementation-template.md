# Phase Implementation Template

Use this helper when you want to draft a **readable, process-heavy phased implementation plan** using the current RULES model:
- one governed summary/index file at `phase/SUMMARY.md`
- one governed child file per live phase under `phase/`

This file is intentionally written as normal markdown.
It is a **helper**, not a governed chain.

---

## Purpose

This template helps you write a phase plan that is:
- easy to read in normal markdown
- explicit about the difference between global control and phase-local execution detail
- traceable back to the design
- clear about TODO and changelog companion work
- structured enough for day-to-day execution tracking
- detailed enough for review, handoff, and governance checkpoints

The semantic rule is `phase-implementation.md`.
The governed structure for phased work is:
- summary/index file: `phase/SUMMARY.md`
- child phase files: `phase/phase-010-<phase-name>.md`

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
  - defines what a valid `/phase` structure should contain

- `phase/SUMMARY.md`
  - the real governed summary/index file
  - the high-signal entry point for the whole phased rollout

- `phase/phase-010-<phase-name>.md`
  - the real governed child phase file
  - the place where live phase-local execution detail should exist

- `design/*.design.md`
  - the design source of truth for intended behavior
  - each child phase should cite the exact design details it is implementing, validating, or synchronizing

- `TODO.md`
  - execution tracking only
  - should reflect active work driven by the summary file and child phases

- `changelog/*.changelog.md`
  - history only
  - should capture synchronized or released outcomes, not replace the plan

- `patches/*.patch.md`
  - separate governed patch/review artifacts
  - not the live phase-plan namespace

A strong phase plan keeps all of these visible without mixing their roles.

---

## Non-negotiable boundary for phased work

If phased planning is used:
- create `phase/SUMMARY.md`
- create one child file per live phase under `phase/`
- do **not** store live phase planning under `/patches`

`SUMMARY.md` exists to stay readable and govern the whole phase workspace.
The child files exist so each phase can evolve without bloating the summary.

---

## Enterprise quick-start checklist

Before you draft the real plan, confirm this:

- [ ] This work genuinely needs phases instead of a simple linear plan
- [ ] I know the governing design file or files
- [ ] I know the exact design sections or requirements that matter
- [ ] I know that `phase/SUMMARY.md` will be the summary/index file
- [ ] I know what child phase files will likely exist
- [ ] I know what active TODO work should move during execution
- [ ] I know what changelog impact should be recorded later
- [ ] I know the main verification gates and rollback boundaries
- [ ] I know the high-risk transitions between phases
- [ ] I know who owns the execution of each major phase
- [ ] I know who or what must review or approve phase completion, if approvals matter

If most of these are unclear, discovery should happen before writing a full phase plan.

---

## What belongs in `phase/SUMMARY.md`

`SUMMARY.md` should keep the global control picture.

Recommended summary sections:
- execution control board
- context
- governing references
- design extraction summary table
- phase overview flow diagram
- review summary table
- phase map / phase index
- cross-phase coordination
- global TODO/changelog coordination
- final verification
- overall rollback / containment

`SUMMARY.md` should **not** become the place where every phase-local checklist is stored in full.

---

## What belongs in each child phase file

Each child phase file should keep the phase-local execution detail.

Recommended child sections:
- control header (`Summary File`, `Phase ID`, `Status`, `Session`)
- design references
- design extraction
- flow diagram
- reviewer checklist
- objective
- why this phase exists
- entry conditions / prerequisites
- action points
- deliverables / outputs
- ownership and approvals
- decision gate
- out of scope
- affected artifacts
- TODO coordination
- changelog coordination
- verification / evidence
- exit criteria
- sign-off record
- risks / rollback notes
- escalation path
- next possible phases

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

Recommended **sign-off status values**:
- `Pending Review`
- `Needs Revision`
- `Approved`
- `Approved With Follow-up`
- `Not Required`

Recommended **reviewer severity values**:
- `Blocking`
- `Non-Blocking`
- `Follow-Up`
- `None`

Recommended **reviewer disposition values**:
- `Must Fix Before Approval`
- `May Proceed With Follow-Up`
- `Approved As-Is`
- `No Review Required`

Recommended **plan-level health labels** if useful:
- `On Track`
- `At Risk`
- `Off Track`

---

## Recommended summary phase map columns

For an enterprise/process-heavy phase plan, this table is usually useful:

| Phase | Status | File | Objective | Design Reference | Depends On | Deliverables | TODO Impact | Changelog Impact | Gate |
|------|--------|------|-----------|------------------|------------|--------------|-------------|------------------|------|
| P1 | Pending | `phase/phase-010-<name>.md` | <objective> | `<design section>` | none | <outputs> | <todo note> | <history note> | <gate> |
| P2 | Pending | `phase/phase-020-<name>.md` | <objective> | `<design section>` | P1 | <outputs> | <todo note> | <history note> | <gate> |

Use fewer columns only if readability improves.
Do not remove file paths, design traceability, TODO impact, or changelog impact unless they are truly not relevant.

---

## `SUMMARY.md` template

Copy this block into the real summary file and replace the placeholders.

```markdown
# <Phase Plan Title>

> **Status:** <Pending / In Progress / Blocked / Completed / Deferred>
> **Target Design:** <design file / section>
> **Session:** <session-id>

---

## Execution control board

- Overall status: <Pending / In Progress / Blocked / Completed / Deferred>
- Plan health: <On Track / At Risk / Off Track>
- Current active phase: <phase id>
- Current blocker: <none / blocker summary>
- Next checkpoint: <what should happen next>
- Summary path: `phase/SUMMARY.md`
- Phase directory: `phase/`
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

## Design extraction summary table

| Phase | Phase File | Design Source | Derived Execution Work | Target Outcome |
|------|------------|---------------|------------------------|----------------|
| P1 | `phase/phase-010-<name>.md` | `<design section>` | <derived work> | <target outcome> |
| P2 | `phase/phase-020-<name>.md` | `<design section>` | <derived work> | <target outcome> |

## Phase overview flow diagram

```text
<design baseline / current-state system>
  → P1: <major phase transformation>
  → P2: <major phase transformation>
  → P3: <major phase transformation>
  → <final target state>
```

## Review summary table

| Phase | Phase File | Sign-Off Status | Reviewer Severity | Reviewer Disposition | Blocker / Follow-Up State |
|------|------------|-----------------|-------------------|----------------------|---------------------------|
| P1 | `phase/phase-010-<name>.md` | <status> | <severity> | <disposition> | <blocker or follow-up note> |
| P2 | `phase/phase-020-<name>.md` | <status> | <severity> | <disposition> | <blocker or follow-up note> |

## Phase map

| Phase | Status | File | Objective | Design Reference | Depends On | Deliverables | TODO Impact | Changelog Impact | Gate |
|------|--------|------|-----------|------------------|------------|--------------|-------------|------------------|------|
| P1 | Pending | `phase/phase-010-<name>.md` | <objective> | `<design section>` | none | <outputs> | <todo note> | <history note> | <gate> |
| P2 | Pending | `phase/phase-020-<name>.md` | <objective> | `<design section>` | P1 | <outputs> | <todo note> | <history note> | <gate> |

## Cross-phase coordination

Explain:
- which outputs from one phase are required by another
- which phases can proceed in parallel
- which verification gates block later work
- which TODO/changelog changes happen only after specific phases finish
- what escalation path exists if the plan becomes blocked

## Global TODO coordination

- <how TODO should move across the whole rollout>

## Global changelog coordination

- <what synchronized history should be recorded later>

## Final verification

- [ ] Phase order matches project reality
- [ ] `SUMMARY.md` points to every live child phase file
- [ ] Child phases own phase-local execution detail
- [ ] TODO coordination is explicit
- [ ] Changelog coordination is explicit
- [ ] End-to-end verification is clear
- [ ] Overall rollback or containment behavior is clear

## Overall rollback / containment

- <what to do if the multi-phase rollout must stop or revert>
```

---

## Child phase-file template

Copy this block into each real child phase file and replace the placeholders.

```markdown
# <Phase Title>

> **Summary File:** [SUMMARY.md](./SUMMARY.md)
> **Phase ID:** <P1 / P2 / P3>
> **Status:** <Pending / In Progress / Blocked / Completed / Deferred>
> **Session:** <session-id>

---

## Design references

- `<design file>` → `<section / anchor / requirement summary>`

## Design extraction

- Source design input: `<exact design section / requirement>`
- Derived execution work: `<what this phase is pulling from design into implementation>`
- Phase intent: `<enhance / develop / migrate / validate / replace>`
- Source element: `<what existing part this phase starts from>`
- Target outcome: `<what resulting component / workflow / state this phase produces>`

## Flow diagram

```text
<source design element or current-state part>
  → <phase action / enhancement / migration / validation>
  → <target component / workflow / operational state>
```

## Reviewer checklist

- [ ] Design source is correct for this phase
- [ ] Derived execution work is justified by the cited design source
- [ ] Source → phase action → target outcome flow is clear
- [ ] Phase boundary is correct and this work belongs here
- [ ] Dependencies and handoffs are clear enough for safe progression
- [ ] Verification evidence is sufficient for review or sign-off

## Review outcome

- Sign-off status: `<Pending Review / Needs Revision / Approved / Approved With Follow-up / Not Required>`
- Reviewer severity: `<Blocking / Non-Blocking / Follow-Up / None>`
- Reviewer disposition: `<Must Fix Before Approval / May Proceed With Follow-Up / Approved As-Is / No Review Required>`
- Review notes: `<short review outcome note>`

## Objective

- <what this phase must achieve>

## Why this phase exists

- <why this is separated from the others>

## Entry conditions / prerequisites

- <what must already be true>

## Action points

- [ ] <first concrete action>
- [ ] <second concrete action>
- [ ] <third concrete action>

## Deliverables / outputs

- <file / artifact / result>
- <file / artifact / result>

## Ownership and approvals

- Owner: <owner>
- Reviewer: <reviewer>
- Approver: <approver or not required>
- Approval condition: <what must be true for approval>

## Decision gate

- <what must be satisfied before moving beyond this phase>

## Out of scope

- <what this phase intentionally does not do>

## Affected artifacts

- `<file / service / document>`
- `<file / service / document>`

## TODO coordination

- <what TODO items should be opened, updated, or closed during this phase>

## Changelog coordination

- <what changelog entry should be added when this phase or rollout completes>

## Verification / evidence

- <phase-level checks>
- <phase-level proof>

## Exit criteria

- <what must be true before leaving this phase>

## Sign-off record

- Decision: <Pending / Approved / Rework Required / Not Required>
- Decided by: <name / role>
- Decision date: <date>
- Decision notes: <notes>

## Risks / rollback notes

- Risk: <risk>
- Rollback / containment: <what to do if this phase fails>

## Escalation path

- <who or what to escalate to if blocked>

## Next possible phases

- <next phase>
- <optional alternate next phase>
```

---

## Minimal realistic example

Below is a small example showing the new model.

### Example file layout

```text
phase/
  SUMMARY.md
  phase-010-create-rule.md
  phase-020-realign-docs.md
  phase-030-verify-rollout.md
```

### Example summary design extraction table

```markdown
| Phase | Phase File | Design Source | Derived Execution Work | Target Outcome |
|------|------------|---------------|------------------------|----------------|
| P1 | `phase/phase-010-create-rule.md` | `design/phase-implementation.design.md` → phase-rule sections | create first-class runtime/design/changelog phase chain | dedicated semantic rule for phased execution |
| P2 | `phase/phase-020-realign-docs.md` | `design/document-patch-control.design.md` + `design/project-documentation-standards.design.md` | rewrite repo governance and namespace rules | `/phase` becomes the active live phase workspace |
| P3 | `phase/phase-030-verify-rollout.md` | active governance requirements across updated docs | run verification and close synchronized rollout state | stable repo state with aligned phase model |
```

### Example summary overview flow

```text
Legacy governance model
  → P1: create first-class phase rule chain
  → P2: realign repo governance and namespace rules
  → P3: verify rollout and close synchronized state
  → target governance model with `/phase/SUMMARY.md` + child phase files
```

### Example review summary table

```markdown
| Phase | Phase File | Sign-Off Status | Reviewer Severity | Reviewer Disposition | Blocker / Follow-Up State |
|------|------------|-----------------|-------------------|----------------------|---------------------------|
| P1 | `phase/phase-010-create-rule.md` | `Approved` | `None` | `Approved As-Is` | none |
| P2 | `phase/phase-020-realign-docs.md` | `Needs Revision` | `Blocking` | `Must Fix Before Approval` | stale `/patches` live-phase wording remains |
| P3 | `phase/phase-030-verify-rollout.md` | `Pending Review` | `None` | `No Review Required` | pending completion of P2 |
```

### Example summary phase map

```markdown
| Phase | Status | File | Objective | Depends On |
|------|--------|------|-----------|------------|
| P1 | Completed | `phase/phase-010-create-rule.md` | Create new rule chain | none |
| P2 | In Progress | `phase/phase-020-realign-docs.md` | Realign governance docs | P1 |
| P3 | Pending | `phase/phase-030-verify-rollout.md` | Verify rollout and close | P2 |
```

### Canonical child phase example

```markdown
# P2 — Realign governance docs

> **Summary File:** [SUMMARY.md](./SUMMARY.md)
> **Phase ID:** P2
> **Status:** In Progress
> **Session:** <session-id>

## Design references
- `design/document-patch-control.design.md` → patch-versus-phase boundary section
- `design/project-documentation-standards.design.md` → repository role model section

## Design extraction
- Source design input: patch layer must stop acting as live phase namespace
- Derived execution work: rewrite governance wording so `/phase` becomes the active phase workspace
- Phase intent: migrate governance semantics
- Source element: legacy patch-oriented phase wording
- Target outcome: explicit `/phase`-first repository behavior

## Flow diagram

```text
Legacy patch-oriented phase wording
  → phase action: rewrite namespace and role boundaries
  → target governance wording with `/phase/SUMMARY.md` + child phase files
```

## Reviewer checklist
- [ ] Design source is correct for this phase
- [x] Derived execution work is justified by the cited design source
- [x] Source → phase action → target outcome flow is clear
- [x] Phase boundary is correct and this work belongs here
- [ ] Dependencies and handoffs are clear enough for safe progression
- [ ] Verification evidence is sufficient for review or sign-off

## Review outcome
- Sign-off status: `Needs Revision`
- Reviewer severity: `Blocking`
- Reviewer disposition: `Must Fix Before Approval`
- Review notes: stale `/patches` phase-namespace wording still appears in active governance docs

## Objective
- Move active governance wording to the `/phase` model without leaving stale patch-based execution semantics behind.

## Why this phase exists
- The repository cannot be reviewed cleanly until the namespace and authority split are aligned across the affected governance documents.

## Entry conditions / prerequisites
- `phase-implementation` already defines `/phase` as the live execution namespace.
- The affected governance files have been identified.

## Action points
- [x] Refocus patch-control wording
- [ ] Update repository role model wording
- [ ] Verify no stale `/patches` live-phase language remains

## Deliverables / outputs
- updated governance wording in affected runtime/design docs
- verified `/phase`-first namespace references

## Ownership and approvals
- Owner: governance maintainer
- Reviewer: repository reviewer
- Approver: not required
- Approval condition: affected docs align and drift search passes

## Decision gate
- Do not close this phase until stale `/patches` live-phase wording is fully removed from the active governance set.

## Out of scope
- installing unrelated new runtime rules
- changing non-phase governance chains that are unaffected by this namespace shift

## Affected artifacts
- `document-patch-control.md`
- `project-documentation-standards.md`
- related design/changelog files

## TODO coordination
- Keep the rollout item open until drift search passes and the summary/child model is fully reflected.

## Changelog coordination
- Record one synchronized history note after all affected governance chains align.

## Verification / evidence
- `/phase/SUMMARY.md` remains the active summary/index
- child phase files hold the live detailed execution checklists
- no active governance file still presents `/patches` as the live phase-plan namespace

## Exit criteria
- Active governance wording is aligned with the `/phase` execution model.
- Reviewers can trace the namespace transition without ambiguity.

## Sign-off record
- Decision: Pending
- Decided by: <name / role>
- Decision date: <date>
- Decision notes: finalize after drift verification passes

## Risks / rollback notes
- Risk: one stale governance file reintroduces patch-based phase confusion.
- Rollback / containment: pause rollout closure and correct the stale reference before proceeding.

## Escalation path
- Escalate to the owner of the stale governance chain if drift remains unresolved.

## Next possible phases
- P3 — Verify rollout and close synchronized state
```

### Short child phase excerpt

```markdown
# P2 — Realign governance docs

> **Summary File:** [SUMMARY.md](./SUMMARY.md)
> **Phase ID:** P2
> **Status:** In Progress
> **Session:** <session-id>

## Design references
- `design/document-patch-control.design.md` → patch-versus-phase boundary section
- `design/project-documentation-standards.design.md` → repository role model section

## Design extraction
- Source design input: patch layer must stop acting as live phase namespace
- Derived execution work: rewrite governance wording so `/phase` becomes the active phase workspace
- Phase intent: migrate governance semantics
- Source element: legacy patch-oriented phase wording
- Target outcome: explicit `/phase`-first repository behavior

## Flow diagram

```text
Legacy patch-oriented phase wording
  → phase action: rewrite namespace and role boundaries
  → target governance wording with `/phase/SUMMARY.md` + child phase files
```
```

---

## Common mistakes

Avoid these mistakes when using phases:
- turning this helper into a pseudo-governed document
- using a fake `Phase 1 → 5` flow even when the project does not need it
- forgetting to create `phase/SUMMARY.md`
- storing live phase planning under `/patches`
- forgetting to cite the design sections that justify a phase
- failing to show what execution work was actually derived from the design
- omitting the review flow diagram for a child phase
- writing child phases with no status or no action checklist
- writing child phases with vague objectives but no observable outputs
- treating TODO as the full plan instead of the execution tracker
- treating changelog as the plan instead of the history record
- forgetting verification evidence, exit criteria, or rollback notes

---

## Completion boundary and stop rule

Treat the phase-planning model as complete when:
- `/phase` is the live namespace
- `phase/SUMMARY.md` contains the required summary-level structures
- child phase files contain the required design, review, and execution structures
- review outcome vocabulary is standardized across child phases
- rule/design/changelog/template/TODO synchronization is complete

After that point:
- do not add new mandatory capability blocks by default
- only continue for bug fixes, wording clarifications, inconsistency corrections, broken references, or explicit user-requested scope changes

## Final reminder

If this plan becomes the real live plan:
- keep `phase/SUMMARY.md` authoritative as the governing summary/index
- keep each live phase in its own child file under `phase/`
- keep live phase planning out of `/patches`
- keep the helper readable
- keep the design references explicit
- keep TODO and changelog visible as companion artifacts
