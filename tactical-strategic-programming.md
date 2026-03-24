# Tactical Strategic Programming

> **Current Version:** 1.0
> **Design:** [design/tactical-strategic-programming.design.md](design/tactical-strategic-programming.design.md) v1.0
> **Session:** 77d0802a-fd64-4023-a66d-88c165ccca12
> **Full history:** [changelog/tactical-strategic-programming.changelog.md](changelog/tactical-strategic-programming.changelog.md)

---

## Rule Statement

**Core Principle: Tactical programming is allowed for speed, but only under a declared strategic target, a visible convergence path, and an eventual strategic end-state. Tactical work is an entry path, not the final architecture authority.**

This rule exists to prevent two opposite failures:
- forcing heavy strategic ceremony before any useful tactical progress can begin
- allowing tactical patches, workarounds, and narrow local optimizations to drift into hidden long-term authority

---

## Core Principles

### 1) Tactical Entry Principle
Tactical work is allowed when it materially improves startup speed, learning speed, or immediate execution efficiency.

Required guidance:
- allow bounded tactical entry when it reduces friction
- do not require strategic completion before any useful implementation can begin
- treat tactical entry as temporary by default unless explicitly promoted

### 2) Strategic Target Principle
Every tactical move must point toward a declared strategic target.

Required guidance:
- identify the intended strategic end-state before or alongside tactical execution
- do not allow tactical work to proceed as if local progress alone defines the long-term direction
- if no strategic target can be named, tactical execution is not ready

### 3) Mandatory Convergence Principle
Every tactical path must include a visible convergence path into strategic structure.

Required guidance:
- say how the tactical slice will be absorbed, promoted, replaced, or retired
- identify what future structure this tactical move should converge into
- do not allow temporary tactical structure to remain indefinitely undefined

### 4) Bounded Tactical Scope Principle
Tactical work must remain bounded.

Required guidance:
- prefer local, reversible, low-blast-radius tactical moves
- do not let tactical entry silently expand into broad unplanned architecture
- keep tactical artifacts narrow enough that they can still converge cleanly

### 5) No Permanent Tactical Drift Principle
Temporary tactical solutions must not become hidden long-term authority.

Required guidance:
- do not allow workaround, patch stack, local bridge, or temporary compatibility path to become the de facto final architecture without explicit promotion
- require retirement, absorption, or formal promotion when tactical work persists
- detect and call out tactical drift early

### 6) Strategic Closure Principle
The intended end-state of non-trivial systems should be strategic programming, not permanent tactical accumulation.

Required guidance:
- strategic structure should eventually own the stable boundaries, roles, and sequencing
- design and phase layers should absorb validated tactical learning
- the final authority should live in strategic artifacts, not in leftover tactical fragments

---

## Classification Model

| Mode | Meaning | Typical Use |
|------|---------|-------------|
| `TACTICAL` | Local bounded execution slice | patch, focused fix, immediate unblock |
| `STRATEGIC` | Directional or architectural planning layer | design, roadmap, phased execution, boundary setting |
| `TACTICAL_WITH_STRATEGIC_TRACK` | Tactical execution that already has a declared strategic target and convergence path | fast-start implementation under strategic control |

---

## Decision Model

Before continuing non-trivial work, answer:

1. Is this tactical, strategic, or tactical-with-strategic-track?
2. What is the strategic target?
3. What is the tactical slice now?
4. How does it converge?
5. What triggers promotion from tactical to strategic closure?

If 2–5 cannot be answered, the work is not ready for tactical execution without further strategic clarification.

---

## Tactical vs Strategic Artifact Map

| Artifact Type | Default Role |
|--------------|--------------|
| `design/*.design.md` | strategic target-state authority |
| `phase/SUMMARY.md` + child phase files | strategic execution program |
| `patches/*.patch.md` or namespaced `patch.md` | tactical artifact |
| `TODO.md` | tactical execution tracking |
| runtime temporary workaround | tactical implementation device |
| stable architecture authority | strategic end-state |

---

## Required Communication Shape

When this doctrine materially matters, the response should make these fields visible:
- **Strategic target** - where the work should end up
- **Tactical now** - what is being done immediately
- **Why tactical first** - why bounded tactical speed is acceptable here
- **Convergence path** - how the current tactical slice will move into strategic structure
- **Strategic end-state** - what should own the final authority

Equivalent headings are acceptable if the meaning stays explicit.

---

## Trigger Model

Apply this rule more strongly when one or more of these signals are present:

| Trigger | Typical Signal | Expected Response |
|--------|-----------------|------------------|
| fast local fix in unclear terrain | "just patch it first", compatibility bridge, shim, thin wrapper | allow tactical entry, but require strategic target + convergence path |
| patch accumulation | repeated local fixes, workaround layering | check for tactical drift and promotion need |
| phase/roadmap planning | staged rollout, migration, multi-system sequencing | strategic framing should dominate |
| temporary runtime structure | temporary service, bridge, adapter, fallback | require retirement or absorption path |
| architecture still emerging | goal is known but final structure is still forming | tactical-with-strategic-track mode |
| long-lived local workaround | tactical artifact persists beyond immediate need | require explicit promotion, retirement, or replacement |

---

## Anti-Patterns to Avoid

| Anti-Pattern | Why It Hurts | Better Behavior |
|--------------|--------------|-----------------|
| tactical patch treated as final architecture | hidden long-term drift | declare strategic target and convergence path |
| strategy-only paralysis before any local progress | slows discovery and learning | allow bounded tactical entry |
| workaround with no retirement path | temporary local logic becomes permanent by accident | require retirement, absorption, or promotion plan |
| design says one thing, tactical implementation drifts elsewhere | authority split and inconsistency | keep tactical work aligned to strategic target |
| phase plan built from accumulated tactical fragments with no structure | sequencing and ownership degrade | strategic program should absorb tactical learning into explicit structure |

---

## Quality Metrics

| Metric | Target |
|--------|--------|
| Tactical-entry clarity | High |
| Strategic-target visibility | High |
| Convergence-path visibility | High |
| Tactical drift detection | High |
| Hidden permanent tactical authority | 0 critical cases |
| Strategic closure clarity | High |

---

## Integration

Related rules:
- [phase-implementation.md](phase-implementation.md) - strategic execution and convergence layer
- [document-patch-control.md](document-patch-control.md) - tactical artifact governance
- [project-documentation-standards.md](project-documentation-standards.md) - tactical vs strategic document-role map
- [runtime-topology-control.md](runtime-topology-control.md) - tactical runtime changes require convergence/retirement path
- [explanation-quality.md](explanation-quality.md) - explains whether work is tactical or strategic and how it converges
- [answer-presentation.md](answer-presentation.md) - presents strategic target, tactical now, convergence path, and end-state clearly

---
