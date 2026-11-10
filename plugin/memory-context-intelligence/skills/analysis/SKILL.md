---
name: analysis
description: Use when the user wants analysis of real work evidence, anchored by memsearch-backed traces and optionally strengthened by durable memory or governance context, so Claude can propose RULES or workflow improvement topics in a proposal-first format.
version: 0.9.42
---

# Memory Context Intelligence Analysis

This skill has one checked registered analysis slash surface:
- `/memory-context-intelligence:analysis`

Checked current bare-alias state:
- bare `/analysis` is not present in checked slash-command registry output
- checked approved non-interactive local invocations of `/memory-context-intelligence:analysis` now return operator-facing output when local command approval is intentionally granted with `--permission-mode bypassPermissions`
- plain no-approval print-mode is not used as proof because this slash surface needs a local command run
- do not treat bare `/analysis` as proved current runtime behavior in this wave

Historical-default contract for this surface:
- default mode: incremental, oldest unprocessed trace within the selected calendar window first; progress is MCI-owned and separate from Memsearch
- scope: broader historical memory across the user's work corpus, limited to the chosen 1–14 calendar days including today; no unbounded historical default
- current-session evidence becomes supporting/provenance context, with freshness value when present, not the primary scope owner
- historical recurring patterns may surface topic candidates from repeated historical trace without requiring current-session trace as the primary gate
- explicit narrowing such as `day=YYYY-MM-DD`, `session=<id>`, or `lookback=<minutes|hours>` remains available when the operator wants it
- do not default to same-day-only or current-session-only recall anymore
- keep the first response as a design-grounded, historical-first RULES/workflow review rather than a session-local trace-pattern summary

Current implemented evidence model for this surface:
- `trace_evidence` remains the live pattern anchor
- `recall_evidence` sharpens exact wording and retrieval detail when memsearch-backed recall is available
- `durable_memory_context` can come from `MEMORY.md` and relevant path-scoped Claude memory files
- `governance_context` can come from checked RULES/design/changelog/TODO/phase/patch surfaces in scope
- durable memory and governance context can strengthen a candidate, but they must not replace missing live trace proof
- source mix should stay visible when durable memory or governance context materially shaped a candidate
- the analysis path now also supports bounded config-policy loading: explicit `--config` or the default user-scope config at `~/.claude/memory-context-intelligence.config.json` may limit source classes, cap historical shards, and request same-day widening only for non-explicit runs
- when config policy narrows the run, `source_policy` should stay visible so the operator can see that the evidence scope was intentionally limited
- `/memory-context-intelligence:init` is the setup companion surface for guided config creation/update when the operator wants question/choice dialogs instead of raw-arg setup

Deferred / non-public command ideas in this wave:
- `/memory-context-intelligence:review`
- `/memory-context-intelligence:packet`
- do not present them as active public commands

## Checked analysis context

```!
"${CLAUDE_PLUGIN_ROOT}/bin/memory-context-intelligence" analysis-surface --startup
```

User arguments: $ARGUMENTS

Startup only locates the available project input and returns `awaiting-caller-scope`; it does not acquire evidence or create pending progress. Interpret the request below before using its `preparation_command`. This caller-driven preparation is the only initial intake. If startup or preparation fails or is unavailable, report the actual blocker without topics or completion.

## Choose the run window before preparation

This command already has a clear purpose: discover eligible RULES/workflow Topics from work history. Do not ask the user to choose a purpose or learn internal mode names. After interpreting the supplied sentence and conversation, ask only for missing choices using `AskUserQuestion` question/choice dialogs before preparation:

- **Period:** offer **1, 3, 7 or 14 calendar days**, counting backwards from the invocation date **including today**. Other explicit durations from 1 through 14 days are valid too. There is no automatic 14-day scan; wait for a period choice when missing. A missing calendar day does not authorize reaching further back.
- **Topic target:** offer **No minimum**, **3 Topics**, **5 Topics**, or **10 Topics** when no target has been given. A custom target is valid. This is a desired eligible count, not guaranteed output or authorization to read more.

Ask both missing choices together in one compact dialog; when only one is missing ask only that one. Preserve answers across turns and retain already supplied period, topic target, language and genuine filters. Do not ask again on every reply or batch. If dialogs are unavailable, ask the same short questions in text and wait. No corpus/progress acquisition occurs while a choice is unresolved.

Resolve the invocation date from checked current-date context, show the inclusive start/end dates briefly, and call preparation with `--window-days <chosen-days> --current-day <invocation-date>`. These are internal controls, not syntax users must learn. Dates stay frozen for continuation even across midnight. A request exceeding 14 days, an older explicit day outside the chosen window, or conflicting constraints requires a corrected choice before reading; never silently clamp, drop a restriction, or widen scope. Do not use rolling-hour `lookback` as a substitute for calendar days.

Plain analysis prepares one bounded batch inside the chosen period. Only an explicit request to read the whole selected period selects catch-up, still within that period. A period choice or topic target alone does not select exhaustive analysis. Always distinguish the selected date range from the actually analyzed batch and its remaining input; never resume an unrestricted historical run or reset/acknowledge its pending batch when selecting a new window.

## Interpret the user request before preparation

`User arguments` are natural-language instructions to Claude, not a retrieval filter. Understand the whole sentence and conversation context, including Thai/English wording and ordinary typos; users need no special argument syntax. Claude owns this interpretation; Python receives existing retrieval controls, not a phrase whitelist or a new natural-language parser.

1. Keep the desired topic count, language, detail and analysis depth in the caller's working context for discovery and presentation. A requested subject can guide semantic analysis without requiring that exact wording to appear in a trace. These instructions are not text-search terms.
2. Identify only the requested evidence restrictions and execution mode. Translate supported natural-language restrictions into existing runtime forms; preserve explicit day/session/lookback, literal text filters, config and mode. Resolve relative dates from checked date/time context. If an unsupported or materially ambiguous retrieval constraint would change the selected evidence, ask one bounded clarification before preparation; do not drop it or guess a broader scope.
3. Call the returned `preparation_command` with `--arguments` containing only the interpreted retrieval controls. Use existing `day=`, `session=` and `lookback=` forms and existing config/mode options internally. Include free text only when the user actually requests a literal text filter, preserving its requested value. Shell-quote every value; quoted text must remain data, never executable substitutions. If literal text collides with control syntax and cannot be represented faithfully, stop for clarification rather than reinterpret it as a control.
4. After the period and topic target are resolved, pass `--arguments ""` when no additional retrieval controls are requested, alongside the selected `--window-days` and frozen `--current-day`. Config/source policy may narrow this window but cannot extend it; retain the user's output instructions for the subsequent analysis. Do not forward the raw sentence, require the user to rewrite it as options, assume an exported `ARGUMENTS` variable, or interpolate user text into an executable injection fence.
5. A requested minimum is a target, not permission to invent, duplicate, revive rejected topics, weaken eligibility, widen scope or switch to catch-up. Analyze the complete authorized batch and report the actual eligible count and any shortfall. Explicit natural-language catch-up intent selects that existing mode; count or depth requests alone do not. Completion still follows semantic analysis and eligibility, never interpretation/preparation alone.

Example: `Minimium Rules 5 topic` asks for at least five RULES improvement topics. Keep that target and ask only for the missing period. After the user chooses 7 days, prepare using `--window-days 7 --current-day <invocation-date> --arguments ""`; do not search for that sentence or for the word `Rules`. If a specific day is also requested, retain it as an additional restriction inside the selected period. If the user explicitly asks to filter traces containing `timeout`, that literal is a real retrieval filter.

Internal serialization examples after interpretation: add the mandatory `--window-days <chosen-days> --current-day <invocation-date>` to every preparation. An explicit session plus literal filter uses `--arguments 'session=run-42 timeout'` (one argument value); explicit catch-up uses `--arguments "" --mode catch-up` within that same period. Add a selected config separately as `--config <shell-quoted-path>`. These are caller-generated controls, not syntax the user must learn. The `session=` control inside `--arguments` is the requested evidence session; the separate `--session-id` option is caller provenance, not an evidence filter. Preserve every selected restriction together and keep unsupported combinations blocked rather than dropping a restriction.

The prepared analysis context emitted by this runtime wrapper includes field-level evidence surfaces such as `source_classes_present`, `source_scope_label`, `source_mix_label`, `historical_strength`, `latest_seen`, `current_session_confirmation`, repeated `topic_cards`, and config-related surfaces such as `source_policy`, `config_questions`, and `suggested_config_path` for the operator-facing result.

## Default first response contract

When invoked for normal operator use:
- if choices are unresolved, the first response is the compact missing-choice dialog above, not a result or a config-setup detour
- after preparation, rely on the rendered memsearch-backed analysis context as the primary checked evidence source
- treat `/memory-context-intelligence:analysis` as the checked registered analysis slash surface in current runtime
- the slash invocation itself is the request, even when the user provides no extra text after `/memory-context-intelligence:analysis`
- do not answer that there is no request when the rendered analysis context is present; render the corresponding `available`, `blocked`, `dormant`, or `no-topics` state instead
- do not present bare `/analysis` as proved current runtime behavior in this wave
- do not present `review` or `packet` as active public commands
- do not default to package-map explanation, governance-map explanation, or internal pipeline narration
- do not summarize ongoing implementation work, doc sync, phase progress, or proof status in the first response
- ignore ambient session progress context unless the user explicitly asks for development status instead of analysis output
- treat the first response as a design-grounded RULES/workflow review of broader historical work patterns rather than a session-local trace summary
- keep historical-first as the default scope basis
- preserve provenance explicitly enough that the user can tell whether the proposal is historical-only or also current-session-confirmed
- when the runtime payload says no config file is loaded, surface the guided config helper from `config_questions` instead of expecting raw args as the normal UX path
- expose `suggested_config_path` when present so the operator can see where the user-scope default config file would live
- keep that guided config helper advisory only; it helps the operator choose config defaults, but it must not be treated as an approved write or automatic config mutation
- when `source_policy` says a config file was loaded, keep that policy-limited context visible enough that the operator can tell whether source classes, historical shard count, or same-day widening defaults narrowed the run
- if config policy disabled `trace_evidence` or left only context-only sources in scope, do not let the response overread that run as a promotable live candidate

## Incremental progress and explicit catch-up

A plain invocation prepares one oldest-unprocessed contiguous batch inside `analysis_window.calendar_window`. The selected 1–14-day interval is the whole run's date boundary, while shard/record/character/byte budgets cap each batch and may stop inside a day. Source coverage identifies the exact complete batch, not the whole selected day or period. Missing dates are not replaced by older dates. Explicit `day=`, `session=`, `lookback=` or text-filter inspection and configured narrow defaults remain non-advancing and inside the same interval; source-policy and calendar-window identities isolate progress from legacy unrestricted runs. Corpus and governance inputs remain read-only. Only MCI's own `~/.claude/memory-context-intelligence/progress.json` is written for pending/completed progress; no Memsearch index/config or Main RULES write is authorized.

When the payload has `progress.batch_id`:

1. Read every canonical excerpt in the prepared batch, perform local semantic discovery and any justified optional viewpoints, and finish the eligibility checks below. Do not treat deterministic `no-topics`, wrapper exit zero, file reading, preparation or generated seeds as semantic completion.
2. After the batch is fully analyzed, invoke the returned `progress.completion_command` through the caller's shell tool. Its `--outcome analyzed` means the analysis completed; replace only that outcome with `no-topics` when the completed analysis yielded zero eligible topics. It is not topic acceptance, approval to emit an artifact or Main promotion. The caller attests completion; Python does not independently verify the model's reasoning.
3. Check the command's structured result and exit status. Only `completed` or matching `already-complete` is acknowledgement. Never acknowledge an unread, incomplete, failed or interrupted batch. For a known analysis failure, `--outcome failed` clears only that pending preparation and does not advance completed progress. If a command outcome is unknown, inspect existing MCI state rather than claiming advancement or replaying blindly.
4. In default incremental mode, stop after this one batch. Show eligible Topic cards (or the honest zero-topic result) and a compact progress/remaining note. No eligible topic is still successful completed analysis, not a trigger to manufacture topics or read extra history.
5. For an explicit `mode=catch-up` invocation, after successful acknowledgement follow `progress.continuation_command` through the same ordinary shell tool while `progress.remaining` is true. Analyze and acknowledge each new batch before requesting another; keep the original run endpoint, frozen calendar window and invocation date, and do not invoke the public Skill recursively. Stop on blocked/error/interruption; a later new invocation resumes only completed progress. Input appended after that endpoint waits for a new invocation. Deduplicate eligible topics across this invocation without keeping raw batches in a durable ledger; if caller context cannot safely retain the selected output, report the completed boundary and stop rather than claim the rest analyzed.

Completion and continuation commands are payload-bound runtime commands, not additional executable startup fences. Do not synthesize batch IDs, cursor positions, run IDs or a successful acknowledgement. `caught-up` means no unprocessed input remains through that invocation endpoint, not that all possible improvement topics were found. A changed prefix or corrupt/stale state stays blocked with its reason; do not reset, overwrite, skip it or widen scope automatically. Budgets too small for one complete record require a deliberate larger bounded budget or a completed source append, not truncation-as-completion.

## Local semantic discovery before generated seeds

Use `topic_discovery_evidence` canonical `content`, not the 220-character display preview. The main session reads these already-collected excerpts before consulting generated titles or ranks and discovers supported decision mechanisms, including when parallel workers are unavailable or skipped. A deterministic `no-topics` result is not a semantic discovery conclusion when usable trace excerpts remain; `blocked` or `dormant` intake does not authorize acquisition or promotion.

- For each supported candidate keep the observed behavior → mechanism → consequence → specific proposed residual gap together, with cited producer-owned run-local excerpt references and material uncertainty/counterevidence. Authored before/after proposals are interventions, not proof of historical occurrence. Plans, precautions, compliant actions and hypotheticals do not prove an alleged defect.
- Compare the meaning of excerpts: distinct Thai or English mechanisms remain distinct, while the same mechanism with different wording is one candidate. Do not force evidence into a generic workflow/evidence/approval title. Name the supported mechanism after understanding it.
- Only then compare with deterministic cards as advisory seeds, not a closed topic catalog. Verify their `evidence_refs` against the canonical excerpts; do not inherit unrelated seed scores, confidence, or recurrence. The worker projection omits private source metadata: claim cross-session/day breadth only when the candidate's actual evidence basis has matching checked provenance, not from an unrelated seed or sample-wide coverage.
- Read `analysis_window.coverage` to distinguish selected, read, and sampled days, empty/unreadable/byte-limited days, unsampled material, and content truncation. Explicit non-advancing inspection is bounded sampling, not all-record coverage. Incremental coverage describes only the complete contiguous batch before its cursor; a day may remain unfinished. Missing or truncated decision evidence cannot be invented or recovered from generated previews.

## Parallel viewpoint discovery before the eligibility gate

The `signals` command creates deterministic local candidates; its in-process lane findings are not spawned workers. The analysis payload includes `topic_discovery_evidence`, a bounded projection of canonical trace content from the same intake with run-local excerpt references. Local semantic discovery remains the baseline; optional workers add independent perspectives. When that evidence supports multiple independent viewpoints and caller-session subagents are available, use caller-session subagent tools to launch one independent read-only subagent per useful perspective, concurrently, capped at three, before the eligibility gate. Skip any perspective that lacks a distinct trace-supported question. This is candidate discovery, not deepening of already-ranked topics, another intake, or proof that more or better topics will result.

- Brief workers to use only the supplied excerpts. Give each worker the same privacy-minimized set of actual bounded trace excerpts from `topic_discovery_evidence`; preserve each run-local excerpt reference so the main session can verify the claim against the same excerpt. The projection is bounded but is not automatically redacted: remove personal data, credentials, private paths/hosts/endpoints, and unrelated payload details before dispatch. If sensitive details cannot be removed without losing the trace claim's meaning, omit that excerpt from the worker packet. Do not include generated titles/ranks or prior generated interpretations in the worker packet. Workers must not invoke file, shell, memsearch, web-research, or write tools during discovery. If a worker needs more evidence or the supplied excerpt cannot support a claim, return zero candidates; do not retrieve or infer supporting history. Do not give workers ambient corpus access, ask them to widen or repeat the selected window, or provide full transcripts.
- Use three non-overlapping lenses: **Developer/process** looks for trace-supported recurring implementation or workflow friction; **Security** looks only for explicit trace-supported security, privacy, or safety gaps, not hypothetical violations; **Architect** looks for trace-supported ownership, state, integration, or dependency problems. Each worker may return zero candidates. Require every result to name its run-local excerpt reference, the specific alleged gap it supports, and material counterevidence or uncertainty. Worker output is evidence input, not authority.
- The main session owns fan-in. Combine worker suggestions with local candidates and verify each cited excerpt and claim against the referenced entry in `topic_discovery_evidence`; apply the complete eligibility gate to the combined candidate set, including semantic deduplication, before any deepening or presentation. Suppress unsupported, covered, completed, duplicate, or materially unresolved candidates; do not rescue a rejected candidate by changing its wording. Parallel discovery does not create `required_topic_ids` or make a candidate an automatic deepening target.
- Run this only when multiple independent evidence axes can be investigated and the likely breadth benefit earns coordination cost; skip parallel discovery when only one meaningful evidence axis remains or the excerpts are insufficient. If the caller cannot keep discovery workers within the excerpt-only boundary, skip parallel discovery. If parallel subagents are unavailable, continue with the bounded local candidates discovered semantically above and state that parallel discovery was unavailable when it was material to the requested analysis. Respect explicit no-agent/model-call restrictions and keep this local discovery active; availability is not permission. Do not describe sequential/in-process lane summaries as parallel agent execution.
- Agent Teams are experimental. Use a Team only when Team capability is available and enabled in the caller's interactive session and shared coordination or peer challenge is materially useful; otherwise prefer independent subagents. Do not enable Agent Teams or change settings, and do not ask the operator to enable them for this analysis.
- This step does not change the one-pass supplemental-search contract below. It never performs another corpus scan to feed workers; any already-authorized supplemental window remains a separate new candidate set subject to the same evidence, deduplication, and eligibility requirements.

## Eligibility gate before presentation

A generated card is only an internal candidate. Before rendering or deepening any topic, pass each one through every check below. The output may contain zero topics.

1. **Trace-to-claim entailment:** inspect the actual bounded trace text in the candidate's cited canonical `topic_discovery_evidence` entries. `Evidence examples` are display previews; use their matching producer references to check canonical content, not the preview alone. It must support the specific problem the topic claims occurred. Titles, signal IDs, keywords, scores, confidence labels, generated before/after text, and a general statement that evidence exists do not prove the claim. If the trace is a plan, precaution, compliant action, or hypothetical rather than evidence of the alleged problem, suppress the candidate. If usable source text is missing, truncated at the decision point, or too weak to establish the claim, suppress the candidate; do not retrieve more evidence to rescue or strengthen that rejected candidate.
2. **Active RULES novelty:** identify the current analyzed project's active root and applicable RULES owner from checked project context. Search and inspect relevant active rule files for the same principle or semantically equivalent behavior; do not rely only on the limited `governance_context` samples embedded in the payload. If the active owner already covers the principle, suppress the candidate. A trace that appears to violate an existing rule is still suppressed; do not re-propose the covered principle as a regression topic.
3. **Completed-work novelty:** inspect the active phase/TODO navigation and relevant referenced completed work; compare candidate behavior, mechanism, and output with the delivered outcome at the same checked proof layer. If the same behavior or outcome is already recorded as delivered, suppress it. A similar title alone is not enough to classify work as completed. Phase075 completion proves the eligibility infrastructure, not that every later candidate was fixed; a genuinely distinct residual delta still needs trace support and active-RULES novelty. A possible material match that cannot be settled remains fail-closed.
4. **Candidate-set deduplication:** compare the remaining candidates by meaning, not only by title. Keep at most one when multiple cards express the same principle, behavior, or outcome.
5. **Fail closed:** if the active root/owner cannot be identified, relevant active RULES or completion state cannot be checked, or a possible match remains materially ambiguous, suppress the candidate rather than assuming novelty. Keep the explanation brief and do not disclose or restate suppressed topic titles.

Do not treat `available`, a high score, historical repetition, or adaptive-deepening selection as an override for this gate. The gate is a final display-eligibility check over bounded candidates; it does not authorize writes or an automatic corpus acquisition.

### One explicit fresh search for different topics

A rejected candidate and a new candidate search are separate decisions. When the user **explicitly asks for additional or different topics** and the current candidates do not satisfy that request, inspect `analysis_window.next_older_than_day`. If it contains a day, run one bounded supplemental historical scan—exactly one supplemental analysis pass—using the same analysis surface and pass `--arguments ""` so the request text cannot accidentally become an intake filter:

```bash
"${CLAUDE_PLUGIN_ROOT}/bin/memory-context-intelligence" analysis-surface --arguments "" --older-than-day "<analysis_window.next_older_than_day>" --window-days "<analysis_window.calendar_window.days>" --current-day "<analysis_window.calendar_window.end_day>"
```

This is a command template, not startup context injection. After the explicit-request and scope checks pass, replace `<analysis_window.next_older_than_day>` with the actual `YYYY-MM-DD` value from the first payload and invoke the command through the caller's shell tool. Never execute the literal placeholder or this supplemental command during skill preprocessing.

If the first analysis used an explicit config path, add `--config "<that same path>"` so the supplemental run preserves its source-policy limits. Copy the calendar controls from the first payload too. This reads only daily shards strictly older than every day in the first checked batch and still inside the original selected calendar window, through the existing bounded intake → signals → present path; it creates a new candidate set from that distinct evidence slice. Reaching the start date ends this option; never start a new or wider period to meet a topic target.

- Run this pass only for an explicit request for more/different topics; a plain `/memory-context-intelligence:analysis` invocation or a routine no-topic result does not trigger it.
- Do not repeat or widen the pass. `supplemental_pass_used: true` means intake completed for the bounded supplemental window; an unavailable or blocked intake is an attempted but unused pass and must not be retried without a material scope/access/policy change.
- First perform local semantic discovery on the new canonical evidence before concluding that the requested fresh pass found no eligible topic. Re-reading Recovery Contract, Scope, or Phase075 history is not fresh discovery. Then apply the complete eligibility gate above before any deepening or presentation. Compare against every candidate already examined and suppress any semantically equivalent topic; do not surface a previously rejected candidate under changed wording.
- The supplemental scan is for candidate discovery, **not to rescue or strengthen any previously rejected candidate**. Never relax trace, active-RULES, completed-work, deduplication, or fail-closed requirements.
- Honor the source policy and scope. If the first run was narrowed, `trace_evidence` was disabled, no older-than boundary is available, or the supplemental pass is blocked/unavailable, do not widen it; report the checked reason and the exact bounded-window limit.
- Read `analysis_window.exclusive_boundary_day`, `checked_days` (selected window, not all-record analysis), `coverage`, `supplemental_intake_status`, `supplemental_pass_attempted`, and `supplemental_pass_used` to report the exact bounded window, actual sampled scope and whether it ran or was unavailable; preserve the returned `reason` when blocked. Report whether fresh candidates were produced or suppressed. A bounded window with no eligible topic does not show that no topic exists in the rest of history; do not imply a corpus-wide search or absence.

- use semantic human-readable titles in the first response; do not leave the user with raw slug/token-bag titles
- the top-level unit of the default first response must be `Topic <n> — <human-readable title>`
- each surfaced topic must use the same repeated pattern format so the user can scan and compare topics directly
- the repeated topic cards must keep the same repeated pattern across Topic 1, Topic 2, Topic 3, instead of switching one topic into a different structural mode
- one topic must not be split across separate report-wrapper sections
- Do not use `Presentation`, `Recommendation`, `Proposal`, and `Related variants` as top-level blocks in normal operator output
- Do not split one topic across multiple sections
- do not merge several surfaced topics into one combined explanation block
- multiple topic cards stay comparison/advisory output only; any later packet/additional-stage flow must keep one selected topic per artifact and split into separate per-topic artifacts
- if one topic is stronger, mark it inside that same topic card as the recommended first topic instead of creating a separate recommendation wrapper section
- same-family weaker topics may still appear, but they should stay in the same repeated topic-card rhythm rather than being moved into a separate global variants wrapper
- repeated recap or summary blocks must be removed; each topic block should add topic-specific meaning rather than restating a global summary again
- the first response must not require a second manual rewrite pass; it should already read as native-first operator-facing output
- treat the analysis surface as adaptive deep-analysis when the rendered payload includes `adaptive_deep_analysis`
- all four internal evidence sources should be treated as the default internal evidence basis when the payload says they are enabled by default
- treat adaptive deep-analysis as subordinate to the eligibility gate: complete the eligibility gate before any adaptive deepening
- deepen eligible topics only; ignore `required_topic_ids` for candidates rejected by the eligibility gate
- when an eligible candidate recommends `subagent-assisted`, use a read-only subagent lane if the current runtime exposes subagent capability
- when an eligible candidate recommends `subagent+external-research`, use the read-only subagent lane plus web/external research if those tools are available in the current runtime
- if the required subagent or web/external research tool is unavailable, you must say so explicitly and keep the skipped deepening visible rather than silently skipping it
- do not silently skip required adaptive deepening
- subagent-assisted deepening should stay read-only and focus on clarifying mechanism, impact, source conflicts, and decision-ready intervention wording for the already-ranked topic
- web/external research enrichment is allowed only as a supporting layer after a trace-backed local topic already exists; it may strengthen principle/mechanism support, constraints, or trade-offs, but it must not replace local trace proof
- keep `trace_evidence` as the live promotion anchor even after adaptive deep-analysis, subagent-assisted deepening, or web/external research enrichment
- `trace_evidence` remains the live promotion anchor even when deeper analysis uses multiple internal sources and optional external support
- trace_evidence remains the live promotion anchor even when deeper analysis uses multiple internal sources and optional external support
- adaptive deepening before topic selection must not be treated as selected or approved; it remains advisory-only until the user chooses a topic or explicitly asks for a change proposal/goal draft
- multiple `required_topic_ids` may be deepened in one analysis pass, but any packet/additional-stage follow-up must still keep one selected topic per artifact and split into separate per-topic artifacts
- keep the topic-card output shape even after deeper analysis; deepen the evidence and mechanism inside the cards rather than replacing them with a new wrapper format

## Optional post-analysis principle synthesis

After the Topic cards and user-selected refinements, the user may invoke `/memory-context-intelligence:summary` for collective read-only synthesis of the full available set and their follow-up purpose. Its targeted public research develops alternatives/counterevidence, can revise the decision criteria, re-compares viable approaches when the frame changes, and explains what the research changed or left intact before integrating practical principles and complete Topic disposition. This is adaptive reasoning, not a fixed result template. It uses actually available caller-session tools, preserving local/history versus external support, privacy and unavailable/no-web limits.

The initial repeated Topic cards remain unchanged. Summary consumes existing material without a new memsearch run; public mechanism research is not a corpus rerun and does not authorize file creation, additional emission or Main promotion. Offer only a compact advisory option when relevant, not automatic invocation or a replacement for per-topic expansion/emission.

## Deterministic post-presentation follow-up contract

The initial analysis remains read-only and advisory for corpus, governance and candidate artifacts; its sole automatic local-state exception is MCI pending preparation and caller-acknowledged progress. Topic presentation, ordinary `choose`, and adaptive deepening do not authorize candidate file creation or Main RULES promotion.

Only when the user makes an explicit later selection of one or several `Topic N` values and asks to create or proceed with additional-stage trial material:
- create one independent packet and one standalone artifact per selected topic
- set `selected_for_additional_trial=True` on each independent packet
- keep `main_rules_promotion_approved=False`
- preserve `trace_evidence` as the live entailment anchor and normalize evidence into standalone doctrine without temporary memory, transcript, packet-report, raw path-line, or `content_preview` dependencies
- run one full-set preflight before any write across every selected packet and destination
- refuse the complete set on any collision, duplicate destination, unsafe path, symlink boundary, packet stop gate, or invalid standalone artifact
- preserve every existing destination byte-for-byte; there is no overwrite option, reuse, merge, rename, or replacement path
- use one rich standalone trial schema per topic and keep Main RULES mutation outside this workflow
- do not ask about template, routing, or source/runtime sync when these governed defaults apply
- ask only when topic identity, owner mapping, destination, collision resolution, approval, or another real safety boundary remains ambiguous

This explicit later follow-up writes only additional-stage trial material after the complete preflight passes. It does not mutate Main RULES, approve promotion, combine topics, or turn the initial analysis response into automatic execution.

If the rendered status is `blocked`:
- say directly that analysis is blocked
- state the memsearch/input reason briefly
- do not invent topics from current conversation context

If the rendered status is `dormant`:
- say directly that analysis is dormant because the memsearch input is stale
- do not invent fresh topics from stale input

If the rendered status is `insufficient` or `no-topics`, or every generated candidate is rejected by the eligibility gate:
- distinguish insufficient historical evidence from candidates suppressed as unsupported, already covered, completed, duplicated, or unverifiable
- do not claim that the historical pattern was insufficient when the actual reason is that no candidate passed the eligibility gate
- give one concise explanation of the checked suppression reason without repeating suppressed topic titles
- when the actual result is insufficient historical evidence, say that broader historical analysis did not find a sufficiently repeated pattern; keep that wording historical-first instead of treating current-session scarcity as the default explanation
- add one short actionable next step from the rendered `no_topics_message`, `no_topics_details`, or `recommended_next_step` only when relevant to the actual result
- if the strongest remaining signal is only a narrow historical pattern such as `2 trace / 1 session / 1 shard`, say that it is too narrow to count as broader historical review
- do not treat durable memory or governance context alone as enough to propose a live candidate
- do not fill the response with workflow explanation just to avoid a short answer

If the rendered status is `available` and `topic_cards` is non-empty:
- first apply the eligibility gate above to the full candidate set, then present only candidates that pass as doctrine-level historical work-pattern review topics
- Render zero or more eligible topics as repeated topic cards using one stable pattern, for example `Topic <n>` such as `Topic 1`, `Topic 2`, `Topic 3`
- Never add filler topics to reach a target count
- each topic card should carry its own short explanation, evidence/provenance line, status, and optional recommendation tag when it is the strongest topic
- broader multi-session/multi-shard patterns may inform evidence strength, but breadth never overrides the eligibility gate
- if a narrow historical pattern is the strongest remaining eligible evidence, say so directly instead of letting it read like broad historical proof
- keep any historical breadth summary to one short line only when it changes interpretation; do not let it become the main wrapper structure ahead of the topics
- keep provenance visible enough to distinguish `historical-only` from `current-session-confirmed` patterns
- top-level topics must stay at RULES/workflow principle or mechanism level rather than incident-level issue wording
- incident details such as `404`, `python error`, or similar case-level examples should stay inside proposal evidence/examples or provenance, not in the title
- include short why/impact wording
- surface compact source mix wording when durable memory or governance context materially shaped a candidate
- include provenance notes for each topic when they materially help the user judge the evidence boundary
- include a recommended first topic when one is materially stronger
- make it clear the proposals do not come from freeform conversation intuition or raw session-id query alone
- show each expanded proposal as `candidate only`, `advisory only`, and `not approved yet`
- every first-pass topic card must include a compact before/after preview through `Before behavior` and `After behavior`, even when no bounded preview record was captured
- those default first-pass before/after previews must stay compact, human-readable, and evidence-calibrated; they are there to help the user picture the change, not to overclaim that the current system always behaved exactly that way
- the live analysis wrapper should render the operator surface through `present --output-mode native-first` rather than leaving first-pass output to `auto` drift
- the wrapper should carry an inferred presentation language and keep Thai as the local fallback when no stronger recent-language signal is available
- `Evidence examples` must still appear only when usable bounded preview evidence exists
- when usable bounded record previews exist, expanded proposals should include concrete `Evidence examples`, `Before behavior`, and `After behavior` sections sourced from found data such as `signal.records[].content_preview`
- incident details must stay inside those proposal evidence/examples sections or provenance rather than leaking back into the title
- if usable bounded preview evidence is absent, do not invent generic case examples; keep the compact before/after preview but omit the evidence-example section
- long-form illustrative before/after belongs to the expanded follow-up layer after the user asks for deeper explanation or selects a topic
- every expanded proposal should still read like human-facing guidance and include sections such as `มันคืออะไร`, `อาการ/ปัญหา`, `ถ้าปรับแล้วจะดีขึ้นยังไง`, `หลักฐานที่ใช้`, and `สถานะตอนนี้`, with the richer example sections appearing only when real evidence exists
- known doctrine-level topics should not stop at Thai labels only; their explanation bodies should also restore richer Thai-native wording in the first pass instead of staying as English labels-only hybrids
- after the topic cards, render one compact advisory bridge titled `Next action options`
- this advisory bridge must stay after the topic cards, not before them, and it must not become a new wrapper that competes with the cards
- the advisory bridge should tell the user they can choose a topic number, type a direct request, or ask for deep thinking / websearch / webfetch before any adjustment
- do not treat next-action options as approved execution, automatic execution, or carry-forward approval
- keep the action bridge compact; it should close the loop from reading a candidate topic to choosing a safe next step without changing the topic-card doctrine
- when checked freshness evidence shows the current session started before the installed plugin update, add one advisory warning framed as `possible stale long-lived session`
- this is a temporary diagnostic safeguard only
- if slash behavior still differs from the installed source, tell the operator to restart this session and retry
- session-dependent no-response remains a bug
- the warning must not turn restart into the final fix
- do not let a single-session/single-shard historical-only pattern read like strong broader historical review in the first response

Only after the user chooses a topic or explicitly asks for internals may the response expand into:
- mechanism detail
- matrix detail
- packet shape
- rollout detail
- package map
- internal command flow

## Boundary conditions

Keep these boundaries:
- memsearch is required during analysis/refinement for this skill's full flow
- `bin/memory-context-intelligence` remains an internal implementation mechanism only
- do not claim plugin-managed auto-flow proof
- do not claim publication, external marketplace release, stable/broad production readiness, or main RULES promotion/mutation/merge beyond checked evidence
- do not touch `/additional/` behavior from this skill response alone
- do not imply that several selected topics can be emitted into one combined additional artifact; downstream packet/additional output must split into separate per-topic artifacts
- do not present candidate topics as already-approved RULES changes
- if memsearch-backed analysis cannot continue, stop at blocked/dormant/no-strong-candidate output rather than improvising equivalent context
- initial and supplemental analysis read only the selected bounded local trace input; supplemental passes use a strict older-than boundary and never imply corpus-wide absence

## Optional internal/operator help

If the user explicitly asks for internals, you may then explain or describe:
- the memsearch-backed `intake`, `signals`, and `present` chain
- bounded `choose`, `enrich`, `orchestrate`, `packet`, `emit`, `replay`, `trial`, and `ready`
- current checked install/runtime boundaries

But that internal/operator help is secondary. The default first response stays proposal-first and memsearch-backed.
