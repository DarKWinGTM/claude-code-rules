# Maintainable Code Structure and Decomposition
> **Current Version:** 1.1
> **Design:** [design/maintainable-code-structure-and-decomposition.design.md](design/maintainable-code-structure-and-decomposition.design.md) v1.1
> **Session:** d42465eb-30a7-4bc8-b9d6-03e52306e9a5
> **Full history:** [changelog/maintainable-code-structure-and-decomposition.changelog.md](changelog/maintainable-code-structure-and-decomposition.changelog.md)
---
## Rule Statement
**Core Principle: During coding and refactoring, preserve maintainable code structure by assigning responsibilities clearly, decomposing only when it improves real changeability, avoiding unnecessary helper-function inflation, adding appropriate source-code explanation, and preventing unnecessary God functions, God files, hidden dependencies, and wrong abstractions without enforcing rigid line-count or architecture-template rules.**
This rule owns coding-time responsibility boundaries, smell-triggered decomposition, smallest-useful-structure decisions, helper-function necessity, source-code comment discipline, anti-overengineering guardrails, and behavior-preserving refactor posture. It does not replace tactical/strategic convergence, project-specific architecture, testing ownership, evidence wording, durable project documentation, or user-directed implementation choices.
---
## Scope Boundary
Apply this rule when writing, modifying, reviewing, or refactoring code and the structure of a function, file, module, component, class, route, service, script, or helper can affect future readability, testability, or change cost.

Use it strongly when work touches:
- broad or growing functions/files
- mixed business logic, UI/presentation, persistence, integration, validation, formatting, config, logging, or orchestration concerns
- refactors that claim to improve structure
- tactical fixes that could become permanent architecture
- generated code that may pass locally but be hard to maintain
- helper chains that add navigation cost without clearer intent
- source-code comments that are missing, excessive, stale, or only repeat syntax

Do not use this rule to force ceremony for trivial local changes, one-off scripts, cohesive small functions, project patterns that are already clear and adequate, or user-directed tactical changes where a later convergence path is explicitly accepted.

พูดง่าย ๆ: AI ควรเขียนโค้ดให้คนแก้ต่อได้ง่าย แต่ไม่ใช่แตก helper ทุกอย่างหรือใส่ comment ทุกบรรทัดเพื่อให้ดูเหมือน clean code.
---
## Core Contract
### 1) Maintainability as change-cost principle
Treat maintainability as the ability to understand, test, modify, extend, or repair the code later with low surprise and bounded blast radius.
Required guidance:
- prefer structure that makes future changes easier to locate and verify
- optimize for readable intent, clear responsibility, testability, and bounded side effects
- do not treat visual neatness, shorter files, more helpers, or more layers as maintainability proof by themselves
- distinguish current maintainability pressure from speculative future possibilities
### 2) Responsibility-by-reason-to-change principle
Group or separate code by why it changes, not by a fixed template.
Required guidance:
- keep cohesive logic together when it changes for one reason
- separate concerns that change for different reasons or are tested/owned differently
- watch for mixed business rules, orchestration, UI, persistence, external integration, validation, formatting, logging, config, and error-handling responsibilities
- use existing project structure first when it remains adequate
### 3) Code smell as trigger, not verdict
Code smells are investigation triggers, not automatic refactor commands.
Required guidance:
- treat God function, God file, long method, large class, helper-function inflation, shotgun surgery, divergent change, feature envy, primitive obsession, hidden dependency, comment spam, stale comments, and speculative generality as reasons to inspect structure
- do not refactor solely because a file or function is long
- do not extract helpers solely because inline code can be extracted
- decide from cohesion, coupling, change axes, testability, navigation cost, comment usefulness, and implementation risk
- preserve uncertainty when the smell is suggestive but the right split is not yet clear
### 4) Smallest useful decomposition principle
Choose the smallest structural move that improves real maintainability.
Required guidance:
- prefer clear local code before extraction when inline flow is easier to read
- prefer clear local extraction before new layers when a named step adds real meaning
- split modules/files only when responsibilities or change axes are materially different
- introduce interfaces, factories, strategies, or plugin-like abstractions only when current evidence justifies them
- keep navigation and call flow easier after the split, not harder
- if a tactical direct edit is safest now, name the convergence path when structure debt remains material
### 5) Helper-function necessity principle
Helper functions must earn their indirection cost.
Required guidance:
- extract a helper when its name captures a real concept, business rule, process step, reusable behavior, testable unit, or side-effect boundary better than inline code
- do not create helpers for obvious expressions, trivial assignments, one-line wrappers, or simple sequential code that is clearer inline
- avoid pass-through helper chains that make readers jump across functions without adding meaning
- inline or fold back helpers whose body is as clear as the name and whose existence adds navigation cost
- single-use helpers are allowed only when the name materially clarifies intent, process, or boundary
### 6) Wrong-abstraction guardrail
Duplication can be safer than coupling unrelated concepts behind a false shared abstraction.
Required guidance:
- do not merge code merely because it looks similar
- extract shared behavior only when the underlying concept and reason to change are genuinely shared
- prefer short-lived duplication over a premature abstraction that makes future change harder
- remove or simplify speculative generality when it adds indirection without current value
### 7) Explicit dependency and state-boundary principle
Make important dependencies and state flow visible enough to reason about.
Required guidance:
- avoid hidden global or ambient state when explicit dependency passing is reasonable
- keep config/environment binding near the edge instead of scattered through domain logic
- separate pure transformation logic from side effects when that improves testing and clarity
- keep error handling and logging close enough to the boundary where they have operational meaning
### 8) Appropriate source-code explanation principle
Names and structure should explain normal flow first; comments explain what code cannot express clearly enough.
Required guidance:
- add concise comments when purpose, why, business rule, process order, constraint, side effect, external contract, compatibility workaround, security/performance/concurrency caveat, or operational consequence would otherwise be hard to understand
- avoid comments that merely repeat syntax, narrate every line, or compensate for unclear names and structure that should be improved instead
- update or remove nearby comments when code behavior changes; stale comments are worse than missing comments
- do not invent explanatory comments for behavior that has not been verified from code, tests, docs, or user-provided requirements
- keep durable policy/spec/architecture authority in governed docs when a comment would become too broad or long-lived as source truth
### 9) Behavior-preserving refactor principle
Refactoring should improve internal structure while preserving externally visible behavior unless a behavior change is explicitly part of the task.
Required guidance:
- separate structural refactor from behavior change when practical
- use small transformations rather than broad rewrites when behavior risk is high
- run relevant tests, type checks, lint, or bounded verification when available
- if verification is incomplete, report the limit instead of claiming the code is fixed, clean, or stable
### 10) Tactical/strategic integration principle
This rule shapes code structure; `tactical-strategic-programming.md` shapes tactical entry and strategic convergence.
Required guidance:
- tactical fixes may stay local, but should not worsen God-file, God-function, helper-inflation, or stale-comment drift without a reason
- if a tactical slice leaves structure or explanation debt, state whether it will be absorbed, promoted, replaced, or retired later
- strategic work should use this rule to define stable responsibility and explanation boundaries rather than accumulating tactical fragments
---
## Decomposition Decision Gate
Before expanding or introducing a substantial function, file, module, class, helper, or abstraction, decide the smallest fitting structure:

| Situation | Preferred action |
|---|---|
| cohesive, small, one reason to change | keep local and clear |
| obvious expression or trivial assignment | keep inline; do not extract a helper |
| repeated named step inside one flow | extract a helper/function when the name improves understanding |
| helper name adds no meaning beyond the body | inline or keep the logic local |
| mixed responsibilities with different change reasons | split by responsibility or module boundary |
| side-effect boundary mixed with pure logic | separate boundary orchestration from pure transformation when useful |
| same concept appears in multiple places | extract shared behavior if concept and change reason match |
| similar code with different business meaning | allow duplication until the real abstraction is clear |
| non-obvious process, constraint, business rule, or side effect | use a named helper and/or concise comment when it reduces cognitive load |
| tactical shortcut needed now | keep bounded and name convergence path when debt is material |
| abstraction added only for imagined future | avoid or remove speculative layer |
---
## Helper Function Decision Gate
Before extracting a helper, answer:
1. Does the helper name express a real concept, rule, process step, or boundary better than the inline code?
2. Is the logic complex enough that a named step lowers cognitive load?
3. Is repeated logic genuinely the same concept and reason to change?
4. Does extraction improve testability, side-effect separation, or future change locality?
5. Does extraction avoid excessive parameter threading and call-chain hopping?
6. Would inline code be clearer?
If the inline form is clearer and the helper adds no semantic value, do not extract or inline the helper back.
---
## Source-Code Comment Decision Gate
Before adding or leaving a comment, answer:
1. Does the comment explain purpose, why, process order, constraint, side effect, external contract, or business rule not obvious from code?
2. Would clearer naming, structure, or a better helper remove the need for this comment?
3. Is the comment still true after the change?
4. Is the comment concise enough to stay local rather than become durable documentation?
5. Is the behavior verified well enough to explain it?
If the comment repeats syntax, narrates obvious code, or is stale, remove or rewrite it.
---
## Smell Trigger Model
| Smell | What it signals | Required response |
|---|---|---|
| God function | one function owns many concerns or change reasons | inspect whether orchestration, domain logic, validation, side effects, or formatting should split |
| God file | one file accumulates unrelated responsibilities | split only along real responsibility/change boundaries |
| Helper-function inflation | many helpers exist without semantic value or force unnecessary call-chain hopping | inline trivial helpers or keep cohesive logic local |
| Long method | sequence is hard to scan or verify | extract named steps only when names improve flow understanding |
| Large class/object | object changes for several unrelated reasons | separate collaborators or responsibilities when cohesion is low |
| Divergent change | one unit changes for unrelated feature families | separate by reason to change |
| Shotgun surgery | one small concept change touches many places | consolidate the concept if it is genuinely one concept |
| Feature envy | behavior lives far from the data/capability it mostly uses | move logic toward the better owner when project structure supports it |
| Primitive obsession | raw strings/dicts/numbers hide domain meaning | introduce type/helper/value object only when it reduces errors or clarifies behavior |
| Hidden dependency | behavior relies on global, ambient, or implicit state | make dependency explicit where practical |
| Comment spam | comments repeat syntax or narrate every line | delete noise and improve names/structure instead |
| Stale or misleading comment | comment claims behavior no longer true | update, remove, or verify before relying on it |
| Speculative generality | abstraction exists for a future not currently needed | simplify, defer, or justify from current evidence |
---
## Anti-Patterns
| Anti-pattern | Better behavior |
|---|---|
| fixed line-count policing | use length as a smell trigger, not a verdict |
| template-first architecture | follow project fit and responsibility pressure before adding layers |
| splitting every function into tiny fragments | split only when names and boundaries improve understanding |
| helper function for every obvious expression | keep simple local code inline |
| pass-through helper chains | inline or collapse wrappers that add no meaning |
| creating interfaces/factories/strategies for one current use | wait for real variation or clear test/ownership benefit |
| merging coincidental duplication | preserve duplication until shared concept is real |
| refactor plus behavior change with no boundary | separate or explicitly state why both are bundled |
| rewriting a whole file to fix one smell | prefer smallest behavior-preserving improvement |
| comments repeat syntax or narrate every line | explain why/process/boundary or remove the comment |
| stale comments left after behavior changes | update or remove comments in the same change |
| local tactical patch becomes hidden permanent structure | add convergence path or promote deliberately |
---
## AI Coding Workflow
When this rule materially applies:
1. identify the responsibility and reason-to-change boundaries before editing
2. inspect existing project structure and reuse it when adequate
3. choose the smallest useful structural move
4. keep cohesive code together and split mixed responsibilities deliberately
5. avoid helper inflation, speculative abstractions, and wrong DRY extractions
6. add or update concise comments when purpose, process, constraints, side effects, or business rules would otherwise be hidden
7. preserve behavior during refactor unless behavior change is explicit
8. verify with relevant checks when available and report verification limits honestly
---
## Verification Checklist
- [ ] Responsibilities and reasons to change are clear enough for the edited code
- [ ] God function / God file pressure was reduced or not worsened without reason
- [ ] Decomposition used the smallest useful structure rather than a rigid template
- [ ] Cohesion improved or stayed strong; coupling did not increase unnecessarily
- [ ] Similar code was not merged into a wrong abstraction
- [ ] Helper functions earn their indirection cost and trivial helpers were avoided or inlined
- [ ] Important dependencies and state flow are explicit enough to test/reason about
- [ ] Refactor steps preserve behavior unless behavior change was explicit
- [ ] Relevant checks were run or verification limits were reported
- [ ] Source-code comments explain useful purpose/process/boundary information without repeating syntax or becoming stale
- [ ] Tactical shortcuts have a visible convergence path when debt remains material
---
## Quality Metrics
| Metric | Target |
|---|---|
| Responsibility clarity | High |
| God function/file drift | Low |
| Smell-triggered judgment quality | High |
| Overengineering from rigid templates | Low |
| Wrong abstraction incidents | Low |
| Helper-function inflation | Low |
| Source-code comment usefulness | High |
| Stale or syntax-repeating comments | Low |
| Refactor behavior preservation | High |
| Verification honesty | High |
---
## Integration
Related rules:
- [tactical-strategic-programming.md](tactical-strategic-programming.md) - owns tactical entry, strategic target, and convergence path; this rule owns code responsibility/decomposition quality inside that path
- [goal-set-review-and-priority-balance.md](goal-set-review-and-priority-balance.md) - keeps structure-first work balanced against the full objective set
- [portable-implementation-and-hardcoding-control.md](portable-implementation-and-hardcoding-control.md) - owns portable/environment binding beyond local structure decisions
- [project-documentation-standards.md](project-documentation-standards.md) - governs durable docs when structural design changes require documentation; source-code comments do not replace governed documentation authority
- [explanation-quality.md](explanation-quality.md) - owns assistant response explanations; this rule owns source-code comment discipline inside implementation
- [evidence-grounded-burden-of-proof.md](evidence-grounded-burden-of-proof.md) - keeps claims about maintainability, smell, and refactor quality evidence-calibrated
- [accurate-communication.md](accurate-communication.md) - keeps edited/tested/fixed/stable wording aligned to checked evidence
---
> **Full history:** [changelog/maintainable-code-structure-and-decomposition.changelog.md](changelog/maintainable-code-structure-and-decomposition.changelog.md)
