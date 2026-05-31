# Memsearch Required Dependency Boundary

## 0) Document Control

> **Parent Scope:** memory-context-intelligence plugin-local governed design chain
> **Current Version:** 0.1.57
> **Session:** d42465eb-30a7-4bc8-b9d6-03e52306e9a5 (2026-05-27)
> **Parent Design:** [design.md](design.md)

---

## 1) Requirement statement

Memsearch remains a required dependency for the implemented analysis path because live pattern detection is still anchored by memsearch-backed trace evidence.

## 2) Why memsearch is still required

The capsule still needs one evidence source that comes from real working traces rather than from retrospective governance prose.

That role still belongs to memsearch because it provides:
- bounded recent historical trace input across the user's work corpus
- explicit per-record provenance that can distinguish historical recurrence from current-session confirmation
- preferred `search → expand` recall support when exact wording or causal detail matters
- stale/unavailable signaling that prevents the runtime from inventing equivalent live evidence

พูดง่าย ๆ: ถึงตอนนี้จะมี `MEMORY.md` และ governance docs เข้ามาช่วยแล้ว แต่ถ้าไม่มี memsearch เราจะไม่มี live trace หลักฐานว่าปัญหาเกิดซ้ำจริงในประวัติการทำงานที่กำลังถูกวิเคราะห์.

## 3) Current implementation truth

The current checked implementation now uses memsearch together with broader context layers.

Implemented source roles:
- memsearch provides `trace_evidence`
- memsearch-backed retrieval can provide `recall_evidence`
- Claude memory files can provide `durable_memory_context`
- governed RULES surfaces can provide `governance_context`

But only memsearch is the required live trace anchor.

## 4) Scope of the requirement

This requirement is local to `plugin/memory-context-intelligence/`.

It does **not** mean:
- root RULES now requires memsearch globally
- all RULES workflows require memsearch
- memsearch output becomes rule authority
- memsearch availability alone is enough to justify rule changes
- durable memory or governance context becomes sufficient by themselves for live candidate promotion
- presentation configuration can weaken authority or evidence wording

## 5) Producer contract expectations

Expected memsearch producer behavior remains:
- memory summaries exist under a project-scoped `.memsearch/memory/`-style root
- summaries are date-sharded and readable as analysis input
- session provenance is available through record anchors when present
- transcript drill-down provenance is available through anchor metadata when present
- summaries are stale-able and therefore require freshness awareness

## 5.1) Checked current recall capability boundary

Checked current memsearch recall behavior from local docs/runtime surfaces still shows:
- deeper recall is `search` → `expand` → transcript drill-down rather than one direct session fetch
- public search exposes query, top-k, and optional `source_prefix` path scoping
- current checked docs/runtime surfaces do not prove first-class public flags for `session-id`, `day`, arbitrary date-window, or configurable lookback
- the analysis surface therefore still owns its own deterministic narrowing layer instead of assuming memsearch provides a one-flag historical/session slicer

Design consequence:
- `/memory-context-intelligence:analysis` should keep memsearch as the live trace source
- `/memory-context-intelligence:analysis` should default to broader historical bounded trace rather than a forced current-session-only slice
- explicit `day`, `session`, and `lookback` narrowing remain analysis-surface choices layered around memsearch, not public memsearch guarantees

## 6) Failure / unavailable posture

If memsearch is absent, stale, or unavailable:
- the live trace path is blocked or dormant
- the capsule must not invent equivalent live evidence from durable memory or governance docs
- it may still retain durable or governance context in the report, but those layers must not be treated as enough to promote a live candidate by themselves

If memsearch exists but broader historical analysis is still too weak:
- the capsule may report `insufficient`
- it may recommend waiting for stronger repeated historical trace or gathering fresher recurrence
- it must not treat durable memory or governance context alone as enough to propose a live candidate

## 7) Authority boundary

Memsearch output is empirical evidence input with provenance during analysis/refinement.

It is not:
- current code truth
- runtime truth
- release proof
- direct rule authority
- a long-term semantic dependency that mature RULES should continue to rely on at runtime

Any strong factual, governance, or completion claim still requires current checked evidence.

---

> Full history: [../changelog/changelog.md](../changelog/changelog.md)
