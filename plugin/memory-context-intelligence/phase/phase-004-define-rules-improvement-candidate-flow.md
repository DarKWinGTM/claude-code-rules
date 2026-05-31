# Phase 004 - Define RULES improvement candidate flow

> **Summary File:** [SUMMARY.md](SUMMARY.md)
> **Phase ID:** 004
> **Status:** Completed
> **Design References:** [../design/design.md](../design/design.md), [../design/01-memsearch-required-dependency.design.md](../design/01-memsearch-required-dependency.design.md), [../design/05-additional-staging-and-promotion.design.md](../design/05-additional-staging-and-promotion.design.md)
> **Patch References:** [../patch/memory-context-intelligence-design-only-baseline.patch.md](../patch/memory-context-intelligence-design-only-baseline.patch.md)

---

## Objective

Define the doctrine for converting memsearch-derived memory signals into advisory candidate packets that can become `/additional/` trial-stage rule proposals only after current evidence and user selection support that path.

## Why this phase exists

The capsule is meant to improve RULES understanding and maturity, but not by directly generating or mutating main RULES from memory. Memory signals can raise candidate topics, but current transcript evidence, active project evidence, active RULES, and user authority decide whether any candidate becomes governed work.

## Goal

Lock the doctrine that turns memory-derived signal into advisory candidate packets without allowing memory to bypass current evidence, user authority, `/additional/` trial staging, or later governed review.

## Output

- defined signal-to-candidate packet flow
- required candidate packet content and authority-boundary notes
- transcript/current-evidence check requirement before stronger claims
- `/additional/` trial-stage mapping before any main RULES merge discussion
- explicit promotion criteria for later governed follow-up
- explicit phase boundary that keeps emission, live trial, promotion audit, and main merge in later phases

## Gate

This phase is complete when the capsule has a doctrine-only candidate flow that is strong enough to govern later implementation phases but still prevents direct memory-to-main-RULES mutation.

## Owner

Capsule governance owner for candidate-flow doctrine and authority boundaries.

## Files

This phase defines doctrine only inside the capsule governance chain. It does not create runtime implementation, emit trial-stage rule material, or mutate main RULES.

## Doctrine

Signal-to-candidate flow:

```text
memsearch-derived work trace signal
  → transcript and current-evidence check
  → advisory candidate packet
  → user-selected governed work candidate
  → `/additional/` trial-stage proposal
  → later promotion audit before any main RULES merge
```

Required candidate packet content:
- source signal and why it surfaced from real work traces
- transcript/current-evidence checks that support or limit the candidate
- authority boundary notes showing active RULES, current evidence, and user instruction outrank memory-derived suggestions
- proposed `/additional/` trial-stage rule shape, not a direct main-rule edit
- promotion evidence needed before later main RULES follow-up

User authority boundary:
- candidate packets are advisory until the user selects them as governed work
- the capsule may recommend `/additional/` trial-stage experimentation, but it must not treat memory frequency, agent synthesis, or research enrichment as permission to merge into main RULES
- promotion from `/additional/` trial-stage use requires observed usefulness, no authority-boundary drift, compatibility with current RULES doctrine, and a later governed review path

Phase boundary:
- Phase 004 defines doctrine only
- actual candidate packet emission belongs to Phase 013
- live bounded `/additional/` trial belongs to Phase 015
- promotion readiness audit belongs to Phase 017
- possible main RULES merge belongs to Phase 018

## Action points

- [x] define signal-to-candidate packet flow
- [x] require transcript/current-evidence checks before stronger claims
- [x] map candidate outputs to `/additional/` trial-stage rule proposals before any main-rule merge
- [x] preserve user authority over whether a candidate becomes governed work
- [x] define promotion criteria from `/additional/` trial-stage use into later main RULES follow-up

## Verification

- memory signals can create candidate packets, but memory does not become direct rule authority
- candidate packets remain advisory until selected by the user and supported by transcript/current-evidence checks
- current evidence, active RULES, and user instruction outrank memory-derived suggestions at every step
- candidate output maps to `/additional/` trial-stage proposal material before any main-rule merge is considered
- promotion requires later evidence from `/additional/` trial-stage use, authority-boundary review, and compatibility with main RULES doctrine
- this phase does not implement emission, live trial, promotion audit, or main merge behavior; those remain assigned to Phases 013, 015, 017, and 018

## Exit criteria

- the capsule has a clear doctrine path from memory signal to candidate packet, user-selected governed work, `/additional/` trial-stage proposal, and later governed review
- stronger claims require transcript/current-evidence checks before candidate material can be treated as more than advisory
- main RULES merge remains impossible from Phase 004 alone and requires the later Phase 017 promotion audit plus Phase 018 merge path
