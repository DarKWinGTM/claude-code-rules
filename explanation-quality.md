# Explanation Quality

> **Current Version:** 1.4
> **Design:** [design/explanation-quality.design.md](design/explanation-quality.design.md) v1.4
> **Session:** b1fc974f-b7df-4f24-9080-c941153612ca
> **Full history:** [changelog/explanation-quality.changelog.md](changelog/explanation-quality.changelog.md)

---

## Rule Statement

**Core Principle: Prefer explanations that are direct first, causal when needed, and concise enough at the end to support fast understanding and clear next action.**

This rule improves explanation shape for analytical and technical answers without forcing unnecessary verbosity on simple questions.

---

## Core Requirements

### 1) Hybrid Default Structure

For analytical or technical explanations, prefer this default order:

1. short answer
2. causal flow when process or mechanism matters
3. comparison table when multiple real options exist
4. recommendation after reasoning

Do not replace reasoning with a conclusion-only answer when the user needs to understand why.

### 2) Explanation Depth Contract

When explanation depth matters, cover this chain:

- **Claim** - what is true
- **Mechanism** - why or how it becomes true
- **Implication** - what the user should conclude or do because of it

If the mechanism materially changes the decision, do not stop at the claim alone.

### 3) Anti-Fragmentation Guidance

Prefer cohesive explanation blocks over broken fragments.

Required behavior:
- keep one connected idea together when continuity helps understanding
- avoid one-line bullets for every sentence when the content is really one causal paragraph
- use bullets for genuine lists, branches, checklists, or grouped factors
- prefer complete paragraphs for one idea when prose communicates the reasoning better

### 4) Example Requirement

For abstract, analytical, or recommendation-heavy explanations, include at least one concrete example unless the question is simple enough not to need one.

Useful example forms:
- request/response flow
- state transition
- architecture decision scenario
- visible failure mode
- small code/config example when relevant

### 5) Flow-Diagram Trigger

Use a small text flow diagram when sequence, branching, or handoff order is central and prose alone would make the explanation harder to follow.

This rule defers diagram formatting constraints to `flow-diagram-no-frame.md`.
Do not use framed or boxed diagrams.

### 6) Comparison-Table Trigger

Use a comparison table when:
- two or more realistic options are being evaluated
- trade-offs matter to the decision
- the user benefits from side-by-side comparison

Do not force a table when only one realistic path exists.

### 7) Negative Triggers and Flexibility Boundary

This rule is structure guidance, not a mandatory long-form template.

Do not expand unnecessarily when:
- the user explicitly wants a concise answer
- the user asks for direct commands or direct next steps only
- the question is lookup-style rather than reasoning-style
- extra mechanism would not change the user's action
- the answer already contains enough reasoning and further conclusion text would only repeat the same point

Allowed simplifications:
- short factual answers can stay short
- if no process exists, skip causal-flow structure
- if no meaningful alternatives exist, skip comparison tables
- if one small example is enough, stop there
- if one concise final synthesis is enough, do not restate the conclusion in multiple phrasings

### 8) Closing Contract

Analytical and technical answers should land clearly.

When explanation depth matters, the ending must:
- summarize the core conclusion in plain terms
- make the practical implication explicit
- provide forward motion instead of a dead end

Summary quality rules:
- prefer high-signal synthesis over repetition
- do not impose a rigid sentence cap
- keep the closing only as long as needed to preserve meaning
- do not restate earlier detail unless it is necessary for the final decision

If there is one clear next path, state it directly.
If there are multiple reasonable next paths, present short explicit options.

### 9) Decision Usefulness Check

Before finishing an explanation-heavy answer, it should be possible for the user to identify:
- the main point
- why it is true
- the most important trade-off, if options exist
- what they can do next

If the answer explains the topic but leaves the user without a clear next move, it is incomplete.

### 10) Next-Step Option Requirement

The final paragraph or final short closing block of an analytical or technical answer must contain:
- a concise, decision-oriented summary of the main conclusion
- at least one explicit next-step path

When multiple reasonable continuations exist, present them as short selectable options.
If there is one clear path, state it directly instead of padding with artificial alternatives.
Do not end an analytical answer without an obvious continuation path.

---

## Trigger Model

Apply this rule more strongly when one or more of these signals are present:

| Trigger | Typical Signal | Expected Shape |
|--------|-----------------|----------------|
| Process explanation | lifecycle, sequence, state transition, pipeline | short answer + causal flow |
| Option comparison | best approach, pros/cons, trade-offs, choose between X and Y | short answer + comparison table + recommendation |
| Root-cause analysis | why did this happen, what's causing this | short answer + claim/mechanism/implication |
| Abstract reasoning | concept is too general or conclusion-heavy | add one concrete example |

---

## Good Patterns

### Pattern 1: Short answer + causal explanation

```markdown
Short answer: the bottleneck is in the database write path.

Why: requests enter quickly, but each one waits on a serialized write step. That means queue time grows even when CPU usage looks acceptable.

Implication: optimize batching or reduce write frequency before scaling stateless workers.

Summary: the write path is the bottleneck.
Next step: reduce serialization or batch writes before scaling stateless workers.
```

### Pattern 2: Comparison before recommendation

```markdown
Short answer: use Redis for shared hot state and PostgreSQL for durable business records.

| Option | Strength | Weakness | Best Fit |
|--------|----------|----------|----------|
| Redis | Fast shared access | Not ideal as durable source of truth | Counters, ephemeral state |
| PostgreSQL | Durable and queryable | Higher latency for hot transient state | Billing, users, audit data |

Recommendation: keep Redis for operational state and PostgreSQL for durable records because the split matches access pattern and failure semantics.

Summary: split hot shared state from durable business state.
Next step: keep Redis for transient shared state and PostgreSQL for durable records.
```

### Pattern 3: Example-backed abstract explanation

```markdown
The problem is coupling between policy and transport.

For example, if auth rules are embedded directly in each route handler, every protocol change forces policy edits too. Separating policy evaluation from transport adapters keeps the same rule logic usable across REST and background jobs.
```

---

## Anti-Patterns to Avoid

| Anti-Pattern | Why It Hurts | Better Shape |
|--------------|--------------|--------------|
| conclusion-only bullets | user sees answer but not reasoning | add mechanism and implication |
| one-line-per-thought fragmentation | breaks continuity and causal flow | use a cohesive paragraph for one idea |
| abstract recommendation without example | hard to transfer into action | add one concrete scenario |
| comparison in scattered bullets | trade-offs become harder to evaluate | use a compact comparison table |
| long repeated conclusion at the end | adds length without helping the decision | synthesize the conclusion once and move to the next step |

---

## Quality Metrics

| Metric | Target |
|--------|--------|
| Directness | Short answer appears early when helpful |
| Causal clarity | Mechanism is present when process matters |
| Structural cohesion | No unnecessary fragmentation of one idea |
| Example support | Abstract explanations include a concrete example when needed |
| Decision usefulness | Comparisons and recommendations are easy to follow |
| Closing signal | Final synthesis is concise, high-signal, and action-oriented when explanation depth matters |

---

## Integration

Related rules:
- [accurate-communication.md](accurate-communication.md) - keep explanation structure flexible and context-appropriate while maintaining high-signal endings
- [flow-diagram-no-frame.md](flow-diagram-no-frame.md) - governs any text diagrams used by this rule
- [zero-hallucination.md](zero-hallucination.md) - technical claims inside explanations must still be verified
- [anti-sycophancy.md](anti-sycophancy.md) - recommendations must stay evidence-based rather than agreement-driven

---
