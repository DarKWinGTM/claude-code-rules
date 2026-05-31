# Phase 011 - Research enrichment engine

> **Summary File:** [SUMMARY.md](SUMMARY.md)
> **Phase ID:** 011
> **Status:** Completed
> **Design References:** [../design/03-research-enrichment.design.md](../design/03-research-enrichment.design.md), [../design/02-topic-list-and-choice-flow.design.md](../design/02-topic-list-and-choice-flow.design.md)
> **Patch References:** [../patch/memory-context-intelligence-design-only-baseline.patch.md](../patch/memory-context-intelligence-design-only-baseline.patch.md)

---

## Objective

Implement optional external research enrichment for selected topics that need broader support.

## Why this phase exists

Some memory-derived topics are local workflow observations only. Before those topics become strong candidate packets, the runtime may need external docs, source-trust comparison, or current practice checks to avoid stale or unsupported recommendations.

## Goal

Add research enrichment that strengthens selected topics without making external research a mandatory step for every topic.

## Output

- enrichment decision gate for when research is needed
- source-query plan structure
- source-trust and freshness notes
- conflict handling for external evidence
- enriched topic summary that separates local memory signals from external support

## Completed implementation

Phase 011 added controlled research enrichment to the isolated runtime package under `<repo-root>/plugin/memory-context-intelligence/`.

Implemented package outputs:
- `lib/research_enrichment.py` consumes exactly one phase-010 choose report and optional controlled/recorded source fixture
- `bin/memory-context-intelligence enrich` exposes the enrichment command surface
- no-research-needed topics return `research-skipped` with an explicit reason
- research-needed topics without a fixture return a skip decision instead of attempting live web access
- research-needed topics with fixtures return bounded enrichment output with source/query plan, source-trust notes, freshness notes, conflict handling, weak-source handling, and local-vs-external evidence separation
- weak or conflicting sources are recorded as limitations and cannot become hard constraints
- boundary flags keep live web access, native-agent orchestration, candidate packet building, `/additional/` emission, main RULES mutation, install, and publication false

## Files

Changed or created package files:
- `<repo-root>/plugin/memory-context-intelligence/lib/research_enrichment.py`
- `<repo-root>/plugin/memory-context-intelligence/tests/test_research_enrichment.py`
- `<repo-root>/plugin/memory-context-intelligence/bin/memory-context-intelligence`
- `<repo-root>/plugin/memory-context-intelligence/.claude-plugin/plugin.json`
- `<repo-root>/plugin/memory-context-intelligence/README.md`
- `<repo-root>/plugin/memory-context-intelligence/design/design.md`
- `<repo-root>/plugin/memory-context-intelligence/changelog/changelog.md`
- `<repo-root>/plugin/memory-context-intelligence/phase/SUMMARY.md`
- `<repo-root>/plugin/memory-context-intelligence/patch/research-enrichment-engine.patch.md`
- `<repo-root>/plugin/memory-context-intelligence/skills/memory-context-intelligence/SKILL.md`
- `<repo-root>/plugin/memory-context-intelligence/agents/research-scout.md`
- `<repo-root>/plugin/memory-context-intelligence/agents/source-trust-reviewer.md`

Changed capsule governance files:
- `README.md`
- `design/design.md`
- `changelog/changelog.md`
- `changelog/v0.1.17-completed-research-enrichment-engine.changelog.md`
- `phase/SUMMARY.md`
- `phase/phase-011-research-enrichment-engine.md`
- `patch/memory-context-intelligence-design-only-baseline.patch.md`
- `<repo-root>/TODO.md`

## Gate

The phase is complete because a selected topic can either skip research with a reason or produce a bounded research-enriched evidence summary from controlled source fixtures.

## Owner

Runtime implementation owner for research enrichment.

## Verification

- `PYTHONDONTWRITEBYTECODE=1 python3 - <<'PY' ... compile(...) ... PY`
  - Result: compiled 7 package Python files in memory without writing package bytecode caches: `lib/intake.py`, `lib/signals.py`, `lib/presentation.py`, `lib/research_enrichment.py`, `tests/test_signals.py`, `tests/test_presentation.py`, and `tests/test_research_enrichment.py`
- `PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s "<repo-root>/plugin/memory-context-intelligence/tests" -p "test_*.py"`
  - Result: 12 focused tests passed
- `bash "<repo-root>/plugin/memory-context-intelligence/bin/memory-context-intelligence" --help`
  - Result: help/status listed `enrich` and stated live web access, native-agent orchestration, candidate packet building, `/additional/` emission, main RULES mutation, install, and publication are not performed
- Controlled `enrich` CLI sample using temporary JSON files under `/tmp`
  - Result: `status=research-enriched`, `gate=research-needed`, `strong_sources=official-docs`, `weak_sources=weak-blog`, `hard_constraint_sources=official-docs`, and live-web/native-agent/candidate-packet/additional/main-rules flags all false
- Additional boundary check around the controlled CLI sample
  - Result: package-local `additional` and `<user-runtime-rules>/additional` existence stayed unchanged before and after enrichment: `additional_paths_unchanged=True`

## Risks / rollback notes

The main risk is turning research into broad raw source absorption or overclaiming from weak sources. Phase 011 contains that risk by using only controlled/recorded fixtures, separating local memory signal from external support, and preventing weak/conflicting sources from becoming hard constraints.

Rollback can remove the `enrich` dispatch path, `lib/research_enrichment.py`, `tests/test_research_enrichment.py`, and phase-011 package docs from the isolated runtime package. Do not treat that rollback as authorization to remove the capsule governance chain, `/additional/` staging direction, or main RULES boundaries.
