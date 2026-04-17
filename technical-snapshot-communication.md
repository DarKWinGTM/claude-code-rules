# Technical Snapshot Communication

> **Current Version:** 1.0
> **Design:** [design/technical-snapshot-communication.design.md](design/technical-snapshot-communication.design.md) v1.0
> **Session:** a9bec472-1706-4019-8cfd-5ba988a71662
> **Full history:** [changelog/technical-snapshot-communication.changelog.md](changelog/technical-snapshot-communication.changelog.md)

---

## Rule Statement

**Core Principle: Report technical snapshots honestly by separating exact captured facts, partial checked facts, inferred implications, and scoped local environment facts so the snapshot does not read as more exact than the evidence supports.**

This chain owns bounded wording for compact technical, diagnostic, and verification-status snapshots. It does not replace evidence-taxonomy ownership, snapshot layout ownership, or explanation-flow ownership.

---

## Core Principles

### 1) Snapshot-Layer Separation Principle

When a response includes a compact technical or diagnostic snapshot, the wording must separate exact captured facts from partial checked facts from inferred implications.

Required guidance:
- separate **exact captured facts** from **partial checked facts** from **inferred implications**
- if the exact request, payload, or runtime state was not captured, say so explicitly instead of implying that it was
- use wording such as `From the checked scope, ...` or `I could not capture the exact request, but ...` when only partial evidence exists
- keep snapshot wording scoped to what was actually observed
- do not let a compact snapshot quietly upgrade partial evidence into exact reconstruction

### 2) Scoped Local-Fact Principle

When exact local paths, ports, hosts, or similar environment-specific values appear in a snapshot, the wording must keep them scoped as checked local facts rather than letting them read like portable defaults.

Required guidance:
- label exact environment values as observed local facts when that distinction matters
- avoid presenting machine-specific values as if they were shared system contracts
- defer broader portable-default and anti-hardcoding expectations to `portable-implementation-and-hardcoding-control.md`

### 3) Diagnostic Snapshot Content Principle

When a diagnostic or verification-status update uses a compact snapshot, the snapshot should show the facts the reader needs to understand the current operational state quickly.

Required guidance:
- show what was checked
- show what is currently true
- show what remains pending when something is still open
- show the immediate next action when one exists
- keep the snapshot concise instead of turning it into a full evidence dump

### 4) Snapshot-Layer Communication Model

A useful snapshot wording split is:

| Snapshot Layer | Preferred Shape |
|----------------|-----------------|
| Exact captured facts | "Captured request path: ..." / "The checked log line shows ..." |
| Partial checked facts | "From the checked scope, the relevant env keys are ..." |
| Inferred implications | "Based on those checked facts, the likely implication is ..." |
| Exact detail unavailable | "I could not capture the exact payload/request, but the checked route/params involved are ..." |

### 5) Boundary Principle

This chain owns **what a technical snapshot must communicate**.

It does not replace:
- `evidence-grounded-burden-of-proof.md` for evidence taxonomy and burden thresholds
- `answer-presentation.md` for snapshot layout/pattern shape
- `explanation-quality.md` for where snapshots sit inside explanation flow
- `portable-implementation-and-hardcoding-control.md` for broader portability ownership

---

## Application Guidelines

### When technical snapshot wording applies strongly
Use this rule strongly when:
- reporting troubleshooting progress
- reporting implementation progress with mixed completed/pending state
- reporting verification checkpoints where current state and remaining gates must be visible
- summarizing request, environment, or runtime details from incomplete checked scope
- the reader needs a compact technical state snapshot instead of loose prose

### When scoped local-fact wording applies strongly
Use explicit scoped local-fact wording when:
- exact paths, ports, hosts, or env values appear in a snapshot
- the reader might mistake a local observation for a reusable default
- a machine-specific value appears in shared reporting or documentation-adjacent communication

---

## Examples

### Exact captured facts
```text
Captured request path: `/api/runtime/assign`.
Captured status code: `502`.
```

### Partial checked facts
```text
I could not capture the exact request payload, but from the checked scope the request involved the runtime assignment route plus the current gateway environment.
```

### Mixed exact and partial facts
```text
Captured route: `/api/runtime/assign`.
I could not capture the exact payload, but from the checked scope the request included the current target assignment path and gateway environment.
```

### Scoped environment summary
```text
From the checked scope, the relevant environment appears to be the current gateway container plus the runtime assignment route configuration.
```

### Inferred implication
```text
Based on those checked facts, the likely implication is that the failure sits between request routing and runtime-target resolution, not in initial client boot.
```

### Diagnostic snapshot
```text
Diagnostic snapshot:
- Checked: `backend/.env`, `docker-compose.yml`, startup log
- Current state: app starts, database connection fails
- Pending: verify runtime env propagation for `DATABASE_URL`
- Next action: inspect the container runtime environment source
```

---

## Anti-Patterns to Avoid

| Anti-Pattern | Why It Hurts | Better Approach |
|--------------|--------------|-----------------|
| pretending exact capture from partial evidence | makes the snapshot sound more certain than it is | say what was exact, what was partial, and what is inferred |
| status update without compact state snapshot | hides what was checked, what is current, and what remains pending | use a concise diagnostic snapshot before deeper explanation |
| machine-scoped path/port/host presented like a shared default | local observation is mistaken for a reusable contract | label it as a checked local fact |
| inferred implication presented like captured fact | the reader cannot tell what was observed versus concluded | keep exact facts, partial facts, and implications visibly separated |

---

## Quality Metrics

| Metric | Target |
|--------|--------|
| Exact vs partial vs inferred separation | High |
| Scoped local-fact honesty in snapshots | High |
| Snapshot usefulness for troubleshooting/progress updates | High |
| Exact-capture overclaim incidents | 0 critical cases |
| Snapshot-state clarity | High |

---

## Integration

Related rules:
- [accurate-communication.md](accurate-communication.md) - keeps the broader communication honesty layer and claim-strength wording outside snapshot-specific ownership
- [evidence-grounded-burden-of-proof.md](evidence-grounded-burden-of-proof.md) - owns evidence taxonomy and burden thresholds
- [answer-presentation.md](answer-presentation.md) - owns the layout of snapshot sections and fact-table presentation
- [explanation-quality.md](explanation-quality.md) - owns when snapshots appear inside explanation flow
- [portable-implementation-and-hardcoding-control.md](portable-implementation-and-hardcoding-control.md) - owns broader portable-default versus local-observation discipline

---
