# Recall Scoping and Time-Window Contract

## 0) Document Control

> **Parent Scope:** memory-context-intelligence plugin-local governed design chain
> **Current Version:** 0.1.57
> **Session:** d42465eb-30a7-4bc8-b9d6-03e52306e9a5 (2026-05-27)
> **Parent Design:** [design.md](design.md)

---

## 1) Goal

Define how `/memory-context-intelligence:analysis` should use memsearch recall efficiently when the operator wants broader historical pattern analysis by default, with explicit narrowing only when a day/session/window slice is actually requested.

This shard covers the memsearch-side `trace_evidence` and `recall_evidence` contract only. It does not define direct ingestion of `MEMORY.md`, path-scoped memory files, or governed docs as the live pattern anchor; those broader source classes are defined in [08-memory-evidence-source-model.design.md](08-memory-evidence-source-model.design.md).

## 2) Checked current recall behavior

Checked local memsearch docs/runtime surfaces currently show this recall model:
- `memory-recall` starts from `memsearch search` with a natural-language query
- relevant results are deepened through `memsearch expand`
- exact conversation detail is recovered through transcript drill-down using anchor metadata
- cold-start session context only injects recent daily logs so Claude knows history exists
- stop/session hooks write summaries into `.memsearch/memory/YYYY-MM-DD.md` and include `session`, `turn`, and `transcript` anchors in HTML comments
- public checked search surfaces currently prove query, top-k, and optional `source_prefix` path scoping
- public checked search surfaces do **not** currently prove first-class `session-id`, `day`, arbitrary date-window, or configurable lookback flags

พูดง่าย ๆ: recall ตอนนี้เก่งที่ `search → expand → transcript` แต่ยังไม่ใช่ API สำเร็จรูปสำหรับ `ขอ session X ช่วงเวลา Y` แบบ one-shot. เพราะงั้น analysis surface ยังต้องเป็นคนจัด scope ของตัวเอง.

## 3) Design consequence

Because current checked recall is query-first rather than session/day/window-first:
- `/memory-context-intelligence:analysis` should own its deterministic narrowing layer
- `/memory-context-intelligence:analysis` should not pretend memsearch already has a built-in public `session/day/lookback` switch
- `/memory-context-intelligence:analysis` should not depend on raw `session_id` search as the only scope selector
- `/memory-context-intelligence:analysis` can default to broader historical bounded trace while still exposing explicit narrowing controls above deeper recall

## 4) Selected scope model for `/analysis`

The selected default is historical-first:
1. current project collection only
2. a bounded recent historical shard set across the user's work corpus
3. repeated historical trace may surface topic candidates without requiring current-session trace as the primary gate
4. current-session evidence becomes supporting provenance/freshness context when present
5. explicit narrowing such as `day=YYYY-MM-DD`, `session=<id>`, or `lookback=<minutes|hours>` remains available when the operator wants it

Default scope policy:
- **project scope:** current project collection only
- **historical scope:** bounded recent historical shards, not broad unbounded all-history
- **day/session narrowing:** off by default unless explicitly requested
- **lookback default:** none when historical-default scope is active
- **lookback configurable:** available only when the operator selects a narrower slice
- **current-session confirmation:** useful as a boost, not a gate

If the broader historical slice is weak:
- report `insufficient` or `no-topics`
- explain that broader historical analysis did not find a sufficiently repeated pattern to propose yet
- recommend waiting for stronger historical recurrence or gathering fresher trace
- do not silently fabricate a topic from context-only sources

If the operator explicitly requests a narrow slice and it is weak:
- keep the response scoped to that requested slice
- say that the explicit slice is insufficient
- do not silently widen beyond the user-selected narrowing basis

## 5) How memsearch recall should be used inside that scope

### L0 — deterministic scope selection
Use the source-of-truth markdown and anchor structure to define the bounded candidate memory slice:
- default historical mode selects a bounded recent shard set
- explicit `day=` selects one date shard
- explicit `session=` narrows to one session when present
- explicit `lookback=` shortens the effective time window inside the selected narrow slice

### L1 — preferred scoped recall search
Inside the selected slice, prefer memsearch `search → expand` retrieval when the runtime can resolve that path in checked scope.

### L1b — bounded raw fallback
If memsearch-backed retrieval is unavailable or returns no useful bounded records, fall back to bounded raw shard filtering before presentation.

### L2 — expand
Use `memsearch expand` when a ranked chunk needs full section context.

### L3 — transcript drill-down
Use transcript drill-down only when exact turn wording or detailed causal sequence materially matters.

## 6) Why this shape is more efficient

This model separates two problems:
- **scope selection** = bounded historical default with explicit narrow overrides
- **semantic deepening** = memsearch search/expand/transcript inside that selected scope

Without this split, `/analysis` would either over-narrow too early to one active session or over-widen into vague freeform history without a checked boundary.

## 7) Boundaries preserved in the implementation wave

This contract still does **not** select:
- unbounded all-history recall
- silent widening beyond an explicitly requested narrow slice
- a first-class new public `review` or `packet` surface
- `/additional/` behavior changes
- plugin-managed auto-flow claims
- publication, external marketplace release, stable/broad production readiness, or main RULES promotion/mutation/merge

## 8) Implementation status after phase 053

This shard no longer describes target-state only.

The current runtime package now applies this historical-default design in checked scope:
- `lib/intake.py` defaults to a bounded recent historical shard set instead of forcing current-session-first narrowing
- explicit `day`, `session`, and `lookback` narrowing still work when requested
- `lib/signals.py` can promote repeated historical trace without requiring current-session confirmation as the primary gate
- current-session confirmation remains visible as provenance and score boost only
- `lib/presentation.py` and `skills/analysis/SKILL.md` now use historical-first insufficiency wording and provenance labels such as `historical-only` versus `confirmed-in-current-session`
- current proof for the scope behavior comes from green focused/full tests plus direct packaged `intake → signals → present` execution
- checked approved non-interactive local slash invocations of `/memory-context-intelligence:analysis` now return operator-facing output when local command approval is intentionally granted with `--permission-mode bypassPermissions`
- plain no-approval print-mode is not used here as proof because this surface needs a local command run

---

> Full history: [../changelog/changelog.md](../changelog/changelog.md)
