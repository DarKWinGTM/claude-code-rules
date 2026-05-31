# Phase 009 - Signal extraction and topic generation

> **Summary File:** [SUMMARY.md](SUMMARY.md)
> **Phase ID:** 009
> **Status:** Completed
> **Design References:** [../design/00-core-concept.design.md](../design/00-core-concept.design.md), [../design/02-topic-list-and-choice-flow.design.md](../design/02-topic-list-and-choice-flow.design.md)
> **Patch References:** [../patch/memory-context-intelligence-design-only-baseline.patch.md](../patch/memory-context-intelligence-design-only-baseline.patch.md); runtime package patch: `<repo-root>/plugin/memory-context-intelligence/patch/signal-extraction-and-topic-generation.patch.md`

---

## Objective

Convert safe memsearch intake records into ranked improvement signals and topic candidates.

## Why this phase exists

The runtime must not jump from raw memory traces to rule proposals. It first needs a signal layer that identifies recurring workflow problems, repeated corrections, evidence gaps, and potential doctrine improvements while preserving uncertainty.

## Goal

Generate internal topic candidates that are useful enough for later user review but still clearly advisory and non-emitting.

## Output

Phase 009 implemented internal signal extraction and topic generation in the runtime package under `<repo-root>/plugin/memory-context-intelligence/`.

Concrete outputs:
- `bin/memory-context-intelligence` now supports `signals` in addition to help/status/no-op and `intake`
- `lib/signals.py` consumes bounded intake JSON and emits an internal-only report
- the internal report includes ranked signals, deduped signal groups for recurring patterns/corrections/blockers/evidence gaps, topic candidates, confidence labels, and evidence labels
- `tests/test_signals.py` covers controlled sample output, duplicate/near-duplicate merging, stale/insufficient input handling, and no-emission flags
- package-local README, design, changelog, phase, patch, skill, trace-scout, and plugin metadata now describe the phase-009 internal-analysis state
- capsule changelog and phase surfaces now mark phase 009 complete and keep phases 010+ pending

The topic candidate model includes purpose, why surfaced, expected behavior impact, high-level mechanism, expected output, confidence, evidence label, and source signal IDs.

## Gate

Completed. Scoped memory input can produce a ranked internal signal/topic report without user-facing choose flow, external research, candidate packet emission, `/additional/` writes, install/publication, or main RULES mutation.

## Owner

Runtime implementation owner for analysis and topic generation. Main RULES owner remains outside this phase.

## Files

Implemented runtime package changes:
- `<repo-root>/plugin/memory-context-intelligence/bin/memory-context-intelligence`
- `<repo-root>/plugin/memory-context-intelligence/lib/signals.py`
- `<repo-root>/plugin/memory-context-intelligence/tests/test_signals.py`
- `<repo-root>/plugin/memory-context-intelligence/README.md`
- `<repo-root>/plugin/memory-context-intelligence/design/design.md`
- `<repo-root>/plugin/memory-context-intelligence/changelog/changelog.md`
- `<repo-root>/plugin/memory-context-intelligence/phase/SUMMARY.md`
- `<repo-root>/plugin/memory-context-intelligence/patch/signal-extraction-and-topic-generation.patch.md`
- `<repo-root>/plugin/memory-context-intelligence/skills/memory-context-intelligence/SKILL.md`
- `<repo-root>/plugin/memory-context-intelligence/agents/trace-scout.md`
- `<repo-root>/plugin/memory-context-intelligence/.claude-plugin/plugin.json`

Updated capsule governance docs:
- `phase/phase-009-signal-extraction-and-topic-generation.md`
- `phase/SUMMARY.md`
- `changelog/changelog.md`
- `changelog/v0.1.15-completed-signal-extraction-and-topic-generation.changelog.md`
- `README.md`
- `design/design.md`
- `patch/memory-context-intelligence-design-only-baseline.patch.md`
- `<repo-root>/TODO.md` compact deferred-tracking note

## Verification

Ran syntax check without writing package bytecode caches:

```bash
python3 - <<'PY'
from pathlib import Path
for path in [Path('<repo-root>/plugin/memory-context-intelligence/lib/intake.py'), Path('<repo-root>/plugin/memory-context-intelligence/lib/signals.py'), Path('<repo-root>/plugin/memory-context-intelligence/tests/test_signals.py')]:
    compile(path.read_text(), str(path), 'exec')
print('syntax-ok')
PY
```

Result:

```text
syntax-ok
```

Ran focused signal-generation tests:

```bash
python3 -m unittest discover -s "<repo-root>/plugin/memory-context-intelligence/tests" -p "test_*.py"
```

Result summary:

```text
Ran 4 tests in 0.002s
OK
```

The focused tests cover:
- controlled sample memory input producing internal signals/topics
- duplicate and near-duplicate merge behavior
- stale input staying low-confidence and producing no promoted topics
- insufficient input producing no promoted topics
- no-emission flags in the internal report

Ran help/status command:

```bash
bash "<repo-root>/plugin/memory-context-intelligence/bin/memory-context-intelligence" --help
```

Result summary:

```text
mode: bounded intake and internal signal analysis available
internal analysis command: signals
topic generation: internal-only report; no choose flow
external research: not performed
/additional/ emission: not performed
main RULES mutation: not performed
runtime install/publication: not performed
```

Ran controlled intake-to-signals integration sample:

```bash
tmp_root="$(mktemp -d /tmp/mci-phase009-memory.XXXXXX)" && python3 - "$tmp_root" <<'PY' && bash "<repo-root>/plugin/memory-context-intelligence/bin/memory-context-intelligence" intake --memory-root "$tmp_root" --scope "verification" --max-shards 1 --max-records 5 --max-chars 2000 | bash "<repo-root>/plugin/memory-context-intelligence/bin/memory-context-intelligence" signals --max-topics 5 > "$tmp_root/signals.json" && python3 - "$tmp_root/signals.json" <<'PY' && rm -rf "$tmp_root"
from pathlib import Path
import sys
root = Path(sys.argv[1])
(root / '2026-05-18.md').write_text('''# Sample memory\n\n### feedback\n- Do not claim fixed before verification; report evidence limits clearly.\n- Avoid claiming fixed before verification; keep evidence limits visible.\n- Do not claim fixed before verification; report evidence limits clearly.\n''')
PY
import json
import sys
from pathlib import Path
report = json.loads(Path(sys.argv[1]).read_text())
assert report['internal_only'] is True
assert report['topic_candidates'], report
assert report['additional_emission_performed'] is False
assert report['main_rules_mutation_performed'] is False
print('signals-status=' + report['status'])
print('signals=' + str(len(report['ranked_signals'])))
print('topics=' + str(len(report['topic_candidates'])))
print('top-confidence=' + report['ranked_signals'][0]['confidence'])
PY
```

Result:

```text
signals-status=available
signals=1
topics=1
top-confidence=medium
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

The main risk is over-promoting plausible memory patterns. Phase 009 contains that risk by ranking only bounded intake evidence, clustering repeated signals, capping stale/insufficient/single-observation inputs as low-confidence, and refusing to run choose flow or emit candidates.

Rollback should remove only the phase-009 signals dispatch/helper/tests and return runtime package docs to the phase-008 bounded-intake state. Preserve the governed capsule chain unless the user explicitly selects broader rollback.
