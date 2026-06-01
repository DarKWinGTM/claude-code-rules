---
name: analysis
description: Use when the user wants analysis of real work evidence, anchored by memsearch-backed traces and optionally strengthened by durable memory or governance context, so Claude can propose RULES or workflow improvement topics in a proposal-first format.
version: 0.9.27
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
- default scope: broader historical memory across the user's work corpus
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
- the analysis path now also supports bounded config-policy loading: explicit `--config` or upward-discovered `memory-context-intelligence.config.json` may limit source classes, cap historical shards, and request same-day widening only for non-explicit runs
- when config policy narrows the run, `source_policy` should stay visible so the operator can see that the evidence scope was intentionally limited

Deferred / non-public command ideas in this wave:
- `/memory-context-intelligence:review`
- `/memory-context-intelligence:packet`
- do not present them as active public commands

## Checked analysis context

```!
memory-context-intelligence analysis-surface
```

The checked analysis context emitted by this runtime wrapper still includes field-level evidence surfaces such as `source_classes_present`, `source_scope_label`, `source_mix_label`, `historical_strength`, `latest_seen`, `current_session_confirmation`, repeated `topic_cards`, and config-related surfaces such as `source_policy`, `config_questions`, and `suggested_config_path` for the operator-facing result.

## Default first response contract

When invoked for normal operator use:
- rely on the rendered memsearch-backed analysis context above as the primary checked evidence source
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
- expose `suggested_config_path` when present so the operator can see where the project default config file would live
- keep that guided config helper advisory only; it helps the operator choose config defaults, but it must not be treated as an approved write or automatic config mutation
- when `source_policy` says a config file was loaded, keep that policy-limited context visible enough that the operator can tell whether source classes, historical shard count, or same-day widening defaults narrowed the run
- if config policy disabled `trace_evidence` or left only context-only sources in scope, do not let the response overread that run as a promotable live candidate
- use semantic human-readable titles in the first response; do not leave the user with raw slug/token-bag titles
- the top-level unit of the default first response must be `Topic <n> — <human-readable title>`
- each surfaced topic must use the same repeated pattern format so the user can scan and compare topics directly
- the repeated topic cards must keep the same repeated pattern across Topic 1, Topic 2, Topic 3, instead of switching one topic into a different structural mode
- one topic must not be split across separate report-wrapper sections
- Do not use `Presentation`, `Recommendation`, `Proposal`, and `Related variants` as top-level blocks in normal operator output
- Do not split one topic across multiple sections
- do not merge several surfaced topics into one combined explanation block
- if one topic is stronger, mark it inside that same topic card as the recommended first topic instead of creating a separate recommendation wrapper section
- same-family weaker topics may still appear, but they should stay in the same repeated topic-card rhythm rather than being moved into a separate global variants wrapper
- repeated recap or summary blocks must be removed; each topic block should add topic-specific meaning rather than restating a global summary again
- the first response must not require a second manual rewrite pass; it should already read as native-first operator-facing output
- treat the analysis surface as adaptive deep-analysis when the rendered payload includes `adaptive_deep_analysis`
- all four internal evidence sources should be treated as the default internal evidence basis when the payload says they are enabled by default
- when `adaptive_deep_analysis.deepening_required` is true, you must deepen the top 1-2 topic candidates named in `adaptive_deep_analysis.required_topic_ids` before the first response instead of silently skipping deepening
- when a required candidate recommends `subagent-assisted`, use a read-only subagent lane if the current runtime exposes subagent capability
- when a required candidate recommends `subagent+external-research`, use the read-only subagent lane plus web/external research if those tools are available in the current runtime
- if the required subagent or web/external research tool is unavailable, you must say so explicitly and keep the skipped deepening visible rather than silently skipping it
- do not silently skip required adaptive deepening
- subagent-assisted deepening should stay read-only and focus on clarifying mechanism, impact, source conflicts, and decision-ready intervention wording for the already-ranked topic
- web/external research enrichment is allowed only as a supporting layer after a trace-backed local topic already exists; it may strengthen principle/mechanism support, constraints, or trade-offs, but it must not replace local trace proof
- keep `trace_evidence` as the live promotion anchor even after adaptive deep-analysis, subagent-assisted deepening, or web/external research enrichment
- `trace_evidence` remains the live promotion anchor even when deeper analysis uses multiple internal sources and optional external support
- trace_evidence remains the live promotion anchor even when deeper analysis uses multiple internal sources and optional external support
- adaptive deepening before topic selection must not be treated as selected or approved; it remains advisory-only until the user chooses a topic or explicitly asks for a change proposal/goal draft
- keep the topic-card output shape even after deeper analysis; deepen the evidence and mechanism inside the cards rather than replacing them with a new wrapper format

If the rendered status is `blocked`:
- say directly that analysis is blocked
- state the memsearch/input reason briefly
- do not invent topics from current conversation context

If the rendered status is `dormant`:
- say directly that analysis is dormant because the memsearch input is stale
- do not invent fresh topics from stale input

If the rendered status is `insufficient` or `no-topics`:
- say directly that broader historical analysis did not find a sufficiently repeated pattern to propose yet
- keep the insufficiency wording historical-first by default instead of treating current-session scarcity as the default explanation
- add one short actionable insufficiency line using the rendered `no_topics_message`
- add one short promotion-gate or next-step line from `no_topics_details` or `recommended_next_step`
- if the strongest remaining signal is only a narrow historical pattern such as `2 trace / 1 session / 1 shard`, say that it is too narrow to count as broader historical review
- do not treat durable memory or governance context alone as enough to propose a live candidate
- do not fill the response with workflow explanation just to avoid a short answer

If the rendered status is `available` and `topic_cards` is non-empty:
- present topic candidates directly as doctrine-level historical work-pattern review topics
- render surfaced topics as repeated topic cards using one stable pattern, for example `Topic <n>` such as `Topic 1`, `Topic 2`, `Topic 3`
- each topic card should carry its own short explanation, evidence/provenance line, status, and optional recommendation tag when it is the strongest topic
- broader multi-session/multi-shard patterns should still outrank narrow historical single-session/single-shard traces when the system chooses which topic cards surface first
- if a narrow historical pattern is the strongest remaining evidence, say so directly instead of letting it read like broad historical proof
- keep any historical breadth summary to one short line only when it changes interpretation; do not let it become the main wrapper structure ahead of the topics
- keep provenance visible enough to distinguish `historical-only` from `current-session-confirmed` patterns
- top-level topics must stay at RULES/workflow principle or mechanism level rather than incident-level issue wording
- incident details such as `404`, `python error`, or similar case-level examples should stay inside proposal evidence/examples or provenance, not in the title
- sparse historical runs may still surface at least 3 advisory topics when the list can split into distinct doctrine lenses rather than an incident list
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
- do not present candidate topics as already-approved RULES changes
- if memsearch-backed analysis cannot continue, stop at blocked/dormant/no-strong-candidate output rather than improvising equivalent context

## Optional internal/operator help

If the user explicitly asks for internals, you may then explain or describe:
- the memsearch-backed `intake`, `signals`, and `present` chain
- bounded `choose`, `enrich`, `orchestrate`, `packet`, `emit`, `replay`, `trial`, and `ready`
- current checked install/runtime boundaries

But that internal/operator help is secondary. The default first response stays proposal-first and memsearch-backed.
