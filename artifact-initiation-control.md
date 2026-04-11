# Artifact Initiation Control

> **Current Version:** 1.2
> **Design:** [design/artifact-initiation-control.design.md](design/artifact-initiation-control.design.md) v1.2
> **Session:** 11c4bd2f-216e-4779-81bf-26d34a4fcaeb
> **Full history:** [changelog/artifact-initiation-control.changelog.md](changelog/artifact-initiation-control.changelog.md)

---

## Rule Statement

**Core Principle: Resolve startup tracking and artifact posture before meaningful governed work drifts, so required design, changelog, TODO, phase, and patch artifacts are either reused, created now, asked about now, or explicitly marked not required, and live task tracking is initialized early when non-trivial work needs it.**

This rule owns the startup decision only. It does not replace the semantic owners of design, changelog, TODO, phase, or patch artifacts.

---

## Core Principles

### 1) Startup-Before-Drift Principle
Do not continue into meaningful governed work while required artifact posture is still implicit.

Required guidance:
- resolve startup artifact posture early
- allow lightweight exploration before the startup boundary
- stop drift once the work becomes meaningfully governed

### 2) Resolve-the-Set Principle
The assistant does not need to create every artifact every time, but it must resolve the required set.

Required guidance:
- for each relevant artifact, choose one explicit state:
  - use existing
  - create now
  - ask now
  - not required
- when the work is non-trivial and tracking is materially useful, initialize the built-in task list early as the live execution surface instead of leaving work state implicit
- when an active phase already exists for the work, treat live task-list initialization as expected rather than optional unless a narrow justified reason clearly blocks it
- do not silently skip artifacts or live tracking surfaces that appear required

### 3) Existing-Authority-First Principle
Reuse valid authority artifacts instead of creating duplicates.

Required guidance:
- prefer existing governed artifacts when they already fit the current scope
- avoid duplicate design/TODO/phase/patch scaffolding
- create new artifacts only when the existing set does not cover the work cleanly

### 4) Ask-Now Principle
If startup posture is unclear, ask immediately instead of drifting.

Required guidance:
- ask when scope, ownership, or workflow shape is still ambiguous
- ask before substantial planning or implementation continues
- do not delay the artifact decision until after the work is already structured implicitly

### 5) Backfill-Is-Repair Principle
Retrospective artifact creation is a repair path, not the preferred operating model.

Required guidance:
- prefer startup establishment over later backfill
- if backfill is needed, treat it as closing startup drift rather than as normal workflow

### 6) Trivial-Work Bypass Principle
Clearly trivial work may bypass heavy artifact setup.

Required guidance:
- keep the bypass narrow
- do not use “trivial” as an excuse for multi-step governed work
- if the task expands beyond triviality, re-run startup artifact resolution

---

## Trigger Model

Apply this rule strongly when one or more of these are present:

| Trigger | Typical Signal | Required Action |
|--------|-----------------|-----------------|
| new governed chain | “create a first-class rule”, “add a new policy chain” | resolve design + changelog + TODO immediately; evaluate phase/patch now |
| multi-file governed change | several governed docs or chains will change together | resolve TODO and likely phase before drift |
| staged work | sequencing, rollout, or rollback boundaries matter | establish `/phase` now or ask now |
| reviewable before/after work | explicit change-surface review matters | establish a patch artifact now or ask now, but only when an existing governed surface actually provides a stable before-state |
| explicit artifact-first request | user wants stronger governance startup behavior | apply the startup gate immediately |
| trivial isolated task | one obvious low-risk change | lightweight bypass allowed |

---

## Artifact Resolution Contract

### Meaningful-work boundary
Meaningful governed work begins when the assistant moves beyond lightweight exploration and starts doing one or more of these:
- target-state design planning
- multi-file governed implementation planning
- rollout or sequencing design
- TODO/workstream decomposition
- patch/review-surface planning
- substantive execution assuming artifact authority already exists

### Artifact requirement matrix

| Artifact | Require at startup when... |
|----------|-----------------------------|
| Design | target behavior, policy, contract, or architecture is new or materially changing |
| Changelog | a governed chain is being created or version-impacting behavior is changing |
| TODO | work is multi-step, tracked, persistent, or likely to span multiple execution slices |
| Live task list | work is non-trivial and the user would materially benefit from seeing pending / in_progress / completed state during active execution; phase-backed work strengthens this from preferred to expected |
| Phase | staged execution, gates, sequencing, rollback boundaries, or explicit user request make `/phase` materially useful |
| Patch | explicit before/after review packaging outside live phase planning is materially useful for an existing governed surface; greenfield startup / baseline formation normally defaults to `not required` unless the user explicitly requests patch packaging |

### Resolution order
Resolve startup artifact posture in this practical order:
1. design
2. changelog
3. TODO
4. phase
5. patch

This is startup-resolution order only.
It does not replace the later synchronization order owned elsewhere.

---

## Communication Contract

When startup artifact resolution is materially relevant, use this schema:

```text
meaningful_work_state: <lightweight_exploration | meaningful_governed_work>
artifact_posture:
- design: <use existing | create now | ask now | not required>
- changelog: <use existing | create now | ask now | not required>
- TODO: <use existing | create now | ask now | not required>
- live task list: <initialize now | not required>
- phase: <use existing | create now | ask now | not required>
- patch: <use existing | create now | ask now | not required>
reason: ...
what_must_happen_before_continuing:
- ...
```

Communication requirements:
- make the startup decision explicit before substantial work continues
- separate “not required” from “not yet decided”
- if asking is necessary, ask before work drifts into implicit structure

---

## Anti-Patterns to Avoid

| Anti-Pattern | Why It Hurts | Better Behavior |
|--------------|--------------|-----------------|
| work starts first and artifacts appear later | direction and rationale drift before authority exists | resolve startup artifact posture first |
| no artifacts are opened because the user did not list them manually | governance remains reactive | evaluate and resolve the required set proactively |
| non-trivial tracked work begins with no live task tracking | the user cannot see planned / active / completed state while the work is underway | initialize the built-in task list early when live tracking materially helps |
| all artifacts are forced every time | creates unnecessary ceremony | resolve only the required subset |
| create patch by default during greenfield startup or baseline formation | startup work is mislabeled as a review delta before a stable before-state exists | default patch to `not required` unless a real existing surface or explicit user request justifies it |
| hygiene blocks required startup artifacts | startup contract loses force | let startup control decide, then let hygiene police non-required files |
| artifact decision is deferred until after planning | the plan is already acting as if authority existed | ask or create immediately |

---

## Flexibility Boundary

Allowed flexibility:
- lightweight exploration before the meaningful-work boundary
- explicit not-required decisions when the task is genuinely small or narrow
- asking when the workflow shape is still ambiguous
- reusing existing authority artifacts instead of creating new ones

Not allowed:
- substantial governed work while required artifact posture is unresolved
- silent omission of clearly required startup artifacts
- treating retrospective artifact backfill as the normal preferred path
- using the trivial bypass for multi-step governed work

---

## Quality Metrics

| Metric | Target |
|--------|--------|
| Startup artifact posture resolved before meaningful drift | 100% |
| Required artifacts silently omitted at startup | 0 critical cases |
| Phase-backed live task tracking omitted at startup | 0 critical cases |
| Retrospective artifact backfill | Low |
| Trivial-work over-ceremony | Low |
| Existing-authority reuse | High |

---

## Integration

Related rules:
- [project-documentation-standards.md](project-documentation-standards.md) - repository role model and later synchronization order
- [phase-implementation.md](phase-implementation.md) - phase semantics after `/phase` is required
- [todo-standards.md](todo-standards.md) - TODO structure and update discipline
- [document-patch-control.md](document-patch-control.md) - patch semantics and before/after artifact behavior
- [strict-file-hygiene.md](strict-file-hygiene.md) - hygiene must defer for required startup artifacts

---

> **Full history:** [changelog/artifact-initiation-control.changelog.md](changelog/artifact-initiation-control.changelog.md)
