# RULES Behavior Playground

## Purpose

This playground shows how the current RULES change AI behavior in practice.

It exists to make the behavior impact visible without turning `README.md` into a large scenario dump and without confusing checked rule behavior with illustrative thought experiments.

---

## What this is

`playground/` is a governed non-runtime family.

Use it to:
- inspect scenario families where RULES materially change AI behavior
- read example-driven prompt ↔ AI response dialogues that make those changes easy to picture
- follow lightweight flow diagrams showing where RULES alter the assistant path
- see which current runtime rules govern each scenario family
- compare `rule-enforced fact`, `observed case`, and `virtual variant` cleanly
- update future observed examples over time without rewriting the whole family

## What this is not

This family is not:
- a runtime install payload
- a replacement for design/changelog/TODO/phase/patch authority
- a place to invent historical examples
- a README-style marketing surface

---

## Reading guide

### Rule-enforced fact
The behavior currently required by checked current RULES.

### Observed case
A checked example from repo or workflow history.

### Virtual variant
An explicitly labeled illustrative scenario used for matrix-style exploration.

---

## Start here

- [coverage.md](coverage.md) — maps all 18 active runtime rules to at least one scenario family
- [matrix.md](matrix.md) — virtual-case matrix across several decision axes
- [templates/case-template.md](templates/case-template.md) — standard shape for future case additions
- [observed/2026-05.md](observed/2026-05.md) — current observed-case log for this month

---

## Scenario families

1. [case-01-authority-collision-resolver.md](cases/case-01-authority-collision-resolver.md)
2. [case-02-evidence-calibrated-diagnosis.md](cases/case-02-evidence-calibrated-diagnosis.md)
3. [case-03-safe-refusal-and-recovery.md](cases/case-03-safe-refusal-and-recovery.md)
4. [case-04-destructive-action-and-topology-gate.md](cases/case-04-destructive-action-and-topology-gate.md)
5. [case-05-communication-and-presentation-calibration.md](cases/case-05-communication-and-presentation-calibration.md)
6. [case-06-audience-safe-disclosure-split.md](cases/case-06-audience-safe-disclosure-split.md)
7. [case-07-coding-change-with-verification-discipline.md](cases/case-07-coding-change-with-verification-discipline.md)
8. [case-08-execution-continuity-and-worker-routing.md](cases/case-08-execution-continuity-and-worker-routing.md)
9. [case-09-governed-artifact-lifecycle.md](cases/case-09-governed-artifact-lifecycle.md)
10. [case-10-external-memory-and-portability-boundary.md](cases/case-10-external-memory-and-portability-boundary.md)

---

## Update flow

When a new real prompt/workflow event shows RULES behavior clearly:
1. classify it into the closest existing scenario family
2. record it in the current monthly observed log
3. update the relevant case file's observed section or note count
4. update `coverage.md` only if the rule-to-scenario mapping changes
5. open a new scenario family only when the current ten no longer model the behavior honestly

---

## Runtime boundary

The active runtime install set remains 18 root runtime rules.

`playground/` is repository-governed content only and stays outside `.claude/rules/` install payloads in this wave.
