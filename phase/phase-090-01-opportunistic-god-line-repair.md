# Phase 090-01 - Opportunistic God-Line Repair

> **Summary File:** [SUMMARY.md](SUMMARY.md)
> **Phase ID:** 090-01
> **Status:** In Progress
> **Session:** d42465eb-30a7-4bc8-b9d6-03e52306e9a5
> **Design References:**
> - [../design/design.md](../design/design.md)
> - [../design/context-load-and-document-density-control.design.md](../design/context-load-and-document-density-control.design.md)
> - [../design/document-consistency.design.md](../design/document-consistency.design.md)
> **Patch References:** [../patch/opportunistic-god-line-repair.patch.md](../patch/opportunistic-god-line-repair.patch.md)

---

## Objective

Refine the context-load and document-density owner so touched active documents do not only warn about God lines. When a touched God-line candidate has a clear, low-risk semantic split, the assistant should repair it in the same edit; when the split is broad, history-heavy, or meaning-risky, it should flag or plan the repair instead of appending more content.

พูดง่าย ๆ: ถ้า AI กำลังแก้เอกสารตรงนั้นอยู่แล้ว และเห็นบรรทัดยักษ์ที่แยกความหมายได้ชัดเจน ก็ควรช่วยแตกบรรทัดให้เลย ไม่ใช่เติมต่อให้ยาวขึ้นอีก.

---

## Why This Phase Exists

P090 added the owner for context-load and document-density control. The follow-up gap is execution behavior when a God-line candidate is actually encountered during a touched-doc edit.

This phase exists because prevention alone is not enough. The runtime rule needs a bounded repair posture:
- repair locally when the touched line is clear and low-risk
- preserve meaning and active document roles
- avoid repo-wide auto-formatting or broad historical rewrites
- flag or plan risky density debt instead of silently appending

---

## Entry Conditions

- P090 / v9.97 context-load and document-density control is completed, installed, pushed, and released.
- Active runtime count before this phase is 47.
- The requested change refines the P090 owner rather than creating a new runtime owner.
- Runtime destination extras remain observed-only and outside cleanup scope.

---

## Expected Output

- `context-load-and-document-density-control` runtime/design/changelog advances to v1.1.
- Opportunistic God-line repair doctrine is installed in the active runtime rule.
- README, master design/changelog, TODO, phase, and patch records align to v9.98 / P090-01.
- README Bash and PowerShell install arrays remain exactly 47 active runtime rule files.
- Runtime install copies the same 47 README-listed source-owned active runtime rules.
- Source/runtime parity and active runtime body sufficiency pass for 47/47 files.
- Density checks confirm touched active docs do not introduce new God-line regressions.
- `master` push and GitHub release `v9.98` are verified.

---

## Implementation Plan

### 1) Open governed execution records

- Create this P090-01 phase record.
- Create `patch/opportunistic-god-line-repair.patch.md` as the before/after review surface.
- Track P090-01 in `TODO.md` and `phase/SUMMARY.md` until release gates pass.

### 2) Refine context-load owner chain

- Update `context-load-and-document-density-control.md` to v1.1.
- Update `design/context-load-and-document-density-control.design.md` to v1.1.
- Update `changelog/context-load-and-document-density-control.changelog.md` to v1.1.

### 3) Sync master records

- Update `design/design.md` to v9.98 while keeping active runtime count at 47.
- Update `changelog/changelog.md` with v9.98 history.
- Update `README.md` current-state cards, latest refinement wording, and quality signals without changing install arrays.
- Update `TODO.md`, `phase/SUMMARY.md`, this phase record, and the P090-01 patch as gates progress.

### 4) Verify, install, push, and release

- Verify README Bash and PowerShell install arrays contain the same 47 files.
- Verify the refined rule/design/changelog chain aligns at v1.1.
- Install only README-listed active runtime rules into `/home/node/.claude/rules/`.
- Verify source/runtime parity and body sufficiency for all 47 active runtime files.
- Run density-oriented checks on touched active docs.
- Commit the governed changes.
- Push `master`.
- Publish and verify GitHub release `v9.98`.

---

## Out of Scope

- No new active runtime rule; active runtime count remains 47.
- No repo-wide automatic God-line rewrite.
- No rewriting history/done shards unless directly needed for a touched active surface.
- No deletion or cleanup of runtime destination extras.
- No replacement of `safe-file-reading`, worker routing, rollover, or document-consistency owners.

---

## Affected Artifacts

### Refined runtime owner chain

- `context-load-and-document-density-control.md`
- `design/context-load-and-document-density-control.design.md`
- `changelog/context-load-and-document-density-control.changelog.md`

### Master records and tracking files

- `design/design.md`
- `changelog/changelog.md`
- `README.md`
- `TODO.md`
- `phase/SUMMARY.md`
- `patch/opportunistic-god-line-repair.patch.md`
- `phase/phase-090-01-opportunistic-god-line-repair.md`

### Runtime destination

- `/home/node/.claude/rules/context-load-and-document-density-control.md`
- Existing destination extras remain observed-only and out of cleanup scope.

---

## TODO and Changelog Coordination

- `TODO.md` records P090-01 as active during source sync and completed only after source audit, runtime install parity/body sufficiency, density review, git push, and release pass.
- `changelog/changelog.md` records v9.98 as current source version during P090-01 and uses final release wording only after runtime install, push, and release gates pass.
- README presents current-state guidance and latest refinement context, not a copied changelog timeline.

---

## Development Verification / TestKit Coverage

This is governance and runtime-rule work, not product code.

Verification route:
- `not_applicable_with_reason` for product TestKit because no product runtime behavior changes.
- Source/runtime parity and active runtime body sufficiency are the main runtime checks.
- README install-array parity and density checks are required closeout checks.

---

## Verification

- [ ] Phase and patch records exist and link correctly.
- [ ] Context-load owner chain advances to v1.1.
- [ ] Master records describe v9.98 / P090-01 consistently.
- [ ] README Bash and PowerShell install arrays remain exactly 47 active runtime rule files.
- [ ] Runtime install copies only README-listed active runtime rules.
- [ ] Source/runtime parity passes for 47 active runtime files.
- [ ] Active runtime body sufficiency passes for 47 active runtime files.
- [ ] Touched active docs pass a density-oriented check.
- [ ] `master` push and GitHub release `v9.98` are verified.

---

## Exit Criteria

- Opportunistic God-line repair doctrine is installed as part of the active context-load owner.
- P090-01 phase and patch records are synchronized.
- Master records describe v9.98 consistently.
- Active runtime count remains 47.
- Source consistency, runtime parity, body sufficiency, and density gates pass.
- Source/runtime release artifacts are pushed and released as `v9.98`.

---

## Risks and Rollback Notes

Risk:
- Opportunistic repair could be misread as permission for broad automatic document rewrites.

Mitigation:
- Restrict immediate repair to touched active docs where the semantic split is clear and low-risk.

Risk:
- A repair could accidentally change meaning in history-heavy or ambiguous lines.

Mitigation:
- Flag or plan broad, history-heavy, or meaning-risky repairs instead of changing them immediately.

Rollback:
- Narrow or remove the opportunistic repair wording through a governed rollback if it overreaches.
- Restore prior v9.97 master records only through governed rollback.
- Reinstall the v9.97 47-file runtime set only under an explicit rollback gate.
- Do not delete destination extras, completed P090 records, or history surfaces as cleanup.

---

## Closeout Summary

Pending until verification, push, and release gates pass.

---

## Next Possible Phases

- None selected during P090-01 startup.
