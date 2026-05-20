# RULES Behavior Playground

## Purpose

This playground shows how the current RULES change AI behavior in practice.

It exists to make the operational effect visible without turning `README.md` into a large scenario dump and without confusing checked rule behavior with illustrative thought experiments.

For `v10.20 / P112`, the family should prefer transcript-grounded observed cases, operational-first case structure, and lightweight flow explanations when checked evidence supports them.

---

## What this is

`playground/` is a governed non-runtime family.

Use it to:
- inspect scenario families where RULES materially change AI behavior
- see the operational path clearly: user objective, execution reality, rule effect, decision, next action, and recovery path
- follow lightweight flow diagrams showing where RULES alter the assistant path
- see which current runtime rules govern each scenario family
- compare `rule-enforced fact`, `observed case`, and `virtual variant` cleanly
- follow transcript-grounded observed entries with exact checked transcript paths and anchor hints

## What this is not

This family is not:
- a runtime install payload
- a replacement for design/changelog/TODO/phase/patch authority
- a place to invent historical examples
- a README-style marketing surface
- a dialogue-first collection where conversation trace hides the operational behavior change

---

## Reading guide

### Rule-enforced fact
The behavior currently required by checked current RULES.

### Observed case
A checked example from repo or workflow history.

Transcript-derived observed cases should cite the exact checked transcript path plus short anchor hints.

### Virtual variant
An explicitly labeled illustrative scenario used for matrix-style exploration.

### Operational sections
The main case body should show:
- User objective
- Operational reality
- RULES effect on execution
- Decision
- What AI does next
- Recovery path
- User-visible reply example
- Behavior delta

Dialogue, if present at all, is supporting illustration only.

---

## Start here

- [coverage.md](coverage.md) — maps all 18 active runtime rules to at least one scenario family
- [matrix.md](matrix.md) — virtual operational-case matrix across decision and execution axes
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
11. [case-11-status-ladder-and-completion-claim-audit.md](cases/case-11-status-ladder-and-completion-claim-audit.md)
12. [case-12-workflow-blocked-visual-qa.md](cases/case-12-workflow-blocked-visual-qa.md)
13. [case-13-live-execution-surface-arbitration.md](cases/case-13-live-execution-surface-arbitration.md)
14. [case-14-combined-rules-execution-state-orchestration.md](cases/case-14-combined-rules-execution-state-orchestration.md)
15. [case-15-language-aware-candidate-goal-promotion.md](cases/case-15-language-aware-candidate-goal-promotion.md)
16. [case-16-end-to-end-language-aligned-goal-surface.md](cases/case-16-end-to-end-language-aligned-goal-surface.md)

---

## Update flow

When a new real prompt/workflow event shows RULES behavior clearly:
1. classify it into the closest existing scenario family
2. record it in the current monthly observed log with exact transcript path and anchor hints when the evidence is transcript-derived
3. update the relevant case file's observed section and operational behavior sections
4. update `coverage.md` only if the rule-to-scenario mapping changes
5. open a new scenario family only when the current families no longer model the behavior honestly and checked transcript evidence supports the split

---

## Runtime boundary

The active runtime install set remains 18 root runtime rules.

`playground/` is repository-governed content only and stays outside `.claude/rules/` install payloads in this wave.
