# Runtime Destination Ownership Boundary Patch

## 0) Document Control

> **Current Version:** 1.0
> **Status:** Completed
> **Target Design:** [../design/authority-and-scope.design.md](../design/authority-and-scope.design.md) v2.5
> **Session:** d42465eb-30a7-4bc8-b9d6-03e52306e9a5
> **Full history:** [../changelog/changelog.md](../changelog/changelog.md)

---

## 1) Context

This patch captures a narrow authority-and-scope clarification for shared runtime destinations.

The immediate issue is that a runtime install destination such as `~/.claude/rules/` can contain files sourced from different projects, plugins, or rule packages. A file appearing beside Main RULES runtime copies does not make that file owned by the Main RULES source project.

This patch is not a new cleanup wave and does not authorize deletion. It clarifies that destination/runtime co-location is weak observed placement, not semantic ownership authority.

---

## 2) Analysis

Risk level: Medium

Dependencies:
- `../authority-and-scope.md`
- `../design/authority-and-scope.design.md`
- `../changelog/authority-and-scope.changelog.md`
- `../design/design.md`
- `../changelog/changelog.md`
- `../README.md`
- `../TODO.md`
- `../phase/SUMMARY.md`

Review concern:
- Main RULES install/parity remains scoped to the active runtime files sourced from the Root RULES Project.
- Runtime files owned by other projects/plugins must not be classified as junk merely because they sit in the same destination directory.
- `TODO.md`, README, phase, patch, design, changelog, and support surfaces remain governance/tracking/support surfaces, not runtime-rule install targets.
- Cleanup, hygiene, git state, and runtime co-location must not become deletion authorization.

---

## 3) Change Items

### RDO-001 — `authority-and-scope.md` Core Rules

- **Target artifact:** `../authority-and-scope.md`
- **Target location:** `## Core Rules`
- **Change type:** additive

**Before**
```text
Core rules defined user authority, hard boundaries, fresh directives, memory boundaries, mode-selection deferral, and shared-board/plugin scope boundaries, but did not explicitly state that shared runtime directory placement is not source/project ownership.
```

**After**
```text
- Runtime co-location is not ownership authority: a file appearing in a shared runtime directory does not make it governed by the current source project.
```

**Preserved behavior**
- User authority still wins in non-hard-boundary space.
- Assistant-generated options remain advisory.
- Shared-board/plugin/external coordination mechanics remain outside Main RULES current doctrine unless selected by the user.

### RDO-002 — `authority-and-scope.md` Repository-Governed Semantic Authority

- **Target artifact:** `../authority-and-scope.md`
- **Target location:** `## Repository-Governed Semantic Authority`
- **Change type:** additive

**Before**
```text
The repository-governed semantic-authority bridge protected master surfaces and governed chains from being outranked by git working state or cleanup heuristics, but it did not explicitly classify runtime-directory co-location as weaker than source/project ownership.
```

**After**
```text
- runtime co-location must not outrank source/project ownership for file meaning
- for destination/runtime files outside the current source-owned install set, resolve owner/project scope before classification, cleanup, or deletion is considered
```

**Preserved behavior**
- Git cleanliness, untracked state, and working-tree noise remain observed local evidence only.
- Cleanup/isolation/hygiene heuristics remain last.
- Files whose meaning could be explained by master surfaces or governed chains still require those checks before non-governed/disposable classification.

### RDO-003 — `design/authority-and-scope.design.md` Target-State Alignment

- **Target artifact:** `../design/authority-and-scope.design.md`
- **Target location:** `## 1.2 Problem Statement` and `## 2.3 Repo-Governed Semantic-Authority Bridge`
- **Change type:** additive

**Before**
```text
The design target state described repo-governed semantic authority above git-state and cleanup heuristics, but did not explicitly name runtime co-location or destination/runtime owner resolution.
```

**After**
```text
The design target state records runtime co-location as non-ownership authority and requires owner/project scope resolution before destination/runtime files outside the current source-owned install set are classified, cleaned up, or considered for deletion.
```

### RDO-004 — Governance Record Synchronization

- **Target artifacts:** `../changelog/authority-and-scope.changelog.md`, `../design/design.md`, `../changelog/changelog.md`, `../README.md`, `../TODO.md`, `../phase/SUMMARY.md`, `../phase/phase-074-01-clarify-runtime-destination-ownership-boundary.md`
- **Target location:** relevant version/history/inventory/tracking/index sections
- **Change type:** additive

**Before**
```text
The runtime rule body had the new boundary, but companion governance records still described the previous v2.4 authority chain and the P073-08 runtime destination wording could be read as only observing destination files outside the active install set rather than clarifying ownership boundaries.
```

**After**
```text
The authority-and-scope chain is recorded as v2.5, master governance surfaces record P074-01, README current refinement wording explains the shared runtime destination boundary, TODO records the completed tracking item, and phase/SUMMARY indexes the new phase with this patch reference.
```

---

## 4) Verification

- [x] `authority-and-scope.md` contains the runtime co-location non-ownership rule.
- [x] `authority-and-scope.md` requires owner/project scope resolution before destination/runtime file classification, cleanup, or deletion when the file is outside the current source-owned install set.
- [x] The patch is scoped to `authority-and-scope.md` and companion governance records only.
- [x] No plugin-owned runtime rule is treated as a cleanup target by this patch.
- [x] `TODO.md` remains a durable tracking surface, not a runtime rule.
- [x] Runtime install/parity remains scoped to source-owned active runtime rule files.

---

## 5) Rollback Approach

If this clarification proves too broad:
- keep the existing repo-governed semantic-authority bridge above git-state and cleanup heuristics
- narrow the destination/runtime wording before removing it entirely
- preserve the rule that cleanup, hygiene, isolation, worktree, sandbox, and runtime co-location do not authorize deletion
- do not revert to a model where files in a shared runtime destination are assumed to belong to the current source project without owner/project scope resolution
