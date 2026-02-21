# Document Changelog & Versions History Control

## 0) Document Control

> **Parent Scope:** RULES System Design
> **Current Version:** 4.4
> **Session:** f19e8a67-d3c2-4c85-aa11-4db6949e61f8 (2026-02-21)

---

## 1) Goal (goal)

- Set version tracking standards that are actually usable and traceable.
- Resolve conflicts between “Every file must have a table” with the Navigator guidelines of design docs
- Establish a single rule for general cases (OR compliance) and cases with double files. design/changelog
- Enforce the actual Session ID to trace back to the session.

---

## 2) Scope

### 2.1 Documents Covered

- Rules documents (`*.md`)
- Design documents (`*.design.md` or `design.md`)
- Changelog documents (`*.changelog.md` or `changelog.md`)

### 2.2 Problem This Design Resolves

- History duplication between design and changelog.
- Requirements between table-only and navigator-only
- Using a placeholder Session ID that cannot be traced

---

## 3) Core Principles

1. **Traceability First**
   - Every document must always have a clear version trace path.

2. **Flexible Compliance (OR)**
   - Documents meet the criteria when at least one of the following criteria is met:
     - (A) There is a `Version History (Unified)` table in the file.
     - (B) Contains a link to the authoritative changelog.

3. **Pair Behavior is Explicit**
   - When having both `design.md` and `changelog.md` in the same scope, explicit separation must be used.

4. **No Mock Session IDs**
   - Do not use `<Session ID>`, `TBD`, or any dummy values.

5. **History Preservation**
   - Do not delete/overwrite the old history without saving the new changes.

---

## 4) Core Requirements

### 4.1 Traceable Version Path (Mandatory)

Every document must have a traceable version path like OR:

- **Option A:** There is a `Version History (Unified)` table in that document.
- **Option B:** has `> Full history: ...` pointing to the main changelog.

### 4.2 Session ID Integrity

- Session ID must be a true value from current environment/session
- Supports UUID format (`xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx`) or `SXXXX`.
- For legacy data, use `LEGACY-XXX` only for historical entries.

### 4.3 History Preservation

- Do not delete the old history.
- If correcting errors in the original history, add a new entry to describe the correction.
- Every entry must have Date + Session ID.

### 4.4 design.md <> changelog.md Pair Rule (Mandatory)

When there is both design/changelog Coupled in the same scope:

| File | MUST use | MUST NOT use |
|------|----------|--------------|
| **design.md** / `*.design.md` | Navigator link-only (`> Full history: ...`) | Full changelog sections, version table/entries In the same file |
| **changelog.md** / `*.changelog.md` | Detailed sections (UPPER) + `Version History (Unified)` table (LOWER) | There are only detailed sections or only a table |

### 4.5 Navigator Definition

Navigator means:

- ✅ Only links to authoritative changelog
- ❌ There is no version history table in the design file.
- ❌ There are no version entries in the design file.

---

## 5) Format Standards

### 5.1 Full Changelog Format

```markdown
# Changelog - <Document Name>

> **Parent Document:** [<doc>.md](../<doc>.md)
> **Current Version:** X.Y
> **Session:** <Real Session ID>

---

## Version X.Y: <Headline>

**Date:** YYYY-MM-DD
**Session:** <Real Session ID>

### Changes
- <Detailed change 1>
- <Detailed change 2>

### Summary
<One-line summary>

---

## Version History (Unified)

| Version | Date | Changes | Session ID |
|---------|------|---------|------------|
| X.Y | YYYY-MM-DD | **[<Headline>](#version-xy)** | <Real Session ID> |
| | | Summary: <One-line summary> | |
```

### 5.2 Design Navigator Format

```markdown
---

> Full history: [changelog/<doc>.changelog.md](../changelog/<doc>.changelog.md)
```

### 5.3 Non-Pair Documents (OR Compliance)

If there is no pair file design/changelog:

- You can use either table-in-file or link-only.
- It is recommended to use table-in-file. When the document is still short and there are few changes

---

## 6) File Organization Patterns

### Pattern 1: Simple (No subdirectories)

```text
./
├── design.md
├── changelog.md
└── src/
```

### Pattern 2: Mixed/Complete

```text
./
├── design/
│   └── *.design.md
├── changelog/
│   ├── changelog.md
│   └── *.changelog.md
└── src/
```

### Decision Rule

```text
Has design/ or changelog/ directory?
├─ YES → Pattern 2
└─ NO  → Pattern 1
```

---

## 7) Compliance Checklist

- [ ] The document now has a traceable path of OR type.
- [ ] Session IDs are true (not placeholder)
- [ ] If it is a design/changelog pair, use separation correctly.
- [ ] changelog file contains both detailed sections + summary table
- [ ] No deletion of the original history.
- [ ] All referral links are working.

---

## 8) Quality Metrics

| Metric | Target |
|--------|--------|
| Traceable version path coverage | 100% |
| Session ID integrity | 100% real values |
| Pair-rule compliance | 100% when pair exists |
| History preservation | 100% |
| Cross-reference validity | 100% |

---

## 9) Related Documents

| Document | Purpose |
|----------|---------|
| [../document-changelog-control.md](../document-changelog-control.md) | Rule definition from this design |
| [../document-design-control.md](../document-design-control.md) | Design document format constraints |
| [../document-consistency.md](../document-consistency.md) | Cross-reference and consistency checks |

---

## 10) Implementation Notes

### 10.1 Common Pitfalls

- Insert the version table in the design doc even though it already has a changelog.
- Write a changelog with only detailed sections, without a summary table.
- Use placeholder Session ID
- Correct old history without adding new correction entries.

### 10.2 Migration Guidance

- If the original file has a table in the design doc and has a pair of changelogs → move the full history to changelog and leave the navigator link in design
- If the original changelog only had one format (only table or detailed) → add another section to complete both sections.

---

> Full history: [../changelog/document-changelog-control.changelog.md](../changelog/document-changelog-control.changelog.md)
