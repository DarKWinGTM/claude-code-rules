# Answer Presentation

> **Current Version:** 1.23
> **Design:** [design/answer-presentation.design.md](design/answer-presentation.design.md) v1.23
> **Session:** 1b81d009-cf82-44a3-9739-cd3ea4af34dd
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

### 1.1 Purpose-First Framing Principle

When the answer is doing a diagnosis, test, recommendation, proposal, or implementation update, make that purpose visible at the start instead of letting the structure begin with setup detail only.

Required guidance:
- place one short purpose-first line near the start when the reader needs to know what the answer is doing before reading the details
- use framing such as `This test checks whether ...`, `Recommended: ...`, `The main issue is ...`, or `This update confirms ...` when that improves orientation
- do not force a dedicated purpose block into naturally simple answers whose first line already states the point clearly

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
- when a table is materially useful, keep the table light and readable rather than heavy or overbuilt
- prefer bullets or lists when the content is not genuinely tabular
- use diagrams only when sequence or branching is central
- use headings that describe section purpose, not just visual styling

### 6) Diagnostic Snapshot Principle

When reporting technical status, use a compact snapshot shape instead of a raw evidence dump.

Required guidance:
- start with one short orienting line when the reader needs context
- use short titled sections such as `Current Status`, `Request Information`, `Environment`, `Checked Scope`, or `What This Means` only when they materially improve scanability
- when an internal shorthand or abstract phrase must still appear, place a short human-language gloss or direct implication near it instead of leaving the term unexplained
- use a small fact table only for stable checked facts that are easier to scan side by side than in prose
- keep tables small, scoped, and fact-oriented
- do not let the table replace the explanation or implication
- when exact local paths, ports, or hosts appear, present them as scoped local facts rather than as portable defaults
- defer broader anti-hardcoding ownership to `portable-implementation-and-hardcoding-control.md`

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
- do not use next-stage blocks as a reason to interrupt active execution when the assistant can continue the requested work directly

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
| purpose-first framing | diagnosis, test, recommendation, proposal, implementation update | short purpose-first line before the deeper structure when needed |
| comparison | options, trade-offs, choose between X and Y | grouped comparison blocks or a light readable table when side-by-side scan helps |
| sequence | steps, rollout order, process | numbered steps or ordered subsections |
| simple status pairs | short state labels with short values | bullets, grouped blocks, or a small table only if side-by-side scan clearly helps |
| branching | conditions, paths, handoffs | text flow diagram or clearly indented branch structure |
| diagnostic snapshot | troubleshooting status, implementation progress report, verification snapshot, environment note | short orienting line + purpose-first line when needed + compact titled snapshot sections + small scoped fact table when helpful |
| scope clarification | what this is vs what it is not, what happens now vs later, current scope vs deferred scope | grouped sections such as `What this is`, `What this is not`, `What happens now`, `What stays later`, `What the user will notice` |
| phase / progress explanation | what this phase is for, what this phase got, what this prepares next | short plain-language opening + concise grouped explanation |
| full-set framing | many relevant areas, complete checklist, several review axes that should be visible together | complete set first, then optional narrowing |
| stage progression | current explanation is already sufficient and the real need is the next state or milestone | short explicit `What happens next` / `Next stage` / `Next state` block |
| goal-set review | current subtask is absorbing too much attention and the reader needs the main goal set visible again | short `Main goals now` / `Current focus` / `Why rebalance` style block |
| governing-basis ambiguity | multiple plausible policies/frames remain live and the answer changes depending on which one is chosen | short clarification block with compact basis options and one `Why it matters` line |
| post-compact continuation | the answer is resuming after compaction and exact prior state may have been compressed | short re-anchor block with current objective, carried-forward facts, needs-recheck details, and next action |
| memory-derived context | the answer materially relies on remembered path-scoped context and the reader needs to see what is remembered versus what is freshly rechecked | short memory-status block with matched path scope, provenance when relevant, and needs-recheck detail |
| variable-heavy explanation | multiple variables, fields, config keys, enum-like values, or internal labels are central to the explanation | short glossary block, variable-role table, or grouped identifier explanation before deeper reasoning |
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
- purpose-first line when the reader needs to know what the answer is doing before the sections begin
- key points or meaningful sections
- details under the correct heading
- concise closing or next step when applicable

### 2.1 Purpose-First Pattern

When the answer is doing a diagnosis, test, recommendation, proposal, or implementation update:
- place one short purpose-first line near the start if the first sentence does not already make that purpose clear
- keep the line direct and operational rather than decorative
- treat it as orientation, not as a long summary block

Preferred phrasing:
- `This test checks whether ...`
- `The main issue is ...`
- `Recommended: ...`
- `This update confirms ...`

### 3) Comparison Pattern

When real alternatives exist:
- frame the comparison briefly
- if side-by-side evaluation helps, use a light readable table or grouped comparison blocks
- recommend after the comparison is visible
- when one path is clearly preferred, surface `Recommended` before the remaining options and add one short `Why this first` reason
- when multiple reasonable options genuinely exist, keep at least one visible alternative under `Other options` instead of reducing the block to the recommendation only

### 3.0 Light Table Pattern

For ordinary answer tables:
- keep the table visually light and easy to scan
- avoid visually heavy framing for ordinary structured facts
- prefer lists or grouped blocks when the content is not genuinely tabular

### 3.1 Proposal Pattern

When the answer is surfacing a future-work idea rather than an active next step:
- label it clearly as a proposal, idea, or future wave
- show the goal
- show what it would improve
- show the expected output or result
- optionally show the success condition when it materially helps the reader evaluate the idea
- do not format a proposal block like implied queued execution

### 3.2 Governing-Basis Clarification Pattern

When multiple materially different governing bases or policies remain live and the answer would change depending on which one is chosen:
- label the block clearly as a clarification request
- show the governing basis choices compactly
- show one short `Why it matters` line
- keep the options mutually exclusive when possible
- prefer a short form-like block over a long comparison essay

### 3.3 Post-Compact Re-Anchor Pattern

When the answer is resuming after compact, present a short re-anchor block before deeper continuation when exact context may have been compressed.

Required guidance:
- label the block clearly as a post-compact re-anchor or equivalent compact state-reset note
- show the current objective compactly
- distinguish carried-forward facts from needs-recheck details when exact prior evidence may no longer be fully preserved
- show one short next-action line
- prefer one short recap block over a long conversation replay

### 3.4 Memory-Status Pattern

When the answer materially relies on remembered context:
- show the matched path scope compactly when that distinction matters
- show remembered-context status separately from freshly checked current-state facts
- show provenance session only when it materially helps trace the memory source
- show one short needs-recheck line when remembered context has not yet been revalidated against the current repo state
- keep the block compact; it should clarify the evidence source, not become a large history replay

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
- when an internal shorthand or abstract phrase must still appear, place a short human-language gloss or direct implication near it instead of leaving the term unexplained
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

### 7.1 Easy-to-Picture Phase/Progress Pattern

When answering what a phase is doing, what it got, or what it prepares next:
- start with one short plain-language line that helps the reader picture the work quickly
- then use one small grouped explanation if needed
- keep the whole explanation concise rather than expanding into a long governance-first block

### 7.1.1 Easy Explanation Pattern

When the user explicitly asks for an easier explanation, less jargon, or plain Thai wording:
- start with one short plain-language line that says what the answer is about
- prefer grouped explanation blocks with human-readable headings over raw internal/system headings
- keep the same simple wording level across later sections instead of starting simple and then switching back to jargon-heavy blocks
- if several items are being explained, prefer a repeated simple shape such as `คืออะไร`, `ทำไมสำคัญ`, `ถ้าลืมจะเกิดอะไร`, or equivalent plain-language groupings when that improves readability
- if a technical label still needs to appear, keep the plain-language explanation visually first and place the technical label as a secondary anchor
- use this pattern only when it materially improves understanding; do not force it into naturally simple one-line answers

### 7.1 Variable-Role Pattern

When multiple variables, fields, config keys, enum-like values, or internal labels are central to the explanation:
- add one short lead-in line so the reader knows why the identifier block is being shown
- use a small glossary-style block, variable-role table, or grouped bullets before the deeper reasoning
- explain what each identifier is, what role it plays, and what important values mean
- keep the structure compact; this pattern should reduce decoding effort, not create a giant glossary for simple answers

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
- use a short grouped forward-moving block only when the user genuinely needs that visibility or the assistant has reached a real boundary

Preferred labels:
- `Recommended`
- `Why this first`
- `Other options`
- `What happens next`
- `Next stage`
- `Next state`
- `Next milestone`

### 10) Canonical Snapshot Shapes

When a compact technical status note would help, the following snapshot shapes are preferred examples rather than rigid mandatory templates.

#### Example shape A: Sectioned snapshot

```markdown
The main issue is that startup succeeds but the database handoff still fails.

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
Recommended
- move to the implementation checklist

Why this first
- the current scope is already clear, so execution now adds more value than further same-scope explanation

Other options
- deepen the same scope further
- jump ahead into deferred work
```

### 14) Framed-Structure Pattern

Before a large list or table:
- provide one short context-setting sentence when the reader needs orientation
- do not drop structure into the response without purpose framing

### 15) Canonical Variable-Role Shape

```markdown
Before the deeper reasoning, here is what the key identifiers mean:

| Identifier | What it is | Role in the flow | Important values mean |
|-----------|------------|------------------|-----------------------|
| `tokenValue` | the real secret value | used when the system actually calls the API | `null` = no usable secret is stored |
| `hasSecretMaterial` | secret-present flag | tells whether the current state still has the real secret | `false` = metadata only |
| `secretMaterialSource` | origin of the current state | tells whether the state came from discovery or reveal | `inventory_or_search` = discovered state, `reveal_endpoint` = revealed state |

What this means: the user can understand the later reasoning without having to decode raw identifiers on the fly.
```

### 16) Canonical Post-Compact Re-Anchor Shape

```markdown
Post-compact re-anchor
- Current objective: continue the active work already selected by the user

Carried-forward facts
- the governing basis is already chosen
- the active touched scope is unchanged

Needs recheck
- exact payload wording or exact previously checked evidence that may have been compressed away

Next action
- continue the active path if the remaining state is still clear; otherwise recheck the exact missing detail before treating it as verified fact
```

### 16.1) Canonical Memory-Status Shape

```markdown
Memory status
- Matched path scope: `/home/node/workplace/AWCLOUD/CLAUDE/NodeClaw-platform/`
- Provenance: remembered from applicable path-scoped memory
- Freshly checked now: current repo state not yet revalidated
- Needs recheck: confirm the current code/config still matches the remembered context before treating it as verified fact
```

### 17) Canonical Governing-Basis Clarification Shape

```markdown
Clarification needed
- Governing basis: which policy/frame should control the answer?

Why it matters
- the downstream answer changes depending on which basis we use

Choose one
1. official semantic truth
2. full comparison of possible interpretations
3. conservative operational policy

Other
- tell me the policy/basis you want me to use
```

### 18) Canonical Goal-Qualified Proposal Shape

```markdown
Proposal
- build an automated visual QA verdict layer

Goal
- turn screenshot capture/compare output into a review result that is easier to act on

Improvement
- reduce the manual work needed to interpret raw compare artifacts

Output
- a machine-readable QA summary with per-device verdicts and concise regression notes

Success condition
- a compare workflow can end with a usable verdict artifact instead of raw screenshots/diff data only
```

### 19) Canonical Purpose-First Shape

```markdown
This test checks whether the setting actually changes Claude Code behavior.

Checked Scope
- current config
- runtime behavior after the setting change

What This Means
- if behavior changes, the setting is live
- if behavior does not change, the setting is not taking effect
```

### 20) Canonical Light Table Shape

For ordinary answer tables, prefer a light readable shape rather than a visually heavy one.

### 21) Canonical List-Instead-of-Table Shape

```markdown
Current work order:
1. phase/design/TODO/changelog sync
2. schema/model migration
3. store/query rewrite
4. tests and verification
```


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
| structure starts with setup but not the purpose | the reader has to infer what the answer is doing from later sections | place one short purpose-first line near the start when needed |
| full-frame ASCII or boxed table used for ordinary structured facts | visual weight increases without adding real semantic value | use a lighter readable table or switch to a list/grouped block |
| oversized or overbuilt table used as the ordinary default | the output becomes heavier than the information needs | keep the table light or switch to a list/grouped block |
| machine-specific value presented like a reusable default | local fact is mistaken for a portable contract | label it as a checked local fact or switch to a portable placeholder |
| scope boundaries buried in long prose | the reader cannot tell what is active now versus deferred | use grouped scope-boundary sections |
| drilling down before the full set is visible | the reader sees only a narrow slice and may miss the real overall scope | show the full relevant set first |
| repeating deeper options when the current stage is already sufficient | the answer feels stuck in the same scope instead of moving forward | add a short `Recommended` / `Why this first` / `Other options` block or a short `What happens next` block |
| oversized table for a small issue | increases visual weight without helping the decision | keep tables small and scoped or use prose |
| table-only status report with no implication | facts are visible, but meaning stays unclear | add one short implication or next-action line |
| raw variables/fields dumped with no role explanation | the reader sees identifiers but must decode them alone | add a short glossary block, grouped bullets, or a small variable-role table before deeper reasoning |
| metaphor-heavy or abstract internal phrase left unglossed in a structured answer | the layout looks organized but the reader still has to decode the meaning alone | add a short gloss, implication line, or direct rewrite near the term |
| future work presented like the next automatic step | the reader cannot tell whether the assistant is proposing an idea or already queueing execution | label it as a proposal and show goal, improvement, output, and optional success condition |
| governing-basis ambiguity answered with a long branch-comparison essay before the user chooses a basis | the clarification is buried inside unnecessary structure | use a short compact clarification block with basis choices and one `Why it matters` line |
| post-compact continuation presented as a long conversation replay | the user has to reread stale history instead of seeing the active state quickly | use one short post-compact re-anchor block with current objective, carried-forward facts, needs-recheck detail, and next action |
| remembered context shown like freshly checked current truth | the reader cannot tell what is recalled versus what is revalidated now | use one short memory-status block that separates matched scope, provenance when relevant, and needs-recheck detail |
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
- next-stage sections are optional unless forward movement is the useful next step and the assistant is not simply able to continue the active objective directly
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
| Purpose-first visibility | High when diagnosis/test/recommendation/proposal answers need fast orientation |
| Section-purpose clarity | High |
| Scanability of complex answers | High |
| Semantic formatting correctness | High |
| Diagnostic snapshot usefulness | High when technical status reporting is used |
| Scope-boundary scanability | High when current-vs-later explanation is used |
| Full-set-first scanability | High when the real decision surface is a larger whole |
| Next-stage visibility | High when the current scope is already sufficient |
| Compact-table efficiency | High when a table is genuinely useful |
| Unnecessary boxed-table incidence | 0 critical cases |
| Decorative formatting without function | 0 critical cases |
| Over-structuring simple answers | Low |
| Wall-of-text incidence in complex answers | Low |

---

## Integration

Related rules:
- [accurate-communication.md](accurate-communication.md) - keeps summaries, signal density, bounded technical snapshot wording, human-language glosses, memory-derived-context disclosure wording, and continuation-vs-option policy useful
- [explanation-quality.md](explanation-quality.md) - shapes analytical reasoning, layered explanation flow, full-set-first framing, and stage progression logic
- [memory-governance-and-session-boundary.md](memory-governance-and-session-boundary.md) - owns memory applicability, root `MEMORY.md` index behavior, path scope, session provenance, and archive semantics
- [flow-diagram-no-frame.md](flow-diagram-no-frame.md) - governs text diagrams used for branching or sequence
- [document-consistency.md](document-consistency.md) - keeps labels, references, and terminology consistent

---
