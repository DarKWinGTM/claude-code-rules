# Phase 089 - Governed Design Sharding Compact Index

> **Summary File:** [SUMMARY.md](SUMMARY.md)
> **Phase ID:** 089
> **Status:** Active
> **Session:** d42465eb-30a7-4bc8-b9d6-03e52306e9a5
> **Design References:** [../design/design.md](../design/design.md), [../design/document-design-control.design.md](../design/document-design-control.design.md), [../design/project-documentation-standards.design.md](../design/project-documentation-standards.design.md), [../design/safe-file-reading.design.md](../design/safe-file-reading.design.md), [../design/document-consistency.design.md](../design/document-consistency.design.md)
> **Patch References:** [../patch/governed-design-sharding-compact-index.patch.md](../patch/governed-design-sharding-compact-index.patch.md)

---

## Objective

Add governed doctrine for large active design documents that need a compact active index plus governed child design shards. The goal is to preserve active target-state truth while preventing broad design reads from refilling context or causing autocompact thrash.

พูดง่าย ๆ: design หลักควรเป็นแผนที่ที่อ่านเร็ว ส่วนรายละเอียดเยอะ ๆ แยกเป็น shard ที่ยังเป็น active design ไม่ใช่ history/done.

---

## Why This Phase Exists

NodeClaw showed a healthy recovery pattern after `api-payg-ai-proxy-gateway.design.md` grew beyond practical active-read size: the main design became a compact index and detailed target-state content moved into `design/api-payg-ai-proxy-gateway/*.design.md` shards. Current RULES doctrine already covers active design bodies, no default `design/done`, and TODO/phase rollover, but it does not explicitly govern active design sharding.

This is a new main phase because governed design sharding is a distinct documentation architecture capability with its own output, verification gate, and read-path behavior. It is related to rollover and safe reading, but it is not merely another TODO/phase history rollover subphase.

---

## Entry Conditions

- P076-04 / v9.95 bounded main/subphase boundary refinement is complete, installed, pushed, and released.
- Active runtime count is 46.
- The user explicitly requested RULES improvement, runtime install, governed design/changelog/TODO/phase/patch sync, git push, release, and systematic phase planning.
- NodeClaw design sharding is evidence for RULES behavior only; this phase does not edit NodeClaw files.

---

## Expected Output

- `document-design-control` describes compact design index plus governed child design shard semantics.
- `project-documentation-standards` includes `design/<slug>/*.design.md` in the repository role model without creating a default `design/done` pattern.
- `safe-file-reading` uses index-first, shard-selective design reading for sharded active designs.
- `document-consistency` verifies index-to-shard references, shard role boundaries, orphan/stale shard risks, and no-drift claims.
- README, master design/changelog, TODO, phase, and patch records align to v9.96 / P089.
- Active runtime count remains 46.

---

## Implementation Plan

### 1) Open governed execution records

- Create this P089 phase record.
- Create `patch/governed-design-sharding-compact-index.patch.md` as the before/after review surface.
- Mark TODO and phase summary as active for P089 until verification/release gates pass.

### 2) Update design-sharding owner chains

- Update `document-design-control` runtime/design/changelog to v1.11.
- Update `project-documentation-standards` runtime/design/changelog to v2.38.
- Update `safe-file-reading` runtime/design/changelog to v1.6.
- Update `document-consistency` runtime/design/changelog to v1.10.

### 3) Sync master records

- Update `design/design.md` to v9.96 with active runtime count 46.
- Update `changelog/changelog.md` with v9.96 release history.
- Update `README.md` current-state guidance without turning it into a changelog dump.
- Update `TODO.md`, `phase/SUMMARY.md`, this phase record, and the P089 patch.

### 4) Verify, install, push, and release

- Verify README Bash and PowerShell install arrays remain aligned at exactly 46 active runtime files.
- Install only README-listed active runtime rules into `/home/node/.claude/rules/`.
- Verify source/runtime parity and body sufficiency for all 46 active runtime files.
- Commit the governed changes.
- Push `master`.
- Publish and verify GitHub release `v9.96`.

---

## Out of Scope

- No new active runtime rule file.
- No active runtime count increase.
- No default `design/done` surface.
- No conversion of governed child design shards into changelog/history shards.
- No direct edits to NodeClaw design files; NodeClaw is evidence only.
- No deletion or cleanup of runtime destination extras or unrelated files.

---

## Affected Artifacts

### Runtime owner chains

- `document-design-control.md`
- `project-documentation-standards.md`
- `safe-file-reading.md`
- `document-consistency.md`

### Design companions

- `design/document-design-control.design.md`
- `design/project-documentation-standards.design.md`
- `design/safe-file-reading.design.md`
- `design/document-consistency.design.md`

### Changelog companions

- `changelog/document-design-control.changelog.md`
- `changelog/project-documentation-standards.changelog.md`
- `changelog/safe-file-reading.changelog.md`
- `changelog/document-consistency.changelog.md`

### Master records and tracking files

- `design/design.md`
- `changelog/changelog.md`
- `README.md`
- `TODO.md`
- `phase/SUMMARY.md`
- `patch/governed-design-sharding-compact-index.patch.md`
- `phase/phase-089-governed-design-sharding-compact-index.md`

---

## TODO and Changelog Coordination

- `TODO.md` records P089 as active during source sync and completed only after source audit, runtime install parity/body sufficiency, git push, and GitHub release pass.
- `changelog/changelog.md` records v9.96 as current source version during P089 and uses final release wording only after runtime install, parity/body sufficiency, push, and release gates pass.
- Owner changelogs record their respective version bumps.
- README presents current-state guidance and latest refinement context, not a copied changelog timeline.

---

## Verification

- [x] Phase and patch records exist and link correctly.
- [x] Owner runtime/design/changelog chains align at target versions.
- [x] Master records describe v9.96 / P089 consistently.
- [x] README Bash and PowerShell install arrays still include exactly 46 active runtime rule files.
- [x] Runtime install copies only README-listed active runtime rules.
- [x] Source/runtime parity passes for 46 active runtime files.
- [x] Active runtime body sufficiency passes for 46 active runtime files.
- [ ] `master` push and GitHub release `v9.96` are verified.

---

## Exit Criteria

- Governed design sharding doctrine is installed in the correct owner chains.
- P089 phase and patch records exist and are synchronized.
- Master records describe v9.96 consistently.
- Active runtime count remains 46.
- Source consistency, runtime parity, and body-sufficiency gates pass.
- Source/runtime release artifacts are pushed and released as `v9.96`.

---

## Risks and Rollback Notes

Risk:
- Design sharding could be mistaken for inactive history rollover.

Mitigation:
- State that child shards remain active governed design target-state unless explicitly retired through changelog/history governance.

Risk:
- The compact index could become a link-only router with no useful target-state summary.

Mitigation:
- Require the index to preserve purpose, authority, shard map, current target-state summary, and read path.

Risk:
- Broad shard reads could recreate the same context-bloat problem.

Mitigation:
- Require index-first and shard-selective reads, with worker filtering for broad shard audits.

Rollback:
- Narrow or remove P089 sharding doctrine through a governed rollback if it over-prescribes repository structure.
- Restore prior v9.95 master records only through governed rollback.
- Reinstall the prior 46-file runtime set only under an explicit rollback gate.
- Do not delete design shards, phase/patch records, history/done shards, or runtime destination extras as cleanup.

---

## Next Possible Phases

- None selected until P089 verification and release gates complete.
