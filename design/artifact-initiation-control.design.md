# Artifact Initiation Control

## 0) Document Control

> **Parent Scope:** RULES System Design
> **Current Version:** 1.0
> **Session:** dd0bf4af-a66b-4b07-bb9d-a90a0e57b54e (2026-03-28)

---

## 1) Goal

Define one first-class startup-governance rule that resolves artifact posture before meaningful governed work drifts.

The target behavior is:
- artifact posture is resolved early
- the assistant does not drift into non-trivial governed work while required artifacts remain implicit
- required startup artifacts are either reused, created now, asked about now, or explicitly marked not required
- trivial work keeps a lightweight bypass

---

## 2) Problem Statement

The repository already defines artifact roles well, but startup behavior remains fragmented.

Observed failure modes:
- design, changelog, TODO, phase, or patch are often created late instead of being established at startup
- the assistant may start meaningful governed work before deciding which artifacts are required
- `strict-file-hygiene` suppresses proactive document creation unless a stronger startup contract exists
- governance artifacts become retrospective backfill instead of direction-setting scaffolding

The repository needs one semantic owner that decides startup artifact posture before work drifts.

---

## 3) Scope

This chain applies to startup behavior for governed work involving these candidate artifact types:
- `design/*.design.md`
- `changelog/*.changelog.md`
- `TODO.md`
- `phase/SUMMARY.md` and executable phase files under `phase/`
- `patch/<context>.patch.md` or root `<context>.patch.md`

This chain does not replace the semantic owners of those artifact types. It owns only the timing and posture-resolution behavior at the start of work.

---

## 4) Core Contract

### 4.1 Startup artifact-resolution rule
Before meaningful governed work continues, the assistant must resolve startup posture for each relevant artifact as one of:
- use existing
- create now
- ask now
- not required

The important requirement is not “create everything.”
The requirement is “leave nothing required unresolved.”

### 4.2 Meaningful-work boundary
Meaningful governed work begins when the assistant moves beyond lightweight exploration and starts doing one or more of these:
- target-state design planning
- multi-file governed implementation planning
- rollout or sequencing design
- TODO/workstream decomposition
- patch/review-surface planning
- substantive execution assuming artifact authority already exists

Lightweight exploration to determine whether artifacts are needed is allowed before the boundary.
Substantial work after the boundary is not.

### 4.3 Required-artifact resolution order
The assistant should evaluate startup artifact posture in this practical order:
1. design
2. changelog
3. TODO
4. phase
5. patch

This is a startup-resolution order only.
It does not replace the later synchronization order owned by `project-documentation-standards`.

### 4.4 Existing-authority reuse
If a valid governing artifact already exists for the current scope, reuse it rather than creating a duplicate.

### 4.5 Ask-now rule
If an artifact appears required but scope, authority, or user intent is still unclear, ask immediately instead of drifting into detailed work.

### 4.6 Backfill-is-repair rule
Retrospective artifact creation is a repair path, not the preferred path.
The preferred path is to resolve startup artifacts before drift.

---

## 5) Trigger Model

### 5.1 High-strength triggers
Apply this chain strongly when one or more are true:
- a new first-class rule chain is being created
- multiple governed chains will be touched
- staged rollout, sequencing, or rollback boundaries matter
- work spans design/runtime/changelog/TODO together
- before/after review packaging may be useful
- the user explicitly requests stronger artifact-first behavior

### 5.2 Artifact-specific triggers

| Artifact | Require at startup when... |
|----------|-----------------------------|
| Design | target behavior, policy, contract, or architecture is new or materially changing |
| Changelog | a governed chain is being created or version-impacting behavior is changing |
| TODO | work is multi-step, tracked, persistent, or likely to span multiple execution slices |
| Phase | staged execution, gates, sequencing, rollback boundaries, or explicit user request make `/phase` materially useful |
| Patch | explicit before/after review packaging outside live phase planning is materially useful |

### 5.3 Low-strength / bypass triggers
A lightweight bypass is allowed when:
- the task is trivial and isolated
- the work is a single obvious low-risk fix
- the interaction is exploratory only
- no governed change has started yet

---

## 6) Establish-Now vs Ask-Now Contract

### 6.1 Create now
Create the required artifact immediately when:
- the need is clear from checked scope
- the artifact role is unambiguous
- no higher-priority user-authority issue blocks creation
- creation follows the repository’s governed model cleanly

### 6.2 Ask now
Ask immediately when:
- multiple plausible scopes exist
- a patch artifact may be useful but is not clearly required
- the user may reasonably want to choose between light and heavy governance paths
- artifact creation would materially change the workflow shape and intent is not yet explicit

### 6.3 Not required
Mark an artifact not required only when that conclusion is actually justified by the current task shape.

---

## 7) Communication Contract

When this rule is materially relevant, the startup snapshot should make these fields visible:
- **Meaningful work state** - whether the task has crossed the startup boundary
- **Artifact posture** - existing / create now / ask now / not required
- **Why this artifact is or is not needed**
- **What must happen before substantive work continues**

Equivalent headings are acceptable if the meaning remains explicit.

---

## 8) Anti-Patterns to Avoid

| Anti-Pattern | Why It Hurts | Better Behavior |
|--------------|--------------|-----------------|
| start work first, backfill artifacts later | direction and rationale drift before authority exists | resolve startup artifact posture first |
| create no artifacts because the user did not explicitly list them | meaningful work loses structure and traceability | evaluate required artifact set proactively |
| force every artifact every time | creates unnecessary ceremony | resolve only the required subset |
| let hygiene rules suppress required startup artifacts | makes governance reactive and late | let startup artifact control decide, then apply hygiene to non-required files |
| ask too late | work already drifts before the user sees the artifact decision | ask immediately when startup posture is unclear |

---

## 9) Quality Metrics

| Metric | Target |
|--------|--------|
| Startup artifact posture resolved before meaningful drift | 100% |
| Required artifacts silently omitted at startup | 0 critical cases |
| Retrospective governance backfill | Low |
| Trivial-work over-ceremony | Low |
| Existing-authority reuse | High |

---

## 10) Integration

| Rule | Relationship |
|------|-------------|
| [project-documentation-standards.md](../project-documentation-standards.md) | Repository-level document-role model and later synchronization order |
| [phase-implementation.md](../phase-implementation.md) | Phase semantics once `/phase` is required |
| [todo-standards.md](../todo-standards.md) | TODO structure and update discipline |
| [document-patch-control.md](../document-patch-control.md) | Patch semantics and before/after review artifact behavior |
| [strict-file-hygiene.md](../strict-file-hygiene.md) | Hygiene boundary that must defer for required startup artifacts |

---

> Full history: [../changelog/artifact-initiation-control.changelog.md](../changelog/artifact-initiation-control.changelog.md)
