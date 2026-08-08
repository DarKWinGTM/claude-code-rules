# Goal Authoring and Route Support
> **Current Version:** 1.1
> **Design:** [design/goal-authoring-and-route-support.design.md](design/goal-authoring-and-route-support.design.md) v1.1
> **Session:** 92c4d51e-eb02-4299-823a-1a6b8270f045
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
- proof/check basis
- scope boundary
- keep constraints
- stop bound when runaway continuation is a risk

Required guidance:
- keep only the parts needed to define completion, proof, scope, and hard guardrails
- when several successor directions remain live, surface compact candidate goals before promoting any one into `/goal`
- if checked surfaces already define a smaller truthful successor slice, derive that smaller slice instead of emitting a broad future label
- if proof cannot be made transcript-visible, do not promote the goal into a copyable `/goal` command

### 4) Route-support and durable `Plan reference` contract
Choose the smallest route support that safely serves the goal:
- direct `/goal` wording for a simple bounded objective
- compact non-durable route notes when ordering matters but still fits the goal-centric surface
- a durable route-only plan file only when complexity or later execution materially needs persistence
- one narrow substantive clarification about the work when objective, scope, or gate is not bounded enough

Ask about the work itself, not routing labels. Do not force trivial goals into durable plan files or pull broad governed context into trivial non-governed work.

A durable `Plan reference` is valid only after the route-only plan file exists in checked scope or was successfully written and verified in the same authoring flow. The copyable artifact starts with `/goal` and places `Plan reference: <exact path>` after it inside the same artifact. Never emit the reference from intention, draft text, or an unwritten file. If creation or verification is blocked, report the blocker instead of emitting a finished plan-backed goal.

### 5) Internal support remains subordinate
Internal analysis, route drafting, verification ordering, testing/log triage, and bounded helper lanes may support goal authoring when materially useful. They remain subordinate route support: not a second objective surface, independent authority, or completion proof.

When the same authoring flow can write and verify required durable route support, do not ask whether to save it and do not ask the user to invoke `/goal` again.

### 6) Authoring stop boundary
If the current turn is only goal or route-support authoring, stop at the final goal artifact plus subordinate route support. Do not append a default execution-style choice menu or begin execution unless execution is separately selected or clearly implied. Preserve internal routing labels only when workflow behavior itself or exact artifact wording is under discussion.

### 7) Candidate, advisory, and selected-goal boundaries
At a true completion or decision boundary, surface compact candidate goals when several materially different successors remain live. Promote at most one best-supported governed candidate into a copyable advisory `/goal`; other candidates may remain prose goals.

An advisory `/goal` remains unselected execution. If safe direct continuation already dominates, continue instead. Do not reduce approval-sensitive, destructive, or materially divergent work to `/goal`.

For a selected goal, keep route detail inside the goal-centric surface first. Open `/plan` only when sequence, task/phase breakdown, verification/owner ordering, explicit standalone planning, or route size no longer fits compactly.

`/goal` owns outcome, done condition, proof/checks, scope, and hard guardrails. `/plan` owns route, sequence, task breakdown, owner ordering, and overflow route detail. Repair route drift instead of letting `/plan` replace the selected objective. Route, helper, or plan completion never closes the goal while its proof or gate remains open.

### 8) Language and exact-literal boundary
Follow the dominant language of the active exchange unless the user explicitly chooses another. Preserve exact literals such as `/goal`, paths, version tags, identifiers, and query parameters; do not translate only the wrapper while leaving the goal body in another language.

### 9) Canonical copyable artifact
When durable route support is present, use this order inside one copied artifact:

```text
/goal <outcome + transcript-visible proof/checks + bounded scope + keep constraints + optional stop bound>
Plan reference: <exact route-only plan path>
```

Wrapper text may surround the artifact, but `Plan reference` must not precede `/goal` or become a detachable preface. Omit it when no verified durable plan file exists.

---

## Application Boundary

This rule is the sole semantic owner for governed `/goal` construction, route-support selection, durable plan-file lifecycle and `Plan reference`, internal authoring support, authoring stop, advisory promotion, selected-goal `/plan` overflow, goal-versus-route authority, and goal-artifact language/exact-literal rules.

Satellite rules retain only local mode-transition, task-materialization, topology, evidence-wording, tone, or rendering responsibilities. It does **not** replace phase/TODO task doctrine, execution continue/stop decisions, evidence wording, or presentation layout.

---

## Anti-Patterns

Avoid:
- emitting `Plan reference` for an unwritten or unchecked plan file
- placing `Plan reference` above `/goal` instead of after it inside the same copied artifact
- treating helper output or route drafts as objective authority
- appending `Subagent-Driven` / `Inline Execution` menus after pure goal/plan-file authoring
- forcing durable plan files for trivial or already direct goals
- teaching `/plan` as the default next surface for every route-heavy goal
- collapsing several materially different successor directions into one premature `/goal`
- treating route completion as goal completion
- pulling heavy governed context into trivial non-governed next steps

---

## Integration

Related owners:
- `phase-todo-artifact.md` — phase/TODO/live-task linkage to selected goals, task materialization, and execution surfaces
- `execution-and-goal-frame.md` — mode selection, continuation, stop gates, next-goal bridge, and selected execution posture
- `accurate-communication.md` — evidence-strength wording and status-ladder discipline
- `explanation-and-presentation.md` — copyable goal artifact shape, recommendation framing, and goal-centered presentation
