# Topic List and Choice Flow

## 0) Document Control

> **Parent Scope:** memory-context-intelligence plugin-local governed design chain
> **Current Version:** 0.1.74
> **Session:** d42465eb-30a7-4bc8-b9d6-03e52306e9a5 (2026-06-01)
> **Parent Design:** [design.md](design.md)

---

## 1) Goal

Define the user-facing analysis flow for this capsule so that it analyzes bounded historical memory evidence, lifts weak/raw incidents through doctrine/mechanism lenses, presents doctrine-level proposed improvement topics first, and only then asks the user to choose which topic to expand.

## 2) Required interaction contract

The flow must be:

1. analyze bounded historical memory evidence
2. present proposed improvement topics as a numbered or sectioned list
3. after the list is visible, keep the slash invocation itself as the active request even when no extra text was supplied
4. after the topic cards, render one compact advisory next-action bridge that keeps topic selection and direct follow-up choices visible
5. expand only the chosen topic into deeper concept/matrix/design output
6. do not mutate RULES directly from this flow

พูดง่าย ๆ: ต้องโชว์รายการหัวข้อก่อน แล้วค่อยให้ user เลือกทีหลัง แต่รอบนี้รายการหัวข้อควรมาจาก broader historical work patterns เป็นค่า default ไม่ใช่ล็อกที่ current session ก่อนเสมอ

## 2.1) Selected memory-input contract

The selected design **is** broader historical analysis by default, but still bounded.

Before topic-list presentation, `/memory-context-intelligence:analysis` should use this scope model:
1. current project collection only
2. bounded recent historical shards across the user's work corpus by default
3. repeated historical trace may surface topic candidates without requiring current-session trace as the primary gate
4. current-session evidence becomes supporting provenance/freshness context when present
5. explicit narrowing such as `day=YYYY-MM-DD`, `session=<id>`, or `lookback=<minutes|hours>` remains available when the operator wants it

Design defaults:
- default project scope = current project collection only
- default historical scope = bounded recent history, not unbounded all-history
- default current-session narrowing = off unless explicitly requested
- default lookback = none in historical-default mode
- explicit narrow-slice runs should stay narrow rather than silently widening beyond the chosen request

Current checked memsearch recall evidence still means this scoping layer must exist **before** deeper recall/analysis, because public recall is search-first and does not currently prove first-class `session/day/lookback` flags.

Within that bounded scope, memsearch recall may still be used in progressive layers:
- L1: query/search inside the bounded selected scope
- L2: expand selected chunks for fuller section context
- L3: transcript drill-down for exact turn-level evidence

## 2.2) Selected public invocation model

The selected user-facing invocation design is analysis-only for now:
- checked registered analysis slash surface: `/memory-context-intelligence:analysis`
- deferred / non-public surfaces: `/memory-context-intelligence:review`, `/memory-context-intelligence:packet`

Checked current bare-alias state:
- bare `/analysis` is not present in checked slash-command registry output
- do not treat bare `/analysis` as proved current runtime behavior in this wave

Why this model is selected now:
- `analysis` already matches the proposal-first topic-list contract
- the user selected one public operator-facing command rather than a multi-command surface
- `review` is not yet distinct enough from expanding or evaluating a chosen proposal
- `packet` is still a second-stage artifact/output shape rather than a first-response command

Current checked implementation aligns the active proposal-first contract to historical-default intake behavior. Proof comes from green focused/full tests plus direct packaged `intake → signals → present` execution, together with checked approved non-interactive local slash output for `/memory-context-intelligence:analysis` when local command approval is intentionally granted with `--permission-mode bypassPermissions`. Plain no-approval print-mode is not used as proof because this surface needs a local command run. Earlier proof for `/memory-context-intelligence:memory-context-intelligence` remains historical pre-implementation evidence only, while `review` and `packet` remain deferred.

## 2.3) Selected evidence-source presentation contract

Current implementation truth:
- first-response topics are now generated from the implemented four-class model
- `trace_evidence` remains the live promotion anchor
- `recall_evidence`, `durable_memory_context`, and `governance_context` can strengthen exactness, durability, or owner fit without replacing live trace proof

Selected operator-visible expectations:
- the first response should disclose the evidence mix compactly enough that the user can tell whether a topic is `historical-only` or `confirmed-in-current-session`
- broader multi-session/multi-shard historical patterns should be prioritized ahead of narrow historical-only signals when the system chooses what to surface first
- narrow historical-only shapes such as `2 trace / 1 session / 1 shard` must not read like strong broader historical review
- durable memory and governance inputs should strengthen context and owner fit, not replace live pattern evidence

## 3) Initial topic families

The first concept set should support topics such as:
- Context Digest
- Workflow Advisor
- Governance Radar
- Signal Schema / Matrix Spec
- Transcript Bridge
- Candidate Packet Builder
- Sensitivity / Disclosure Filter

Each topic shown in the first output layer should include a balanced explanation of:
- what the topic is for
- why it surfaced from real work traces
- how it would affect behavior, workflow, or understanding if adopted
- what output or product the user would receive from expanding it
- whether serious external research is likely needed before the proposal becomes strong enough to trust

High-level mechanism notes are optional in the first layer. They should appear only when they materially help the user understand the proposal; they must not become the default center of the first response.

The explanation should be rich enough that the user can understand the proposal without guessing, but still compact enough to scan as a list.

This means the first list is a proposal surface. It is presenting candidate improvement topics or candidate RULES-adjacent mechanisms, not performing the improvement yet.

## 4) Output layering

### First output layer

Show only the topic list with short descriptions, short why/impact wording, and a recommended first topic when one is materially stronger.

The first output layer must:
- frame the result as a design-grounded RULES/workflow review surface, not as a generic recurring-pattern summary
- present topic candidates directly as doctrine-level historical work-pattern review topics
- rewrite titles into semantic human-readable titles rather than exposing raw slug/token-bag wording
- keep top-level topic names at RULES/workflow principle or mechanism level rather than incident-level issue wording
- keep incident details such as `404`, `python error`, or similar case examples inside proposal evidence/examples or provenance instead of the title
- allow sparse historical runs to keep at least 3 advisory topics by splitting distinct doctrine lenses rather than emitting an incident list
- the slash invocation itself must count as the request even when the user provides no extra text after `/memory-context-intelligence:analysis`
- when rendered analysis context exists, the first response must not fall back to a generic `no request` answer and must instead render the corresponding `available`, `blocked`, `dormant`, or `no-topics` state
- the first response must render surfaced topics as repeated topic cards, for example `Topic 1`, `Topic 2`, `Topic 3`
- each surfaced topic must keep the same repeated presentation pattern so the user can compare topics directly without reading a wrapper report first
- one topic must not be split across separate top-level report-wrapper sections
- if one topic is stronger, mark it inside that same topic card as the recommended first topic instead of opening a separate recommendation section
- same-family weaker topics may still appear, but they should stay in the same repeated topic-card rhythm rather than being moved into a separate global variants block
- after the topic cards, render one compact advisory `Next action options` bridge
- that bridge must stay after the topic cards, not before them, and it must not become a new competing wrapper structure
- the bridge should tell the user they can choose a topic number, type a direct request, or ask for deep thinking / websearch / webfetch before any adjustment
- the bridge must stay advisory-only and must not be treated as approval, automatic execution, or carry-forward permission
- keep provenance visible enough to distinguish `historical-only` from `confirmed-in-current-session`
- make the breadth summary explicit enough to show when broader multi-session/multi-shard history outranked narrow historical-only signals
- surface compact source-mix wording when durable memory or governance context materially shaped a candidate
- when no config file is loaded for the run, the operator-facing payload may expose an advisory guided config helper with `config_questions` and `suggested_config_path` instead of treating raw args as the normal config UX
- when `adaptive_deep_analysis.deepening_required` is true, the first response must run one bounded deepening pass for the top 1-2 topic ids named in `adaptive_deep_analysis.required_topic_ids` before the topic cards are rendered
- that deepening pass may use read-only subagent help plus supporting web/external research when those tools are available, but it must stay advisory-only and must not replace local trace proof
- if a required deepening tool is unavailable, the response must say so explicitly instead of silently skipping the deepening step
- include provenance notes when they materially help the user judge the evidence boundary
- every first-pass topic card should include a compact `Before behavior` and `After behavior` preview so the user can picture the change immediately without waiting for a second prompt
- those first-pass before/after previews must stay compact, human-readable, and evidence-calibrated; they help visualize the target change but must not overclaim that the current system always behaved exactly that way
- when usable bounded record previews exist, expanded proposals should include concrete `Evidence examples`, `Before behavior`, and `After behavior` sections sourced from found data such as `signal.records[].content_preview`
- if usable bounded preview evidence is absent, do not invent generic case examples; keep the compact before/after preview but omit the evidence-example section
- long-form illustrative before/after belongs to the expanded follow-up layer after the user asks for deeper explanation or selects a topic
- the live wrapper should call `present` in `native-first` mode instead of `auto` so operator-facing rendering does not drift away from the intended native-first contract when no stronger explicit mode choice was selected
- when recent user-facing context does not provide a stronger language signal, the live operator wrapper should keep the local Thai-native fallback instead of silently falling back to English labels-only output
- known doctrine-level topic cards should restore richer Thai explanation bodies for `มันคืออะไร`, `อาการ/ปัญหา`, `ก่อนปรับ`, `หลังปรับ`, and `ถ้าปรับแล้วจะดีขึ้นยังไง` instead of localizing only the labels while leaving the explanation body in English
- show each expanded proposal as `candidate only`, `advisory only`, and `not approved yet`
- let the first response read as native-first operator-facing output without requiring a second manual rewrite pass
- avoid package-map explanation, governance-map explanation, internal pipeline narration, or development/progress-summary output by default

If no strong candidate exists:
- say directly that broader historical analysis did not find a sufficiently repeated pattern to propose yet
- include one short actionable insufficiency line
- include one short next-step or promotion-gate line
- do not fill the response with workflow explanation just to avoid a short answer

If memsearch-backed analysis is blocked:
- say so directly with the memsearch/input reason

If memsearch-backed analysis is dormant:
- say so directly because the memsearch input is stale

If the operator explicitly selected a narrow slice and it is weak:
- keep the response scoped to that explicit slice
- say that the selected narrow scope is insufficient
- do not silently widen beyond the chosen narrowing request

The list should be presented in the user's active working language where practical.

### Second output layer

After user choice or explicit request for internals:
- expand the selected topic
- show matrix / mechanism / boundary / rollout detail for that topic
- keep unchosen topics collapsed
- keep explanatory text in the user's active working language where practical
- preserve canonical technical identifiers, file paths, commands, env vars, and exact evidence anchors in exact form

## 5) Interactive presentation configuration

The presentation layer should support interactive configuration for how analysis results are shown.

Minimum output modes:
- `auto` — detect the user's active working language and adapt automatically
- `native-first` — explain primarily in the user's language while preserving canonical technical terms where needed
- `bilingual` — explain in the user's language while retaining key technical labels in English
- `fixed` — lock presentation to a user-selected language

The analysis method itself should default to one full-power evidence-backed distillation path rather than several user-facing research modes.

That full-power method combines:
- `trace_evidence` from bounded memsearch work traces
- `recall_evidence` when exact search/expand/transcript detail is needed
- `durable_memory_context` from `MEMORY.md` and relevant path-scoped memory files when durable context matters
- `governance_context` from checked owner surfaces when doctrine fit or promotion routing matters
- topic-specific external research when broader support is needed
- source-trust review
- confidence and limitation reporting
- synthesis through native agent lanes when the scope is broad enough to benefit from delegated gathering/review

Effective precedence:
- explicit per-run presentation or source-policy choice
- current session skill config
- default skill config or persisted config-file source policy

## 5.1) Selected config-file source-policy boundary

Phase 067 implements the bounded config-file source-policy behavior for this analysis surface.

Current checked behavior:
- the intake layer accepts explicit `--config <path>` and also discovers `memory-context-intelligence.config.json` upward from the current working directory when no explicit path is supplied
- the config file may hold late-bound source-selection/source-limit defaults for the existing four evidence classes
- current checked fields include `enabled_source_classes`, `max_historical_shards`, and `allow_same_day_widening`
- explicit narrow runs stay narrow even when config requests same-day widening; config widening applies only to non-explicit runs unless the operator explicitly asks for widening
- when no config file is loaded, the analysis surface may emit advisory `config_questions` plus `suggested_config_path` so the operator gets guided config help instead of depending on raw args as the normal UX path
- the guided helper remains advisory only; it does not write config automatically and does not replace phase-010 structured fileless selected-topic state
- config policy must not be treated as a fifth evidence class, semantic authority, or live promotion proof
- config policy must not override evidence/provenance wording boundaries or turn durable/governance context into trace-equivalent proof
- portable defaults must not hard-code machine-local paths; exact local paths stay runtime-discovered facts or explicit machine-scoped overrides only

## 6) Language-aware presentation boundary

Presentation should follow the user's active working language where practical.

Required behavior:
- localize headings, descriptions, summaries, and choice prompts to the user's active working language
- preserve canonical technical identifiers in exact form
- keep quoted evidence exact when fidelity matters
- if translation could weaken authority or evidence meaning, show the native explanation plus the canonical technical term
- let the choice UI follow the currently selected output mode

## 7) Boundary conditions

This flow must not:
- skip the topic-list stage
- auto-select a topic without the user
- hide that the output is memory-derived and non-authoritative
- present candidate topics as if they were already-approved RULES changes
- treat topic expansion as permission to create or modify real RULES immediately
- translate identifiers, file paths, commands, config keys, or anchors into approximate wording
- let presentation configuration override authority or evidence wording boundaries

## 8) Runtime implementation status

Phase 010 implemented the list-first runtime steps in the isolated package under `<repo-root>/plugin/memory-context-intelligence/`:
- `present` renders the list-first topic review from phase-009 signals output
- `choose` records one selected topic as structured fileless state
- `auto`, `native-first`, `bilingual`, and `fixed` modes are supported
- canonical technical identifiers are copied through rather than translated
- unselected topics remain advisory-only

Phase 053 extends the active behavior around that presentation layer:
- the default scope feeding `present` is now broader historical bounded memory rather than current-session-first narrowing
- topic provenance now distinguishes `historical-only` from `confirmed-in-current-session`
- no-topics wording is now historical-first by default
- current-session confirmation is a boost, not the primary gate

Phase 054 extends the active communication contract around that same layer:
- `lib/signals.py` now rewrites recurring output into semantic human-readable titles instead of leaving keyword-bag titles as the user-facing default
- `lib/presentation.py` now separates `presentation / recommendation / proposal` in the first-pass output
- native-first output now exposes a human-readable expanded proposal contract with `มันคืออะไร`, `อาการ/ปัญหา`, `ถ้าปรับแล้วจะดีขึ้นยังไง`, `หลักฐานที่ใช้`, and `สถานะตอนนี้`
- the expanded proposal keeps status visible as `candidate only`, `advisory only`, and `not approved yet`
- the first pass no longer depends on a second manual rewrite request before it reads as operator-facing guidance

Phase 058 then lifts surfaced topics through doctrine/mechanism lenses so incident details stay out of titles and remain inside proposal evidence/examples or provenance.

Phase 059 then extends the same proposal layer further:
- when usable bounded preview evidence exists, the proposal body now adds `Evidence examples`, `Before behavior`, and `After behavior`
- those sections are sourced from found data such as `signal.records[].content_preview`
- if usable bounded preview evidence is absent, those example sections are omitted rather than replaced with fabricated generic case examples

Phase 060 then preserved the now-historical wrapper-spine experiment.

Phase 061 then corrects the operator-facing target shape:
- the default first response is now repeated topic cards rather than `presentation / recommendation / proposal / related variants` wrapper blocks
- each surfaced topic is rendered as its own topic unit with the same repeated pattern
- same-family variants remain separate topic cards in the same scan rhythm instead of being folded into one global variants wrapper
- repeated recap prose is removed so each topic card explains only that topic

Phase 062 then hardens the same operator layer further:
- the slash invocation itself is treated as the request even when the user provides no extra text after `/memory-context-intelligence:analysis`
- when rendered analysis context exists, generic `no request` fallback is disallowed and the surface must render the corresponding `available`, `blocked`, `dormant`, or `no-topics` state instead
- after the topic cards, the first response now adds one compact advisory `Next action options` bridge so the user can choose a topic number, type a direct request, or ask for deep thinking / websearch / webfetch before any adjustment
- the advisory bridge stays after the topic cards and does not become a new wrapper that competes with the repeated-card rhythm

Phase 063 then adds a temporary stale-session diagnostic safeguard:
- when checked freshness evidence shows the current session started before the installed plugin update, the surface may append one advisory `possible stale long-lived session` warning
- that warning stays additive only and must not change the normal `available` / `blocked` / `dormant` / `no-topics` status flow
- the warning may tell the operator to restart this session and retry only as a diagnostic step when slash behavior still differs from the installed source
- the warning must not normalize the bug: session-dependent no-response still remains a bug, and restart must not be framed as the final fix

Phase 064 now promotes compact `Before behavior` / `After behavior` previews into every first-pass topic card while keeping `Evidence examples` real-preview-only and leaving long-form illustrative before/after in the expanded follow-up layer.

Phase 065 then restores the richer easy-to-understand native-first first-pass explanation contract: the live analysis wrapper now renders through `present --output-mode native-first`, carries an inferred presentation language with Thai as the local fallback when no stronger recent-language signal is available, and restores richer Thai explanation bodies for the known doctrine-level topic cards instead of English labels-only hybrids.

Phase 067 then implements the bounded config-file source-policy layer: `lib/intake.py` now accepts explicit `--config` plus upward discovery of `memory-context-intelligence.config.json`, applies source-class and historical-shard limits before `intake → signals → present`, keeps explicit narrow runs narrow when config requests same-day widening, exposes policy-limited provenance through later layers, and lets the public analysis surface emit advisory guided config questions when no config file is loaded.

The later full-power method remains gated. The runtime does not start public `review`, public `packet`, `/additional/` mutation, install, publication, or main RULES mutation from this first-response layer.

## 9) Fit with future implementation

The runtime UX should preserve the same order:
- present list first in normal response text
- present choice input second
- allow the user to adjust output mode interactively without skipping the topic-list stage
- use the chosen topic to drive the next deeper packet
- run the same full-power evidence-backed distillation method for the chosen topic
- if the chosen topic needs broader fact support, enrich the packet with focused research before presenting the stronger proposal
- use native agent lanes to gather or review evidence when the scope is broad enough to benefit from delegated work

---

> Full history: [../changelog/changelog.md](../changelog/changelog.md)
