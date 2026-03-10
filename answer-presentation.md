# Answer Presentation

> **Current Version:** 1.0
> **Design:** [design/answer-presentation.design.md](design/answer-presentation.design.md) v1.0
> **Session:** 468e053d-9953-496e-8e83-910e2ae67402
> **Full history:** [changelog/answer-presentation.changelog.md](changelog/answer-presentation.changelog.md)

---

## Rule Statement

**Core Principle: Present answers so they are orderly, readable, and easy to scan, while keeping structure flexible enough to match the user’s actual need.**

This rule governs answer presentation at the layout layer. It does not replace reasoning-quality, truthfulness, or verification rules. Instead, it helps good content land clearly.

---

## Core Principles

### 1) Main-Point-First Principle

When user orientation matters, put the main point early.

Required guidance:
- give a short answer or orienting statement near the start when it helps the user understand faster
- do not bury the key conclusion inside avoidable detail

### 2) Structure-Follows-Intent Principle

The layout should reflect the kind of answer being given.

Required guidance:
- simple answers may stay compact
- analytical answers should become more visibly structured
- comparisons should use comparison-friendly presentation
- procedures should use ordered presentation

### 3) Scannability-Over-Density Principle

As answers grow in complexity, scanability should improve rather than collapse.

Required guidance:
- use headings for real section boundaries
- separate conceptual blocks with whitespace
- do not allow long complex answers to degrade into walls of text

### 4) Semantic Formatting Principle

Formatting should carry meaning, not decoration.

Required guidance:
- use bullets for grouped items
- use numbered lists for sequence or order
- use tables only for genuine comparison or structured facts
- use diagrams only when sequence or branching is central
- use headings that describe section purpose, not just visual styling

### 5) One-Block-One-Purpose Principle

Each paragraph, list, table, or section should do one clear job.

Required guidance:
- keep one main idea per paragraph when possible
- introduce lists and tables when framing helps readability
- avoid mixing multiple unrelated purposes into one block

### 6) Readability-Over-Decoration Principle

Readable markdown structure matters more than ornamental formatting.

Required guidance:
- avoid decorative sectioning that does not help the reader
- keep heading, emphasis, and list style consistent
- prefer plain, functional formatting over visual noise

---

## Trigger Model

Apply stronger presentation structure when one or more of these triggers are present:

| Trigger | Typical Signal | Preferred Presentation |
|--------|-----------------|------------------------|
| simple answer | factual lookup, low complexity, direct request | compact paragraph or short list |
| analytical answer | explanation, diagnosis, architectural reasoning | short orienting answer + sections |
| comparison | options, trade-offs, choose between X and Y | comparison table or grouped comparison blocks |
| sequence | steps, rollout order, process | numbered steps or ordered subsections |
| branching | conditions, paths, handoffs | text flow diagram or clearly indented branch structure |
| long answer | multiple concepts or dependencies | headings, grouped blocks, concise summary |

Do not use this trigger model to force sectioning into answers that are naturally simple.

---

## Preferred Output Patterns

### 1) Compact Direct Pattern

For simple questions:
- one or two short paragraphs may be enough
- add a short list only if it clearly improves scanability

### 2) Structured Analytical Pattern

For reasoning-heavy answers, prefer:
- short answer or orienting line
- key points or meaningful sections
- details under the correct heading
- concise closing or next step when applicable

### 3) Comparison Pattern

When real alternatives exist:
- frame the comparison briefly
- use a comparison table if side-by-side evaluation helps
- recommend after the comparison is visible

### 4) Sequence Pattern

When order matters:
- use numbered steps or clearly ordered subsections
- do not present sequence as unordered bullets

### 5) Flow Pattern

When branching or handoff order matters:
- use a small text flow diagram or equivalent indented structure
- follow `flow-diagram-no-frame.md` for diagram formatting

### 6) Framed-Structure Pattern

Before a large list or table:
- provide one short context-setting sentence when the reader needs orientation
- do not drop structure into the response without purpose framing

---

## Anti-Patterns to Avoid

| Anti-Pattern | Why It Hurts | Better Shape |
|--------------|--------------|--------------|
| wall of text for complex content | hard to scan and mentally expensive | split into sections or shorter blocks |
| decorative headings | visual noise without navigational value | use headings only for real section purpose |
| bullet fragmentation | breaks one idea into disconnected fragments | use prose for one continuous idea |
| unordered list for ordered process | hides sequence and dependencies | use numbered steps |
| forced table without true comparison | adds weight without value | use prose or grouped bullets |
| list or table with no framing | reader must infer its purpose | add a short context-setting line |
| over-structuring simple answers | makes a short answer feel heavy | keep simple answers compact |
| inconsistent heading or emphasis style | weakens visual order | keep presentation consistent |

---

## Flexibility Boundary

This rule is principle-first, not template-first.

Allowed flexibility:
- short answers may stay short
- headings are optional when the response is naturally compact
- tables are optional unless comparison structure clearly helps
- lists may be skipped when prose is more coherent
- structure may vary as long as readability, scanability, and semantic formatting remain strong

Not allowed:
- using flexibility as a reason to keep complex answers visually disorganized
- using formatting as decoration rather than meaning
- using presentation patterns that obscure sequence, comparison, or section purpose

---

## Quality Metrics

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

## Integration

Related rules:
- [accurate-communication.md](accurate-communication.md) - keeps summaries, signal density, and closing guidance useful
- [explanation-quality.md](explanation-quality.md) - shapes analytical reasoning and explanation flow
- [flow-diagram-no-frame.md](flow-diagram-no-frame.md) - governs text diagrams used for branching or sequence
- [document-consistency.md](document-consistency.md) - keeps labels, references, and terminology consistent

---
