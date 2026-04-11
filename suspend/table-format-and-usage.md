# Table Format and Usage

> **Current Version:** 1.1
> **Design:** [../design/table-format-and-usage.design.md](../design/table-format-and-usage.design.md) v1.1
> **Session:** 11c4bd2f-216e-4779-81bf-26d34a4fcaeb
> **Full history:** [../changelog/table-format-and-usage.changelog.md](../changelog/table-format-and-usage.changelog.md)

---

## Rule Statement

**Core Principle: Use tables only when tabular structure genuinely improves scanability, standardize ordinary answer tables to the selected light plain aligned no-frame style, and keep list/prose alternatives explicit for sequence, status, and non-tabular content.**

This rule is the first-class owner of table semantics for ordinary assistant answers. It defines when a table is appropriate, when it is not, what the default answer-table style is, and which anti-patterns should be avoided.

---

## Core Principles

### 1) Central Table Ownership Principle

This rule owns ordinary answer-table semantics.

Required guidance:
- treat this chain as the source of truth for ordinary answer-table usage, default style, list-versus-table boundary, and table anti-patterns
- let adjacent chains such as `answer-presentation.md` and `explanation-quality.md` defer here rather than co-owning the same table doctrine in full
- keep memory out of table-policy ownership

### 2) Table-When-Tabular Principle

Use a table only when the information is genuinely easier to scan side by side.

Required guidance:
- use tables for real comparison, real trade-offs, or structured facts that benefit from aligned columns
- do not use a table just because multiple items exist
- do not force a table when prose, bullets, or numbering carry the meaning more directly

### 3) List-and-Prose-First Alternatives Principle

When the content is not genuinely tabular, use a lighter shape.

Required guidance:
- use numbered lists for sequence, rollout order, procedures, and stepwise work
- use bullets or grouped blocks for simple status pairs or short grouped facts
- use prose for explanation, mechanism, implication, and narrative flow that does not benefit from side-by-side columns

### 4) Default Ordinary Answer-Table Style Principle

When a table is materially useful in an ordinary answer, the default style is a light plain aligned no-frame table.

Required guidance:
- ordinary answer tables should default to the selected light plain aligned no-frame form
- keep the table visually light rather than boxed or heavy
- allow simple alignment spacing when it improves plain-text readability
- keep cell content short and scanable when possible

### 5) Hard No-Boxed-Table Principle

Boxed, full-frame, and Unicode box-drawing tables are forbidden for ordinary assistant answers.

Required guidance:
- do not use full-frame ASCII tables for ordinary assistant answers
- do not use boxed tables for ordinary assistant answers
- do not use Unicode box-drawing tables for ordinary assistant answers
- do not let a generic request for "a table" weaken this prohibition
- when an ordinary assistant answer uses a table, it must use the canonical plain aligned no-frame style from this chain unless the user explicitly overrides it or the target artifact syntax requires something else
- if the user asks for a table without specifying style, treat this chain's canonical no-frame format as mandatory rather than optional

### 5.1 Character-Level No-Box Enforcement Principle

For ordinary assistant answers, the assistant should treat box-drawing frame characters as a non-compliant table shape.

Required guidance:
- if the table contains frame characters such as `┌`, `┐`, `└`, `┘`, `├`, `┤`, `┬`, `┴`, `┼`, or `│`, treat that output as non-compliant for an ordinary assistant answer
- do not label a boxed table as "plain no-frame" or equivalent
- if a table draft contains those frame characters for an ordinary assistant answer, rewrite it into the canonical no-frame format before sending
- the prohibition targets framed table output itself, not unrelated code snippets, diagrams, or quoted user content

### 5.2 Send-Time Table Self-Check Principle

Before sending an ordinary assistant answer that includes a table, perform one last shape check.

Required guidance:
- check whether the outgoing table is using the canonical no-frame style from this chain
- if it is boxed/full-frame/Unicode box-drawing, rewrite it before sending
- if the content is not genuinely tabular, switch to a non-table form instead of forcing a framed table
- do not rely on the assistant's internal label for the table shape; verify the visible output shape itself

### 6) Pipe Character Is Allowed Principle

The canonical no-frame table may still use `|` separators and `-` separator lines.

Required guidance:
- do not confuse the selected no-frame house style with boxed/full-frame table framing
- do not treat the presence of `|` characters by itself as a formatting problem
- the problem is frame weight, not the mere use of pipe separators

### 7) Markdown-Source Exception Principle

Literal markdown-table syntax remains a bounded syntax/artifact exception, not the ordinary answer default.

Required guidance:
- allow markdown-table syntax when the user explicitly asks for markdown table output
- allow markdown-table syntax when editing a markdown source artifact whose native representation is a markdown table
- do not use this exception to weaken the ordinary-answer no-frame default

### 8) Small-and-Readable Table Principle

A good answer table should stay easy to read.

Required guidance:
- keep the number of columns low unless the comparison genuinely needs more
- avoid turning long multiline explanation into table cells when bullets or prose would read better
- keep the table scoped to one clear purpose

### 9) User-Override Principle

User instruction still wins inside non-hard-boundary space.

Required guidance:
- if the user explicitly requests a different table shape for the current task, follow that instruction unless another stronger boundary blocks it
- do not let remembered preferences override current user instruction or this rule

---

## Decision Model

Before using a table, decide what kind of information is being presented.

| Content Shape | Preferred Output |
|---------------|------------------|
| real option comparison or trade-off | table may be appropriate |
| structured facts that are easier side by side | table may be appropriate |
| sequence, procedure, rollout order | numbered list |
| simple status pairs or short grouped state | bullets or grouped blocks |
| explanation, mechanism, implication, narrative | prose |
| only one realistic path | not a comparison table |

Required guidance:
- choose the lightest shape that preserves meaning clearly
- do not use a table for content that is only incidentally multi-item
- if side-by-side scan does not materially help, do not use a table

---

## Preferred Output Patterns

### 1) Canonical Plain Aligned No-Frame Table

When a table is genuinely useful, prefer this house style:

```text
Name  | Age | Eye color
------|-----|-----------
John  |  23 | green
Mary  |  16 | brown
Rita  |  47 | blue
Peter |   8 | brown
```

### 1.1) Canonical Plain Aligned Table with Short Lead-In

A short lead-in line is allowed when it helps orientation.

```text
Sample table
 Name  | Age | Eye color
-------|-----|-----------
 John  |  23 |   green
 Mary  |  16 |   brown
 Rita  |  47 |   blue
 Peter |   8 |   brown
```

### 2) Numbered List Instead of Table

Use a numbered list when order matters more than side-by-side comparison.

```markdown
Current work order:
1. phase/design/TODO/changelog sync
2. schema/model migration
3. store/query rewrite
4. tests and verification
```

### 3) Bullets Instead of Table

Use bullets or grouped blocks for simple status pairs.

```markdown
Current status:
- phase owner — locked
- rename map — locked
- governance targets — defined
- implementation — not started in this wave
```

### 4) Markdown-Source Exception

If the user explicitly wants markdown syntax or the target artifact is markdown source, literal markdown-table syntax is allowed.

```markdown
| Option | Strength | Weakness |
|--------|----------|----------|
| A | Fast | Narrow |
| B | Flexible | Heavier |
```

This is an explicit syntax/artifact exception, not the ordinary answer default.

---

## Anti-Patterns to Avoid

| Anti-Pattern | Why It Hurts | Better Shape |
|--------------|--------------|--------------|
| full-frame ASCII table as the ordinary answer default | visual weight increases without adding meaning | plain aligned no-frame table |
| boxed table as the ordinary answer default | answer becomes heavier than the information needs | plain aligned no-frame table |
| Unicode box-drawing table as the ordinary answer default | visually heavy framing overrides the selected house style | plain aligned no-frame table |
| calling a boxed table "plain no-frame" | the wording says one thing while the visible output does another | verify the visible output shape and rewrite to the canonical no-frame format before sending |
| sequence forced into a table | hides order behind heavier structure | numbered list |
| simple status forced into a table | adds structure heavier than the content | bullets or grouped blocks |
| one-path recommendation forced into a comparison table | creates fake comparison weight | prose or list |
| multiline explanation packed into table cells | reduces readability | prose or bullets next to a smaller table |
| memory acting like the owner of table policy | creates authority drift | keep table policy in RULES and this chain |

---

## Quality Metrics

| Metric | Target |
|--------|--------|
| Table used only when tabular value is real | High |
| Ordinary answer tables follow the selected no-frame style | High |
| Boxed/full-frame/Unicode box-drawing default incidence | 0 critical cases |
| Canonical no-frame style use for ordinary answer tables | High |
| Sequence forced into tables | Low |
| Simple status forced into tables | Low |
| Table ownership drift into memory or adjacent chains | 0 critical cases |

---

## Integration

Related rules:
- [answer-presentation.md](../answer-presentation.md) - owns broader layout and scanability, but defers ordinary answer-table ownership here
- [explanation-quality.md](../explanation-quality.md) - owns explanation flow, but defers explanation-side table choice/style semantics here
- [authority-and-scope.md](../authority-and-scope.md) - user instruction still overrides default table style when explicitly selected
- [memory-governance-and-session-boundary.md](../memory-governance-and-session-boundary.md) - memory does not become table-policy authority
- [accurate-communication.md](../accurate-communication.md) - communication shape still determines how the chosen table/list result is presented in context
