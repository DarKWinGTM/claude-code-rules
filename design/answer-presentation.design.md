# Answer Presentation

## 0) Document Control

> **Parent Scope:** RULES System Design
> **Current Version:** 1.7
> **Session:** dd0bf4af-a66b-4b07-bb9d-a90a0e57b54e (2026-04-02)

---

## 1) Goal

Define one first-class rule chain for answer presentation so responses are orderly, readable, scannable, and visually disciplined without forcing one rigid template onto every answer.

The target behavior is principle-first and trigger-driven:
- lead with the main point when helpful
- structure by user need and answer type
- use headings, lists, tables, and spacing as semantic tools
- make compact diagnostic snapshots explicit when technical status or checked scope matters
- make scope-boundary explanations easy to scan when the answer needs to separate now vs later or what-it-is vs what-it-is-not
- help the reader see the full relevant set before optional drill-down when that is the real decision surface
- make stage progression visible when the answer should move forward rather than deepen the same scope again
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
- technical updates arrive as raw evidence dumps instead of bounded status notes
- small troubleshooting issues are presented with oversized tables or overbuilt formatting
- answers contain the right reasoning but remain hard to scan quickly
- layout becomes decorative instead of functional
- simple answers are over-structured while complex answers remain under-structured
- formatting is technically organized but still feels stiff, overbuilt, or obviously templated

This design defines presentation-layer guidance that improves readability and scanability while staying compatible with existing explanation and communication rules.
It should support natural professional communication by making structure useful without making answers feel templated or stiff.

---

## 3) Core Presentation Principles

### 3.1 Main-Point-First Principle

When user orientation matters, place the main point early.

Required guidance:
- use a short answer or short orienting statement near the start when it helps the user understand the response faster
- do not bury the conclusion deep inside the answer unless chronology truly matters

### 3.2 Structure-Follows-Intent Principle

Presentation shape should reflect the kind of answer being given.

Required guidance:
- simple factual answers may stay compact
- analytical answers should use clearer sectional structure
- comparisons should use comparison-oriented layouts
- procedures should use sequence-oriented layouts
- technical status notes should use compact snapshot-oriented layouts

### 3.3 Natural-Flow Formatting Principle

Structure should help the answer read like a strong human response, not like a rigid template.

Required guidance:
- use structure only when it helps the reader understand faster
- keep simple answers compact rather than forcing section blocks
- prefer prose continuity when one idea reads better as a short human paragraph than as fragmented bullets

### 3.4 Scannability-Over-Density Principle

When answers become longer or more complex, scanability should improve rather than degrade.

Required guidance:
- use headings to separate different purposes
- use whitespace to separate conceptual blocks
- avoid dense uninterrupted text when structure would improve reading speed

### 3.5 Semantic Formatting Principle

Formatting should communicate meaning, not decoration.

Required guidance:
- use bullets for grouped items
- use numbered lists for ordered steps or sequences
- use tables for real comparison or structured facts only
- use diagrams only when sequence or branching is central
- ensure headings are short, functional, and content-representative

### 3.6 Diagnostic Snapshot Principle

When reporting technical status, present the snapshot as a compact structured note rather than as a raw dump.

Required guidance:
- start with one orienting line before the snapshot when context is needed
- use short titled sections such as `Current Status`, `Request Information`, `Environment`, `Checked Scope`, or `What This Means` only when they materially improve scanability
- use small fact tables only for stable checked facts that are easier to scan side by side than in prose
- keep snapshot tables narrow, scoped, and fact-oriented
- do not let the table replace the explanation or implication
- when exact local paths, ports, or hosts appear, present them as scoped local facts rather than as portable defaults
- defer broader anti-hardcoding ownership to `portable-implementation-and-hardcoding-control.md`

### 3.7 One-Block-One-Purpose Principle

Each paragraph, list, table, or section should have a clear job.

Required guidance:
- keep one main idea per paragraph when possible
- introduce lists and tables with a short context-setting line when needed
- do not mix multiple unrelated purposes into one section

### 3.8 Readability-Over-Decoration Principle

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
| diagnostic snapshot | troubleshooting status, implementation progress report, verification note, environment summary | short orienting line + compact titled snapshot sections + small scoped fact table when helpful |
| scope clarification | current scope vs future scope, what this is vs what this is not, staged rollout boundary | grouped section blocks such as `What this is`, `What this is not`, `What happens now`, `What stays later` |
| full-set framing | many relevant areas, complete checklist, multiple review axes that should be visible together | complete set first, then optional narrowing |
| stage progression | current explanation is already sufficient and the real need is the next state or milestone | one short progression block such as `What happens next` or `Next stage` |
| long/complex answer | many concepts, many dependencies, high cognitive load | headings, grouped blocks, whitespace, concise summary |
| rigid template feel | answer is technically structured but does not read naturally | reduce unnecessary headings/blocks and restore a more human flow |

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

### 5.6 Diagnostic Snapshot Pattern

When reporting troubleshooting or implementation status:
- begin with one short orienting line or short answer
- then surface the stable checked facts in compact titled sections
- use a small fact table only when it improves scanability for stable facts such as request details, current state, checked scope, or environment
- follow the snapshot with one short implication line or next-action line when the reader needs to know what the snapshot means

Typical section labels, when helpful:
- `Current Status`
- `Request Information`
- `Environment`
- `Checked Scope`
- `What This Means`

### 5.7 Scope-Boundary Pattern

When the answer needs to separate active scope from deferred scope, preferred grouped section labels include:
- `What this is`
- `What this is not`
- `What happens now`
- `What stays later`
- `What the user will notice`

These blocks are especially useful for roadmap, phase, rollout, and product-scope clarification responses.

### 5.7.1 Full-Set-First Pattern

When the reader should reason about a larger complete set, show that full set before narrowing into sub-items.

Preferred shapes:
- `There are 10 areas to review:` followed by the full list
- `Full checklist:` followed by the complete set
- `Complete scope:` followed by the full set and then optional drill-down

### 5.7.2 Next-Stage Pattern

When the current explanation is already sufficient, prefer a short grouped block that moves the reader forward.

Preferred labels:
- `What happens next`
- `Next stage`
- `Next state`
- `Next milestone`

### 5.8 Canonical Snapshot Shapes

When a compact technical status note would help, preferred house-style examples include:

#### Example shape A: Sectioned snapshot

```markdown
Current Status
- App boots successfully
- Database connection still fails

Checked Scope
- `backend/.env`
- `docker-compose.yml`
- startup log

What This Means
- Failure is likely in env propagation, not initial boot

Next Action
- Inspect the failing container runtime environment
```

#### Example shape B: Small fact table + implication

```markdown
| Field | Value |
|------|-------|
| Status | Failing at DB handoff |
| Checked | `.env`, compose, startup log |
| Pending | Runtime env injection |
| Next | Inspect container env source |

What this means: startup is succeeding, so the likely issue is between configuration handoff and the first database call.
```

These are canonical examples for recognizable presentation style, not rigid templates that override judgment.

### 5.9 Intro-Before-Structure Pattern

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
| raw evidence dump with no orienting line | checked facts appear but meaning stays unclear | start with a short orientation, then present the snapshot |
| scope boundaries buried in long prose | the reader cannot tell what is included now versus later | use grouped scope-boundary sections such as `What this is` / `What this is not` / `What happens now` / `What stays later` |
| drilling down before the full set is visible | the reader sees only a narrow slice and may miss the real overall scope | show the full relevant set first, then narrow |
| repeating deeper options when the current stage is already sufficient | the answer feels stuck in the same scope instead of moving forward | add a short `What happens next` or `Next stage` block |
| oversized table for a small issue | increases visual weight without helping the decision | keep tables small and scoped or use prose |
| table-only technical note with no implication | facts are visible but the reader cannot tell what they mean | add one short implication or next-action line |
| over-structuring simple answers | makes a small answer feel heavy | keep simple cases compact |
| structure feels templated rather than useful | reader notices the format more than the content | use only the smallest structure that improves scanability |
| inconsistent emphasis or heading style | weakens visual order | maintain consistent markdown hierarchy |

---

## 7) Flexibility Boundary

This rule is principle-first, not template-first.

Allowed flexibility:
- short answers may stay short
- headings are not required when the answer is naturally compact
- tables are optional unless comparison structure clearly helps
- lists may be skipped when prose is more coherent
- snapshot sections are optional unless they materially improve technical scanability
- the structure may vary as long as readability, scanability, and semantic formatting remain strong

Not allowed:
- using flexibility as a reason to keep complex answers visually disorganized
- using decoration instead of structure
- using formatting patterns that obscure sequence, comparison, or section purpose
- using snapshot tables as a substitute for orientation or explanation

---

## 8) Quality Metrics

| Metric | Target |
|--------|--------|
| Main-point visibility | High |
| Section-purpose clarity | High |
| Scanability of complex answers | High |
| Semantic formatting correctness | High |
| Diagnostic snapshot usefulness | High when technical status reporting is used |
| Decorative formatting without function | 0 critical cases |
| Over-structuring simple answers | Low |
| Wall-of-text incidence in complex answers | Low |

---

## 9) Integration

| Document | Relationship |
|----------|--------------|
| [../answer-presentation.md](../answer-presentation.md) | Runtime implementation of this design |
| [accurate-communication.design.md](accurate-communication.design.md) | Clear summaries, bounded technical snapshot wording, and next-step endings |
| [explanation-quality.design.md](explanation-quality.design.md) | Reasoning structure and layered analytical explanation quality |
| [flow-diagram-no-frame.design.md](flow-diagram-no-frame.design.md) | Text-diagram formatting constraints |
| [document-consistency.design.md](document-consistency.design.md) | Consistency in terminology, references, and labeling |

---

> Full history: [../changelog/answer-presentation.changelog.md](../changelog/answer-presentation.changelog.md)
