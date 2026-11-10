# Memory Evidence Source Model

## 0) Document Control

> **Parent Scope:** memory-context-intelligence plugin-local governed design chain
> **Current Version:** 0.1.88
> **Session:** 08244912-a195-4926-84e6-8c202c667ba5 (2026-11-10)
> **Parent Design:** [design.md](design.md)

---

## 1) Goal

Define the source-of-analysis architecture for `/memory-context-intelligence:analysis` so current implementation truth, source classes, provenance handling, weighting, and promotion logic are explicit in checked scope.

## 2) Current implemented source model

The current checked implementation uses four explicit source classes.

## 2.0) Same-intake topic-discovery evidence projection

The selected correction makes intake the semantic evidence owner. Assign a run-local `ref` to each policy-enabled trace record before signals; signals and candidate evidence references retain that same reference. The analysis wrapper projects `topic_discovery_evidence` from the already-loaded intake records, not signal/display previews, and does not run intake again. Each item contains `ref`, the bounded privacy-minimized `content`, and truthful `content_truncated` metadata; include at most 50 trace excerpts and no more than intake's character budget. A 220-character `content_preview` remains presentation/index text, never canonical discovery evidence or a fallback for missing content.

Exclude transcript paths, session IDs, shard/section locators, generated interpretations, and context-only records from the caller/worker evidence projection. Reuse intake minimization and retain caller sanitization before worker dispatch: remove remaining sensitive/unrelated details or omit an excerpt when sanitization would destroy its evidentiary meaning. The same references identify evidence for local semantic discovery, optional independent workers, and main-session verification. Workers acquire no new evidence and return zero candidates when supplied content cannot support a claim.

This projection is not a new evidence class, persistent identifier, across-run provenance claim, eligibility decision, or promotion state. Report sampling/source-read limits separately from record-content truncation; neither a bounded excerpt nor a selected day means every historical record was analyzed. Missing or genuinely truncated decision evidence remains subject to the unchanged Phase075 fail-closed gate.

| Source class | Current implemented input | Main purpose | Current role in promotion |
|---|---|---|---|
| `trace_evidence` | oldest-unprocessed complete `.memsearch/memory/YYYY-MM-DD.md` records in bounded chronological batches by default; explicit narrow/supplemental inspection remains stateless | detect repeated historical work patterns, friction, or workflow drift | required live pattern anchor |
| `recall_evidence` | memsearch-backed `search → expand` records when available inside the selected bounded scope | recover exact wording, sequence, and causal detail for a candidate pattern | supporting exactness only |
| `durable_memory_context` | `MEMORY.md` plus relevant path-scoped memory entries when available in checked scope | supply durable preference, recurring project context, and previously validated operating constraints | supporting context only |
| `governance_context` | checked RULES/design/changelog/TODO/phase/patch surfaces in scope | map owner chains, existing doctrine, boundaries, rollout posture, and promotion destination | supporting owner/boundary fit only |

## 2.1) Selected config-file source-policy boundary

Phase 067 implements the bounded config-file source-policy behavior for this source model.

Current checked behavior:
- the config file is a late-bound analysis-default/source-limit policy for the existing evidence model
- the default config target is now the user-scope file `~/.claude/memory-context-intelligence.config.json`
- the intake layer accepts explicit `--config <path>` and otherwise falls back to that user-scope default path instead of project-local upward discovery
- current checked fields now include `analysis.scope_policy.default_scope_mode`, `scope_day_shard`, `scope_session_id`, `scope_lookback_minutes`, plus `enabled_source_classes`, `max_historical_shards`, and `allow_same_day_widening`
- source-policy filtering now runs before later signals/presentation stages, so policy-limited runs only carry the remaining allowed source classes forward
- stored `scope_policy` applies only when the operator did not explicitly narrow the run; explicit `day` / `session` / `lookback` requests stay stronger than stored defaults
- when no config file is loaded, the public analysis surface may expose advisory guided config questions with `suggested_config_path` and point the operator to `/memory-context-intelligence:init`
- `/memory-context-intelligence:init` is the dedicated public setup/config surface that writes this user-scope file
- config policy is **not** a fifth evidence class
- it is **not** semantic authority
- it is **not** promotion proof by itself
- it must not persist selected-topic state that phase-010 still treats as structured fileless state
- the selected default path is intentionally user-scope under `~/.claude`; it is no longer a project-local portable default

### 2.2) Coverage and progress are separate from candidate truth

`progressive_batch` describes the contiguous complete source prefix offered to the caller and the unprocessed remainder. Run-local `ref` remains only a same-intake evidence reference; persistent progress uses exact consumed-byte digests and opaque source keys. MCI progress is not another evidence class, topic ledger, selected-topic state, Memsearch index or proof that a proposal is novel. Store only MCI pending/completed bindings and source positions in the separate user-scope progress file defined by [07](07-recall-scoping-and-time-window.design.md); keep raw trace/transcript and candidate data out.

Successful zero-topic analysis may acknowledge that exact batch. Preparation, signals, sampling, unread/truncated evidence and errors cannot certify semantic completion. The caller's explicit acknowledgement is the completion witness; source fixtures cannot prove actual model adherence. Historical age remains visible, but intentional complete backlog is not downgraded solely because it is old. Cross-batch recurrence accumulation is not implemented or claimed; each signal report still judges its supplied batch.

## 3) What each source class is meant to prove

### 3.1 `trace_evidence`

Use `trace_evidence` to answer questions like:
- did this pattern actually happen across the user's recent historical work?
- is it repeated enough across shards or sessions to surface as a topic?
- how recent is the recurrence?
- is the pattern historical-only or also confirmed in the current session?

This remains the strongest live operational source.

### 3.2 `recall_evidence`

Use `recall_evidence` when the topic needs exact remembered detail such as:
- what wording triggered the failure?
- what correction sequence happened across turns?
- what transcript-adjacent detail best explains the candidate?

This sharpens a pattern found in `trace_evidence`; it does not replace the existence of a live pattern.

### 3.3 `durable_memory_context`

Use `durable_memory_context` to answer questions like:
- is this preference or correction durable beyond one session?
- is there relevant project context that explains why the pattern matters?
- is there remembered user guidance that changes how strong the proposal should be?

This is reusable context, not live empirical proof.

### 3.4 `governance_context`

Use `governance_context` to answer questions like:
- which owner surface should absorb the improvement if it survives review?
- does existing doctrine already cover this?
- is the proposal blocked by an existing boundary or deferred phase?
- what promotion path would be correct if the candidate later advances?

This is authority-fit context, not pattern discovery input by itself.

### 3.5) Supplemental historical trace windows

An explicitly requested supplemental analysis may consume one bounded daily-shard window strictly older than the actual budget-aligned first historical-default window. Intake applies existing shard/record/character/byte and source-policy caps, rotates representative records across days/sessions/entries, and owns selected/read/sampled coverage, empty/unreadable/byte-limited days, sampling limits and content-truncated references. The analysis surface exposes that coverage alongside its selected window, exclusive boundary and pass status; a single selected historical day is not an explicit day override. Days excluded by the record budget remain eligible in the next window. This remains bounded sampling, not all-record coverage, and adds no evidence class or persistent search state.

Supplemental trace discovery is unavailable when the run was explicitly/configurationally narrowed, the first-pass boundary is missing, or source policy disables `trace_evidence`. If the first analysis used an explicit config path, the same path must be passed into the supplemental invocation so configured source restrictions remain in force. An unavailable or empty window retains its reason and checked-boundary metadata where available; it must not be rendered as corpus-wide absence. Supplemental evidence creates a new candidate set and cannot strengthen or relabel rejected candidates from the earlier pass.

## 4) Provenance contract

Every surfaced topic should preserve provenance by source class.

Current implementation expectations:
- `trace_evidence`: keep `historical-only` versus `confirmed-in-current-session` visible
- `recall_evidence`: remain visible when memsearch-backed retrieval materially sharpened the candidate
- `durable_memory_context`: remain visible when durable memory materially strengthened the candidate
- `governance_context`: remain visible when owner/boundary/promotion fit materially shaped the candidate
- config-file source policy: remain visible when source selection or source limits materially narrowed what the run could judge, so a limited-source run does not overread as broader evidence than it actually holds
- adaptive deepening: if read-only subagent or web/external research support materially strengthened the explanation, keep that support visible as supporting evidence rather than letting it read like a new promotion anchor

The first operator-facing response does not need raw dumps, but it should make the evidence mix visible enough that the user can tell where the proposal came from.

### 4.1) Normalized standalone evidence contract

Raw evidence anchors and emitted additional-stage doctrine serve different purposes and must remain separate.

Internal analysis, orchestration, or packet reports may retain bounded raw anchors when they are needed for leader audit or candidate entailment review. Those internal anchors may include shard identity, section identity, record previews, source paths, session provenance, or other trace-local detail.

An emitted additional-stage rule must instead carry a self-contained normalized evidence basis. It should preserve:
- the evidence classes that materially shaped the candidate
- whether the pattern is historical-only or also current-session-confirmed
- recurrence and breadth at the level needed to judge strength
- confidence and evidence label
- the transferable observed pattern
- relevant conflicts, uncertainty, and excluded scope
- why the evidence supports the proposed doctrine mechanism
- what still needs leader verification before promotion consideration

The emitted rule must not depend on:
- `.memsearch` or memory-shard filenames
- transcript or JSONL paths
- temporary directories or packet-report paths
- absolute workstation paths used only during evidence gathering
- raw `path:line` or shard/section anchors
- raw record previews that are necessary to reconstruct the candidate's meaning

Evidence normalization is a semantic distillation step, not simple redaction. The normalized text must explain the repeated mechanism well enough that the trial artifact remains understandable if the original transient evidence files disappear.

Before ranking or emission, the selected candidate must pass an entailment check:
- retain when bounded trace evidence directly supports the stated mechanism
- narrow when it supports only part of the proposed doctrine
- mark context-only and non-promotable when the source does not prove a live pattern
- reject when the evidence is semantically unrelated to the candidate title or mechanism

Durable memory and governance context may sharpen the normalized explanation, but they must not replace missing `trace_evidence` as the live trial anchor.

## 5) Weighting model

This implementation uses role-weighted evidence, not one flat score.

### 5.1 Pattern-strength weighting

Primary pattern-strength order:
1. `trace_evidence`
2. `recall_evidence`
3. `durable_memory_context`
4. `governance_context`

Interpretation:
- `trace_evidence` is the main signal that something is happening repeatedly in the user's broader historical work
- `recall_evidence` sharpens exactness and causal detail
- `durable_memory_context` strengthens confidence that the pattern matters beyond one isolated moment
- `governance_context` strengthens fit, not existence

### 5.2 Historical ranking factors

Inside `trace_evidence`, the active ranking now favors:
1. repeated historical trace count
2. cross-session breadth
3. recency
4. current-session confirmation as an additional boost when present

`current_session_confirmation` improves confidence, but it is not the primary promotion gate anymore.

## 6) Promotion logic

### 6.1 No strong candidate

Report no strong candidate when:
- broader historical trace does not repeat strongly enough yet
- only `durable_memory_context` or `governance_context` exists without live trace support
- `recall_evidence` exists but only sharpens a non-repeated pattern
- a config-file source limit leaves no remaining live trace support inside the selected bounded run
- the strongest historical signal is still below the promotion gate in the selected bounded batch; this says nothing about unprocessed history

### 6.2 Proposal-first topic is allowed

A proposal-first topic may surface when:
- `trace_evidence` shows a repeated historical pattern strong enough to review
- `recall_evidence`, `durable_memory_context`, or `governance_context` strengthen the candidate when relevant
- adaptive deepening may sharpen mechanism, stop-gate wording, source-trust framing, or supporting principle detail, but it must stay explicitly subordinate to the trace-backed local topic
- the result can still be framed honestly as a design-grounded review topic rather than a promotion-ready rule change

### 6.3 Promotion-consideration candidate

A candidate is ready for later trial/promotion consideration only when:
- live pattern strength is already established through `trace_evidence`
- supporting exactness/context from `recall_evidence` and/or `durable_memory_context` is sufficient for review
- `governance_context` identifies the correct owner surface, active boundaries, and later staging path
- any config-file source policy in play limited or selected the run honestly without being mistaken for proof itself

This still does **not** authorize direct main RULES mutation.

## 7) Operator-facing output implications

The first response should stay proposal-first or actionable-insufficiency-first.

Current implementation expectations:
- topics include short why/impact wording
- source mix is surfaced compactly when durable memory or governance context materially shaped a candidate
- provenance is visible enough to distinguish `historical-only` from `confirmed-in-current-session`
- if no strong candidate exists, the response says so directly instead of using governance or memory context as a substitute for live trace proof
- package-map or internal pipeline explanation still must not appear by default just to avoid a short answer

## 8) Remaining boundaries

This implemented source model still does **not** claim:
- interactive config-file writing, auto-save, or automatic config mutation from the guided helper
- selected-topic persistence inside config
- proof beyond the checked standalone `/additional/` source/test/smoke and tagged-release scope; design approval alone is not implementation proof
- plugin-managed first-response auto-flow proof
- marketplace installation or marketplace publication
- stability over time or stable-broad readiness
- main RULES promotion
- main RULES mutation
- main RULES merge

---

> Full history: [../changelog/changelog.md](../changelog/changelog.md)
