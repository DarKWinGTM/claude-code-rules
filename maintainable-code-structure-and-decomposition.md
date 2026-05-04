# Maintainable Code Structure and Decomposition
> **Current Version:** 1.1
> **Design:** [design/maintainable-code-structure-and-decomposition.design.md](design/maintainable-code-structure-and-decomposition.design.md) v1.1
> **Session:** d42465eb-30a7-4bc8-b9d6-03e52306e9a5
> **Full history:** [changelog/maintainable-code-structure-and-decomposition.changelog.md](changelog/maintainable-code-structure-and-decomposition.changelog.md)
---
## Rule Statement
**Core Principle: During coding and refactoring, preserve maintainable code structure by assigning responsibilities clearly, decomposing only when it lowers real change cost, avoiding helper-function inflation and wrong abstractions, making important dependencies visible, using source comments for non-obvious purpose or constraints, and preserving behavior unless behavior change is explicit.**
This rule owns coding-time responsibility boundaries, smell-triggered decomposition, smallest-useful-structure decisions, helper-function necessity, source-code comment discipline, anti-overengineering guardrails, and behavior-preserving refactor posture. It does not replace tactical/strategic convergence, project-specific architecture, testing ownership, evidence wording, durable project documentation, or user-directed implementation choices.
---
## Scope Boundary
Apply this rule when writing, modifying, reviewing, or refactoring code whose structure can affect future readability, testing, extension, repair, or blast radius.

Use it strongly for broad or growing functions/files, mixed concerns, refactors, tactical fixes that may persist, generated code that may be hard to maintain, helper chains that add navigation cost, or source comments that are missing, excessive, stale, or syntax-repeating.

Do not use it to force ceremony for trivial local changes, one-off scripts, cohesive small functions, adequate project patterns, or user-directed tactical work with an accepted convergence path.

พูดง่าย ๆ: AI ควรเขียนโค้ดให้คนแก้ต่อได้ง่าย แต่ไม่ใช่แตก helper ทุกอย่างหรือใส่ comment ทุกบรรทัดเพื่อให้ดูเหมือน clean code.
---
## Core Contract
### 1) Maintainability as change-cost principle
Maintainability means people can understand, test, modify, extend, or repair code later with low surprise and bounded side effects.

Required guidance:
- optimize for readable intent, clear responsibility, testability, and visible side effects
- treat shorter files, more helpers, or extra layers as useful only when they reduce real change cost
- separate current maintainability pressure from speculative future possibilities

### 2) Responsibility-by-reason-to-change principle
Group or split code by why it changes, not by a fixed template.

Required guidance:
- keep cohesive logic together when it changes for one reason
- separate responsibilities that change for different reasons or are tested/owned differently
- inspect mixed business rules, orchestration, UI, persistence, integrations, validation, formatting, config, logging, and error handling
- reuse existing project structure when it remains adequate

### 3) Code smell as trigger, not verdict
Code smells are reasons to inspect structure, not automatic refactor commands.

Required guidance:
- treat God function/file, long method, large class, helper inflation, shotgun surgery, divergent change, feature envy, primitive obsession, hidden dependency, comment spam, stale comments, and speculative generality as investigation signals
- do not refactor solely because a unit is long, and do not extract helpers merely because extraction is possible
- decide from cohesion, coupling, change axes, testability, navigation cost, comment usefulness, and implementation risk
- preserve uncertainty when the smell is suggestive but the right split is not yet clear

### 4) Smallest useful decomposition principle
Choose the smallest structural move that improves real maintainability.

Required guidance:
- prefer clear local code before extraction when inline flow is easier to read
- extract a named local step only when the name adds meaning or test/side-effect boundaries
- split modules/files only when responsibilities or change axes materially differ
- add interfaces, factories, strategies, or plugin-like abstractions only when current evidence justifies variation or isolation
- keep navigation and call flow easier after the split, not harder
- if a tactical direct edit is safest now, name the convergence path when material structure debt remains

### 5) Helper-function necessity principle
Helper functions must earn their indirection cost.

Required guidance:
- extract a helper when its name captures a real concept, business rule, process step, reusable behavior, testable unit, or side-effect boundary better than inline code
- do not create helpers for obvious expressions, trivial assignments, one-line wrappers, or simple sequential code that is clearer inline
- avoid pass-through helper chains and inline helpers whose body is as clear as the name
- single-use helpers are allowed only when the name materially clarifies intent, process, or boundary

### 6) Wrong-abstraction guardrail
Duplication can be safer than coupling unrelated concepts behind a false shared abstraction.

Required guidance:
- do not merge code merely because it looks similar
- extract shared behavior only when the underlying concept and reason to change are genuinely shared
- prefer short-lived duplication over premature abstraction that makes future change harder
- remove or simplify speculative generality when it adds indirection without current value

### 7) Explicit dependency and state-boundary principle
Make important dependencies and state flow visible enough to reason about.

Required guidance:
- avoid hidden global or ambient state when explicit dependency passing is reasonable
- bind config/environment at edges instead of scattering it through domain logic
- separate pure transformation from side effects when it improves testing and clarity
- keep error handling and logging close enough to the boundary where they have operational meaning

### 8) Appropriate source-code explanation principle
Names and structure should explain normal flow first; comments explain what code cannot express clearly enough.

Required guidance:
- add concise comments for purpose, why, business rule, process order, constraint, side effect, external contract, compatibility workaround, security/performance/concurrency caveat, or operational consequence that would otherwise be hard to understand
- avoid comments that repeat syntax, narrate every line, or compensate for unclear names/structure
- update or remove nearby comments when behavior changes; stale comments are worse than missing comments
- do not invent explanatory comments for behavior not verified from code, tests, docs, or user-provided requirements
- keep broad policy/spec/architecture authority in governed docs, not oversized source comments

### 9) Behavior-preserving refactor principle
Refactoring should improve internal structure while preserving externally visible behavior unless behavior change is explicitly part of the task.

Required guidance:
- separate structural refactor from behavior change when practical
- use small transformations rather than broad rewrites when behavior risk is high
- run relevant tests, type checks, lint, or bounded verification when available
- if verification is incomplete, report the limit instead of claiming the code is fixed, clean, or stable

### 10) Tactical/strategic integration principle
This rule shapes code structure; `tactical-strategic-programming.md` shapes tactical entry and strategic convergence.

Required guidance:
- tactical fixes may stay local but should not worsen God-file, God-function, helper-inflation, or stale-comment drift without a reason
- if tactical work leaves structure or explanation debt, state whether it will be absorbed, promoted, replaced, or retired later
- strategic work should turn validated tactical learning into stable responsibility and explanation boundaries
---
## Decomposition Decision Gate
Before expanding or introducing a substantial function, file, module, class, helper, or abstraction, choose the smallest fitting structure:
- cohesive, small, one reason to change -> keep local and clear
- obvious expression or trivial assignment -> keep inline; do not extract a helper
- repeated named step inside one flow -> extract only when the name improves understanding
- mixed responsibilities or different change reasons -> split by responsibility/module boundary
- side-effect boundary mixed with pure logic -> separate orchestration from pure transformation when useful
- same concept in multiple places -> extract only when concept and reason to change match
- similar code with different business meaning -> allow duplication until the real abstraction is clear
- non-obvious process, constraint, business rule, or side effect -> use a named helper and/or concise comment when it reduces cognitive load
- tactical shortcut -> keep bounded and name convergence when debt is material
- abstraction for imagined future only -> avoid, remove, or justify from current evidence

## Helper Function Decision Gate
Before extracting a helper, answer:
1. Does the helper name express a real concept, rule, process step, reusable behavior, testable unit, or side-effect boundary better than the inline code?
2. Is the logic complex enough that a named step lowers cognitive load?
3. Is repeated logic genuinely the same concept and reason to change?
4. Does extraction improve testability, side-effect separation, or future change locality?
5. Does extraction avoid excessive parameter threading and call-chain hopping?
6. Would inline code be clearer?

If the inline form is clearer or the helper adds no semantic value, do not extract it; keep the code local or inline the helper back.

## Source-Code Comment Decision Gate
Before adding or leaving a comment, answer:
1. Does the comment explain purpose, why, process order, constraint, side effect, external contract, or business rule not obvious from code?
2. Would clearer naming, structure, or a better helper remove the need for this comment?
3. Is the comment still true after the change?
4. Is the comment concise enough to stay local rather than become durable documentation?
5. Is the behavior verified well enough to explain it?

If the comment repeats syntax, narrates obvious code, is stale, or belongs in governed docs, remove or rewrite it.
---
## Smell Trigger Model
Code smells are inspection prompts, not verdicts. Use them to decide whether responsibility, cohesion, coupling, or explanation pressure justifies a structural move.

| Smell | What it signals | Required response |
|---|---|---|
| God function / God file | one unit may own too many concerns or change reasons | inspect whether orchestration, domain logic, validation, side effects, formatting, or ownership should split |
| Helper-function inflation | helpers add navigation cost without semantic value | inline trivial wrappers or keep cohesive logic local |
| Long method / large object | sequence or object responsibility may be hard to scan or verify | extract named steps or separate collaborators only when names/boundaries improve understanding |
| Divergent change / shotgun surgery | one change axis touches too many places, or one unit changes for unrelated reasons | separate unrelated axes, or consolidate only a genuinely shared concept |
| Feature envy / primitive obsession | behavior or raw values may live far from the better owner | move logic toward the better owner or introduce a type/helper only when it reduces errors or clarifies behavior |
| Hidden dependency | behavior relies on global, ambient, or implicit state | make dependency/state flow explicit where practical |
| Comment spam / stale comment | comments repeat syntax or no longer match behavior | remove noise, improve names/structure, or update verified explanation |
| Speculative generality | abstraction exists for a future not currently needed | simplify, defer, or justify from current evidence |
---
## Anti-Patterns
Avoid fixed line-count policing, template-first architecture, splitting every function into tiny fragments, helper wrappers for obvious expressions, pass-through helper chains, interfaces/factories/strategies for one current use, merging coincidental duplication, refactor-plus-behavior-change without a boundary, rewriting a whole file for one smell, syntax-narrating comments, stale comments, and local tactical patches that become hidden permanent structure.
---
## AI Coding Workflow and Verification
When this rule materially applies:
1. identify responsibility and reason-to-change boundaries before editing
2. inspect existing project structure and reuse it when adequate
3. choose the smallest useful structural move
4. keep cohesive code together and split mixed responsibilities deliberately
5. avoid helper inflation, speculative abstractions, and wrong DRY extractions
6. add or update concise comments only for useful purpose/process/boundary information
7. preserve behavior during refactor unless behavior change is explicit
8. verify with relevant checks when available and report limits honestly

Verification checklist:
- [ ] responsibilities and reasons to change are clear
- [ ] God function/file pressure is reduced or not worsened without reason
- [ ] decomposition uses the smallest useful structure and avoids wrong abstractions
- [ ] cohesion stays strong; coupling does not increase unnecessarily
- [ ] helpers earn their indirection cost
- [ ] dependencies, state flow, and useful source comments are clear enough to test/reason about
- [ ] refactors preserve behavior unless behavior change is explicit
- [ ] relevant checks, verification limits, and tactical convergence debt are reported
---
## Quality Metrics
Quality target: high responsibility clarity, smell-triggered judgment, smallest-useful decomposition, useful source comments, behavior preservation, and verification honesty; low helper inflation, wrong abstractions, hidden dependencies, and God function/file drift.
---
## Integration
Related rules:
- [tactical-strategic-programming.md](tactical-strategic-programming.md) - owns tactical entry, strategic target, and convergence path
- [goal-set-review-and-priority-balance.md](goal-set-review-and-priority-balance.md) - keeps structure-first work balanced against the full objective set
- [portable-implementation-and-hardcoding-control.md](portable-implementation-and-hardcoding-control.md) - owns portable/environment binding beyond local structure decisions
- [project-documentation-standards.md](project-documentation-standards.md) - governs durable docs when source comments are not enough
- [explanation-quality.md](explanation-quality.md) - owns assistant response explanations; this rule owns source-code comment discipline
- [evidence-grounded-burden-of-proof.md](evidence-grounded-burden-of-proof.md) - keeps maintainability claims evidence-calibrated
- [accurate-communication.md](accurate-communication.md) - keeps edited/tested/fixed/stable wording evidence-aligned
---
> **Full history:** [changelog/maintainable-code-structure-and-decomposition.changelog.md](changelog/maintainable-code-structure-and-decomposition.changelog.md)
