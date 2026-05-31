# Phase 069 - adaptive deep-analysis required bounded deepening

## Summary File

[SUMMARY.md](SUMMARY.md)

## Phase ID

069

## Status

Completed

## Design References

- [../design/design.md](../design/design.md)
- [../design/02-topic-list-and-choice-flow.design.md](../design/02-topic-list-and-choice-flow.design.md)
- [../design/04-native-agent-orchestration.design.md](../design/04-native-agent-orchestration.design.md)
- [../design/08-memory-evidence-source-model.design.md](../design/08-memory-evidence-source-model.design.md)

## Patch References

- [../patch/analysis-adaptive-deep-analysis-required-bounded-deepening.patch.md](../patch/analysis-adaptive-deep-analysis-required-bounded-deepening.patch.md)

## Objective

Strengthen `/memory-context-intelligence:analysis` so adaptive deep-analysis does not stop at advisory metadata only: when the rendered payload marks bounded deepening as required, the analysis skill must actually perform one bounded deepening pass for the required top topic candidates before the first response, while preserving `trace_evidence` as the live promotion anchor and keeping the repeated topic-card output shape.

## Why this phase exists

The earlier adaptive deep-analysis implementation surfaced a plan in the runtime payload, but the checked local non-interactive slash proof still skipped real deepening even when Topic 1 was marked `subagent+external-research`. That meant the capability existed as a recommendation layer, not yet as an enforced first-response behavior. This phase closes that gap with the smallest bounded fix: add an explicit execution contract to the adaptive payload, strengthen the analysis-skill contract so required deepening cannot be skipped silently, and re-prove the live slash surface with actual read-only deepening.

## Gate

Phase 069 closes only when all of the following are true in checked scope:
- `lib/orchestration.py` returns an explicit adaptive execution contract that names whether deepening is required, which topic ids require it, and that skipped deepening must be reported when the required tool is unavailable
- `skills/analysis/SKILL.md` requires the first response to perform bounded deepening for required topic ids instead of only allowing it optionally
- the strengthened contract still preserves `trace_evidence` as the live promotion anchor and keeps subagent/web research as supporting layers only
- focused adaptive tests pass for orchestration payload, analysis-surface payload, and analysis-skill contract
- the full plugin suite passes after the contract change
- one direct packaged `analysis-surface` proof shows `must_deepen_before_first_response`, `required_topic_ids`, and the explicit execution contract in the rendered payload
- one approved non-interactive local slash proof shows actual bounded deepening behavior in the first response when a required topic exists
- structured local proof evidence shows the slash response really invoked read-only deepening support instead of only rephrasing the payload

## Verification / closeout

Phase 069 is completed in checked scope.

This closeout now holds:
- adaptive deep-analysis now emits a stronger execution contract through `must_deepen_before_first_response`, `required_topic_ids`, `tool_unavailability_requires_note`, and `execution_contract`
- the analysis skill now requires bounded deepening for the required top candidates instead of silently treating deepening as optional metadata
- focused adaptive verification passed across:
  - `test_orchestration.py`
  - `test_analysis_surface.py`
  - `test_analysis_skill_contract.py`
- the full plugin suite passed with `102` tests
- direct packaged proof from a temporary workspace with a symlinked `.memsearch/memory` root showed `adaptive_deep_analysis.deepening_required = true`, `must_deepen_before_first_response = true`, and `required_topic_ids = ["topic-001"]`
- approved non-interactive local slash proof from that same bounded temp workspace produced a first response that explicitly stated bounded adaptive deepening was performed for Topic 1, preserved topic-card output, kept the result advisory-only, and listed supporting external sources
- structured slash proof showed actual tool use during the bounded deepening step, including:
  - `Agent` with subagent type `memory-context-intelligence:synthesis-lead`
  - `WebSearch` for workflow failure / stop-gate / recovery-path support

## Verification limits

This phase does not claim that every larger parent workspace can always run the same non-interactive proof path unchanged. In checked scope, a root-CLAUDE print-mode attempt still overflowed prompt budget with `Prompt is too long`; the successful deepening proof therefore used a bounded temporary workspace plus the real historical memory root so the public slash surface could be verified without that unrelated context-load blocker.

## Boundaries preserved after closeout

Phase 069 still does not claim:
- direct promotion from `recall_evidence`, `durable_memory_context`, or `governance_context` without `trace_evidence`
- topic selection approval, candidate-packet build, or `/additional/` emission from the first response
- plugin-managed auto-flow proof
- publication or external marketplace release
- stable behavior or broad production readiness
- main RULES promotion
- main RULES mutation
- main RULES merge
