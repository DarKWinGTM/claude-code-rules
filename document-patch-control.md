# Document Patch Control

> **Current Version:** 1.0

## Rule Statement

**Core Principle: Standardized Tactical Implementation Plans**

Patch Documents (`.patch.md`) must be used for documenting complex state transitions, migrations, and "monkey patches". They bridge the gap between "Design" (Target State) and "Changelog" (History) by detailing the "Transition Plan".

**Based on:** [document-patch-control.design.md](design/document-patch-control.design.md) v1.0
**Related Reference:** [document-design-control.md](document-design-control.md) v1.3

---

## Core Requirements

### 1. Naming & Location

**Required Format:**
- Extension: MUST be `.patch.md` (NOT `-patch.md`)
- Format: `<context>.patch.md` (e.g., `db-migration.patch.md`)

**Location:**
- **Simple Projects:** Project Root
- **Complex Projects:** `./patches/` directory

### 2. Document Structure (Mandatory)

Every Patch Document MUST contain these sections:

1.  **Header:** Title, Status, Target Design link, Related Issue.
2.  **Context:** Why is this needed? Current State vs Target State.
3.  **Analysis:** Risks, Impact, Gap Analysis.
4.  **Implementation Plan:** Phased execution steps.
5.  **Verification:** How to verify success and Rollback plan.

### 3. Lifecycle Management

- **Draft:** Initial creation and analysis.
- **In Progress:** Implementation steps are being executed (tracked in TODO.md).
- **Completed:** All steps finished, verification passed.
- **Archived:** Merged into codebase history, file can be moved to `./patches/archive/` or kept as record.

---

## When to Create a Patch Document

| Scenario | Create .patch.md? | Reason |
|----------|-------------------|--------|
| **Simple Bug Fix** | ❌ No | Direct code fix + Changelog entry is sufficient. |
| **New Feature** | ❌ No | Use `design.md` for specification + `TODO.md` for tasks. |
| **Complex Refactor** | ✅ Yes | Needs a step-by-step plan to ensure safety. |
| **Data Migration** | ✅ Yes | Critical risk; needs rollback plan and verification. |
| **Monkey Patch** | ✅ Yes | Deviates from standard design; needs explicit documentation. |
| **Multi-stage Rollout**| ✅ Yes | Describes the transition phases clearly. |

---

## Integration with Other Rules

- **Design Control:** The `.patch.md` must implement the specific requirements of a `.design.md`.
- **Changelog Control:** Upon completion, the result of a patch is summarized in `.changelog.md`.
- **TODO Standards:** The "Implementation Plan" section of a patch should be broken down into tasks in `TODO.md`.

---

## Quality Metrics

| Metric | Target |
|--------|--------|
| Naming Compliance | 100% (`.patch.md`) |
| Structure Completeness | 100% (All 5 mandatory sections) |
| Risk Assessment | Required for all patches |
| Verification Plan | Required for all patches |

---

> **Full history:** [changelog/document-patch-control.changelog.md](changelog/document-patch-control.changelog.md)
