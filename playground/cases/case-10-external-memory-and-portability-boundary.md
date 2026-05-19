# Case 10 — External, Memory, and Portability Boundary

## What this case proves

This case family shows how RULES stop current external facts, remembered context, and local machine details from being blended into one unreliable answer.

---

## Scenario family

- Primary family: external, memory, and portability boundary
- Current status: governed baseline; checked observed examples present; virtual variants available

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
- distinguish source-side repo paths from runtime/install destinations

---

## Observed case

Checked observed examples in repo scope:
- the released `v10.18 / P110` wave moved install guidance to clone → launcher with project-local `.claude/rules/` as the primary target and explicitly removed unsupported Codex/Gemini install-surface claims in touched scope
- this observed effect is recorded in `playground/observed/2026-05.md` as `O-2026-05-01`

---

## Virtual variant

- User asks for install guidance using an exact local machine path as if it were a shared default.
- Memory says a path or file existed earlier, but the repo may have changed.
- An external CLI/API behavior claim matters to the user’s next decision and may have drifted.

Expected behavior: verify current facts, preserve path scope, and keep shared docs portable.

---

## Example dialogue (virtual)

### User
`Use the old path from memory and write the install guide with it.`

### AI without this rule family risk
`Sure — use /home/node/... as the default install path.`

### AI with RULES active
`I can use that exact path as a checked local fact for this machine, but shared install guidance should stay portable. I will verify the current source and then write the guide with `<project-root>` or another portable contract label.`

---

## Flow diagram

```text
Memory or external fact enters the decision
  ↓
Current source-of-truth is re-checked
  ↓
Local fact is separated from shared contract
  ↓
Portable wording is chosen for shared docs
  ↓
Exact local detail stays scoped instead of becoming the default
```

---

## Matrix axes in play

- request type: install guidance / external fact / memory reuse / path-specific recommendation
- evidence state: verified / recalled / stale risk / external-drift risk
- scope clarity: mixed until source-of-truth is checked
- risk level: medium
- expected rule response: verify, recheck, and keep shared contracts portable

---

## Behavior delta

Without this family, the assistant can treat memory or local machine detail as if it were a portable current default.

With RULES active, external facts, memory, and portability boundaries stay separated more cleanly.
