# Retire Memsearch Custom-Skill and Bridge Doctrine Patch

## 0) Document Control

> **Current Version:** 1.0
> **Status:** Completed
> **Target Design:** [../design/memory-governance-and-session-boundary.design.md](../design/memory-governance-and-session-boundary.design.md) v1.5
> **Session:** a9bec472-1706-4019-8cfd-5ba988a71662
> **Full history:** [../changelog/changelog.md](../changelog/changelog.md)

---

## 1) Context

This patch captures the bounded retirement-and-cleanup wave that removes discontinued memsearch custom-skill doctrine and the former `session-coordination-bridge` path from Main RULES active teaching.

Why this matters:
- the local RULES plugin shell no longer exists under `TEMPLATE/RULES/`
- the former `claude-code-rules:session-coordination-bridge` path is not actually usable from this repo now
- custom memsearch skill development is being discontinued from the user's RULES workflow
- Main RULES should not keep teaching retired custom-skill mechanics as if they remain active capability

---

## 2) Analysis

Risk level: Medium

Dependencies:
- `../memory-governance-and-session-boundary.md`
- `../project-documentation-standards.md`
- `../execution-continuity-and-mode-selection.md`
- `../authority-and-scope.md`
- `../phase-implementation.md`
- `../README.md`
- `../design/design.md`
- `../design/rules-plugin-extension.design.md`
- `../TODO.md`
- `../phase/SUMMARY.md`
- `../changelog/changelog.md`
- `../changelog/rules-plugin-extension.changelog.md`

Review concern:
- active doctrine should stop implying discontinued plugin/skill support
- historical artifacts should remain readable as history without being mistaken for current capability
- cleanup should not invent a new doctrine chain when existing owners can be narrowed or retired cleanly

---

## 3) Change Items

### Change Item 1
- **Target location:** `memory-governance-and-session-boundary`
- **Change type:** replacement

**Before**
```text
Main RULES still named memsearch or similar extension/plugin recall layers directly.
```

**After**
```text
Main RULES now uses generic optional external recall wording only, without teaching a memsearch-specific custom-skill path.
```

### Change Item 2
- **Target location:** active runtime owners with stale coordination defers
- **Change type:** replacement

**Before**
```text
Several active rules still deferred coordination semantics to `shared-execution-coordination.md`.
```

**After**
```text
Those rules now state directly that shared-board, plugin, and external coordination/runtime mechanics stay outside Main RULES current doctrine.
```

### Change Item 3
- **Target location:** master active-facing summaries
- **Change type:** replacement

**Before**
```text
README and master design still advertised memsearch-style recall doctrine in active summary wording.
```

**After**
```text
README and master design now use generic optional external recall wording and no longer imply a Main RULES-managed custom-skill path.
```

### Change Item 4
- **Target location:** historical/index surfaces
- **Change type:** replacement

**Before**
```text
Historical index surfaces still risked reading like former memsearch and bridge-skill waves remained practically usable.
```

**After**
```text
Historical index surfaces now frame those waves as retired history only, not current usable capability.
```

---

## 4) Verification

- [x] active Main RULES doctrine no longer teaches memsearch-specific custom-skill support
- [x] active Main RULES doctrine no longer treats `session-coordination-bridge` as a usable path
- [x] stale deferrals to `shared-execution-coordination.md` are removed from touched active owners
- [x] master/index/history surfaces now frame the old bridge/memsearch waves as retired history only

---

## 5) Rollback Approach

If this retirement wave proves too broad:
- keep the plugin shell removal and historical-boundary framing intact
- keep Main RULES free of memsearch-specific custom-skill doctrine
- narrow historical wording changes before reintroducing any active-facing capability wording
- do not roll back into a state where Main RULES again implies that the former bridge skill or discontinued custom memsearch paths are usable from this repo now
