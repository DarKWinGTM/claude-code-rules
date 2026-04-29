# Phase Implementation

> **Current Version:** 2.25
> **Design:** [design/phase-implementation.design.md](design/phase-implementation.design.md) v2.25
> **Session:** d42465eb-30a7-4bc8-b9d6-03e52306e9a5
> **Full history:** [changelog/phase-implementation.changelog.md](changelog/phase-implementation.changelog.md)

---

## Rule Statement

**Core Principle: Use phased planning only when staged execution improves clarity, synthesize sufficiently clear governed design into live phase execution order, establish a dedicated active `/phase` workspace with mandatory `SUMMARY.md` and deterministic `NNN` / `NNN-NN` IDs, allow completed phase details to move to inactive `phase/done/` history, resolve phase posture early through startup governance, and declare governed patch participation when patch is in scope.**

This rule owns phase-execution semantics. `phase/SUMMARY.md` is the governed summary/index; active child phase files hold phase-local execution detail; `phase/done/` may hold inactive completed phase history; design is target-state authority; patch is governed before/after review authority; root phase helpers are non-governed. Multi-session shared-board, plugin, and external coordination/runtime mechanics stay outside Main RULES doctrine.

---

## Purpose and Authority Boundary

`phase-implementation.md` defines:
- when phase planning should be used or skipped
- `/phase` structure, phase ID grammar, and child phase field expectations
- how design and governed patch references map into phases
- how completed phase history may move to `phase/done/` without becoming active execution input by default
- cross-phase handoffs, TODO/changelog coordination, verification, rollback boundaries, and closeout reporting expectations
- how phase may synthesize sufficiently clear design and patch inputs one-way into execution order without becoming source of truth

It does **not** replace `phase/SUMMARY.md`, child phase files, design docs, patch docs, `TODO.md`, changelogs, or `artifact-initiation-control.md`.

---

## When to Use Phase Planning

Use phases when work has meaningful stages, gated rollout/migration/verification, rollback or containment boundaries, later stages depending on earlier outputs, multi-system/multi-owner coordination, or a need to show how design/TODO/changelog move together.

Do not force phases for a single obvious low-risk change, a normal checklist, or filler stages with no execution meaning.

If staged work is clearly implied, startup governance must resolve phase posture as `use existing`, `create now`, or `ask now` before substantial drift. If phase need is ambiguous, ask immediately. Retrospective phase creation is a repair path, not the preferred path. If phase-shaped context is clear but the exact next phase file does not yet exist, live task shaping should still follow the implied current phase/stage provisionally.

---

## Phase Workspace Contract

### Identity grammar
- major phase: `NNN`
- subphase: `NNN-NN`
- `NNN` = top-level execution phase or grouped rollout stage
- `NNN-NN` = child execution slice inside major phase `NNN`
- hierarchy is expressed by the hyphen suffix, not prose alone
- zero-padded lexical ordering is preferred; major phases may be split, merged, skipped, repeated, or reordered when reality requires it; subphases are optional

### Required files
When phased planning is used:
- `phase/SUMMARY.md` is mandatory
- active executable files live under `phase/`
- valid active paths are `phase/phase-NNN-<phase-name>.md` and `phase/phase-NNN-NN-<subphase-name>.md`
- completed phase-detail history may live under `phase/done/` with the same filename grammar
- live phased execution files inside patch artifacts are **not allowed**

### Completed phase history
`phase/done/` is inactive-by-default completed phase history.

Required guidance:
- active execution scans start with `phase/SUMMARY.md` and active child phase files in `phase/`
- consult `phase/done/` only for history, audit, rollback, provenance, or trace reconstruction
- do not treat files in `phase/done/` as junk or deletion-authorized by their completed status alone
- `phase/done/` must not replace `phase/SUMMARY.md` or become the live phase-plan namespace

### Source-input synthesis
`/phase` is a live execution synthesis layer, not source of truth. It may consume design target-state input and governed patch review input when relevant. This is one-way: design/patch do not need to point back to phase, and phase usage does not move planning into patch or turn phase into design authority.

### Design-to-phase synthesis
When governed design is sufficiently clear for staged execution, `/phase` should actively derive or update the execution order from normalized design truth instead of waiting for a separate retrospective planning request.

Required guidance:
- split design target state into outcome-sized phases by dependency, risk, rollout boundary, and verification gate
- create or update `phase/SUMMARY.md` and the current child phase files from design truth when phase posture resolves to `create now` or `use existing`
- initialize or extend live tasks for the current active phase when non-trivial work begins
- continue phase-by-phase through active execution surfaces unless a real stop gate exists
- keep synthesis one-way: phase executes design; phase does not replace design as target-state authority
- ask only when design ambiguity, materially different rollout choices, missing access, destructive/high-impact action, or approval-sensitive scope changes the phase plan

### Patch linkage
When phased work uses a governed patch artifact:
- `phase/SUMMARY.md` must name the governing patch artifact(s) or explicitly state `none`
- each child phase using patch-derived work must include `Patch References`, or explicit `none`
- `none` is valid only when patch is truly not required, not when unresolved

---

## `SUMMARY.md` Responsibilities

`phase/SUMMARY.md` should keep the global execution picture:
- context, target state, risk, constraints, dependencies
- phase map/index and active child phase references
- completed `phase/done/` references only when history/audit/rollback/trace continuity requires them
- summary-level design/patch source inputs and governing patch references
- cross-phase handoffs and dependency rules
- TODO/changelog coordination
- end-to-end verification and rollback/containment behavior

When external docs/specs/provider references materially constrain execution, phase should point to normalized design truth so later slices do not depend on transient reading memory after compact or handoff.

---

## Child Phase Field Contract

Each executable phase file should define or map to:
- Summary File, Phase ID, Status
- Design references
- Patch references or explicit `none`
- Objective and why the phase exists
- implementation-relevant doc/spec-derived constraints when material
- Entry conditions/prerequisites
- Action checklist
- Out of scope
- Affected artifacts
- TODO and changelog coordination
- Verification
- Closeout summary: delivered work, feature/improvement, user/system impact, verification basis, and next phase state when relevant
- Exit criteria
- Risks/rollback notes
- Next possible phases

---

## Live Task-List Linkage Contract

When a phase is active and work is non-trivial, the built-in task list should mirror current phase execution slices.

Required guidance:
- inspect relevant `/phase` context before shaping/extending tasks; detached generic task wording is execution drift
- default tasks to the current active phase before future phases
- if the exact next phase file is absent but the current phase family/stage is clear, align tasks to that implied structure
- one phase may have many outcome-sized tasks
- prefer current phase ID in task subjects when useful
- extend the current task list for the same objective/phase family instead of recreating it
- task wording should follow the actual active session language/register; Thai-led or Thai/English mixed wording is acceptable when that matches the session; technical labels may remain technical when clearer
- use current phase, phase family, `phase/SUMMARY.md`, `TODO.md`, authored `Next possible phases`, and checked implementation state as bounded execution-discovery surfaces
- authored future-phase context may inform continuity and draft visibility but is not active execution until opened/selected/made active
- if the current phase is complete and the next phase is the implied active path, say the current phase is complete before continuing

---

## Verification, Closeout, and Rollback Contract

Each child phase should define phase-level verification, closeout summary expectations, and local rollback/containment notes. `phase/SUMMARY.md` must still define end-to-end verification and overall rollback/containment behavior. Patch artifacts must remain outside the live phase-plan namespace.

Phase-backed closeout should report what the phase delivered in practical terms, not only checked files, task IDs, or audit status. Required guidance:
- identify the delivered feature, capability, behavior, governance improvement, or verification gate
- explain the user/system impact or why the change matters
- keep verification basis explicit and evidence-strength aligned
- state next phase state when relevant: not started, draft/planned, selected, active, or none opened
- keep closeout concise and avoid forcing this report shape onto trivial non-phase work

---

## Verification Checklist

- [ ] `NNN` and `NNN-NN` are the active phase grammar
- [ ] startup governance establishes or asks about `/phase` before drift when phase is required
- [ ] staged/governed work is not left without explicit phase posture until late backfill
- [ ] `phase/SUMMARY.md` and valid active child phase paths are used
- [ ] completed phase history under `phase/done/` remains inactive by default and is not treated as junk/deletion authority
- [ ] sufficiently clear governed design for staged execution is synthesized into phase summary, current child phase files, and current-phase live tasks without replacing design authority
- [ ] patch-derived phase work shows explicit phase-to-patch linkage
- [ ] child phases include required source references and execution fields
- [ ] phase closeout reports delivered work, feature/improvement, impact, verification basis, and next phase state when relevant
- [ ] task creation aligns to active phase or clearly implied staged context
- [ ] authored future-phase context informs continuity without becoming active execution
- [ ] patch artifacts stay outside live phase workspace

---

## Integration

Related rules:
- [artifact-initiation-control.md](artifact-initiation-control.md) - startup phase posture
- [document-patch-control.md](document-patch-control.md) - patch governance boundary
- [project-documentation-standards.md](project-documentation-standards.md) - repository document model
- [todo-standards.md](todo-standards.md) - TODO and live task coordination
