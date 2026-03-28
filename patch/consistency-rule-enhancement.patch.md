# Consistency Rule Enhancement Patch

## 0) Document Control

> **Current Version:** 1.1
> **Status:** Historical example normalized
> **Target Design:** [../design/document-consistency.design.md](../design/document-consistency.design.md) v1.2
> **Target Rule:** [../document-consistency.md](../document-consistency.md)
> **Session:** dd0bf4af-a66b-4b07-bb9d-a90a0e57b54e
> **Full history:** [../changelog/consistency-rule-enhancement.changelog.md](../changelog/consistency-rule-enhancement.changelog.md)

---

## 1) Context

This patch exists to show a governed example of what a patch should look like.

Target artifact:
- `document-consistency.md`

Why the change mattered:
- the historical rule body was too minimal
- the design expected stronger verification-label guidance
- the patch needed to show the exact current→target surface instead of only describing the change in prose

---

## 2) Analysis

Risk level: Low

Dependencies:
- `design/document-consistency.design.md`
- `changelog/consistency-rule-enhancement.changelog.md`

Review concern:
- the patch must let a reviewer see the exact rule-text expansion, not just a summary of intent

---

## 3) Change Items

### Change Item 1
- **Target location:** `document-consistency.md` → verification-label guidance section
- **Change type:** additive

**Before**
```markdown
## Rules
- verify cross-references before finalizing output
```

**After**
```markdown
## Verification Standards (Mandatory)
Use these labels when referencing external entities:
- ✅ Verified: Entity exists (confirmed via tools)
- ⚠️ Unverified: Existence not checked
- ❌ Not Found: Confirmed missing

## Rules
- verify cross-references before finalizing output
```

### Change Item 2
- **Target location:** `document-consistency.md` → verification-method guidance
- **Change type:** additive

**Before**
```markdown
- verify references before use
```

**After**
```markdown
- verify references before use with appropriate project evidence tools such as Read, Glob, or Grep
```

### Change Item 3
- **Target location:** `document-consistency.md` → cross-section validation wording
- **Change type:** replacement

**Before**
```markdown
- keep related sections aligned
```

**After**
```markdown
- verify cross-section propagation so naming, metadata, references, and linked expectations stay aligned across the touched artifacts
```

---

## 4) Verification

- [ ] Confirm the target rule contains the verification-label block
- [ ] Confirm the target rule includes explicit verification-method wording
- [ ] Confirm the rule text matches the target design requirements
- [ ] Confirm the patch remains readable as a before/after artifact

---

## 5) Rollback Approach

If this change causes confusion or over-specifies the target rule:
- remove the additive verification-label block
- revert the verification-method wording to the prior baseline
- keep the changelog entry so the attempted enhancement remains historically visible
