# Memory Evidence Source Model

## 0) Document Control

> **Parent Scope:** memory-context-intelligence plugin-local governed design chain
> **Current Version:** 0.1.75
> **Session:** d42465eb-30a7-4bc8-b9d6-03e52306e9a5 (2026-06-01)
> **Parent Design:** [design.md](design.md)

---

## 1) Goal

Define the source-of-analysis architecture for `/memory-context-intelligence:analysis` so current implementation truth, source classes, provenance handling, weighting, and promotion logic are explicit in checked scope.

## 2) Current implemented source model

The current checked implementation uses four explicit source classes.

| Source class | Current implemented input | Main purpose | Current role in promotion |
|---|---|---|---|
| `trace_evidence` | bounded recent `.memsearch/memory/YYYY-MM-DD.md` records across the active project’s recent historical shard set by default | detect repeated historical work patterns, friction, or workflow drift | required live pattern anchor |
| `recall_evidence` | memsearch-backed `search → expand` records when available inside the selected bounded scope | recover exact wording, sequence, and causal detail for a candidate pattern | supporting exactness only |
| `durable_memory_context` | `MEMORY.md` plus relevant path-scoped memory entries when available in checked scope | supply durable preference, recurring project context, and previously validated operating constraints | supporting context only |
| `governance_context` | checked RULES/design/changelog/TODO/phase/patch surfaces in scope | map owner chains, existing doctrine, boundaries, rollout posture, and promotion destination | supporting owner/boundary fit only |

## 2.1) Selected config-file source-policy boundary

Phase 067 implements the bounded config-file source-policy behavior for this source model.

Current checked behavior:
- the config file is a late-bound source-selection/source-limit policy for the four existing source classes
- the intake layer accepts explicit `--config <path>` and also discovers `memory-context-intelligence.config.json` upward from the current working directory when no explicit path is supplied
- current checked fields include `enabled_source_classes`, `max_historical_shards`, and `allow_same_day_widening`
- source-policy filtering now runs before later signals/presentation stages, so policy-limited runs only carry the remaining allowed source classes forward
- same-day widening requested by config does not override an explicit narrow run; explicit `day` / `session` / `lookback` requests stay narrow unless the operator explicitly asks for widening
- when no config file is loaded, the public analysis surface may expose advisory guided config questions with `suggested_config_path`, but that helper does not write config automatically
- config policy is **not** a fifth evidence class
- it is **not** semantic authority
- it is **not** promotion proof by itself
- it must not persist selected-topic state that phase-010 still treats as structured fileless state
- it must not hard-code machine-local paths as portable defaults; exact local paths stay runtime-discovered facts or explicit machine-scoped overrides only

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
- the strongest historical signal is still below the promotion gate even after bounded recent history was checked

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
- `/additional/` behavior changes
- plugin-managed auto-flow proof
- publication
- external marketplace release
- stable-broad readiness
- main RULES promotion
- main RULES mutation
- main RULES merge

---

> Full history: [../changelog/changelog.md](../changelog/changelog.md)
