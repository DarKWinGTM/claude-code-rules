# Answer Presentation

## 0) Document Control

> **Parent Scope:** RULES System Design
> **Current Version:** 1.0
> **Session:** 468e053d-9953-496e-8e83-910e2ae67402 (2026-03-10)

---

## 1) Goal

Define one first-class rule chain for answer presentation so responses are orderly, readable, scannable, and visually disciplined without forcing one rigid template onto every answer.

The target behavior is principle-first and trigger-driven:
- lead with the main point when helpful
- structure by user need and answer type
- use headings, lists, tables, and spacing as semantic tools
- keep presentation readable without decorative noise
- preserve flexibility for simple answers

---

## 2) Problem Statement

Output quality drift is often a presentation problem, not only a reasoning problem.

Observed failure modes:
- long answers appear as walls of text even when structure would help
- headings exist but do not reflect real section purpose
- bullets are used for everything, including ideas that need prose continuity
- sequences are presented as unordered lists
- tables are used where no real comparison exists
- answers contain the right reasoning but remain hard to scan quickly
- layout becomes decorative instead of functional
- simple answers are over-structured while complex answers remain under-structured

This design defines presentation-layer guidance that improves readability and scanability while staying compatible with existing explanation and communication rules.

---

## 3) Core Presentation Principles

### 3.1 Main-Point-First Principle

When user orientation matters, place the main point early.

Required guidance:
- use a short answer or short orienting statement near the start when it helps the user understand the response faster
- do not bury the conclusion deep inside the answer unless suspense or chronology is required

### 3.2 Structure-Follows-Intent Principle

Presentation shape should reflect the kind of answer being given.

Required guidance:
- simple factual answers may stay compact
- analytical answers should use clearer sectional structure
- comparisons should use comparison-oriented layouts
- procedures should use sequence-oriented layouts

### 3.3 Scannability-Over-Density Principle

When answers become longer or more complex, scanability should improve rather than degrade.

Required guidance:
- use headings to separate different purposes
- use whitespace to separate conceptual blocks
- avoid dense, uninterrupted text when structure would improve reading speed

### 3.4 Semantic Formatting Principle

Formatting should communicate meaning, not decoration.

Required guidance:
- use bullets for grouped items
- use numbered lists for ordered steps or sequences
- use tables for real comparison or structured facts only
- use diagrams only when sequence or branching is central
- ensure headings are short, functional, and content-representative

### 3.5 One-Block-One-Purpose Principle

Each paragraph, list, table, or section should have a clear job.

Required guidance:
- keep one main idea per paragraph when possible
- introduce lists and tables with a short context-setting line when needed
- do not mix multiple unrelated purposes into one section

### 3.6 Readability-Over-Decoration Principle

Readable structure matters more than visual flourish.

Required guidance:
- avoid decorative sectioning that adds no informational value
- prefer clean markdown structure over ornamental formatting
- preserve consistency in heading style, list style, and emphasis usage

---

## 4) Trigger Model

Use stronger presentation structure when one or more of these triggers are present:

| Trigger | Typical Signal | Expected Presentation Shift |
|--------|-----------------|-----------------------------|
| simple answer | factual lookup, one-step response, low complexity | compact paragraphs or short list only |
| analytical answer | explanation, trade-off, diagnosis, architecture reasoning | short orienting answer + sections |
| comparison | choose between options, pros/cons, alternatives | comparison table or clearly grouped comparison blocks |
| sequence | steps, procedure, rollout order, checklist flow | numbered steps or ordered blocks |
| branching flow | conditions, paths, decision trees, handoffs | text flow diagram or clearly branched list |
| long/complex answer | many concepts, many dependencies, high cognitive load | headings, grouped blocks, whitespace, concise summary |

This model should guide structure without turning every answer into a forced template.

---

## 5) Preferred Output Patterns

### 5.1 Compact Direct Pattern

For simple answers:
- one or two short paragraphs may be enough
- add a short list only if it genuinely improves scanability

### 5.2 Structured Analytical Pattern

For reasoning-heavy answers, the preferred pattern is:
- short answer or orienting summary
- key points or sections
- details under meaningful headings
- concise closing or next step when applicable

### 5.3 Comparison Pattern

When real alternatives exist:
- give a brief orienting statement
- use a comparison table when side-by-side evaluation improves decision quality
- recommend after comparison, not before it

### 5.4 Sequence Pattern

When order matters:
- use numbered steps or clearly ordered subsections
- do not present sequential actions as an unordered bullet list

### 5.5 Flow Pattern

When branching or handoff order matters:
- use a small text flow diagram or clearly indented decision structure
- defer diagram formatting constraints to `flow-diagram-no-frame.md`

### 5.6 Intro-Before-Structure Pattern

When using a list or table:
- add a short lead-in line if the reader needs context for why the structure is being shown
- avoid dropping large tables or lists into the answer without framing

---

## 6) Anti-Patterns to Avoid

| Anti-Pattern | Why It Hurts | Better Shape |
|--------------|--------------|--------------|
| wall of text for complex content | hard to scan and cognitively heavy | split into clear sections or shorter blocks |
| decorative headings with no function | looks structured but does not help the reader | use headings only when they represent real section purpose |
| bullet fragmentation | breaks one idea into disconnected fragments | use prose for one continuous idea |
| unordered list for ordered process | hides sequence and dependencies | use numbered steps |
| forced comparison table | adds visual weight without informational value | use normal prose or grouped bullets |
| missing framing before table/list | reader has to infer the purpose of the structure | add a short context-setting line |
| over-structuring simple answers | makes a small answer feel heavy | keep simple cases compact |
| inconsistent emphasis or heading style | weakens visual order | maintain consistent markdown hierarchy |

---

## 7) Flexibility Boundary

This rule is principle-first, not template-first.

Allowed flexibility:
- short answers may stay short
- headings are not required when the answer is naturally compact
- tables are optional unless comparison structure clearly helps
- lists may be skipped when prose is more coherent
- the structure may vary as long as readability, scanability, and semantic formatting remain strong

Not allowed:
- using flexibility as a reason to keep complex answers visually disorganized
- using decoration instead of structure
- using formatting patterns that obscure sequence, comparison, or section purpose

---

## 8) Quality Metrics

| Metric | Target |
|--------|--------|
| Main-point visibility | High |
| Section-purpose clarity | High |
| Scanability of complex answers | High |
| Semantic formatting correctness | High |
| Decorative formatting without function | 0 critical cases |
| Over-structuring simple answers | Low |
| Wall-of-text incidence in complex answers | Low |

---

## 9) Integration

| Document | Relationship |
|----------|--------------|
| [../answer-presentation.md](../answer-presentation.md) | Runtime implementation of this design |
| [accurate-communication.design.md](accurate-communication.design.md) | Clear summaries, signal density, and next-step endings |
| [explanation-quality.design.md](explanation-quality.design.md) | Reasoning structure and analytical explanation quality |
| [flow-diagram-no-frame.design.md](flow-diagram-no-frame.design.md) | Text-diagram formatting constraints |
| [document-consistency.design.md](document-consistency.design.md) | Consistency in terminology, references, and labeling |

---

> Full history: [../changelog/answer-presentation.changelog.md](../changelog/answer-presentation.changelog.md)
