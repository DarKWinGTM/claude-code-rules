# Case 09 — Governed Artifact Lifecycle

## What this case proves

This case family shows how RULES keep design, changelog, TODO, phase, patch, and related repo surfaces synchronized under the right owners instead of letting documentation drift or bloat into one file.

---

## Scenario family

- Primary family: governed artifact lifecycle
- Current status: transcript-grounded observed examples present; virtual variants available

---

## Governing rules

- `phase-todo-artifact.md` — startup posture, phase execution, TODO/live-task separation
- `document-governance.md` — document-role boundaries, runtime body sufficiency, and sync order
- `document-integrity.md` — cross-reference consistency, rollover, no-delete-by-hygiene, and no-drift checks
- `safe-io.md` — parent-first reading, bounded entrypoint reads, and rollover signals
- `authority-and-scope.md` — repo-governed semantic meaning outranks git cleanliness or heuristics

---

## Rule-enforced fact

Current RULES require the assistant to:
- open or reuse the correct governed surfaces before meaningful work drifts
- keep design as target-state truth, changelog as version/history authority, TODO as compact durable index, phase as staged execution, and patch as before/after review
- preserve history by rollover or sharding rather than deletion when files grow too large
- verify cross-surface sync before claiming no-drift or release-ready status

---

## Observed case

Checked transcript-derived example:
- Transcript path: `/home/node/.claude/projects/-home-node-workplace-AWCLOUD-CLAUDE/0c68a707-81d9-4d1a-bcda-6fc04ae11efc.jsonl`
- Anchor hints: `rollover / compact current index`, `Completed status ไม่ใช่ deletion authority`, `TODO.md`, `phase/SUMMARY.md`
- Observed effect: oversized `TODO.md` and `phase/SUMMARY.md` were compacted through rollover while preserving current-state navigation and completed-history reachability.
- Scope note: this proves lifecycle-preserving rollover behavior in that checked session; it does not authorize broad deletion or arbitrary restructuring elsewhere.

Supporting repo-scope master-surface sync behavior is also recorded in `playground/observed/2026-05.md` as `O-2026-05-05`.

---

## Virtual variant

- A new design family is needed but README is the only edited file.
- `TODO.md` grows by absorbing completed closeout history directly into the active section.
- A patch starts behaving like a live phase workspace instead of a before/after review surface.

Expected behavior: create or repair the proper owner surface instead of overloading the wrong one.

---

## Example dialogue

### Dialogue label
`virtual trace patterned on a checked transcript-derived observed case`

### Turn 1 — User
`TODO.md and phase/SUMMARY.md are getting huge. Can you clean them up?`

### Turn 1 — AI without this rule family risk
`Sure, I’ll delete the completed parts so the active files stay short.`

### Turn 1 — AI with RULES active
`I need to preserve history and owner roles here. If the problem is entrypoint bloat, the safe repair is rollover and compact-current-index maintenance, not deleting completed work.`

### Turn 2 — Evidence, correction, or blocker
`The checked session shows TODO around 336 lines / 32.5 KB and the phase summary around 401 lines / 37.8 KB.`

### Turn 2 — AI without this rule family risk
`That confirms the old material is disposable.`

### Turn 2 — AI with RULES active
`That confirms a rollover trigger, not disposal authority. Active state should stay compact while moved history remains reachable through the right owner surfaces.`

### Turn 3 — Next-step narrowing / recovery / closeout
`The repo still needs current navigation after the cleanup.`

### Turn 3 — AI with RULES active
`I’ll keep TODO and phase as compact current entrypoints, move historical bulk into referenced history or done shards, and then verify that the active links still point to the right owner surfaces.`

---

## Flow diagram

```text
Active entrypoint grows too large
  ↓
Current state is separated from history bulk
  ↓
Correct owner surfaces are chosen
  ↓
Rollover preserves references and history reachability
  ↓
Compact active entrypoint remains the navigation surface
```

---

## Matrix axes in play

- request type: design sync / release sync / phase planning / rollover repair
- evidence state: checked locally plus transcript-grounded
- scope clarity: multi-surface but owner-aligned
- risk level: medium
- expected rule response: sync the correct owner surfaces and preserve history cleanly
- turn count: 3
- user behavior: cleanup-style request with lifecycle implications
- evidence source: local file-size facts plus transcript anchor
- failure mode: God-file drift and accidental history loss
- tool discovery or lane shape: direct governance repair
- completion state: compact current index with preserved history

---

## Behavior delta

Without this family, governed docs can drift, duplicate authority, or turn into God files.

With RULES active, the repository stays easier to navigate because each document family keeps its own role and large active entrypoints are compacted without losing meaning.
