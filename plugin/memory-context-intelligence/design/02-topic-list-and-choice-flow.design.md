# Topic List and Choice Flow

## 0) Document Control

> **Parent Scope:** memory-context-intelligence plugin-local governed design chain
> **Current Version:** 0.1.90
> **Session:** 08244912-a195-4926-84e6-8c202c667ba5 (2026-11-10)
> **Parent Design:** [design.md](design.md)

---

## 1) Goal

Define the user-facing analysis flow for this capsule so that it analyzes bounded historical memory evidence, lifts weak/raw incidents through doctrine/mechanism lenses, presents doctrine-level proposed improvement topics first, and only then asks the user to choose which topic to expand.

## 2) Required interaction contract

The flow must be:

1. after fileless startup, Claude interprets the slash text, retains output intent and asks only for missing period/topic-target choices; prepare only after resolving a 1–14-calendar-day interval including today, with configured narrowing inside it, and report complete-prefix/remaining coverage without claiming selected days are complete
2. the main session discovers observed mechanisms from canonical intake `topic_discovery_evidence` before consulting generated titles/ranks; when independent perspectives and permitted caller tools justify it, workers add candidates, otherwise local semantic discovery still runs
3. fan in local semantic candidates, advisory deterministic seeds, and worker suggestions; verify cited producer-owned trace references against the same content projection
4. apply the full eligibility gate to the combined set, including semantic deduplication, before deepening or presentation
5. after fully analyzing a progressive batch, explicitly acknowledge `analyzed` or successful `no-topics`; only then may catch-up prepare its next batch. Present only eligible improvement topics, deduplicated across the invocation; zero eligible topics is valid
6. after the list is visible, keep the slash invocation itself as the active request even when no extra text was supplied
7. after the topic cards, render one compact advisory next-action bridge that keeps topic selection and direct follow-up choices visible
8. expand only the chosen eligible topic into deeper concept/matrix/design output
9. do not mutate RULES directly from this flow

พูดง่าย ๆ: ต้องโชว์รายการหัวข้อก่อน แล้วค่อยให้ user เลือกทีหลัง แต่รอบนี้รายการหัวข้อควรมาจาก broader historical work patterns เป็นค่า default ไม่ใช่ล็อกที่ current session ก่อนเสมอ

### Guided invocation

The command already has one purpose, so do not ask users to select a purpose or learn mode jargon. Before corpus/progress acquisition, ask only for missing choices in one question/choice dialog: period **1, 3, 7 or 14 calendar days** and Topic target **No minimum, 3, 5 or 10** (custom values allowed). Other explicitly selected integer durations within 1–14 days are valid. Preserve period/count/language/filters across turns; if only one value is missing, ask only that value. An unavailable dialog falls back to a concise text question, not guessed defaults.

Count today as day1, show inclusive start/end dates, and freeze the invocation date for continuation. Missing calendar days do not authorize older input. Requests exceeding14 days or conflicting with an explicit/configured day require correction before reading, not silent clamping or dropping restrictions. A period/count choice alone selects one batch; only an explicit request to read the entire selected period selects bounded catch-up. Minimum count never guarantees output, weakens eligibility or authorizes extra dates/batches. Runtime enforcement belongs to [07](07-recall-scoping-and-time-window.design.md).

### Natural-language request interpretation

`ARGUMENTS` is the Skill's input-text carrier, not a requirement for CLI syntax or permission to treat every word as a literal search. Claude understands the whole sentence and context before acquisition. Keep topic-count targets, subject, language, detail and depth as invocation-local analysis/output instructions; send only the user's actual day/session/lookback/text restrictions, config and execution mode to the existing runtime. A subject such as RULES does not itself require matching that word in a trace. After the run choices resolve, prepare with the selected `--window-days` and frozen `--current-day`; with no additional retrieval controls, use an explicit empty `--arguments` value. Config/source policy may narrow, never extend, that interval.

For example, `Minimium Rules 5 topic` retains the five-topic target and asks only for the missing period, not a search for that sentence. The same count request with a chosen period and explicit date retains the count and transmits the calendar controls plus that in-range date restriction. An explicit request for traces containing `timeout` retains that genuine literal filter. Natural-language catch-up intent selects the existing catch-up mode; a count/depth target alone does not widen acquisition, change batch budgets or authorize filler topics. Beyond the missing run choices, ask only when an unsupported or materially ambiguous constraint prevents faithful scope selection. Existing eligibility and caller-acknowledged completion remain binding; runtime serialization/safety belongs to [07](07-recall-scoping-and-time-window.design.md). No phrase-whitelist parser, new config or durable intent state is introduced.

### 2.0.1) Topic eligibility and novelty gate

A signal or generated card is only an internal candidate. Before adaptive deepening or presentation, every candidate must pass each check:

1. **Trace-to-claim entailment:** inspect the bounded source-backed trace text for the candidate. It must support the specific alleged problem. Generated titles, keywords, scores, confidence labels, signal IDs, generic before/after templates, and a general evidence count cannot substitute. Plans, precautions, compliant actions, hypotheticals, missing/truncated evidence, or evidence that does not establish the claim are suppressed; do not retrieve more evidence to rescue or strengthen that rejected candidate.
2. **Active RULES novelty:** identify the analyzed project's active root and inspect the relevant active RULES owner, not only sampled `governance_context`. Suppress topics whose principle or behavior is already covered, including a trace that appears to violate that rule; analysis does not re-propose covered doctrine as a regression topic.
3. **Completed-work novelty:** follow active phase/TODO navigation and compare the candidate's behavior, mechanism, and output with the actual delivered outcome at its checked proof layer. Suppress matching delivered outcomes, not merely similar titles or a completed topic-filtering system. Phase075 completion establishes its eligibility infrastructure, not resolution of every later candidate. A genuinely distinct residual delta still needs trace support, checked unfinished outcome, and active-RULES novelty; possible material matches that cannot be settled remain fail-closed.
4. **Candidate-set deduplication:** compare meaning across candidates and retain at most one per principle, behavior, or outcome.
5. **Fail closed:** suppress if the active root/owner or relevant completion state cannot be checked, or if a material semantic match remains ambiguous.

When every candidate is suppressed, distinguish unsupported evidence from active-rule coverage, completed work, duplicate candidates, or an unresolved check. Do not mislabel suppression as insufficient trace repetition. The first-response analysis remains read-only for corpus/governance/candidate artifacts and never mutates RULES; its only state-writing exception is MCI-owned pending/completed progress, not topic acceptance or promotion.

#### 2.0.2) Parallel candidate discovery before eligibility

When multiple distinct trace-backed evidence axes exist and independent caller-session subagents are available, provide every worker the same bounded, privacy-minimized `topic_discovery_evidence` projection from the existing intake. The projection is not automatically redacted: remove personal data, credentials, private paths/hosts/endpoints, and unrelated payload details before dispatch, and omit an excerpt if sanitization would destroy its evidentiary meaning. Each excerpt carries a run-local reference for leader verification. The three optional lenses are Developer/process, Security, and Architect; each may return zero candidates. Do not launch discovery when one meaningful axis remains, excerpts are insufficient, or the caller cannot keep worker tasks bounded to the supplied evidence.

The main session first discovers observed mechanisms from canonical intake content, then verifies every cited excerpt, combines local semantic candidates and worker suggestions with advisory deterministic seeds, and applies the unchanged eligibility checks in §2.0.1—including semantic deduplication—to the combined set. No-worker discovery remains active; seed scores/confidence/breadth cannot be copied to a different semantic evidence basis. Workers are instructed not to acquire trace data, decide novelty, deepen candidates, or write. Candidate discovery is distinct from Phase 012's in-process simulated lane findings, Phase 069 adaptive deepening, and Phase 076's explicit older-window scan. Agent Teams are conditional caller-session tooling and do not become a package dependency or setting change.

### 2.0.3) One explicit supplemental search for new topics

Skill preprocessing executes only fileless `analysis-surface --startup`; the caller interprets the natural-language request, binds only requested retrieval controls and performs initial preparation explicitly. Normal incremental/catch-up payloads intentionally expose no `next_older_than_day`; their continuation is the acknowledgement-bound progress path in [07](07-recall-scoping-and-time-window.design.md). The older-than path remains an explicit stateless inspection, never implicit default progress. The supplemental command is an ordinary shell template, not an executable context-injection block: the caller runs it only after checking the explicit request and scope, replacing the date placeholder with the actual `YYYY-MM-DD` value from the initial payload. A prose condition cannot defer an executable injection block because the harness runs injection before Claude receives the instructions.

A user request for additional/different topics authorizes one bounded supplemental scan only when the original candidate set does not meet that request. The analysis surface reports the exact daily shards in its first bounded window and, only for a historical-default run with trace evidence enabled and no explicit narrowing, the next available boundary as `analysis_window.next_older_than_day`. The internal supplemental path selects shards strictly older than that batch boundary but still inside the original calendar interval. It carries forward the frozen day/window and same explicit config path, applies the same shard/record/character/byte and source-class limits, and returns a new candidate set from those records. At the interval's start no older boundary is offered.

The supplemental scan is a new candidate-discovery operation, not a repeat of the prior run and not additional evidence to rescue a rejected candidate. The skill must process no more than one supplemental window for an explicit request, perform local semantic discovery on the new content before concluding, compare candidates against all previously examined meanings, and apply the full eligibility gate before deepening or display. Re-reading rule coverage or Phase075 history cannot stand for this fresh evidence pass. Report selected/read/sampled scope and actual attempted/used status, not candidate suppression as proof of completed discovery. It does not run by default for a slash invocation or an ordinary no-topic result. It cannot widen an explicitly narrowed or policy-limited scope, and it is unavailable if configured source policy disables `trace_evidence`. Output identifies the exclusive boundary, exact checked days, attempted/used state, and intake status; if unavailable, preserve the intake reason and do not report the supplemental window as used. Report whether candidates were produced or suppressed; an empty or ineligible bounded window is not evidence that the remaining corpus has no topics.

## 2.1) Selected memory-input contract

The selected design **is** broader historical analysis by default, but still bounded.

Before topic-list presentation, `/memory-context-intelligence:analysis` should use this scope model:
1. current project collection only
2. oldest unprocessed historical records inside the chosen 1–14-calendar-day interval in bounded chronological batches
3. repeated historical trace may surface topic candidates without requiring current-session trace as the primary gate
4. current-session evidence becomes supporting provenance/freshness context when present
5. explicit narrowing such as `day=YYYY-MM-DD`, `session=<id>`, or `lookback=<minutes|hours>` remains available when the operator wants it

Design defaults:
- default project scope = current project collection only
- historical scope = the explicitly chosen recent calendar interval including today; batch acquisition stays bounded and plain incremental stops after one completed batch
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

Before preparation, show only the missing-choice dialog. Once preparation and eligibility finish, show the topic list with short descriptions, short why/impact wording, and a recommended first topic when one is materially stronger. Briefly distinguish the selected date interval from the batch actually analyzed and remaining input.

The first output layer must:
- frame the result as a design-grounded RULES/workflow review surface, not as a generic recurring-pattern summary
- present topic candidates directly as doctrine-level historical work-pattern review topics
- rewrite titles into semantic human-readable titles rather than exposing raw slug/token-bag wording
- keep top-level topic names at RULES/workflow principle or mechanism level rather than incident-level issue wording
- keep incident details such as `404`, `python error`, or similar case examples inside proposal evidence/examples or provenance instead of the title
- render zero or more eligible topics; never add filler cards to reach a target count
- only retain one candidate for a shared principle, behavior, or outcome, even when titles differ
- do not present candidates already covered by applicable active RULES or already delivered in checked completed work
- the slash invocation itself must count as the request even when the user provides no extra text after `/memory-context-intelligence:analysis`
- when rendered analysis context exists, the first response must not fall back to a generic `no request` answer and must instead render the corresponding `available`, `blocked`, `dormant`, or `no-topics` state
- render only eligibility-approved topics as repeated topic cards, with zero topics allowed when none pass
- each surfaced topic must keep the same repeated presentation pattern so the user can compare the full displayed set without reading a wrapper report first
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
- when `adaptive_deep_analysis.deepening_required` is true, complete the eligibility gate first, then run one bounded deepening pass only for eligible topic ids named in `adaptive_deep_analysis.required_topic_ids` before rendering; rejected candidates are never deepened
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

### Collective post-analysis synthesis

After analysis and any user-selected refinements, `/memory-context-intelligence:summary` compares the complete accessible Topic set and user purpose, forms provisional mechanism families/criteria, researches public alternatives and counterevidence, and revises transferable principles/strategies/practice into an integrated method. [Post-Analysis Principle Synthesis](10-post-analysis-principle-synthesis.design.md) owns this manual advisory contract, permitted caller-session public tools, source/history separation, comparison/revision, privacy/failure limits and complete Topic disposition.

This is a separate advisory response, not a replacement for initial repeated Topic cards or a combined packet/additional artifact. It consumes available evidence without starting another memsearch/corpus run; analysis acquisition requirements remain unchanged. Missing or ambiguous input gets a bounded clarification, not invented mechanisms. Invocation does not authorize file creation, additional emission or Main promotion.

### Post-presentation selected-topic follow-up

The initial `/memory-context-intelligence:analysis` surface remains proposal-first and advisory, with corpus/governance/candidate artifacts read-only and only MCI pending/completed progress writable. It must not parse topic-selection wording as an analysis-scope mutation or perform an additional-stage write during the first-response flow.

After the topic cards are visible, a later explicit user instruction may select one or several topics for additional-stage trial creation. When that follow-up is clear, the assistant should apply one deterministic workflow instead of asking the user to choose internal routing, template, collision, or source-sync options that already have governed defaults.

Selected defaults:
- preserve every existing additional-stage artifact unchanged
- create one new semantic file per selected topic
- use the rich standalone trial-rule schema owned by `05-additional-staging-and-promotion.design.md`
- normalize evidence into self-contained doctrine under the contract owned by `08-memory-evidence-source-model.design.md`
- use the user-runtime additional-stage namespace for `memory-context-intelligence`
- preflight all selected filenames and destinations before writing
- refuse collisions and do not offer an overwrite path in the normal selected-topic workflow
- keep initial analysis, additional-stage selection, and later Main RULES promotion as three distinct states
- record explicit state equivalent to `selected_for_additional_trial=True` and `main_rules_promotion_approved=False` after the user selects trial creation
- set additional-stage selection without implying Main RULES promotion approval
- if several topics are selected, process them as independent one-topic packets/artifacts rather than a combined file

A follow-up question is justified only when the user-selected topics, intended owner, destination, or collision state remains materially ambiguous. The assistant should not ask preference questions merely to expose internal implementation choices when one governed safe continuation already dominates.

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
