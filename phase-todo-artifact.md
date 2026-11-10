# Phase, TODO, and Artifact Initiation
> **Current Version:** 1.40
> **Design:** [design/phase-todo-artifact.design.md](design/phase-todo-artifact.design.md) v1.40
> **Session:** 08244912-a195-4926-84e6-8c202c667ba5
> **Full history:** [changelog/phase-todo-artifact.changelog.md](changelog/phase-todo-artifact.changelog.md)
> **Absorbed:** artifact-initiation-control v1.9, phase-implementation v2.35, todo-standards v2.28

## Rule Statement

**Core Principle: Activate artifacts, phases and live tasks only for real ownership/persistence/output gates. Track bounded outcomes rather than commands/files/helpers, preserve strict lineage and selected semantic proof, and keep durable/live state compact. Findings and available helpers do not recursively generate work.**

พูดง่าย ๆ: หลายคำสั่งเป็นงานเดียวได้; เปิดเอกสาร/task/phaseเมื่อมีหน้าที่จริง และจบตามผลลัพธ์ที่เลือก.

## Part A — Artifact Startup and Ownership

Before meaningful governed work classify relevant surfaces `use existing`, `create now`, `ask now`, `not required`; live tasks `initialize now`/`not required`. Light exploration may precede, target planning/staged rollout/durable decomposition/Patch review may not. One checked outcome/owner decision discharges non-triggered surfaces together, not one ritual per missing artifact. Reuse owners; clarify only material ownership/scope/workflow/approval. Revisit changed posture only. Retrospective artifacts are repair; `trivial`/cleanup/`not required` never permits removal.

Default order: design → diagram when triggered → changelog → TODO → phase → Patch.

| Surface | Real trigger |
|---|---|
| design | new/material target behavior, policy, contract or architecture |
| diagram | changed structure/visual authority/relationships/topology or existing diagram correctness; ordinary design edits may be `not required`, no automatic subject diagram |
| changelog | new governed chain or version-impacting behavior |
| TODO | execution must persist beyond interaction, spans real slices or needs durable index—not command count |
| live tasks | independently meaningful acceptance/block/handoff/resume gates, phase work, material continuity or explicit tracking request |
| phase | independent stages/dependencies/approval/proof/rollback, rollout/multi-owner integration or explicit request—not individual helpers/files |
| Patch | before/after review/rollback boundary adds real value or user requests it—not ordinary edits/greenfield by reflex |

When Patch is `create now`, capture one UTC instant to seconds and derive filename plus `Created At` from that value. Follow [document-governance.md](document-governance.md)'s exact grammar/evidence; create exclusively, fail on collision, no overwrite/suffix fallback. Revisions/moves preserve original creation identity. Emergency startup exception belongs to action safety: only smallest safe reversible containment/diagnosis when delay materially increases harm, with normal recording resumed immediately.

### Touched artifact pressure

When touched density/God pressure materially affects selected work beyond safe local repair, use its owner: active design shards; same-chain `changelog/<chain>/v*.changelog.md`; inactive history `changelog/done/`; TODO/phase history/done; God Phase lineage; God Patch review family. No changelog fallback. Clear ownership permits reuse/create, ambiguity needs a bounded question; unrelated pressure stays advisory. `create now` does not imply new major; outputs/gates, not helper counts, earn slices.

State lightweight/governed posture and unresolved gate only when it changes continuation. [document-integrity.md](document-integrity.md) owns preservation, rollover and no-loss proof.

### Governed-chain startup

Before append/split/normalize design/changelog, apply the document owner and record decision-changing `docs_analysis`:
- `document_role`, `namespace_and_subject`
- `active_parent` with generic/semantic/coexistence basis
- `selected_chain_shape`, `transition_basis` (bootstrap exit/shard/append basis)
- `action` (`append | sibling shard | same-stem child | normalize | history/done`)
- `example_basis` (observed/extracted/selected/equivalence when used)
- `integrity_updates` (map/backlinks/version/orphan prevention)

Do not infer nested detail from a filename or append merely because no shard exists. Resolve authority ambiguity before growth; do not restate the whole chain contract.

## Part B — Phase Execution and Lineage

Phases are for selected real staging/rollout/dependency/approval/proof/rollback/owner boundaries, not one same-owner outcome plus focused tests or filler stages. Active navigation is mandatory bodyful `phase/SUMMARY.md` → active child files; live execution never resides inside Patch artifacts. Daily movement is `phase/history/YYYY-MM-DD*.md`; completed detail is inactive `phase/done/`, reachable through active references.

Forward-valid paths: `phase/phase-NNN-*.md`, `phase/phase-NNN-NN-*.md`, `phase/phase-NNN-NN-NN-*.md`. Major `NNN`, subphase `NNN-NN`, nested child `NNN-NN-NN`; observed `NNN-NNa` is legacy-only; deeper hybrid `NNN-NN-NNb` is not forward-valid unless later doctrine explicitly normalizes it.

### Strict fall-through, not a menu

1. **Update current active phase first** if checked summary/child/tasks share execution slice, goal/output/gate, dependency or rollback boundary.
2. **Existing-family child second** if current cannot absorb but bounded rollout/gate family continues: major opens `NNN-NN`, subphase opens `NNN-NN-NN`.
3. **New major third** only when checked current/child fit fails and a distinct top-level capability/output/rollout/proof-release/rollback family exists; record failed earlier bases.
4. Ask/record governing basis only when several lineages remain materially plausible.

A new file, completed phase, continued task, fresh concern or milestone is not a lineage break. Topic similarity alone does not prove child fit: shared meaning, immediate lineage and bounded rollout must match.

A God Phase mixes independent primary goals/unrelated outputs/gates/rollback or design/changelog/TODO/Patch roles. Repair via the same lineage gate, update navigation/tasks, preserve legacy history and block closeout until touched pressure is repaired or visibly planned.

### Design-to-phase synthesis and coverage

`/phase` consumes normalized design/Patch review, never owns target truth. Derive outcome stages from dependencies/risk/rollout/output/proof; update selected summary/children/live tasks. Keep setup/edit/check/correction under one gate, not phases per helper/facade/file. Helpers stay subordinate; Main integrates source.

Capture selected behavior/invariants/failures/state-dependencies/acceptance/exclusions compactly in phase/tasks. `not started`/`implemented` are intermediate; final dispositions are `verified`, `deferred`, `blocked`, `not applicable`, `out of scope`. Preserve pending durability/recovery/retry/idempotency/rollback rather than close on headline output.

### Summary, child and reference roles

Summary owns compact context/target/risk/dependencies/roadmap, active/latest-completed visibility, lineage/design/Patch links, handoffs/TODO/changelog, end-to-end proof and rollback. Active children identify summary/ID/status/design/local TODO-changelog and own objective/why/output/gate/entry/exclusions, semantics, affected artifacts/checklist, local proof/containment and relevant governed next state. Coding exits show `Development Verification / TestKit Coverage` or equivalent. Refer detailed history to history/done, not overloaded active bodies.

Evidence-supported roadmap entries name goal/output/gate/dependencies/deliverables and posture: `active`, `selected`, `implied-unblocked`, `proposal`, `blocked`, `needs-approval`, `none opened`. Visibility selects no execution; [execution](execution-and-goal-frame.md) owns continuation, goal-authoring construction.

Summary/Patch-derived children use exact timestamped `Patch References`, not ID/index/basename/wildcard guesses; `none` only when unnecessary. Closeout reports behavior/impact, matching proof/limits, semantic dispositions and actual next-phase state, not counts.

## Part C — Durable TODO and Live Tasks

`TODO.md` indexes durable active/deferred work, release/wave context and brief completed highlights with reachable history/done. It is not version authority/live board/roadmap/release timeline/log. Changelog owns version detail, phase stage detail; live tasks coordinate outcomes without replacing persistence.

Admit tasks for multiple meaningful outcomes/gates, phase work, material handoff/continuity or explicit request—not command/file counts or implementation plus focused test. One outcome stays one task unless owner/approval/rollback/proof/resume differs. Keep ordered substeps, selections, changes, actual checks/evidence and remainder inside, in the working language; honor Thai checklist requests. Checkpoint real continuation risk, not each command/finding/helper.

### Phase-linked task lifecycle

- inspect current phase and execute selected current work before unselected later phases; subject/description keeps phase/goal linkage when applicable
- shape by accepted output/gate; separate implementation/proof/governance only for real acceptance/owner/resume distinctions
- merge required same-owner corrective findings into current task; leave optional cleanup/successors unselected
- mark `in_progress` before work and `completed` promptly only when its bounded gate is actually satisfied
- preserve selected semantic/proof coverage and material verification tasks, including blocked state/resume when required capability is unavailable
- review selected obligations at execution's start/resume/change/closeout boundaries; reconcile done/remaining/blocked state in the existing record, not new tasks/checklists per command
- discover next work from tasks → active phase/SUMMARY → compact TODO → checked implementation; history/done through active references only

Consume execution's proof-selection policy rather than reconstruct it: close satisfied source/non-live tasks before optional live/rendered observation, which stays excluded/advisory without a task until selected. If preflight repairs an infeasible assistant-inferred Goal/plan point, remove that accidental blocker immediately and retain completed proof; explicitly selected live proof remains blocked with its enabling condition under `NO_RETRY_UNTIL_CHANGE`. Do not silently demote required proof or leave optional proof blocking the current family.

Materialize tasks for selected execution only when admitted; authoring alone is not execution. Worker support cannot manufacture task boundaries. Ask one substantive work question only for insufficient scope/gate/access/approval, never internal routing menus. Progress layout belongs to presentation and must not become a dashboard or pause ceremony.

### Evidence handoff and finalization

If durable docs are owed, reuse/init one fitting finalization task before all family tasks close; no duplicate gate. Evidence/handoff/owner sync stays ordered substeps unless independent owner/acceptance/resume earns a task. Dependencies gate finalization completion, not local handoff or supported interim [sync](execution-and-goal-frame.md); required proof stays binding. Technical tasks may close after verified evidence handoff. Finalization reconciles completed/pending task detail against source/design/proof and durable owners, verifies handoff, then completes last—not the first documentation opportunity. Do not empty the board then reconstruct transcripts. An open task is no persistence guarantee; no cleanup mechanism is assumed.

No docs obligation means no invented final task or dummy sentinel. Do not hold or close unrelated/other-session tasks. Missing evidence requires an honest coverage limit and resume condition, not board reset/recreation or fabricated prior results. [document-governance.md](document-governance.md) owns synthesis by document role, not raw task-log duplication.

### Tracking failures and synchronization

If task creation/update fails, decide whether tracking is material. Repair title/scope/phase linkage before non-trivial phase-backed sync/closeout; bounded research may continue if tracking is non-material with its limitation stated. Task friction cannot excuse required durable state. Do not infer ownership/completion solely from convenient board status; checked design/implementation/proof remains stronger evidence.

Pending sections contain pending work only; completed detail goes to completed/history/referenced done. Avoid counters/priority grids/per-task timestamps/deadlines/telemetry and task-per-command overhead. Governance TODO order is design → runtime rule → changelog → TODO (plus required rollover links); late sync does not replace startup.

## Trigger Dispatch and Boundaries

- material governed outcome → classify once, activate only real owner surfaces
- independently staged rollout/approval/proof → strict phase lineage and semantic coverage
- selected Goal/phase execution → outcome-sized task admission, visible owner/gate
- selected proof pending → required verification remains; optional live successor does not
- oversized active entrypoint → preservation-first owner repair, never deletion by size
- bounded gate passes → reconcile/close tasks; successor visibility does not select its execution

No filler phases, one task/phase/Patch per microstep, automatic new major, orphan history, second design authority, edit-only completion, unchanged retry or unselected successor scaffolding.

## Integration

Artifact/chain/integrity: [document-governance.md](document-governance.md), [document-integrity.md](document-integrity.md). Work/proof/goal: [execution-and-goal-frame.md](execution-and-goal-frame.md), [goal-authoring-and-route-support.md](goal-authoring-and-route-support.md), [coding-discipline.md](coding-discipline.md). Helper/capture: [worker-routing-and-context.md](worker-routing-and-context.md), [safe-io.md](safe-io.md).
