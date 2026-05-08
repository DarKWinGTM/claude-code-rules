# Memory Root Index Relative Scope Compaction Patch

## 0) Document Control

> **Current Version:** 1.0
> **Status:** Completed
> **Target Design:** [../design/memory-governance-and-session-boundary.design.md](../design/memory-governance-and-session-boundary.design.md) v1.7
> **Target Rule:** [../memory-governance-and-session-boundary.md](../memory-governance-and-session-boundary.md)
> **Session:** d42465eb-30a7-4bc8-b9d6-03e52306e9a5
> **Full history:** [../changelog/memory-governance-and-session-boundary.changelog.md](../changelog/memory-governance-and-session-boundary.changelog.md)

---

## 1) Context

This patch captures P088 / v9.93, which improves root memory indexing without hiding active memory context.

The existing root `MEMORY.md` already used one-line hooks, but path-scoped sections repeated long memory-relative folders in every entry. The user explicitly rejected turning `MEMORY.md` into a second-layer router because loaded context would stop seeing useful memory. The target is a scope-relative tree index: one `Scope`, one `Memory base`, and visible relative hooks.

---

## 2) Analysis

Risk level: Medium

Dependencies:
- `../memory-governance-and-session-boundary.md`
- `../design/memory-governance-and-session-boundary.design.md`
- `../changelog/memory-governance-and-session-boundary.changelog.md`
- `/home/node/.claude/projects/-home-node-workplace-AWCLOUD-CLAUDE/memory/MEMORY.md`
- `../README.md`
- `../design/design.md`
- `../changelog/changelog.md`
- `../TODO.md`
- `../phase/SUMMARY.md`

Review concerns:
- root `MEMORY.md` must not become a link-only router
- active hooks must remain visible enough for memory to help without extra reads
- relative entries must not use fake markdown alias syntax that resolves incorrectly
- detail memory files must not be deleted or treated as junk

---

## 3) Change Items

### Change Item 1
- **Target location:** `memory-governance-and-session-boundary.md` and design companion
- **Change type:** replacement

**Before**
```text
Root MEMORY.md should be a compact active index and loader warnings should trigger maintenance, but the doctrine does not specify how to reduce repeated scope paths without hiding active memory meaning.
```

**After**
```text
Root MEMORY.md declares one Scope and one Memory base per path scope when repetition creates bloat, then lists active memory entries as visible relative one-line hooks under that base.
```

### Change Item 2
- **Target location:** root memory index format
- **Change type:** restructuring

**Before**
```text
## PATH_SCOPE:/home/node/workplace/AWCLOUD/TEMPLATE/RULES/
- [RULES scope declaration](path/home-node-workplace-AWCLOUD-TEMPLATE-RULES/SCOPE.md) — Canonical path scope for RULES repository memory.
- [RULES runtime install boundary](path/home-node-workplace-AWCLOUD-TEMPLATE-RULES/feedback/feedback_rules_runtime_should_not_install_readme_todo.md) — TODO/README are not rules; preserve plugin-owned runtime rules.
```

**After**
```text
## PATH_SCOPE: RULES repository
Scope: `/home/node/workplace/AWCLOUD/TEMPLATE/RULES/`
Memory base: `path/home-node-workplace-AWCLOUD-TEMPLATE-RULES/`

### Root
- `SCOPE.md` — Canonical path scope for RULES repository memory.

### feedback/
- `feedback/feedback_rules_runtime_should_not_install_readme_todo.md` — Runtime install excludes README/TODO/design/changelog/phase/patch.
```

### Change Item 3
- **Target location:** root memory index visibility boundary
- **Change type:** additive

**Before**
```text
Compaction could be misread as permission to replace active hooks with only SCOPE.md or second-layer index pointers.
```

**After**
```text
Compaction must keep one-line active hooks visible in root MEMORY.md and must not hide active meaning behind link-only routing or second-layer indexes.
```

### Change Item 4
- **Target location:** release governance records
- **Change type:** additive

**Before**
```text
v9.92 records describe daily-first governed rollover but do not record P088 memory root-index relative compaction.
```

**After**
```text
v9.93 records describe P088 memory root-index relative compaction, active runtime count remains 46, and release verification records source/runtime parity plus body sufficiency.
```

---

## 4) Verification

- [x] Confirm `memory-governance-and-session-boundary` runtime/design/changelog align at v1.7.
- [x] Confirm root `MEMORY.md` declares `Memory base` for path-scoped sections.
- [x] Confirm root `MEMORY.md` preserves active one-line hooks instead of becoming a link-only router.
- [x] Confirm scoped entries use relative paths under `Memory base` and do not use fake alias links.
- [x] Confirm no memory detail files are deleted or archived by compaction alone.
- [x] Confirm README/master design/master changelog/TODO/phase align at v9.93 / P088.
- [x] Confirm runtime install copies only the 46 README-listed active runtime rule files.
- [x] Confirm source/runtime parity and active runtime body sufficiency pass 46/46.
- [x] Confirm `master` push and GitHub release `v9.93` are verified.

---

## 5) Rollback Approach

If the relative root-index format proves less useful:
- revert the v9.93 commit to restore the prior root `MEMORY.md` layout and v1.6 doctrine
- keep memory detail files intact
- do not delete or archive memories as rollback cleanup
- select a narrower root-index compaction strategy only after preserving active hook visibility
