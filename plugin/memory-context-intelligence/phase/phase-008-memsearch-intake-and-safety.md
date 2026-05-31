# Phase 008 - Memsearch intake and safety

> **Summary File:** [SUMMARY.md](SUMMARY.md)
> **Phase ID:** 008
> **Status:** Completed
> **Design References:** [../design/01-memsearch-required-dependency.design.md](../design/01-memsearch-required-dependency.design.md), [../design/00-core-concept.design.md](../design/00-core-concept.design.md)
> **Patch References:** [../patch/memory-context-intelligence-design-only-baseline.patch.md](../patch/memory-context-intelligence-design-only-baseline.patch.md); runtime package patch: `<repo-root>/plugin/memory-context-intelligence/patch/memsearch-intake-and-safety.patch.md`

---

## Objective

Implement safe memsearch intake so the runtime can consume memory summaries as work-trace input without treating memory as RULES authority.

## Why this phase exists

All later signal extraction depends on real memory traces. This phase creates the safety boundary first: scope selection, stale/unavailable handling, privacy limits, and evidence-strength labels before any recommendation is generated.

## Goal

Produce a bounded intake layer that can gather relevant memory-context records and classify their reliability.

## Output

Phase 008 implemented bounded safe intake in the runtime package under `<repo-root>/plugin/memory-context-intelligence/`.

Concrete outputs:
- `bin/memory-context-intelligence` now supports `intake` in addition to help/status/no-op
- `lib/intake.py` provides explicit memory-root availability checks, daily markdown shard discovery, bounded scoped reads, status classification, privacy minimization, and JSON report emission
- package docs now describe the phase-008 intake boundary while preserving no topic generation, no `/additional/`, no install, and no main RULES mutation
- capsule changelog and phase surfaces now mark phase 008 complete and keep phases 009+ pending

The intake record model includes source, scope, freshness/timestamp, status, evidence-strength, sample records, limits, and explicit non-generation/non-emission notes.

## Gate

Completed. The runtime can retrieve or gracefully decline memsearch input and produce a bounded intake report without generating topics.

## Owner

Runtime implementation owner for memsearch ingestion and safety checks. Main RULES owner remains outside this phase.

## Files

Implemented runtime package changes:
- `<repo-root>/plugin/memory-context-intelligence/bin/memory-context-intelligence`
- `<repo-root>/plugin/memory-context-intelligence/lib/intake.py`
- `<repo-root>/plugin/memory-context-intelligence/README.md`
- `<repo-root>/plugin/memory-context-intelligence/design/design.md`
- `<repo-root>/plugin/memory-context-intelligence/changelog/changelog.md`
- `<repo-root>/plugin/memory-context-intelligence/phase/SUMMARY.md`
- `<repo-root>/plugin/memory-context-intelligence/patch/memsearch-intake-and-safety.patch.md`
- `<repo-root>/plugin/memory-context-intelligence/skills/memory-context-intelligence/SKILL.md`
- `<repo-root>/plugin/memory-context-intelligence/agents/trace-scout.md`
- `<repo-root>/plugin/memory-context-intelligence/.claude-plugin/plugin.json`

Updated capsule governance docs:
- `phase/phase-008-memsearch-intake-and-safety.md`
- `phase/SUMMARY.md`
- `changelog/changelog.md`
- `changelog/v0.1.14-completed-memsearch-intake-and-safety.changelog.md`
- `README.md`
- `design/design.md`
- `patch/memory-context-intelligence-design-only-baseline.patch.md`
- `<repo-root>/TODO.md` compact deferred-tracking note

## Verification

Ran syntax check without writing package bytecode caches:

```bash
python3 - <<'PY'
from pathlib import Path
path = Path('<repo-root>/plugin/memory-context-intelligence/lib/intake.py')
compile(path.read_text(), str(path), 'exec')
print('syntax-ok')
PY
```

Result:

```text
syntax-ok
```

Ran help/status command:

```bash
bash "<repo-root>/plugin/memory-context-intelligence/bin/memory-context-intelligence" --help
```

Result summary:

```text
mode: bounded intake available
topic generation: not performed
/additional/ emission: not performed
main RULES mutation: not performed
configuration: late-bound; no machine-specific memsearch paths are package defaults
```

Ran available-root intake check with bounded scope:

```bash
bash "<repo-root>/plugin/memory-context-intelligence/bin/memory-context-intelligence" intake --memory-root "<workspace-root>/.memsearch/memory" --scope "memory-context-intelligence" --max-shards 2 --max-records 2 --max-chars 1200
```

Result summary:

```text
status: available
evidence_strength: observed-local-bounded
daily_shards_discovered: 49
daily_shards_considered: 2026-05-18.md, 2026-05-17.md
topic_generation_performed: false
additional_emission_performed: false
main_rules_mutation_performed: false
```

Ran unavailable-root check:

```bash
bash "<repo-root>/plugin/memory-context-intelligence/bin/memory-context-intelligence" intake --memory-root "/tmp/mci-phase008-missing-memory-root" --max-records 1
```

Result summary:

```text
status: unavailable
evidence_strength: not-found-in-checked-scope
```

Ran insufficient-scope check:

```bash
bash "<repo-root>/plugin/memory-context-intelligence/bin/memory-context-intelligence" intake --memory-root "<workspace-root>/.memsearch/memory" --scope "__mci_phase008_no_match__" --max-shards 1 --max-records 1
```

Result summary:

```text
status: insufficient
evidence_strength: insufficient-observed-local
```

Ran stale-root check:

```bash
bash "<repo-root>/plugin/memory-context-intelligence/bin/memory-context-intelligence" intake --memory-root "<template-plugin-root>/media-generator/.memsearch/memory" --max-age-days 1 --max-shards 1 --max-records 1
```

Result summary:

```text
status: stale
evidence_strength: observed-local-stale
freshness.classification: stale
```

Additional-write boundary check:

```bash
python3 - <<'PY'
from pathlib import Path
p = Path('<user-runtime-rules>/additional')
print('exists=' + str(p.exists()))
PY
```

Result:

```text
exists=False
```

## Risks / rollback notes

The main risk is over-trusting memory. Phase 008 contains that risk by labeling memory as observational input, bounding reads, minimizing sample content, and refusing to generate topics or emit candidates.

Rollback should remove only the phase-008 intake dispatch/helper and return runtime package docs to phase-007 scaffold-only wording. Preserve the governed capsule chain unless the user explicitly selects broader rollback.
