# memory-context-intelligence

> **Status:** Phase 068 completed plugin-scoped git push update and release in checked scope
> **Current Version:** 0.1.72
> **Session:** d42465eb-30a7-4bc8-b9d6-03e52306e9a5 (2026-06-01)

---

## What this is

`memory-context-intelligence` is a plugin-local governed capsule under `RULES/plugin/` for exploring how memsearch-produced work traces can be distilled into stronger RULES context, workflow doctrine, and governance understanding.

Phase 008 added bounded safe intake to the isolated runtime package. Phase 009 added internal signal/topic analysis from bounded intake output. Phase 010 added list-first topic presentation plus a choose flow that records exactly one selected topic as structured fileless state. Phase 011 added optional controlled research enrichment from one selected topic plus recorded source fixtures. Phase 012 added deterministic runtime-local orchestration that composes trace, research, source-trust, and synthesis lane findings into phase-013 candidate-input readiness. Phase 013 added candidate packet building and gated additional-stage emission so selected evidence can become reviewable trial material without mutating main RULES. Phase 014 added deterministic historical replay validation so the existing chain can be checked against bounded historical memory traces. Phase 015 added bounded live additional-stage trial reporting and emitted one approved trial artifact under the selected `/additional/` root. Phase 016 added checked-scope readiness reporting with final wording `usable in checked scope` only when replay, trial, artifact, boundary, and main RULES unchanged gates pass. Phases 050-053 then clarified and implemented the broader historical evidence model: `/memory-context-intelligence:analysis` now defaults to bounded broader historical memory across the user's work corpus, repeated historical trace can surface topics without requiring current-session trace as the primary gate, current-session evidence is supporting provenance/freshness context only, and operator-facing output now distinguishes `historical-only` from `confirmed-in-current-session` evidence without leaking development/progress-summary narration. Phase 056 then tightened the broader-historical review contract further: a narrow historical-only shape such as `2 trace / 1 session / 1 shard` no longer reads like strong broad history by default, broader multi-session/multi-shard evidence is prioritized more clearly, and the first response now exposes a compact historical breadth summary before collapsing into one proposal. Phase 057 then replaced the permission-blocked inline analysis skill wrapper with the fixed `memory-context-intelligence analysis-surface` runtime subcommand, so checked non-interactive local slash proof can now return operator-facing output when local command approval is intentionally granted. Phase 058 then lifted surfaced topics through doctrine/mechanism lenses so incident details stay inside proposal evidence/examples while top-level topic names stay at RULES/workflow principle level. Phase 059 then extended those doctrine-level proposals with concrete evidence-grounded `Evidence examples` plus explicit `Before behavior` / `After behavior` sections when usable bounded preview evidence exists, while omitting fabricated examples when it does not. Phase 061 then replaced the report-wrapper operator surface with repeated topic cards so each surfaced topic is rendered separately in one stable per-topic pattern instead of being merged into one combined explanation block. Phase 062 then hardened the observed session-dependent no-response defect at the operator contract layer: the slash invocation itself counts as the request, generic `no request` fallback is disallowed when rendered analysis context exists, and the topic-card response closes with one compact advisory `Next action options` bridge. Phase 063 then added a temporary stale-session diagnostic safeguard: when checked freshness evidence shows the current long-lived session started before the installed plugin update, the analysis surface can emit one advisory `possible stale long-lived session` warning without changing the normal analysis status/output or normalizing the underlying bug. Phase 064 then added compact `Before behavior` / `After behavior` previews to every first-pass topic card so the user can see the intended change immediately, while keeping `Evidence examples` real-preview-only and leaving long-form illustrative before/after in the expanded follow-up layer. Phase 065 then restores the richer easy-to-understand Thai-native first-pass explanation style by forcing native-first wrapper rendering again and localizing the known doctrine-level topic-card bodies instead of leaving them as English labels-only hybrids. Phase 066 then synchronized the governed docs around the selected multi-source-by-design + config-file source-policy direction as a docs-only wave. Phase 067 then implements that bounded config-policy layer in runtime: the intake path now accepts explicit `--config` or upward-discovers `memory-context-intelligence.config.json`, applies source-class and historical-shard limits before `intake → signals → present`, keeps explicit narrow runs narrow even when config requests same-day widening, surfaces policy-limited provenance honestly, and lets `/memory-context-intelligence:analysis` emit guided config questions when no config file is loaded instead of making raw args the normal UX.

The installability family is now aligned to one single-source RULES-owned model under the root `TEMPLATE` shared `darkwingtm` marketplace. The selected target install ID remains `memory-context-intelligence@darkwingtm`. Active source authority remains `RULES/plugin/memory-context-intelligence/`, and active runtime marketplace truth now comes from the root `TEMPLATE` marketplace file with supported in-base source `./RULES/plugin/memory-context-intelligence`, not from a separate projection tree. The earlier `TEMPLATE/PLUGIN/memory-context-intelligence/` projection family is retained only as historical installability evidence from phases 031-033; that duplicate path is no longer part of current runtime truth. Current checked local evidence shows `memory-context-intelligence@darkwingtm` installed/enabled in `scope: local` for `/home/node/workplace/AWCLOUD/CLAUDE`, normal plus bare plugin details still show one skill and four agents under source `memory-context-intelligence@darkwingtm`, `known_marketplaces.json` maps `darkwingtm` to the root `TEMPLATE` marketplace, and current checked runtime evidence keeps the plugin-registered analysis slash surface as `/memory-context-intelligence:analysis`, not bare `/analysis`. Official Claude Code docs checked in scope state that plugin skills use the `plugin-name:skill-name` namespace when invoked as slash commands, so this capsule no longer treats a true bare `/analysis` command as something that should be proved or owned by the plugin skill surface itself. If a true bare `/analysis` is selected later, it must come from a non-plugin harness-native owner surface outside the plugin namespace. Earlier proof for `/memory-context-intelligence:memory-context-intelligence` remains historical pre-implementation evidence only. Plugin-managed auto-flow remains unproven in checked local scope: `claude plugin details "memory-context-intelligence@darkwingtm"` shows one skill, four agents, `Hooks (0)`, and `MCP servers (0)`, the installed package contains no `hooks/hooks.json` or `monitors/monitors.json`, and this transcript still contains no autonomous auto-flow invocation event. This still does not claim direct `--plugin-dir` session identity as `memory-context-intelligence@darkwingtm`; direct disk loading remains the separate `memory-context-intelligence@inline` session-only boundary from the earlier split-proof model. It also still does not claim publication, external marketplace release, stable/broad production readiness, or main RULES promotion/mutation/merge.

พูดง่าย ๆ: ตอนนี้เหลือ source หลักที่เดียวคือ `RULES/plugin/memory-context-intelligence/` และ `memory-context-intelligence@darkwingtm` ยังอยู่ชื่อเดิมผ่าน root `TEMPLATE` marketplace; path `TEMPLATE/PLUGIN/memory-context-intelligence/` ไม่ใช่ current truth แล้วและถูกเก็บไว้แค่เป็นหลักฐานประวัติของ wave เก่าเท่านั้น.

## Harness-facing surface model

`memory-context-intelligence` is one plugin capability with three peer harness-facing entry surfaces:
- harness-native skill
- named slash-command surface
- plugin-managed auto flow surface

These three surfaces are peer entry shapes for the same capability contract. They are not three different products and they must not drift into separate semantic meanings.

`bin/memory-context-intelligence` remains an internal implementation adapter only. It may support development, testing, or runtime wiring, but it is not the primary post-install workflow for the user and it must not be documented as the main user-facing usage path.

Proof separation remains strict:
- install/load proof does not by itself prove skill invocation
- skill invocation proof does not by itself prove slash-command/chat invocation
- slash-command proof does not by itself prove plugin-managed auto flow
- internal adapter command behavior does not by itself prove any harness-facing surface

Current checked outcome:
- the current RULES-owned package now implements the historical-default analysis chain, the doctrine-level topic-synthesis refinement, the evidence-grounded proposal-example/before-after refinement, the compact post-topic `Next action options` bridge, the explicit slash-request hardening for the operator-facing analysis surface, the temporary stale-session diagnostic safeguard for freshness mismatch visibility, the restored native-first Thai-rich explanation contract for the known doctrine-level topic cards, and the bounded config-policy loading layer for source routing
- the governed docs now say consistently that config file remains a late-bound source-selection/source-limit policy for `trace_evidence`, `recall_evidence`, `durable_memory_context`, and `governance_context`, not a fifth evidence class, not semantic authority, and not a substitute for trace-anchored promotion proof
- focused `test_intake.py`, `test_signals.py`, `test_analysis_surface.py`, `test_presentation.py`, and `test_analysis_skill_contract.py` passed, and the full runtime package suite passed with `98` tests
- direct packaged `intake → signals → present` proof now confirms config-policy loading exists, policy-limited runs keep `trace_evidence` as the live promotion anchor, repeated topic-card output still holds, and `Next action options` still render; an additional packaged recall-only proof now confirms that a policy-limited `recall_evidence`-only run stays low-confidence and emits no live topic candidates without trace support
- checked approved non-interactive local invocations of `/memory-context-intelligence:analysis` now prove both guided config-helper output when no config file is loaded and no-args auto-discovered config loading when a project config file is present
- current checked slash proof now includes doctrine-level topics, compact `Before behavior` / `After behavior` previews in every first-pass topic card, richer Thai-native explanation bodies for the restored doctrine-level cards, concrete `Evidence examples` only when usable bounded preview evidence exists, a compact advisory `Next action options` bridge after the topic cards, an additive warning path for `possible stale long-lived session` when checked freshness evidence supports it, and advisory `config_questions` plus `suggested_config_path` when config is not loaded
- the runtime wrapper now carries explicit request-ownership markers such as `analysis_request_present`, `invocation_mode`, `render_required_now`, and `generic_no_request_response_allowed: false` so a rendered analysis result cannot truthfully fall back to a generic `no request` response in checked contract scope
- the stale-session safeguard stays advisory-only: it does not change normal analysis status/output and does not treat restart as the final fix
- plain no-approval print-mode is not used as proof because the slash surface needs a local command run
- plugin-managed auto-flow remains unclaimed because no `hooks/hooks.json` or `monitors/monitors.json` component and no transcript-visible autonomous auto-flow invocation are present in checked scope

## Selected invocation design

Checked registered analysis slash surface:
- `/memory-context-intelligence:analysis`
- official Claude Code docs checked in scope state that plugin skills use the `plugin-name:skill-name` namespace when invoked as slash commands

Checked current bare-command state:
- bare `/analysis` is not present in checked slash-command registry output
- checked approved non-interactive local slash proof now exists for `/memory-context-intelligence:analysis` when local command approval is intentionally granted with `--permission-mode bypassPermissions`
- plain no-approval print-mode still is not used as proof because the slash surface needs a local command run
- do not treat bare `/analysis` as proved current runtime behavior in the active contract
- if a true bare `/analysis` command is selected later, it must be owned by a non-plugin harness-native surface rather than the plugin skill namespace

Deferred / non-public commands in this wave:
- `/memory-context-intelligence:review`
- `/memory-context-intelligence:packet`

Implemented first-response contract:
- proposal-first topic suggestions sourced from broader historical memsearch-backed work evidence remain the default when a strong candidate exists
- bounded broader historical memory across the user's work corpus is now the default scope owner
- repeated historical trace can surface topic candidates without requiring current-session trace as the primary gate
- current-session evidence is supporting provenance/freshness context only and becomes a confirmation boost when present
- explicit narrowing such as `day=YYYY-MM-DD`, `session=<id>`, or `lookback=<minutes|hours>` remains available when the operator wants it
- design-grounded RULES/workflow review framing remains the default rather than generic recurring-pattern mining
- top-level topic names now stay at doctrine/mechanism level rather than incident-level issue wording
- incident details such as `404`, `passStatusCodes`, or similar case-level evidence now stay inside proposal evidence/examples or provenance instead of the title
- the slash invocation itself now counts as the request, even when the user provides no extra text after `/memory-context-intelligence:analysis`
- when rendered analysis context exists, the operator contract now disallows a generic `no request` fallback and instead requires the corresponding `available`, `blocked`, `dormant`, or `no-topics` state
- the first response now renders surfaced topics as repeated topic cards such as `Topic 1`, `Topic 2`, and `Topic 3`
- each topic uses the same repeated pattern so the user can compare topics directly instead of reading a wrapper report first
- if one topic is stronger, it is marked inside that same topic card as the recommended first topic instead of being expanded into a separate global recommendation/proposal wrapper
- after the topic cards, the response now ends with one compact advisory `Next action options` bridge that tells the user they can choose a topic number, type a direct request, or ask for deep thinking / websearch / webfetch before any adjustment
- when checked freshness evidence shows that the current session is older than the installed plugin update, the response may add one advisory `possible stale long-lived session` warning that tells the operator to restart this session and retry only as a temporary diagnostic safeguard
- the stale-session warning must not normalize the bug: session-dependent no-response still remains a bug, and restart must not be presented as the final fix
- when usable bounded preview evidence exists, the proposal body now adds concrete `Evidence examples`, `Before behavior`, and `After behavior` sections sourced from found data such as `signal.records[].content_preview`
- if usable bounded preview evidence does not exist, those example sections are omitted rather than filled with fabricated generic cases
- sparse historical runs can still surface at least 3 advisory topics by splitting distinct doctrine lenses instead of emitting an incident list
- short why/impact wording remains part of the first response
- a recommended first topic appears when one candidate is materially stronger
- provenance now stays visible enough to distinguish `historical-only` from `confirmed-in-current-session`, with compact source-mix wording when durable memory or governance context materially shaped a candidate
- no development/progress-summary leakage, package-map explanation, governance-map explanation, or internal pipeline/runtime narration appears in the first response
- if memsearch-backed analysis is blocked, say so directly with the input reason
- if memsearch-backed analysis is dormant, say the memsearch input is stale and stop there
- if broader historical analysis does not find a sufficiently repeated pattern to propose yet, say so directly with actionable insufficiency text, promotion-gate context, and next-step guidance

Current checked proof for the active runtime/config-policy wave:
- focused `tests/test_intake.py`, `tests/test_signals.py`, `tests/test_analysis_surface.py`, `tests/test_presentation.py`, and `tests/test_analysis_skill_contract.py` are green in checked scope
- the full runtime package suite passed with `98` tests
- the packaged runtime `intake → signals → present` chain proves config-policy loading exists, policy-limited runs can reduce source classes and historical shards before later stages, repeated topic cards still render, `next_action_options` still appear, and trace-anchored promotion is preserved; an added packaged recall-only proof also confirms that `recall_evidence` alone stays low-confidence and does not promote a live topic candidate without `trace_evidence`
- a checked approved non-interactive local `/memory-context-intelligence:analysis` run without a config file now returns topic cards plus advisory guided config-helper output with `config_questions` and `suggested_config_path`
- a second checked approved non-interactive local `/memory-context-intelligence:analysis` run with an auto-discovered project config file now returns topic cards without the guided helper, proving no-args config loading works from the active public surface
- current proof also preserves the earlier operator-facing improvements: doctrine-level topics, compact `Before behavior` / `After behavior` previews, richer Thai-native explanation bodies, conditional real-preview-only `Evidence examples`, explicit request-ownership markers, and the additive stale-session advisory path when freshness evidence supports it
- earlier proof for `/memory-context-intelligence:memory-context-intelligence` remains historical pre-implementation evidence only

Boundary of the current implementation:
- `review` and `packet` are still deferred, not newly opened public commands
- `bin/memory-context-intelligence` remains internal implementation only

## What this is not

This capsule and scaffold are **not**:
- an active main RULES runtime mutation
- a stable or broadly production-ready runtime
- a distinct plugin-managed auto-flow proof
- publication or external marketplace release proof
- main RULES promotion approval
- main RULES merge approval
- a direct memory-to-rule generator
- a hook or heavy automation owner despite the completed phase-032 supported marketplace exposure proof
- a marketplace-published or externally released package
- proof that phase 032 by itself left `memory-context-intelligence@darkwingtm` installed/enabled after the approved uninstall-only closeout
- proof that the runtime-facing projection is an independent source of truth separate from `RULES/plugin/memory-context-intelligence/`
- proof that main RULES should depend on memory at runtime
- a source of semantic truth stronger than active RULES, current user instruction, or checked evidence

## Required dependency

For the future capsule concept, **memsearch is a required producer dependency during analysis/refinement** because the intended distillation flow depends on memory summaries generated by memsearch as traces of real work.

That requirement is local to this capsule. It does **not** automatically make memsearch a mandatory root RULES infrastructure dependency, and it does not mean mature RULES should remain dependent on memory at runtime.

Phase 067 is the completed bounded config-policy implementation wave on top of that current truth. It now proves that runtime config-file loading exists for the analysis path, but only as a late-bound source-selection/source-limit policy for the existing four evidence classes. It still does **not** weaken the current rule that memsearch-backed `trace_evidence` remains the live promotion anchor, and it still does **not** turn config into semantic authority, selected-topic persistence, or automatic config mutation.

Phase 016 closes checked-scope readiness after bounded safe intake, internal signal/topic analysis, list-first presentation, explicit choose-flow recording, optional controlled research enrichment, runtime-local bounded orchestration, candidate packet building, gated additional-stage emission, deterministic historical replay validation, and bounded live additional-stage trial reporting. Phase 019 opened installability planning for later load/install lifecycle proof. Phase 020 prepared source-side manifest and marketplace bootstrap metadata. Phase 021 proved session-only inline load availability from the checked source package. Phase 022 proved local-scope persistent CLI install availability as `memory-context-intelligence@rules-local` from `<workspace-root>`. Phase 023 proved approved uninstall-only closeout while retaining the local marketplace and source package. Phase 024 reclassified those proofs under the selected `darkwingtm` namespace basis. Phases 025-027 remain completed historical checked evidence from a temporary/remapped `darkwingtm` state, not current restored shared-marketplace proof. Phase 028 completed docs-only governance alignment to the restored shared-marketplace state. Phase 029 completed docs-only selection of the shared-marketplace bridge design. Phase 030 is blocked because that bridge-entry implementation made `memory-context-intelligence` appear in the available list but Claude Code rejected the outside-base source path as unsupported / path traversal during install. Phases 031-033 are now preserved as historical installability/projection-family evidence only: they recorded the earlier `TEMPLATE/PLUGIN/memory-context-intelligence/` workaround/proof cycle, but phase 055 later removed that duplicate tree from current runtime truth. Phase 058 lifted surfaced topics through doctrine/mechanism lenses so incident details stayed inside proposal evidence/examples rather than top-level titles, and Phase 059 added concrete evidence-grounded proposal examples plus explicit before/after behavior when usable bounded preview evidence exists. Intake, signals, presentation, choose output, enrichment output, orchestration output, candidate packets, emitted trial material, replay reports, trial reports, readiness reports, installability plans, source-side bootstrap surfaces, transitional availability proof, transitional local installability proof, transitional lifecycle evidence, docs-only governance evidence, historical phase-025 split-proof evidence, historical phase-026 persistent install evidence, historical phase-027 uninstall lifecycle evidence, phase-029 docs-only design-selection evidence, phase-030 blocked-attempt evidence, phase-031 selected design evidence, phase-032 checked-local implementation/reproof evidence, and phase-033 broader correction-closeout evidence remain observational/evidence inputs, validation evidence, trial-stage material, checked-scope readiness evidence, planning surfaces, source-side bootstrap surfaces, transitional proof, historical evidence, docs-only governance evidence, selected design evidence, blocked implementation evidence, or checked-local implementation/reproof evidence only.

## Intended user flow

```text
real work happens
  → memsearch captures memory summaries as work traces
  → bounded intake reads a scoped, privacy-minimized sample
  → internal signals mode analyzes those traces for recurring patterns
  → present improvement topics as a list first
  → explain each topic in the user's active working language
  → show for each topic:
      - what it is for
      - how it would affect RULES behavior or workflow understanding
      - how the mechanism works at a high level
      - what output or product the user would receive
      - whether external research is likely needed
  → allow interactive presentation config (`auto`, `native-first`, `bilingual`, `fixed`)
  → ask the user to choose a topic second
  → optionally enrich the selected topic with controlled/recorded source evidence
  → orchestrate Trace Scout, Research Scout, Source-Trust Reviewer, and Synthesis Lead findings locally
  → build candidate packets from selected phase-013 input
  → preview or explicitly emit selected trial material under a controlled additional root
  → replay the chain over bounded historical memory traces with no approved writes
  → run one bounded live trial and emit approved trial material under `/additional/`
  → aggregate replay, trial, artifact, boundary, and main RULES unchanged evidence
  → report `usable in checked scope` only when readiness gates pass
  → open installability planning as a separate 019-023 family
  → preserve 020-023 as transitional `@inline` / `rules-local` checked-local proof
  → select `memory-context-intelligence@darkwingtm` as the target install ID
  → complete phase 024 namespace governance/design sync without runtime mutation
  → preserve phase 025-027 as historical checked evidence from the temporary/remapped darkwingtm state
  → restore active runtime marketplace truth to `darkwingtm` -> `<template-plugin-root>`
  → complete phase 028 docs-only restored shared-marketplace governance sync
  → complete phase 029 docs-only shared-marketplace bridge design selection
  → attempt phase 030 bridge-entry implementation under the shared darkwingtm marketplace
  → block phase 030 when Claude Code rejects the outside-base bridge source as unsupported / path traversal
  → complete phase 031 docs-only design selection for a supported runtime-facing package projection at `TEMPLATE/PLUGIN/memory-context-intelligence/` synced from `RULES/plugin/memory-context-intelligence/`
  → complete phase 032 as approved implementation and checked-local reproof for the runtime-facing package projection
  → keep main RULES promotion/merge deferred to separate phases 017-018
```

## Topic presentation shape

The first visible topic list should not be label-only.

Each listed topic should explain:
- purpose
- why the topic surfaced from real work traces
- behavior or workflow impact
- high-level mechanism
- expected output/product

The explanation density should stay balanced: complete enough to understand, but not so long that the list becomes hard to scan.

พูดง่าย ๆ: user ต้องอ่านรายการหัวข้อแล้วเข้าใจทันทีว่าถ้าเลือกหัวข้อนี้ จะได้อะไร ทำไมเรื่องนี้ถึงถูกเสนอขึ้นมา และระบบจะทำงานต่างไปอย่างไร โดยไม่ต้องเดาเอง

## Trial-stage rule direction

When this capsule produces a candidate strong enough for real rule experimentation, the selected trial-stage target is:
- `~/.claude/rules/additional/`

That means the candidate should remain separated from main-stage RULES first. If the trial proves useful, it can later become a governed merge candidate for the main RULES source chain.

Phase 013 previews additional-stage material by default and writes only when `--approved-write` is explicitly supplied. Approved emission remains scoped to the selected additional root, refuses unapproved overwrites and unsafe paths, and does not mutate main RULES.

Phase 014 historical replay uses dry-run emit preview only when preview is enabled. Replay does not expose approved writes.

Phase 015 completed one bounded live approved additional-stage trial. The checked local emitted artifact is `<user-runtime-rules>/additional/memory-context-intelligence/phase-015-live-bounded-additional-stage-trial.md` with disposition `continue`. That emitted file is trial-stage material only, not install proof, publication proof, stable behavior proof, or main RULES promotion approval.

Phase 016 completed checked-scope readiness reporting. The readiness path may report `usable in checked scope` only when focused stage checks, replay/trial summaries, phase-015 artifact evidence, boundary flags, and checked main RULES unchanged audit pass. It is not stable behavior, broad production readiness, install/publication proof, marketplace release proof, main RULES promotion, main RULES mutation, or main RULES merge.

Phases 019-023 completed checked-local installability evidence, but phase 024 reclassifies phases 020-023 as transitional proof under the later selected namespace basis. The selected target install ID remains `memory-context-intelligence@darkwingtm`; phases 025-027 remain completed historical checked evidence from the temporary/remapped `darkwingtm` state, not current restored shared-marketplace proof. Phase 028 completed docs-only restored shared-marketplace governance sync. Phase 029 completed docs-only selection of the shared `darkwingtm` marketplace bridge design. Phase 030 is blocked because the shared-marketplace bridge entry using source `../RULES/plugin/memory-context-intelligence` was rejected by Claude Code as unsupported / path traversal outside the marketplace base during install. Phases 031-033 are now historical projection-family evidence only, and phase 055 supersedes their active-authority assumptions by keeping the root `TEMPLATE` marketplace plus `./RULES/plugin/memory-context-intelligence` as the current truth. Phases 017-018 remain deferred for main RULES promotion/merge, and `/additional/` trial-stage behavior remains unchanged.

## Implementation phase program

The full program is defined in [phase/SUMMARY.md](phase/SUMMARY.md) without duplicating the phase table here.

Compact shape:
- 001-006 keep the existing design concept lineage
- 007 created the isolated runtime package scaffold
- 008 implemented bounded safe memsearch intake
- 009 implemented internal signal extraction and topic generation
- 010 implemented list-first topic presentation and choose-flow selection
- 011 implemented optional controlled research enrichment
- 012 implemented runtime-local bounded native-agent orchestration findings
- 013 implemented candidate packet building and gated additional-stage emission
- 014 implemented deterministic historical replay validation
- 015 implemented bounded live additional-stage trial reporting and emitted one approved trial artifact
- 016 implemented checked-scope readiness reporting and reports `usable in checked scope` only when evidence gates pass
- 017-018 remain planned/deferred for conditional main RULES promotion readiness and possible merge closeout
- 019 completed installability planning and opened the 019-023 installability family without claiming install proof
- 020 completed source-side manifest and local marketplace/bootstrap surfaces, now reclassified as transitional namespace evidence
- 021 completed session-only inline load proof as `memory-context-intelligence@inline`, now reclassified as transitional proof
- 022 completed local-scope persistent CLI install proof as `memory-context-intelligence@rules-local`, now reclassified as transitional proof
- 023 completed reload/new-process evidence reuse, approved uninstall-only proof, and install documentation closeout for `rules-local`
- 024 completed docs-only namespace governance sync for the selected target install ID `memory-context-intelligence@darkwingtm`
- 025 remains completed historical darkwingtm session-only split-proof evidence from the temporary/remapped state
- 026 remains completed historical local-scope persistent install proof from the temporary/remapped state
- 027 remains completed historical uninstall-only lifecycle closeout evidence from the temporary/remapped state
- 028 completed docs-only restored darkwingtm shared-marketplace governance sync
- 029 completed docs-only shared darkwingtm marketplace bridge design selection
- 030 is blocked because the shared-marketplace bridge entry was rejected as unsupported / path traversal during install
- 031 completed docs-only supported runtime package exposure design
- 032 is completed as supported runtime-facing package implementation and checked-local reproof
- 033 is completed as direct runtime-loaded proof and broader transcript-governed darkwingtm correction closeout in checked local scope
- 034 is completed as docs-only harness-surface governance sync that classifies skill, slash, and auto flow as peer harness-facing surfaces while reclassifying `bin/memory-context-intelligence` as an internal implementation adapter only
- 035 completed named slash proof plus exact auto-flow blocker capture
- 036 completed analysis-only invocation design sync
- 037 completed the implementation-planning wave
- 038 completed runtime analysis-surface implementation in checked local scope
- 039-041 completed the earlier namespaced-authority correction family
- 042 completed the earlier single public `/analysis` memsearch-backed operator-surface sync
- 043 completed recall-scoped design clarification before runtime realignment
- 044 completed scope-first recall runtime implementation and compatibility/verification closeout
- 045 completed the registered analysis surface correction
- 046 completed the bare `/analysis` surface model selection
- 047 completed the design-grounded current-session-first analysis review correction
- 048 completed the memsearch-backed analysis retrieval correction
- 049 completed the analysis-surface output-contract correction
- 050 completed the governed source-model clarification wave that separated current memsearch-only truth from the later four-class evidence target
- 051 completed the multi-source evidence implementation wave that made `trace_evidence`, `recall_evidence`, `durable_memory_context`, and `governance_context` real in checked scope
- 052 completed the no-bug diagnosis wave that proved an earlier `no-topics` result was expected current-session insufficiency at that moment
- 053 completed the historical-default redesign wave that moved default analysis to broader historical memory, re-ranked promotion around historical repetition / cross-session breadth / recency, and synced governed plus runtime-facing docs
- 054 completed the native-first communication-contract wave that separated `presentation / recommendation / proposal` and made first-pass output operator-facing without a second rewrite pass
- 055 completed the single-source authority cleanup wave for the root `TEMPLATE` marketplace + `./RULES/plugin/memory-context-intelligence` model
- 056 completed the historical breadth/ordering correction wave
- 057 completed the permission-safe slash-wrapper correction wave
- 058 completed the doctrine-level topic-synthesis wave
- 059 completed the evidence-grounded proposal-example and before/after refinement wave
- 060 completed the historical wrapper-spine cleanup attempt and is now preserved as historical correction context only
- 061 completed the repeated topic-card operator-output correction wave
- 062 completed the session-independent slash no-request contract hardening wave
- 063 completed the stale-session diagnostic safeguard wave
- 064 completed the compact first-pass before/after preview wave
- 065 completed the rich topic-card explanation restoration wave
- 066 completed the docs-only multi-source config-policy sync wave
- 067 completed the runtime config-policy loading and guided config-helper wave

## Scope boundary

Capsule governance lives here:
- `README.md`
- `design/`
- `changelog/`
- `phase/`
- `patch/`

Active runtime implementation home is the capsule path:
- `<repo-root>/plugin/memory-context-intelligence/`
- checked local path: `<repo-root>/plugin/memory-context-intelligence/`

Through phase 038, active runtime implementation and source authority remain package-local in that source home. The active source package contents include:
- `.claude-plugin/plugin.json`
- `bin/memory-context-intelligence`
- `lib/config_policy.py`
- `lib/intake.py`
- `lib/signals.py`
- `lib/presentation.py`
- `lib/research_enrichment.py`
- `lib/orchestration.py`
- `lib/candidate_packet.py`
- `lib/historical_replay.py`
- `lib/live_trial.py`
- `lib/readiness.py`
- `tests/test_intake.py`
- `tests/test_signals.py`
- `tests/test_presentation.py`
- `tests/test_analysis_surface.py`
- `tests/test_analysis_skill_contract.py`
- `tests/test_research_enrichment.py`
- `tests/test_orchestration.py`
- `tests/test_candidate_packet.py`
- `tests/test_historical_replay.py`
- `tests/test_live_trial.py`
- `tests/test_readiness.py`
- `skills/analysis/SKILL.md`
- `agents/*.md`
- package-local `design/`, `changelog/`, `phase/`, and `patch/`

Transitional local settings/cache/install outputs from phase 022 `rules-local` proof, phase 023 uninstall-only closeout, the historical temporary/remapped darkwingtm proof, and the phase 032 uninstall-only lifecycle closeout remain evidence surfaces only. They are not the active source home and must not be treated as source authority.

Phase 028 records the earlier restored shared-marketplace baseline, phase 029 selected the shared-marketplace bridge design without runtime mutation, and phase 030 proved that the `../RULES/plugin/memory-context-intelligence` bridge entry is unsupported because Claude Code rejects that outside-base source as path traversal during install. Phases 031-033 are now retained as historical installability evidence for the removed projection family only: they recorded the earlier `TEMPLATE/PLUGIN/memory-context-intelligence/` export/projection experiment and its local proof cycle, but that tree is no longer part of current runtime truth. The active model after phase 055 keeps one source home only, keeps `darkwingtm` mapped to the root `TEMPLATE` marketplace, and resolves `memory-context-intelligence` from that marketplace through supported in-base source `./RULES/plugin/memory-context-intelligence`. Phase 025 session split proof, phase 026 local install proof, and phase 027 uninstall lifecycle closeout remain valid historical checked evidence from the temporary/remapped state, but not current runtime truth. Retained `rules-local` evidence, source package, retained cache/data, historical phase-026 darkwingtm install evidence, historical phase-027 darkwingtm uninstall evidence, and `/additional/` trial material remain preserved. The capsule still does not create hooks, install into main RULES, publish to a marketplace, run live web access, spawn external agent processes, expose approved replay writes, claim stable or broad production readiness, perform main RULES promotion, merge main RULES, mutate main RULES, or claim a distinct plugin-managed auto-flow proof.

## Local governance map

Active parent files:
- `design/design.md` — active parent design index
- `changelog/changelog.md` — active parent changelog authority
- `phase/SUMMARY.md` — local roadmap
- `patch/analysis-config-policy-runtime-implementation.patch.md` — active capsule review artifact for the completed phase 067 runtime config-policy loading and guided config-helper wave

Active sibling shard files:
- `design/00-core-concept.design.md`
- `design/01-memsearch-required-dependency.design.md`
- `design/02-topic-list-and-choice-flow.design.md`
- `design/03-research-enrichment.design.md`
- `design/04-native-agent-orchestration.design.md`
- `design/05-additional-staging-and-promotion.design.md`
- `design/06-plugin-installability.design.md`
- active changelog detail shards now extend through `changelog/v0.1.72-completed-plugin-scoped-git-push-and-release.changelog.md`

## Path and portability note

The source shape this capsule is designed around is a project-scoped `.memsearch/memory/` summary root used as an observational input during analysis.

The end goal is not to make RULES depend on memory. The goal is to distill recurring lessons from real work so mature RULES can stand on their own.

Exact local absolute paths may be cited in local analysis or audit work, but they are checked local facts, not reusable defaults. Runtime package configuration must stay late-bound rather than hardcoding machine-specific memsearch paths as defaults.
