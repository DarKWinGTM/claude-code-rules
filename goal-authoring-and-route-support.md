# Goal Authoring and Route Support
> **Current Version:** 1.3
> **Design:** [design/goal-authoring-and-route-support.design.md](design/goal-authoring-and-route-support.design.md) v1.3
> **Session:** 48a3ef9b-50cf-4574-8f00-4f6b6e28f76e
> **Full history:** [changelog/goal-authoring-and-route-support.changelog.md](changelog/goal-authoring-and-route-support.changelog.md)

---

## Rule Statement

**Core Principle: Keep `/goal` as the objective authority surface, keep route support subordinate to that goal, source governed goal artifacts from checked execution surfaces rather than improvised prose, and open `/plan` only when route detail no longer fits safely inside the goal-centric surface.**

พูดง่าย ๆ: `/goal` บอกว่าจะทำอะไรและอะไรนับว่าทำเสร็จ ส่วน route support บอกว่าจะเดินไปทางไหนโดยไม่แย่งความเป็นเจ้าของ objective.

---

## Core Contract

### 1) Plain governed goal requests are enough
When the user plainly asks for a governed goal, that request is enough to trigger planning-depth resolution.

Required guidance:
- do not require wording such as `goal plan file` before deciding what route support is needed
- keep `/goal` as the objective owner for outcome, proof/checks, scope, and hard guardrails
- if the current turn is only goal or plan-file authoring, stop at the final goal artifact plus subordinate route support unless execution is also selected or clearly implied elsewhere

### 2) Source governed `/goal` from checked execution surfaces
When the requested or successor objective is repo-governed and depends materially on current execution state, source the goal from checked governed surfaces rather than improvised prose.

Use this sourcing order:
- design first for target-state truth and authoritative meaning of done
- active execution surfaces next: current phase, built-in task list, `TODO.md`, and checked implementation state
- changelog only when version/release/current-state truth materially shapes completion
- patch only when before/after review boundaries materially shape the objective
- README only when front-page current-state, install guidance, or user-visible repo impact materially shapes completion

Governed-surface context is mandatory only when the request or successor objective is materially repo-governed, such as:
- multi-step work inside the current source tree
- phase-backed or lane-backed work
- design target-state truth materially shaping the objective
- runtime-rule-impacting, doc-sync, release-sync, parity, or verification work
- current-state, release, or review truth depending materially on changelog, patch, or README alignment

### 3) Translate governed context into one bounded goal artifact
When a governed `/goal` is appropriate, translate checked execution context into these concept slots:
- candidate goal label
- done condition
- `required_proof_layer`: the proof layer selected as the current goal's completion gate
- `current_reachable_layer`: the strongest proof reachable in the selected scope with currently available and approved capability
- `excluded_or_successor_layers` when materially different, with each layer classified explicitly as excluded or successor
- route prerequisites when a later proof layer depends on state, access, approval, deployment, restart, or another capability change
- scope boundary
- keep constraints
- stop bound when runaway continuation is a risk

Required guidance:
- keep only the parts needed to define completion, proof, scope, and hard guardrails
- bind `required_proof_layer` to the current goal's selected completion gate, not to the strongest imaginable whole-system proof
- for a source/code goal, must not infer live, authenticated, deployed, installed, or restarted Product proof into `required_proof_layer`; absent explicit selection by the user or checked governed authority, keep that proof in `excluded_or_successor_layers`
- generic wording such as `complete`, `verify`, `working`, or `done` does not explicitly select live proof, and an assistant-authored recommendation cannot promote live proof into the current goal's terminal gate by assistant inference
- use `current_reachable_layer` to expose a real proof gap; do not present it as completion when it is weaker than `required_proof_layer`
- classify proof outside the current goal explicitly as excluded or successor; do not turn it into an accidental blocker or silently drop it
- if an explicitly selected terminal proof is stronger than the current reachable layer, keep that proof inside the current goal and keep the goal open with its prerequisite or blocker; difficulty, externality, or unavailable capability does not demote it
- classify material proof reachability as `REACHABLE_NOW`, `REQUIRES_APPROVAL`, `REQUIRES_EXTERNAL_STATE_CHANGE`, `REQUIRES_USER_ACTION`, `UNAVAILABLE_WITH_CURRENT_CAPABILITY`, or `NOT_APPLICABLE`; the label exposes the gate but does not change the selected terminal proof
- when several successor directions remain live, surface compact candidate goals before promoting any one into `/goal`
- if checked surfaces already define a smaller truthful successor slice, derive that smaller slice instead of emitting a broad future label
- for an advisory `/goal`, do not emit a copyable command unless the required proof, or a checked prerequisite path to it, can become transcript-visible; an already selected terminal proof remains binding and may be reported blocked rather than demoted

### 4) Route-support and durable `Plan reference` contract
Choose the smallest route support that safely serves the goal:
- direct `/goal` wording for a simple bounded objective
- compact non-durable route notes when ordering matters but still fits the goal-centric surface
- a durable route-only plan file only when complexity or later execution materially needs persistence
- one narrow substantive clarification about the work when objective, scope, or gate is not bounded enough

Order prerequisites that change state, identity, access, approval, or runtime capability before dependent proof checks. Do not repeat a downstream check unchanged while unmet prerequisites mean it cannot add signal. Route prerequisites remain subordinate: they do not replace the goal's proof gate or become completion proof by themselves.

Ask about the work itself, not routing labels. Do not force trivial goals into durable plan files or pull broad governed context into trivial non-governed work.

A durable `Plan reference` requires a route-only plan file that exists in checked scope or was successfully written and verified in the same authoring flow. Never emit it from intention, draft text, or an unwritten file; report a creation/verification blocker instead. Canonical artifact order is defined in section 9.

### 5) Internal support remains subordinate
Internal analysis, route drafting, verification ordering, testing/log triage, and bounded helper lanes may support goal authoring when materially useful. They remain subordinate route support: not a second objective surface, independent authority, or completion proof.

When the same authoring flow can write and verify required durable route support, do not ask whether to save it and do not ask the user to invoke `/goal` again.

### 6) Authoring stop boundary
If the current turn is only goal or route-support authoring, stop at the final goal artifact plus subordinate route support. Do not append a default execution-style choice menu or begin execution unless execution is separately selected or clearly implied. Preserve internal routing labels only when workflow behavior itself or exact artifact wording is under discussion.

### 7) Selected advisory-goal and `/plan` boundaries
`execution-and-goal-frame.md` decides whether a boundary calls for direct continuation, candidate goals, one advisory `/goal`, clarification, or no successor. This rule receives that selected posture and constructs the bounded goal artifact; it does not independently promote a candidate.

An advisory `/goal` remains unselected execution. Do not construct one from approval-sensitive, destructive, or materially divergent work unless the execution owner has resolved the required basis or approval.

Goal-authoring encodes the proof-layer posture selected by execution or the user; it does not independently move proof between the current goal and successor scope. An explicitly selected terminal proof remains the current goal's terminal gate until it passes or the user explicitly narrows the goal.

For a selected goal, keep route detail inside the goal-centric surface first. Open `/plan` only when sequence, task/phase breakdown, verification/owner ordering, explicit standalone planning, or route size no longer fits compactly.

`/goal` owns outcome, done condition, proof/checks, scope, and hard guardrails. `/plan` owns route, sequence, task breakdown, owner ordering, and overflow route detail. Repair route drift instead of letting `/plan` replace the selected objective. Route, helper, or plan completion never closes the goal while its proof or gate remains open.

### 8) Language and exact-literal boundary
Follow the dominant language of the active exchange unless the user explicitly chooses another. Preserve exact literals such as `/goal`, paths, version tags, identifiers, and query parameters; do not translate only the wrapper while leaving the goal body in another language.

### 9) Canonical copyable artifact
When durable route support is present, use this order inside one copied artifact:

```text
/goal <outcome + required transcript-visible proof/checks + bounded scope + keep constraints + material proof-layer/prerequisite distinctions + optional stop bound>
Plan reference: <exact route-only plan path>
```

Include proof-layer distinctions and route prerequisites only when they materially differ; simple goals keep one direct proof/check statement. Wrapper text may surround the artifact; omit `Plan reference` when no verified durable plan file exists.

---

## Application Boundary

This rule is the sole semantic owner for governed `/goal` construction after execution selects the posture, route-support selection, durable plan-file lifecycle and `Plan reference`, internal authoring support, authoring stop, selected-goal `/plan` overflow, goal-versus-route authority, and goal-artifact language/exact-literal rules.

`execution-and-goal-frame.md` owns continuation and candidate/advisory eligibility; `explanation-and-presentation.md` owns rendering. Other satellite rules retain only local task, topology, evidence-wording, or tone consequences.

---

## Anti-Patterns

Avoid:
- emitting an unwritten/unchecked `Plan reference` or placing it before `/goal`
- treating helper output or route drafts as objective authority
- appending `Subagent-Driven` / `Inline Execution` menus after pure goal/plan-file authoring
- forcing durable plan files for trivial or already direct goals
- teaching `/plan` as the default next surface for every route-heavy goal
- collapsing several materially different successor directions into one premature `/goal`
- treating route completion as goal completion
- demoting an explicitly selected terminal proof because it is external, difficult, approval-gated, or not currently reachable
- treating a weaker current reachable layer as if it satisfied a stronger required proof layer
- importing excluded or successor proof into the current goal accidentally, or leaving its status ambiguous
- running dependent proof before route prerequisites can make the check informative
- pulling heavy governed context into trivial non-governed next steps

---

## Integration
Related owners: [phase-todo-artifact.md](phase-todo-artifact.md) (goal-linked tasks/execution surfaces); [execution-and-goal-frame.md](execution-and-goal-frame.md) (mode/continuation/next-goal decisions); [accurate-communication.md](accurate-communication.md) (evidence-strength wording); [explanation-and-presentation.md](explanation-and-presentation.md) (goal rendering).
