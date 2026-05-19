# Runtime Architecture - RULES System Design

> **Parent Design:** [../design.md](../design.md)
> **Current Version:** 10.09
> **Session:** 1f1873d2-0feb-485f-a5ff-d383254590dd (2026-05-17)
> **Section:** Rule architecture
> **Full history:** [../../changelog/changelog.md](../../changelog/changelog.md)
> **Status:** Active target-state shard

---

## Active Runtime Inventory

The active runtime inventory contains 18 source-owned root rule files.

| # | Rule | Design Doc | Purpose |
|---|---|---|---|
| 1 | `accurate-communication.md` | `accurate-communication.design.md v2.27` | Evidence-calibrated status, claim-state wording, meaning-first identifier gloss, and phase closeout wording |
| 2 | `action-safety.md` | `action-safety.design.md v1.0` | Destructive/high-impact action safety, topology control, emergency posture, and bounded retry handling |
| 3 | `audience-surface-disclosure-control.md` | `audience-surface-disclosure-control.design.md v1.0` | Direct-user transparency plus audience-appropriate generated public/operator/customer disclosure |
| 4 | `authority-and-scope.md` | `authority-and-scope.design.md v2.5` | User authority, hard-boundary precedence, and source/project ownership boundaries |
| 5 | `coding-discipline.md` | `coding-discipline.design.md v1.1` | Maintainable code structure, verification strategy, coding/debug root-cause narrowing, and tactical-to-strategic convergence |
| 6 | `communication-register.md` | `communication-register.design.md v1.5` | Natural professional tone, user-aligned easy explanation, anti-over-agreement, and signal discipline |
| 7 | `document-governance.md` | `document-governance.design.md v1.8` | Repository document roles, parent/shard authority, append-vs-shard doctrine, patch governance, and UDVC-1 |
| 8 | `document-integrity.md` | `document-integrity.design.md v1.6` | Cross-reference consistency, rollover integrity, document-density/God-file repair, and no-delete-by-cleanup discipline |
| 9 | `evidence-discipline.md` | `evidence-discipline.design.md v1.2` | Verify-first factual discipline, concern-vs-conclusion discipline, scoped non-findings, and real-vs-mock boundaries |
| 10 | `execution-and-goal-frame.md` | `execution-and-goal-frame.design.md v1.6` | Discussion/execution mode, visible intent read, premise separation, next-work boundaries, and lineage-first phase-shaped continuation |
| 11 | `explanation-and-presentation.md` | `explanation-and-presentation.design.md v1.3` | Plain-language explanation, meaning-first identifier walkthroughs, diagram discipline, and concise action framing |
| 12 | `external-verification-and-source-trust.md` | `external-verification-and-source-trust.design.md v1.2` | External source verification, trust ranking, corroboration, and source-conflict handling |
| 13 | `memory-governance-and-session-boundary.md` | `memory-governance-and-session-boundary.design.md v1.7` | Scoped memory governance, compact memory index behavior, path scope, and optional recall boundaries |
| 14 | `phase-todo-artifact.md` | `phase-todo-artifact.design.md v1.9` | Startup artifact posture, phase execution, compact TODO/phase entrypoints, live task tracking, and lineage-first phase identity selection |
| 15 | `portable-implementation-and-hardcoding-control.md` | `portable-implementation-and-hardcoding-control.design.md v1.3` | Portable defaults, late-bound environment resolution, and source/destination notation discipline |
| 16 | `refusal-and-recovery.md` | `refusal-and-recovery.design.md v1.1` | Wrapper normalization, refusal classification, minimization, and recovery paths |
| 17 | `safe-io.md` | `safe-io.design.md v1.3` | Bounded file reading/output with parent-first and smallest-shard-first behavior |
| 18 | `worker-routing-and-context.md` | `worker-routing-and-context.design.md v1.9` | Intent taxonomy, worker routing, diagnosis-first mixed-intent handling, and the routing decision boundary for document-heavy work |

---

## Category View

### Communication, Explanation, and Disclosure
- Rules: `accurate-communication`, `communication-register`, `explanation-and-presentation`, `audience-surface-disclosure-control`
- Purpose: keep user-facing communication clear, evidence-calibrated, naturally professional, readable, and audience-safe

### Evidence, Authority, and Safety
- Rules: `evidence-discipline`, `authority-and-scope`, `refusal-and-recovery`, `action-safety`
- Purpose: separate verified fact from inference, preserve user authority inside hard boundaries, recover safely from blocked requests, and gate destructive or high-impact action

### Execution, Coding, and Worker Control
- Rules: `execution-and-goal-frame`, `coding-discipline`, `worker-routing-and-context`, `safe-io`
- Purpose: keep active work goal-aligned, maintainable, proportionately verified, context-safe, and delegated only when worker lanes add value

### Governance, Memory, and Portability
- Rules: `document-governance`, `document-integrity`, `phase-todo-artifact`, `memory-governance-and-session-boundary`, `portable-implementation-and-hardcoding-control`, `external-verification-and-source-trust`
- Purpose: keep repository docs governed, path-normalized when broad, cross-references consistent, startup/phase/TODO surfaces aligned, memory scoped, shared artifacts portable, and external facts source-ranked
