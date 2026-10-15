# Phase, TODO, and Artifact Initiation
> **Current Version:** 1.38
> **Design:** [design/phase-todo-artifact.design.md](design/phase-todo-artifact.design.md) v1.38
> **Session:** b8a3c38a-53b5-4d7d-a9ac-6a6f082911b2
> **Full history:** [changelog/phase-todo-artifact.changelog.md](changelog/phase-todo-artifact.changelog.md)
> **Absorbed:** artifact-initiation-control v1.9, phase-implementation v2.35, todo-standards v2.28

## Rule Statement

**Core Principle: Activate artifacts, phases and live tasks only for real ownership/persistence/output gates. Track bounded outcomes rather than commands/files/helpers, preserve strict lineage and selected semantic proof, and keep durable/live state compact. Findings and available helpers do not recursively generate work.**

พูดง่าย ๆ: หลายคำสั่งเป็นงานเดียวได้; เปิดเอกสาร/task/phaseเมื่อมีหน้าที่จริง และจบตามผลลัพธ์ที่เลือก.

## Part A — Artifact Startup and Ownership

Before meaningful governed work resolve relevant surfaces as `use existing`, `create now`, `ask now`, `not required`; live tasks as `initialize now` or `not required`. Lightweight exploration may precede this boundary; target planning, staged rollout/durable decomposition/Patch review may not. One checked outcome/owner classification discharges all non-triggered surfaces together—no ritual per absent artifact. Reuse fitting authority; ask only about material ownership/scope/workflow/approval ambiguity. Re-evaluate affected posture only if work shape changes. Retrospective artifacts are repair, not normal startup; `trivial`, cleanup or `not required` never authorizes removal.

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

When density/God pressure materially affects selected work and cannot safely stay local, route to the real owner: design active sharding; changelog same-chain `changelog/<chain>/v*.changelog.md`; inactive applicable history `changelog/done/`; TODO/phase history/done; God Phase via lineage; God Patch via review family. No changelog fallback authority. Clear fitting owner permits reuse/create; ambiguity requires a bounded question. Unrelated pressure stays advisory. `create now` never implies a new major; task/phase slices need independent outputs/gates, not extracted helper count.

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

`/phase` consumes normalized design/Patch review one-way, never replaces target truth. Derive outcome stages by dependencies, risk, rollout/output/proof; update summary/active children/live tasks when selected. Keep setup/edit/focused check/correction together for one gate; responsibility-family repair is not one phase per helper/facade/file. Helpers remain subordinate and main source integration stays leader-owned.

For each selected design slice identify behavior/invariants/failure modes/state-dependencies/acceptance clues/exclusions. Preserve concise coverage in phase/tasks, not the whole design. Track `not started` or `implemented` (intermediate until material proof); final disposition is `verified`, `deferred`, `blocked`, `not applicable`, `out of scope`, visibly preserving pending semantics. Headline output cannot hide uncovered durability/recovery/retry/idempotency/rollback.

### Summary, child and reference roles

Summary owns compact global context/target/risk/dependency/roadmap, active-or-latest-completed visibility, lineage/design/Patch links, handoffs/TODO/changelog, end-to-end proof and overall rollback. Each active child defines or maps to its summary, phase ID/status, design references and local TODO/changelog coordination. Children own objective/why/output/gate/entry/exclusions, selected semantics, affected artifacts/checklist, local verification/containment and decision-relevant already-governed next state. Coding exits show `Development Verification / TestKit Coverage` or equivalent. Move detailed history to referenced history/done rather than overload active bodies.

When evidence supports forecasting, roadmap entries name goal/output/gate/dependencies/deliverables and `active`, `selected`, `implied-unblocked`, `proposal`, `blocked`, `needs-approval`, `none opened`. Visibility is not automatic execution. [execution-and-goal-frame.md](execution-and-goal-frame.md) owns continuation/successor posture; goal construction belongs to its goal-authoring owner.

Summary and Patch-derived children name exact timestamped `Patch References`; no ID/index/basename/wildcard guess. `none` is valid only if Patch is genuinely unnecessary. Closeout states delivered behavior and impact, matching proof/limits, semantic dispositions and actual next-phase state—not merely files/tasks/audit counts.

## Part C — Durable TODO and Live Tasks

`TODO.md` is a compact durable current index, not version authority, primary live board, roadmap, release timeline or log dump. Keep active/deferred items, release/wave context and brief completed highlights with reachable history/done. Version detail belongs changelog; stage detail belongs phase. Live tasks coordinate independently acceptable planned/in-progress/completed outcomes without replacing TODO persistence.

Admit tasks for two or more meaningful outcomes/gates, phase-backed work, material handoff/continuity, or explicit user request. Several commands/files or implementation plus its focused test are not sufficient alone. One outcome stays one task unless distinct owner/approval/rollback/proof/resume conditions justify split. Keep useful ordered substeps, selected decisions, changes, actual checks, evidence pointers and remaining obligations inside those tasks, in the working language; honor an explicit Thai checklist request. Checkpoint real continuation/handoff risk, not every command. Do not create tasks from every finding/helper/worker lane.

### Phase-linked task lifecycle

- inspect current phase and execute selected current work before unselected later phases; subject/description keeps phase/goal linkage when applicable
- shape by accepted output/gate; separate implementation/proof/governance only for real acceptance/owner/resume distinctions
- merge required same-owner corrective findings into current task; leave optional cleanup/successors unselected
- mark `in_progress` before work and `completed` promptly only when its bounded gate is actually satisfied
- preserve selected semantic/proof coverage and material verification tasks, including blocked state/resume when required capability is unavailable
- discover next work from tasks → active phase/SUMMARY → compact TODO → checked implementation; history/done through active references only

Consume execution's proof-selection policy rather than reconstruct it: close satisfied source/non-live tasks before optional live/rendered observation, which stays excluded/advisory without a task until selected. If preflight repairs an infeasible assistant-inferred Goal/plan point, remove that accidental blocker immediately and retain completed proof; explicitly selected live proof remains blocked with its enabling condition under `NO_RETRY_UNTIL_CHANGE`. Do not silently demote required proof or leave optional proof blocking the current family.

Materialize tasks for selected execution only when admitted; authoring alone is not execution. Worker support cannot manufacture task boundaries. Ask one substantive work question only for insufficient scope/gate/access/approval, never internal routing menus. Progress layout belongs to presentation and must not become a dashboard or pause ceremony.

### Evidence handoff and finalization

When a selected family owes durable docs, initialize a real docs-finalization task before all relevant tasks close. Technical tasks may close at their verified gates after handing off their evidence. Finalization reads relevant completed and pending task details, checks them against source/design/proof, synthesizes the fitting durable owners and verifies that handoff before completing last in that family. Do not empty the board first and then recover details from transcripts. An outstanding task is not a persistence guarantee; no particular cleanup/deletion mechanism is assumed.

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
