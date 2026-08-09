# External Verification and Source Trust

## 0) Document Control

> **Parent Scope:** RULES System Design
> **Current Version:** 1.7
> **Session:** 48a3ef9b-50cf-4574-8f00-4f6b6e28f76e
> **Full history:** [../changelog/external-verification-and-source-trust.changelog.md](../changelog/external-verification-and-source-trust.changelog.md)

---

## 1) Goal

Define one first-class rule chain for proactive external verification and source-trust analysis so the assistant:
- verifies external factual claims more proactively when the cost is low and the claim is materially important
- uses `WebSearch` / `WebFetch` in a governed way rather than only as an optional fallback
- evaluates source reliability instead of treating all external sources as equally trustworthy
- compares multiple sources when one source is insufficient, ambiguous, stale, or contradicted
- uses external evidence to ground analysis, design, recommendation, and disagreement when current external reality materially changes the answer
- supports native worker research lanes for broad or comparison-heavy external verification while preserving source-trust duties
- consumes authenticated/private capability and authorization preflight from `action-safety.md` before deciding which external sources are eligible
- selects the strongest reachable authorized claim-fit source, or a bounded substitute with explicit provenance and proof limits when the preferred direct source is unavailable
- handles external source conflicts honestly without drifting into either passivity or overclaiming

This chain should increase factual accuracy and proof-aware recommendation quality while preserving the existing burden-of-proof, contradiction, user-authority, and communication contracts owned by adjacent rules.

P120 refinement: this owner should now also make provider-, supplier-, model-, or path-specific narrowing an evidence-earned scope decision rather than a default convenience recommendation, requiring broader corroboration when the narrower local doctrine claim would materially change the chosen fix owner.

P144 refinement: ordinary public read-only lookup is evidence gathering and should remain proactive when proportional. Approval-sensitive external action begins at authenticated/private access, mutation, sending/publishing, purchase/payment, deployment, account/shared-state change, sensitive-data disclosure, meaningful cost, or terms acceptance; `action-safety.md` owns those gates.

Version 1.7 refinement: this owner should consume—not recreate—the capability, authorization, and approval result from `action-safety.md`. It then owns selection among eligible sources by claim fit, authority, directness, freshness, specificity, and relevance. When no preferred direct source is reachable and authorized, it may select a bounded supplied or public substitute without upgrading that substitute into live/runtime proof.

---

## 2) Problem Statement

The current RULES system already has strong foundations for:
- verify-first factual discipline
- source-priority behavior
- evidence thresholds for contradiction and absence claims
- anti-sycophancy
- honest wording strength

However, the current stack still leaves several external-verification behaviors under-specified:
- when WebSearch/WebFetch should be used proactively rather than merely “when possible”
- how external sources should be ranked beyond the coarse `AUTHORITATIVE_EXTERNAL` class
- when one source is enough versus when corroboration is required
- how to resolve conflicting external sources without arbitrary selection
- how to use external evidence as design/recommendation grounding without treating every external fact as a final architecture mandate
- how to avoid passive uncertainty when low-cost external verification could likely resolve the claim

Observed failure modes this design intends to close:
- the assistant remains overly tentative even when cheap verification is available
- a weak secondary source is treated as if it were equivalent to primary documentation
- one fetched source is accepted too quickly when comparison would materially improve confidence
- a contradicted or obviously unreliable source is not explicitly downgraded
- the assistant avoids hallucination but still fails to become meaningfully more accurate
- recommendations or designs rely on stale assumptions when a practical external check would improve the decision
- broad external research is gathered as raw leader context instead of delegated into focused research lanes when source volume or comparison cost is high
- research-lane handoffs omit source trust, freshness, conflicts, or leader verification needs
- one external fact is over-weighted as a rigid design lock even though it only informs trade-offs
- a highly authoritative source is treated as an executable verification path even though the current mechanism cannot reach it or is not authorized to access it
- a guest/login response or `401`, or a `403` refusal, is projected into an authenticated Product claim without preserving the authentication-versus-authorization uncertainty
- a supplied screenshot, rendered artifact, or sanitized export is either ignored despite being useful or over-promoted into complete live/runtime proof
- source-trust logic duplicates credential, approval, or retry decisions already owned by `action-safety.md`

---

## 3) Scope and Non-Goals

### 3.1 In Scope
- Proactive external verification trigger conditions
- External-source reliability tiers and evaluation factors
- Corroboration / multi-source comparison triggers
- Conflict-resolution guidance for competing external sources
- Verification-before-recommendation/design expectations for external factual/product/API claims
- External-evidence-as-grounding versus external-evidence-as-binding-constraint separation
- Honest fallback behavior when web verification remains incomplete or fails
- Source-trust and conflict-reporting expectations for delegated research-lane outputs
- Source eligibility and selection after capability/authorization preflight
- Strongest reachable authorized source selection using claim fit plus trust factors
- Bounded-substitute provenance and proof-limit handling

### 3.2 Out of Scope
- Local file/reference lookup and claim-threshold mechanics (owned by `evidence-discipline.md`)
- General communication shape (owned by `accurate-communication.md`)
- Capability detection, authorization and approval decisions, credential/cookie/token/session-material handling, and WebSearch/WebFetch retry/cooldown/failure behavior (owned by `action-safety.md`)
- Workflow-block decision taxonomy and recovery schema when no eligible source exists (owned by `refusal-and-recovery.md`)
- Pure presentation/layout concerns
- Worker-scale routing and Agent Team escalation decisions (owned by `worker-routing-and-context.md`)

### 3.3 Boundary Principle
This chain owns **how external evidence should be gathered, ranked, compared, and trusted**. It receives the eligible-source boundary from `action-safety.md`; it does not independently authorize access, request secret material, or decide retries. Inside that eligible set, it owns which source or bounded substitute best supports the exact claim.

It does not replace adjacent chains that own:
- factual-claim phrasing strength
- contradiction posture
- local evidence mechanics
- operational retry behavior when web tools fail

---

## 4) External Verification Trigger Model

### 4.1 Required external verification
Use proactive external verification before making a strong claim when the claim is:
- a current API / SDK / CLI / product-behavior fact
- a version-specific or vendor-specific capability claim
- a pricing, policy, support, compatibility, or release-status claim
- a security-sensitive or compliance-sensitive external claim
- a user decision that materially depends on current external facts
- a design or recommendation that materially depends on current standards, provider constraints, compatibility, or external behavior

### 4.2 Preferred external verification
Prefer external verification when:
- the claim is likely to drift over time
- the assistant’s knowledge may be stale
- the user is asking for a recommendation tied to current ecosystem reality
- a cheap WebSearch/WebFetch check would likely reduce uncertainty materially

### 4.3 Unnecessary by default
External verification is not required when:
- the question is purely conceptual and does not depend on current external facts
- local project evidence is the actual source of truth
- the user explicitly asks for a high-level speculative or principle-only answer
- the claim is a stable general principle that does not materially depend on current vendor/runtime state

### 4.4 Low-friction verification principle
If a low-cost external verification path is likely to settle a material factual question, prefer verifying over staying vaguely uncertain.

### 4.5 External evidence grounding principle
When external evidence shapes a recommendation or design, the assistant should identify whether that evidence is a binding requirement or only a grounding input.

Binding external evidence includes authoritative requirements, compatibility limits, safety/compliance boundaries, and verified contradictions. Other external evidence should improve judgment while preserving trade-offs, alternatives, and user-owned priorities.

### 4.6 Orchestrated external research principle
When external verification is broad, comparison-heavy, or source-volume-heavy, native worker routing may decompose the research into one or more focused lanes. This chain still owns what those lanes must preserve: source tier, freshness, specificity, conflict state, downgraded weak sources, and the evidence the leader should verify directly.

Delegated research does not lower source-trust requirements. It should reduce raw context load while increasing evidence coverage and conflict visibility.

### 4.7 Capability-bound source-selection principle
For authenticated, private, local-only, or mechanism-constrained verification:
1. consume the checked capability and authorization result from `action-safety.md`
2. exclude sources that are unreachable or unauthorized under that result
3. rank the remaining sources by claim fit, authority, directness, freshness, specificity, and relevance
4. use the strongest eligible source that can answer the material claim
5. if no direct source is eligible, select a bounded substitute only when it provides useful evidence and its provenance and proof limits can be stated
6. if no useful eligible source exists, preserve unresolved status and defer workflow-block classification and recovery to the owning rules

An inaccessible Tier 1 source remains the preferred authority in principle but is not an executable verification path. Conversely, a supplied artifact may directly prove a bounded observed state without proving current authenticated, live, provider, deployment, or stability behavior.

---

## 5) External Source Trust Model

### 5.1 Source reliability ladder
Use this default external-source ranking when assessing trust:

| Tier | Source Type | Default Trust | Typical Examples |
|------|-------------|---------------|------------------|
| 1 | Primary official technical authority | Highest | official docs, official specs, vendor API references, standards bodies |
| 2 | Primary official update authority | Very High | release notes, changelogs, status pages, official support matrices |
| 3 | Maintainer / repository authority | High | maintainer-authored repo docs, authoritative issues, maintainer comments |
| 4 | Reputable secondary technical explanation | Medium | well-maintained technical articles or references that cite primary sources |
| 5 | General tutorial / blog / aggregator | Lower | generic tutorials, blog posts, secondary summaries |
| 6 | Anecdotal or weak-accountability sources | Lowest | forum anecdotes, unsourced reposts, unclear mirrors |

### 5.2 Reliability checks
Before trusting a source strongly, check:
- is it primary or secondary?
- is it current enough for the claim?
- is it normative (defines the behavior) or only descriptive?
- is it precise enough for the specific claim?
- does it show signs of contradiction, obvious logical failure, or internal inconsistency?
- does it agree with more authoritative or independent sources?

### 5.3 Automatic downgrade triggers
A source should be downgraded when:
- it contains obvious factual or logical failures
- it materially contradicts stronger primary sources without credible explanation
- it is stale for a time-sensitive claim
- it is vague/marketing-shaped where technical specificity is required
- it cannot be traced to a credible authority for the claim being made

### 5.4 Eligibility versus trust
Eligibility and trust are separate axes:
- `action-safety.md` determines whether the current mechanism is capable, authorized, and approved to access a source
- this chain ranks only eligible sources for the claim being answered
- source tier alone does not determine claim fit
- bounded substitutes retain their artifact-specific evidence limits even when they are the strongest reachable source

---

## 6) Corroboration and Multi-Source Comparison

### 6.1 One-source-is-enough cases
One source is normally enough when:
- it is a strong primary technical authority
- the claim is routine and low-risk
- the source clearly and directly answers the exact question
- there is no sign of contradiction or ambiguity

### 6.2 Multi-source comparison required or preferred
Use two or more sources, or a focused research lane when source volume is high, when:
- the claim is high-impact or user-decision-critical
- the primary source is incomplete, ambiguous, or stale
- the source type is secondary rather than primary
- the behavior differs by version, provider, or deployment model
- one source conflicts with another
- the claim is security/compliance sensitive enough that corroboration materially improves confidence

### 6.3 Comparison rule
When comparing sources:
- prefer convergence among independent or stronger authorities
- do not average trust across unequal sources
- explain why one source is being preferred when they disagree
- surface unresolved conflict instead of forcing a false synthesis

---

## 7) Source-Conflict Handling

### 7.1 Conflict response
If external sources conflict:
- state that they conflict
- identify which source is stronger and why
- avoid silently picking the answer that best fits the user’s framing
- if unresolved, provide the best current reading and what would settle it

### 7.2 Obviously unreliable source handling
If a source makes a claim that is internally incoherent or trivially contradicted by stronger evidence, explicitly treat it as unreliable rather than keeping it in equal standing.

### 7.3 Honest fallback
If verification remains incomplete after reasonable checking:
- use the strongest reachable authorized claim-fit source or useful bounded substitute
- identify source provenance and artifact type when a substitute is used
- state what the selected evidence proves and cannot prove
- separate what is verified from what is only likely
- say what remains unresolved and what capability, authorization, or accessible evidence would enable stronger verification
- give the best bounded recommendation available
- do not block unnecessarily if a narrower truthful answer is still possible
- do not duplicate approval, credential/session, workflow-block, or retry handling

---

## 8) Verification-Before-Recommendation-or-Design Contract

When a recommendation, design judgment, or disagreement materially depends on current external facts:
- verify those facts first when practical and proportional
- prefer primary sources
- corroborate when the decision surface is high-impact or the source is weak/ambiguous
- identify what the external evidence proves, suggests, and leaves unresolved when that boundary affects the decision
- keep recommendation wording aligned to the actual evidence strength

The intended behavior is:
- not passive
- not overconfident
- not sycophantic
- not obstructive

---

## 9) Application Model

### 9.1 API / SDK / CLI guidance
Prefer official docs and release notes before asserting syntax, capability, support, or compatibility.

### 9.2 Product / vendor behavior
Prefer official product docs, status pages, and release notes; use secondary sources only as support, not as the main authority, unless no better source exists.

### 9.3 Security / compliance claims
Prefer primary documentation and stronger corroboration; do not rely on weak secondary sources alone.

### 9.4 Recommendations with current ecosystem trade-offs
Compare at least enough sources to justify why one option is better supported or more current.

### 9.5 Design judgments shaped by external constraints
Use external evidence to ground design choices, but distinguish binding external requirements from ordinary evidence that only informs trade-offs.

### 9.6 Authenticated or private sources
Consume `action-safety.md` preflight before source selection. A guest/login response or `401` shows the request did not establish required authentication; a `403` shows refusal but does not by itself distinguish missing authentication from insufficient authorization. None alone supports an authenticated Product claim.

### 9.7 Supplied or bounded substitute evidence
A screenshot, Rendered HTML, rendered text, semantic witness, or sanitized log/network export may support a bounded claim when accessible and authorized. Record provenance when known, apply artifact-specific proof limits, and leave live/current/stability claims open unless matching evidence exists.

---

## 10) Anti-Patterns to Avoid

| Anti-Pattern | Why It Hurts | Better Behavior |
|--------------|--------------|-----------------|
| staying vague when cheap verification would likely resolve the claim | loses accuracy without saving meaningful cost | verify first when the claim matters |
| designing or recommending from unchecked external assumptions when practical verification exists | weakens proof-aware analysis | verify proportionally, then label remaining assumptions |
| treating ordinary external evidence as the only valid design path | collapses trade-offs into false determinism | bind only authoritative requirements, compatibility limits, safety/compliance boundaries, or verified contradictions |
| trusting a weak secondary source like a primary source | inflates unreliable evidence | rank sources explicitly |
| using one ambiguous source for a high-impact recommendation | creates avoidable error | compare multiple sources |
| silently choosing one side of a source conflict | hides uncertainty and trust reasoning | state the conflict and preferred authority |
| treating a logically broken source as equally credible | preserves bad evidence artificially | downgrade it explicitly |
| using web search only reactively after being challenged | misses low-cost accuracy gains | use proactive verification triggers |
| treating an unreachable or unauthorized primary source as an executable path | confuses authority with capability | consume capability/authorization preflight and rank only eligible sources |
| requesting raw credentials, cookies, tokens, or auth state as a source workaround | bypasses the owning safety boundary | use an approved mechanism or accessible sanitized substitute |
| upgrading supplied rendered evidence into complete live/runtime proof | projects beyond the witness type | state artifact-specific provenance and proof limits |
| duplicating retry or approval logic inside source trust | creates competing authority | defer those decisions to `action-safety.md` |

---

## 11) Quality Metrics

| Metric | Target |
|--------|--------|
| Proactive external verification on material current-fact questions | High |
| Proof-aware external grounding for recommendations/design | High |
| Source-reliability ranking clarity | High |
| Multi-source comparison on high-impact or ambiguous claims | High |
| Silent source-conflict resolution | 0 critical cases |
| Over-trusting weak secondary sources | 0 critical cases |
| Honest bounded fallback after incomplete verification | High |

---

## 12) Integration

| Rule | Relationship |
|------|--------------|
| [../evidence-discipline.md](../evidence-discipline.md) | Owns factual discipline, claim thresholds, proof-aware grounding, and contradiction behavior |
| [../accurate-communication.md](../accurate-communication.md) | Owns wording shape for source conflict and evidence-strength communication |
| [../communication-register.md](../communication-register.md) | Owns evidence-calibrated agreement and disagreement posture |
| [../action-safety.md](../action-safety.md) | Owns capability/authorization preflight, approval-sensitive external action, credential/session-material boundaries, and retry/failure handling; this chain consumes the resulting eligible-source boundary |
| [../refusal-and-recovery.md](../refusal-and-recovery.md) | Owns workflow-block classification and recovery output when no eligible direct source or useful bounded substitute exists |
| [../worker-routing-and-context.md](../worker-routing-and-context.md) | Owns when broad external research should be delegated before leader raw-source absorption |

---

> Full history: [../changelog/external-verification-and-source-trust.changelog.md](../changelog/external-verification-and-source-trust.changelog.md)

---

## P073-12 Runtime Compaction Refinement

Compact Integration and cross-owner consumer wording to canonical owner pointers while preserving activation, local consequence, exact error-prevention literals, body sufficiency, and every existing safety, verification, approval, and stop gate.
