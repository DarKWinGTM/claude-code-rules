# Artifact Initiation Control
> **Current Version:** 1.7
> **Design:** [design/artifact-initiation-control.design.md](design/artifact-initiation-control.design.md) v1.7
> **Session:** d42465eb-30a7-4bc8-b9d6-03e52306e9a5
> **Full history:** [changelog/artifact-initiation-control.changelog.md](changelog/artifact-initiation-control.changelog.md)
---
## Rule Statement
**Core Principle: Resolve startup tracking and artifact posture before meaningful governed work drifts, so required design, changelog, TODO, phase, and patch artifacts are either reused, created now, asked about now, or explicitly marked not required, and live task tracking is initialized early when non-trivial work needs it.**
This rule owns startup decisions only. It does not replace the semantic owners of design, changelog, TODO, phase, or patch artifacts.
---
## Core Principles
### 1) Startup before drift
Do not continue into meaningful governed work while required artifact posture is still implicit.
Required guidance:
- resolve startup artifact posture early
- allow lightweight exploration before the startup boundary
- stop drift once work becomes meaningfully governed
### 2) Resolve the set
The assistant need not create every artifact every time, but it must resolve the required set.
For each relevant artifact choose one explicit state: `use existing`, `create now`, `ask now`, or `not required`.
Required guidance:
- initialize the built-in task list early when work is non-trivial and live visibility materially helps
- if governed design is already sufficiently clear and staged execution is warranted, resolve phase posture to `use existing` or `create now` instead of leaving phase planning implicit
- when phase posture resolves to `create now`, defer phase identity selection to `phase-implementation.md` so creation may mean updating a current phase, creating a subphase under an existing family, opening a new major phase, or asking when lineage is unresolved
- when an active phase already exists, live task-list initialization is expected unless a narrow justified reason blocks it
- once initialized for the active objective, reuse the live task-list surface unless true objective-boundary reset or explicit user reset applies
- do not silently skip artifacts or live tracking surfaces that appear required
- do not collapse `not required` into `safe to remove` for an existing/newly encountered file without stronger semantic authority and deletion authorization
### 3) Existing authority first
Reuse valid authority artifacts instead of creating duplicates.
Required guidance:
- prefer existing governed artifacts when they fit current scope
- avoid duplicate design/TODO/phase/patch scaffolding
- create new artifacts only when the existing set does not cover the work cleanly
- when a new file appears during governed work and its role is unclear, check governed surfaces/history before treating it as unnecessary
### 4) Ask now
If startup posture is unclear, ask immediately instead of drifting.
Required guidance:
- ask when scope, ownership, or workflow shape is ambiguous
- ask before substantial planning or implementation continues
- do not delay artifact decisions until the work is already implicitly structured
### 5) Backfill is repair
Retrospective artifact creation is a repair path, not the preferred operating model. Prefer startup establishment; if backfill is needed, treat it as closing startup drift.
### 6) Trivial-work bypass
Clearly trivial work may bypass heavy artifact setup.
Required guidance:
- keep the bypass narrow
- do not use “trivial” for multi-step governed work
- if the task expands beyond triviality, re-run startup artifact resolution
- do not use trivial/cleanup framing to bypass unresolved classification of a newly encountered file during governed work
---
## Trigger Model
| Trigger | Typical signal | Required action |
|---|---|---|
| new governed chain | create a first-class rule / policy chain | resolve design + changelog + TODO; evaluate phase/patch |
| multi-file governed change | several governed docs/chains change together | resolve TODO and likely phase before drift |
| staged work | sequencing, rollout, rollback boundaries | establish `/phase` now through the phase lineage gate or ask now |
| clear governed design for staged execution | target-state design already defines enough implementation order, dependency, risk, or verification gates | resolve phase posture to `use existing` or `create now`; if a phase file is created, select current phase vs subphase vs new major through `phase-implementation.md` |
| reviewable before/after work | explicit change-surface review | establish patch only when an existing governed surface provides stable before-state, or ask now |
| explicit artifact-first request | user wants stronger governance startup behavior | apply startup gate immediately |
| trivial isolated task | one obvious low-risk change | lightweight bypass allowed |
---
## Artifact Resolution Contract
Meaningful governed work begins when the assistant moves beyond lightweight exploration into target-state design planning, multi-file governed planning, rollout/sequencing design, TODO/workstream decomposition, patch/review-surface planning, or substantive execution assuming artifact authority already exists.
| Artifact | Require at startup when... |
|---|---|
| Design | target behavior, policy, contract, or architecture is new/materially changing |
| Changelog | governed chain is created or version-impacting behavior changes |
| TODO | work is multi-step, tracked, persistent, or likely to span slices |
| Live task list | non-trivial work benefits from live pending/in_progress/completed visibility; phase-backed work makes this expected |
| Phase | staged execution, gates, sequencing, rollback boundaries, or explicit request make `/phase` useful; phase identity selection remains owned by `phase-implementation.md` |
| Patch | before/after review packaging outside live phase is useful for an existing governed surface; greenfield/baseline formation defaults to `not required` unless requested |
Startup resolution order: design → changelog → TODO → phase → patch. This does not replace later synchronization order.
---
## Communication Contract
When startup artifact resolution materially matters, use this schema:
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
Required guidance:
- make the startup decision explicit before substantial work continues
- separate `not required` from `not yet decided`
- if asking is necessary, ask before implicit structure drifts
---
## Anti-Patterns
| Anti-pattern | Better behavior |
|---|---|
| work starts first and artifacts appear later | resolve startup artifact posture first |
| no artifacts opened because user did not list them | evaluate and resolve the required set proactively |
| non-trivial tracked work begins with no live task tracking | initialize built-in task list when live visibility helps |
| all artifacts forced every time | resolve only the required subset |
| patch by default during greenfield/baseline formation | default patch to `not required` unless existing before-state or explicit request justifies it |
| treating phase `create now` as automatic new-major creation | use `phase-implementation.md` to select current phase, existing-family subphase, new major, or ask-now lineage handling |
| hygiene blocks required startup artifacts | let startup control decide, then let hygiene police non-required files |
| artifact decision deferred until after planning | ask or create immediately |
---
## Flexibility Boundary
Allowed: lightweight exploration before the meaningful-work boundary, explicit not-required decisions for genuinely small/narrow tasks, asking when workflow shape is ambiguous, and reusing existing authority artifacts.
Not allowed: substantial governed work while required posture is unresolved, silent omission of clearly required artifacts, treating backfill as normal preferred flow, or using trivial bypass for multi-step governed work.
---
## Quality Metrics
| Metric | Target |
|---|---|
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
