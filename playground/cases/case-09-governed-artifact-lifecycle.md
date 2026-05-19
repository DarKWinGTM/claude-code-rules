# Case 09 — Governed Artifact Lifecycle

## What this case proves

This case family shows how RULES keep design, changelog, TODO, phase, patch, and related repo surfaces synchronized under the right owners instead of letting documentation drift or bloat into one file.

---

## Scenario family

- Primary family: governed artifact lifecycle
- Current status: governed baseline; checked observed examples present; virtual variants available

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
- preserve history by rollover/sharding rather than deletion when files grow too large
- verify cross-surface sync before claiming no-drift or release-ready status

---

## Observed case

Checked observed examples in repo scope:
- released recent waves are recorded through synchronized README/design/changelog/TODO/phase/patch surfaces rather than one-off local notes
- `v10.17 / P109` and `v10.18 / P110` both show phase, patch, changelog detail, master surfaces, and release records moving together under the governed model
- these observed effects are recorded in `playground/observed/2026-05.md` as `O-2026-05-03` and `O-2026-05-05`

---

## Virtual variant

- A new design family is needed but README is the only edited file.
- `TODO.md` grows by absorbing completed closeout history directly into the active section.
- A patch starts behaving like a live phase workspace instead of a before/after review surface.

Expected behavior: create or repair the proper owner surface instead of overloading the wrong one.

---

## Example dialogue (virtual)

### User
`Add this new governed family to the repo.`

### AI without this rule family risk
`I updated README with a new section.`

### AI with RULES active
`This needs the proper owner surfaces, so I will open design, changelog, TODO, phase, and patch where they are actually required instead of letting README carry the whole change.`

---

## Flow diagram

```text
New governed work is selected
  ↓
Startup posture is resolved
  ↓
Correct owner surfaces are opened
  ↓
Family files are created and synced
  ↓
No-drift / release-ready checks happen on the right artifacts
```

---

## Matrix axes in play

- request type: design sync / release sync / phase planning / rollover repair
- evidence state: usually checked locally across several repo surfaces
- scope clarity: multi-surface but owner-aligned
- risk level: medium
- expected rule response: sync the correct owner surfaces and preserve history cleanly

---

## Behavior delta

Without this family, governed docs can drift, duplicate authority, or turn into God files.

With RULES active, the repository should stay easier to navigate because each document family keeps its own role.
