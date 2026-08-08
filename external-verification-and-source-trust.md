# External Verification and Source Trust
> **Current Version:** 1.4
> **Design:** [design/external-verification-and-source-trust.design.md](design/external-verification-and-source-trust.design.md) v1.4
> **Session:** 92c4d51e-eb02-4299-823a-1a6b8270f045
> **Full history:** [changelog/external-verification-and-source-trust.changelog.md](changelog/external-verification-and-source-trust.changelog.md)
---
## Rule Statement
**Core Principle: When external factual claims materially affect analysis, design, accuracy, or recommendations, verify proactively, rank source trust explicitly, compare sources when needed, and report conflicts honestly.**
---
## Core Contract
### Proactive verification
When a cheap external check resolves a material factual question:
- verify current external facts when material
- prefer checking over unsupported reassurance or passive hesitation
- skip external checks for trivial, conceptual, speculative, or local-source-of-truth questions
### Orchestrated external research
When external research is broad, comparison-heavy, source-volume-heavy, or intended to improve a design/recommendation, use `worker-routing-and-context.md` to decide whether one or more research lanes should gather evidence before the leader absorbs raw sources.
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

When a recommendation is about provider-, supplier-, model-, or path-specific fix scope, treat that narrower scope as something the evidence must earn. Compare whether the same observed issue is better explained by a shared mechanism before presenting the local scope as the strategic fix owner.
### Honest fallback
If verification remains incomplete, separate verified from likely, state what remains unresolved, provide the best bounded recommendation still justified, and avoid false certainty or unnecessary blockage.
---
## External Verification Triggers
Verify drift-prone or decision-critical current API/SDK/CLI/product behavior, vendor/version capability, pricing/support/release/policy/compatibility, standards/provider constraints, security/compliance facts, and claims that materially narrow a fix to one supplier/model/path. Broad source-heavy design/recommendation research passes the worker research gate. Skip conceptual, speculative, or local-source-of-truth questions unless external facts materially affect the answer.
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
## Integration
Related owners: [evidence-discipline.md](evidence-discipline.md) for claim thresholds, [accurate-communication.md](accurate-communication.md) and [communication-register.md](communication-register.md) for wording/disagreement, [worker-routing-and-context.md](worker-routing-and-context.md) for broad research, and [action-safety.md](action-safety.md) for lookup failure/retry behavior.
---
