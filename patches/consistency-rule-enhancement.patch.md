# Consistency Rule Enhancement Patch

## 0) Document Control

> **Status:** Completed
> **Target Design:** design/document-consistency.design.md v1.0
> **Target Rule:** document-consistency.md
> **Session:** a77b77ae-ef2a-49f6-93d9-f78c8ac2d2f7

---

## 1. Context

Current `document-consistency.md` is too minimal. It captures the core principles but misses specific formatting standards defined in the design document (Section 4.2 Verification Labels and Section 2.2 Reference Types). This leads to inconsistent output formatting despite correct logic.

## 2. Analysis

**Missing Elements from Design:**
1. **Verification Labels:** Design explicitly asks for `✅ Verified`, `⚠️ Unverified`, `❌ Not Found`.
2. **Verification Methods:** Design specifies tools (`ls`, `grep`) which should be hinted at to ensure rigorous checking.
3. **Cross-Section Validation:** The logic for "Change Propagation" is present but vague in the rule.

**Impact:**
- AI output varies in style (sometimes text-only, sometimes bullets).
- Verification status is not instantly visible.

## 3. Implementation Plan

**Update `document-consistency.md` to v1.1:**
- Add explicit "Verification Standards" section.
- Enforce the use of emoji labels defined in design.
- Expand "Rules" to include method hints.

**Draft Content:**

```markdown
## Verification Standards (Mandatory)
Use these labels when referencing external entities:
- ✅ Verified: Entity exists (confirmed via tools)
- ⚠️ Unverified: Existence not checked
- ❌ Not Found: Confirmed missing

## Rules
...
- Verify existence using appropriate tools (Read/Ls/Grep) before referencing.
...
```

## 4. Verification

- [ ] Check if `document-consistency.md` contains the new labels.
- [ ] Check if `changelog` is updated.
- [ ] Verify content matches `design/document-consistency.design.md` requirements.
