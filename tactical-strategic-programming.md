# Tactical Strategic Programming
> **Current Version:** 1.3
> **Design:** [design/tactical-strategic-programming.design.md](design/tactical-strategic-programming.design.md) v1.3
> **Session:** d42465eb-30a7-4bc8-b9d6-03e52306e9a5
> **Full history:** [changelog/tactical-strategic-programming.changelog.md](changelog/tactical-strategic-programming.changelog.md)
---
## Rule Statement
**Core Principle: Tactical programming is allowed for speed only when it has a declared strategic target, visible convergence path, and eventual strategic end-state. Tactical work is an entry path, not final architecture authority.**
This prevents both strategy paralysis and hidden permanent workaround drift.
---
## Core Contract
### Tactical entry
Tactical work is allowed when it materially improves startup speed, learning speed, or immediate execution.
Required guidance:
- allow bounded tactical entry when it reduces friction
- do not require complete strategic design before useful implementation can begin
- treat tactical entry as temporary unless explicitly promoted
### Strategic target
Every tactical move must point toward a declared strategic target.
Required guidance:
- identify the intended strategic end-state before or alongside tactical execution
- do not let local progress define the long-term direction by itself
- if no strategic target can be named, tactical execution is not ready
### Mandatory convergence
Every tactical path must show how it converges into strategic structure.
Required guidance:
- say whether the tactical slice will be absorbed, promoted, replaced, or retired
- identify the future structure it should converge into
- do not leave temporary tactical structure indefinitely undefined
### Bounded tactical scope
Tactical work must stay narrow enough to converge cleanly.
Required guidance:
- prefer local, reversible, low-blast-radius tactical moves
- do not let tactical entry silently expand into broad unplanned architecture
- do not let machine-local hardcoded paths, hosts, or install assumptions become defaults unless explicitly machine-scoped
- defer portable-default and anti-hardcoding ownership to `portable-implementation-and-hardcoding-control.md`
### No permanent tactical drift
Temporary solutions must not become hidden long-term authority.
Required guidance:
- do not let workaround, patch stack, bridge, or compatibility path become final architecture without explicit promotion
- require retirement, absorption, or formal promotion when tactical work persists
- detect and call out tactical drift early
### Strategic closure
Non-trivial systems should end in strategic structure, not permanent tactical accumulation.
Required guidance:
- strategic structure should own stable boundaries, roles, and sequencing
- design and phase layers should absorb validated tactical learning
- final authority should live in strategic artifacts, not leftover tactical fragments
### Maintainable structure boundary
Tactical and strategic programming must still preserve maintainable coding structure.
Required guidance:
- use `maintainable-code-structure-and-decomposition.md` for code responsibility, decomposition, God function/file, code-smell, wrong-abstraction, and behavior-preserving refactor decisions
- tactical fixes may stay local and fast, but should not silently worsen God-function or God-file drift without a narrow reason
- when a tactical slice leaves material structure debt, include a convergence path for absorbing, replacing, promoting, or retiring that structure
- strategic work should let stable responsibility boundaries absorb validated tactical learning rather than accumulating tactical fragments
---
## Classification Model
| Mode | Meaning | Typical use |
|---|---|---|
| `TACTICAL` | local bounded execution slice | patch artifact, focused fix, immediate unblock |
| `STRATEGIC` | directional/architectural planning layer | design, roadmap, phased execution, boundary setting |
| `TACTICAL_WITH_STRATEGIC_TRACK` | tactical execution with target and convergence path | fast-start implementation under strategic control |
---
## Decision Model
Before non-trivial tactical execution, answer:
1. Is this tactical, strategic, or tactical-with-strategic-track?
2. What is the strategic target?
3. What is the tactical slice now?
4. How does it converge?
5. What triggers promotion to strategic closure?
If 2-5 cannot be answered, clarify strategy before tactical execution.
---
## Artifact Map
| Artifact type | Default role |
|---|---|
| `design/*.design.md` | strategic target-state authority |
| `phase/SUMMARY.md` + child phase files | strategic execution program |
| `patch/<context>.patch.md` or root `<context>.patch.md` | tactical change artifact |
| `TODO.md` | tactical execution tracking |
| runtime temporary workaround | tactical implementation device |
| stable architecture authority | strategic end-state |
---
## Communication Shape
When this doctrine materially matters, make these fields visible:
- **Strategic target** — where the work should end up
- **Tactical now** — what is being done immediately
- **Why tactical first** — why bounded tactical speed is acceptable
- **Convergence path** — how the slice moves into strategic structure
- **Strategic end-state** — what owns final authority
Equivalent headings are acceptable if the meaning stays explicit.
---
## Trigger Model
| Trigger | Expected response |
|---|---|
| fast local fix in unclear terrain | allow only with strategic target and convergence path |
| patch accumulation | check for tactical drift and promotion need |
| phase/roadmap planning | let strategic framing dominate |
| temporary runtime structure | require retirement or absorption path |
| architecture still emerging | use tactical-with-strategic-track mode |
| long-lived workaround | require promotion, retirement, or replacement |
| tactical fix changes code structure | preserve responsibility clarity, avoid avoidable God function/file drift, and name convergence if material debt remains |
---
## Anti-Patterns
| Anti-pattern | Better behavior |
|---|---|
| tactical patch treated as final architecture | declare target and convergence path |
| strategy-only paralysis | allow bounded tactical entry |
| workaround with no retirement path | require retirement, absorption, or promotion |
| design and implementation drift apart | keep tactical work aligned to strategic target |
| phase plan built from unstructured patches | let strategic program absorb learning explicitly |
| tactical code patch grows God functions or God files with no convergence path | use maintainable structure guidance and keep material debt visible |
---
## Quality Metrics
| Metric | Target |
|---|---|
| Tactical-entry clarity | High |
| Strategic-target visibility | High |
| Convergence-path visibility | High |
| Tactical drift detection | High |
| Hidden permanent tactical authority | 0 critical cases |
| Strategic closure clarity | High |
| Tactical structure debt visibility | High |
| Unnecessary God function/file drift from tactical slices | Low |
---
## Integration
Related rules:
- [phase-implementation.md](phase-implementation.md) - strategic execution and convergence layer
- [document-patch-control.md](document-patch-control.md) - tactical artifact governance
- [project-documentation-standards.md](project-documentation-standards.md) - tactical vs strategic document-role map
- [runtime-topology-control.md](runtime-topology-control.md) - runtime convergence/retirement path
- [maintainable-code-structure-and-decomposition.md](maintainable-code-structure-and-decomposition.md) - coding-time responsibility boundaries, decomposition, God function/file, wrong-abstraction, and behavior-preserving refactor quality inside tactical or strategic implementation
- [explanation-quality.md](explanation-quality.md) - tactical/strategic explanation
- [answer-presentation.md](answer-presentation.md) - target/tactical/convergence/end-state presentation
---
