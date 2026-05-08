# Phase P088 — Memory Root Index Relative Scope Compaction

> **Summary File:** [SUMMARY.md](SUMMARY.md)
> **Phase ID:** P088
> **Status:** Completed
> **Design References:** [../design/memory-governance-and-session-boundary.design.md](../design/memory-governance-and-session-boundary.design.md) v1.7
> **Patch References:** [../patch/memory-root-index-relative-scope-compaction.patch.md](../patch/memory-root-index-relative-scope-compaction.patch.md)
> **Session:** d42465eb-30a7-4bc8-b9d6-03e52306e9a5

---

## Objective

Make root memory indexing smaller without hiding active memory meaning. P088 updates RULES doctrine and the active root `MEMORY.md` so path-scoped memory sections declare one canonical `Scope` and one `Memory base`, then list entries as visible relative hooks.

## Why This Phase Exists

The loaded root `MEMORY.md` had useful one-line memory hooks, but repeated long path folders consumed context. A link-only or second-layer index would save tokens but would also make loaded memory much less useful. The target is a compact tree-style root index, not hidden memory.

## Expected Output

- `memory-governance-and-session-boundary` runtime/design/changelog updated to v1.7.
- Active root `MEMORY.md` rewritten into scope-relative sections with visible hooks.
- README, master design/changelog, TODO, phase, and patch records synced for v9.93 / P088.
- Runtime install copies the 46 README-listed active rules only.
- Source/runtime parity and body sufficiency pass 46/46.
- `master` is pushed and GitHub release `v9.93` is verified.

## Completion Gate

P088 is complete only when source docs are synchronized, active memory index compaction is verified, runtime install/parity/body-sufficiency pass for 46/46 source-owned active rules, git push succeeds, and GitHub release `v9.93` is verified.

## Action Checklist

- [x] Select P088 as the governed memory-root-index compaction phase.
- [x] Update memory governance runtime/design/changelog to v1.7.
- [x] Compact active root `MEMORY.md` using `Scope` + `Memory base` sections.
- [x] Sync master design, master changelog, README, TODO, phase summary, and patch records for v9.93.
- [x] Install README-listed active runtime rules to `~/.claude/rules/`.
- [x] Verify 46/46 source/runtime parity and active runtime body sufficiency.
- [x] Push `master` and publish/verify GitHub release `v9.93`.

## Out of Scope

- Deleting memory detail files.
- Archiving active memories just to reduce root index size.
- Introducing `MEMORY.md -> SCOPE.md -> INDEX.md` hidden-memory routing.
- Starting P086 constructive-dissent work.
- Installing README, TODO, design, changelog, phase, or patch files as runtime rules.

## Affected Artifacts

- `memory-governance-and-session-boundary.md`
- `design/memory-governance-and-session-boundary.design.md`
- `changelog/memory-governance-and-session-boundary.changelog.md`
- `/home/node/.claude/projects/-home-node-workplace-AWCLOUD-CLAUDE/memory/MEMORY.md`
- `README.md`
- `design/design.md`
- `changelog/changelog.md`
- `TODO.md`
- `phase/SUMMARY.md`
- `patch/memory-root-index-relative-scope-compaction.patch.md`

## Verification

- Root `MEMORY.md` keeps active hooks visible and no longer repeats the same long path base on every scoped entry.
- Memory governance triad versions align at v1.7.
- Master source-governance surfaces align at v9.93 / P088 while active runtime count remains 46.
- Runtime destination matches the README-listed 46 source-owned active rule files with no hash mismatches.
- Active runtime body sufficiency passes for all 46 files.

## Closeout Summary

P088 delivered memory-root index compaction without hiding active memory meaning: root `MEMORY.md` keeps visible one-line hooks while path-scoped sections use one `Scope` and one `Memory base`. Runtime install copied only the 46 README-listed active rules, source/runtime parity plus body sufficiency passed 46/46 with destination extras observed-only, `master` was pushed, and GitHub release `v9.93` was verified.

## Risks and Rollback

Risk: over-compressing `MEMORY.md` into hidden memory. Mitigation: preserve one-line hooks in the root index.

Risk: broken relative references. Mitigation: use explicit `Memory base` plus inline relative paths unless links are fully resolvable.

Rollback: revert the v9.93 commit and restore the pre-P088 root `MEMORY.md` if the relative format proves less useful. Do not delete memory detail files as part of rollback.
