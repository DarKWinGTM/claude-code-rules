# Memory Context Intelligence Core Concept

## 0) Document Control

> **Parent Scope:** memory-context-intelligence plugin-local governed design chain
> **Current Version:** 0.1.57
> **Session:** d42465eb-30a7-4bc8-b9d6-03e52306e9a5 (2026-05-27)
> **Parent Design:** [design.md](design.md)

---

## 1) Goal

Use bounded memory evidence from real work to distill stronger RULES/workflow improvements without treating memory as authority or making mature RULES depend on memory at runtime.

## 2) Core idea

พูดง่าย ๆ: `memory-context-intelligence` ควรดูรูปแบบการทำงานย้อนหลังของผู้ใช้แบบกว้างขึ้น across sessions ก่อน แล้วค่อยใช้ current-session evidence เป็นตัวช่วยยืนยันความสดใหม่หรือความต่อเนื่อง ไม่ใช่เป็นเจ้าของ scope เริ่มต้นอีกต่อไป.

The capsule supports a flow where evidence is analyzed into signals, those signals are grouped into topic candidates, and the user chooses which topic to expand before any deeper candidate or promotion material is produced.

## 3) Current implemented source model

The current checked implementation distinguishes these source classes explicitly:
- `trace_evidence`
- `recall_evidence`
- `durable_memory_context`
- `governance_context`

### 3.1 `trace_evidence`

`trace_evidence` remains the live anchor.

It now comes from:
- the project-scoped `.memsearch/memory/` root
- a bounded recent historical shard set across the user's work corpus by default
- explicit narrowing such as `day=YYYY-MM-DD`, `session=<id>`, or `lookback=<minutes|hours>` when the operator asks for it
- provenance fields that distinguish `historical-only` from `confirmed-in-current-session`

### 3.2 `recall_evidence`

`recall_evidence` is represented explicitly when memsearch-backed retrieval is available.

It comes from:
- preferred memsearch `search → expand` retrieval inside the bounded scope selected for the run
- explicit source-class tagging so later stages can distinguish exact-recall support from ordinary trace context

### 3.3 `durable_memory_context`

`durable_memory_context` comes from Claude memory files when present in checked scope.

Current implementation can use:
- `MEMORY.md`
- relevant path-scoped memory files referenced from that index
- durable feedback/project/reference notes as supporting context

### 3.4 `governance_context`

`governance_context` comes from checked governed surfaces in scope.

Current implementation can use bounded context from:
- plugin-local `design/`
- plugin-local `phase/`
- plugin-local `patch/`
- plugin-local `changelog/`
- root RULES `TODO.md`

## 4) Live-pattern anchor rule

Even with the broader historical scope and four-class source model, live topic promotion is still anchored by memsearch-backed `trace_evidence`.

That means:
- `durable_memory_context` can strengthen durability or user-preference context
- `governance_context` can strengthen owner/boundary fit
- `recall_evidence` can sharpen exactness
- but those sources must not replace missing live trace evidence when the system decides whether a candidate is strong enough to propose

## 5) Allowed influence of memory evidence

Memory evidence may be used to:
- suggest likely context boundaries that RULES should internalize better
- identify repeated user corrections or workflow preferences that may justify stronger doctrine
- identify repeated evidence/verification failures that may justify clearer gates
- identify recurring work-shape or operator-surface failures worth later review
- point to transcript or repo evidence that should be rechecked before formal doctrine changes
- map repeated historical patterns against current-session confirmation, durable memory context, and governed owner surfaces

## 6) What memory evidence must not decide by itself

Memory evidence must not:
- directly generate new RULES
- directly edit or mutate RULES
- act as current code/runtime truth
- overrule active user instruction
- overrule active RULES doctrine
- create verified/fixed/working/release-ready claims by itself
- become a long-term operational dependency for mature RULES behavior
- let durable memory or governance documents replace live trace evidence

## 7) Signal model

Representative signal families remain:
- context digest hints
- workflow advisor hints
- governance radar candidates
- signal-schema candidates
- transcript bridge/provenance hints
- sensitivity/disclosure handling candidates

Signals are still candidates or hints, not semantic truth.

Under the current implementation:
- `trace_evidence` drives live pattern strength
- `recall_evidence` sharpens exactness
- `durable_memory_context` strengthens durable context
- `governance_context` strengthens owner/boundary/promotion fit
- historical repetition, cross-session breadth, and recency rank ahead of current-session confirmation
- current-session confirmation is a boost, not the primary promotion gate

## 8) Consumer model

This capsule still designs consumers such as:
- context digest
- workflow advisor
- governance radar
- candidate packet builder
- transcript bridge
- sensitivity filter

These consumers are not immediate RULES edits. They are proposal/analysis lanes that help the user understand possible improvement directions before any governed RULES change is selected.

## 9) First-response behavior expectation

The first user-facing action should present topic candidates directly as historical work-pattern review topics.

That first response should:
- stay proposal-first or actionable-insufficiency-first
- avoid package-map, internal pipeline, or development-progress-summary narration by default
- keep provenance visible enough to distinguish `historical-only` from `confirmed-in-current-session`
- show compact source mix wording when durable memory or governance context materially shaped the candidate
- say directly when broader historical analysis did not find a sufficiently repeated pattern to propose yet
- expand deeper only after the user chooses a topic or explicitly asks for internals

## 10) Boundary with root RULES

This capsule can recommend later governed follow-up, but any active RULES change must still pass through normal evidence, design, changelog, phase, patch, and user-selected review paths.

---

> Full history: [../changelog/changelog.md](../changelog/changelog.md)
