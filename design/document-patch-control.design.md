# Document Patch Control

## 0) Document Control

> **Parent Scope:** Project Documentation Standards
> **Current Version:** 1.0
> **Session:** a77b77ae-ef2a-49f6-93d9-f78c8ac2d2f7 (2026-02-01)

---

## 1) Goal

Standardize the creation, structure, and lifecycle of **Patch Documents** (`.patch.md`) to manage tactical implementation plans and complex state transitions.

---

## 2) Concept & Scope

### What is a Patch Document?
A **Patch Document** describes the **process** of moving from State A to State B.
- **Design Document (`.design.md`)**: Describes the *Target State* (State B).
- **Changelog (`.changelog.md`)**: Records the *History* of changes.
- **Patch Document (`.patch.md`)**: Describes the *Transition Plan* (How to get from A to B).

### When to use?
- Complex refactoring
- Migrations (Database, API, Dependencies)
- Multi-step bug fixes involving multiple systems
- "Monkey Patches" or temporary fixes that need documentation

---

## 3) Naming & Location

**File Extension:** `.patch.md` (replaces ad-hoc `-patch.md`)

**Naming Format:**
- `<context>.patch.md`
- Example: `database-migration.patch.md`, `auth-refactor.patch.md`

**Location:**
- **Project Root**: For simple/single patches.
- **`./patches/` directory**: For complex projects with multiple active patches.

---

## 4) Document Structure

Every Patch Document MUST include:

### 4.1 Header (Document Control)
```markdown
# [Patch Name]

> **Status:** [Draft/In Progress/Completed]
> **Target Design:** [Link to .design.md]
> **Related Issue:** [Issue ID]
```

### 4.2 Context
- **Why** is this patch needed?
- **Current State (A):** What is broken or needs changing?
- **Target State (B):** What is the expected outcome?

### 4.3 Analysis
- Gap Analysis
- Risks & Impact
- Dependencies

### 4.4 Implementation Plan (Phased)
- Phase 1: Preparation
- Phase 2: Execution
- Phase 3: Cleanup

### 4.5 Verification
- How do we know it worked?
- Rollback plan

---

## 5) Integration Rules

| Component | Interaction |
|-----------|-------------|
| **Design Doc** | Patch implements the requirements defined in a Design Doc. |
| **TODO.md** | Action items from the Patch Plan are tracked in `TODO.md`. |
| **Changelog** | Completion of a Patch generates a Changelog entry. |

---

> Full history: [document-patch-control.changelog.md](../changelog/document-patch-control.changelog.md)
