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
- create new Patch artifacts from one verified UTC creation instant using `YYYY-MM-DDTHH-mm-ssZ--<semantic-slug>.patch.md`, matching `Created At`/Creation Evidence, exclusive collision refusal, and no Patch ID/index
- keep the active changelog parent as current-version/map/navigation authority, indexed same-chain shards as active version detail, and `changelog/done/` as inactive reference/provenance history rather than a fallback owner
- preserve history by rollover or sharding rather than deletion when files grow too large
- verify cross-surface sync before claiming no-drift or release-ready status

---

## Observed case

Checked transcript-derived example:
- Transcript path: `<claude-project-scope-root>/0c68a707-81d9-4d1a-bcda-6fc04ae11efc.jsonl`
- Anchor hints: `rollover / compact current index`, `Completed status ไม่ใช่ deletion authority`, `TODO.md`, `phase/SUMMARY.md`
- Observed effect: oversized `TODO.md` and `phase/SUMMARY.md` were compacted through rollover while preserving current-state navigation and completed-history reachability.
- Scope note: this proves lifecycle-preserving rollover behavior in that checked session; it does not authorize broad deletion or arbitrary restructuring elsewhere.

Supporting repo-scope master-surface sync behavior is also recorded in `playground/observed/2026-05.md` as `O-2026-05-05`.

---

## Virtual variant

- A new design family is needed but README is the only edited file.
- `TODO.md` grows by absorbing completed closeout history directly into the active section.
- A patch starts behaving like a live phase workspace instead of a before/after review surface.
- A repair instruction calls indexed active changelog version detail `fallback` and treats inactive `changelog/done/` history as an ordinary resolution source.
- An ordinary wording-only design edit is proposed with no structural or visual change; diagram posture may be `not required`.
- A folder-topology or visual-authority change is proposed; startup must evaluate diagram after design, while subject diagrams open only for a real visual question.
- A new Patch is proposed from separate clock reads, collision auto-suffixing, a Patch ID or `patch/INDEX.md`, or mtime/ctime-based creation metadata.
- A legacy Patch rename proposes global basename replacement, serialized request-payload rewriting, or normalization of a suspended archive.

Expected behavior: create or repair the proper owner surface instead of overloading the wrong one. Correct the changelog roles explicitly: active parent for current version/map/navigation, indexed same-chain shard for active detail, inactive `done/` for reference/provenance only, and no fallback owner. For Patch chronology, capture UTC once, create exclusively, keep filename and metadata equivalent, require admissible evidence for legacy rows, update only exact governed references through a hash-bound manifest, and preserve suspended archives unchanged and inactive.

---

## User objective

Repair or extend governed documentation without letting current-state, history, and owner roles drift into one overloaded surface.

---

## Operational reality

- Several governed surfaces can be in play at once: design, changelog, TODO, phase, patch, and README.
- Large active files often need rollover or sharding, but that is preservation work rather than cleanup deletion.
- The main risk is owner drift and history loss, not only file size.

---

## RULES effect on execution

- Choose the correct owner surface before editing.
- Evaluate diagram after design when structure, visual authority, diagram relationships, visual topology, or existing diagram correctness changes; ordinary design edits may mark it `not required` without opening a subject diagram.
- Route changelog current state, indexed active detail, and inactive history to distinct governed roles without fallback semantics.
- Give each new Patch verified original-creation chronology without IDs/indexes; block ambiguous legacy migration rather than infer timestamps.
- Propagate legacy renames only through exact resolved references and preserve excluded serialized payloads plus suspended archives.
- Preserve history by rollover or sharding instead of deletion.
- Verify cross-surface sync before claiming no-drift or release readiness.

---

## Decision

Treat the issue as governed-structure repair under the correct owner, not as generic cleanup.

---

## What AI does next

- Classify which owner surface should hold the new or moved content.
- Compact the active entrypoint if it is oversized.
- Update references and verify sync across the touched surfaces.

---

## Recovery path

- If the split is broad or owner boundaries are unclear, open a bounded repair slice instead of forcing an unsafe compact.
- If history must move, preserve reachability and bidirectional references.

---

## User-visible reply example

`This is a governed-structure repair, not a generic cleanup. I should compact the active index, preserve history, and sync the owner surfaces before calling it aligned.`

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
