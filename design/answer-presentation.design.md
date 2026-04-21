# Answer Presentation

## 0) Document Control

> **Parent Scope:** RULES System Design
> **Current Version:** 1.25
> **Session:** a9bec472-1706-4019-8cfd-5ba988a71662 (2026-04-17)

---

## 1) Goal

Define one first-class rule chain for answer presentation so responses are orderly, readable, scannable, and visually disciplined without forcing one rigid template onto every answer.

The target behavior is principle-first and trigger-driven:
- lead with the main point when helpful
- show the purpose early when the answer is doing diagnosis, testing, recommendation, proposal, or implementation reporting
- structure by user need and answer type
- use headings, lists, tables, and spacing as semantic tools
- defer ordinary answer-table usage and style semantics to a dedicated central owner when table governance becomes first-class
- keep broader presentation structure responsible for framing and scanability around the chosen table/list shape
- make compact diagnostic snapshots explicit when technical status or checked scope matters
- make variable-heavy explanations easier to scan by allowing short glossary blocks or small variable-role tables before deeper reasoning
- keep metaphor-heavy or abstract internal phrases from being left visually unexplained when a short gloss or implication line would make the practical meaning clear
- support easy-explanation layouts where plain-language headings stay visually primary when the user explicitly asked for simpler wording
- make scope-boundary explanations easy to scan when the answer needs to separate now vs later or what-it-is vs what-it-is-not
- help the reader see the full relevant set before optional drill-down when that is the real decision surface
- make stage progression visible when the answer should move forward rather than deepen the same scope again
- make easy-to-picture phase/progress explanations easy to present through one short plain-language opening plus a concise grouped explanation
- make materially outcome-changing governing-basis ambiguity easy to present as a short structured clarification instead of a long branch-comparison essay
- make post-compact continuation easy to present as one short re-anchor block instead of a long replay
- make memory-derived context easy to present as one short block that separates matched path scope, provenance when relevant, and needs-recheck detail from freshly checked current-state facts
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
- ordinary structured facts are presented with full-frame ASCII / boxed tables or generic dense pipe-table styling because table semantics are not yet centralized enough
- technical updates arrive as raw evidence dumps instead of bounded status notes
- small troubleshooting issues are presented with oversized tables or overbuilt formatting
- an answer can look well-structured while still leaving metaphor-heavy or abstract internal wording unexplained
- answers contain the right reasoning but remain hard to scan quickly
- the structure begins with setup detail while the answer purpose stays implicit until later
- layout becomes decorative instead of functional
- simple answers are over-structured while complex answers remain under-structured
- formatting is technically organized but still feels stiff, overbuilt, or obviously templated
- materially different governing-basis options are explained through long comparison prose when the real need is one short structured clarification block
- post-compact continuation is presented as a long replay of the prior conversation instead of a short active-state re-anchor

This design defines presentation-layer guidance that improves readability and scanability while staying compatible with existing explanation and communication rules.
It should support natural professional communication by making structure useful without making answers feel templated or stiff.

---

## 3) Core Presentation Principles

### 3.1 Main-Point-First Principle

When user orientation matters, place the main point early.

Required guidance:
- use a short answer or short orienting statement near the start when it helps the user understand the response faster
- do not bury the conclusion deep inside the answer unless chronology truly matters

### 3.1.1 Purpose-First Framing Principle

When the answer is doing diagnosis, testing, recommendation, proposal, or implementation reporting, the layout should make that purpose visible near the start rather than letting the structure begin with setup detail only.

Required guidance:
- place one short purpose-first line near the start when the reader needs to know what the answer is doing before reading deeper sections
- use direct operational phrasing such as `This test checks whether ...`, `The main issue is ...`, `Recommended: ...`, or `This update confirms ...` when that improves orientation
- do not force a dedicated purpose block into naturally simple answers whose first sentence already states the point clearly

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
- use a light table when side-by-side structure materially improves comprehension for comparison, stable structured facts, analytical clarification, diagnostic fact sets, or multi-field explanation
- keep ordinary tables light and readable rather than heavy or overbuilt
- prefer lists or grouped blocks when the content is not genuinely tabular or when a table would add more weight than scanability
- use diagrams only when sequence or branching is central
- ensure headings are short, functional, and content-representative

### 3.6 Diagnostic Snapshot Principle

When reporting technical status, present the snapshot as a compact structured note rather than as a raw dump.

Required guidance:
- start with one orienting line before the snapshot when context is needed
- use short titled sections such as `Current Status`, `Request Information`, `Environment`, `Checked Scope`, or `What This Means` only when they materially improve scanability
- when an internal shorthand or abstract phrase must still appear, place a short human-language gloss or direct implication near it instead of leaving the term unexplained
- proactively prefer a small fact table when several stable checked facts, dimensions, or status fields are easier to scan side by side than in prose
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
| purpose-first framing | diagnosis, test, recommendation, proposal, implementation update | short purpose-first line before the deeper structure when needed |
| comparison | choose between options, pros/cons, alternatives | grouped comparison blocks or a light readable table when side-by-side scan helps |
| sequence | steps, procedure, rollout order, checklist flow | numbered steps or ordered blocks |
| simple status pairs | short state labels with short values | bullets, grouped blocks, or a small table only if side-by-side scan clearly helps |
| branching flow | conditions, paths, decision trees, handoffs | text flow diagram or clearly branched list |
| diagnostic snapshot | troubleshooting status, implementation progress report, verification note, environment summary | short orienting line + purpose-first line when needed + compact titled snapshot sections + small scoped fact table when helpful |
| scope clarification | current scope vs future scope, what this is vs what this is not, staged rollout boundary | grouped section blocks such as `What this is`, `What this is not`, `What happens now`, `What stays later` |
| full-set framing | many relevant areas, complete checklist, multiple review axes that should be visible together | complete set first, then optional narrowing |
| stage progression | current explanation is already sufficient and the real need is the next state or milestone | one short progression block such as `What happens next` or `Next stage` |
| variable-heavy explanation | multiple variables, fields, config keys, enum-like values, or internal labels are central to the explanation | short glossary block, variable-role table, or grouped identifier explanation before deeper reasoning |
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
- purpose-first line when the reader needs to know what the answer is doing before the sections begin
- key points or sections
- details under meaningful headings
- concise closing or next step when applicable

### 5.2.1 Purpose-First Pattern

When the answer is doing diagnosis, testing, recommendation, proposal, or implementation reporting:
- place one short purpose-first line near the start if the first sentence does not already make that purpose clear
- keep the line direct and operational rather than decorative
- treat it as orientation, not as a long summary block

Preferred phrasing:
- `This test checks whether ...`
- `The main issue is ...`
- `Recommended: ...`
- `This update confirms ...`

### 5.3 Comparison Pattern

When real alternatives exist:
- give a brief orienting statement
- if side-by-side evaluation improves decision quality, use a light readable table or grouped comparison blocks
- recommend after comparison, not before it
- when one path is clearly preferred, surface `Recommended` first and add one short `Why this first` reason before listing the remaining options
- when multiple reasonable options genuinely exist, keep at least one visible alternative instead of reducing the block to the recommendation only

### 5.3.0 Light Table Pattern

For ordinary answer tables:
- keep the table visually light and easy to scan
- avoid visually heavy framing for ordinary structured facts
- prefer lists or grouped blocks when the content is not genuinely tabular

### 5.3.1 Proposal Pattern

When the answer is surfacing a future-work idea rather than an active next step:
- label it clearly as a proposal, idea, or future wave
- show the goal
- show what it would improve
- show the expected output or result
- optionally show the success condition when it materially helps the reader evaluate the idea
- do not format a proposal block like implied queued execution

### 5.3.2 Governing-Basis Clarification Pattern

When multiple materially different governing bases or policies remain live and the answer would change depending on which one is chosen:
- label the block clearly as a clarification request
- show the governing basis choices compactly
- show one short `Why it matters` line
- keep the options mutually exclusive when possible
- prefer a short form-like block over a long comparison essay

### 5.3.3 Post-Compact Re-Anchor Pattern

When the answer is resuming after compact, present a short re-anchor block before deeper continuation when exact context may have been compressed.

Required guidance:
- label the block clearly as a post-compact re-anchor or equivalent compact state-reset note
- show the current objective compactly
- distinguish carried-forward facts from needs-recheck details when exact prior evidence may no longer be fully preserved
- show one short next-action line
- prefer one short recap block over a long conversation replay

### 5.3.4 Memory-Status Pattern

When the answer materially relies on remembered context:
- show the matched path scope compactly when that distinction matters
- show remembered-context status separately from freshly checked current-state facts
- show provenance session only when it materially helps trace the memory source
- show one short needs-recheck line when remembered context has not yet been revalidated against the current repo state
- keep the block compact; it should clarify the evidence source, not become a large history replay

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

### 5.7.0 Governing-Basis Clarification Pattern

When multiple materially different governing bases or policies remain live and the answer would change depending on which one is chosen:
- label the block clearly as a clarification request
- show the governing basis choices compactly
- show one short `Why it matters` line
- keep the options mutually exclusive when possible
- prefer a short form-like block over a long comparison essay

### 5.7.1 Variable-Role Pattern

When multiple variables, fields, config keys, enum-like values, or internal labels are central to the explanation:
- add one short lead-in line so the reader knows why the identifier block is being shown
- use a small glossary-style block, variable-role table, or grouped bullets before the deeper reasoning
- explain what each identifier is, what role it plays, and what important values mean
- keep the structure compact; this pattern should reduce decoding effort rather than create a giant glossary for simple answers

### 5.7.2 Full-Set-First Pattern

When the reader should reason about a larger complete set, show that full set before narrowing into sub-items.

Preferred shapes:
- `There are 10 areas to review:` followed by the full list
- `Full checklist:` followed by the complete set
- `Complete scope:` followed by the full set and then optional drill-down

### 5.7.3 Next-Stage Pattern

When the current explanation is already sufficient, prefer a short grouped block that moves the reader forward.

Preferred labels:
- `Recommended`
- `Why this first`
- `Other options`
- `What happens next`
- `Next stage`
- `Next state`
- `Next milestone`

Boundary guidance:
- next-stage blocks are optional presentation tools
- they should not interrupt active execution when the assistant can continue the requested work directly
- use them when the user genuinely needs stage visibility or a real boundary has been reached

### 5.8 Canonical Snapshot Shapes

When a compact technical status note would help, preferred house-style examples include:

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

These are canonical examples for recognizable presentation style, not rigid templates that override judgment.

### 5.9 Intro-Before-Structure Pattern

When using a list or table:
- add a short lead-in line if the reader needs context for why the structure is being shown
- avoid dropping large tables or lists into the answer without framing

### 5.10 Canonical Governing-Basis Clarification Shape

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

### 5.11 Canonical Post-Compact Re-Anchor Shape

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

### 5.11.1 Canonical Memory-Status Shape

```markdown
Memory status
- Matched path scope: `/home/node/workplace/AWCLOUD/CLAUDE/NodeClaw-platform/`
- Provenance: remembered from applicable path-scoped memory
- Freshly checked now: current repo state not yet revalidated
- Needs recheck: confirm the current code/config still matches the remembered context before treating it as verified fact
```

### 5.11.2 Canonical Light Table Shape

For ordinary answer tables, prefer a light readable shape rather than a visually heavy one.

### 5.12 Canonical Variable-Role Shape

```markdown
Before the deeper reasoning, here is what the key identifiers mean:

| Identifier | What it is | Role in the flow | Important values mean |
|-----------|------------|------------------|-----------------------|
| `tokenValue` | the real secret value | used when the system actually calls the API | `null` = no usable secret is stored |
| `hasSecretMaterial` | secret-present flag | tells whether the current state still has the real secret | `false` = metadata only |
| `secretMaterialSource` | origin of the current state | tells whether the state came from discovery or reveal | `inventory_or_search` = discovered state, `reveal_endpoint` = revealed state |

What this means: the user can understand the later reasoning without having to decode raw identifiers on the fly.
```

### 5.13 Canonical Goal-Qualified Proposal Shape

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

### 5.13.1 Canonical Markdown-Table Exception Shape

Use literal markdown-table syntax only when the user explicitly asks for it or when the target artifact is markdown source.

```markdown
| เรื่อง | สถานะ |
| --- | --- |
| phase owner | locked |
| rename map | locked |
| governance targets | defined |
```

### 5.13.2 Canonical List-Instead-of-Table Shape

```markdown
Current work order:
1. phase/design/TODO/changelog sync
2. schema/model migration
3. store/query rewrite
4. tests and verification
```

### 5.14 Canonical Purpose-First Shape

```markdown
This test checks whether the setting actually changes Claude Code behavior.

Checked Scope
- current config
- runtime behavior after the setting change

What This Means
- if behavior changes, the setting is live
- if behavior does not change, the setting is not taking effect
```

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
| structure starts with setup but not the purpose | the reader has to infer what the answer is doing from later sections | place one short purpose-first line near the start when needed |
| ordinary structured facts presented with full-frame ASCII / boxed tables | the layout becomes heavier than the information needs | use a lighter readable table or switch to a list/grouped block |
| oversized or overbuilt table used as the ordinary default | the output becomes heavier than the information needs | keep the table light or switch to a list/grouped block |
| scope boundaries buried in long prose | the reader cannot tell what is included now versus later | use grouped scope-boundary sections such as `What this is` / `What this is not` / `What happens now` / `What stays later` |
| drilling down before the full set is visible | the reader sees only a narrow slice and may miss the real overall scope | show the full relevant set first, then narrow |
| repeating deeper options when the current stage is already sufficient | the answer feels stuck in the same scope instead of moving forward | add a short `What happens next` or `Next stage` block |
| oversized table for a small issue | increases visual weight without helping the decision | keep tables small and scoped or use prose |
| table-only technical note with no implication | facts are visible but the reader cannot tell what they mean | add one short implication or next-action line |
| governing-basis ambiguity answered with a long branch-comparison essay before the user chooses a basis | the clarification is buried inside unnecessary structure | use a short compact clarification block with basis choices and one `Why it matters` line |
| post-compact continuation presented as a long conversation replay | the reader has to reread stale history instead of seeing the active state quickly | use one short post-compact re-anchor block with current objective, carried-forward facts, needs-recheck detail, and next action |
| remembered context shown like freshly checked current truth | the reader cannot tell what is recalled versus what is revalidated now | use one short memory-status block that separates matched scope, provenance when relevant, and needs-recheck detail |
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
| Purpose-first visibility | High when diagnosis/test/recommendation/proposal answers need fast orientation |
| Section-purpose clarity | High |
| Scanability of complex answers | High |
| Semantic formatting correctness | High |
| Diagnostic snapshot usefulness | High when technical status reporting is used |
| Compact-table efficiency | High when a table is genuinely useful |
| Unnecessary boxed-table incidence | 0 critical cases |
| Decorative formatting without function | 0 critical cases |
| Over-structuring simple answers | Low |
| Wall-of-text incidence in complex answers | Low |

---

## 9) Integration

| Document | Relationship |
|----------|--------------|
| [../answer-presentation.md](../answer-presentation.md) | Runtime implementation of this design |
| [accurate-communication.design.md](accurate-communication.design.md) | Broader communication honesty, human-language glosses, memory-derived-context disclosure wording, and continuation-vs-option policy |
| [technical-snapshot-communication.design.md](technical-snapshot-communication.design.md) | Owns bounded technical snapshot wording semantics while answer-presentation keeps snapshot layout patterns |
| [response-closing-and-action-framing.design.md](response-closing-and-action-framing.design.md) | Owns concise synthesis, recommendation-with-reason framing, and advisory proposal framing while answer-presentation keeps closing-block layout patterns |
| [explanation-quality.design.md](explanation-quality.design.md) | Reasoning structure and layered analytical explanation quality |
| [memory-governance-and-session-boundary.design.md](memory-governance-and-session-boundary.design.md) | Owns memory applicability, root `MEMORY.md` index behavior, path scope, session provenance, and archive semantics |
| [flow-diagram-no-frame.design.md](flow-diagram-no-frame.design.md) | Text-diagram formatting constraints |
| [document-consistency.design.md](document-consistency.design.md) | Consistency in terminology, references, and labeling |

---

> Full history: [../changelog/answer-presentation.changelog.md](../changelog/answer-presentation.changelog.md)
