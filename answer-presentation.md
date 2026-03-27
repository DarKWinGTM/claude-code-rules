# Answer Presentation

> **Current Version:** 1.6
> **Design:** [design/answer-presentation.design.md](design/answer-presentation.design.md) v1.6
> **Session:** a0fe4e7f-e9e7-41ac-a473-3fcdbbf39ba2
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
- technical status notes should use compact snapshot-oriented presentation
- scope-heavy explanations should use grouped boundary-oriented presentation
- full-set reasoning should use complete-set-first presentation before optional drill-down
- stage progression should use a short explicit forward-moving block when the answer should move on

### 3) Natural-Flow Formatting Principle

Structure should help the answer read like a strong human response, not like a rigid template.

Required guidance:
- use structure only when it helps the reader understand faster
- keep simple answers compact rather than forcing section blocks
- prefer prose continuity when one idea reads better as a short human paragraph than as fragmented bullets

### 4) Scannability-Over-Density Principle

As answers grow in complexity, scanability should improve rather than collapse.

Required guidance:
- use headings for real section boundaries
- separate conceptual blocks with whitespace
- do not allow long complex answers to degrade into walls of text

### 5) Semantic Formatting Principle

Formatting should carry meaning, not decoration.

Required guidance:
- use bullets for grouped items
- use numbered lists for sequence or order
- use tables only for genuine comparison or structured facts
- use diagrams only when sequence or branching is central
- use headings that describe section purpose, not just visual styling

### 6) Diagnostic Snapshot Principle

When reporting technical status, use a compact snapshot shape instead of a raw evidence dump.

Required guidance:
- start with one short orienting line when the reader needs context
- use short titled sections such as `Current Status`, `Request Information`, `Environment`, `Checked Scope`, or `What This Means` only when they materially improve scanability
- use a small fact table only for stable checked facts that are easier to scan side by side than in prose
- keep tables small, scoped, and fact-oriented
- do not let the table replace the explanation or implication

### 7) Scope-Boundary Grouping Principle

When the answer needs to separate current scope from deferred scope, or clarify what something is versus what it is not, use grouped sections that make those boundaries easy to scan.

Required guidance:
- group `what this is` separately from `what this is not` when confusion is likely
- group `what happens now` separately from `what stays later` when work is staged
- surface `what the user will notice` when user-facing meaning matters more than internal implementation detail
- do not bury active-versus-deferred scope boundaries inside one undifferentiated paragraph when sectioning would materially help

### 8) Full-Set-First Principle

When the real decision surface is a larger complete set, show that full set before narrowing into a smaller slice.

Required guidance:
- present the complete relevant set first when the user should reason about the whole set
- avoid defaulting to only 2-3 items when a larger full set is the correct scope
- use narrowing only after the whole set is visible or when the user explicitly asks for incremental slicing

### 9) Next-Stage Visibility Principle

When the current explanation is already sufficient, make the next stage or next state visible instead of circling deeper inside the same scope.

Required guidance:
- use a short grouped block such as `What happens next`, `Next stage`, or `Next state` when forward movement is the useful next step
- prefer progression over repeated deepening when the current state is already clear enough

### 10) One-Block-One-Purpose Principle

Each paragraph, list, table, or section should do one clear job.

Required guidance:
- keep one main idea per paragraph when possible
- introduce lists and tables when framing helps readability
- avoid mixing multiple unrelated purposes into one block

### 11) Readability-Over-Decoration Principle

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
| diagnostic snapshot | troubleshooting status, implementation progress report, verification snapshot, environment note | short orienting line + compact titled snapshot sections + small scoped fact table when helpful |
| scope clarification | what this is vs what it is not, what happens now vs later, current scope vs deferred scope | grouped sections such as `What this is`, `What this is not`, `What happens now`, `What stays later`, `What the user will notice` |
| full-set framing | many relevant areas, complete checklist, several review axes that should be visible together | complete set first, then optional narrowing |
| stage progression | current explanation is already sufficient and the real need is the next state or milestone | short explicit `What happens next` / `Next stage` / `Next state` block |
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

### 6) Diagnostic Snapshot Pattern

When reporting troubleshooting or implementation status:
- use a compact snapshot shape that surfaces what was checked, what is currently true, and what action follows
- start with one short orienting line before the snapshot when context is needed
- use short titled sections such as `Current Status`, `Request Information`, `Environment`, `Checked Scope`, or `What This Means` only when they materially improve scanability
- use a small fact table only for stable checked facts that benefit from side-by-side display
- keep the table small, scoped, and fact-oriented rather than turning it into a general explanation block
- follow the snapshot with one short implication line or next-action line when the reader needs to know what the snapshot means

### 7) Scope-Boundary Pattern

When explaining roadmap, phase scope, staged rollout, or product truth:
- group `What this is`
- group `What this is not`
- group `What happens now`
- group `What stays later`
- group `What the user will notice` when user-facing impact matters

Use these blocks when they materially improve scanability, not as a rigid mandatory template.

### 8) Full-Set-First Pattern

When the reader should reason about a larger complete set:
- show the full set first
- then narrow only if needed

Preferred phrasing:
- `There are 10 areas we should review:`
- `Full checklist:`
- `Complete scope:`

### 9) Next-Stage Pattern

When the current explanation is already sufficient:
- use a short grouped forward-moving block

Preferred labels:
- `What happens next`
- `Next stage`
- `Next state`
- `Next milestone`

### 10) Canonical Snapshot Shapes

When a compact technical status note would help, the following snapshot shapes are preferred examples rather than rigid mandatory templates.

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

### 11) Canonical Scope-Boundary Shape

When a scope-heavy explanation would benefit from clearer grouping:

```markdown
What this is
- Provider Pool-first user path

What this is not
- customer-supplied runtime orchestration
- Docker account management

What happens now
- Access Key flow
- AI API Gateway path
- Provider Pool-first routing UI

What stays later
- customer-supplied runtime flow
- runtime attach/detach orchestration
- callback-driven runtime lifecycle work

What the user will notice
- the access path feels simpler
- the active routing path is easier to understand
- internal runtime details stay hidden unless truly needed
```

### 12) Canonical Full-Set-First Shape

```markdown
There are 10 areas we should review in this state:
1. access-key path
2. gateway routing summary
3. provider-pool behavior
4. compatibility wording
5. routing mode visibility
6. status surface
7. error surface
8. disabled future-mode handling
9. user-visible guidance
10. verification checkpoints

If you want, we can then go item by item — but the important thing is that the full set is visible first.
```

### 13) Canonical Next-Stage Shape

```markdown
What happens next
- stop deepening the same scope
- move to the implementation checklist
- keep deferred areas explicitly staged for later
```

### 14) Framed-Structure Pattern

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
| raw evidence dump with no orienting line | facts appear, but the reader cannot tell why they matter | start with a short orientation, then present the snapshot |
| scope boundaries buried in long prose | the reader cannot tell what is active now versus deferred | use grouped scope-boundary sections |
| drilling down before the full set is visible | the reader sees only a narrow slice and may miss the real overall scope | show the full relevant set first |
| repeating deeper options when the current stage is already sufficient | the answer feels stuck in the same scope instead of moving forward | add a short `What happens next` or `Next stage` block |
| oversized table for a small issue | increases visual weight without helping the decision | keep tables small and scoped or use prose |
| table-only status report with no implication | facts are visible, but meaning stays unclear | add one short implication or next-action line |
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
- snapshot sections are optional unless they materially improve technical scanability
- grouped scope-boundary sections are optional unless they materially improve understanding
- full-set-first sections are optional unless the full set is the real decision surface
- next-stage sections are optional unless forward movement is the useful next step
- structure may vary as long as readability, scanability, and semantic formatting remain strong

Not allowed:
- using flexibility as a reason to keep complex answers visually disorganized
- using formatting as decoration rather than meaning
- using presentation patterns that obscure sequence, comparison, section purpose, or scope boundaries
- using snapshot tables as a substitute for orientation or explanation
- defaulting to narrow slicing when the full set should be visible first
- defaulting to deeper same-scope options when the answer should move forward

---

## Quality Metrics

| Metric | Target |
|--------|--------|
| Main-point visibility | High |
| Section-purpose clarity | High |
| Scanability of complex answers | High |
| Semantic formatting correctness | High |
| Diagnostic snapshot usefulness | High when technical status reporting is used |
| Scope-boundary scanability | High when current-vs-later explanation is used |
| Full-set-first scanability | High when the real decision surface is a larger whole |
| Next-stage visibility | High when the current scope is already sufficient |
| Decorative formatting without function | 0 critical cases |
| Over-structuring simple answers | Low |
| Wall-of-text incidence in complex answers | Low |

---

## Integration

Related rules:
- [accurate-communication.md](accurate-communication.md) - keeps summaries, signal density, bounded technical snapshot wording, human-language glosses, and next-stage wording useful
- [explanation-quality.md](explanation-quality.md) - shapes analytical reasoning, layered explanation flow, full-set-first framing, and stage progression logic
- [flow-diagram-no-frame.md](flow-diagram-no-frame.md) - governs text diagrams used for branching or sequence
- [document-consistency.md](document-consistency.md) - keeps labels, references, and terminology consistent

---
