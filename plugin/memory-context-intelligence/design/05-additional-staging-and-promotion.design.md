# Additional Staging and Promotion

## 0) Document Control

> **Parent Scope:** memory-context-intelligence plugin-local governed design chain
> **Current Version:** 0.1.54
> **Session:** d42465eb-30a7-4bc8-b9d6-03e52306e9a5 (2026-05-21)
> **Parent Design:** [design.md](design.md)

---

## 1) Goal

Define where selected `memory-context-intelligence` proposals should go before they are allowed to become main RULES changes.

## 2) Core direction

พูดง่าย ๆ: ถ้า plugin นี้เสนอ rule improvement จริง มันไม่ควรไปแก้ main RULES ทันที แต่ควรลง stage ทดลองใน `/additional/` ก่อน แล้วค่อยตัดสินว่าจะ merge ขึ้น main rules หรือไม่

## 3) Master-project condition

When `<repo-root>/` exists, treat it as the master source project for RULES governance and release history.

That means:
- main rule doctrine still belongs to the master project
- proposal packets should still name the intended owner domain in the master project
- but trial-stage rule material should be separated from main rule bodies first

## 4) Trial-stage target

The selected trial-stage target for this concept is:
- `~/.claude/rules/additional/`

This `additional/` layer means:
- the rule is still in testing / evaluation
- it is not yet merged into main-stage RULES
- it may still be active in runtime if the chosen runtime activation path loads or exports it there
- successful use in `additional/` is evidence for later promotion, not automatic merge authority
- phase 015 emitted one checked local trial artifact at `<user-runtime-rules>/additional/memory-context-intelligence/phase-015-live-bounded-additional-stage-trial.md` with disposition `continue`; this path is local evidence, not a portable default
- phase 016 added checked-scope readiness reporting and may report `usable in checked scope` only when replay, trial, artifact, boundary, and main RULES unchanged gates pass

## 5) What the plugin should propose first

When a candidate is strong enough to become a real trial rule, the plugin should propose:
- target main rule domain or nearest owner chain
- trial rule name under `additional/`
- why the candidate belongs in trial first instead of main RULES immediately
- what evidence would prove the trial is useful enough to promote
- what merge target would be considered later if the trial succeeds
- which source classes carried the candidate: `trace_evidence`, `recall_evidence`, `durable_memory_context`, and `governance_context`
- whether the candidate has strong live pattern proof, only supporting durable context, or both

## 6) Promotion path

```text
memory-derived candidate
  → user selects candidate for real trial consideration
  → confirm live pattern strength from trace_evidence
  → use recall_evidence when exact wording/sequence is needed
  → use durable_memory_context to confirm lasting preference/project context when relevant
  → map intended main rule owner domain through governance_context
  → create additional-stage trial rule under ~/.claude/rules/additional/
  → observe whether the trial improves behavior in practice
  → aggregate replay, trial, artifact, boundary, and main RULES unchanged evidence
  → if the trial and readiness evidence justify promotion consideration
      → open governed follow-up for main RULES source chain
  → otherwise keep it trial-only, revise it, or retire it
```

## 6.1) Promotion gate by source class

Promotion consideration should follow this minimum logic:
- `trace_evidence` is required to prove a live repeated pattern worth trialing
- `recall_evidence` strengthens exactness when the pattern depends on subtle wording or sequence
- `durable_memory_context` strengthens long-lived preference/project-context confidence but must not substitute for missing live pattern evidence
- `governance_context` is required before owner mapping, phase routing, or later main RULES follow-up can be called well-formed

A candidate with only durable memory plus governance fit may still be useful as a design note, but it is not strong enough for trial-first promotion flow by itself.

## 7) Boundary conditions

This design must not treat `additional/` as:
- automatic main-rule authority
- proof that the rule is final
- a reason to skip design/changelog/phase/patch follow-up when promotion is chosen
- a guarantee that runtime loading behavior exists unless the activation contract is separately checked

It should treat `additional/` as:
- selected trial stage
- staging boundary before main-rule merge
- evidence-gathering layer for rule experimentation
- a write destination that requires explicit approval, selected-root containment, overwrite control, and path-safety checks

## 8) Implementation phase touchpoints

The phase program keeps `/additional/` staging in the runtime path before main RULES promotion:
- Phase 013 builds candidate packets and previews or explicitly emits approved trial material under a selected additional root
- Phase 014 validates historical replay with dry-run emit preview only and no approved replay writes
- Phase 015 completed one bounded live additional-stage trial, emitted one explicitly approved local trial artifact, and verified success criteria plus rollback notes without claiming install, publication, stable behavior, or main RULES promotion
- Phase 016 completed checked-scope readiness reporting and may report `usable in checked scope` only when focused runtime, replay, trial, artifact, boundary, and main RULES unchanged evidence gates pass
- Phase 017 audits whether additional-stage and checked-scope runtime evidence justify a main RULES promotion proposal
- Phase 018 handles main RULES merge only if the user selects promotion

## 9) Expected output

A promotion-ready candidate packet should include:
- candidate summary
- signal/evidence basis
- intended main RULES owner domain and target
- proposed `additional/` rule path/name
- why this should remain trial-stage first
- success criteria for promotion
- rollback notes for retiring, replacing, or removing trial-stage material
- stop gates and leader verification needs
- risks or reasons not to merge yet

---

> Full history: [../changelog/changelog.md](../changelog/changelog.md)
