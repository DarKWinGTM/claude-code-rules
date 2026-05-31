# Architecture Layers

## 0) Document Control

> **Parent Scope:** governed-docs plugin-local governed design chain
> **Current Version:** 0.1.0
> **Session:** b7f7ee85-27ec-467a-ba63-568c831fcd36 (2026-05-31)
> **Parent Design:** [design.md](design.md)

---

## 1) Goal

Define the internal architecture of the governed-docs companion so responsibility stays separated between observation, doctrine judgment, repair planning, and bounded execution.

## 2) Entry gate before the layer model

Before any layer runs, the plugin should require one explicit target workspace path from the operator.

Required posture:
- user-facing commands must name the governed project path they want inspected
- ambient cwd is not enough when several projects may coexist in one session
- if the path is missing, the command fails closed and returns a path-required guidance message
- if the path is ambiguous, non-existent, or outside the intended governance boundary, the command stops before scanning

Example target shape:
- `/governed-docs:scan /home/node/workplace/AWCLOUD/TEMPLATE/RULES/`
- `/governed-docs:review /home/node/workplace/AWCLOUD/TEMPLATE/RULES/`

## 3) Layer model

The plugin should use four explicit layers.

### Layer A — Surface Scanner

Purpose:
- inventory governed surfaces under the explicitly selected target workspace path
- classify file families, parent/shard shapes, and phase filename patterns
- detect current-state signals such as rollover pressure, release-surface mismatches, or role overload

Outputs:
- document inventory
- chain-shape map
- phase filename inventory
- rollover pressure report
- release-sync snapshot

This layer observes only. It does not decide semantics.

### Layer B — Doctrine Evaluator

Purpose:
- compare scanner output against existing RULES doctrine
- classify findings by policy meaning rather than by string mismatch only

Expected classifications include:
- `compliant`
- `legacy-but-allowed`
- `drift`
- `ambiguous-needs-basis`
- `safe-auto-repair`
- `blocked`

This layer is the main policy interpreter, but it still does not mutate files.

### Layer C — Repair Planner

Purpose:
- convert doctrine-classified findings into action packages that are small, reviewable, and approval-aware

Typical outputs:
- report-only recommendation
- repair-plan artifact
- open-repair-patch recommendation
- plan-in-current-phase recommendation
- block-closeout verdict
- bounded-normalize candidate

This layer decides the shape of the fix, not the semantics of the target doctrine.

### Layer D — Bounded Executor

Purpose:
- apply deterministic, low-risk changes only after the action policy allows them

Allowed examples in principle:
- backlink repairs
- shard-map synchronization
- missing pointer insertion
- compact formatting normalization
- wording normalization from already-verified release facts

Disallowed examples by default:
- authority reassignment
- lineage reassignment
- renaming governed files
- history deletion
- destructive cleanup

## 3) End-to-end flow

```text
Governed repo state
  → Surface Scanner
  → Doctrine Evaluator
  → Repair Planner
  → (optional) Bounded Executor
  → operator-facing review / release gate / repair artifact
```

## 4) Why this is better than a monolith

A monolithic plugin would blur:
- what was observed
- what RULES say it means
- what should be changed
- what can safely be changed automatically

That blur is dangerous in a governance-heavy domain. The layered model keeps evidence, judgment, planning, and execution separable.

## 5) Why this is better than audit-only

An audit-only model is safer than a monolith, but it leaves too much repetitive work manual:
- deterministic reference repair
- pointer sync
- compact low-risk normalization
- release-surface wording updates from already-verified evidence

The layered model keeps those tasks available without turning the plugin into a full autonomous maintainer.

## 6) Default posture inside the architecture

The default posture for the architecture is:
- scanner: always safe
- evaluator: always safe
- planner: always safe
- executor: guarded and bounded only

This keeps the default system in line with `guarded-execute` rather than `normalize-first`.

---

> Architecture rule of thumb: every layer should be replaceable or testable without requiring the next layer to exist.
