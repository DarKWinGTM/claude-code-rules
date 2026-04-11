# Explanation Quality

## 0) Document Control

> **Parent Scope:** RULES System Design
> **Current Version:** 2.15
> **Session:** 11c4bd2f-216e-4779-81bf-26d34a4fcaeb (2026-04-09)

---

## 1) Goal

Define one rule chain that improves the structure of analytical and technical explanations so answers stay easy to follow, feel natural step by step, and preserve causal reasoning depth.

The target behavior is a layered natural explanation style:
- short answer first
- purpose-first framing when the reader needs to know what the explanation is doing before the detail starts
- simple explanation before deep protocol detail
- compact technical snapshot when status or checked scope matters
- step-by-step implication or fix path when walkthrough value exists
- explicit clarification of what the thing is, what it is not, what happens now, and what stays deferred when scope management matters
- explicit clarification of what variable names, field names, config keys, enum-like values, and internal labels mean when the explanation depends on them
- whole-set framing when the user benefits from seeing the full actionable set before drilling down
- a tendency to move to the next meaningful stage/state when the current one is already sufficiently clarified
- direct human-readable translation of metaphor-heavy or architecture-first wording before deeper explanation depends on it
- easy-to-picture phase/progress explanation before denser governance or mechanism detail when the user is trying to understand what a phase is doing
- concise, high-signal ending with a real next move only when one genuinely exists
- goal-qualified proposal framing when future ideas are useful after bounded completion
- governing-basis clarification before deepening several materially different branches
- compact post-compact re-anchor before explanation resumes after compaction may have compressed exact context
- explanation-side table usage/style semantics defer to a central table owner while explanation flow still decides when true comparison exists
- explanation that sounds like a capable professional colleague rather than a scripted narrator or over-produced tutor

---

## 2) Problem Statement

Recent explanation quality drift is primarily structural rather than factual.

Observed failure modes:
- answers collapse into short fragments that break one idea across many lines
- bullets present conclusions without enough mechanism or causal flow
- trade-off discussions appear without side-by-side comparison structure
- recommendations arrive before the reasoning that justifies them
- the explanation starts with setup detail and only reveals its purpose later
- abstract analytical claims appear without a concrete example or clarifying model
- changes are described as one blob instead of before/after or patch-by-patch progression
- endings repeat prior detail instead of synthesizing the real conclusion
- responses stop after explanation without making the next action or completion state clear
- progress or troubleshooting updates bury current state and checked scope inside long narrative blocks
- explanation is structurally correct but still sounds scripted, over-signposted, or more performative than useful
- over-explaining continues after the user already has enough context to decide or proceed
- metaphor-heavy or architecture-first wording is left unexplained, forcing the reader to decode internal shorthand before they can understand the practical meaning
- multiple materially different policy/frame branches are explained in depth before the active governing basis is chosen
- post-compact explanation restarts by replaying stale history instead of re-anchoring the active objective and checked state first

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
- implementation progress, troubleshooting state, or verification checkpoints where a compact status snapshot improves clarity
- change walkthroughs where before/after or patch-by-patch framing helps
- scope clarification where the user needs to understand what is included now versus what stays deferred
- sequence/status explanations where list-vs-table choice affects scanability and answer weight
- abstract analytical answers that would be clearer with one concrete example, a small analogy, or a direct human-language paraphrase

This rule is not meant to force long-form structure onto simple factual or low-complexity questions.

---

## 4) Plain-Language-First and Layered Default Structure

When the task is analytical, the preferred default order is:

Short answer
  ↓
Purpose-first framing when needed
  ↓
Simple explanation
  ↓
Compact technical snapshot when needed
  ↓
Step-by-step implication or fix
  ↓
Concise synthesis and next move when genuinely useful

### 4.1 Plain-Language-First Principle

Start with the simplest truthful framing that helps the user understand the situation quickly.

Required guidance:
- explain what the issue means before diving into lower-level protocol detail when the topic is complex
- prefer a human-readable opening model before dense implementation detail
- when useful, explicitly separate a simple version from a technical version

### 4.1.1 Purpose-First Explanation Step

When an explanation is doing operational work such as diagnosing, testing, recommending, proposing, or reporting implementation state, the opening should first say what the explanation is doing before it starts unpacking the mechanism.

Required guidance:
- open with one direct sentence that states what is being tested, diagnosed, proposed, recommended, or concluded when that orientation materially improves understanding
- make the explanation purpose legible before background, mechanism, or supporting evidence expands the answer
- if a labeled structure is used, let the first line or first short block carry the purpose-first statement
- if the first sentence already states the purpose clearly, do not force a second redundant framing line

### 4.2 Layered Natural Explanation Pattern

Use layered explanation so the reader can stop early if the simple model is enough, but still go deeper when needed.

Required guidance:
- begin with a short answer
- follow with a simple explanation
- add a compact technical snapshot when status or checked scope matters
- then explain the deeper mechanism, implication, or fix path step by step

### 4.3 Simple Version First, Technical Version Second

When both accessibility and technical precision matter:
- present the simple version first
- then present the technical version second
- do not bury the simple model inside the technical explanation

### 4.3.1 Human-Language Paraphrase Guidance

When the topic includes internal product, runtime, architectural, or workflow terminology, provide a plain-language paraphrase when it materially improves understanding.

Required guidance:
- translate internal or technical phrases into user-facing language when the literal term alone would be hard to follow
- prefer phrasing such as `พูดง่าย ๆ`, `ถ้าพูดแบบภาษาคน`, or the English equivalent when the explanation benefits from a direct human-language gloss
- use the paraphrase to clarify the term, not to replace the underlying technical truth

### 4.3.2 Variable and Field Role Explanation Pattern

When an explanation depends on variable names, field names, config keys, enum-like values, or internal labels, the explanation should not assume the identifier name is enough.

Required guidance:
- explain what the identifier is in plain language
- explain what job it does in the mechanism, state, or decision flow
- explain where it sits in the flow when sequence matters
- explain what important values or states mean when they change the practical interpretation
- if several identifiers are central to the same explanation, group them before deep reasoning so the user is not forced to decode them one by one mid-argument

### 4.4 Good-Operator Explanation Principle

The explanation should feel like it came from a strong professional operator or collaborator, not from a scripted narrator.

Required guidance:
- prefer practical explanatory flow over performance language
- keep transitions short and functional
- use plain language without sounding patronizing or over-simplified
- explain enough for action, not enough to display intelligence for its own sake

### 4.5 Diagnostic Snapshot First for Status-Heavy Updates

When the response is a troubleshooting, implementation-progress, or verification-state update, place a compact diagnostic snapshot before deep reasoning.

Required guidance:
- show what was checked
- show what is currently true versus still pending
- show the immediate next decision or action
- keep the snapshot concise and scoped to material evidence

### 4.5.1 Main-Point-First Status Framing

For status-heavy updates, the opening line should tell the reader what the update means before the snapshot details begin.

Required guidance:
- use a short opening such as `The main issue is ...`, `This update confirms ...`, or `This test checks whether ...` when the status note would otherwise begin with raw detail
- do not make the reader infer the update purpose from the middle of the snapshot
- keep the opening claim-strength aligned to what was actually checked

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

## 6) Stepwise Natural Explanation Guidance

The rule should reduce readability loss caused by over-fragmentation and out-of-order deep detail.

Required guidance:
- avoid splitting one causal idea into many one-line bullets when a coherent paragraph would read better
- keep related reasoning steps together unless separation clearly improves scanning
- move from simple framing to deeper detail in a clear order
- explain one patch, one transition, or one causal jump at a time when the user needs a walkthrough
- when the answer is about a change, explain what changed before discussing its side effects

The goal is not verbosity. The goal is cohesion.

### 6.1 Stop-Before-Overexplaining Boundary

When the user already has enough context to understand the issue or make the next decision, the explanation should stop before it becomes stiff, repetitive, or over-produced.

Required guidance:
- do not keep deepening the same point once the practical decision surface is already clear
- prefer progression, synthesis, or closure over extra explanatory ornament
- avoid explanation that feels like a lecture when a colleague-style explanation is enough

### 6.2 Governing-Basis Clarification Boundary
When multiple materially different governing bases remain live and the answer would change depending on which one is chosen, prefer one short clarification gate over a long explanation that explores every branch.

Required guidance:
- if the governing basis is unresolved, avoid deepening several mutually exclusive downstream branches before the user chooses the active frame
- once the user chooses a basis, explain the selected branch cleanly instead of continuing to carry all branches forward
- treat unresolved basis selection as a reason to reduce complexity, not as a reason to display more analysis

---

## 7) Example, Before/After, Patch-by-Patch, and Analogy Guidance

### 7.1 Example Requirement

When an explanation is abstract, analytical, or recommendation-heavy, include at least one concrete clarifier unless the task is too simple to need one.

Acceptable clarifier forms:
- request/response lifecycle
- state transition
- architecture decision scenario
- user-visible failure case
- small code or configuration example when relevant
- before/after explanation
- patch-by-patch explanation

### 7.2 Before/After Explanation Pattern

Use before/after framing when the reader needs to understand a change in behavior, structure, ownership, or execution order.

Required guidance:
- identify the prior state
- identify the new state
- explain why the change matters

### 7.2.1 What-It-Is / What-It-Is-Not Pattern

When scope clarity matters, explicitly separate what the thing is from what it is not.

Required guidance:
- state what the current phase, feature, response, or proposal actually covers
- state what it does not cover when omission clarity matters
- use this especially when users may otherwise confuse current scope with future scope

### 7.2.2 Now / Later Pattern

When work is intentionally staged, make the timing boundary explicit.

Required guidance:
- identify what is being done now
- identify what is deferred to later
- avoid mixing active scope with future scope in one undifferentiated explanation block

### 7.2.3 User-Visible Outcome Pattern

When explaining product or workflow changes, include what the user will actually see, feel, or be able to do.

Required guidance:
- surface the user-facing outcome, not only the internal implementation
- explain what becomes easier, clearer, or intentionally hidden from the user
- use this especially when internal architecture detail is not the main point the user needs

### 7.2.4 Stage/State Progression Pattern

When the current stage is already sufficiently explained, the response should prefer the next meaningful stage, state, milestone, or decision boundary instead of continuing to deepen the same scope by default.

Required guidance:
- if the current state is already clear enough for the user's decision, move the explanation forward
- distinguish between `clarify more` and `progress next` rather than treating deeper elaboration as the default continuation
- prefer the next meaningful stage when more depth in the current stage would add little new value

### 7.2.5 Whole-Set Framing Pattern

When the checked scope shows that the user should reason about a larger complete set, present that full set before narrowing into sub-items.

Required guidance:
- present the full relevant set when that is the real decision surface
- avoid defaulting to only 2-3 items when the response should establish a larger whole first
- use narrowing only after the whole set is visible or when the user explicitly asked for incremental slicing

### 7.2.6 Governing-Basis Clarification Pattern

When multiple materially different governing bases remain live and the answer would change depending on which one is chosen, the explanation should stop and clarify the active frame before deepening the downstream analysis.

Required guidance:
- prefer one short clarification gate over explaining several mutually exclusive branches in depth
- if the governing basis is unresolved, avoid carrying all branches forward as if they were equally active
- once the user chooses a basis, deepen only the selected branch unless a real follow-up comparison is still needed
- treat unresolved basis selection as a reason to reduce complexity rather than expand it

### 7.2.7 Post-Compact Re-Anchor Pattern

When explanation resumes after compact, the explanation should re-anchor the active objective before deepening the next step.

Required guidance:
- prefer one short post-compact re-anchor over retelling the full prior conversation
- separate carried-forward facts from needs-recheck details when exact wording, exact payloads, or exact checked scope may no longer be fully preserved
- preserve the latest user-selected frame instead of reopening stale assistant branches from before compact
- continue the active selected path after re-anchor rather than rebuilding several old branches
- treat post-compact continuation as a reason to reduce replay, not a reason to expand historical narration

### 7.3 Patch-by-Patch Explanation Pattern

Use patch-by-patch framing when multiple edits or stages would otherwise blur together.

Required guidance:
- explain one patch or one phase at a time
- make order meaningful when order affects reasoning
- show how earlier changes enable later ones when that dependency matters

### 7.4 Analogy or Metaphor Guidance

Analogy is allowed when it materially clarifies an abstract mechanism.

Required guidance:
- use analogy only when it reduces confusion
- keep it short and purpose-driven
- return to the literal technical explanation after the analogy does its job
- do not let the analogy replace the real mechanism

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

Required guidance:
- when comparison-side tabular structure is justified, a table is still appropriate when it materially helps side-by-side understanding
- do not force a table when there is only one realistic path or when the comparison would be artificial
- do not force a table when the content is really a sequence, checklist, or simple status snapshot
- prefer numbered lists for sequence and bullets/grouped blocks for simple status pairs unless side-by-side scan materially improves comprehension

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
- if the content is really a sequence or a short status list, prefer numbered lists or bullets over a table
- if one short clarifier is enough, do not expand into unnecessary depth
- if one concise final synthesis is enough, do not restate the conclusion in multiple phrasings
- this rule shapes explanation quality; it does not weaken verification, safety, or user-authority rules

This design is intentionally compatible with `accurate-communication.md`, which already allows context-based flexibility.

---

## 11) Closing Contract

Analytical and technical answers should land clearly, not just stop after explanation.

This design does not own the default continuation-vs-option policy. That ownership belongs to `accurate-communication`. Explanation-quality should support clean landing and useful progression only when the user actually needs that visibility.

Required closing behavior when explanation depth matters:
- summarize the core conclusion in plain terms
- make the practical implication explicit
- provide forward motion when a real continuation path exists
- if future ideas are offered after the active work is complete or intentionally bounded, frame them as proposals rather than as implied execution continuation

Summary quality rules:
- prefer high-signal synthesis over repetition
- do not impose a rigid sentence cap
- keep the summary only as long as needed to preserve meaning
- do not restate earlier detail unless it is necessary for the final decision

Default expectation:
- if there is one clear next path and it would genuinely help the user act, state it directly
- if there are multiple reasonable next paths and presenting them would materially help the user, present short explicit options the user can choose from
- when one option is better-supported, make the recommendation explicit and explain briefly why it should happen first
- when multiple reasonable next paths genuinely remain open, preserve at least one alternative instead of collapsing the visible decision surface into the recommended path only
- if the task is already complete and no real continuation is needed, do not invent artificial next-step options
- if future ideas are offered after bounded completion, make the proposal clearly advisory and state the goal plus the expected improvement/result
- when choosing between deeper explanation of the current stage and progression to the next stage, prefer progression if the current stage is already sufficiently clear
- when the real decision surface is a larger complete set, show that full set before narrowing into sub-items

### 11.1 Short Recap Pattern

When an explanation is long, layered, or has multiple boundaries, a second-pass short recap is encouraged.

Required guidance:
- compress the explanation into one short recap after the deeper explanation if that recap materially improves retention
- use this especially after long scope clarifications, staged-plan explanations, or multi-part comparisons
- keep the recap clearly shorter and simpler than the main explanation
- do not repeat the whole answer verbatim

This contract is about response landing quality, not forced verbosity.

---

## 12) Decision Usefulness Check

Before finishing an explanation-heavy answer, it should be possible for the user to identify:
- what the main point is
- why it is true
- what trade-off matters most, if options exist
- what they can do next, if a real next move exists
- whether the response should now move to the next stage/state instead of continuing to deepen the current one
- whether the full relevant set is visible before any optional narrowing begins
- or that the task is complete, if no real continuation is needed

If the answer explains the topic well but leaves the user unable to tell either the next move or the completion state, the response is incomplete.

---

## 13) Good Patterns

### Pattern 1: Simple version first, technical version second

```markdown
Short answer: the failure is in environment handoff, not app boot.

Purpose: this explanation is diagnosing where the failure sits before we talk about the lower-level mechanism.

Simple explanation: the app starts, but when it reaches the database step it does not have the value it needs.

Technical version: startup succeeds, the first DB call fails, and the checked scope currently points to missing or misrouted `DATABASE_URL` propagation rather than a syntax or boot-time crash.
```

### Pattern 2: Before/after explanation

```markdown
Before: each route handled auth and policy checks inline.
After: the policy check moved into shared middleware.

Why this matters: transport-specific handlers now stay thinner, while the same rule logic can be reused across routes and background jobs.
```

### Pattern 2.1: List instead of table for sequence

```markdown
Current work order:
1. phase/design/TODO/changelog sync
2. schema/model migration
3. store/query rewrite
4. tests and verification
```

### Pattern 2.2: Bullets instead of table for simple status

```markdown
Current status:
- phase owner — locked
- rename map — locked
- governance targets — defined
- implementation — not started in this wave
```

### Pattern 3: Patch-by-patch explanation

```markdown
Patch 1 removes the duplicate state source.
Patch 2 rewires reads to the remaining authority.
Patch 3 updates verification so success is measured against the new path.
```

### Pattern 4: Analogy-assisted explanation

```markdown
Think of it like moving the circuit breaker out of each room and into one shared panel.

In technical terms, the auth rule moved out of each route handler into shared middleware, so one policy change no longer requires editing every handler separately.
```

### Pattern 5: Governing-basis clarification before deep analysis

```markdown
Short answer: the answer changes depending on which policy/frame we use.

Clarification needed:
- Basis A = official semantic truth
- Basis B = full comparison of possible interpretations
- Basis C = conservative operational policy

Why this matters: each basis leads to a different downstream answer.

Choose one and I’ll continue on that basis.
```

### Pattern 6: Layered walkthrough with snapshot in the middle

```markdown
Short answer: the bug is in environment handoff, not app boot.

Purpose: this update is diagnosing whether the failure happens during startup or later during database handoff.

Simple explanation: the service starts normally, but it reaches the database step without the value it needs.

Diagnostic snapshot:
- Checked: `backend/.env`, `docker-compose.yml`, startup log
- Current state: app boots, database connection fails
- Pending: verify `DATABASE_URL` injection path
- Next action: confirm runtime env source for the failing container

Reasoning path:
1. Process startup succeeds, so boot-time syntax/config parsing is not the first failure.
2. The first database call fails, which narrows the problem to configuration handoff or runtime environment state.
3. The next useful check is the actual runtime environment seen by the failing container.

What this means: fix the env propagation path before spending time on unrelated boot logic.
```

### Pattern 6: What it is / what it is not / now vs later

```markdown
What this is:
- Phase 12 is the provider-pool-first user path.

What this is not:
- It is not customer-supplied runtime orchestration.
- It is not Docker account management.

What happens now:
- Access Key flow
- AI API Gateway path
- Provider Pool-first routing UI

What stays later:
- customer-supplied runtime flow
- runtime attach/detach orchestration
- callback-driven runtime lifecycle work
```

### Pattern 7: User-visible outcome summary

```markdown
What the user will notice after this work:
- creating an Access Key feels straightforward
- the routing path is explained clearly
- the user sees that the system uses Provider Pool first
- the user does not need to understand Docker internals to use the feature
```

### Pattern 8: Patch-by-patch rollout with why each step exists

```markdown
Patch 1 removes the duplicate state source.
- Why: until there is one authority, later fixes can still read stale state.

Patch 2 rewires reads to the remaining authority.
- Why: now every consumer reads from the same source of truth.

Patch 3 updates verification against the new path.
- Why: success should be measured against the authority that now owns the flow.

This order matters because patch 2 would still be ambiguous if patch 1 had not already removed the duplicate authority.
```

### Pattern 9: Full-set framing before narrowing

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

### Pattern 10: Move to the next stage when current scope is sufficient

```markdown
Short answer: Phase 12 is clear enough now.

What happens next:
- stop deepening the same Phase 12 explanation
- move to the implementation checklist for Phase 12
- keep Phase 18 as deferred scope
```

### Pattern 11: Short recap after a long explanation

```markdown
Short recap:
- Phase 12 = what we are really doing now
- Phase 18 = the future runtime-management path
- the current goal is a simpler Provider Pool-first user flow
```

### Pattern 12: Variable and field explanation before deep reasoning

```markdown
Short answer: the current state is not holding a usable secret anymore.

Before the deeper reasoning, clarify the identifiers:
- `tokenValue` = the real secret value the system can use to call the API
- `hasSecretMaterial` = whether the current state still has that real secret stored
- `secretMaterialSource` = where the current state came from, such as inventory/search or a reveal step

What the values mean here:
- `tokenValue = null` = no usable secret is stored in this state
- `hasSecretMaterial = false` = the state has metadata only, not the real key
- `secretMaterialSource = inventory_or_search` = this state came from discovery, not from a successful reveal

Reasoning path:
1. the lane previously passed proof, so it had a usable secret earlier
2. the current state now shows metadata-only values
3. that means the current state was likely overwritten or downgraded after the earlier usable state existed
```

### Pattern 13: Post-compact re-anchor before continued explanation

```markdown
Short answer: we can continue, but first I need to re-anchor the active state after compact.

Post-compact re-anchor:
- Current objective: continue the active implementation slice already chosen by the user
- Carried-forward facts: the governing basis is already selected and the touched owner set is unchanged
- Needs recheck: any exact payload wording or exact previously checked evidence that may have been compressed away
- Next action: continue the active path if the remaining state is still clear; otherwise recheck the exact missing detail before treating it as verified fact
```

### Pattern 14: Goal-qualified proposal after bounded completion

```markdown
The active cleanup wave is done.

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

## 13.1 Anti-Patterns to Avoid

| Anti-Pattern | Why It Hurts | Better Shape |
|--------------|--------------|--------------|
| architecture-first or metaphor-heavy explanation with no direct human-action/result translation | the reader understands the system wording only after extra decoding | restate the explanation in direct terms that say what changed, what the user can do, or what result is visible |
| the explanation starts with setup detail instead of what it is doing | the reader only discovers the point after reading several sentences | open with one purpose-first sentence that says what is being tested, diagnosed, proposed, recommended, or concluded |
| raw identifiers used as if their names explain the mechanism | the reader sees variable names but not their job or value meaning | explain what the identifier is, what role it plays, where it sits in the flow, and what important values mean before deeper reasoning |
| comparison in scattered bullets | trade-offs become harder to evaluate | use a compact comparison table |
| sequence forced into a table | the reader gets a heavier layout than the information needs | use a numbered list instead |
| simple status pairs forced into a table | visual structure becomes heavier than the content | use bullets or grouped blocks unless side-by-side scan materially helps |
| boxed ASCII table used as the ordinary explanation-side default | source becomes bulky and harder to maintain without adding semantic value | prefer a lighter table or a non-table form instead |

---

## 14) Integration with Existing Rules

| Rule | Relationship |
|------|--------------|
| `accurate-communication.md` | Keeps explanation structure flexible while requiring concise, high-signal endings and honest snapshot wording |
| `answer-presentation.md` | Owns the layout of snapshot sections, headings, and small fact tables |
| `flow-diagram-no-frame.md` | Governs any text flow diagram used by this rule |
| `zero-hallucination.md` | Preserves verification requirements for technical claims inside explanations |
| `anti-sycophancy.md` | Prevents recommendation quality from drifting into agreement without reasoning |

---

> Full history: [../changelog/explanation-quality.changelog.md](../changelog/explanation-quality.changelog.md)
