# Technical Snapshot Communication Design

## 0) Document Control

> **Parent Scope:** RULES System Design
> **Current Version:** 1.0
> **Session:** a9bec472-1706-4019-8cfd-5ba988a71662 (2026-04-17)

---

## 1) Goal

Define one first-class rule chain that owns the wording of compact technical snapshots so exact captured facts, partial checked facts, inferred implications, and scoped local environment facts remain clearly separated in technical status communication.

This chain should make troubleshooting/progress/verification snapshots easier to trust without replacing evidence-taxonomy, presentation-layout, or explanation-flow owners.

---

## 2) Problem Statement

Observed failure modes:
- partial evidence is phrased as if the exact request, payload, or runtime state had been captured
- local paths, ports, hosts, or env values are reported in snapshots as if they were shared portable defaults
- technical progress updates are reported as loose prose, making checked scope, current state, pending state, and next action harder to scan
- inferred implications are mixed into exact facts, making the snapshot read more certain than the evidence supports

The repository needs one explicit owner for the communication shape of compact technical snapshots.

---

## 3) Core Principles

### 3.1 Snapshot-Layer Separation Principle
The chain should keep exact captured facts, partial checked facts, inferred implications, and exact-detail-unavailable wording visibly separate.

### 3.2 Scoped Local-Fact Principle
Exact local paths, ports, hosts, and similar values should stay scoped as observed local facts when they appear in snapshots.

### 3.3 Diagnostic Snapshot Content Principle
Compact technical snapshots should show what was checked, what is currently true, what remains pending, and what action follows when those details materially help the reader.

### 3.4 Boundary Principle
This chain owns **snapshot wording semantics** only.
It should not replace:
- evidence-taxonomy ownership
- snapshot layout/presentation ownership
- explanation-flow ownership
- broader portability/anti-hardcoding ownership

---

## 4) Application Model

Use this chain when:
- reporting troubleshooting progress
- reporting implementation progress with mixed completed/pending state
- reporting verification checkpoints where current state and remaining gates must be visible
- summarizing request, environment, or runtime details from incomplete checked scope
- exact local environment facts appear in a compact technical snapshot

---

## 5) Communication Model

| Snapshot Layer | Preferred Communication Shape |
|---------------|-------------------------------|
| Exact captured facts | "Captured request path: ..." / "The checked log line shows ..." |
| Partial checked facts | "From the checked scope, ..." |
| Inferred implications | "Based on those checked facts, the likely implication is ..." |
| Exact detail unavailable | "I could not capture the exact payload/request, but ..." |

---

## 6) Examples

- "Captured request path: `/api/runtime/assign`."
- "I could not capture the exact request payload, but from the checked scope the request involved the runtime assignment route plus the current gateway environment."
- "Based on those checked facts, the likely implication is that the failure sits between request routing and runtime-target resolution, not in initial client boot."
- "Diagnostic snapshot: Checked / Current state / Pending / Next action"

---

## 7) Anti-Patterns

- partial evidence phrased like exact capture
- local environment facts phrased like shared defaults
- status updates with no compact checked/current/pending/next snapshot
- inferred implications blended into observed facts without wording separation

---

## 8) Success Criteria

This chain succeeds when:
- snapshot wording no longer overclaims exact capture from partial evidence
- compact technical snapshots are easier to scan and trust
- local environment values remain visibly scoped as local facts
- adjacent owners can defer snapshot semantics cleanly without duplicating them

---

## 9) Integration

| Rule | Relationship |
|------|--------------|
| [../accurate-communication.md](../accurate-communication.md) | Keeps broader communication honesty and claim-strength wording outside snapshot-specific ownership |
| [evidence-grounded-burden-of-proof.design.md](evidence-grounded-burden-of-proof.design.md) | Owns evidence taxonomy and burden thresholds |
| [answer-presentation.design.md](answer-presentation.design.md) | Owns snapshot layout and presentation patterns |
| [explanation-quality.design.md](explanation-quality.design.md) | Owns explanation-flow placement for snapshots |
| [portable-implementation-and-hardcoding-control.design.md](portable-implementation-and-hardcoding-control.design.md) | Owns broader portable-default versus local-observation discipline |

---

> Full history: [../changelog/technical-snapshot-communication.changelog.md](../changelog/technical-snapshot-communication.changelog.md)
