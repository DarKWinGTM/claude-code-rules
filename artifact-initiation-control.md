# Artifact Initiation Control
> **Current Version:** 1.7
> **Design:** [design/artifact-initiation-control.design.md](design/artifact-initiation-control.design.md) v1.7
> **Session:** d42465eb-30a7-4bc8-b9d6-03e52306e9a5
> **Full history:** [changelog/artifact-initiation-control.changelog.md](changelog/artifact-initiation-control.changelog.md)
---
## Rule Statement
**Core Principle: Resolve startup tracking and artifact posture before meaningful governed work drifts, so required design, changelog, TODO, phase, and patch artifacts are reused, created now, asked about now, or explicitly marked not required, and live task tracking starts early when non-trivial work needs it.**
This rule owns startup decisions only. Semantic ownership stays with the design, changelog, TODO, phase, and patch rules.
---
## Startup Contract
Before meaningful governed work continues, resolve every relevant startup surface with one explicit state: `use existing`, `create now`, `ask now`, or `not required`. For the built-in task list, use `initialize now` or `not required`.

Guidance:
- allow lightweight exploration before the startup boundary, but stop drift once work becomes meaningfully governed
- reuse valid existing authority artifacts; create new ones only when the current set does not cleanly cover the work
- ask immediately when scope, ownership, workflow shape, or artifact need is ambiguous
- treat retrospective artifact creation as repair, not the preferred path
- keep trivial-work bypass narrow; if an isolated task expands into multi-step governed work, rerun startup resolution
- initialize the built-in task list when non-trivial work benefits from live pending/in_progress/completed visibility; active phase work makes this expected unless a narrow reason blocks it
- once initialized for the active objective, reuse the live task-list surface unless true objective closure or explicit user reset applies
- do not silently skip required artifacts or live tracking surfaces
- do not use `trivial`, cleanup, or `not required` wording to classify an existing/newly encountered file as removable or `safe to remove`; file meaning and deletion authority require stronger owners
---
## Phase and Patch Startup Rules
Phase:
- if staged execution, gates, rollback boundaries, or sufficiently clear governed design make `/phase` useful, resolve phase posture now as `use existing`, `create now`, or `ask now`
- `create now` does not mean automatic new-major creation; `phase-implementation.md` decides current phase update, existing-family subphase, new major, or ask-now lineage handling

Patch:
- establish patch only when before/after review packaging is useful for an existing governed surface or the user requests it
- greenfield/baseline formation defaults to `not required` unless an existing before-state or explicit request justifies patch governance
---
## Trigger Model
| Trigger | Startup action |
|---|---|
| new governed chain | resolve design + changelog + TODO; evaluate phase/patch |
| multi-file governed change | resolve TODO and likely phase before drift |
| staged work or rollout gates | establish `/phase` through the lineage gate, or ask now |
| clear governed design for staged execution | use/create phase surfaces from design truth; phase identity stays with `phase-implementation.md` |
| reviewable before/after change | establish patch only when patch criteria are met, or ask now |
| explicit artifact-first request | apply the startup gate immediately |
| trivial isolated task | bypass allowed only while it remains obvious, low-risk, and narrow |
---
## Artifact Resolution Contract
Meaningful governed work begins when the assistant moves beyond lightweight exploration into target-state design planning, multi-file governed planning, rollout/sequencing design, TODO/workstream decomposition, patch/review-surface planning, or substantive execution that assumes artifact authority already exists.

| Artifact | Require at startup when... |
|---|---|
| Design | target behavior, policy, contract, or architecture is new/materially changing |
| Changelog | a governed chain is created or version-impacting behavior changes |
| TODO | work is multi-step, tracked, persistent, or likely to span slices |
| Live task list | non-trivial active work benefits from live visibility; phase-backed work makes this expected |
| Phase | staged execution, gates, sequencing, rollback boundaries, or explicit request make `/phase` useful |
| Patch | governed before/after review packaging is useful and patch criteria are met |

Startup resolution order: design → changelog → TODO → phase → patch. Later synchronization order remains owned by the relevant document rules.
---
## Communication Contract
When startup artifact resolution materially matters, use this compact schema:
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
State the decision before substantial work continues, keep `not required` separate from `not yet decided`, and ask before implicit structure drifts.
---
## Anti-Patterns
| Anti-pattern | Better behavior |
|---|---|
| work starts first and artifacts appear later | resolve startup posture first |
| no artifacts opened because user did not list them | proactively evaluate the required set |
| non-trivial tracked work begins with no live task tracking | initialize the built-in task list when live visibility helps |
| all artifacts forced every time | resolve only the required subset |
| patch by default during greenfield/baseline formation | default patch to `not required` unless justified |
| phase `create now` treated as new-major creation | use `phase-implementation.md` lineage handling |
| hygiene blocks required startup artifacts | let startup control decide, then hygiene governs non-required files |
---
## Flexibility Boundary
Allowed: lightweight exploration, explicit not-required decisions for narrow work, asking when workflow shape is ambiguous, and reusing existing authority artifacts.
Not allowed: substantial governed work while required posture is unresolved, silent omission of required artifacts, normalizing backfill as preferred flow, or using trivial/cleanup framing to bypass governed file classification.
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
