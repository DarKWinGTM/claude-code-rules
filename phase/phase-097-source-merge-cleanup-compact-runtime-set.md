# P097 — Source Merge Cleanup Compact Runtime Set

> **Summary File:** [SUMMARY.md](SUMMARY.md)
> **Phase ID:** P097
> **Status:** Released / Completed
> **Target Release:** v10.05
> **Design References:**
> - [../design/design.md](../design/design.md) v10.05
> - merged active runtime companion designs under [../design/](../design/)
> **Patch References:** [../patch/source-merge-cleanup-compact-runtime-set.patch.md](../patch/source-merge-cleanup-compact-runtime-set.patch.md)
> **Session:** 6ecc64cf-8eed-497a-9b84-02f5d5228ee3
> **Full history:** [../changelog/changelog.md](../changelog/changelog.md)

---

## Objective

Release the compact 18-rule merged runtime set as the active source-owned RULES runtime install target.

---

## Why This Phase Exists

The source tree has moved from many small overlapping runtime rule files into merged body-sufficient owner rules.

P097 turns that source-local cleanup into a governed release by synchronizing metadata, companion design/changelog surfaces, install scope, validation, push, and GitHub release evidence.

---

## Expected Output

- README installs exactly the 18 active merged runtime rules.
- Absorbed legacy root rule files are removed from active source authority.
- Merged runtime rules have resolvable design and changelog companions.
- `.claude-code-rules-legacy-backup/` remains local preservation output, not active runtime authority.
- Runtime install and source/runtime parity pass for 18/18 active rules.
- GitHub release `v10.05` is created and verified.

---

## Action Checklist

- [x] Confirm `v10.05` release/tag is not already present.
- [x] Confirm current cleanup scope targets the compact 18-rule merged set.
- [x] Repair merged rule metadata and missing design/changelog companions.
- [x] Sync README, master design, master changelog, TODO, phase summary, phase, and patch records to P097 pre-release state.
- [x] Validate README install arrays, metadata links, source body sufficiency, runtime install, and source/runtime parity.
- [x] Commit source release, push `master`, create GitHub release `v10.05`, and verify release state.
- [x] Finalize P097 closeout records after release verification passes.

---

## Out of Scope

- Deleting local backup/provenance output as cleanup.
- Treating destination runtime extras as owned by this release without owner scope.
- Reintroducing absorbed legacy root rules as active runtime authority.
- Claiming GitHub release verification before push and release checks pass.

---

## Completion Gate

- README Bash and PowerShell install arrays define exactly the same 18 active runtime files.
- All 18 source root runtime files have substantive active bodies.
- All 18 active runtime files have resolvable `Design` and `Full history` metadata.
- Runtime install copies only the 18 README-listed active runtime rules.
- Source/runtime parity and destination body sufficiency pass for 18/18 files.
- `.claude-code-rules-legacy-backup/` is excluded from active source authority.
- `master` push and GitHub release `v10.05` verification pass.

---

## Current Status

P097 is released and closed for `v10.05`.

Completed:
- preflight selected `v10.05 / P097` because `v10.05` release and tag were not found
- active runtime target is the compact 18-rule merged set
- merged-rule metadata and missing companion links were repaired
- README, master design, master changelog, TODO, phase, and patch records are synchronized to released `v10.05 / P097` state
- runtime install copied the 18 README-listed active runtime rules
- 18/18 source/runtime parity and source/destination body sufficiency passed
- metadata-link validation passed for 18/18 active runtime files
- consistency sweep passed for P097 surfaces
- `master` push and GitHub release `v10.05` verification passed

Release evidence:
- Release URL: https://github.com/DarKWinGTM/claude-code-rules/releases/tag/v10.05
- Release target and tag point to commit `14310761b1804d3355d5a1fa2b380901daf1ce6d`.
- Published at `2026-05-15T21:39:33Z`.

No pending P097 release gates remain in checked scope.
