# Adaptive deep-analysis required bounded deepening patch

> **Current Version:** 0.1.73
> **Session:** d42465eb-30a7-4bc8-b9d6-03e52306e9a5 (2026-06-01)
> **Status:** Phase 069 completed adaptive deep-analysis required bounded deepening in checked scope
> **Target Design:** [../design/design.md](../design/design.md) v0.1.73
> **Full history:** [../changelog/changelog.md](../changelog/changelog.md)

---

## 1) Context

`memory-context-intelligence` already exposed an adaptive deep-analysis plan in its runtime payload, but the checked local non-interactive slash proof still skipped actual deepening even when Topic 1 was flagged `subagent+external-research`. The missing gap was not broad architecture; it was contract enforcement.

## 2) Analysis

The smallest useful fix is to strengthen the adaptive payload and the analysis-skill contract together. The payload must say that deepening is required, name which topics require it, and require visible reporting when the needed tool is unavailable. The skill must then follow that stronger contract before the first response while keeping the same topic-card output shape and preserving `trace_evidence` as the live promotion anchor.

## 3) Change items

### 3.1 Strengthen adaptive execution metadata
- **Target artifact:** `../lib/orchestration.py`
- **Change type:** replacement
- **Before:** adaptive payload exposed `deepening_required` and candidate recommendations, but did not make the execution step mandatory
- **After:** adaptive payload explicitly exposes `must_deepen_before_first_response`, `required_topic_ids`, `tool_unavailability_requires_note`, and `execution_contract`

### 3.2 Strengthen slash-surface behavior contract
- **Target artifact:** `../skills/analysis/SKILL.md`
- **Change type:** replacement
- **Before:** the skill said it *may* deepen the top candidates
- **After:** the skill says it *must* deepen required candidates before the first response, must report tool unavailability explicitly, and must not silently skip required adaptive deepening

### 3.3 Lock the stronger contract with focused tests
- **Target artifact:** `../tests/test_orchestration.py`, `../tests/test_analysis_surface.py`, `../tests/test_analysis_skill_contract.py`
- **Change type:** replacement
- **Before:** focused tests proved adaptive metadata existed, but not that the contract enforced required deepening
- **After:** focused tests assert the stronger execution contract fields and required-skill wording

## 4) Verification

- run focused adaptive tests:
  - `python3 -m unittest discover -s tests -p 'test_orchestration.py' -v`
  - `python3 -m unittest discover -s tests -p 'test_analysis_surface.py' -v`
  - `python3 -m unittest discover -s tests -p 'test_analysis_skill_contract.py' -v`
- run the full plugin suite:
  - `python3 -m unittest discover -s tests -p 'test_*.py' -v`
- run a direct packaged `analysis-surface` proof from a bounded temp workspace with a symlinked `.memsearch/memory` root and confirm the adaptive payload now requires bounded deepening
- run an approved non-interactive local slash proof from that same bounded temp workspace and confirm the first response says bounded adaptive deepening was actually performed
- inspect the structured slash proof and confirm actual tool use includes `Agent` and `WebSearch`

## 5) Rollback approach

If this wave is rolled back, revert only the stronger adaptive contract and its focused tests. Do not use rollback as authority to weaken `trace_evidence`, change topic-card shape, reopen `/additional/`, or claim broader runtime/publication/readiness behavior.
