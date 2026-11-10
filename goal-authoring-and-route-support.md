# Goal Authoring and Route Support
> **Current Version:** 1.5
> **Design:** [design/goal-authoring-and-route-support.design.md](design/goal-authoring-and-route-support.design.md) v1.5
> **Session:** 08244912-a195-4926-84e6-8c202c667ba5
> **Full history:** [changelog/goal-authoring-and-route-support.changelog.md](changelog/goal-authoring-and-route-support.changelog.md)

## Rule Statement

**Core Principle: `/goal` owns outcome, completion proof, scope and hard guards. Construct it from checked context; route support is subordinate. Use `/plan` only for route overflow or explicit planning. Authoring cannot select execution/successors or weaken proof.**

พูดง่าย ๆ: `/goal` บอกว่าจะทำอะไรและอะไรนับว่าเสร็จ; route บอกลำดับที่จำเป็น ไม่สร้าง objective อีกอัน.

## Goal Construction and Sources

A plain governed goal request warrants planning-depth resolution; no special “goal plan file” wording needed. [Execution](execution-and-goal-frame.md) selects direct continuation, candidates, one advisory `/goal`, clarification or none. Consume that posture, not promote candidates. Materially different directions remain prose until selected/sufficiently bounded.

Read governed context only for materially repo-governed source-tree/phase/design, Runtime/doc/release/parity/proof or current-state/review work—not trivial unrelated tasks. Source in order:
1. design: target and meaning of done
2. phase/live tasks/TODO/checked implementation: applicable execution state
3. changelog: version/release/current state when relevant
4. Patch: meaningful before/after boundary
5. README: user-facing/install/front-page state

Construct one bounded artifact from checked meaning:

| Slot | Meaning |
|---|---|
| candidate label / done condition | selected outcome and observable completion |
| `required_proof_layer` | selected terminal gate, not maximum conceivable proof |
| `current_reachable_layer` | strongest approved/available proof; expose gaps, not weaker completion |
| `excluded_or_successor_layers` | distinct later/excluded proof |
| route prerequisites | state/access/identity/approval/deploy/restart/capability before dependent proof |
| scope / keep constraints / stop bound | bounded change, protected behavior, useful runaway stop |

Keep decision-changing slots only; simple goals need one direct check. Before emission/start, test each done point against scope, actual environment/capability/approval and observable proof. Reachability: `REACHABLE_NOW`, `REQUIRES_APPROVAL`, `REQUIRES_EXTERNAL_STATE_CHANGE`, `REQUIRES_USER_ACTION`, `UNAVAILABLE_WITH_CURRENT_CAPABILITY`, `NOT_APPLICABLE`.

Consume execution's proof policy: “done/working/verify,” operational nouns and diagnostic/recovery/mutation capabilities do not select authenticated/live/deploy/install/restart proof for source/code work. Such proof is excluded/successor unless explicitly selected by user/authority. Selected terminal proof remains binding even if unavailable: preserve prerequisites/blocker, do not demote. Repair an infeasible assistant-inferred gate in the existing Goal/plan/tasks; difficulty/duration/remaining work alone is not infeasibility.

An advisory `/goal` is not execution selection. Do not construct one from unresolved destructive/approval-sensitive/divergent work. Emit a copyable command only if required proof or a checked enabling route can become transcript-visible; already-selected unreachable proof may remain honestly blocked. Never shift required proof to a successor for closure.

## Smallest Sufficient Route

| Need | Support |
|---|---|
| simple bounded goal | direct `/goal` |
| useful compact ordering | non-durable notes in/adjacent to goal |
| complexity/continuation needs persistence | durable route-only file |
| outcome-changing scope/gate unknown | one substantive work question, not routing labels |

Order state/identity/access/approval/runtime prerequisites before dependent checks. Map each slice to output/gate/reachability, ending at selected Goal proof. Excluded/unselected successors do not block the route. Rechecking unchanged unmet prerequisites adds no signal. Repair drift with the Goal, not a second `/plan` objective or replacement Goal.

Reasoning, bounded helpers, test/log triage and check ordering support authoring only when useful; they are not authority/proof. Main owns synthesis; [routing](worker-routing-and-context.md) selects support.

### Durable Plan-reference lifecycle

`Plan reference` requires a checked existing route-only file or one successfully written/verified in this flow. Never emit an intention/draft/unwritten path; surface the blocker. If safe writing/verification is possible, perform it without save-plan confirmation or asking the user to invoke `/goal` again.

Keep route goal-centric first. `/plan` is overflow for meaningful sequence/task/phase/owner/proof detail or explicit standalone planning, not the default second command. `/goal` retains outcome/done/proof/scope/guards; `/plan` sequence/order. Route/helper/plan completion cannot close an objective.

## Authoring Stop and Exact Artifact

Authoring-only stops at Goal plus subordinate route unless execution is separately selected/clearly implied. Do not execute or append `Subagent-Driven`/`Inline Execution` menus; retain routing labels only when discussing their literal workflow.

Use the dominant exchange language unless changed explicitly. Keep `/goal`, paths, versions, identifiers/query parameters exact; translating the wrapper alone is insufficient. [Presentation](explanation-and-presentation.md) renders, not promotes, the artifact.

With verified durable support, emit one copyable artifact in this order:
```text
/goal <outcome + required transcript-visible proof/checks + bounded scope + keep constraints + material proof/prerequisite distinctions + optional stop bound>
Plan reference: <exact route-only plan path>
```

Without a verified file, omit `Plan reference`. Include layer/prerequisite distinctions only when material. Wrapper prose cannot be the sole durable pointer outside the artifact.

## Trigger Dispatch and Boundaries

- governed goal → checked construction/smallest route, no special syntax
- source/code done → reachable observable proof; preserve selected terminal gate
- durable route → write/verify before `/goal` then `Plan reference:`
- authoring only → stop at artifact, no execution menu
- selected route overflow → `/plan`, not a new objective

No fake reference, heavy sourcing/durable plan for trivial work, candidate promotion for routing convenience or weaker proof as completion.

## Integration

[Execution](execution-and-goal-frame.md) selects decisions/closure; [tasks/phases](phase-todo-artifact.md) admit structure; [accurate wording](accurate-communication.md)/[presentation](explanation-and-presentation.md) render proof faithfully.
