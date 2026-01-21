# Project Documentation Standards

> **Current Version:** 1.0

## Rule Statement

**Core Principle: Every project must maintain standardized documentation following defined rules**

This rule ensures all projects have proper documentation structure from the start, integrating document-design-control.md, document-changelog-control.md, and todo-standards.design.md requirements.

**Design:** [project-documentation-standards.design.md](design/project-documentation-standards.design.md) v1.0

---

## Core Requirements

### 1. Required Documents

Every project MUST have these documents based on project needs:

| Document | Required When | Purpose | Rule Reference |
|----------|---------------|---------|----------------|
| **README.md** | Every project | Project overview, quick start, installation | Standard practice |
| **design.md** | Project has design specifications | Architecture, standards, specifications | [document-design-control.md](document-design-control.md) v1.1 |
| **changelog.md** | Project needs version tracking | Version history, changes tracking | [document-changelog-control.md](document-changelog-control.md) v4.3 |
| **TODO.md** | Project has tasks | Task tracking, progress management | [todo-standards.design.md](design/todo-standards.design.md) v1.0 |

**Required Actions:**
- Use the decision tree (Section 2) to determine which documents are needed
- Create documents following their respective rule formats
- Ensure all Session IDs are real UUIDs (no placeholders)

### 2. Decision Tree for Document Creation

```
Project starting?
  ↓ YES
Create README.md (overview + quick start)
  ↓
Has design/specifications?
  ↓ YES → Create design.md (follow document-design-control.md)
  ↓ NO
Needs version tracking?
  ↓ YES → Create changelog.md (follow document-changelog-control.md)
  ↓ NO
Has tasks to track?
  ↓ YES → Create TODO.md (follow todo-standards.design.md)
  ↓ NO
Project ready
```

### 3. Document Rule Compliance

When creating documentation, follow these rules:

| Document Type | Follow This Rule | Key Requirements |
|---------------|------------------|-------------------|
| **design.md** | document-design-control.md | `.design.md` suffix, `./design/` location, Navigator format |
| **changelog.md** | document-changelog-control.md | Version History (Unified) table, real Session IDs |
| **TODO.md** | todo-standards.design.md | P0-P3 priorities, timestamps, status sections |

### 4. Project Start Checklist

**Before Starting:**
- [ ] Determine project type (Simple vs Complex vs Design-heavy)
- [ ] Identify required documents using decision tree
- [ ] Plan documentation structure
- [ ] Set up directory structure (`./design/`, `./changelog/` if needed)

**During Setup:**
- [ ] Create README.md with project overview and quick start
- [ ] If design needed: Create design.md following document-design-control.md
- [ ] If version tracking needed: Create changelog.md following document-changelog-control.md
- [ ] If tasks needed: Create TODO.md following todo-standards.design.md

**Verification:**
- [ ] All Session IDs are real UUIDs (no placeholders like `<Session ID>`, `TBD`)
- [ ] All cross-references work (test links)
- [ ] All documents follow their respective rule formats
- [ ] No duplicate/unnecessary files (follow strict-file-hygiene.md)

### 5. Onboarding Requirements

New projects MUST acknowledge documentation standards:

1. **Read Standards** - Understand project-documentation-standards.md
2. **Know Rules** - Understand which rules apply when
3. **Follow Format** - Follow proper document formats

---

## Examples

### ✅ Correct: Simple Project

```
simple-project/
├── README.md           # Project overview, quick start
└── src/
```

**Documents:** README.md only

### ✅ Correct: Standard Project

```
standard-project/
├── README.md           # Project overview, quick start
├── design.md           # Architecture, specifications
├── TODO.md             # Task tracking
└── src/
```

**Documents:** README.md + design.md + TODO.md

### ✅ Correct: Complex Project

```
complex-project/
├── README.md
├── design/
│   ├── design.md       # Master design
│   ├── api.design.md   # API design
│   └── database.design.md  # Database design
├── changelog/
│   ├── changelog.md    # Master changelog
│   └── api.changelog.md    # API changelog
├── TODO.md
└── src/
```

**Documents:** README.md + multiple design.md + changelog.md + TODO.md

---

## Quality Metrics

| Metric | Target | Measurement |
|--------|--------|-------------|
| Required documents presence | 100% | Checklist in Section 4 |
| Rule compliance | 100% | Follow respective rules |
| Session ID accuracy | 100% | Real UUIDs only, no placeholders |
| Cross-reference validity | 100% | All links working |
| Format consistency | 100% | Follow document-design-control.md |

---

## Integration

This rule integrates with:

| Rule | Relationship |
|------|-------------|
| **document-design-control.md** v1.1 | Defines design document format standards |
| **document-changelog-control.md** v4.3 | Defines version tracking format |
| **todo-standards.design.md** v1.0 | Defines TODO/task format |
| **strict-file-hygiene.md** v1.2 | Prevents unrequested file creation |

---

## Enforcement

**Mandatory for:**
- All new projects starting from now
- Projects requiring documentation updates
- Projects with multiple documents

**Verification:**
- Use Project Start Checklist before beginning
- Test all cross-references
- Verify Session IDs are real UUIDs
- Ensure format compliance with respective rules

---

> Full history: [changelog/project-documentation-standards.changelog.md](changelog/project-documentation-standards.changelog.md)
