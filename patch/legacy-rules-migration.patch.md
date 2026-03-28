# Legacy Rules Migration Patch

## 0) Document Control

> **Current Version:** 1.3
> **Status:** Historical example normalized
> **Target Design:** [../design/design.md](../design/design.md) v1.5
> **Session:** dd0bf4af-a66b-4b07-bb9d-a90a0e57b54e
> **Full history:** [../changelog/legacy-rules-migration.changelog.md](../changelog/legacy-rules-migration.changelog.md)

---

## 1) Context

This patch is a historical non-code patch example.

It documents a governed migration from legacy rule formatting to the standardized runtime/design/changelog contract. The patch is non-code, but it still has to show structured before/after state instead of only listing migration phases.

Affected artifacts:
- root runtime rule files
- `design/*.design.md`
- `changelog/*.changelog.md`

---

## 2) Analysis

Patch class: non-code / governance patch

Risk level: Medium

Why this patch existed:
- legacy rule files used inconsistent headers and history handling
- design files still carried outdated formatting patterns
- changelog authority needed to become explicit and deterministic

Review concern:
- even for governance work, the reviewer must be able to compare the old document state to the target document state directly

---

## 3) Change Items

### Change Item 1
- **Target location:** legacy root rule files → metadata header block
- **Change type:** replacement

**Before**
```markdown
# Rule Name

> Based on: design/rule.design.md
```

**After**
```markdown
# Rule Name

> **Current Version:** X.Y
> **Design:** [design/rule.design.md](design/rule.design.md) vX.Y
> **Session:** <real-session-id>
> **Full history:** [changelog/rule.changelog.md](changelog/rule.changelog.md)
```

### Change Item 2
- **Target location:** legacy design files → active body/history handling
- **Change type:** restructuring

**Before**
```markdown
## Version History
<embedded long-form version table inside the active design file>
```

**After**
```markdown
## 0) Document Control
> **Parent Scope:** <scope>
> **Current Version:** X.Y
> **Session:** <real-session-id> (YYYY-MM-DD)

<active target-state guidance only>

> Full history: [../changelog/<name>.changelog.md](../changelog/<name>.changelog.md)
```

### Change Item 3
- **Target location:** governed chains without authoritative history files
- **Change type:** additive

**Before**
```markdown
No dedicated per-chain changelog file existed.
```

**After**
```markdown
Each governed chain has one authoritative changelog file with:
- Parent Document
- Current Version
- Session
- unified version history
```

### Change Item 4
- **Target location:** migration-control wording itself
- **Change type:** replacement

**Before**
```markdown
Migration described mainly as phased checklist prose.
```

**After**
```markdown
Migration documented as explicit current→target document-state changes so reviewers can see what formatting and authority behavior changed.
```

---

## 4) Verification

- [ ] Confirm runtime rule files follow the canonical header contract
- [ ] Confirm design files keep active guidance separate from historical detail
- [ ] Confirm each migrated rule chain has an authoritative changelog file
- [ ] Confirm this patch reads as a before/after governance patch rather than a prose-only migration summary

---

## 5) Rollback Approach

If the migration model needs to be partially reverted:
- restore prior chain files from version control
- keep changelog authority records intact so migration history is not lost
- re-apply standardization in smaller bounded slices instead of one broad migration wave
