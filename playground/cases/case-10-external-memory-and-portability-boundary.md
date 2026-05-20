# Case 10 — External, Memory, and Portability Boundary

## What this case proves

This case family shows how RULES stop current external facts, remembered context, and local machine details from being blended into one unreliable answer.

---

## Scenario family

- Primary family: external, memory, and portability boundary
- Current status: transcript-grounded observed examples present; virtual variants available

---

## Governing rules

- `external-verification-and-source-trust.md` — authoritative external verification and conflict handling
- `memory-governance-and-session-boundary.md` — memory is scoped context, not current truth
- `portable-implementation-and-hardcoding-control.md` — placeholders and late binding for shared artifacts
- `evidence-discipline.md` — verify local facts before stating them strongly
- `document-governance.md` — public onboarding/install guidance stays portable by default
- `document-integrity.md` — source/runtime scope and reference consistency stay explicit

---

## Rule-enforced fact

Current RULES require the assistant to:
- verify material external facts when they affect the recommendation
- recheck path-scoped memory before using it as current exact repo truth
- keep shared artifacts portable by default instead of hardcoding local paths as defaults
- distinguish source-side repo paths from runtime or install destinations

---

## Observed case

Checked transcript-derived example:
- Transcript path: `<claude-project-scope-root>/1b81d009-cf82-44a3-9739-cd3ea4af34dd/subagents/agent-a11775f8a9be66221.jsonl`
- Anchor hints: `Short answer: จาก official Claude Code docs ที่เช็กแล้ว`, `Official plugin structure/reference ไม่ได้ list`, `claude --plugin-dir`, `/plugin install`
- Observed effect: the answer was narrowed to what official Claude Code plugin docs actually support instead of overclaiming that plugin installation also covers `.claude/rules/` or `CLAUDE.md` surfaces.
- Scope note: this proves external-doc verification plus boundary narrowing in that checked session; it does not mean all install surfaces are interchangeable.

Supporting repo-scope install-boundary behavior is also recorded in `playground/observed/2026-05.md` as `O-2026-05-01`.

---

## Virtual variant

- User asks for install guidance using an exact local machine path as if it were a shared default.
- Memory says a path or file existed earlier, but the repo may have changed.
- An external CLI or API behavior claim matters to the user’s next decision and may have drifted.

Expected behavior: verify current facts, preserve path scope, and keep shared docs portable.

---

## User objective

Answer a question that mixes current external facts, remembered context, and local-path convenience without turning them into one unsupported recommendation.

---

## Operational reality

- External docs may have changed.
- Path-scoped memory can help continuity but may not reflect current repo truth.
- An exact local machine path can be real in one environment while still being the wrong shared default.

---

## RULES effect on execution

- Verify the external fact before leaning on it.
- Recheck memory before using it as current exact truth.
- Keep shared wording portable and separate local exact paths from reusable guidance.

---

## Decision

Narrow the answer to checked support, and treat any exact local path as a scoped local fact rather than a portable default.

---

## What AI does next

- Check the official or current authoritative source.
- Separate remembered context from freshly checked fact.
- Use placeholders or late-bound wording for shared artifacts.

---

## Recovery path

- If the user truly needs a machine-scoped example, provide it explicitly as local-only context.
- If support remains unclear, keep the answer bounded instead of overclaiming equivalence.

---

## User-visible reply example

`The checked docs support the plugin surface only. For shared guidance I will keep the path portable, and I will mention an exact local path only if you need a machine-scoped example.`

---

## Flow diagram

```text
Memory or external fact enters the decision
  ↓
Current source-of-truth is re-checked
  ↓
Supported install surface is narrowed
  ↓
Local fact is separated from shared contract
  ↓
Portable wording is chosen for shared docs
```

---

## Matrix axes in play

- request type: install guidance / external fact / memory reuse / path-specific recommendation
- evidence state: verified / recalled / stale-risk / external-drift risk
- scope clarity: mixed until source-of-truth is checked
- risk level: medium
- expected rule response: verify, recheck, and keep shared contracts portable
- turn count: 3
- user behavior: request mixes current support claim with local-path convenience
- evidence source: official docs, memory, and local-path context
- failure mode: overclaim risk plus portability drift
- tool discovery or lane shape: external-doc verification
- completion state: narrowed recommendation after verification

---

## Behavior delta

Without this family, the assistant can treat memory or local machine detail as if it were a portable current default.

With RULES active, external facts, memory, and portability boundaries stay separated more cleanly.
