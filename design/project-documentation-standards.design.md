# Project Documentation Standards

## 0) Document Control

> **Parent Scope:** RULES System Design
> **Current Version:** 1.4
> **Session:** a77b77ae-ef2a-49f6-93d9-f78c8ac2d2f7 (2026-02-01)

---

## 1) Goal (goal)

- Set document standards for every project to be consistent.
- Specify when and what rules to use to create documents.
- Make sure every project has complete documentation according to specified standards.
- Reduce confusion in writing and managing documents

---

## 2) Scope

### 2.1 Projects Covered

- Every new project started
- Every project with updated design or specifications
- Every project that requires version tracking

### 2.2 Standards Defined

- Specify which documents are required for each project.
- Determine when to use which rules.
- Specify compliance checklist for inspection
- Define the onboarding process for new projects.

---

## 3) Required Documents

### 3.1 Core Documents

| Document | Required When | Purpose | Rule Reference |
|----------|---------------|---------|----------------|
| **README.md** | every project | Project overview, quick start, installation | Standard practice |
| **design.md** | when there are design specs | Architecture, standards, specifications | [document-design-control.md](../document-design-control.md) v1.1 |
| **changelog.md** | when version tracking is required | Version history, changes tracking | [document-changelog-control.md](../document-changelog-control.md) v4.4 |
| **TODO.md** | when there are tasks | Task tracking, progress management | [todo-standards.md](../todo-standards.md) v2.0 |
| **patch.md** | When you have to do Monkey Patch | Transition plan, complex state changes | [document-patch-control.md](../document-patch-control.md) v1.0 |

### 3.2 Decision Tree

```
Project started?
  ↓ YES
Create README.md (overview + quick start)
  ↓
Is there a design/specifications?
  ↓ YES → Create design.md (based on document-design-control.md)
  ↓ NO
Want track versions?
  ↓ YES → Create changelog.md (based on document-changelog-control.md)
  ↓ NO
Have tasks that need to be done?
  ↓ YES → Create TODO.md (based on todo-standards.md)
  ↓ NO
Do I have to do a Monkey Patch or Complex Migration?
  ↓ YES → Create *.patch.md (based on document-patch-control.md)
  ↓ NO
Project ready to use
```

---

## 4) Document Rules Applied

### 4.1 Rule Integration

When creating each type of document Relevant rules must be followed:

| Rule | When to use | Important requirements |
|------|------------------|-------------------|
| **document-design-control.md** | Create .design.md files | - Use suffix `.design.md`<br>- in `./design/`<br>- Navigator format |
| **document-changelog-control.md** | Create version tracking | - Version History (Unified) table<br>- Real Session IDs<br>- No placeholders |
| **todo-standards.md** | Create TODO.md | - Checkbox tasks (`- [ ]`)<br>- No priorities (P0-P3)<br>- No per-task timestamps |
| **document-patch-control.md** | Create .patch.md files | - Format `.patch.md`<br>- Structure (5 sections)<br>- Lifecycle states |

### 4.2 Cross-Reference Standards

All documents must be linked together:

```
project-documentation-standards.md (This rule)
  ↓ Specify which rule to use when.

document-design-control.md
  ↓ Set format .design.md

document-changelog-control.md
  ↓ Set the version tracking format.

todo-standards.md
  ↓ Define TODO/tasks format.

document-patch-control.md
  ↓ Set the Patch/Migration format.
```

### 4.3 Versioning Authority

- **Single Source of Truth:** `changelog.md` is the single source of the Version Number.
- **Synchronization Rule:**
  - When editing a Design document → always update the Changelog.
  - The Version number in the document Header (Design/Rule) must match the latest Changelog.
  - Do not update Design without updating Changelog.
  - Do not use a Version Number that does not match the Changelog.

---

## 5) Project Start Checklist (project start checklist)

### 5.1 Before Starting (before starting)

- [ ] **Determine project type** - Simple vs Complex vs Design-heavy
- [ ] **Identify required documents** - Use the decision tree in Section 3.2.
- [ ] **Plan documentation structure** - Single file or multiple files required?
- [ ] **Set up directory structure** - `./design/`, `./changelog/`, `./patches/` if necessary.

### 5.2 During Setup (during setup)

- [ ] **Create README.md** - Project overview, quick start
- [ ] **If design needed:** Create `design.md` following document-design-control.md
  - [ ] File named `*.design.md`
  - [ ] Located in `./design/`
  - [ ] Has Document Control section
  - [ ] Has changelog link at end
- [ ] **If version tracking needed:** Create `changelog.md` following document-changelog-control.md
  - [ ] Version History (Unified) format
  - [ ] Real Session IDs (no placeholders)
  - [ ] Detailed sections (UPPER) + Table (LOWER)
- [ ] **If tasks needed:** Create `TODO.md` following todo-standards.md
  - [ ] Use simple checkbox format (`- [ ]`)
  - [ ] No priorities (P0-P3)
  - [ ] No per-task timestamps
- [ ] **If patch needed:** Create `*.patch.md` following document-patch-control.md
  - [ ] Extension `.patch.md`
  - [ ] 5 mandatory sections (Context, Analysis, Plan, etc.)

### 5.3 Verification (check)

- [ ] **All Session IDs are real UUIDs** - No `<Session ID>`, `TBD`, or placeholders
- [ ] **All cross-references work** - Test all links
- [ ] **Format compliance** - All documents follow their respective rules
- [ ] **No duplicate files** - Follow strict-file-hygiene.md

---

## 6) Onboarding Integration (linking with onboarding)

### 6.1 New Projects

New projects must acknowledge:

1. **Documentation Standards Read** ✅
   - Read and understand project-documentation-standards.md
   - Understand what documents are required

2. **Rule Compliance** ✅
   - Know when to use which rules.
   - You can see the interest from the checklist in Section 5.

3. **Format Standards** ✅
   - Understand the format of each type of document
   - Can see examples from related rules.

### 6.2 Project Template (optional)

You can create a project template that includes:

```
project-template/
├── README.md (template)
├── design/
│   └── .gitkeep
├── changelog/
│   └── .gitkeep
└── .claude/
    └── rules/
        └── project-documentation-standards.md
```

---

## 7) Compliance Metrics

### 7.1 Quality Metrics

| Metric | Target | Measurement |
|--------|--------|-------------|
| Required documents presence | 100% | Checklist in Section 5 |
| Rule compliance | 100% | Follow respective rules |
| Session ID accuracy | 100% | Real UUIDs only |
| Cross-reference validity | 100% | All links work |
| Format consistency | 100% | Follow document-design-control.md |

### 7.2 Compliance Levels

**Minimum Compliance (minimum):**
- README.md is available in every project.
- Other documents as required by the project

**Recommended Compliance (recommended):**
- Every document follows format according to relevant rules.
- There is a changelog.md for version tracking.
- There is TODO.md for task tracking.
- Every Session ID is a real UUID.

---

## 8) Examples

### 8.1 Simple Project (small project)

```
simple-project/
├── README.md           # Project overview, quick start
└── src/
```

**Use only:** README.md

### 8.2 Standard Project (standard project)

```
standard-project/
├── README.md           # Project overview, quick start
├── design.md           # Architecture, specifications
├── TODO.md             # Task tracking
└── src/
```

**Use:** README.md + design.md + TODO.md

### 8.3 Complex Project (complex project)

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
├── patches/            # (Optional) Patch docs
│   └── db-migration.patch.md
├── TODO.md
└── src/
```

**Use:** README.md + multiple design.md + changelog.md + TODO.md

---

## 9) Related Documents

| Document | Purpose | Link |
|----------|---------|------|
| **document-design-control.md** | Design document standards | [../document-design-control.md](../document-design-control.md) v1.1 |
| **document-changelog-control.md** | Version tracking system | [../document-changelog-control.md](../document-changelog-control.md) v4.4 |
| **todo-standards.md** | TODO/task standards | [../todo-standards.md](../todo-standards.md) v2.0 |
| **document-patch-control.md** | Patch document standards | [../document-patch-control.md](../document-patch-control.md) v1.0 |
| **strict-file-hygiene.md** | No unrequested files | [../strict-file-hygiene.md](../strict-file-hygiene.md) v1.2 |

---

## 10) Implementation Notes

### 10.1 When to Apply

**Project Start:**
- Use the checklist in Section 5 to define the required documents.

**Document Creation:**
- Use rules related to the created document.

**Updates:**
- When changes are made, use changelog.md according to document-changelog-control.md.

### 10.2 Common Pitfalls (Common Pitfalls)

- ❌ Don't create README.md - every project should have one.
- ❌ Use placeholder Session IDs - must use real UUID
- ❌ Not following the format according to the rule - makes the document uneven
- ❌ Create unnecessary file - violate strict-file-hygiene.md

---

## Version History (Unified)

| Version | Date | Changes | Session ID |
|---------|------|---------|------------|
| 1.4 | 2026-02-21 | **[Synced references to document-changelog-control v4.4](changelog/project-documentation-standards.changelog.md#version-14)** | f19e8a67-d3c2-4c85-aa11-4db6949e61f8 |
| | | Summary: Updated changelog control reference and synchronized design-to-changelog linkage | |
| 1.2 | 2026-02-01 | **[Added Patches Directory Support](changelog/project-documentation-standards.changelog.md#version-12)** | a77b77ae-ef2a-49f6-93d9-f78c8ac2d2f7 |
| | | Summary: Added ./patches/ directory support for complex projects | |
| 1.1 | 2026-02-01 | **[Added Document Patch Control Integration](changelog/project-documentation-standards.changelog.md#version-11)** | a77b77ae-ef2a-49f6-93d9-f78c8ac2d2f7 |
| | | Summary: Integrated Document Patch Control standards | |
| 1.0 | 2026-01-21 | **[Initial Version](changelog/project-documentation-standards.changelog.md#version-10)** | a77b77ae-ef2a-49f6-93d9-f78c8ac2d2f7 |
| | | Summary: Initial release of Project Documentation Standards | |

> Full history: [changelog/project-documentation-standards.changelog.md](changelog/project-documentation-standards.changelog.md)
