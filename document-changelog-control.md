# Document Changelog & Versions History Control

> **Current Version:** 4.4
> **Based on:** document-changelog-control.design.md v4.4
> **Session:** (use current session ID from <env>)

> **Full history:** [changelog/document-changelog-control.changelog.md](changelog/document-changelog-control.changelog.md)

---

## Rule Statement

**Core Principle: Every document must have a traceable version path with real session IDs**

This rule defines practical, non-conflicting version governance for rules, design, and changelog documents. It supports **OR compliance** for general cases and enforces explicit behavior when `design` and `changelog` files exist as a pair.

---

## Core Requirements

### 1. Traceable Version Path (Mandatory, OR Compliance)

Every document MUST satisfy at least one of the following:

- **Option A:** Has a local `Version History (Unified)` table
- **Option B:** Has a link to authoritative changelog (`> Full history: ...`)

**Important:**
- This is **OR**, not AND
- The goal is traceability without unnecessary duplication

### 2. Session ID Integrity

**Required Actions:**
- Session ID MUST come from `<env>` in the active session
- Acceptable format: UUID (36 chars) or `SXXXX`
- NEVER use placeholders: `<Session ID>`, `TBD`, `pending`, mock values
- Legacy historical entries may use `LEGACY-XXX` only when true session data is unavailable

### 3. History Preservation

**Required Actions:**
- NEVER delete or truncate existing history entries
- If an old entry is incorrect, add a **new correction entry** instead of silently rewriting history intent
- Every entry MUST include Date and Session ID

### 4. design.md <> changelog.md Pair Rule (Mandatory when Pair Exists)

When both design and changelog documents exist in the same scope:

| File | MUST use | MUST NOT use |
|------|----------|--------------|
| **design.md** / `*.design.md` | Navigator link-only (`> Full history: ...`) | Full changelog sections, local version table/entries |
| **changelog.md** / `*.changelog.md` | Detailed sections (UPPER) + `Version History (Unified)` table (LOWER) | Detailed-only or table-only formats |

### 5. Changelog Linking

If using Option B (link-based traceability):
- link MUST point to existing authoritative changelog file
- link format should be explicit and testable
- link should appear in a stable location (usually end of document)

---

## What "Navigator" Means

For `design.md` / `*.design.md` in a pair model:

- ✅ Include only a navigation link to full changelog
- ❌ Do not embed full version table
- ❌ Do not embed detailed changelog sections

Example:

```markdown
---

> Full history: [../changelog/<doc>.changelog.md](../changelog/<doc>.changelog.md)
```

---

## Format Standards

### A) Full Changelog Format (authoritative)

```markdown
# Changelog - <Document>

> **Parent Document:** [../<doc>.md](../<doc>.md)
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

### B) Navigator Design Format (pair mode)

```markdown
---

> Full history: [../changelog/<doc>.changelog.md](../changelog/<doc>.changelog.md)
```

### C) Non-Pair Documents (OR mode)

When no design/changelog pair exists, either approach is valid:
- local unified table, OR
- authoritative changelog link

---

## File Organization Patterns

### Pattern 1: Simple

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

Decision:

```text
Has design/ or changelog/ directory?
├─ YES → Pattern 2
└─ NO  → Pattern 1
```

---

## Minimum Compliance

A document is compliant if:
1. It has a traceable version path (Option A or B), and
2. Session IDs are real values, and
3. Existing history is preserved

Additional requirement when pair exists:
4. design/changelog separation must follow Pair Rule

---

## Quality Metrics

| Metric | Target |
|--------|--------|
| Traceable version path coverage | 100% |
| Session ID integrity | 100% real values |
| Pair-rule compliance (when applicable) | 100% |
| History preservation | 100% |
| Cross-reference validity | 100% |

---

## Compliance Checklist

- [ ] Document has traceable version path (OR satisfied)
- [ ] Session IDs are real (no placeholders)
- [ ] No silent history deletion/truncation
- [ ] Pair behavior enforced when design/changelog coexist
- [ ] Full changelog has BOTH detailed sections + unified table
- [ ] Full history links resolve correctly

---

## Reserved Terms & Naming Guidance

| Term | Meaning |
|------|---------|
| `Version History (Unified)` | Canonical summary table name |
| `.design.md` | Design document suffix |
| `.changelog.md` | Changelog document suffix |

---

## Enforcement Notes

- **Single Source of Truth:** authoritative changelog governs latest version
- **No duplicate full history:** avoid copying full changelog into multiple files
- **Git handles line-level diff history; changelog handles human-readable release intent**

---

> **Full history:** [changelog/document-changelog-control.changelog.md](changelog/document-changelog-control.changelog.md)
