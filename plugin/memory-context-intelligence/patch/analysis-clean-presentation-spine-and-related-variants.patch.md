# Clean presentation spine and related variants patch

> **Current Version:** 0.1.64
> **Session:** d42465eb-30a7-4bc8-b9d6-03e52306e9a5 (2026-05-30)
> **Status:** Phase 060 completed clean presentation spine and related variants in checked scope
> **Target Design:** [../design/design.md](../design/design.md) v0.1.64
> **Full history:** [../changelog/changelog.md](../changelog/changelog.md)

---

## 1) Context

Phase 059 already made proposal bodies richer with concrete examples and before/after behavior, but the first response could still read as cluttered because weaker same-family topics repeated in the main list and the real slash output had no explicit `Related variants` section.

## 2) Analysis

The correct repair is a presentation-spine cleanup, not another evidence-model rewrite.

The patch therefore keeps:
- historical-first scope
- doctrine-level titles
- trace-anchored promotion
- bounded preview-derived `Evidence examples` / `Before behavior` / `After behavior`

And changes:
- the main first-response list now keeps only primary topic families
- one strongest primary topic still drives `recommendation` and the expanded `proposal`
- weaker same-family follow-ups move into `related variants`
- the structured output now exposes explicit section order, section roles, and a no-repeated-recap policy for the first-response spine
- the checked analysis context now forwards `related_variants`, `first_response_spine`, and `first_response_contract`

## 3) Change items

### 3.1 Main list compression for same-family topics
- **Target artifact:** `../lib/presentation.py`, `../tests/test_presentation.py`
- **Change type:** replacement
- **Before:** weaker same-family topics still stayed inside the main `topic_list` / `presentation.topic_list` even after a stronger primary topic from the same family was already surfaced
- **After:** the main first-response list now keeps only primary topic families while weaker same-family candidates are compressed out of the main list

### 3.2 Runtime payload exposure for clean spine fields
- **Target artifact:** `../lib/analysis_surface.py`, `../tests/test_analysis_surface.py`
- **Change type:** additive
- **Before:** the checked analysis context forwarded `presentation`, `recommendation`, `proposal`, and `topic_list`, but not `related_variants` or `first_response_spine`
- **After:** the checked analysis context now forwards `related_variants` plus `first_response_spine`, so the real slash surface can see the full intended spine

### 3.3 Public contract and governed sync
- **Target artifact:** `../skills/analysis/SKILL.md`, `../tests/test_analysis_skill_contract.py`, `../README.md`, `../design/design.md`, `../design/02-topic-list-and-choice-flow.design.md`, `../phase/SUMMARY.md`, `../phase/phase-060-clean-presentation-spine-and-related-variants.md`, `../changelog/changelog.md`, `../changelog/v0.1.64-completed-clean-presentation-spine-and-related-variants.changelog.md`, `/home/node/workplace/AWCLOUD/TEMPLATE/RULES/TODO.md`, and `../.claude-plugin/plugin.json`
- **Change type:** replacement/additive
- **Before:** active docs still stopped at `presentation / recommendation / proposal` and did not fully state the primary-family-only list plus explicit `related variants` contract
- **After:** active docs now state the four-part spine, forbid repeating same-family weaker topics in the main list, and keep the richer proposal-body contract intact

## 4) Verification

- focused RED/GREEN proof for same-family compression in `presentation.topic_list`
- focused RED/GREEN proof for the explicit structured section-order / section-role / no-repeated-recap contract
- focused RED/GREEN proof for `analysis_surface.py` forwarding `related_variants`, `first_response_spine`, and `first_response_contract`
- focused skill-contract proof for the four-part spine wording plus one-section-per-role / no-repeated-recap wording
- full runtime/source suite green
- one real local `/memory-context-intelligence:analysis` run via `--plugin-dir` showing a primary-family-only main list plus an explicit `Related variants` section

## 5) Rollback approach

If this refinement is rolled back, restore the old repeated same-family main-list behavior and remove explicit `related variants` exposure while preserving historical-first scope, doctrine-level titles, conditional evidence-example sections, and `/additional/` boundaries unless a broader rollback is explicitly selected.
