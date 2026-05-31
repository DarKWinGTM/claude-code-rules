# Evidence-grounded proposal examples and before/after patch

> **Current Version:** 0.1.63
> **Session:** d42465eb-30a7-4bc8-b9d6-03e52306e9a5 (2026-05-30)
> **Status:** Phase 059 completed evidence-grounded proposal examples and before/after behavior in checked scope
> **Target Design:** [../design/design.md](../design/design.md) v0.1.63
> **Full history:** [../changelog/changelog.md](../changelog/changelog.md)

---

## 1) Context

Phase 058 already corrected topic-title abstraction, but proposal bodies still relied too much on generic explanation. The user explicitly wanted examples drawn from found data and clearer before/after behavior.

## 2) Analysis

The correct extension is a bounded evidence-example layer, not a rewrite of the output model.

The patch therefore keeps:
- historical-first scope
- doctrine-level titles
- proposal-first `presentation / recommendation / proposal`
- trace-anchored promotion

And adds:
- concrete `Evidence examples` sourced from bounded found previews
- explicit `Before behavior`
- explicit `After behavior`
- omission of those sections when usable preview evidence is absent

## 3) Change items

### 3.1 Signal payload enrichment
- **Target artifact:** `../lib/signals.py`, `../tests/test_signals.py`
- **Change type:** replacement
- **Before:** topic candidates exposed `example_bad`, `example_good`, and `evidence_summary`, but they did not expose explicit `evidence_examples`, `before_behavior`, or `after_behavior`
- **After:** topic candidates now expose those new fields from bounded preview-derived evidence when a usable doctrine/example path exists

### 3.2 Proposal rendering refinement
- **Target artifact:** `../lib/presentation.py`, `../tests/test_presentation.py`
- **Change type:** replacement
- **Before:** proposal rendering fell back to generic example sections by default
- **After:** proposal rendering shows `Evidence examples`, `Before behavior`, and `After behavior` only when usable evidence exists and omits fabricated generic case examples when it does not

### 3.3 Contract and governed sync
- **Target artifact:** `../skills/analysis/SKILL.md`, `../tests/test_analysis_skill_contract.py`, `../README.md`, `../design/design.md`, `../design/02-topic-list-and-choice-flow.design.md`, `../phase/SUMMARY.md`, `../phase/phase-059-evidence-grounded-proposal-examples-and-before-after.md`, `../changelog/changelog.md`, `../changelog/v0.1.63-completed-evidence-grounded-proposal-examples-and-before-after.changelog.md`, `/home/node/workplace/AWCLOUD/TEMPLATE/RULES/TODO.md`, and `../.claude-plugin/plugin.json`
- **Change type:** replacement/additive
- **Before:** active docs stopped at doctrine-level titles and did not fully state the new evidence-example / before-after proposal contract
- **After:** active docs now state when those sections appear, how they are sourced, and that fabricated generic examples must not appear when preview evidence is absent

## 4) Verification

- focused RED/GREEN proof for signal-level evidence-example and before/after fields
- focused RED/GREEN proof for proposal rendering of `Evidence examples`, `Before behavior`, and `After behavior`
- focused RED/GREEN proof for omission behavior when usable preview evidence is absent
- focused skill-contract proof for the public contract wording
- full runtime/source suite green
- one real local `/memory-context-intelligence:analysis` run after local plugin update showing doctrine-level topics with concrete bounded examples plus before/after behavior where usable evidence exists

## 5) Rollback approach

If this refinement is rolled back, remove the richer proposal-body example sections while preserving historical-first scope, doctrine-level titles, trace-anchored promotion, and `/additional/` boundaries unless a broader rollback is explicitly selected.
