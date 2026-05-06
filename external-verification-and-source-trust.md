# External Verification and Source Trust
> **Current Version:** 1.2
> **Design:** [design/external-verification-and-source-trust.design.md](design/external-verification-and-source-trust.design.md) v1.2
> **Session:** d42465eb-30a7-4bc8-b9d6-03e52306e9a5
> **Full history:** [changelog/external-verification-and-source-trust.changelog.md](changelog/external-verification-and-source-trust.changelog.md)
---
## Rule Statement
**Core Principle: When external factual claims materially affect analysis, design, accuracy, or recommendations, verify proactively, rank source trust explicitly, compare sources when needed, and report conflicts honestly.**
This rule owns WebSearch/WebFetch-backed external verification triggers, source trust, corroboration, source-conflict handling, research-lane source-trust expectations, and external evidence as proof-aware grounding rather than automatic decision lock. It does not replace native worker routing, which decides when broad research should be delegated.
---
## Core Contract
### Proactive verification
When a cheap external check resolves a material factual question:
- verify current external facts when material
- prefer checking over unsupported reassurance or passive hesitation
- skip external checks for trivial, conceptual, speculative, or local-source-of-truth questions
### Orchestrated external research
When external research is broad, comparison-heavy, source-volume-heavy, or intended to improve a design/recommendation, use `native-worker-agent-routing-and-context-control.md` to decide whether one or more research lanes should gather evidence before the leader absorbs raw sources.
Required guidance:
- research lane assignments should include the factual question, decision surface, preferred source tiers, and conflict-reporting expectations
- research lane handoffs should report checked topic/query families, source authority/freshness/specificity, downgraded weak sources, conflicts, and what evidence the leader should verify directly
- worker-collected sources remain evidence inputs; leader synthesis still decides claim strength and recommendation wording
- do not delegate trivial one-source checks merely because an external lookup is involved
### Source trust
Rank sources by authority, freshness, specificity, and relevance.
Required guidance:
- prefer `AUTHORITATIVE_EXTERNAL` primary technical authorities over secondary summaries
- downgrade stale, vague, inconsistent, marketing-shaped, untraceable, broken, or weak-accountability sources
- do not average trust across unequal sources
### Corroboration and conflict
Use multiple sources for high-impact, ambiguous, contradictory, stale, non-primary, version/provider-dependent, or security/compliance-sensitive claims. If sources conflict, name the conflict, identify the stronger source and why, avoid silently picking convenience, and say what would settle unresolved conflict.
### Recommendation and design integrity
If a recommendation, disagreement, or design judgment depends on current external facts, verify first when practical and proportional, prefer primary sources, corroborate when impact is high or source strength is weak, and align wording to gathered evidence. External evidence becomes binding only when it is an authoritative requirement, compatibility limit, safety/compliance boundary, or verified contradiction; otherwise preserve trade-offs and user goals.
### Honest fallback
If verification remains incomplete, separate verified from likely, state what remains unresolved, provide the best bounded recommendation still justified, and avoid false certainty or unnecessary blockage.
---
## External Verification Triggers
Use proactive WebSearch/WebFetch-backed verification for:
- current API / SDK / CLI / product behavior
- version-specific or vendor-specific capability
- pricing, support, release status, policy, or compatibility
- security-sensitive or compliance-sensitive external fact
- decision-critical external fact the user may act on
- standards, provider constraints, or current behavior that materially shapes analysis, design, or recommendation
- broad design-improvement or recommendation research where source breadth, comparison cost, or topic independence makes worker-lane research useful
Prefer verification when information drifts, depends on current vendor/runtime state, quick checking reduces material uncertainty, or the user prioritizes accuracy. Usually skip when the question is conceptual, local project evidence is source of truth, or the user asks for speculative discussion.
---
## Source Reliability Ladder
| Tier | Source Type | Trust | Examples |
|---|---|---|---|
| 1 | primary official technical authority | highest | docs, specs, API references, standards bodies |
| 2 | primary official update authority | very high | release notes, changelogs, status pages, support matrices |
| 3 | maintainer/repository authority | high | maintainer docs, authoritative issues/comments |
| 4 | reputable secondary explanation | medium | references citing primary sources |
| 5 | tutorial/blog/aggregator | lower | tutorials, blogs, generic summaries |
| 6 | anecdotal/weak-accountability source | lowest | forum anecdotes, reposts, unclear mirrors |
Before trusting strongly, check whether the source is primary, fresh, normative, precise, consistent with stronger sources, and free of obvious failure.
---
## Corroboration and Conflict Rules
One source is enough only when it is strong primary authority, directly answers a routine low-risk claim, and no contradiction or ambiguity is visible.

Multi-source comparison is required or preferred when the claim is high-impact, recommendation-critical, incomplete, ambiguous, stale, secondary-source-based, version/provider-dependent, conflicting, or security/compliance-sensitive.

When comparing:
- prefer stronger independent convergence
- explain why one source is preferred when they disagree
- do not treat sources as equal because they mention the same topic
- if conflict remains unresolved, give the best bounded reading and what would settle it
- if a source is incoherent or contradicted by stronger evidence, treat it as unreliable rather than equal
---
## Anti-Patterns
Avoid vague non-checking when cheap verification matters, unchecked external assumptions in recommendations, weak-source trust, one-source high-impact conclusions, silent source-conflict resolution, broken-source credibility, raw research-lane source dumps without trust/conflict analysis, leader over-absorption of broad external research that should have been lane-filtered, and treating ordinary external evidence as the only valid design path.
---
## Quality Metrics
| Metric | Target |
|---|---|
| Proactive external verification on material current facts | High |
| Proof-aware external grounding for recommendations/design | High |
| Source reliability ranking clarity | High |
| Multi-source comparison on high-impact/ambiguous claims | High |
| Silent source-conflict resolution | 0 critical cases |
| Over-trusting weak secondary sources | 0 critical cases |
| Honest bounded fallback | High |
| Research-lane source-trust handoff quality | High when broad research is delegated |
---
## Integration
Related rules:
- [zero-hallucination.md](zero-hallucination.md) - factual discipline; deeper external source trust defers here
- [evidence-grounded-burden-of-proof.md](evidence-grounded-burden-of-proof.md) - consumes source strength into claim thresholds
- [accurate-communication.md](accurate-communication.md) - source conflict and evidence-strength wording
- [anti-sycophancy.md](anti-sycophancy.md) - disagreement posture when stronger external evidence conflicts with a claim
- [operational-failure-handling.md](operational-failure-handling.md) - retry/stop/escalation after web failures
- [native-worker-agent-routing-and-context-control.md](native-worker-agent-routing-and-context-control.md) - decides when broad external research should be decomposed into standalone worker lanes before leader raw source absorption
---
