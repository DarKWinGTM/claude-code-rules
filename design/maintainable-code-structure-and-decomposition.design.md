# Maintainable Code Structure and Decomposition

## 0) Document Control

> **Parent Scope:** RULES System Design
> **Current Version:** 1.1
> **Session:** d42465eb-30a7-4bc8-b9d6-03e52306e9a5 (2026-05-04)
> **Full history:** [../changelog/maintainable-code-structure-and-decomposition.changelog.md](../changelog/maintainable-code-structure-and-decomposition.changelog.md)

---

## 1) Goal

Define a first-class coding-structure rule that helps AI write and refactor code with clear responsibility boundaries, maintainable decomposition, helper-function necessity, appropriate source-code comments, and anti-God-function / anti-God-file discipline while avoiding rigid line-count rules and architecture-template overuse.

The target state is practical:
- code remains readable, testable, and easier to change later
- responsibility boundaries follow real reasons to change
- code smells trigger investigation rather than automatic refactor
- decomposition stays smallest-useful rather than ceremony-first
- helper functions earn their indirection cost rather than appearing for every trivial expression
- source-code comments explain useful purpose, process, constraints, side effects, and business rules without repeating syntax or becoming stale
- tactical programming remains allowed, but tactical shortcuts do not become hidden permanent structure

---

## 2) Problem Statement

AI coding can fail in two opposite ways:

| Failure Mode | Consequence |
|---|---|
| under-structured implementation | God functions, God files, hidden dependencies, mixed concerns, hard-to-test changes |
| over-structured implementation | unnecessary layers, premature abstractions, wrong DRY extraction, helper-function inflation, harder navigation |
| under-explained implementation | code has working structure but hides purpose, process, constraints, side effects, or business-rule rationale |
| over-commented implementation | comments repeat syntax, narrate every line, become stale, or substitute for clearer structure |

The repository already has `tactical-strategic-programming.md` for tactical entry and strategic convergence, but that chain does not own coding-time function/file/module responsibility decisions. This design adds a dedicated owner for maintainable code structure so implementation work can be fast without normalizing structure debt.

---

## 3) Design Principles

### 3.1 Maintainability means future changeability
Maintainability is treated as the ability to understand, test, modify, extend, or repair code later with low surprise and bounded blast radius. More files or more layers are not automatically more maintainable.

### 3.2 Responsibility follows reason to change
Code should be grouped or separated according to why it changes. Business logic, orchestration, UI/presentation, persistence, external integration, validation, formatting, logging, config, and error handling may deserve separation when they change independently or obscure each other.

### 3.3 Smells are triggers, not verdicts
Long functions, large files, and mixed objects are not automatic defects. They trigger analysis of cohesion, coupling, testability, change axes, and risk.

### 3.4 Smallest useful decomposition
The intended decomposition path is local clarity first, then helper extraction only when a named helper improves understanding, then module/file split, and only then heavier abstractions when current evidence justifies them.

### 3.5 Helper functions must earn indirection
A helper function is useful when it names a real concept, business rule, process step, reusable behavior, testable unit, or side-effect boundary. It is not useful when it wraps an obvious expression, creates pass-through call chains, or makes readers jump around without adding meaning.

### 3.6 Wrong abstraction is worse than bounded duplication
Do not merge code only because it looks similar. Shared abstraction needs a shared concept and shared reason to change.

### 3.7 Source-code comments explain hidden context
Names and structure should explain normal flow first. Comments should be concise and explain why, purpose, process order, business rules, constraints, side effects, external contracts, or workarounds when that information is not obvious from code. Comments that repeat syntax, narrate every line, or become stale should be removed or rewritten.

### 3.8 Refactor preserves behavior
Refactoring should improve internal structure while preserving external behavior unless behavior change is explicitly part of the task. Verification limits must remain visible.

---

## 4) Target Runtime Behavior

When coding or refactoring, the assistant should:
1. identify the responsibility and reason-to-change boundaries before or during editing
2. inspect existing project structure before introducing new shapes
3. choose the smallest structural move that improves maintainability
4. keep cohesive code together and split mixed responsibilities deliberately
5. avoid helper-function inflation, speculative abstractions, template-first architecture, and line-count policing
6. add or update source-code comments when they explain useful purpose, process, constraints, side effects, or business-rule context
7. preserve behavior during refactors unless behavior change is explicit
8. verify relevant behavior when available and report unverified limits honestly

---

## 5) Decomposition Decision Model

```text
Need to write or change code
  ↓
Does the current unit have one clear responsibility and reason to change?
  → Yes: keep it local unless readability/testability still suffers
  → No: inspect the mixed concerns
  ↓
Can a named helper clarify a real concept, process step, repeated behavior, testable unit, or side-effect boundary?
  → Yes: extract a helper/function if it lowers cognitive load
  → No: keep the code local when inline reading is clearer
  ↓
Would the helper merely wrap an obvious expression or force call-chain hopping?
  → Yes: do not extract, or inline it back
  → No: continue
  ↓
Are responsibilities changed/tested/owned differently?
  → Yes: split module/file/component/class by responsibility
  → No: continue
  ↓
Is a heavier abstraction justified by current variation, test boundary, or ownership need?
  → Yes: introduce the smallest fitting abstraction
  → No: avoid speculative generality and preserve local clarity
```

---

## 6) Smell Trigger Set

The runtime rule should recognize these signals:
- God function
- God file
- long method
- large class/object
- divergent change
- shotgun surgery
- feature envy
- primitive obsession
- hidden dependency
- helper-function inflation
- comment spam
- stale or misleading comments
- speculative generality

Each signal should prompt bounded analysis and the smallest useful response, not automatic splitting, automatic helper extraction, or automatic comment insertion.

---

## 7) Integration Boundaries

| Adjacent rule | Boundary |
|---|---|
| `tactical-strategic-programming.md` | owns tactical/strategic mode, target, convergence, and closure |
| `maintainable-code-structure-and-decomposition.md` | owns code responsibility, decomposition, God function/file, and wrong-abstraction posture |
| `goal-set-review-and-priority-balance.md` | prevents local structure polishing from crowding out the full active objective |
| `portable-implementation-and-hardcoding-control.md` | owns portable env/config/default binding beyond local structure |
| `project-documentation-standards.md` | owns governed docs when structural target state needs durable documentation; inline comments do not replace durable docs |
| `explanation-quality.md` | owns assistant-facing explanations; this design owns source-code comment discipline only |
| `accurate-communication.md` | owns evidence-honest edited/tested/fixed/stable wording |

---

## 8) Anti-Goals

This design intentionally does not add:
- hard maximum line counts for functions/files
- mandatory Clean Architecture, MVC, service/repository, or controller/service/repository templates
- mandatory splitting for every long function
- helper function extraction for every simple expression or local sequence
- comment-every-line style or comments that merely repeat syntax
- stale comments left behind after behavior changes
- speculative interfaces or factories for imagined future variation
- refactor-by-rewrite as a default
- maintainability claims without checked evidence or verification limits

---

## 9) Verification Expectations

A compliant implementation should verify:
- the runtime/design/changelog triad aligns at v1.1
- README and master design stay at 43 active runtime rules because this is a refinement, not a new rule
- helper-function guidance avoids both God-function drift and helper-function inflation
- comment guidance explains useful source-code context without comment spam or stale-comment drift
- tactical-strategic integration remains a boundary and does not take over coding-time responsibility
- source/runtime parity passes after runtime install
- phase and patch records describe the refinement as principle-based code quality guidance, not a rigid template doctrine

---

> Full history: [../changelog/maintainable-code-structure-and-decomposition.changelog.md](../changelog/maintainable-code-structure-and-decomposition.changelog.md)
