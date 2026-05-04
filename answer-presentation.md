# Answer Presentation
> **Current Version:** 1.26
> **Design:** [design/answer-presentation.design.md](design/answer-presentation.design.md) v1.26
> **Session:** d42465eb-30a7-4bc8-b9d6-03e52306e9a5
> **Full history:** [changelog/answer-presentation.changelog.md](changelog/answer-presentation.changelog.md)
---
## Rule Statement
**Core Principle: Present answers so they are orderly, readable, and easy to scan, while keeping structure flexible enough to match the user's actual need.**
This rule owns layout and scanability. It does not replace reasoning quality, truthfulness, verification, evidence wording, or execution-continuity ownership.
---
## Core Principles
### 1) Main point and purpose first
Put the main point early when orientation matters.
Required guidance:
- give a short answer or orienting statement near the start when it helps understanding
- for diagnosis, test, recommendation, proposal, or implementation update, make the purpose visible before setup detail
- useful frames include `This test checks whether ...`, `Recommended: ...`, `The main issue is ...`, and `This update confirms ...`
- do not add a separate purpose block when the first sentence already states the point
- do not bury the key conclusion inside avoidable background
### 2) Structure follows intent
Layout should match the answer type.
Required guidance:
- simple answers may stay compact
- analytical answers should use meaningful sections when complexity rises
- comparisons should use comparison-friendly grouping or a light table
- procedures should use ordered lists
- technical status should use compact snapshot-oriented presentation
- scope-heavy explanations should separate active/current scope from deferred or excluded scope
- full-set reasoning should show the complete relevant set before narrowing
- stage progression should make the next state visible when the current stage is already clear
### 3) Natural flow and semantic formatting
Structure should help the answer read like a capable human response, not a rigid template.
Required guidance:
- use headings only for real section boundaries
- use bullets for grouped items and numbered lists for sequence
- use a light table when side-by-side structure materially improves comprehension
- keep tables small, scoped, and readable; do not use heavy boxed tables for ordinary facts
- prefer prose when one idea reads better as one continuous paragraph
- use diagrams only when sequence or branching is central, following `flow-diagram-no-frame.md`
- every paragraph, list, table, or section should have one clear purpose
- formatting must carry meaning, not decoration
### 4) Diagnostic snapshot
When reporting technical status, use a compact snapshot instead of a raw evidence dump.
Required guidance:
- start with one short orienting line when context is needed
- use short sections such as `Current Status`, `Checked Scope`, `What This Means`, or `Next Action` only when they improve scanability
- use a small fact table only when stable checked facts scan better side by side
- keep exact local paths, ports, and hosts scoped as local facts, not portable defaults
- add one implication or next-action line when a table alone would leave meaning unclear
- snapshot wording honesty defers to `technical-snapshot-communication.md`
### 5) Scope-boundary pattern
When confusion is likely, separate what something is from what it is not.
Required guidance:
- group `What this is` separately from `What this is not`
- group `What happens now` separately from `What stays later`
- include `What the user will notice` when user-facing meaning matters
- do not bury active-versus-deferred scope boundaries inside one long paragraph when grouping would help
### 6) Full-set-first pattern
When the real decision surface is a larger complete set, show that set before narrowing.
Required guidance:
- present the complete relevant set first when the user should reason about the whole set
- avoid defaulting to only 2-3 items when the correct scope is larger
- narrow only after the whole set is visible or when the user explicitly asks for incremental slicing
### 7) Next-stage pattern
When the current explanation is sufficient, show the next state instead of circling deeper.
Required guidance:
- use a short `What happens next`, `Next stage`, or `Next state` block when forward movement is useful
- prefer progression over repeated deepening when the current state is already clear
- do not use next-stage blocks as a reason to interrupt active execution when safe continuation is possible
### 8) Specialized compact patterns
| Pattern | Use when | Required preservation |
|---|---|---|
| Light table | repeated dimensions, field roles, trade-offs, diagnostic facts | small, readable, side-by-side only when useful |
| Variable-role | several identifiers, config keys, fields, enum values | explain what each identifier is, its role, and important values |
| Governing-basis clarification | multiple policies/frames change the answer | ask for basis first with one `Why it matters` line |
| Post-compact re-anchor | compact may have compressed exact evidence | current objective, carried-forward facts, needs-recheck, next action |
| Memory-status | remembered context materially affects the answer | matched path scope, remembered vs freshly checked status, needs-recheck |
| Phase-backed closeout | closing phase-backed work | delivered work, feature/improvement, impact, verification, next phase state when relevant |
| Proposal | future work not yet selected | label as proposal/idea/future wave; show goal, improvement, output, optional success condition |
| Easy explanation | user asks for plain Thai, easier wording, or less jargon | human-meaning-first headings and technical labels second |
---
## Trigger Model
| Trigger | Preferred presentation |
|---|---|
| simple answer | compact paragraph or short list |
| analytical / long answer | short orientation, meaningful headings, grouped details, concise synthesis |
| purpose-first framing | one direct purpose line before supporting detail |
| comparison | grouped comparison or light table, then recommendation when justified |
| sequence / branching | numbered steps, ordered subsections, or small text flow |
| diagnostic snapshot | orienting line, checked facts, current state, implication, next action |
| scope clarification | grouped current/deferred and is/is-not sections |
| phase/progress or closeout | plain-language opening plus delivery/feature/impact/verification/next-state grouping |
| full-set or stage progression | complete set first; short next-state block when useful |
| goal-set review | `Main goals now` / `Current focus` / `Why rebalance` style block |
| governing-basis ambiguity | compact clarification block before deep branch analysis |
| post-compact or memory-derived context | compact re-anchor/status before selected-path continuation |
| variable-heavy explanation | short glossary, grouped identifiers, or variable-role table |
Do not force sectioning into naturally simple answers.
---
## Preferred Output Shapes
- **Compact direct:** one or two short paragraphs, with a short list only if it improves scanability.
- **Structured analytical:** short answer/orientation, optional purpose line, meaningful sections, details under the right section, concise synthesis or next action.
- **Comparison:** brief framing, light table only when useful, `Recommended` plus `Why this first` when one path is stronger, and a real `Other options` alternative when paths remain live.
- **Diagnostic snapshot:** orienting line plus `Current`, `Checked`, `Meaning`, and `Next`; use a fact table only when stable facts scan better, and add one implication or next-action line.
- **Scope-boundary:** `What this is`, `What this is not`, `What happens now`, `What stays later`, and `What the user will notice` when those boundaries matter.
- **Phase-backed closeout:** `What this phase delivered`, `Feature / Improvement`, `Impact`, `Verification`, and `Next phase state`; use only fields that improve clarity and do not force this onto trivial non-phase completions.
- **Full-set / next-stage / recommendation:** show the complete relevant set first, then state the next stage or recommendation with one reason and preserve real alternatives.
- **Variable-role / post-compact / memory / basis / proposal:** explain identifier roles; use current objective / carried-forward facts / needs-recheck / next action; separate remembered from freshly checked state; ask governing basis first; label future work as advisory with goal, improvement, output, and optional success condition.
---
## Anti-Patterns
| Anti-pattern | Better shape |
|---|---|
| wall of text, decorative headings, or bullet fragmentation | use meaningful sections or prose where each unit has one purpose |
| unordered list for ordered process | use numbered steps |
| forced/heavy table without scanability gain | use prose, grouped blocks, or a light table only when useful |
| list/table with no framing or implication | add context plus meaning or next action |
| raw evidence dump or table-only status | orient, snapshot, then explain implication |
| setup detail before purpose | place the purpose-first line early |
| local value presented as portable default | label as scoped local fact or use placeholder |
| scope boundaries buried in prose | group active/deferred and is/is-not sections |
| drilling down before full set is visible | show complete relevant set first |
| deeper same-scope options after stage is clear | move to next stage/state |
| raw identifiers with no role explanation | use variable-role pattern |
| future work phrased like queued execution | label as proposal and show goal/output |
| governing-basis ambiguity answered with long branches | ask compactly for the governing basis first |
| post-compact replay or remembered context as fresh truth | use compact re-anchor/status and separate recheck needs |
| over-structuring simple answers | keep simple answers compact |
---
## Flexibility Boundary
Allowed: short answers may stay short; headings, tables, snapshots, scope blocks, full-set blocks, and next-stage blocks are optional unless they improve comprehension; structure may vary as long as readability, scanability, and semantic formatting remain strong.
Not allowed: using flexibility to keep complex answers disorganized; using formatting as decoration; obscuring sequence, comparison, scope, or section purpose; using snapshot tables as a substitute for orientation or implication; defaulting to a narrow slice when the full set should be visible; defaulting to deeper same-scope explanation when the answer should move forward.
---
## Quality Metrics
| Metric | Target |
|---|---|
| Main-point and purpose visibility | high when needed |
| Section-purpose clarity, scanability, and semantic formatting | high |
| Diagnostic, scope, full-set, next-stage, and compact-table usefulness | high when relevant |
| Unnecessary boxed table or decorative formatting | 0 critical cases |
---
## Integration
Related rules:
- [accurate-communication.md](accurate-communication.md) - evidence-honest wording, human-language glosses, memory disclosure, continuation policy
- [technical-snapshot-communication.md](technical-snapshot-communication.md) - bounded snapshot wording semantics
- [response-closing-and-action-framing.md](response-closing-and-action-framing.md) - closing synthesis, recommendations, alternatives, advisory proposals
- [explanation-quality.md](explanation-quality.md) - explanation flow, full-set-first logic, stage progression
- [memory-governance-and-session-boundary.md](memory-governance-and-session-boundary.md) - memory applicability and path scope
- [flow-diagram-no-frame.md](flow-diagram-no-frame.md) - text diagram formatting
- [document-consistency.md](document-consistency.md) - labels, references, and terminology consistency
---
