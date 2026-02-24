# Legacy Rules Migration Plan

## 0) Document Control
> **Parent Scope:** Claude Code Rules System
> **Current Version:** 1.2
> **Status:** Completed
> **Target Design:** [../design/design.md](../design/design.md) v1.5
> **Session:** f19e8a67-d3c2-4c85-aa11-4db6949e61f8
> **Full history:** [../changelog/legacy-rules-migration.changelog.md](../changelog/legacy-rules-migration.changelog.md)

---

## 1. Context
12 core rules exist in a legacy format that predates the current `document-design-control` standards. To ensure system-wide consistency and traceability, these must be migrated to the new v1.4 standard templates defined in the master design.

## 2. Migration Scope
**Target Rules:**
1. anti-mockup.md
2. anti-sycophancy.md
3. authority-and-scope.md
4. document-consistency.md
5. emergency-protocol.md
6. flow-diagram-no-frame.md
7. functional-intent-verification.md
8. no-variable-guessing.md
9. safe-file-reading.md
10. safe-terminal-output.md
11. strict-file-hygiene.md
12. zero-hallucination.md

## 3. Implementation Plan

### Phase 1: Preparation
- [x] Create `changelog/` files for all 12 rules (Pattern 2 compliance).
- [x] Extract existing version history (if any) from .md files and move to new changelogs.
- [x] Ensure correct headers in changelogs.

### Phase 2: Design Doc Standardization
- [x] Update all 12 `design/*.design.md` files.
- [x] Add "0) Document Control" header with real UUIDs.
- [x] Remove any version tables (Navigator format only).
- [x] Add link to new changelog files at the bottom.

### Phase 3: Rule File Standardization
- [x] Update all 12 root `*.md` files.
- [x] Add Standard Header:
  `> **Current Version:** X.X`
  `> **Design:** file.design.md vX.X`
- [x] Add Standard Footer:
  `> Full history: changelog/file.changelog.md`
- [x] Remove any embedded version tables.

## 4. Verification
- [x] All 12 rules must have a corresponding `.design.md` and `.changelog.md`.
- [x] No version tables should remain in Rule or Design files.
- [x] All links (Header/Footer) must be valid.

---

> Full history: [../changelog/legacy-rules-migration.changelog.md](../changelog/legacy-rules-migration.changelog.md)
