# Tactical Strategic Programming

## 0) Document Control

> **Parent Scope:** RULES System Design
> **Current Version:** 1.3
> **Session:** d42465eb-30a7-4bc8-b9d6-03e52306e9a5 (2026-05-04)

---

## 1) Goal

Define one first-class strategy rule that allows tactical programming for speed while requiring strategic convergence as the intended end-state.

This rule exists to prevent two opposite failures:
- forcing heavy strategic ceremony before any useful tactical progress can begin
- allowing tactical patches, workarounds, and narrow local optimizations to drift into hidden long-term authority

The target model is:
- **tactical entry is allowed**
- **strategic target is mandatory**
- **convergence path is visible**
- **strategic closure is the intended end-state**
- **coding-time structure quality is delegated to `maintainable-code-structure-and-decomposition.md` while tactical/strategic keeps convergence ownership**

---

## 2) Problem Statement

Engineering work often starts under incomplete clarity.
In that state, teams need tactical speed, but they also need strategic discipline.
Without an explicit rule, one of two bad outcomes usually appears:

| Failure Mode | Consequence |
|-------------|-------------|
| Strategic-overload too early | Slow starts, analysis paralysis, delayed learning |
| Tactical drift too long | Temporary structures become hidden architecture authority |

The repository already contains related concepts across patch, phase, documentation, runtime-topology, and explanation rules, but the tactical-versus-strategic doctrine itself still lacks a single semantic owner.

---

## 3) Core Definitions

### 3.1 Tactical programming
Tactical programming is bounded local execution intended to create speed, unlock visibility, or solve a narrow immediate problem.

Typical traits:
- local scope
- reversible or replaceable
- short time horizon
- low-to-medium blast radius
- useful for first-step implementation, fast learning, or narrow fixes

Typical artifacts:
- patch
- implementation checklist
- focused compatibility layer
- bounded workaround
- local proof-of-direction

### 3.2 Strategic programming
Strategic programming is directional and structural work intended to define or reinforce the long-term shape of the system.

Typical traits:
- broader scope
- longer time horizon
- cross-system or cross-phase implications
- higher change cost later
- architecture, sequencing, ownership, and target-state clarity matter

Typical artifacts:
- design
- phase planning
- architecture direction
- strategic program sequencing
- long-horizon operating structure

### 3.3 Tactical-with-strategic-track
This is the preferred bridge mode when tactical execution begins before the whole system is fully settled.

It means:
- tactical implementation is allowed now
- strategic target is already declared
- convergence path is visible
- the tactical slice is not pretending to be final authority

---

## 4) Core Principles

### 4.1 Tactical Entry Principle
Tactical work is allowed when it materially improves startup speed, learning speed, or immediate execution efficiency.

Required guidance:
- allow bounded tactical entry when it reduces friction
- do not require strategic completion before any useful implementation can begin
- treat tactical entry as temporary by default unless explicitly promoted

### 4.2 Strategic Target Principle
Every tactical move must point toward a declared strategic target.

Required guidance:
- identify the intended strategic end-state before or alongside tactical execution
- do not allow tactical work to proceed as if local progress alone defines the long-term direction
- if no strategic target can be named, tactical execution is not ready

### 4.3 Mandatory Convergence Principle
Every tactical path must include a visible convergence path into strategic structure.

Required guidance:
- say how the tactical slice will be absorbed, promoted, replaced, or retired
- identify what future structure this tactical move should converge into
- do not allow temporary tactical structure to remain indefinitely undefined

### 4.4 Bounded Tactical Scope Principle
Tactical work must remain bounded.

Required guidance:
- prefer local, reversible, low-blast-radius tactical moves
- do not let tactical entry silently expand into broad unplanned architecture
- keep tactical artifacts narrow enough that they can still converge cleanly
- do not let machine-local paths, hosts, or install assumptions become tactical defaults unless a machine-scoped contract is explicitly intended
- defer broader anti-hardcoding ownership to `portable-implementation-and-hardcoding-control.md`

### 4.5 No Permanent Tactical Drift Principle
Temporary tactical solutions must not become hidden long-term authority.

Required guidance:
- do not allow workaround, patch stack, local bridge, or temporary compatibility path to become the de facto final architecture without explicit promotion
- require retirement, absorption, or formal promotion when tactical work persists
- detect and call out tactical drift early

### 4.6 Strategic Closure Principle
The intended end-state of non-trivial systems should be strategic programming, not permanent tactical accumulation.

Required guidance:
- strategic structure should eventually own the stable boundaries, roles, and sequencing
- design and phase layers should absorb validated tactical learning
- the final authority should live in strategic artifacts, not in leftover tactical fragments

### 4.7 Maintainable Structure Boundary Principle
Tactical/strategic doctrine owns execution posture and convergence, not every coding-time decomposition decision.

Required guidance:
- delegate function/file/module responsibility, God function/file, code smell, smallest-useful decomposition, wrong-abstraction, and behavior-preserving refactor decisions to `maintainable-code-structure-and-decomposition.md`
- tactical fixes may stay local for speed, but material structure debt should have an explicit convergence path
- strategic programming should absorb validated tactical learning into stable responsibility boundaries instead of accumulating unrelated tactical fragments

---

## 5) Classification Model

| Mode | Meaning | Typical Use |
|------|---------|-------------|
| `TACTICAL` | Local bounded execution slice | patch, focused fix, immediate unblock |
| `STRATEGIC` | Directional or architectural planning layer | design, roadmap, phased execution, boundary setting |
| `TACTICAL_WITH_STRATEGIC_TRACK` | Tactical execution that already has a declared strategic target and convergence path | fast-start implementation under strategic control |

---

## 6) Decision Model

Before continuing non-trivial work, answer:

1. Is this tactical, strategic, or tactical-with-strategic-track?
2. What is the strategic target?
3. What is the tactical slice now?
4. How does it converge?
5. What triggers promotion from tactical to strategic closure?

If 2–5 cannot be answered, the work is not ready for tactical execution without further strategic clarification.

---

## 7) Tactical vs Strategic Artifact Map

| Artifact Type | Default Role |
|--------------|--------------|
| `design/*.design.md` | strategic target-state authority |
| `phase/SUMMARY.md` + child phase files | strategic execution program |
| `patch/<context>.patch.md` or root `<context>.patch.md` | tactical artifact |
| `TODO.md` | tactical execution tracking |
| runtime temporary workaround | tactical implementation device |
| stable architecture authority | strategic end-state |

---

## 8) Required Communication Shape

When this doctrine materially matters, the response should make these fields visible:
- **Strategic target** - where the work should end up
- **Tactical now** - what is being done immediately
- **Why tactical first** - why bounded tactical speed is acceptable here
- **Convergence path** - how the current tactical slice will move into strategic structure
- **Strategic end-state** - what should own the final authority

Equivalent headings are acceptable if the meaning stays explicit.

---

## 9) Trigger Model

Apply this rule more strongly when one or more of these signals are present:

| Trigger | Typical Signal | Expected Response |
|--------|-----------------|------------------|
| fast local fix in unclear terrain | "just patch it first", compatibility bridge, shim, thin wrapper | allow tactical entry, but require strategic target + convergence path |
| patch accumulation | repeated local fixes, workaround layering | check for tactical drift and promotion need |
| phase/roadmap planning | staged rollout, migration, multi-system sequencing | strategic framing should dominate |
| temporary runtime structure | temporary service, bridge, adapter, fallback | require retirement or absorption path |
| architecture still emerging | goal is known but final structure is still forming | tactical-with-strategic-track mode |
| long-lived local workaround | tactical artifact persists beyond immediate need | require explicit promotion, retirement, or replacement |
| tactical code structure debt | tactical fix grows God function/file pressure or mixed responsibilities | keep the slice bounded and point structural cleanup/convergence to the maintainable code structure owner |

---

## 10) Anti-Patterns to Avoid

| Anti-Pattern | Why It Hurts | Better Behavior |
|--------------|--------------|-----------------|
| tactical patch treated as final architecture | hidden long-term drift | declare strategic target and convergence path |
| strategy-only paralysis before any local progress | slows discovery and learning | allow bounded tactical entry |
| workaround with no retirement path | temporary local logic becomes permanent by accident | require retirement, absorption, or promotion plan |
| design says one thing, tactical implementation drifts elsewhere | authority split and inconsistency | keep tactical work aligned to strategic target |
| phase plan built from accumulated tactical fragments with no structure | sequencing and ownership degrade | strategic program should absorb tactical learning into explicit structure |
| tactical coding shortcut silently becomes God file or God function structure | maintainability debt becomes permanent by accident | keep material code-structure debt visible and converge through `maintainable-code-structure-and-decomposition.md` |

---

## 11) Quality Metrics

| Metric | Target |
|--------|--------|
| Tactical-entry clarity | High |
| Strategic-target visibility | High |
| Convergence-path visibility | High |
| Tactical drift detection | High |
| Hidden permanent tactical authority | 0 critical cases |
| Strategic closure clarity | High |

---

## 12) Integration with Existing Rules

| Rule | Relationship |
|------|--------------|
| `phase-implementation.md` | Strategic execution and convergence layer |
| `document-patch-control.md` | Tactical artifact governance |
| `project-documentation-standards.md` | Tactical vs strategic document-role map |
| `runtime-topology-control.md` | Tactical runtime changes require convergence/retirement path |
| `maintainable-code-structure-and-decomposition.md` | Owns coding-time responsibility boundaries, decomposition, God function/file pressure, wrong-abstraction guardrails, and behavior-preserving refactor quality inside tactical or strategic implementation |
| `explanation-quality.md` | Explains whether work is tactical or strategic and how it converges |
| `answer-presentation.md` | Presents strategic target, tactical now, convergence path, and end-state clearly |

---

> Full history: [../changelog/tactical-strategic-programming.changelog.md](../changelog/tactical-strategic-programming.changelog.md)
