# Goal Authoring and Route Support
> **Current Version:** 1.4
> **Design:** [design/goal-authoring-and-route-support.design.md](design/goal-authoring-and-route-support.design.md) v1.4
> **Session:** adda8afb-6edf-466b-add9-b9649b718e01
> **Full history:** [changelog/goal-authoring-and-route-support.changelog.md](changelog/goal-authoring-and-route-support.changelog.md)

## Rule Statement

**Core Principle: `/goal` owns outcome, completion proof, scope and hard guardrails. Construct it from checked governing context, keep route support subordinate, and open `/plan` only for route overflow or an explicit planning request. Goal construction never selects its own successor, execution or weaker proof.**

พูดง่าย ๆ: `/goal` บอกว่าจะทำอะไรและอะไรนับว่าเสร็จ; route บอกลำดับที่จำเป็น ไม่สร้าง objective อีกอัน.

## Goal Construction and Sources

A plain governed goal request is enough for planning-depth resolution; do not require special “goal plan file” wording. [execution-and-goal-frame.md](execution-and-goal-frame.md) selects direct continuation, candidate goals, one advisory `/goal`, clarification or none. Receive that posture rather than independently promote candidates. Several materially different directions remain prose candidate goals until one is selected/sufficiently bounded.

Use governed sources only when materially repo-governed: current source-tree multi-step/phase/design work, runtime-rule/doc/release/parity/proof work, or current-state/review truth. Do not pull heavy context into trivial/non-governed work. Sourcing order:
1. design for target truth and meaning of done
2. current phase, live tasks, TODO and checked implementation for applicable execution state
3. changelog when version/release/current state matters
4. Patch when before/after boundary matters
5. README when user-facing/install/front-page state matters

Translate checked context into one bounded artifact, not improvised requirement prose:

| Slot | Meaning |
|---|---|
| candidate goal label / done condition | selected outcome and observable completion |
| `required_proof_layer` | current Goal's selected terminal gate, not maximum imaginable proof |
| `current_reachable_layer` | strongest currently available/approved proof; expose a gap, do not call weaker proof complete |
| `excluded_or_successor_layers` | explicitly classify materially distinct later/excluded proof |
| route prerequisites | state/access/identity/approval/deployment/restart/capability changes before dependent proof |
| scope / keep constraints / stop bound | bounded change, protected behavior and runaway stop if needed |

Keep only decision-changing slots; a simple goal uses one direct proof/check. Before emission/starting, test every proposed done point against scope, current environment/capability/approval and a credible observable proof path. Reachability labels are `REACHABLE_NOW`, `REQUIRES_APPROVAL`, `REQUIRES_EXTERNAL_STATE_CHANGE`, `REQUIRES_USER_ACTION`, `UNAVAILABLE_WITH_CURRENT_CAPABILITY`, `NOT_APPLICABLE`.

Consume execution's proof-selection contract: a source/code goal cannot infer authenticated/live/deployed/installed/restarted Product proof from “done/working/verify,” operational nouns or diagnostic/recovery/mutation capabilities. Such proof is excluded/successor unless explicitly selected by user/governed authority. Explicit terminal proof remains binding despite unavailable capability; record prerequisites/blocker instead of demotion. Repair an infeasible assistant-inferred gate in the existing Goal/plan and reconcile tasks; remaining work/duration/difficulty alone is not infeasibility.

An advisory `/goal` stays unselected execution. Do not construct it from unresolved approval-sensitive/destructive/divergent work. Emit a copyable advisory command only if its required proof or checked prerequisite path can become transcript-visible; already selected unreachable proof may instead be honestly blocked. This rule encodes selected proof, never moves required proof to a successor just for closure.

## Smallest Sufficient Route

| Need | Route support |
|---|---|
| simple bounded goal | direct `/goal` |
| useful ordering that fits compactly | non-durable route notes inside/adjacent to the goal |
| complexity or later continuation materially needs persistence | durable route-only file |
| outcome-changing scope/gate unknown | one substantive work question, not routing-choice labels |

Order enabling state/identity/access/approval/runtime prerequisites before dependent checks. Map each slice to output/gate/reachability; the route ends at selected Goal proof. Excluded or unselected successor operations are outside blocking task order. Unmet unchanged prerequisites mean repeated downstream checks add no signal. Repair route drift with the Goal rather than make `/plan` a second objective or force replacement goals.

Internal reasoning, bounded helper analysis, log/test triage and verification ordering support authoring only when useful. They are not objective authority/proof. Main synthesis and construction remain responsible; [worker-routing-and-context.md](worker-routing-and-context.md) owns support selection.

### Durable Plan-reference lifecycle

`Plan reference` is valid only for a checked existing route-only file or one successfully written and verified during this authoring flow. Never emit an intention, draft or unwritten path; surface the write/verification blocker. When the flow can safely write/verify required route support, do it without save-plan confirmation or asking the user to invoke `/goal` again.

For a selected goal keep route inside the goal-centric presentation first. `/plan` is overflow for meaningful sequence/task/phase/owner/verification detail or explicit standalone planning—not the default second command. `/goal` retains outcome/done/proof/scope/hard guards; `/plan` retains route/sequence/task/owner order. Route/helper/plan completion cannot close an open objective gate.

## Authoring Stop and Exact Artifact

Authoring-only requests stop at final Goal plus subordinate route support unless execution is separately selected or clearly implied. Do not begin execution or append `Subagent-Driven`/`Inline Execution` menus. Preserve internal routing labels only when the workflow/literal itself is under discussion.

Use the dominant exchange language unless explicitly changed. Keep `/goal`, paths, version tags, identifiers and query parameters exact; translating only wrapper labels while leaving the body in another language is insufficient. [explanation-and-presentation.md](explanation-and-presentation.md) renders the selected artifact; it does not promote or change its authority.

With verified durable support, use one copied artifact in this order:
```text
/goal <outcome + required transcript-visible proof/checks + bounded scope + keep constraints + material proof/prerequisite distinctions + optional stop bound>
Plan reference: <exact route-only plan path>
```

Omit `Plan reference` without a verified durable file. Include layer/prerequisite distinctions only when material; wrapper text is allowed but cannot carry the sole durable pointer outside the copied artifact.

## Trigger Dispatch and Boundaries

- plain governed goal → checked construction and smallest route, no special syntax required
- source/code done point → credible reachable proof; preserve explicit terminal selection and classify others
- durable route → write/verify first, then `/goal` followed by `Plan reference:`
- authoring only → stop at artifact, no execution-choice ceremony
- selected route too large → `/plan` overflow without replacing objective

No fake Plan reference, heavy sourcing/durable plans for trivial work, candidate promotion from route convenience, or weaker proof presented as selected completion.

## Integration

Decision/closure: [execution-and-goal-frame.md](execution-and-goal-frame.md). Task/phase: [phase-todo-artifact.md](phase-todo-artifact.md). Claim strength/rendering: [accurate-communication.md](accurate-communication.md), [explanation-and-presentation.md](explanation-and-presentation.md).
