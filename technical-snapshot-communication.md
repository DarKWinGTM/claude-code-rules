# Technical Snapshot Communication

> **Current Version:** 1.0
> **Design:** [design/technical-snapshot-communication.design.md](design/technical-snapshot-communication.design.md) v1.0
> **Session:** a9bec472-1706-4019-8cfd-5ba988a71662
> **Full history:** [changelog/technical-snapshot-communication.changelog.md](changelog/technical-snapshot-communication.changelog.md)

---

## Rule Statement

**Core Principle: Report technical snapshots by separating exact captured facts, partial checked facts, inferred implications, and scoped local facts so compact status wording does not overclaim.**

This chain owns bounded wording for compact technical, diagnostic, and verification-status snapshots. Evidence taxonomy, snapshot layout, explanation flow, and portability remain owned by their specialist rules.

---

## Core Principles

### 1) Snapshot-Layer Separation Principle

When a response includes a compact technical or diagnostic snapshot, separate **exact captured facts**, **partial checked facts**, **inferred implications**, and **exact detail unavailable**.

Required guidance:
- if the exact request, payload, or runtime state was not captured, say so
- use wording such as `From the checked scope, ...` or `I could not capture the exact request, but ...` when evidence is partial
- keep snapshot wording scoped to what was actually observed
- do not let a compact snapshot upgrade partial evidence into exact reconstruction

### 2) Scoped Local-Fact Principle

Exact local paths, ports, hosts, and environment values in a snapshot must read as checked local facts, not portable defaults.

Required guidance:
- label environment-specific values as observed local facts when the distinction matters
- avoid presenting machine-specific values as shared contracts
- defer broader portable-default discipline to `portable-implementation-and-hardcoding-control.md`

### 3) Diagnostic Snapshot Content Principle

A diagnostic or verification-status snapshot should show only the facts needed to understand current operational state quickly: what was checked, what is currently true, what remains pending, and the immediate next action when one exists.

Keep snapshots concise; do not turn them into evidence dumps.

### 4) Boundary Principle

This chain owns what a technical snapshot must communicate. It does not replace:
- `evidence-grounded-burden-of-proof.md` for evidence taxonomy and burden thresholds
- `answer-presentation.md` for snapshot layout and fact-table shape
- `explanation-quality.md` for snapshot placement inside explanation flow
- `portable-implementation-and-hardcoding-control.md` for broader portability ownership

---

## Snapshot Wording Model

| Snapshot layer | Preferred wording shape |
|---|---|
| Exact captured facts | `Captured request path: ...` / `The checked log line shows ...` |
| Partial checked facts | `From the checked scope, ...` |
| Inferred implication | `Based on those checked facts, the likely implication is ...` |
| Exact detail unavailable | `I could not capture the exact payload/request, but ...` |

Example:
```text
Diagnostic snapshot:
- Checked: `backend/.env`, `docker-compose.yml`, startup log
- Current state: app starts, database connection fails
- Pending: verify runtime env propagation for `DATABASE_URL`
- Next action: inspect the container runtime environment source
```

Use this rule strongly for troubleshooting progress, mixed done/pending implementation status, verification checkpoints, incomplete request/environment/runtime details, and exact local values that could be mistaken for portable defaults.

---

## Anti-Patterns to Avoid

| Anti-pattern | Better approach |
|---|---|
| pretending exact capture from partial evidence | say what was exact, partial, and inferred |
| status update without compact state | show checked/current/pending/next |
| machine-scoped path/port/host as shared default | label it as checked local fact |
| inferred implication presented as captured fact | keep observation and conclusion separate |

---

## Quality Metrics

| Metric | Target |
|---|---|
| Exact/partial/inferred separation, scoped local-fact honesty, and snapshot usefulness | High |
| Exact-capture overclaim incidents | 0 critical cases |

---

## Integration

Related rules:
- [accurate-communication.md](accurate-communication.md) - broader evidence-honest wording
- [evidence-grounded-burden-of-proof.md](evidence-grounded-burden-of-proof.md) - evidence taxonomy and burden thresholds
- [answer-presentation.md](answer-presentation.md) - snapshot layout and fact-table presentation
- [explanation-quality.md](explanation-quality.md) - snapshot placement inside explanation flow
- [portable-implementation-and-hardcoding-control.md](portable-implementation-and-hardcoding-control.md) - portable-default versus local-observation discipline

---
