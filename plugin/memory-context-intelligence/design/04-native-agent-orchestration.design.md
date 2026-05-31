# Native Agent Orchestration

## 0) Document Control

> **Parent Scope:** memory-context-intelligence plugin-local governed design chain
> **Current Version:** 0.1.18
> **Session:** d42465eb-30a7-4bc8-b9d6-03e52306e9a5 (2026-05-18)
> **Parent Design:** [design.md](design.md)

---

## 1) Goal

Define how native-agent-style lanes support the full-power evidence-backed distillation method for this capsule.

Phase 012 implements the first runtime form of this design as deterministic runtime-local orchestration. It produces four lane findings in process instead of spawning external agent processes.

## 2) Why native-agent lanes belong here

This capsule is meant to analyze real work traces, strengthen selected topics with broader evidence when needed, and eventually return structured proposal packets. When the topic scope is broad, lane separation improves efficiency by splitting gathering and review work into bounded findings before final synthesis.

พูดง่าย ๆ: lane เหล่านี้ช่วยแยกงานเก็บหลักฐาน/วิจัย/ตรวจ source/สรุปผลให้เป็นระเบียบ แต่ยังไม่ใช่ตัวตัดสินแทน RULES หรือแทนผู้ใช้

## 3) Phase-012 implemented lane shape

The runtime package under `<repo-root>/plugin/memory-context-intelligence/` now exposes `orchestrate`, which returns runtime-local findings for:
- **Trace Scout** — summarizes bounded intake and internal signal-report scope, trace anchors, topic candidate state, and trace uncertainty
- **Research Scout** — summarizes selected-topic research status, controlled source fixture use, query families, and missing-evidence gates
- **Source-Trust Reviewer** — summarizes source authority, freshness, weak-source handling, conflicts, and source-strength limits
- **Synthesis Lead** — merges lane findings into readiness states and emits bounded `phase_013_candidate_input`

The lead session remains responsible for final framing, authority boundaries, direct verification of material anchors, and what is shown to the user.

## 4) When to use orchestration

Use orchestration when at least one is true:
- bounded trace evidence and signal output need lane-shaped review
- one selected topic needs controlled enrichment or enrichment-status reporting
- source trust or conflict handling should become explicit before candidate input is carried forward
- phase-013 candidate-input readiness needs a deterministic summary
- the leader needs stop gates and verification needs collected in one structured result

Do not force orchestration for trivial or single-surface topics.

## 5) Output contract

Each lane finding returns:
- checked scope
- source basis or anchors
- findings
- confidence or evidence-strength notes where relevant
- conflicts or uncertainty
- stop gates
- leader verification needs
- evidence-input-only status

For the Research Scout and Source-Trust Reviewer lanes, output must separate local memory signal, controlled source support, weak source limits, and conflicting claims.

For the Synthesis Lead lane, output must include a readiness state such as `ready-for-phase-013-input`, `phase-013-input-with-stop-gates`, `trace-only-needs-topic-selection`, or `blocked-insufficient-trace-input`.

## 6) Boundary conditions

Native-agent-style orchestration must not:
- spawn external agent processes in phase 012
- run live web access in phase 012
- build candidate packets in phase 012
- write `/additional/` material in phase 012
- mutate RULES directly
- silently broaden scope beyond the selected topic
- treat memory, enrichment, or lane output as authority by itself
- auto-approve a proposal
- replace the user’s topic choice

## 7) Future implementation note

Phase 012 creates runtime-local lane findings only. Later governed phases may build candidate packets, validate historical replay, run bounded `/additional/` trials, or consider main RULES promotion. Those later steps remain unavailable until their phase gates are implemented and verified.

---

> Full history: [../changelog/changelog.md](../changelog/changelog.md)
