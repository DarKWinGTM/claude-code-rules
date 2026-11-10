# Recall Scoping and Time-Window Contract

## 0) Document Control

> **Parent Scope:** memory-context-intelligence plugin-local governed design chain
> **Current Version:** 0.1.90
> **Session:** 08244912-a195-4926-84e6-8c202c667ba5 (2026-11-10)
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
2. one oldest-unprocessed contiguous batch within the chosen 1–14-calendar-day interval including today
3. repeated historical trace may surface topic candidates without requiring current-session trace as the primary gate
4. current-session evidence becomes supporting provenance/freshness context when present
5. explicit narrowing such as `day=YYYY-MM-DD`, `session=<id>`, or `lookback=<minutes|hours>` remains available when the operator wants it

Default scope policy:
- **project scope:** current project collection only
- **historical scope:** the selected inclusive recent calendar interval, consumed in bounded batches rather than loaded all at once
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

Before preparation the Skill resolves the missing run choices under [02](02-topic-list-and-choice-flow.design.md). Internal `analysis-surface --window-days <1..14> --current-day YYYY-MM-DD` validates the interval; absent period returns `awaiting-caller-scope` before corpus/progress access. Compute `start_day = invocation_day - (days - 1)` and `end_day = invocation_day` once. Filter date-named shard discovery before hashing or reading: no future dates, older dates or compensation for missing dates. Explicit/configured day restrictions and supplemental boundaries must fit; conflicting constraints block without clamping or dropping them. `lookback` still filters same-day clock time, never substitutes for a multi-day calendar interval.

Use the source-of-truth markdown and anchor structure to define the bounded candidate memory slice:
- normal analysis selects oldest-unprocessed shards inside that interval in chronological order, up to the configured shard cap (at most10 per batch) and record/character/byte budgets; default8 records need not cover the full interval
- read complete newline-terminated records without sampling or truncating a record and moving beyond it; stop before a record that will not fit, retaining its position for a later batch
- reconstruct bounded parser context when resuming inside a shard; source-position keys and the digest of the exact consumed bytes bind completion, not run-local excerpt IDs
- intake distinguishes contiguous batch coverage from remaining days/tails; byte-limited or incomplete lines remain unprocessed. A byte window can commit its complete earlier prefix, never the omitted tail. An oversized single record needs a larger bounded budget; an unfinished append needs completion
- explicit older-than supplemental inspection retains balanced bounded sampling, stays inside the original calendar interval and keeps its existing no-rescue eligibility contract; it never advances normal progress
- explicit `day=` selects one date shard
- explicit `session=` narrows to one session when present
- explicit `lookback=` shortens the effective time window inside the selected narrow slice

Explicit/configured day/session/lookback/text filters and scoped session retrieval retain their existing ordering/narrowing semantics and are non-advancing inspection. Direct `intake`, replay and trial stay stateless unless the analysis surface explicitly supplies its MCI batch request.

### Incremental completion and catch-up

Normal analysis reads `~/.claude/memory-context-intelligence/progress.json`, separated by canonical memory-root, enabled-source-class fingerprint and exact calendar-window identity. No checkpoint starts at the oldest input in that interval. Legacy unrestricted entries and pending batches remain unchanged in the same store; selecting a recent interval never resets, migrates or acknowledges them. Different date intervals have independent progress identities, not separate stores. State contains pending and last-completed bindings plus per-shard byte-prefix cursors, hashes and opaque record keys; it excludes raw traces, transcripts and topic artifacts. Keeping per-shard completed prefixes permits a later append to an older date to be found without treating every earlier day as sealed. A rewrite, missing source, invalid state, stale batch or changed scope blocks instead of resetting or skipping.

Preparation captures a finite endpoint (shard names, byte lengths, content digests), emits canonical evidence and installs only a pending binding under the MCI lock. A nonblocking native file lock, expected-version/position checks and atomic owner-only temporary-file replacement protect state updates. No completion is inferred from exit0, intake success, candidate generation or a deterministic no-topic result. After semantic discovery/eligibility finishes for the complete batch, the caller invokes internal `complete --batch-id <id> --outcome analyzed|no-topics|failed`. Successful analyzed/zero-topic acknowledgements validate consumed source prefixes and advance exactly that batch; failure/no acknowledgement does not advance. Duplicate completion is idempotent. This is caller attestation, not an independent proof of model reasoning.

Plain invocation stops after one acknowledged batch. Only explicit whole-period intent selects `mode=catch-up`, using the same caller cycle, fixed run endpoint and calendar interval, never a Python preparation-only loop, new background entity or recursive Skill call. Continuation requires the preceding acknowledgement and carries the original `--window-days`/`--current-day` even across midnight; changed intervals or legacy run IDs cannot resume it. Stop on failure/interruption/context limit; a later invocation with the same interval resumes its committed progress with a fresh endpoint. New/backdated appends beyond the original endpoint wait for that new invocation and still must fit its interval. `caught-up` is endpoint coverage within the selected dates, not corpus-wide absence of improvement topics. Freshness remains metadata, never authority to read outside the selected interval.

Skill startup uses one `--startup` injection that reads no corpus/progress. Claude receives slash text through documented Skill substitution and first interprets it under [02](02-topic-list-and-choice-flow.design.md). Before acquisition, serialize only requested retrieval controls using the existing day/session/lookback/text/config/mode interfaces. Always pass the resolved calendar controls; pass explicit `--arguments ""` when no additional restrictions are requested, retaining output instructions in caller context. Free text reaches the existing scope parser only for a genuine literal-filter request; direct internal CLI parsing remains unchanged. Shell-quote values as data, never evaluate substitutions or interpolate user text into eager execution. Unsupported/ambiguous constraints or a literal colliding with control syntax must be clarified rather than silently discarded or reinterpreted. This neither assumes a shell-exported argument variable nor adds a natural-language parser or second state owner.

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
- normal `analysis-surface` uses the Phase078 date-bound oldest-unprocessed progressive request; direct `lib/intake.py` retains existing stateless behavior unless the analysis surface supplies its optional calendar controls
- explicit `day`, `session`, and `lookback` narrowing still work when requested
- `lib/signals.py` can promote repeated historical trace without requiring current-session confirmation as the primary gate
- current-session confirmation remains visible as provenance and score boost only
- `lib/presentation.py` and `skills/analysis/SKILL.md` now use historical-first insufficiency wording and provenance labels such as `historical-only` versus `confirmed-in-current-session`
- current proof for the scope behavior comes from green focused/full tests plus direct packaged `intake → signals → present` execution
- checked approved non-interactive local slash invocations of `/memory-context-intelligence:analysis` now return operator-facing output when local command approval is intentionally granted with `--permission-mode bypassPermissions`
- plain no-approval print-mode is not used here as proof because this surface needs a local command run

---

> Full history: [../changelog/changelog.md](../changelog/changelog.md)
