# Phase, TODO, and Artifact Initiation
> **Current Version:** 1.33
> **Design:** [design/phase-todo-artifact.design.md](design/phase-todo-artifact.design.md) v1.33
> **Session:** 92c4d51e-eb02-4299-823a-1a6b8270f045
> **Full history:** [changelog/phase-todo-artifact.changelog.md](changelog/phase-todo-artifact.changelog.md)
> **Absorbed:** artifact-initiation-control v1.9, phase-implementation v2.35, todo-standards v2.28

---

## Rule Statement

**Core Principle: Resolve required design/changelog/TODO/phase/patch and live-task posture before governed work drifts; use phases only when staged execution adds value; keep `phase/SUMMARY.md` and `TODO.md` compact; and use the built-in task list as live state for non-trivial execution. Preserve strict phase lineage, selected-design semantic coverage, verification-before-closeout, and bounded helper-lane linkage without transferring source ownership.**

พูดง่าย ๆ: lock ก่อนว่า artifact ไหนเป็น owner, ใช้ phase เมื่อมี stage/gate จริง, `TODO.md` เป็น durable index, และ built-in tasks เป็น live board.

---

## Part A — Artifact Initiation and Startup

### 1) Startup posture

Before meaningful governed work, resolve each relevant surface as:
- `use existing`
- `create now`
- `ask now`
- `not required`

For the built-in task list use `initialize now` or `not required`.

Lightweight exploration may precede this boundary, but target-state planning, multi-file governed planning/execution, rollout sequencing, TODO decomposition, or patch review does not. Reuse fitting authority; create only when needed; ask when ownership, scope, workflow, or approval-sensitive meaning is ambiguous. Retrospective artifact creation is repair, not the normal path. If trivial work expands, rerun startup resolution. Never use `trivial`, cleanup, or `not required` as removal authority.

Default startup order:
1. design
2. changelog
3. TODO
4. phase
5. patch

Required triggers:
- **Design:** new/materially changed target behavior, policy, contract, or architecture
- **Changelog:** new governed chain or version-impacting behavior
- **TODO:** multi-step, persistent, tracked, or multi-slice work
- **Live task list:** active non-trivial work; expected for phase-backed execution
- **Phase:** meaningful stages, dependencies, verification/rollback gates, multi-system/owner coordination, or explicit request
- **Patch:** useful governed before/after review surface

Emergency exception: when delay materially increases immediate harm, `action-safety.md` may permit only the smallest safe reversible containment/diagnostic action before this sequence. Approval-sensitive work remains gated; startup/recovery synchronization resumes immediately afterward.

### 2) Repair and phase/patch boundaries

When God-artifact pressure cannot be repaired safely in place, resolve its owner immediately: design sharding → design; active same-chain version detail → `changelog/<chain>/v*.changelog.md`; inactive completed/reference history → `changelog/done/` when that governed role applies; TODO accumulation → TODO history/done; God Phase → phase lineage; God Patch → patch; non-trivial cross-surface repair → live tasks. No fallback owner or automatic resolution path exists for changelog content. Use existing authority when it fits, create when ownership is clear, and ask only for real ambiguity.

Clear staged work may be `use existing`, `create now`, or `ask now`; `create now` still passes the lineage gate and never implies a new major. Patch is non-default during greenfield/baseline work unless a real before/after review surface exists or the user requests it.

When posture affects continuation, state whether work is lightweight or governed, the relevant posture/reason, and any gate before proceeding. Keep rendering compact but do not hide unresolved required surfaces.

### 3) Governed-chain startup decision

When startup may append, split, or normalize design/changelog, apply `document-governance.md` and record only decision-changing state:

```text
docs_analysis:
- document_role: <design | changelog>
- namespace_and_subject: <scope + real chain subject>
- active_parent: <checked file + generic/semantic model + coexistence state>
- selected_chain_shape: <canonical shape>
- transition_basis: <bootstrap exit, shard opening, or append-vs-shard reason>
- action: <append | sibling shard | same-stem child | normalize | history/done>
- example_basis: <observed/extracted/selected/equivalence state when an example is used>
- integrity_updates: <map, backlinks, current/version alignment, orphan prevention>
```

Resolve ambiguity before deeper edits; do not restate chain doctrine or append merely because no shard exists.

---

## Part B — Phase Implementation

### 1) Phase workspace and applicability

Use phases for meaningful stages, rollout/migration, dependency sequencing, verification/rollback/containment gates, multi-system/owner coordination, or design/TODO/changelog movement. Do not force phases onto one obvious low-risk change, an ordinary checklist, or filler stages.

When phases are used:
- `phase/SUMMARY.md` is the mandatory compact live roadmap/index
- active execution files live under `phase/`
- forward-valid forms are `phase/phase-NNN-*.md`, `phase/phase-NNN-NN-*.md`, and `phase/phase-NNN-NN-NN-*.md`
- observed alphanumeric forms such as `phase-NNN-NNa-*.md` remain legacy-only unless later doctrine normalizes them
- daily movement may use `phase/history/YYYY-MM-DD*.md`; completed detail may use `phase/done/`
- live phase files never live inside patch artifacts

`phase/history/` is referenced movement history; `phase/done/` is inactive completed history. Active scans begin at compact `phase/SUMMARY.md` and active child files.

### 2) Identity grammar and strict lineage gate

Identity grammar:
- major: `NNN`
- subphase: `NNN-NN`
- nested child: `NNN-NN-NN`
- `NNN-NNa` is legacy-only; deeper hybrids such as `NNN-NN-NNb` are not forward-valid unless later doctrine normalizes them

Choose the smallest truthful identity through strict fall-through, not a menu:
1. **Update current active phase first** when checked summary, active child, and phase-linked tasks still share the execution slice, goal, output, gate, dependency path, or rollback boundary.
2. **Create an existing-family child second** when current phase cannot absorb the work but the same bounded gate/rollout family continues. A major parent opens `NNN-NN`; a subphase opens `NNN-NN-NN`.
3. **Create a new major third** only after evidence rules out current and child fit and the work forms a distinct top-level rollout family, capability/output, verification/release gate, or rollback boundary. Record why current and child failed.
4. Ask or record the governing basis when several lineages remain plausible.

A new file, completed current phase, task continuation, fresh concern wording, or milestone closeout is not itself a lineage break. Child fit requires shared goal/output/gate meaning, immediate parent lineage, and bounded rollout continuity—not broad topic similarity.

A God Phase carries independently completable primary goals, unrelated outputs/gates/rollback boundaries, or mixed roadmap/changelog/TODO/patch/execution roles. Repair through the same lineage gate, update summary/tasks when navigation changes, preserve legacy grammar, and block closeout until touched pressure is repaired or visibly planned.

### 3) Design-to-phase synthesis and lanes

`/phase` consumes normalized design truth and governed patch review one-way; it is not target-state authority. Derive outcome-sized phases from design by dependency, risk, rollout boundary, output, and verification gate. Update summary, active children, and phase-linked live tasks when posture is `create now` or `use existing`, and continue phase-by-phase unless a real stop gate exists.

Ask only when design ambiguity, materially different rollout choices, missing access, destructive/high-impact action, or approval-sensitive scope changes the route.

For broad phase-backed objectives, define bounded implementation, verification, governance/release-sync, evidence-audit, or research lanes by goal, output, and gate. Lane changes still pass lineage; do not scaffold trivial/tightly sequential work. `worker-routing-and-context.md` may attach bounded helper support, while phase retains the staged map and source ownership remains with the leader.

### 4) Selected design-slice semantic coverage

Before a selected design slice is called implemented or complete:
- identify the selected section/shard/target subset
- extract material behavior, invariant, failure mode, required dependency/state, acceptance/verification clue, and explicit out-of-scope boundary
- keep enough coverage in phase/task surfaces to prevent silent loss without copying the whole design
- track implementation coverage as `not started` or `implemented`; `implemented` is intermediate while material verification remains
- assign terminal disposition before closeout: `verified`, `deferred`, `blocked`, `not applicable`, or `out of scope`
- keep deferred/blocked/not-applicable/out-of-scope status visible

A headline output does not close uncovered durability, recovery, retry, idempotency, rollback, or other selected semantics. Phase tracks execution coverage; it must not become a second design authority.

### 5) Roadmap, goal, and patch linkage

When evidence supports forecasting, `phase/SUMMARY.md` should carry a bounded roadmap/matrix with goal, output, gate, dependencies, deliverables, and status: `active`, `selected`, `implied-unblocked`, `proposal`, `blocked`, `needs-approval`, or `none opened`. Roadmap context is not automatic execution authority. Before ending closeout, inspect checked roadmap and goal surfaces; when meaningful successor work exists, name it with why/output/gate.

Design, active phase, built-in tasks, TODO, and checked implementation state supply governed goal evidence; release/review surfaces matter only when they affect completion. Keep selected goal, phase/task linkage, and verification gate visible when route notes, `Plan reference:`, or `/plan` exists. Route completion never replaces the goal gate; goal construction belongs to `goal-authoring-and-route-support.md`.

When patch is used, `phase/SUMMARY.md` names governing patch artifact(s) or explicit `none`, and each patch-derived child has `Patch References` or `none`. `none` is valid only when patch is genuinely unnecessary.

### 6) Phase responsibility and closeout

`phase/SUMMARY.md` owns the compact global execution picture: context, target, risk/constraints, dependencies, phase/roadmap map, active child and history/done pointers, lineage, design/patch references, handoffs, TODO/changelog coordination, end-to-end verification, next-goal basis, and overall rollback. Its normalized compact form must preserve current status, active-or-latest-completed phase visibility, verification focus, rollback/containment state, and explicit history/done references. Push detailed execution into children/history/done.

Each active child defines or maps to:
- summary/phase ID/status, design references, patch references or `none`
- objective, why, expected output, completion/verification gate, entry conditions, and out-of-scope
- selected design slice/semantic status and lane ordering when applicable
- affected artifacts, TODO/changelog coordination, checklist
- Development Verification / TestKit Coverage when coding verification affects exit
- verification/exit/closeout, risks/rollback, and meaningful next possibilities

Child phases own local verification and rollback/containment; summary owns end-to-end verification and overall rollback. Closeout reports delivered capability/behavior/governance/verification gate, user/system impact, evidence-aligned verification, explicit semantic-item dispositions, relevant next-phase state, and a supported successor recommendation when one exists—not just files/tasks/audit state.

---

## Part C — TODO and Live Tasks

### 1) Durable versus live state

`TODO.md` is the compact durable current execution index, not version authority or the primary live board. It must not absorb live execution, detailed history, phase roadmap, release notes, or verification logs; version detail belongs in changelog and staged-execution detail in phase. Keep release/active-wave context, compact completed highlights, still-visible active/deferred items, and reachable history/done links; roll accumulated history under `document-integrity.md` without losing current/deferred visibility.

The built-in task list is live execution state for non-trivial work: planned, in-progress, and completed slices. It is not a governed repository document and does not replace TODO durability.

Use live tasks by default for work with 3+ steps, multiple files/stages, continuation across slices, active phases, distinct lanes, or separate implementation/verification outcomes. Do not force them onto trivial isolated lookup/fix work.

### 2) Phase-linked task shaping

For phase-backed work:
- inspect current `/phase` first; execute current phase before later phases
- keep lineage and phase context visible in task subject/description
- shape outcome-sized tasks around output and gate, not individual commands
- split implementation, verification, and governance/release-sync only when combining them hides gates/ownership
- mark `in_progress` when work begins and `completed` immediately when the slice is actually done
- preserve a verification task while material checks remain
- discover next work from the task list, then active phase, summary, TODO, and checked implementation

When a selected non-trivial goal/plan enters execution, materialize bounded tasks before deep continuation. Authoring alone does not trigger execution. Keep goal/plan linkage; ask one substantive question only when objective, scope, gate, access, or approval is insufficient. Worker helper topology belongs to `worker-routing-and-context.md`.

Progress rendering belongs to `explanation-and-presentation.md`; do not turn task/phase state into a dashboard or stop ceremony.

### 3) Tracking failure, simplicity, and sync

If live task creation/update fails, determine whether tracking is material. Repair task title/scope/phase linkage before claiming non-trivial phase-backed work synchronized. A bounded research/review lane may continue when tracking is non-material, but report the limit; never use task friction to skip required durable sync. Restore material tracking before broad continuation.

Pending sections contain only pending items. Completed work belongs in Completed/History/referenced `todo/done/`. Avoid counters, priority grids, per-task timestamps, deadlines, telemetry blocks, and one-task-per-command overhead.

When governance changes governed artifacts, TODO sync order remains:
1. design
2. runtime rule
3. changelog
4. TODO, including rollover references when triggered

Later sync does not weaken early startup or live-task requirements.

---

## Trigger Model

| Trigger | Required handling |
|---|---|
| new chain or multi-file governed change | resolve design/changelog/TODO, evaluate phase/patch, initialize live tasks when non-trivial |
| staged/rollout/verification gates | establish phase through strict lineage |
| clear design for staged execution | synthesize phases and current-phase tasks from design truth |
| broad phase objective | define outcome-sized lanes/tasks before deep work |
| selected design semantics exceed headline output | extract obligations and explicit implementation/terminal states |
| active phase/lane | expose phase context and continue current-phase-first |
| selected non-trivial goal/plan executes | materialize bounded tasks with distinct gates when needed |
| governance/release-sync inside phase | separate its lane/task when mixing obscures ownership |
| oversized TODO/summary or God Phase/TODO | invoke preservation-first rollover/repair while keeping active navigation |
| implementation done, verification material | keep verification visible; do not close early |
| objective complete with meaningful successor | report supported next phase/wave/goal with why/output/gate |

## Anti-Patterns

Avoid unresolved startup posture; `create now` or task continuation treated as automatic new-major authority; `not required`/cleanup as deletion authority; filler phases/lanes; invalid forward phase grammar; God Phase/TODO bodies; history replacing active entrypoints; live tasks replacing durable state; authoring treated as execution; hidden goal/phase/gate context; closeout before semantic disposition or verification; and file/task-only closeout without delivery, impact, and evidence.

## Integration

- [document-governance.md](document-governance.md) / [document-integrity.md](document-integrity.md) — roles, sync, preservation, rollover
- [worker-routing-and-context.md](worker-routing-and-context.md) / [safe-io.md](safe-io.md) — helper topology and bounded intake
- [coding-discipline.md](coding-discipline.md) — coding verification/TestKit
- [execution-and-goal-frame.md](execution-and-goal-frame.md) / [goal-authoring-and-route-support.md](goal-authoring-and-route-support.md) — continuation, goals, route support
