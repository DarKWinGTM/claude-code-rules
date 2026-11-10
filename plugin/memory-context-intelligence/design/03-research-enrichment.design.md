# Research Enrichment

## 0) Document Control

> **Parent Scope:** memory-context-intelligence plugin-local governed design chain
> **Current Version:** 0.1.82
> **Session:** 7194487f-fe8b-4383-8756-3db4c5612392 (2026-10-02)
> **Parent Design:** [design.md](design.md)

---

## 1) Goal

Define when and how externally researched evidence should enrich candidate improvement topics that were first detected from local work traces.

## 2) Core idea

พูดง่าย ๆ: local work traces บอกว่า "ควรดูเรื่องอะไร" แล้ว research enrichment ช่วยบอกว่า "เรื่องนั้นในโลกจริงมี fact, strategy, or best practice อะไรรองรับ"

The capsule should not rely on local memory alone when a candidate topic depends on external theory, standards, best practices, human factors, or broader technical guidance. In those cases, the topic should be enriched by deep, topic-specific web research before a stronger proposal packet is produced.

That research should be serious enough to test whether the candidate is fact-supported, strategically sound, and practical in the real world rather than being a shallow search pass.

## 3) When research is needed

External research is likely needed when a candidate topic depends on:
- broader workflow or governance best practices
- explanation or presentation strategy
- disclosure, audience, or safety framing
- memory/retrieval architecture theory
- standards, policies, or widely shared conventions
- claims about what is practical, stable, or effective beyond the local project

External research is usually not needed when the topic is purely local, such as:
- local naming and path conventions
- local document ownership choices
- local repository topology
- local sync order already defined by current authority

## 4) Full-power method

The capsule should default to one full-power evidence-backed distillation method rather than several user-facing research modes.

That full-power method should combine:
- local work-trace analysis first
- topic-specific external research when broader support is needed
- source-trust review
- confidence and limitation reporting
- native agent lanes for delegated gathering/review when the scope is broad enough to benefit from them

A dedicated Research Scout lane should own the deep web research portion when the topic is broad enough or important enough to justify more serious evidence gathering.

พูดง่าย ๆ: เอาข้อดีของ local-only, hybrid, research-first, และ verification-heavy มารวมเป็น flow เดียวที่เน้นความลึกและความน่าเชื่อถือ
## Collective synthesis and checked capability

[Post-Analysis Principle Synthesis](10-post-analysis-principle-synthesis.design.md) owns the manual summary workflow: complete existing Topics → provisional mechanisms/criteria/options → iterative public alternatives and counterevidence → evidence-led criteria reassessment and viable-option re-comparison when the decision frame changes → explicit research delta → revised principles and integrated method. The sequence supports traceability, not a fixed pipeline or output form. Research can add, remove, retain, refine, replace or withdraw a provisional answer; diversity supports contextual selection, not a source/option quota. It does not prove missing historical incidents or approve writes/promotion.

This manual skill uses public search/fetch tools actually available and permitted in its caller session. Existing `lib/research_enrichment.py` evaluates supplied controlled source records, while `lib/orchestration.py` and named plugin lane reports are deterministic in-process evidence. They do not perform live web access or acquire that capability from a prompt change. The candidate-specific flow below remains distinct; summary does not call it to rerun acquisition or create packets.

## 5) Research flow

```text
local work traces
  → detect candidate topic
  → classify whether broader support is needed
  → launch native agent lanes as useful
  → run focused web research
  → review source trust
  → compare local pain with external support
  → synthesize a stronger candidate packet with confidence/limits
```

## 6) Source trust boundary

Research enrichment should prefer stronger sources first.

Typical trust order:
- primary/official documentation, standards, specs
- maintainer or institutional engineering guidance
- reputable secondary technical explanations
- weak/accountability-light sources last

The goal is not to collect many sources. The goal is to determine whether the candidate topic has enough external support to justify a stronger proposal.

## 7) What research enrichment changes

Research enrichment changes the strength of the proposal, not the authority order.

It may:
- strengthen the explanation of why a candidate matters
- strengthen confidence that the candidate is practical or aligned with best practice
- reveal conflicts between local habit and external guidance
- refine mechanism or rollout design

It must not:
- override current user instruction
- override current checked RULES authority
- turn an unsupported topic into a selected change automatically

## 8) Expected output

A research-enriched topic expansion should include:
- local reason the topic surfaced
- whether research was needed and why
- what external themes or sources were consulted
- whether local and external signals align or conflict
- how the enriched proposal would affect RULES behavior, workflow, explanation, or governance understanding
- confidence and limitation notes
- what output or product the user receives next

Research output should be strong enough to distinguish:
- what is well-supported fact
- what is a best-practice recommendation
- what remains uncertain or contested

---

> Full history: [../changelog/changelog.md](../changelog/changelog.md)
