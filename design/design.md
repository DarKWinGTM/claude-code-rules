# Claude Code Rules System

## Master Design Document

> **Parent Scope:** RULES System Design
> **Current Version:** 1.6
> **Session:** a77b77ae-ef2a-49f6-93d9-f78c8ac2d2f7 (2026-01-21)
> **Full history:** [../changelog/changelog.md](../changelog/changelog.md)

---

## I. Document Control

### I.1 Version Information

**Current Version:** 1.4
**Last Updated:** 2026-01-21
**Status:** Active

### I.2 Change Summary

| Version | Date | Summary | Session ID |
|---------|------|---------|------------|
| 1.6 | 2026-01-21 | Removed Session ID from TODO standard - TODO.md should not have Session ID header | a77b77ae-ef2a-49f6-93d9-f78c8ac2d2f7 |
| 1.5 | 2026-01-21 | Added todo-standards and project-documentation-standards to rule hierarchy, updated rule count to 16 | a77b77ae-ef2a-49f6-93d9-f78c8ac2d2f7 |
| 1.4 | 2026-01-21 | Removed Session ID from Rules File Standard Template (not required for rules files) | a77b77ae-ef2a-49f6-93d9-f78c8ac2d2f7 |
| 1.3 | 2026-01-21 | Restructured to systematic format (Sections I-VIII), added Rules File Standard Template | a77b77ae-ef2a-49f6-93d9-f78c8ac2d2f7 |
| 1.2 | 2026-01-20 | Updated document-changelog-control to v4.3 | a77b77ae-ef2a-49f6-93d9-f78c8ac2d2f7 |
| 1.1 | 2026-01-20 | Added Image Generation Framework | a77b77ae-ef2a-49f6-93d9-f78c8ac2d2f7 |
| 1.0 | 2026-01-16 | Initial master design | a77b77ae-ef2a-49f6-93d9-f78c8ac2d2f7 |

---

## II. Overview

### II.1 Purpose

**Claude Code Rules System** คือชุด rules ที่ควบคุมพฤติกรรมของ AI ใน Claude Code เพื่อ:

- รักษาความถูกต้องและความน่าเชื่อถือ
- ป้องกันปัญหาที่พบบ่อย (hallucination, terminal flooding, etc.)
- ให้ user มี control เหนือ AI
- รักษามาตรฐานคุณภาพสูง

### II.2 Rule Categories

| Category | Rules | Purpose |
|----------|-------|---------|
| **Accuracy & Truth** | zero-hallucination, anti-sycophancy, no-variable-guessing | ข้อมูลถูกต้อง |
| **Output Safety** | safe-file-reading, safe-terminal-output, flow-diagram-no-frame | ป้องกัน flooding |
| **User Control** | authority-and-scope, emergency-protocol, functional-intent-verification | รักษา user authority |
| **Quality** | document-consistency, document-changelog-control, document-design-control, anti-mockup, strict-file-hygiene | คุณภาพ output |

### II.3 Scope

This design document covers:
- Architecture of the rules system
- Standards for creating rules files
- Version tracking and changelog integration
- Quality metrics and compliance
- Usage guidelines

---

## III. Architecture

### III.1 Rule Hierarchy

```
Claude Code Rules System
  ├─ Core Rules (Must Follow)
  │   ├─ authority-and-scope
  │   ├─ zero-hallucination
  │   └─ anti-sycophancy
  │
  ├─ Safety Rules (Prevent Harm)
  │   ├─ safe-file-reading
  │   ├─ safe-terminal-output
  │   ├─ emergency-protocol
  │   └─ functional-intent-verification
  │
  ├─ Quality Rules (Improve Output)
  │   ├─ document-consistency
  │   ├─ document-changelog-control (v4.3)
  │   ├─ document-design-control (v1.2)
  │   ├─ todo-standards (v2.0)
  │   ├─ project-documentation-standards
  │   ├─ anti-mockup
  │   ├─ no-variable-guessing
  │   ├─ flow-diagram-no-frame
  │   └─ strict-file-hygiene
  │
  └─ [Future Rules]
```

### III.2 Rule Dependencies

```
authority-and-scope (Foundation)
  ↓
zero-hallucination + anti-sycophancy (Truth)
  ↓
no-variable-guessing + document-consistency (Verification)
  ↓
safe-file-reading + safe-terminal-output (Safety)
  ↓
flow-diagram-no-frame + anti-mockup (Output Quality)
  ↓
emergency-protocol + functional-intent-verification (Execution)
```

---

## IV. Sub-Rule Index

### IV.1 Current Rules (16 Rules)

| # | Rule | Design Doc | Purpose |
|---|------|------------|---------|
| 1 | anti-mockup.md | anti-mockup.design.md | Real systems over mocks |
| 2 | anti-sycophancy.md | anti-sycophancy.design.md | Truth over pleasing |
| 3 | authority-and-scope.md | authority-and-scope.design.md | User authority |
| 4 | document-consistency.md | document-consistency.design.md | Cross-reference validation |
| 5 | document-changelog-control.md | document-changelog-control.design.md v4.3 | Version tracking standard |
| 6 | document-design-control.md | document-design-control.design.md v1.2 | Design document standards |
| 7 | emergency-protocol.md | emergency-protocol.design.md | Emergency response |
| 8 | flow-diagram-no-frame.md | flow-diagram-no-frame.design.md | No box diagrams |
| 9 | functional-intent-verification.md | functional-intent-verification.design.md | Verify before destructive |
| 10 | no-variable-guessing.md | no-variable-guessing.design.md | Read before reference |
| 11 | project-documentation-standards.md | project-documentation-standards.design.md | Project documentation standards |
| 12 | safe-file-reading.md | safe-file-reading.design.md | UOLF for file reading |
| 13 | safe-terminal-output.md | safe-terminal-output.design.md | UOLF for terminal output |
| 14 | strict-file-hygiene.md | strict-file-hygiene.design.md | Prevent non-functional files |
| 15 | todo-standards.md | todo-standards.design.md v2.0 | Simple TODO lists |
| 16 | zero-hallucination.md | zero-hallucination.design.md | Verified information only |

### IV.2 Reserved for Future Rules

| Category | Potential Rules | Purpose |
|----------|-----------------|---------|
| Security | code-review-security | Security review automation |
| Performance | performance-optimization | Performance guidelines |
| Testing | test-coverage | Testing requirements |
| Documentation | auto-documentation | Documentation generation |

---

## V. Standards & Frameworks

### V.1 Memory Hierarchy (Official Spec)

> **Source:** [Memory Management - Claude Code Docs](https://code.claude.com/docs/en/memory)

Claude Code uses a **hierarchical memory system** with 5 levels:

| Memory Type | Location | Purpose | Shared With | Priority |
|-------------|----------|---------|-------------|----------|
| **Enterprise Policy** | macOS: `/Library/Application Support/ClaudeCode/CLAUDE.md`<br>Linux: `/etc/claude-code/CLAUDE.md`<br>Windows: `C:\Program Files\ClaudeCode\CLAUDE.md` | Organization-wide instructions | All users | 1 (Highest) |
| **Project Memory** | `./CLAUDE.md` or `./.claude/CLAUDE.md` | Team-shared instructions | Team via git | 2 |
| **Project Rules** | `./.claude/rules/*.md` | Modular, topic-specific rules | Team via git | 2 |
| **User Memory** | `~/.claude/CLAUDE.md` | Personal preferences | Just you (all projects) | 3 |
| **Project Local** | `./CLAUDE.local.md` | Personal project-specific | Just you (current project) | 4 (Lowest) |

### V.2 .claude/rules/ Format (Official Spec)

> **Source:** [Memory Management - Modular Rules](https://code.claude.com/docs/en/memory#modular-rules-with-clauderules)

**Directory Structure:**
```
your-project/
├── .claude/
│   ├── CLAUDE.md           # Main project instructions
│   └── rules/
│       ├── code-style.md   # Topic-specific rules
│       ├── frontend/       # Subdirectories allowed
│       │   ├── react.md
│       │   └── styles.md
│       └── backend/
│           ├── api.md
│           └── database.md
```

**Path-Specific Rules (YAML frontmatter):**
```yaml
---
paths:
  - "src/api/**/*.ts"
  - "lib/**/*.ts"
---

# API Development Rules
- All API endpoints must include input validation
```

### V.3 Memory Import Syntax (Official Spec)

> **Source:** [Memory Management - CLAUDE.md Imports](https://code.claude.com/docs/en/memory#claudemd-imports)

**Syntax:** `@path/to/import`

```markdown
See @README for project overview and @package.json for available commands.

# Additional Instructions
- git workflow @docs/git-instructions.md
```

**Features:**
- Relative and absolute paths supported
- Max recursion: 5 hops
- Can import from user home: `@~/.claude/my-project-instructions.md`

### V.4 Subagents Format (Official Spec)

> **Source:** [Subagents - Claude Code Docs](https://code.claude.com/docs/en/sub-agents)

**YAML Frontmatter:**
```yaml
---
name: code-reviewer
description: Reviews code for quality and best practices
tools: Read, Glob, Grep
model: sonnet
---

You are a code reviewer...
```

**Scope:**
| Location | Priority |
|----------|----------|
| `--agents` CLI flag | 1 (highest) |
| `.claude/agents/` | 2 |
| `~/.claude/agents/` | 3 |
| Plugin's `agents/` | 4 (lowest) |

### V.5 Shared Frameworks

**UOLF (Universal Output Limit Framework)**
- Used by: safe-file-reading, safe-terminal-output
- MAX_OUTPUT_CHARS = 5000 (hard limit)
- Double limit: `<command> | head -100 | head -c 5000`

**Evidence-Based Framework**
- Used by: zero-hallucination, anti-sycophancy, no-variable-guessing
- Verify before stating claims
- Acknowledge uncertainty when unsure

**User Authority Framework**
- Used by: authority-and-scope, emergency-protocol, functional-intent-verification
- Priority: User > Safety > Rules > Defaults

---

## VI. Rules File Standard Template

### VI.1 Purpose

กำหนดรูปแบบมาตรฐาน (standard template) สำหรับ rules files (`.md`) เพื่อให้ทุกไฟล์มีความสม่ำเสมอกัน

### VI.2 Mandatory Structure

**All rules files MUST follow this template:**

```markdown
# [Rule Name]

> **Current Version:** X.X

## Rule Statement

**Core Principle:** [One-line summary]

**Design:** [rule-name.design.md](design/rule-name.design.md) vX.X

This rule ensures...

---

[Content sections...]

---

> Full history: [changelog/rule-name.changelog.md](changelog/rule-name.changelog.md)
```

### VI.3 Header Requirements (MANDATORY)

| Element | Required | Format |
|---------|----------|--------|
| **Current Version** | ✅ Yes | `> **Current Version:** X.X` |
| **Design Link** | Optional | `**Design:** [file.design.md](design/file.design.md) vX.X` |

### VI.4 Content Sections

**Rules files should include:**

1. **Rule Statement** - Core principle
2. **Core Requirements** - Mandatory actions
3. **Examples** - ✅ Correct/❌ Incorrect patterns
4. **Quality Metrics** - Measurable targets
5. **Integration** - Related rules

### VI.5 PROHIBITED Elements

| Element | Why Prohibited | Correct Alternative |
|---------|----------------|---------------------|
| **Version Table** | Version history belongs in changelog | Use changelog link |
| **Placeholders** | Violates changelog rules | Use real data or omit |
| **Mixed Formats** | Breaks consistency | Follow this template |

### VI.6 Changelog Integration

**Rules files MUST:**

1. **Link to changelog** (at end):
   ```markdown
   > Full history: [changelog/rule-name.changelog.md](changelog/rule-name.changelog.md)
   ```

2. **NOT have Version table** in rules file:
   - ❌ WRONG: Version table in rules file
   - ✅ RIGHT: Version table ONLY in changelog file

3. **Changelog file format:**
   - changelog/rule-name.changelog.md = Full history with detailed sections
   - changelog/changelog.md = Master changelog (for entire project)

### VI.7 Examples

**✅ Correct Rules File:**

```markdown
# Document Changelog Control

> **Current Version:** 4.3

## Rule Statement

Core Principle: Every document must have traceable version history with real session IDs.

---

[Content...]

---

> Full history: [changelog/document-changelog-control.changelog.md](changelog/document-changelog-control.changelog.md)
```

**❌ Incorrect Rules File:**

```markdown
# Some Rule

## Rule Statement
...

---

## Version  ← WRONG: Remove this table
| Version | Date | Notes |
| 1.0 | 2026-01-21 | Initial |
```

---

## VII. Quality Metrics

### VII.1 System-Wide Metrics

| Metric | Target | Rules Involved |
|--------|--------|----------------|
| Accuracy | 100% | zero-hallucination, anti-sycophancy |
| User Authority | Preserved | authority-and-scope, emergency-protocol |
| Output Safety | ≤ 5000 chars | safe-file-reading, safe-terminal-output |
| Verification | Default | no-variable-guessing, document-consistency |
| Transparency | 100% | anti-mockup |
| Document Consistency | 100% | document-*, flow-diagram-no-frame |

### VII.2 Compliance Rate

- **Constitutional Compliance**: 100% (No exceptions)
- **User Override Respect**: 100%
- **Evidence-Based**: Default behavior
- **Hallucination**: 0%
- **Template Compliance**: 100% (all rules follow standard template)

---

## VIII. Creating New Rules

### VIII.1 Step-by-Step Process

**Step 1: Create Design Document**
```bash
touch design/[rule-name].design.md
```

**Step 2: Create Rules File**
```bash
touch [rule-name].md
```

**Step 3: Create Changelog**
```bash
touch changelog/[rule-name].changelog.md
```

**Step 4: Add to Master Design**
- Update Sub-Rule Index (Section IV)
- Update Rule Hierarchy (Section III)
- Add to Rule Categories (Section II)

**Step 5: Update README**
- Add rule to rules list
- Update documentation

### VIII.2 Rules File Template

```markdown
# [Rule Name]

> **Current Version:** 1.0
> **Session:** [UUID] (YYYY-MM-DD)

## Rule Statement

**Core Principle:** [One-line principle]

**Design:** [rule-name.design.md](design/rule-name.design.md) v1.0

This rule ensures...

---

## Core Requirements

### 1. [Category]

**Required Actions:**
- [Action 1]
- [Action 2]

---

## Examples

### ✅ Correct

[Example of correct usage]

### ❌ Incorrect

[Example of incorrect usage]

---

## Quality Metrics

| Metric | Target |
|--------|--------|
| [Metric 1] | [Target] |

---

## Integration

Related Rules:
- [rule-1.md](rule-1.md)
- [rule-2.md](rule-2.md)

---

> Full history: [changelog/rule-name.changelog.md](changelog/rule-name.changelog.md)
```

### VIII.3 Checklist for New Rules

- [ ] Create `[rule-name].md` following standard template
- [ ] Create `[rule-name].design.md` with design details
- [ ] Create `changelog/[rule-name].changelog.md` for version tracking
- [ ] Add to master design (Section IV: Sub-Rule Index)
- [ ] Update rule hierarchy if needed
- [ ] Define quality metrics
- [ ] Specify related rules
- [ ] Update README.md
- [ ] Test rule with real scenarios
- [ ] Document examples

---

## Appendix A: Image Generation Framework

### A.1 Purpose

Framework สำหรับสร้างภาพประกอบของ Claude Code Rules System
ออกแบบโดย A-PIRO (Automatic Prompt Intent Recognition Optimization)

### A.2 File Structure

```
/home/node/workplace/AWCLOUD/CLAUDE/claude-code-image-generator/
├── image_gen.py                 # Image generation script
├── image.prompt.design.md       # 140 prompts (10 styles × 14 rules)
├── generated_images/            # Generated images
└── design.md                     # Master design reference
```

### A.3 10 Visual Styles

| # | Style Name | Concept | Best For |
|---|------------|---------|----------|
| 1 | Citadel | Architectural fortress | Technical documentation |
| 2 | World Tree | Organic bioluminescent tree | Natural presentation |
| 3 | Orrery | Steampunk mechanical clock | Precision/engineering |
| 4 | Geometric | Abstract 3D shapes | Minimalist/modern |
| 5 | Constellation | Cosmic star patterns | Inspirational/cosmic |
| 6 | Zen Garden | Japanese balanced garden | Balance/harmony |
| 7 | Wardens | Cyberpunk guardians | Team/guardian narrative |
| 8 | Blueprint | Holographic HUD interface | Technical/HUD |
| 9 | Neural | Brain-like command center | AI/brain metaphor |
| 10 | Alchemical | Surrealist transformation | Artistic/philosophical |

### A.4 Generation Command

> **See:** [image.prompt.design.md](image.prompt.design.md) for complete prompt specifications

```bash
# Generate image for specific rule
python image_gen.py "<prompt>" --doc <rule-name>.md --aspect-ratio 16:9 --image-size 2K
```

---

> Full history: [changelog/changelog.md](changelog/changelog.md)
