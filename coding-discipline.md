# Coding Discipline
> **Current Version:** 1.0
> **Design:** [design/coding-discipline.design.md](design/coding-discipline.design.md) v1.0
> **Session:** d42465eb-30a7-4bc8-b9d6-03e52306e9a5
> **Full history:** [changelog/coding-discipline.changelog.md](changelog/coding-discipline.changelog.md)
> **Absorbed:** maintainable-code-structure-and-decomposition v1.2, development-verification-and-debug-strategy v1.1, tactical-strategic-programming v1.3

---

## Rule Statement

**Core Principle: Code with maintainable structure, proportionate verification, and tactical-to-strategic convergence. Preserve responsibility clarity, decompose only when it lowers real change cost, carry a verification strategy before completion claims, and anchor tactical work to a declared strategic target with a visible convergence path.**

This rule covers coding-time responsibility, decomposition, helper-function necessity, source-code comment discipline, behavior-preserving refactor, verification strategy, debug signal selection, TestKit/scenario decisions, evidence-calibrated closeout, tactical entry, strategic target, convergence, and anti-drift posture.

พูดง่าย ๆ: เขียนโค้ดให้คนแก้ต่อได้ง่าย, พิสูจน์ได้ว่าของจริงใช้ได้แค่ไหน, และ tactical ต้องมีปลายทาง strategic ไม่ใช่ชั่วคราวถาวร.

---

## Part A — Maintainable Code Structure

### 1) Maintainability as change-cost
Maintainability means future readers can understand, test, modify, extend, or repair code with low surprise. Optimize for readable intent, clear responsibility, testability, and visible side effects. Treat shorter files, more helpers, or extra layers as useful only when they reduce real change cost. Separate current pressure from speculative futures.

### 2) Responsibility by reason-to-change
Group or split code by why it changes, not by a fixed template. Keep cohesive logic together when it changes for one reason; separate responsibilities that change for different reasons or are tested/owned differently. Inspect mixed business rules, orchestration, UI, persistence, integrations, validation, formatting, config, logging, and error handling. Reuse existing project structure when adequate.

### 3) Code smell as trigger, not verdict
Treat God function/file, long method, large class, helper inflation, shotgun surgery, divergent change, feature envy, primitive obsession, hidden dependency, comment spam, stale comments, and speculative generality as investigation signals. Do not refactor solely because a unit is long; do not extract helpers merely because extraction is possible. Decide from cohesion, coupling, change axes, testability, navigation cost, comment usefulness, and implementation risk. Preserve uncertainty when the right split is not yet clear.

### 4) Smallest useful decomposition
Choose the smallest structural move that improves real maintainability. Prefer clear local code before extraction when inline flow is easier to read. Extract a named local step only when the name adds meaning or test/side-effect boundaries. Split modules/files only when responsibilities or change axes materially differ. Add interfaces, factories, strategies, or plugin-like abstractions only when current evidence justifies variation or isolation. Keep navigation and call flow easier after the split, not harder. If a tactical direct edit is safest now, name the convergence path when material structure debt remains.

### 5) Helper-function necessity
Helper functions must earn their indirection cost. Extract when the name captures a real concept, business rule, process step, reusable behavior, testable unit, or side-effect boundary better than inline code. Do not create helpers for obvious expressions, trivial assignments, one-line wrappers, or simple sequential code clearer inline. Avoid pass-through helper chains and inline helpers whose body is as clear as the name. Single-use helpers are allowed only when the name materially clarifies intent, process, or boundary.

### 6) Wrong-abstraction guardrail
Duplication can be safer than coupling unrelated concepts behind a false shared abstraction. Do not merge code merely because it looks similar. Extract shared behavior only when the underlying concept and reason to change are genuinely shared. Prefer short-lived duplication over premature abstraction that makes future change harder. Remove or simplify speculative generality when it adds indirection without current value.

### 7) Explicit dependency and state-boundary
Make important dependencies and state flow visible enough to reason about. Avoid hidden global or ambient state when explicit dependency passing is reasonable. Bind config/environment at edges instead of scattering through domain logic. Separate pure transformation from side effects when it improves testing and clarity. Keep error handling and logging close to the boundary where they have operational meaning.

### 8) Appropriate source-code explanation
Names and structure explain normal flow first; comments explain what code cannot express clearly enough. Add concise comments for purpose, why, business rule, process order, constraint, side effect, external contract, compatibility workaround, security/performance/concurrency caveat, or operational consequence otherwise hard to understand. Avoid comments that repeat syntax, narrate every line, or compensate for unclear names/structure. Update or remove nearby comments when behavior changes; stale comments are worse than missing comments. Do not invent explanatory comments for behavior not verified from code, tests, docs, or user-provided requirements. Keep broad policy/spec/architecture authority in governed docs, not oversized source comments.

### 9) Behavior-preserving refactor
Refactoring should improve internal structure while preserving externally visible behavior unless behavior change is explicitly part of the task. Separate structural refactor from behavior change when practical. Use small transformations rather than broad rewrites when behavior risk is high. Run relevant tests, type checks, lint, or bounded verification when available. If verification is incomplete, report the limit instead of claiming the code is fixed, clean, or stable.

### 10) Decomposition Decision Gate
Before expanding or introducing a substantial function, file, module, class, helper, or abstraction:
- cohesive, small, one reason to change → keep local and clear
- obvious expression or trivial assignment → keep inline; do not extract a helper
- repeated named step inside one flow → extract only when the name improves understanding
- mixed responsibilities or different change reasons → split by responsibility/module boundary
- side-effect boundary mixed with pure logic → separate orchestration from pure transformation when useful
- same concept in multiple places → extract only when concept and reason to change match
- similar code with different business meaning → allow duplication until the real abstraction is clear
- non-obvious process/constraint/business rule/side effect → use a named helper and/or concise comment when it reduces cognitive load
- tactical shortcut → keep bounded and name convergence when debt is material
- abstraction for imagined future only → avoid, remove, or justify from current evidence

### 11) Helper Function Decision Gate
Before extracting a helper, answer:
1. Does the helper name express a real concept, rule, process step, reusable behavior, testable unit, or side-effect boundary better than the inline code?
2. Is the logic complex enough that a named step lowers cognitive load?
3. Is repeated logic genuinely the same concept and reason to change?
4. Does extraction improve testability, side-effect separation, or future change locality?
5. Does extraction avoid excessive parameter threading and call-chain hopping?
6. Would inline code be clearer?

If the inline form is clearer or the helper adds no semantic value, do not extract; keep the code local or inline the helper back.

### 12) Source-Code Comment Decision Gate
Before adding or leaving a comment, answer:
1. Does the comment explain purpose, why, process order, constraint, side effect, external contract, or business rule not obvious from code?
2. Would clearer naming, structure, or a better helper remove the need for this comment?
3. Is the comment still true after the change?
4. Is the comment concise enough to stay local rather than become durable documentation?
5. Is the behavior verified well enough to explain it?

If the comment repeats syntax, narrates obvious code, is stale, or belongs in governed docs, remove or rewrite it.

### 13) Smell Trigger Model

| Smell | Signals | Required response |
|---|---|---|
| God function / God file | too many concerns or change reasons in one unit | inspect whether orchestration, domain logic, validation, side effects, formatting, or ownership should split |
| Helper-function inflation | helpers add navigation cost without semantic value | inline trivial wrappers or keep cohesive logic local |
| Long method / large object | sequence or object responsibility hard to scan/verify | extract named steps or separate collaborators only when names/boundaries improve understanding |
| Divergent change / shotgun surgery | one axis touches too many places, or one unit changes for unrelated reasons | separate unrelated axes, or consolidate only a genuinely shared concept |
| Feature envy / primitive obsession | behavior or raw values live far from better owner | move logic toward the better owner or introduce a type/helper only when it reduces errors or clarifies behavior |
| Hidden dependency | behavior relies on global/ambient/implicit state | make dependency/state flow explicit where practical |
| Comment spam / stale comment | comments repeat syntax or no longer match behavior | remove noise, improve names/structure, or update verified explanation |
| Speculative generality | abstraction exists for a future not currently needed | simplify, defer, or justify from current evidence |

---

## Part B — Development Verification Strategy

### 1) Verification strategy as a coding default
Before or alongside non-trivial coding work, identify the behavior under change, the risk of being wrong, the debug signal that would show failure/success, and the smallest useful verification depth. Do not wait until after implementation to invent testing posture.
- classify whether the work changes behavior, structure only, integration, config/runtime behavior, data flow, security-sensitive behavior, or documentation/governance only
- choose verification depth from the actual behavior/risk/signal available, not from a rigid command template
- make the TestKit/scenario decision explicit when behavior is scenario-like, multi-step, integration-heavy, or safety-sensitive
- if verification is not applicable or not practical, state the narrow reason and preserve evidence limits
- do not claim fixed, working, stable, or release-ready from edits alone

### 2) Verification depth model
Use the smallest verification layer that gives meaningful signal.

| Work shape | Default verification posture |
|---|---|
| typo, docs-only, metadata-only, no behavior change | review or no test with reason |
| small pure logic or UI behavior change | unit or focused test when available |
| refactor intended to preserve behavior | existing focused/regression tests for the affected behavior |
| integration, adapter, API, database, queue, or event behavior | integration/fake-adapter/contract test when practical |
| multi-step user/system flow | scenario harness, TestKit, or equivalent workflow test |
| payment, auth, secrets, quota, runtime, provider, external dependency, or privacy-sensitive behavior | fake/local first plus explicit smoke/live decision and safety boundary |
| production/shared-state/destructive path | approval-sensitive verification gate plus rollback/containment owner |

Strategy, not ceremony. A stronger existing test may replace a new scenario; a scenario harness may replace fragile ad hoc checks; a live check remains conditional on user approval, safety, and environment readiness.

### 3) Debug strategy contract
For bug-fix, failure, flaky behavior, or complex integration work, keep a debug path visible enough to guide implementation.
- identify the observed failure or reproduction target when available
- state the working hypothesis without treating it as proven cause
- define the signal that would confirm the fix or invalidate the hypothesis
- prefer a failing test, focused reproduction, TestKit scenario, fixture, fake adapter, log/report, or failure injection when practical
- if reproduction is unavailable, state what evidence is missing and use bounded diagnostics rather than guessing

### 4) TestKit / scenario decision contract
For non-trivial coding work, select one verification route explicitly:
- `existing_test`: an existing focused/regression test covers the behavior
- `new_focused_test`: a small new test should be added
- `new_testkit_scenario`: a scenario/TestKit path should be added or extended
- `smoke_check`: a lightweight end-to-end or runtime check is appropriate
- `live_check_required`: live/provider/runtime verification is needed and approval/environment gating applies
- `not_applicable_with_reason`: no meaningful test applies, with a short reason

Do not create TestKit scenarios for every task by reflex. Do not skip the decision silently when behavior risk is material.

### 5) Evidence boundary and closeout discipline

| Evidence held | Acceptable status | Do not claim |
|---|---|---|
| checklist, plan, or artifact ready | prepared | implemented, tested, verified, live, fixed, stable |
| settings or wiring changed | configured | runtime/live-verified or working unless checked |
| source edited | implemented | fixed, verified, working |
| unit/focused tests passed | tested / verified-in-scope | whole system or live dependency works |
| fake/local TestKit scenario passed | fake/local verified-in-scope | real provider/runtime/deploy works |
| smoke check passed once | smoke-tested / runtime-checked once | stable over time |
| real provider/runtime/deploy checked | runtime/live-verified | stable unless repeated/time-based evidence supports it |
| failure scope reproduced and corrected with matching evidence | fixed in checked scope | globally stable or all edge cases covered |
| no test run | not tested | verified behavior |

Coding closeout should include the compact verification record when material:
```text
Verification:
- Ran: <commands/scenarios/checks or not run>
- Result: <passed/failed/not run>
- Covers: <behavior/scope>
- Does not cover: <live/provider/runtime/deploy/edge cases if material>
- Confidence: <evidence-calibrated wording>
```

### 6) Phase, TODO, and continuation behavior
For phase-backed coding work, phase records should show `Development Verification / TestKit Coverage` or equivalent when verification materially affects exit criteria. Live task lists should include or preserve a verification slice for non-trivial coding work when implementation and verification are distinct outcomes. Execution continuity should continue from implementation into verification when no real stop gate exists.

---

## Part C — Tactical/Strategic Programming

### Tactical entry
Tactical work is allowed when it materially improves startup speed, learning speed, or immediate execution. Keep it bounded and temporary unless explicitly promoted; do not require complete strategic design before useful implementation can begin.

### Strategic target
Every tactical move must point toward a declared strategic target. Identify the intended end-state before or alongside tactical execution; do not let local progress define the long-term direction by itself; do not proceed tactically when no strategic target can be named.

### Mandatory convergence
Every tactical path must show how it converges into strategic structure: absorbed, promoted, replaced, or retired; the future structure it converges into; and the trigger for strategic closure. Temporary structure must not remain indefinitely undefined.

### Bounded tactical scope
Tactical work must stay narrow enough to converge cleanly. Prefer local, reversible, low-blast-radius moves; do not let tactical entry silently expand into broad unplanned architecture; do not let machine-local paths, hosts, or install assumptions become defaults unless explicitly machine-scoped. Broader portable-default and anti-hardcoding ownership defers to `portable-implementation-and-hardcoding-control.md`.

### No permanent tactical drift
Temporary solutions must not become hidden long-term authority. Workarounds, patch stacks, bridges, or compatibility paths require retirement, absorption, or formal promotion when they persist; detect and call out drift early.

### Strategic closure
Non-trivial systems should end in strategic structure. Stable boundaries, roles, and sequencing belong in strategic authority; design and phase layers should absorb validated tactical learning; final authority should not live in leftover tactical fragments.

### Classification and Decision Model

| Mode | Meaning | Typical use |
|---|---|---|
| `TACTICAL` | local bounded execution slice | patch artifact, focused fix, immediate unblock |
| `STRATEGIC` | directional/architectural planning layer | design, roadmap, phased execution, boundary setting |
| `TACTICAL_WITH_STRATEGIC_TRACK` | tactical execution with target and convergence path | fast-start implementation under strategic control |

Before non-trivial tactical execution, answer:
1. Is this tactical, strategic, or tactical-with-strategic-track?
2. What is the strategic target?
3. What is the tactical slice now?
4. How does it converge?
5. What triggers promotion to strategic closure?

If answers 2-5 are unclear, clarify strategy before tactical execution.

### Artifact Map

| Artifact type | Default role |
|---|---|
| `design/*.design.md` | strategic target-state authority |
| `phase/SUMMARY.md` + child phase files | strategic execution program |
| `patch/<context>.patch.md` or root `<context>.patch.md` | tactical change artifact |
| `TODO.md` | tactical execution tracking |
| runtime temporary workaround | tactical implementation device |
| stable architecture authority | strategic end-state |

### Communication Shape
When this doctrine materially matters, make these meanings visible: **Strategic target**, **Tactical now**, **Why tactical first**, **Convergence path**, and **Strategic end-state**. Equivalent headings acceptable if the meaning stays explicit.

---

## Trigger Model

| Trigger | Required behavior |
|---|---|
| non-trivial coding feature | choose verification depth and TestKit/scenario decision before closeout |
| bug/debug request | define observed failure/reproduction, hypothesis, signal, fix, and regression check when practical |
| refactor | preserve behavior and rerun affected tests or state verification limits |
| integration/provider/runtime/payment/auth/privacy work | fake/local verification first, then explicit smoke/live decision and safety boundary |
| scenario-like flow | prefer TestKit/scenario harness or explain why focused tests are stronger |
| implementation completed but not tested | continue to verification when safe instead of stopping at edit-only progress |
| checklist/config/scaffold readiness | report prepared/configured/implemented only; do not claim tested, verified, live, fixed, or stable without matching evidence |
| trivial no-behavior change | avoid ceremony; mark test not applicable with reason when needed |
| broad/growing function/file | inspect for God/responsibility split before continuing to grow |
| fast local fix in unclear terrain | allow only with strategic target and convergence path |
| patch accumulation | check for tactical drift and promotion need |
| phase/roadmap planning | let strategic framing dominate |
| temporary runtime structure | require retirement or absorption path |
| architecture still emerging | use `TACTICAL_WITH_STRATEGIC_TRACK` |
| long-lived workaround | require promotion, retirement, or replacement |
| tactical fix changes code structure | preserve responsibility clarity, avoid avoidable God function/file drift, name convergence if material debt remains |

---

## Anti-Patterns

Avoid:
- fixed line-count policing, template-first architecture, splitting every function into tiny fragments
- helper wrappers for obvious expressions, pass-through helper chains
- interfaces/factories/strategies for one current use, merging coincidental duplication
- refactor-plus-behavior-change without a boundary, rewriting a whole file for one smell
- syntax-narrating comments, stale comments
- local tactical patches that become hidden permanent structure
- edit-only completion, testing as an afterthought, mandatory TestKit creation for trivial work
- fake/local pass presented as live proof, refactor without behavior-preservation checks
- debugging from guesses without a signal, adding tests that do not cover the changed behavior
- running broad/noisy tests without worker filtering when appropriate
- reporting fixed/stable beyond checked evidence
- tactical entry without a declared strategic target or convergence path

Better behavior: identify responsibility, choose the smallest useful structural move, understand behavior, choose a proportionate verification route, preserve not-tested scope, report evidence at the correct strength, and anchor tactical work to a declared strategic target.

---

## AI Coding Workflow

When this rule materially applies:
1. identify responsibility and reason-to-change boundaries before editing
2. inspect existing project structure and reuse it when adequate
3. classify the work as tactical, strategic, or tactical-with-strategic-track
4. identify the strategic target and convergence path when tactical
5. choose the smallest useful structural move
6. keep cohesive code together and split mixed responsibilities deliberately
7. avoid helper inflation, speculative abstractions, and wrong DRY extractions
8. add or update concise comments only for useful purpose/process/boundary information
9. identify behavior under change, risk, debug signal, and verification depth
10. make the TestKit/scenario decision explicit when material
11. preserve behavior during refactor unless behavior change is explicit
12. run proportionate checks; report verification limits honestly
13. report edited/tested/fake-local/live/fixed/stable wording at correct evidence strength
14. name tactical convergence when material structure debt remains

---

## Integration

Related rules:
- [accurate-communication.md](accurate-communication.md) - evidence-strength wording for edited/tested/fixed/stable claims
- [phase-todo-artifact.md](phase-todo-artifact.md) - phase-backed verification and closeout surfaces
- [phase-todo-artifact.md](phase-todo-artifact.md) - live task-list verification slices
- [execution-and-goal-frame.md](execution-and-goal-frame.md) - continue from implementation into verification when safe
- [worker-routing-and-context.md](worker-routing-and-context.md) - worker filtering for broad/noisy test/log output
- [action-safety.md](action-safety.md) - runtime mutation and live/smoke verification gates
- [document-governance.md](document-governance.md) - tactical patch artifacts
- [document-governance.md](document-governance.md) - document roles and durable docs beyond source comments
- [portable-implementation-and-hardcoding-control.md](portable-implementation-and-hardcoding-control.md) - portable/environment binding
- [execution-and-goal-frame.md](execution-and-goal-frame.md) - structure-first balance against objectives
- [explanation-and-presentation.md](explanation-and-presentation.md) - assistant response explanations (source comments owned here)
- [evidence-discipline.md](evidence-discipline.md) - maintainability claim calibration
