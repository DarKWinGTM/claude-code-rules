# Phase, TODO, and Artifact Initiation
> **Current Version:** 1.31
> **Design:** [design/phase-todo-artifact.design.md](design/phase-todo-artifact.design.md) v1.31
> **Session:** 92c4d51e-eb02-4299-823a-1a6b8270f045
> **Full history:** [changelog/phase-todo-artifact.changelog.md](changelog/phase-todo-artifact.changelog.md)
> **Absorbed:** artifact-initiation-control v1.9, phase-implementation v2.35, todo-standards v2.28

---

## Rule Statement

**Core Principle: Resolve artifact posture and governed documentation chain naming/shape analysis before work drifts, use phases only when staged execution adds real value, resolve planning depth for plain governed goal requests, keep `phase/SUMMARY.md` and `TODO.md` as compact active entrypoints, and treat the built-in task list as the live execution surface for non-trivial phase-backed work, including lane-oriented continuation when broad worker-fit execution needs explicit structure.**

This rule unifies startup artifact initiation, live phase execution semantics, and durable-vs-live task tracking. It keeps staged work aligned to real goals, outputs, and gates without letting TODO, phase, patch, or startup posture drift into retrospective cleanup.

พูดง่าย ๆ: ก่อนงาน governed จะไหล ต้องล็อกก่อนว่า design / changelog / TODO / phase / patch ใช้อะไร; ถ้างานควรแบ่ง phase ก็ใช้ให้ชัด; `TODO.md` เป็น durable index, ส่วน built-in task list คือ live board ของงานจริง.

---

## Part A — Artifact Initiation and Startup Posture

### 1) Resolve posture before drift
Before meaningful governed work continues, resolve every relevant startup surface with one explicit state:
- `use existing`
- `create now`
- `ask now`
- `not required`

For the built-in task list, use `initialize now` or `not required`.

Required guidance:
- allow lightweight exploration before the startup boundary, but stop drift once work becomes meaningfully governed
- reuse valid existing authority artifacts; create new ones only when the current set does not cleanly cover the work
- ask immediately when scope, ownership, workflow shape, or artifact need is ambiguous
- treat retrospective artifact creation as repair, not the preferred flow
- keep trivial-work bypass narrow; if isolated work expands into multi-step governed work, rerun startup resolution
- do not silently skip required artifacts or live tracking surfaces
- do not use `trivial`, cleanup, or `not required` wording as file-removal authority

### 2) Startup resolution model
Meaningful governed work begins when the assistant moves beyond lightweight exploration into target-state planning, multi-file governed planning, rollout/sequencing design, TODO/workstream decomposition, patch/review planning, or substantive execution that assumes artifact authority already exists.

Default startup order:
1. design
2. changelog
3. TODO
4. phase
5. patch

Required-at-startup triggers:
- **Design:** target behavior, policy, contract, or architecture is new/materially changing
- **Changelog:** a governed chain is created or version-impacting behavior changes
- **TODO:** work is multi-step, tracked, persistent, or likely to span slices
- **Live task list:** non-trivial active work benefits from live visibility; phase-backed work makes this expected
- **Phase:** staged execution, gates, sequencing, rollback boundaries, or explicit request make `/phase` useful
- **Patch:** governed before/after review packaging is useful and patch criteria are met

### 3) God-artifact repair posture at startup
When detected God-artifact pressure cannot be repaired safely in place, resolve the required governed repair surface immediately.
- use existing artifacts when they already fit
- create now when the owner route is clear
- ask now only when owner, scope, phase lineage, patch need, or approval-sensitive meaning is ambiguous

Typical owner routes:
- design sharding or design split → design posture
- bulky version history → changelog or changelog/done posture
- accumulated TODO movement → TODO history/done posture
- God Phase pressure → phase lineage posture
- God Patch pressure → patch posture
- cross-surface repair → live task tracking when non-trivial

`not required` for a surface never means the artifact is safe to ignore or delete.

### 4) Phase and patch startup boundary
- resolve clear staged work as `use existing`, `create now`, or `ask now`; `create now` still passes the canonical lineage gate in Part B and never implies a new major
- patch is non-default during greenfield/baseline formation unless a real before/after review surface exists or the user explicitly asks for it

### 5) Startup communication contract
When posture materially affects continuation, state whether work is lightweight exploration or meaningful governed work, each relevant surface's exact posture, the reason, and what must happen before continuing. Rendering may stay compact; do not omit unresolved required surfaces.

### 5.1) Documentation-chain startup decision
When startup work may append, split, or normalize a design/changelog chain, apply the canonical model in `document-governance.md` and record only decision-changing state:

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

Resolve ambiguity before deeper edits; do not restate chain-selection doctrine or append by default merely because no shard exists.

---

## Part B — Phase Implementation

### 1) When phases are appropriate
Use phased planning only when staged execution improves clarity.
Good fits:
- meaningful stages
- rollout / migration / verification gates
- rollback or containment boundaries
- dependency-driven sequencing
- multi-system or multi-owner coordination
- a need to show how design / TODO / changelog move together

Do not force phases for a single obvious low-risk change, a normal checklist, or filler stages with no execution meaning.

### 2) Phase workspace contract
When phased planning is used:
- `phase/SUMMARY.md` is mandatory as the compact live roadmap/index
- active executable files live under `phase/`
- active phase files use `phase/phase-NNN-*.md`, `phase/phase-NNN-NN-*.md`, or `phase/phase-NNN-NN-NN-*.md`
- existing alphanumeric forms such as `phase-NNN-NNa-*.md` remain legacy-only unless a later doctrine explicitly normalizes them
- daily movement may live under `phase/history/YYYY-MM-DD*.md`
- completed phase detail may live under `phase/done/`
- live phased execution files are not allowed inside patch artifacts

`phase/history/` is referenced movement history; `phase/done/` is inactive completed history. Active scans start from compact `phase/SUMMARY.md` and active child files.

### 3) Identity grammar and lineage gate
Identity grammar:
- major phase: `NNN`
- subphase: `NNN-NN`
- nested child phase: `NNN-NN-NN`
- existing alphanumeric forms such as `NNN-NNa` remain legacy-only observed lineage, not forward-valid grammar
- deeper hybrid forms such as `NNN-NN-NNb` are not forward-valid grammar unless a later doctrine explicitly normalizes them

Before opening a new major phase, choose the smallest truthful identity.

Required identity decision order is strict fall-through, not a menu:
- update the current active phase first when checked `phase/SUMMARY.md`, the current active child phase, and visible phase-linked live tasks show that the work still fits the same execution slice, goal, expected output, completion gate, dependency path, or rollback boundary
- create an existing-family child phase second when the current phase cannot truthfully absorb the work, but the work still continues the same bounded execution gate or rollout family inside the existing lineage
- if the current active phase is a major phase, the next truthful child form is `NNN-NN`
- if the current active phase is a subphase and the work still belongs inside that same bounded gate family, the next truthful child form is `NNN-NN-NN`
- create a new major phase third only after checked evidence rules out both current-phase update and existing-family child fit, and the work forms a distinct top-level rollout family, capability boundary, output, verification gate, release boundary, or rollback boundary
- when a new major phase is selected, record visible why-not-current and why-not-child-phase basis rather than leaving the negative checks implicit
- ask or record the governing basis when multiple families plausibly fit and checked evidence does not settle lineage

A new file need, completed current phase, task-list continuation, fresh concern wording, or milestone closeout is not by itself a lineage break.

Child-phase fit depends on real shared goal/output/gate meaning, immediate parent lineage, and bounded rollout continuity, not only broad product area or historical proximity.

### 4) God Phase repair
A God Phase is a phase file that tries to execute several independent phases at once.
Signals include:
- multiple primary goals that can complete independently
- multiple expected outputs that do not share one bounded gate
- unrelated verification gates or rollback boundaries
- roadmap/changelog/TODO/patch/execution all mixed in one active body

Repair posture:
- apply the canonical lineage gate: restructure the current phase when one bounded goal/output/gate remains, otherwise choose the smallest truthful child or major result
- keep existing alphanumeric child forms legacy-only unless later doctrine selects normalization
- update `phase/SUMMARY.md` and visible phase-linked tasks when the split changes execution/navigation
- block closeout while touched-scope God Phase pressure remains unrepaired or unplanned

### 5) Design-to-phase synthesis
`/phase` is a live execution synthesis layer, not source-of-truth authority.
- phase consumes normalized design truth and governed patch review input one-way
- when design is clear enough for staged execution, derive or update phase order from design truth instead of waiting for retrospective planning
- split target state into outcome-sized phases by dependency, risk, rollout boundary, expected output, and verification gate
- create/update `phase/SUMMARY.md`, current child files, and current-phase live tasks when posture resolves to `create now` or `use existing`
- continue phase-by-phase unless a real stop gate exists

Ask only when design ambiguity, materially different rollout choices, missing access, destructive/high-impact action, or approval-sensitive scope would change the plan.

### 5.1) Phase-backed lane structuring
When a phase-backed objective is broad enough to contain distinct execution shapes, structure it into lanes before deep work drifts.
- lanes are bounded execution slices such as implementation, verification, governance/release-sync, evidence audit, or bounded research
- each lane should map to a clear goal, expected output, and completion gate rather than acting as a command bucket
- lane changes pass the canonical lineage gate and must not open a major phase by momentum
- worker routing decides whether a lane becomes a standalone subagent or stays direct; phase only keeps the staged execution map visible
- do not create lane scaffolding for trivial, tightly sequential, or one-step work

### 5.2) Design-slice semantic coverage
When a governed design section, slice, shard, or target-state subset is selected for implementation, phase synthesis must account for the selected semantic slice before the slice can be called implemented or complete.
- identify the selected design slice explicitly enough that later execution, review, and closeout can tell which target-state subset is being carried
- extract implementation-relevant semantic items from that slice when materially present: behavior, invariant, failure mode, required dependency/state requirement, acceptance/verification clue, and explicit out-of-scope boundary
- phase/task surfaces may stay compact and do not need to copy the whole design body, but the selected semantic coverage must stay visible enough to prevent silent loss
- each selected semantic item must reach an explicit state before closeout: `implemented`, `verified`, `deferred`, `blocked`, `not applicable`, or `out of scope`
- a visible headline output is not enough when selected invariants, durability, recovery, retry, idempotency, rollback, or similar semantics remain uncovered
- if a selected semantic item is deferred, blocked, not applicable, or out of scope, keep that status visible in phase/task/verification surfaces rather than silently dropping it from execution
- phase consumes design truth as execution coverage; it must not become a second design-authority summary of the whole source material

### 6) Roadmap and next-phase synthesis
When a governed objective has enough evidence to forecast beyond the current slice, `phase/SUMMARY.md` should carry a bounded roadmap or phase matrix.
Roadmap entries should expose:
- goal
- expected output
- completion gate
- dependencies
- deliverables
- status such as `active`, `selected`, `implied-unblocked`, `proposal`, `blocked`, `needs-approval`, or `none opened`

Roadmap entries are planning context, not automatic execution authority.
After a phase-backed objective closes, inspect checked roadmap and goal surfaces before ending closeout. If future work is meaningful, name the best-supported next phase/wave/goal with why, expected output, and gate.

### 6.1) Goal linkage from phase/TODO surfaces
Design, active phase, built-in tasks, `TODO.md`, and checked implementation state supply execution evidence for governed goal shaping; release/review surfaces matter only when they affect completion. Keep the selected goal, phase/task linkage, and verification gate visible when route notes, a plan reference, or `/plan` exists. Route completion must not replace the goal gate. Goal construction and route-support rules defer to `goal-authoring-and-route-support.md`.

### 7) Patch linkage inside phase
When phased work uses a governed patch artifact:
- `phase/SUMMARY.md` must name governing patch artifact(s) or explicitly state `none`
- each child phase using patch-derived work must include `Patch References` or explicit `none`
- `none` is valid only when patch is truly not required, not when unresolved

### 8) Phase file responsibilities
`phase/SUMMARY.md` keeps the compact global execution picture: context, target state, risk, constraints, dependencies, roadmap/phase matrix, phase map, active child references, lineage context, history/done pointers, design/patch references, handoffs, TODO/changelog coordination, end-to-end verification, next-goal basis, and rollback behavior.

In normalized compact-entrypoint form it should keep current status, active-or-latest-completed phase visibility, verification focus, rollback/containment state, and explicit history/done references while pushing bulky execution detail into child phase files or `history/` / `done/` shards.

Each active child phase should define or map to:
- Summary File / Phase ID / Status
- design references
- patch references or `none`
- objective and why the phase exists
- expected output
- completion gate / verification gate
- selected design slice and semantic coverage status when the phase executes a bounded design subset with materially distinct obligations
- lane map or lane ordering when the phase contains distinct implementation / verification / governance slices
- entry conditions
- action checklist and out-of-scope boundaries
- affected artifacts
- TODO and changelog coordination
- Development Verification / TestKit Coverage when coding verification materially affects exit criteria
- verification / exit criteria / closeout summary
- risks / rollback notes
- next possible phases or roadmap/next-goal recommendation when meaningful

### 9) Verification, closeout, and rollback
Each child phase should define local verification, closeout, and rollback/containment notes. `phase/SUMMARY.md` still owns end-to-end verification and overall rollback behavior.

Phase-backed closeout should report practical delivery, not just files/tasks/audit state:
- delivered feature, capability, behavior, governance improvement, or verification gate
- user/system impact
- evidence-strength-aligned verification basis
- selected design-slice semantic items are either verified or carried forward with an explicit status instead of being silently omitted behind a visible headline output
- next phase state when relevant
- a compact supported next-phase/wave/goal recommendation when checked surfaces show meaningful successor work

---

## Part C — TODO and Live Task Tracking

### 1) Durable vs live tracking
`TODO.md` is the compact durable current execution index.
- it is not version authority
- it does not replace live task visibility
- it should not carry accumulated history once rollover is required
- in normalized compact-entrypoint form it should keep release/active-wave context, compact completed highlights, current active or deferred items that still need visibility, and explicit `history/` / `done/` references

Claude Code's built-in task list is the live execution-tracking surface for active non-trivial work.
- use the built-in task list for planned / in-progress / completed slices during active work
- keep `TODO.md` for current durable tracking plus pointers to moved history/detail
- do not treat the built-in task list as a governed repository document
- do not treat `TODO.md` as the primary live execution board during active non-trivial work

### 2) TODO compaction consequence
`TODO.md` stays a compact current execution index rather than absorbing live execution, detailed history, phase roadmap, release notes, or verification logs. When size/thrash or mixed-role pressure triggers rollover, apply the preservation, shard, snapshot, threshold, and no-delete contract in `document-integrity.md`; retain current/deferred visibility and reachable history references in `TODO.md`, while version and staged-execution detail remain in changelog and phase.

### 4) Live task-list trigger model
Use the built-in task list by default when work is non-trivial, has 3+ steps, spans multiple files/stages, may continue across slices, benefits from live visibility, has an active phase, decomposes into distinct lanes, or has non-trivial coding work where implementation and verification are distinct outcomes.

Do not force task-list overhead for trivial isolated work or one-step lookup/fix work.

### 5) Phase-linked live task shaping
When the built-in task list is in use for phase-backed work:
- inspect `/phase` context first and default to the current active phase before later phases
- when a task creates or extends phase artifacts, keep the canonical lineage result visible; a new major records why current and existing-family child fits failed
- keep phase context visible in task subject or description
- shape tasks around outcome, expected output, and completion gate when that prevents command-only drift
- split implementation, verification, and governance/release-sync into separate tasks only when combining them would hide gates or ownership
- keep tasks outcome-sized rather than command-sized
- mark `in_progress` when real work begins and `completed` as soon as the slice is actually done
- preserve a visible verification slice when implementation is done but targeted verification remains material
- use the task list first for the next unfinished slice; if insufficient, fall back to active phase context, `phase/SUMMARY.md`, `TODO.md`, and checked implementation state

### 5.1) Selected-goal task materialization
When a selected goal or plan-backed route is execution-ready and non-trivial, materialize it into bounded built-in tasks before deep continuation. Authoring alone does not trigger execution. Keep goal/plan linkage visible, ask one substantive question if objective/scope/gate/access/approval is insufficient, and separate implementation, verification, or governance tasks when their gates differ. Worker topology defers to `worker-routing-and-context.md`.

### 5.2) Progress rendering
Progress layout defers to `explanation-and-presentation.md`; keep completed scope checked and bounded, and do not turn phase/task tracking into a dashboard or stop ceremony.

### 7) Live tracking friction recovery
If live task-list creation or update fails, classify whether tracking is material to safe continuation.
- when live tracking is material for non-trivial phase-backed, multi-step, or coordinated work, repair the task entry/title/scope/phase linkage before treating work as synchronized
- when tracking friction is non-material to a bounded standalone research/review lane, continue the worker-routing path and report the tracking limit instead of collapsing it into leader raw absorption
- do not let task-list friction justify skipping required durable TODO/phase/design/changelog sync when those surfaces are in scope
- restore or update live tracking before broader continuation if the objective remains non-trivial

### 8) Pending-only and simplicity discipline
- pending sections contain pending tasks only
- completed content belongs in `Completed`, `History`, or referenced `todo/done/`
- avoid dashboard counters, priority grids, per-task timestamps, deadline fields, telemetry blocks, or one-task-per-command overhead

### 9) TODO synchronization order
When governance work changes governed artifacts, TODO sync still comes after:
1. design
2. runtime rule
3. changelog
4. TODO, including active-entrypoint compaction and history/done reference updates when rollover is triggered

The later sync order does not weaken early startup establishment or live task-list expectations.

---

## Trigger Model

| Trigger | Required handling |
|---|---|
| new governed chain | resolve design + changelog + TODO; evaluate phase/patch; initialize live task list when non-trivial |
| multi-file governed change | resolve TODO and likely phase before drift |
| staged work or rollout gates | establish `/phase` via lineage handling |
| clear governed design for staged execution | synthesize phases from design truth and keep current-phase live tasks visible |
| broad phase-backed objective with distinct implementation / verification / governance slices | define lanes or lane-aligned tasks before deep execution |
| selected design slice carries behavior, invariant, failure-mode, or dependency semantics beyond the headline feature label | extract the selected semantic items into phase/task/verification coverage and assign explicit statuses before closeout |
| active phase or implied staged lane | expose phase context in built-in tasks and current-phase-first execution |
| current phase lane closes and the next lane is selected or clearly implied | continue into the next lane and keep phase linkage visible |
| selected non-trivial goal/plan enters execution | materialize bounded tasks with visible goal linkage and distinct verification/governance gates when needed |
| governance/release-sync slice inside an active phase | give it its own lane or task when mixing it with implementation would blur ownership or gates |
| oversized `TODO.md` or `phase/SUMMARY.md` | invoke the `document-integrity.md` rollover contract and keep compact active entrypoints |
| God Phase or TODO overload | keep the active role visible and route repair through the owning phase or document-integrity contract |
| implementation done but verification still material | preserve a verification slice in phase closeout and live task tracking |
| true objective completion with meaningful successor work | report supported next phase/wave/goal with why, output, and gate |

---

## Anti-Patterns
Avoid unresolved startup posture; `create now` or task continuation treated as automatic new-major authority; `not required`/cleanup as deletion authority; filler phases or trivial lane scaffolding; God Phase/TODO bodies; history replacing active entrypoints; live tasks replacing durable surfaces; authoring materialized as execution; hidden phase/goal/gate context; closeout before selected semantics and verification are explicitly resolved; or file/task-only closeout without delivery, impact, and evidence basis.

---

## Integration
Related owners:
- [document-governance.md](document-governance.md) / [document-integrity.md](document-integrity.md) — document roles, sync, rollover, hygiene
- [worker-routing-and-context.md](worker-routing-and-context.md) / [safe-io.md](safe-io.md) — lane topology and bounded intake
- [coding-discipline.md](coding-discipline.md) — coding verification/TestKit
- [execution-and-goal-frame.md](execution-and-goal-frame.md) / [goal-authoring-and-route-support.md](goal-authoring-and-route-support.md) — continuation, goals, and route support
