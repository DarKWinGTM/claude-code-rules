# Runtime Architecture - RULES System Design

> **Parent Design:** [../design.md](../design.md)
> **Current Version:** 10.76
> **Session:** 8176a2ea-c50d-48aa-9367-d0328016f821
> **Section:** Rule architecture
> **Full history:** [../../changelog/changelog.md](../../changelog/changelog.md)
> **Status:** Active target-state shard; source/install baseline, publication proof tracked separately

## Active Runtime Inventory

Exactly nineteen source-owned root Rules retain one body-sufficient owner per responsibility. Same-owner compaction is governed by [runtime-compaction.design.md](runtime-compaction.design.md); support trials and plugins do not enter this Main payload.

| # | Rule | Paired design version | Responsibility |
|---|---|---|---|
| 1 | `accurate-communication.md` | `accurate-communication.design.md v2.46` | actual-action/current-state reporting, claim/status strength, identifier meaning and capture labels |
| 2 | `action-safety.md` | `action-safety.design.md v1.8` | destructive/private/topology/emergency/retry gates, same-operation outcome reconciliation |
| 3 | `audience-surface-disclosure-control.md` | `audience-surface-disclosure-control.design.md v1.2` | direct-user transparency and generated audience disclosure |
| 4 | `authority-and-scope.md` | `authority-and-scope.design.md v2.9` | user precedence, advisory selection and Active Project Root |
| 5 | `coding-discipline.md` | `coding-discipline.design.md v1.10` | caller-first/prevention-owner coding, bound workflow proof, source-tool/probe lifecycle, debug and architecture fitness |
| 6 | `communication-register.md` | `communication-register.design.md v1.29` | plain action/outcome language, user/peer recipient clarity, signal, agreement and explicit retraction |
| 7 | `document-governance.md` | `document-governance.design.md v1.23` | artifact roles, affected-owner synthesis, chain selection, diagram/Patch and UDVC-1 eligibility |
| 8 | `document-integrity.md` | `document-integrity.design.md v1.15` | references, lossless rollover, payload/project proof and preservation |
| 9 | `evidence-discipline.md` | `evidence-discipline.design.md v1.10` | decisive assumptions, bound receipts, evidence kinds/claim states and cause/nonfinding/mock/witness limits |
| 10 | `execution-and-goal-frame.md` | `execution-and-goal-frame.design.md v1.38` | fact-led route/cadence, evidence-backed codebase challenge, mode/scope, proof selection and closure |
| 11 | `explanation-and-presentation.md` | `explanation-and-presentation.design.md v1.27` | complete inventories, visible needed action, outcome-first reporting, flexible grouping and unframed diagrams |
| 12 | `goal-authoring-and-route-support.md` | `goal-authoring-and-route-support.design.md v1.4` | checked Goal construction, proof slots and verified route/Plan-reference lifecycle |
| 13 | `external-verification-and-source-trust.md` | `external-verification-and-source-trust.design.md v1.8` | eligible source ranking/corroboration/conflicts |
| 14 | `memory-governance-and-session-boundary.md` | `memory-governance-and-session-boundary.design.md v2.0` | path/freshness applicability, active meaning hooks and optional recall |
| 15 | `phase-todo-artifact.md` | `phase-todo-artifact.design.md v1.39` | startup/task admission, strict lineage, semantic coverage and evidence handoff before final closure |
| 16 | `portable-implementation-and-hardcoding-control.md` | `portable-implementation-and-hardcoding-control.design.md v1.6` | late-bound portable forms, local exceptions and source/destination notation |
| 17 | `refusal-and-recovery.md` | `refusal-and-recovery.design.md v1.5` | normalized request/class/decision and actionable recovery |
| 18 | `safe-io.md` | `safe-io.design.md v1.10` | preparse input/record/retention bounds, bounded capture versus source-tool ownership, parent-first intake and burst detection |
| 19 | `worker-routing-and-context.md` | `worker-routing-and-context.design.md v1.18` | helper net benefit/topology/brief/lifecycle/handoff and main verification |

## Category View

- Communication/disclosure: accurate, register, presentation and audience owners make explanations clear and evidence-bounded.
- Evidence/authority/safety: evidence, authority, refusal and safety preserve checked facts, user choices and consequential boundaries.
- Execution/coding/helpers: execution, goal, coding, worker and Safe I/O keep source work complete, bounded and verifiable.
- Governance/context: document, integrity, phase, memory, portability and external trust preserve coherent artifact/context authority.

Consumers retain activation/local consequence and necessary synchronized literals, not another complete contract. Runtime copies are downstream from the selected source root; payload parity does not prove full-project convergence or future AI effectiveness.
