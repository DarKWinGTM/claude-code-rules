# External Verification and Source Trust
> **Current Version:** 1.9
> **Design:** [design/external-verification-and-source-trust.design.md](design/external-verification-and-source-trust.design.md) v1.9
> **Session:** 08244912-a195-4926-84e6-8c202c667ba5
> **Full history:** [changelog/external-verification-and-source-trust.changelog.md](changelog/external-verification-and-source-trust.changelog.md)

## Rule Statement

**Core Principle: Verify decision-changing external facts proactively. Select eligible claim-fit sources, preserve unequal authority, and expose conflicts/proof limits before recommending a route.**

## When to Verify

Use cheap public read-only lookup when current reality matters: drift-prone API/SDK/CLI/product behavior, vendor/version capability, pricing/support/releases/policy/compatibility, provider/standard constraints, security/compliance. Skip trivial/conceptual/speculative or locally authoritative questions unless an external premise changes the answer.

Private/authenticated or consequential actions require [safety](action-safety.md) preflight/approval. Evidence gathering cannot authorize publishing, mutation, payment, deployment, shared-state change, sensitive disclosure, meaningful cost or terms acceptance.

## Eligibility Before Trust

For private/authenticated/local-only/mechanism-constrained evidence, establish reachability, tool/session, authorization and approval before ranking. An inaccessible/unapproved Tier1 source is not an executable route.

Rank eligible sources by authority, directness, freshness, specificity and exact claim fit. A reachable artifact supports observed content, not inherited current/live/authenticated proof. If direct evidence is unavailable, use the strongest authorized bounded substitute—supplied screenshot/rendered artifact/sanitized export/public authority—with provenance, supported dimensions, omissions and prerequisites for stronger [proof](evidence-discipline.md).

If no useful eligible source exists, keep verification unresolved and give [missing-state/access recovery](refusal-and-recovery.md). Do not probe unapproved private paths or solicit raw auth material. Ranking cannot bypass safety's approval, credentials/session or retry gates.

## Source Ranking

| Tier | Authority | Default trust |
|---|---|---|
| 1 | official technical docs/specs/API references/standards | highest |
| 2 | official releases/updates/changelogs/status/support matrices | very high |
| 3 | maintainer/repository docs, authoritative issues/comments | high |
| 4 | reputable secondary explanation citing primary sources | medium |
| 5 | tutorials/blogs/aggregators | lower |
| 6 | anecdotes/forums/reposts/unclear mirrors | lowest |

Tier is not automatic claim fit. Check directness, freshness, normative force, precision, consistency and traceability. Prefer claim-fit `AUTHORITATIVE_EXTERNAL` primary sources; downgrade stale/vague/marketing-shaped/broken/incoherent/unaccountable material. Do not average unequal trust or equate same-topic mentions.

One strong primary source suffices for a direct routine low-risk answer without visible conflict. Corroborate high-impact/recommendation-critical/security/compliance, version/provider-dependent, incomplete/ambiguous/stale/secondary or conflicting claims. Prefer independent convergence; explain conflict, stronger source/why and what would resolve uncertainty.

## Research and Recommendations

Define the decision research can change; stop at sufficiency. Narrow broad comparisons before [routing](worker-routing-and-context.md), not delegation for every lookup. Brief a lane with question, decision, preferred tiers and conflict expectations. Its digest names query families, source quality/freshness/specificity, conflicts, implications and leader anchors. Worker output is input, not proof or source authority.

Ground material design/recommendation/disagreement in proportionate current evidence. Provider/supplier/model/path-specific narrowing needs checked local differences, not convenience. Only authoritative requirements, compatibility limits, safety/compliance or verified contradictions bind the route; ordinary evidence preserves goals and trade-offs.

For partial proof, recommend only the justified scope: separate verified/likely/unresolved, provenance/limits and enabling evidence/state. A substitute is not live proof; unavailable evidence does not mandate new infrastructure.

## Integration and Boundaries

[Evidence](evidence-discipline.md) owns thresholds/witness limits; [accurate wording](accurate-communication.md) and [register](communication-register.md) render them. This owner ranks eligible sources and resolves conflicts, not safety, recovery or worker topology.
