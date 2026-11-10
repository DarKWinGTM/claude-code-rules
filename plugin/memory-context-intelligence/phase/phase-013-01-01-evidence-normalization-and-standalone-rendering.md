# Phase 013-01-01 — Evidence Normalization and Standalone Rendering

> **Parent Phase:** [phase-013-01-deterministic-standalone-additional-stage-emission.md](phase-013-01-deterministic-standalone-additional-stage-emission.md)
> **Summary File:** [SUMMARY.md](SUMMARY.md)
> **Current Version:** 0.1.78
> **Status:** Completed / verified in focused source scope
> **Target Design:** [../design/design.md](../design/design.md) v0.1.78
> **Patch Reference:** [../patch/deterministic-standalone-additional-stage-emission.patch.md](../patch/deterministic-standalone-additional-stage-emission.patch.md)
> **Session:** 48a3ef9b-50cf-4574-8f00-4f6b6e28f76e (2026-08-09)

---

## Objective

Implements the evidence-linkage, entailment, normalized evidence, and rich standalone renderer slices. Runtime/source edits remain main-session-owned.

## Inherited boundaries

- Initial analysis remains read-only and advisory.
- One selected topic maps to one artifact.
- Existing additional-stage files are preserved; no overwrite path is active.
- Main RULES and Phases 017-018 remain unchanged.
- Completion wording is limited to direct verification evidence.

---

### Task 1: Repair date-sensitive test fixtures and establish a green baseline

**Files:**
- Modify: `tests/test_live_trial.py:6-33`
- Modify: `tests/test_historical_replay.py:6-34`
- Modify: `tests/test_readiness.py:6-33`

**Interfaces:**
- Consumes: existing `write_memory_shard(memory_root: Path, ...)` helpers.
- Produces: fresh daily-shard fixtures that remain inside the runtime default `max_age_days=30` gate.

- [x] **Step 1: Replace hard-coded shard days with the current test day**

Add the standard-library import and compute the filename inside each helper:

```python
from datetime import date


def write_memory_shard(memory_root: Path, *, content: str | None = None) -> None:
    memory_root.mkdir(parents=True, exist_ok=True)
    shard_day = date.today().isoformat()
    (memory_root / f"{shard_day}.md").write_text(
        content or "...",
        encoding="utf-8",
    )
```

For helpers without the optional `content` argument, preserve their existing body and change only the date import, `shard_day`, and destination filename. Keep controlled source-fixture dates as historical fixture metadata unless a test directly uses them for freshness.

- [x] **Step 2: Run the focused pre-feature baseline**

Run:

```bash
cd /home/node/workplace/AWCLOUD/TEMPLATE/RULES/plugin/memory-context-intelligence
python3 -m pytest -q \
  tests/test_candidate_packet.py \
  tests/test_live_trial.py \
  tests/test_historical_replay.py \
  tests/test_readiness.py \
  tests/test_analysis_skill_contract.py
```

Expected: all 32 focused tests pass. If another failure remains, stop and classify it before adding v0.1.78 RED tests; do not call it a feature regression without matching evidence.

- [x] **Step 3: Record the baseline in the phase verification section**

Record the exact command, count, and result. Maximum claim: `baseline tested in focused scope`.

---

### Task 2: Attach a deterministic entailment basis to signals and selected trace anchors

**Files:**
- Modify: `lib/signals.py:539-566,821-854`
- Modify: `lib/orchestration.py:145-166,464-479`
- Modify: `tests/test_signals.py`
- Modify: `tests/test_orchestration.py`

**Interfaces:**
- Produces on every promoted topic:

```python
"candidate_entailment_basis": {
    "candidate_title": str,
    "source_signal_ids": list[str],
    "trace_record_count": int,
    "source_keywords": list[str],
    "transferable_observed_pattern": str,
    "supported_mechanism": str,
}
```

- Changes signature to:

```python
def signal_anchors(
    signals_report: dict[str, Any] | None,
    signal_ids: set[str] | None = None,
    limit: int = 12,
) -> list[dict[str, Any]]:
```

- Each selected trace anchor additionally carries `session_id` and `source_classes`.

- [x] **Step 1: Add the failing signal test**

Add `test_promoted_topic_carries_entailment_basis_linked_to_source_signal`:

```python
topic = report["topic_candidates"][0]
basis = topic["candidate_entailment_basis"]
self.assertEqual(basis["candidate_title"], topic["title"])
self.assertEqual(basis["source_signal_ids"], topic["source_signal_ids"])
self.assertEqual(basis["trace_record_count"], report["ranked_signals"][0]["trace_record_count"])
self.assertTrue(basis["source_keywords"])
self.assertTrue(basis["transferable_observed_pattern"])
self.assertEqual(basis["supported_mechanism"], topic["high_level_mechanism"])
```

- [x] **Step 2: Add the failing orchestration test**

Add `test_candidate_input_trace_anchors_are_filtered_to_selected_topic`. Build a signal report with `signal-001` and `signal-002`, select Topic 1, then assert:

```python
anchors = report["phase_013_candidate_input"]["trace_anchors"]
self.assertTrue(anchors)
self.assertEqual({item["signal_id"] for item in anchors}, {"signal-001"})
self.assertTrue(all("session_id" in item for item in anchors))
self.assertTrue(all("source_classes" in item for item in anchors))
```

- [x] **Step 3: Confirm RED**

Run:

```bash
python3 -m pytest -q \
  tests/test_signals.py::SignalGenerationTests::test_promoted_topic_carries_entailment_basis_linked_to_source_signal \
  tests/test_orchestration.py::OrchestrationTests::test_candidate_input_trace_anchors_are_filtered_to_selected_topic
```

Expected: FAIL because the basis and filtered anchor metadata do not exist.

- [x] **Step 4: Implement the smallest semantic linkage**

Inside `topic_from_signal`, construct the basis from the already-checked signal and topic semantics. Use the existing topic title, `source_signal_ids`, `trace_record_count`, keywords, `why_surfaced`, and `high_level_mechanism`; do not infer doctrine from raw names alone.

Update `signal_anchors` to skip signals outside `signal_ids` when a filter is supplied and to include:

```python
{
    "signal_id": signal.get("id"),
    "signal_rank": signal.get("rank"),
    "shard": record.get("shard"),
    "section": record.get("section"),
    "session_id": record.get("session_id"),
    "source_classes": signal.get("source_classes", []),
    "content_preview": record.get("content_preview"),
}
```

The trace lane must call `signal_anchors(..., signal_ids=set(selected_topic["source_signal_ids"]))` when a selected topic exists.

- [x] **Step 5: Run focused GREEN checks**

```bash
python3 -m pytest -q tests/test_signals.py tests/test_orchestration.py
```

Expected: both files pass.

---

### Task 3: Separate trial selection from Main RULES promotion and normalize candidate evidence

**Files:**
- Modify: `lib/candidate_packet.py:253-387`
- Modify: `tests/test_candidate_packet.py`

**Interfaces:**

Change the packet builder signature to:

```python
def build_candidate_packet(
    candidate_input: dict[str, Any],
    *,
    owner_domain: str | None = None,
    main_rule_target: str | None = None,
    integration_anchors: list[str] | None = None,
    additional_name: str | None = None,
    additional_relative_path: str | None = None,
    selected_for_additional_trial: bool = False,
) -> dict[str, Any]:
```

Add:

```python
def evaluate_candidate_entailment(
    topic: dict[str, Any],
    trace_anchors: list[dict[str, Any]],
) -> dict[str, Any]:
    ...


def normalize_evidence_basis(
    topic: dict[str, Any],
    selected_trace_anchors: list[dict[str, Any]],
    source_anchors: list[dict[str, Any]],
    conflicts_uncertainty: list[str],
    entailment: dict[str, Any],
) -> dict[str, Any]:
    ...


def build_trial_rule_draft(
    topic: dict[str, Any],
    entailment: dict[str, Any],
) -> dict[str, Any]:
    ...
```

`evaluate_candidate_entailment` returns:

```python
{
    "decision": "retain" | "narrow" | "context-only" | "reject",
    "selected_signal_ids": list[str],
    "support_reason": str,
    "transferable_observed_pattern": str,
    "supported_mechanism": str,
    "eligible_for_additional_trial": bool,
}
```

The packet/report explicitly carries:

```python
"selected_for_additional_trial": bool,
"main_rules_promotion_approved": False,
```

Raw `trace_anchors` and `source_anchors` remain inside internal `signal_evidence_basis` for audit. The renderer must consume only `normalized_evidence_basis`.

- [x] **Step 1: Add selection-state and entailment RED tests**

Add:
- `test_packet_records_additional_trial_selection_without_main_rules_promotion`
- `test_packet_rejects_context_only_or_unrelated_entailment`
- `test_packet_narrows_partially_supported_mechanism_before_render`

Core assertions:

```python
report = candidate_packet.build_candidate_packet(
    candidate_input,
    owner_domain="evidence-discipline",
    main_rule_target="rules/evidence-discipline.md",
    selected_for_additional_trial=True,
)
self.assertTrue(report["selected_for_additional_trial"])
self.assertFalse(report["main_rules_promotion_approved"])
self.assertTrue(report["candidate_packet"]["selected_for_additional_trial"])
self.assertFalse(report["candidate_packet"]["main_rules_promotion_approved"])
```

For context-only/reject input, assert the packet has a stop gate and cannot be approved for additional write. For partial support, assert `decision == "narrow"` and the rendered mechanism equals the evidence-supported narrowed mechanism rather than the original broader title.

- [x] **Step 2: Confirm RED**

```bash
python3 -m pytest -q tests/test_candidate_packet.py -k 'selection_without_main_rules or context_only or narrows_partially'
```

Expected: FAIL on missing fields/functions.

- [x] **Step 3: Implement entailment decisions without keyword theater**

Use `candidate_entailment_basis.source_signal_ids` and selected anchor `signal_id` values as the hard linkage. Apply this deterministic policy:

```text
no selected signal ids or no matching trace anchors → context-only
basis mechanism missing or semantically empty → reject
all selected signal ids have matching trace support → retain
some selected signal ids match and a narrower supported mechanism exists → narrow
```

`eligible_for_additional_trial` is true only for `retain` and `narrow` with matching trace support. Durable/governance/source anchors may add context but cannot make `context-only` or `reject` eligible.

- [x] **Step 4: Build normalized evidence**

The normalized evidence object must contain:

```python
{
    "source_classes": list[str],
    "current_session_confirmation": str,
    "trace_record_count": int,
    "session_count": int,
    "shard_count": int,
    "confidence": str,
    "evidence_label": str,
    "transferable_observed_pattern": str,
    "mechanism_support": str,
    "conflicts_uncertainty": list[str],
    "limits": list[str],
    "excluded_scope": list[str],
}
```

Counts come from bounded selected anchors, not prose parsing. Do not copy raw shard names, session identifiers, `content_preview`, URLs, or absolute paths into this emitted model.

- [x] **Step 5: Run packet tests**

```bash
python3 -m pytest -q tests/test_candidate_packet.py
```

Expected: all packet tests added so far pass except later renderer/batch RED tests not yet introduced.

---

### Task 4: Replace the thin renderer with the rich standalone artifact contract

**Files:**
- Modify: `lib/candidate_packet.py:390-474`
- Modify: `tests/test_candidate_packet.py`

**Interfaces:**

Add:

```python
def validate_standalone_artifact(material: str) -> dict[str, Any]:
    ...
```

Required headings:

```python
REQUIRED_STANDALONE_HEADINGS = (
    "## Candidate summary",
    "## Trial rule draft",
    "### Core principle",
    "### Draft operating clauses",
    "### Before behavior",
    "### After behavior",
    "## Signal and evidence basis",
    "## Owner-domain mapping",
    "## Trial-first rationale",
    "## Risks",
    "## Success criteria",
    "## Rollback notes",
    "## Stop gates",
    "## Leader verification needs",
    "## Promotion boundary",
)
```

Validator output:

```python
{
    "valid": bool,
    "missing_headings": list[str],
    "forbidden_dependencies": list[str],
}
```

- [x] **Step 1: Add renderer RED tests**

Add:
- `test_rendered_artifact_has_complete_standalone_schema`
- `test_rendered_artifact_excludes_ephemeral_evidence_dependencies`

Build a packet whose internal raw anchors contain `.memsearch/memory/2026-08-09.md`, `/tmp/packet.json`, a transcript `.jsonl`, `/home/node/...`, `file.md:390`, and `content_preview`. Assert these remain available in internal packet audit state but are absent from `preview_material`.

```python
validation = candidate_packet.validate_standalone_artifact(material)
self.assertTrue(validation["valid"])
self.assertEqual(validation["missing_headings"], [])
self.assertEqual(validation["forbidden_dependencies"], [])
self.assertIn("Main RULES mutation:** Not performed", material)
```

- [x] **Step 2: Confirm RED**

```bash
python3 -m pytest -q tests/test_candidate_packet.py -k 'complete_standalone_schema or excludes_ephemeral'
```

Expected: FAIL because the thin renderer lacks required sections and validator.

- [x] **Step 3: Implement rich rendering**

Render one independently understandable artifact with:
- one selected topic source
- intended owner plus integration anchors
- `Main RULES mutation: Not performed`
- candidate summary
- trial rule draft with core principle, concrete operating clauses, before behavior, and after behavior
- normalized evidence basis with breadth/confidence/conflicts/limits
- owner reasoning
- trial-first rationale
- risks, success criteria, rollback notes, stop gates, leader verification needs, and promotion boundary

Do not render `signal_evidence_basis.trace_anchors`, `source_anchors`, or raw previews.

- [x] **Step 4: Implement forbidden-dependency validation**

Reject material matching these semantic classes:
- `.memsearch` and memory-shard paths
- transcript or `.jsonl` paths
- `/tmp/`, temp packet/report paths
- absolute analysis-only workstation paths such as `/home/...`
- raw path-line forms such as `name.md:390`
- literal `content_preview` reconstruction dependencies

Exact session metadata in governed trial headers is allowed only when it is provenance and the file remains understandable without it.

- [x] **Step 5: Run renderer GREEN tests**

```bash
python3 -m pytest -q tests/test_candidate_packet.py
```

Expected: all current packet/renderer tests pass.

---

## Execution result

Completed in the main session with source ownership retained locally.

Verification evidence:
- date-sensitive helper fixtures were made deterministic without changing production freshness behavior
- signal/topic entailment linkage and selected-anchor filtering passed focused tests
- packet state separation, retain/narrow/context-only/reject decisions, and normalized evidence passed focused tests
- rich standalone schema and forbidden transient-dependency validation passed focused tests
- all later integrated plugin checks remained green, including the final `132 passed` full suite

Covers: source-level entailment, evidence normalization, selection/promotion state, and standalone rendering.

Does not cover: remote release, installed marketplace runtime, or stability over time.

---
