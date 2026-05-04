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
Tactical work is allowed when it materially improves startup speed, learning speed, or immediate execution. Keep it bounded and temporary unless explicitly promoted; do not require complete strategic design before useful implementation can begin.

### Strategic target
Every tactical move must point toward a declared strategic target. Identify the intended end-state before or alongside tactical execution, do not let local progress define the long-term direction by itself, and do not proceed tactically when no strategic target can be named.

### Mandatory convergence
Every tactical path must show how it converges into strategic structure: absorbed, promoted, replaced, or retired; the future structure it converges into; and the trigger for strategic closure. Temporary structure must not remain indefinitely undefined.

### Bounded tactical scope
Tactical work must stay narrow enough to converge cleanly. Prefer local, reversible, low-blast-radius moves; do not let tactical entry silently expand into broad unplanned architecture; and do not let machine-local paths, hosts, or install assumptions become defaults unless explicitly machine-scoped. Portable-default and anti-hardcoding ownership defer to `portable-implementation-and-hardcoding-control.md`.

### No permanent tactical drift
Temporary solutions must not become hidden long-term authority. Workarounds, patch stacks, bridges, or compatibility paths require retirement, absorption, or formal promotion when they persist; detect and call out drift early.

### Strategic closure
Non-trivial systems should end in strategic structure. Stable boundaries, roles, and sequencing belong in strategic authority; design and phase layers should absorb validated tactical learning; final authority should not live in leftover tactical fragments.

### Maintainable structure boundary
Tactical and strategic programming must still preserve maintainable coding structure. Use `maintainable-code-structure-and-decomposition.md` for code responsibility, decomposition, God function/file, code smells, wrong abstraction, comments, and behavior-preserving refactor decisions. Tactical fixes may stay local and fast, but should not silently worsen structure debt without a narrow reason; material debt needs a convergence path.
---
## Classification and Decision Model
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
When this doctrine materially matters, make these meanings visible: **Strategic target**, **Tactical now**, **Why tactical first**, **Convergence path**, and **Strategic end-state**. Equivalent headings are acceptable if the meaning stays explicit.
---
## Trigger Model
- Fast local fix in unclear terrain: allow only with strategic target and convergence path.
- Patch accumulation: check for tactical drift and promotion need.
- Phase/roadmap planning: let strategic framing dominate.
- Temporary runtime structure: require retirement or absorption path.
- Architecture still emerging: use `TACTICAL_WITH_STRATEGIC_TRACK`.
- Long-lived workaround: require promotion, retirement, or replacement.
- Tactical fix changes code structure: preserve responsibility clarity, avoid avoidable God function/file drift, and name convergence if material debt remains.
---
## Verification Checklist
- [ ] Tactical entry is bounded and justified by speed/learning/immediate execution value
- [ ] Strategic target and end-state are declared before or alongside tactical execution
- [ ] Convergence path says absorb, promote, replace, or retire
- [ ] Temporary workarounds do not become hidden permanent authority
- [ ] Design/phase or stable architecture absorbs validated tactical learning when strategic closure is needed
- [ ] Tactical code changes do not silently worsen maintainability debt without a narrow reason and convergence path
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
Related rules: `phase-implementation.md` owns strategic execution; `document-patch-control.md` owns tactical patch artifacts; `project-documentation-standards.md` owns document roles; `runtime-topology-control.md` owns runtime convergence; `maintainable-code-structure-and-decomposition.md` owns coding-time structure; explanation/presentation chains own user-facing framing.
---
