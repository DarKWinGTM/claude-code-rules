# Phase, TODO, and Artifact Initiation
> **Current Version:** 1.18
> **Design:** [design/phase-todo-artifact.design.md](design/phase-todo-artifact.design.md) v1.18
> **Session:** 1f1873d2-0feb-485f-a5ff-d383254590dd
> **Full history:** [changelog/phase-todo-artifact.changelog.md](changelog/phase-todo-artifact.changelog.md)
> **Absorbed:** artifact-initiation-control v1.9, phase-implementation v2.34, todo-standards v2.28

---

## Rule Statement

**Core Principle: Resolve artifact posture and governed documentation chain naming/shape analysis before work drifts, use phases only when staged execution adds real value, keep `phase/SUMMARY.md` and `TODO.md` as compact active entrypoints, and treat the built-in task list as the live execution surface for non-trivial phase-backed work, including lane-oriented continuation when broad worker-fit execution needs explicit structure.**

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
- if staged work is clear, resolve phase posture now as `use existing`, `create now`, or `ask now`
- `create now` does not mean automatic new-major creation; phase lineage still decides current phase update vs subphase vs new major
- phase identity selection must still run in strict order: current active phase update → existing-family subphase → new major phase → ask/record basis
- patch is non-default during greenfield/baseline formation unless a real before/after review surface exists or the user explicitly asks for it

### 5) Startup communication contract
When startup posture materially matters, use a compact explicit shape:
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

### 5.1) Documentation chain naming and chain-shape analysis
When meaningful governed work will normalize or split active design/changelog documentation, resolve the chain naming basis and chain-shape decision before deeper edits.

Use a compact `docs_analysis` form:
```text
docs_analysis:
- document_role: <design | changelog>
- namespace_scope: <folder-scoped-single-chain | shared-multi-chain>
- actual_chain_subject: <real topic/capsule/component name>
- parent_authority: <checked parent file>
- parent_model_choice: <generic-parent | semantic-parent>
- selected_parent_filename: <active filename chosen for this chain>
- parent_model_basis: <folder-already-scopes-one-chain | shared-folder-needs-self-identifying-name | compatibility-only-legacy | unresolved>
- coexistence_state: <single-active-parent | generic-plus-semantic-ambiguous | generic-plus-semantic-compatibility-only>
- current_chain_shape: <single-file-bootstrap | flat-sibling-shards | same-stem-subfolder-normalized | archive-history-fallback>
- observed_project_shape: <checked local/example structure | unknown | not-applicable>
- extracted_doctrine: <reusable governance principle derived from checked evidence | none>
- selected_chain_shape: <single-file-bootstrap | flat-sibling-shards | same-stem-subfolder-normalized | archive-history-fallback>
- selected_target_form: <target structure intentionally chosen for this RULES chain>
- bootstrap_exit_trigger: <none | parent no longer compact | 2+ coherent slices | God-file pressure | other checked reason>
- shard_opening_basis: <why same-stem or flat-sibling shards are justified now>
- normalization_action: <append-in-parent | create-or-update-flat-sibling | create-or-update-same-stem-child | migrate-flat-to-same-stem | use-history-or-done>
- equivalence_claim_basis: <checked proof of equivalence | no equivalence claim>
- append_vs_shard_reason: <why the next detail belongs in parent or shard>
- parent_index_update_required: <yes | no>
- integrity_checks: <shard map, backlinks, version/current-state alignment, no orphan detail>
```

Required guidance:
- use this form when a governed design/changelog parent is about to receive enough new detail that append-versus-shard choice materially changes the resulting structure
- resolve `namespace_scope`, `actual_chain_subject`, `parent_model_choice`, and `selected_parent_filename` before deeper shape edits continue
- if the current folder already fully scopes one chain, a generic parent such as `design.md` or `changelog.md` may be the selected active parent model
- if the current folder contains several chains, the selected parent filename should stay self-identifying for that shared namespace
- if the current folder already acts as the chain namespace, `create-or-update-flat-sibling` may be selected without creating a redundant same-stem nested folder
- if the chain is broad, root-heavy, multi-shard, or already showing God-file pressure, same-stem nested normalization remains the strong-preferred direction
- if `bootstrap_exit_trigger` is `none`, keep the chosen parent bootstrap-first instead of opening a same-stem shard directory early
- `shard_opening_basis` must name the checked reason the chain no longer stays compact as one parent body
- `coexistence_state` must not be left ambiguous when a generic parent and a semantic parent both appear in checked scope
- only one active parent model may remain for the same chain; the other must be compatibility-only or absent
- `observed_project_shape` records what was actually checked in the example rather than what the assistant wishes the example had looked like
- `extracted_doctrine` records the reusable lesson taken from the checked example
- `selected_target_form` records the structure intentionally chosen for the current RULES chain
- if `equivalence_claim_basis` is not `checked proof of equivalence`, do not phrase the selected RULES target form as if it were the literal observed project pattern
- do not silently keep appending to a parent authority file merely because no child shard exists yet; the absence of shards should trigger classification, not default approval

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
- active phase files use `phase/phase-NNN-*.md` or `phase/phase-NNN-NN-*.md`
- daily movement may live under `phase/history/YYYY-MM-DD*.md`
- completed phase detail may live under `phase/done/`
- live phased execution files are not allowed inside patch artifacts

`phase/history/` is referenced movement history; `phase/done/` is inactive completed history. Active scans start from compact `phase/SUMMARY.md` and active child files.

### 3) Identity grammar and lineage gate
Identity grammar:
- major phase: `NNN`
- subphase: `NNN-NN`

Before opening a new major phase, choose the smallest truthful identity.

Required identity decision order is strict fall-through, not a menu:
- update the current active phase first when checked `phase/SUMMARY.md`, the current active child phase, and visible phase-linked live tasks show that the work still fits the same execution slice, goal, expected output, completion gate, dependency path, or rollback boundary
- create a new subphase second when the current phase cannot truthfully absorb the work, but the work still continues the same bounded execution gate or rollout family inside an existing major phase
- create a new major phase third only after checked evidence rules out both current-phase update and existing-family subphase, and the work forms a distinct top-level rollout family, capability boundary, output, verification gate, release boundary, or rollback boundary
- when a new major phase is selected, record visible why-not-current and why-not-subphase basis rather than leaving the negative checks implicit
- ask or record the governing basis when multiple families plausibly fit and checked evidence does not settle lineage

A new file need, completed current phase, task-list continuation, fresh concern wording, or milestone closeout is not by itself a lineage break.

Subphase fit depends on real shared goal/output/gate meaning, not only broad product area or historical proximity.

### 4) God Phase repair
A God Phase is a phase file that tries to execute several independent phases at once.
Signals include:
- multiple primary goals that can complete independently
- multiple expected outputs that do not share one bounded gate
- unrelated verification gates or rollback boundaries
- roadmap/changelog/TODO/patch/execution all mixed in one active body

Repair posture:
- restructure in place when one bounded goal/output/gate still exists
- split into `NNN-NN` subphases when work shares the parent rollout gate
- open a new major phase when capability, release, verification, output, or rollback boundary is distinct
- update `phase/SUMMARY.md` when the split changes navigation
- create or extend visible phase-linked live tasks when repair is non-trivial
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
- lane changes inside the same rollout family should normally stay in the current phase or a truthful subphase rather than opening a fresh major phase by momentum
- for lane changes, apply the same identity order explicitly: current active phase first, existing-family subphase second, new major phase only after both earlier fits are ruled out by checked phase context
- worker routing decides whether a lane becomes a standalone subagent or stays direct; phase only keeps the staged execution map visible
- do not create lane scaffolding for trivial, tightly sequential, or one-step work

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

### 6.1) `/goal` suggestion sourcing from governed surfaces
When another owner has already decided that an advisory `/goal` command is the right next-step shape, source the command from checked governed execution surfaces rather than from improvised prose.

Governed-surface context is mandatory only when the successor objective is repo-governed and at least one of these is true:
- the work is multi-step inside the current source tree
- the work is phase-backed or lane-backed
- design target-state truth materially defines the next outcome
- runtime-rule-impacting, doc-sync, release-sync, parity, or verification work is the objective
- current-state, release, or review truth depends materially on changelog, patch, or README alignment

Use this sourcing order:
- design first for target-state truth and the authoritative meaning of done
- active execution surfaces next: current phase, built-in task list, `TODO.md`, and checked implementation state
- changelog only when version/release/current-state truth materially shapes completion
- patch only when before/after review boundaries materially shape the next objective
- README only when front-page current-state, install guidance, or user-visible repository impact materially shapes completion

Use this translation model:
- candidate goal label ← current goal plus expected output plus the smallest useful gate clue when several successor directions remain live
- done condition (`Done when` in English-only examples) ← current goal plus expected output
- proof/check basis (`Prove with` in English-only examples) ← completion gate plus verification basis that can be surfaced in transcript
- scope boundary (`Scope` in English-only examples) ← touched artifacts, lane boundary, or bounded execution slice
- keep constraints (`Keep` in English-only examples) ← out-of-scope boundary plus preserve-semantics constraints that materially matter
- stop bound (`Stop after` in English-only examples) ← bounded execution guard when runaway continuation risk matters

Required guidance:
- do not invent a new durable tracking schema only for `/goal`
- treat the translated slots above as concept slots rather than as mandatory English surface labels; emitted natural-language scaffold should follow the dominant language of the active exchange even when the user did not issue a direct language instruction
- treat an explicit user language request as a stronger override than the default active-exchange inference
- when several successor directions remain live, shape them as candidate goals before promoting any one of them into `/goal`
- when checked phase/roadmap/TODO surfaces already show several unselected but materially different next slices and no one continuation path clearly dominates, use those surfaces to shape compact candidate goals rather than plain unlabeled next-step bullets
- when current phase/roadmap/TODO wording names only a broad future label such as `implementation wave ใหม่`, but checked goal/output/gate/touched-surface context already defines a smaller bounded successor slice, derive that smaller slice before emitting successor wording
- do not leave successor output as a generic future note when the smaller bounded slice is already derivable from checked execution surfaces
- preserve exact literals such as `/goal`, file paths, identifiers, version tags, and query parameters where exactness matters, but do not treat the whole emitted command body as one exact literal
- do not turn all roadmap/TODO detail into command text; keep only the parts needed to define completion, proof, scope, and hard guardrails
- when the user remains inside the existing `/goal` surface and the selected governed work is still non-trivial, governed execution may shape a compact `Plan draft` or verification/testing route through conditional internal native subagent assistance, but that support remains subordinate to the goal and does not create a new public route owner
- do not pull heavy governed-surface context into trivial non-governed next steps
- if the governed surfaces do not yet provide a bounded, provable successor slice, do not force a `/goal` command

### 6.2) Selected goal to `/plan` bridge for governed work
When a governed goal is already selected and the remaining work is route-heavy, the execution surfaces should bridge that goal into `/plan` rather than stuffing route detail back into goal text.
- keep `/goal` as the objective contract for outcome, proof, scope, and hard guardrails
- use `/plan` to choose sequence, phase/lane breakdown, owner ordering, and verification order when those route decisions are materially non-trivial
- bridge into `/plan` when the selected goal is multi-step, multi-file, phase-backed, owner-splitting, release-sync-heavy, or still has several materially different execution routes
- when that bridge condition holds, execution surfaces should explicitly recommend `/plan` as the next surface instead of broad prose follow-up
- if the current turn still needs bounded analysis, verification, testing, or compact route drafting inside the existing `/goal` surface, conditional internal helper use may support the selected goal without changing `/plan` route ownership
- if the selected goal is already direct, bounded, and safe to continue, keep execution in goal/phase/task surfaces without forcing a plan
- when a plan is opened, phase and task surfaces should keep visible which selected goal the route serves
- closeout should still verify the selected goal gate rather than treating completed plan steps or worker-produced route drafts as sufficient proof by themselves

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

### 2) Daily-first TODO rollover
When `TODO.md` grows past practical active-scan limits, preserve old content in reachable history/done shards and keep the main file as a compact current-state index.
- `TODO.md` keeps current active work, deferred/open items that still need active visibility, compact completed highlights, and references to `todo/history/` / `todo/done/`
- `todo/history/YYYY-MM-DD*.md` records daily movement, rollover notes, and links back to `TODO.md`
- `todo/done/<task-or-wave>.md` may hold large completed closeout detail
- pre-rollover snapshots are allowed for preservation but must be referenced rather than duplicated
- rollover is not deletion authority

### 3) TODO God-file prevention
`TODO.md` becomes a God file when it tries to store live execution, detailed history, completed closeouts, phase roadmap, release notes, verification logs, and future proposals in the active entrypoint.

Required repair posture:
- keep the active TODO as a compact current execution index
- move daily movement to `todo/history/` and large completed detail to `todo/done/`
- keep version authority in changelog and staged execution detail in phase
- do not append completed history into pending sections or current active bullets
- if a TODO update would create a large mixed-responsibility entry, split it into a current-state bullet plus history/done reference

### 4) Live task-list trigger model
Use the built-in task list by default when work is non-trivial, has 3+ steps, spans multiple files/stages, may continue across slices, benefits from live visibility, has an active phase, decomposes into distinct lanes, or has non-trivial coding work where implementation and verification are distinct outcomes.

Do not force task-list overhead for trivial isolated work or one-step lookup/fix work.

### 5) Phase-linked live task shaping
When the built-in task list is in use for phase-backed work:
- inspect `/phase` context first and default to the current active phase before later phases
- when a task would create or extend phase artifacts, keep the identity basis visible: current-phase update, existing-family subphase, new major, or ask/record basis
- a new-major basis must include why current-phase update and existing-family subphase do not fit
- keep phase context visible in task subject or description
- shape tasks around outcome, expected output, and completion gate when that prevents command-only drift
- split implementation, verification, and governance/release-sync into separate tasks only when combining them would hide gates or ownership
- keep tasks outcome-sized rather than command-sized
- mark `in_progress` when real work begins and `completed` as soon as the slice is actually done
- preserve a visible verification slice when implementation is done but targeted verification remains material
- use the task list first for the next unfinished slice; if insufficient, fall back to active phase context, `phase/SUMMARY.md`, `TODO.md`, and checked implementation state

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
| active phase or implied staged lane | expose phase context in built-in tasks and current-phase-first execution |
| current phase lane closes and the next lane is selected or clearly implied | continue into the next lane and keep phase linkage visible |
| selected governed goal has a non-trivial route still to choose | explicitly recommend `/plan` as the next surface while preserving visible linkage back to the selected goal |
| governance/release-sync slice inside an active phase | give it its own lane or task when mixing it with implementation would blur ownership or gates |
| oversized `TODO.md` or `phase/SUMMARY.md` | roll history/detail into referenced `history/` / `done/` shards and keep compact active entrypoints |
| God Phase or TODO overload | repair now when clear, otherwise create/extend a visible governed repair slice |
| implementation done but verification still material | preserve a verification slice in phase closeout and live task tracking |
| true objective completion with meaningful successor work | report supported next phase/wave/goal with why, output, and gate |

---

## Anti-Patterns

Avoid:
- meaningful governed work starting before startup artifact posture is resolved
- treating `create now` for phase as automatic new-major creation
- using `not required`, cleanup, or trivial framing as file-removal authority
- forcing phases for filler stages with no execution meaning
- phase files that mix several independent goals/outputs/gates into one active body
- letting `phase/history/` or `phase/done/` replace active phase navigation
- turning `TODO.md` into a history dump, roadmap dump, or verification log dump
- generic live task titles that hide active phase context
- treating the built-in task list as a replacement for durable TODO/phase surfaces
- lane decomposition that is forced onto trivial or tightly sequential work
- lane-aware tasks that hide goal/output/gate or collapse governance/release-sync into a generic implementation bucket
- letting task-list continuation silently allocate a new major phase
- stopping after implementation when phase-backed verification is still the active remaining slice
- phase or TODO closeout that reports only files/tasks/audit status and not delivered result / impact / verification basis

---

## Integration

Related rules:
- [document-governance.md](document-governance.md) - repository document model and sync order
- [document-governance.md](document-governance.md) - patch semantics and patch-vs-phase boundary
- [worker-routing-and-context.md](worker-routing-and-context.md) - worker scale stays separate from phase-backed lane structure
- [safe-io.md](safe-io.md) - bounded read/output behavior for broad phase-backed lanes
- [coding-discipline.md](coding-discipline.md) - phase-backed coding verification and TestKit/scenario decisions
- [execution-and-goal-frame.md](execution-and-goal-frame.md) - goal/output/gate semantics and next-goal boundaries
- [document-integrity.md](document-integrity.md) - daily-first `TODO.md` and `phase/SUMMARY.md` rollover owner
- [document-integrity.md](document-integrity.md) - hygiene must defer to required artifact posture and does not authorize deletion
