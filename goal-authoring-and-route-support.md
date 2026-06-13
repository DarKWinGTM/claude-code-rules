# Goal Authoring and Route Support
> **Current Version:** 1.0
> **Design:** [design/goal-authoring-and-route-support.design.md](design/goal-authoring-and-route-support.design.md) v1.0
> **Session:** 8b04beb0-b5ef-4500-a3f5-558bcedd088a
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

### 4) Choose the smallest sufficient route support
Select route support proportionally:
- direct `/goal` wording for simple bounded objectives
- compact non-durable route notes when ordering matters but fits inside the goal-centric surface
- durable route-only plan file only when route complexity or later execution needs persistence
- one narrow substantive clarification when objective, scope, or gate is still not bounded enough

Required guidance:
- ask about the work itself, not routing labels such as `Subagent-Driven`, `Inline Execution`, `/plan`, or `goal plan file`
- trivial or already direct goals should stay lightweight and must not be forced into durable plan files
- do not pull heavy governed-surface context into trivial non-governed next steps

### 5) Durable `Plan reference` contract
Durable route support must be a route-only plan file that already exists in checked scope or was successfully written in the same governed authoring flow.

Required guidance:
- never emit `Plan reference` from intention, draft text, or an unwritten file
- the copied goal artifact must show `/goal` first and `Plan reference: <exact path>` after it inside the same artifact
- do not place `Plan reference` above the command as a detachable preface
- the plan file remains route support only and must not become objective authority or completion proof
- if the plan write/verify step is blocked, report that blocker instead of implying a finished plan-backed goal

### 6) Internal planning/helper support stays subordinate
Governed `/goal` authoring may use internal planning or helper support when route complexity materially justifies it.

Allowed support shapes include:
- analysis support
- route drafting
- verification ordering
- test/log triage
- `Plan draft`
- `Verification / testing route`
- plan basis

Required guidance:
- helper output remains subordinate route support for the goal
- helper output must not become a second public objective surface
- helper output must not become completion proof by itself
- do not ask whether to save a plan when the same authoring flow can write/verify it directly
- do not ask the user to invoke `/goal` again when no real stop gate exists

### 7) Authoring stop boundary
If the current turn is only goal or plan-file authoring, stop at the final goal artifact plus subordinate route support.

Required guidance:
- do not append default execution-style choice menus after authoring
- do not auto-open execution-style follow-up unless execution is already selected or clearly implied by stronger checked context
- preserve exact internal routing labels only when governance/workflow behavior itself is under discussion or exact copied artifact wording materially requires them

### 8) Advisory `/goal` suggestion boundary
After a true completion boundary, the assistant may promote one bounded governed successor into an advisory `/goal` command instead of leaving it only as prose.

Use this only when all conditions hold:
- one successor objective is singular enough that a single command will not hide a real multi-path decision surface
- the candidate is already the best-supported successor rather than one of several still-undifferentiated options
- the completion condition fits within a compact goal artifact
- proof/check basis can be surfaced in the conversation
- suggesting `/goal` is more useful than directly continuing the current execution path

Required guidance:
- keep `/goal` suggestions advisory, not selected execution
- if safe direct continuation already exists, continue directly rather than pausing only to emit `/goal`
- if the next step is approval-sensitive, destructive, or materially divergent, do not reduce it to `/goal`

### 9) Selected goal overflow and `/plan` boundary
When a goal is already selected, keep route detail inside the goal-centric surface first.

Open `/plan` only when:
- route selection no longer fits safely in the selected goal surface
- sequence or execution order needs a standalone route surface
- phase/lane breakdown or task breakdown no longer fits compactly
- verification ordering or owner ordering needs explicit standalone handling
- the user explicitly asks for standalone planning

Required guidance:
- do not teach `/plan` as the ordinary paired next surface for every route-heavy goal
- if compact route notes are enough, keep them inside the selected goal surface
- if the route in `/plan` drifts from the selected goal, repair the route or revisit the goal basis instead of silently treating `/plan` as new authority
- completed plan steps do not close the goal while goal proof/gate remains open

### 10) Goal-vs-plan authority split
Keep these meanings separate:
- `/goal` owns outcome, done condition, proof/checks, scope, and hard guardrails
- `/plan` owns route, sequence, task breakdown, owner ordering, and overflow route detail only when needed

Required guidance:
- do not let route support read like objective ownership
- do not let plan completion read like goal completion
- when both surfaces are mentioned together, make it visible whether the status being reported is objective status or route status

### 11) Candidate goals before one promoted `/goal`
When several meaningful successor directions remain live, surface compact candidate goals first.

Required guidance:
- preserve the real decision surface instead of collapsing it too early into one path
- promote only one best-supported governed candidate into a copyable `/goal` artifact
- other candidate goals may remain prose goals rather than command blocks

### 12) Language and exact-literal boundary
For goal artifacts and surrounding route-support wording:
- follow the dominant language of the active exchange by default
- let explicit user language requests override that default
- preserve exact literals such as `/goal`, file paths, version tags, identifiers, and query parameters when they should remain exact
- do not translate only the wrapper while leaving the goal body in another language except for preserved literals

---

## Application Boundary

This rule is the canonical runtime owner for:
- governed `/goal` authoring
- route-only plan support
- `Plan reference` formatting/validity
- internal planning support inside governed goal authoring
- selected-goal overflow handling into `/plan`
- advisory `/goal` promotion conditions

It does **not** replace:
- phase/TODO/live-task doctrine (`phase-todo-artifact.md`)
- discussion vs execution / continue vs stop / next-goal decision boundaries (`execution-and-goal-frame.md`)
- evidence-strength wording (`accurate-communication.md`)
- closing/presentation behavior (`explanation-and-presentation.md`)

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
