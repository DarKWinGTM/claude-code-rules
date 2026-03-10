# Explanation Quality

## 0) Document Control

> **Parent Scope:** RULES System Design
> **Current Version:** 1.4
> **Session:** b1fc974f-b7df-4f24-9080-c941153612ca (2026-03-09)

---

## 1) Goal

Define one rule chain that improves the structure of analytical and technical explanations so answers stay easy to scan without losing causal reasoning depth.

The target behavior is a hybrid default:
- short answer first
- causal flow when process or state change matters
- comparison table when options or trade-offs exist
- recommendation after the reasoning, not instead of it
- concise, high-signal ending that makes the next path clear

---

## 2) Problem Statement

Recent explanation quality drift is primarily structural rather than factual.

Observed failure modes:
- answers collapse into short fragments that break one idea across many lines
- bullets present conclusions without enough mechanism or causal flow
- trade-off discussions appear without side-by-side comparison structure
- recommendations arrive before the reasoning that justifies them
- abstract analytical claims appear without a concrete example
- endings repeat prior detail instead of synthesizing the real conclusion
- responses stop after explanation without making the next action clear

This design addresses explanation shape while preserving existing verification and accuracy requirements.

---

## 3) Scope and Trigger Conditions

This rule is intended for responses where explanation quality depends on reasoning flow, not only correctness.

Typical triggers:
- root-cause analysis
- architectural reasoning
- process, sequence, or state-transition explanation
- technical comparison between options
- recommendation requests where the user needs to understand why
- abstract analytical answers that would be clearer with one concrete example

This rule is not meant to force long-form structure onto simple factual or low-complexity questions.

---

## 4) Hybrid Default Answer Structure

When the task is analytical, the preferred default order is:

Short answer
  ↓
Causal flow or mechanism
  ↓
Comparison table when options exist
  ↓
Recommendation with reasoning
  ↓
Concise synthesis and next-step path

### 4.1 Short Answer First

Start with a brief direct answer so the user can orient quickly.

### 4.2 Causal Flow When Process Exists

If the topic involves sequence, dependency, state transition, or mechanism, explain the chain in order rather than jumping from premise to conclusion.

### 4.3 Comparison Table When Options Exist

If the user is choosing between meaningful alternatives, present trade-offs in a compact comparison table before recommending one path.

### 4.4 Recommendation Last

A recommendation should close the reasoning phase after the causal reasoning or comparison is visible.

### 4.5 Concise Synthesis Last

When explanation depth matters, the answer should still land with a concise, high-signal synthesis and a clear next-step path.

---

## 5) Explanation Depth Contract

Analytical explanations should usually satisfy this depth chain:

Claim
  ↓
Mechanism
  ↓
Implication

Meaning:
- **Claim** = what is true
- **Mechanism** = why or how it becomes true
- **Implication** = what the user should conclude, change, or decide because of it

For explanation-heavy answers, stopping at the claim is insufficient when the mechanism materially affects user understanding.

---

## 6) Anti-Fragmentation Guidance

The rule should reduce readability loss caused by over-fragmentation.

Required guidance:
- avoid splitting one causal idea into many one-line bullets when a coherent paragraph would read better
- keep related reasoning steps together unless separation clearly improves scanning
- use bullets for genuine sets, branches, or checklists, not as a substitute for connective prose
- prefer one complete paragraph per idea when the thought needs continuity

The goal is not verbosity. The goal is cohesion.

---

## 7) Example Requirement

When an explanation is abstract, analytical, or recommendation-heavy, include at least one concrete example unless the task is too simple to need one.

Acceptable example forms:
- request/response lifecycle
- state transition
- architecture decision scenario
- user-visible failure case
- small code or configuration example when relevant

Example:
- Weak explanation: "Redis is better here because it is fast."
- Better explanation: "Redis is better here because this data is shared operational state that multiple services must read and update quickly; for example, a rate-limit counter or transient job status benefits from low-latency shared access, while durable billing records should stay in PostgreSQL."

---

## 8) Flow-Diagram Trigger

Use a small text flow diagram when sequence or branching is central and prose alone would make ordering harder to follow.

Trigger cases:
- request lifecycle
- state machine progression
- conditional branch explanation
- pipeline or handoff sequence

This rule must reference `flow-diagram-no-frame.md` for diagram formatting constraints.
It must not duplicate that rule's box-drawing prohibitions or connector standards.

---

## 9) Comparison-Table Trigger

Use a comparison table when:
- two or more realistic options are being evaluated
- trade-offs matter to the decision
- the user needs dimension-by-dimension comparison rather than isolated bullets

Preferred columns depend on context, but common dimensions include:
- option
- strength
- weakness
- best fit

Do not force a table when there is only one realistic path or when the comparison would be artificial.

---

## 10) Negative Triggers and Flexibility Boundaries

This rule should stay compatible with concise communication and action-first requests.

Do not expand unnecessarily when:
- the user explicitly asks for a concise answer
- the user asks for direct commands or direct next steps only
- the question is lookup-style rather than reasoning-style
- added mechanism would not change the user's decision or action
- the answer already contains enough reasoning and further conclusion text would only repeat the same point

Boundaries:
- simple factual questions may use a short direct answer only
- if no process exists, skip causal-flow structure
- if no real alternatives exist, skip comparison tables
- if one short example is enough, do not expand into unnecessary depth
- if one concise final synthesis is enough, do not restate the conclusion in multiple phrasings
- this rule shapes explanation quality; it does not weaken verification, safety, or user-authority rules

This design is intentionally compatible with `accurate-communication.md`, which already allows context-based flexibility.

---

## 11) Closing Contract

Analytical and technical answers should land clearly, not just stop after explanation.

Required closing behavior when explanation depth matters:
- the ending must summarize the core conclusion in plain terms
- the ending must make the practical implication explicit
- the response must provide forward motion rather than a dead end

Summary quality rules:
- prefer high-signal synthesis over repetition
- do not impose a rigid sentence cap
- keep the summary only as long as needed to preserve meaning
- do not restate earlier detail unless it is necessary for the final decision

Default expectation:
- if there is one clear next path, state it directly
- if there are multiple reasonable next paths, present short explicit options the user can choose from

Example closing shape:
- final takeaway summary
- then one or more clear next-step options

This contract is about response landing quality, not forced verbosity.

---

## 12) Decision Usefulness Check

Before finishing an explanation-heavy answer, it should be possible for the user to identify:
- what the main point is
- why it is true
- what trade-off matters most, if options exist
- what they can do next

If the answer explains the topic well but leaves the user without a clear next move, the response is incomplete.

---

## 13) Next-Step Option Requirement

When a response closes with next actions, it should preserve user choice.

Required behavior:
- the final paragraph or final short closing block must contain a concise, decision-oriented summary of the answer's main conclusion
- after that summary, provide at least one explicit next-step path
- when multiple reasonable continuations exist, present them as short selectable options
- if there is one clear path, state it directly instead of padding with artificial alternatives
- do not end an analytical answer in a way that leaves no obvious continuation path

Example pattern:
- "Summary: X is the right path here. Next step: do Y."
- "Summary: the implementation is sound, but final verification is still pending. Next step: run the production check."
- "We can continue in 2 ways: A or B."

This requirement complements the closing contract by ensuring the answer always offers a clear continuation path.

---

## 14) Integration with Existing Rules

| Rule | Relationship |
|------|--------------|
| `accurate-communication.md` | Keeps explanation structure flexible while requiring concise, high-signal endings |
| `flow-diagram-no-frame.md` | Governs any text flow diagram used by this rule |
| `zero-hallucination.md` | Preserves verification requirements for technical claims inside explanations |
| `anti-sycophancy.md` | Prevents recommendation quality from drifting into agreement without reasoning |

---

## 15) Rollout State

### Phase A (Completed)

- Created `design/explanation-quality.design.md`.
- Created `changelog/explanation-quality.changelog.md`.
- Registered the chain in master design/changelog/TODO as pending activation.

### Phase B (Completed)

- Materialized runtime `explanation-quality.md` at v1.1.
- Promoted the chain from pending activation to active runtime state.
- Aligned master design/changelog/TODO and README active-rule inventory after activation.

---

> Full history: [../changelog/explanation-quality.changelog.md](../changelog/explanation-quality.changelog.md)
