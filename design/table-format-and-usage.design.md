# Table Format and Usage

## 0) Document Control

> **Parent Scope:** RULES System Design
> **Current Version:** 1.0
> **Session:** 11c4bd2f-216e-4779-81bf-26d34a4fcaeb (2026-04-11)

---

## 1) Goal

Define one first-class rule chain for table semantics so ordinary assistant answers use tables only when they are genuinely helpful, use the selected light plain aligned no-frame style consistently, and keep lighter non-table alternatives explicit for sequence, simple status, and non-tabular explanation.

The target behavior is:
- one semantic owner for ordinary answer-table usage and style
- consistent no-frame default styling for ordinary answer tables
- explicit list-versus-table boundary
- explicit anti-pattern rejection for boxed/full-frame and generic markdown-pipe defaults in ordinary answers
- bounded exceptions for markdown-source artifacts or explicit user requests
- narrower adjacent ownership in `answer-presentation` and `explanation-quality`

---

## 2) Problem Statement

The repository already improved table behavior in recent waves, but table semantics still live across multiple adjacent owners.

Observed failure modes this design intends to close:
- table usage guidance is split between presentation and explanation owners, so the source of truth is still diffuse
- table style can drift because the assistant still sees several different places talking about table behavior
- boxed/full-frame or generic markdown-pipe defaults can reappear when the ownership boundary is not central enough
- sequence and simple status content can still be forced into tables when the list-versus-table boundary is not taught through one owner
- memory or remembered preference can overreach unless table policy is visibly locked to RULES

This design solves that by creating one first-class table owner and narrowing adjacent chains to defer/reference posture.

---

## 3) Scope and Non-Goals

### 3.1 In Scope
- ordinary answer-table usage semantics
- ordinary answer-table default style
- list-versus-table boundary
- comparison-table legitimacy boundary
- anti-patterns for boxed/full-frame and generic markdown-pipe defaults in ordinary answers
- bounded markdown-source / explicit-request exceptions
- ownership transfer out of `answer-presentation` and `explanation-quality`

### 3.2 Out of Scope
- broader layout patterns such as headings, scope-grouping, and snapshot section structure
- broader explanation flow such as claim/mechanism/implication sequencing
- repository markdown authoring conventions as a whole
- flow-diagram ownership
- memory governance outside the narrow table-policy boundary

### 3.3 Boundary Principle
This chain owns **ordinary answer-table semantics**.

It does not replace:
- `answer-presentation.md` for overall layout and scanability
- `explanation-quality.md` for explanation flow and reasoning shape
- `authority-and-scope.md` for user override precedence
- `project-documentation-standards.md` for general repository-document governance

---

## 4) Core Table Model

### 4.1 Central Ownership Principle
One chain should own ordinary answer-table semantics.

Required behavior:
- table usage, default style, list-versus-table boundary, and table anti-patterns should have one semantic owner
- adjacent chains should defer here instead of re-owning the same doctrine in full
- memory must not act like a competing table-policy source

### 4.2 Table-When-Tabular Principle
Use a table only when aligned columns materially improve scanability.

Required behavior:
- use tables for real comparison, real trade-offs, or structured facts that benefit from side-by-side reading
- do not use a table just because multiple items exist
- choose a lighter form when alignment does not add meaning

### 4.3 List-and-Prose Alternatives Principle
Non-tabular content should not be forced into tables.

Required behavior:
- sequence, rollout order, and procedures prefer numbered lists
- simple status pairs prefer bullets or grouped blocks
- explanation, mechanism, and implication prefer prose unless tabular structure truly helps

### 4.4 Default Style Principle
Ordinary answer tables should use the selected light plain aligned no-frame style.

Required behavior:
- keep the table visually light
- allow simple alignment spacing when it improves plain-text reading
- keep the selected house style explicit enough that model drift back to heavier defaults is less likely

### 4.5 Anti-Heavy-Frame Principle
Boxed and full-frame defaults are not the ordinary answer style.

Required behavior:
- reject full-frame ASCII defaults
- reject boxed-table defaults
- reject visually heavy framing when it adds noise but not meaning

### 4.6 Anti-Generic-Pipe-Default Principle
Generic markdown-pipe tables are not the ordinary answer default.

Required behavior:
- do not teach generic markdown-pipe framing as the default ordinary answer-table shape
- keep the markdown-table form available only for explicit syntax/artifact exceptions
- make the exception boundary visible enough that it does not quietly become the default again

### 4.7 Small-and-Readable Principle
A good answer table should remain easy to scan.

Required behavior:
- keep column count low unless the comparison genuinely needs more
- keep cell content short where possible
- avoid multiline explanation cells when prose or bullets would be clearer
- keep one table for one clear job

### 4.8 Markdown-Source Exception Principle
There are bounded contexts where literal markdown-table syntax is still appropriate.

Required behavior:
- allow markdown-table syntax when the user explicitly asks for markdown table output
- allow markdown-table syntax when editing a markdown source artifact whose native representation is a markdown table
- keep those cases explicit so they do not reset the ordinary answer default

---

## 5) Decision Model

Before using a table, classify the content shape.

| Content Shape | Preferred Output |
|---------------|------------------|
| real option comparison | table may be appropriate |
| structured facts easier side by side | table may be appropriate |
| sequence / steps / rollout order | numbered list |
| simple status pairs | bullets or grouped blocks |
| explanation / narrative reasoning | prose |
| only one realistic path | not a comparison table |

Required behavior:
- choose the lightest format that preserves meaning clearly
- treat side-by-side value as the deciding factor, not item count alone
- prefer non-table forms when table weight is not justified

---

## 6) Ownership Transfer Model

### 6.1 `answer-presentation` after transfer
`answer-presentation` should still:
- govern broader layout and scanability
- govern how tables sit inside larger answer structure
- govern framing before/after a chosen table

But it should no longer be the primary owner of:
- table default style
- table-versus-list doctrine
- detailed table anti-pattern semantics

### 6.2 `explanation-quality` after transfer
`explanation-quality` should still:
- govern explanation flow
- govern when the answer is doing real comparison in explanation terms
- govern reasoning usefulness and progression

But it should no longer be the primary owner of:
- explanation-side table default style
- detailed table-versus-list doctrine
- table anti-pattern semantics

### 6.3 Defer-by-reference target
After the transfer:
- `answer-presentation` should reference this chain for table/list choice and default style
- `explanation-quality` should reference this chain for explanation-side table use/style semantics

---

## 7) Canonical Patterns

### 7.1 Canonical ordinary answer-table style

```text
Name  | Age | Eye color
------|-----|-----------
John  |  23 | green
Mary  |  16 | brown
Rita  |  47 | blue
Peter |   8 | brown
```

### 7.2 Canonical titled variant

```text
Sample table
 Name  | Age | Eye color
-------|-----|-----------
 John  |  23 |   green
 Mary  |  16 |   brown
 Rita  |  47 |   blue
 Peter |   8 |   brown
```

### 7.3 Canonical list alternative

```markdown
Current work order:
1. phase/design/TODO/changelog sync
2. schema/model migration
3. store/query rewrite
4. tests and verification
```

### 7.4 Canonical status alternative

```markdown
Current status:
- phase owner — locked
- rename map — locked
- governance targets — defined
- implementation — not started in this wave
```

---

## 8) Anti-Patterns to Avoid

| Anti-Pattern | Why It Hurts | Better Behavior |
|--------------|--------------|-----------------|
| creating a central table rule but leaving adjacent owners fully co-owning the doctrine | centralization becomes cosmetic only | transfer ownership and make adjacent chains defer here |
| full-frame or boxed ordinary answer tables | output becomes heavier than the information needs | use the selected plain aligned no-frame form |
| generic markdown-pipe table as the ordinary answer default | style drifts away from the chosen house contract | keep markdown-table syntax as an explicit exception only |
| sequence forced into a table | order is less direct and layout gets heavier | use a numbered list |
| simple status forced into a table | visual structure becomes heavier than the content | use bullets or grouped blocks |
| long explanation packed into cells | readability falls sharply | move explanation into prose or bullets |
| memory acting like table-policy authority | governance drifts away from RULES | keep policy in RULES and this chain |

---

## 9) Quality Metrics

| Metric | Target |
|--------|--------|
| Ordinary answer-table owner clarity | 100% |
| Default no-frame style consistency | High |
| Boxed/full-frame default incidence | 0 critical cases |
| Generic markdown-pipe default incidence in ordinary answers | 0 critical cases |
| Adjacent-chain overlap after transfer | Low |
| Table/list decision consistency | High |

---

## 10) Integration

Related chains:
- `answer-presentation.md`
- `explanation-quality.md`
- `authority-and-scope.md`
- `memory-governance-and-session-boundary.md`
- `accurate-communication.md`
