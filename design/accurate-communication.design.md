# Accurate Communication Standard Design

## 0) Document Control

> **Parent Scope:** RULES System Design
> **Current Version:** 1.3
> **Session:** b1fc974f-b7df-4f24-9080-c941153612ca (2026-03-09)

---

## 1) Goal

Define one communication rule chain that improves clarity and verification honesty without forcing rigid formatting on every response.

The target behavior is not just correctness. It is also high-signal communication that lands clearly and helps the recipient know what matters most and what to do next.

---

## 2) Problem Statement

Communication quality failures are often structural rather than factual.

Observed failure modes:
- status messages omit enough context for the recipient to understand impact or required action
- success claims are stated more strongly than the available verification supports
- simple cases get over-explained while complex cases remain underspecified
- message style becomes rigid instead of context-sensitive
- closing summaries repeat prior detail instead of synthesizing the answer
- responses end without a clear next step even when one exists

This design defines flexible principles that improve clarity while preserving judgment.

---

## 3) Core Principles

### 3.1 Communication Clarity Principle

Recipients should be able to understand enough context from a single message to interpret the situation correctly.

Required guidance:
- explain what happened when the context is not already obvious
- clarify impact when ambiguity could mislead the recipient
- make action requirements explicit when action is needed
- avoid adding unnecessary structure when the context is already clear

### 3.2 Verification Honesty Principle

Claims must match the real level of verification.

Typical mapping:

| Verification Level | Acceptable Statement |
|--------------------|---------------------|
| Not yet done | "Will do X" |
| Done, not tested | "Done, awaiting verification" |
| Partially tested | "X passed, Y pending" |
| Fully tested | "Working correctly" |
| Stable over time | "Fixed" |

Required guidance:
- do not overstate certainty
- simple tasks may need less formal reporting than complex ones
- critical work requires more explicit verification status

### 3.3 Signal Density and Closing Clarity Principle

The end of the response should synthesize, not merely repeat.

Required guidance:
- prefer high-signal synthesis over rephrasing prior detail
- keep final summaries concise and decision-oriented
- do not impose a rigid sentence cap; the summary should be only as long as needed to preserve meaning
- if a clear next action exists, state it directly
- if multiple reasonable next actions exist, present short explicit options

---

## 4) Application Model

### 4.1 When Clarity Guidance Applies Strongly

Use stronger clarity behavior when:
- something unexpected was found
- a status report could be misunderstood
- impact or next action is not obvious from context alone

### 4.2 When Verification Honesty Applies Strongly

Use stronger verification reporting when:
- claiming that something works or is fixed
- summarizing implementation completion
- reporting success on work that still has open validation steps

### 4.3 When Closing Guidance Applies Strongly

Use stronger concise-closing behavior when:
- the answer is analytical or technical
- the response contains enough reasoning that the user needs synthesis at the end
- a practical next path exists and should be made explicit

### 4.4 Flexibility Boundary

This rule is principle-based, not rigid-format based.

Allowed flexibility:
- short direct answers for simple contexts
- explicit verification breakdown for complex contexts
- context-based omission of redundant details when the recipient already has the relevant frame
- summaries that are as short as possible, but long enough to preserve meaning

---

## 5) Examples

### 5.1 Problem Reporting Example

Simple case:
- "Found a typo here."

Complex case:
- "Found that X is missing parameter Y.

  Impact: requests fail when the optional fallback is absent.
  Action: add the missing parameter before release."

### 5.2 Success-Claim Example

Simple case:
- "Fixed the typo."

Complex case:
- "Implementation complete.

  Status:
  - code updated
  - syntax verified
  - production validation still pending

  Awaiting final verification before confirming fixed."

### 5.3 Closing Example

Weak closing:
- repeats the same reasoning in different words
- still leaves the recipient to guess what should happen next

Better closing:
- concise synthesis of the real conclusion
- direct next action or short option list

---

## 6) Anti-Patterns to Avoid

| Anti-Pattern | Why It Hurts | Better Shape |
|--------------|--------------|--------------|
| vague problem statement with no impact | recipient must ask follow-up questions just to understand the situation | include impact and action when needed |
| claiming "fixed" before verification supports it | creates false completion confidence | state the actual verification state |
| over-explaining obvious simple work | adds noise without value | keep simple cases concise |
| forcing one format for every message | reduces usability and judgment | adapt to context |
| summary repeats the whole answer | adds length without signal | synthesize only the conclusion and implication |
| ending with no next path | recipient understands but cannot act | add a direct next step or short options |

---

## 7) Quality Metrics

| Metric | Target |
|--------|--------|
| Context clarity | Recipient understands enough from one message |
| Verification honesty | Claims match verified state |
| Flexibility | Context-appropriate structure |
| Signal density | Summary and closing guidance stay high-signal and non-repetitive |
| Closing usefulness | Ending makes the next path clear |
| Anti-pattern avoidance | No vague problem-only reports, no premature success claims, no summary repetition |

---

## 8) Integration

| Rule | Relationship |
|------|--------------|
| [../accurate-communication.md](../accurate-communication.md) | Runtime implementation |
| [zero-hallucination.design.md](zero-hallucination.design.md) | Verification honesty depends on evidence discipline |
| [anti-sycophancy.design.md](anti-sycophancy.design.md) | Prevents comfort-first communication drift |
| [explanation-quality.design.md](explanation-quality.design.md) | Analytical explanations should end with concise synthesis and clear next-step guidance |

---

> Full history: [../changelog/accurate-communication.changelog.md](../changelog/accurate-communication.changelog.md)
