# Claude Code Rules System

## Master Design Document

---

## Changelog

| Date | Change |
|------|--------|
| 2026-01-16 | สร้าง Master Design Document สำหรับระบบ Rules |
| 2026-01-16 | รวม design จาก 11 sub-rules |
| 2026-01-16 | กำหนดโครงสร้างสำหรับ rules ใหม่ในอนาคต |

---

## 1. Overview

### 1.1 Purpose

**Claude Code Rules System** คือชุด rules ที่ควบคุมพฤติกรรมของ AI ใน Claude Code เพื่อ:

- รักษาความถูกต้องและความน่าเชื่อถือ
- ป้องกันปัญหาที่พบบ่อย (hallucination, terminal flooding, etc.)
- ให้ user มี control เหนือ AI
- รักษามาตรฐานคุณภาพสูง

### 1.2 Rule Categories

| Category | Rules | Purpose |
|----------|-------|---------|
| **Accuracy & Truth** | zero-hallucination, anti-sycophancy, no-variable-guessing | ข้อมูลถูกต้อง |
| **Output Safety** | safe-file-reading, safe-terminal-output, flow-diagram-no-frame | ป้องกัน flooding |
| **User Control** | authority-and-scope, emergency-protocol, functional-intent-verification | รักษา user authority |
| **Quality** | document-consistency, anti-mockup | คุณภาพ output |

---

## 2. Architecture

### 2.1 Rule Hierarchy

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
  │   ├─ anti-mockup
  │   ├─ no-variable-guessing
  │   └─ flow-diagram-no-frame
  │
  └─ [Future Rules]
```

### 2.2 Rule Dependencies

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

## 3. Sub-Rule Index

### 3.1 Current Rules (11 Rules)

| # | Rule | Design Doc | Purpose |
|---|------|------------|---------|
| 1 | anti-mockup.md | anti-mockup.design.md | Real systems over mocks |
| 2 | anti-sycophancy.md | anti-sycophancy.design.md | Truth over pleasing |
| 3 | authority-and-scope.md | authority-and-scope.design.md | User authority |
| 4 | document-consistency.md | document-consistency.design.md | Cross-reference validation |
| 5 | emergency-protocol.md | emergency-protocol.design.md | Emergency response |
| 6 | flow-diagram-no-frame.md | flow-diagram-no-frame.design.md | No box diagrams |
| 7 | functional-intent-verification.md | functional-intent-verification.design.md | Verify before destructive |
| 8 | no-variable-guessing.md | no-variable-guessing.design.md | Read before reference |
| 9 | safe-file-reading.md | safe-file-reading.design.md | UOLF for file reading |
| 10 | safe-terminal-output.md | safe-terminal-output.design.md | UOLF for terminal output |
| 11 | zero-hallucination.md | zero-hallucination.design.md | Verified information only |

### 3.2 Reserved for Future Rules

| Category | Potential Rules | Purpose |
|----------|-----------------|---------|
| Security | code-review-security | Security review automation |
| Performance | performance-optimization | Performance guidelines |
| Testing | test-coverage | Testing requirements |
| Documentation | auto-documentation | Documentation generation |

---

## 4. Shared Frameworks

### 4.1 UOLF (Universal Output Limit Framework)

**Used by:** safe-file-reading, safe-terminal-output

| Constant | Value | Purpose |
|----------|-------|---------|
| MAX_OUTPUT_CHARS | 5000 | Hard limit ทุกกรณี |
| MAX_OUTPUT_LINES | 100 | Soft limit |
| RISKY_FILE_CHARS | 3000 | For risky files |
| PREVIEW_CHARS | 2000 | Quick preview |

**Double Limit Pattern:**
```bash
<command> | head -100 | head -c 5000
```

### 4.2 Evidence-Based Framework

**Used by:** zero-hallucination, anti-sycophancy, no-variable-guessing

```
Before Making Claim
  ↓
Can verify with tools? → Verify
  ↓
Verified? → State with confidence
  ↓
Uncertain? → Acknowledge uncertainty
```

### 4.3 User Authority Framework

**Used by:** authority-and-scope, emergency-protocol, functional-intent-verification

```
Priority Order:
1. User Instructions (Highest)
2. Safety Policies
3. Project Rules
4. Default Behaviors (Lowest)
```

---

## 5. Quality Metrics

### 5.1 System-Wide Metrics

| Metric | Target | Rules Involved |
|--------|--------|----------------|
| Accuracy | 100% | zero-hallucination, anti-sycophancy |
| User Authority | Preserved | authority-and-scope, emergency-protocol |
| Output Safety | ≤ 5000 chars | safe-file-reading, safe-terminal-output |
| Verification | Default | no-variable-guessing, document-consistency |
| Transparency | 100% | anti-mockup |

### 5.2 Compliance Rate

- **Constitutional Compliance**: 100% (No exceptions)
- **User Override Respect**: 100%
- **Evidence-Based**: Default behavior
- **Hallucination**: 0%

---

## 6. Adding New Rules

### 6.1 Rule Template

```markdown
# [Rule Name]

## Rule Statement

**Core Principle: [One-line principle]**

[Description]

---

## Core Requirements

### 1. [Requirement Category]

**Required Actions:**
- [Action 1]
- [Action 2]

---

## Quality Metrics

| Metric | Target |
|--------|--------|
| [Metric 1] | [Target] |

---

## Version

| Version | Date | Notes |
|---------|------|-------|
| 1.0 | [Date] | Initial version |
```

### 6.2 Design Document Template

```markdown
# [Rule Name]

## Rule Design Document

---

## Changelog

| Date | Change |
|------|--------|
| [Date] | Initial design document |

---

## 1. Overview

### 1.1 Purpose
[Why this rule exists]

### 1.2 Problem Statement
[What problem it solves]

### 1.3 Solution
[How it solves the problem]

---

## 2. Core Principles
[Key principles]

---

## 3. Implementation
[How to implement]

---

## 4. Quality Metrics
[Metrics to track]

---

## 5. Integration
[Related rules and tools]

---

## 6. Version
[Version history]
```

### 6.3 Checklist for New Rules

- [ ] Create `[rule-name].md` with rule content
- [ ] Create `[rule-name].design.md` with design details
- [ ] Add to this master design document
- [ ] Define quality metrics
- [ ] Specify related rules
- [ ] Update README.md

---

## 7. File Structure

```
/TEMPLATE/RULES/
  ├─ README.md                           # Overview
  ├─ design.md                           # This master design
  │
  ├─ anti-mockup.md                      # Rule files
  ├─ anti-mockup.design.md               # Design docs
  ├─ anti-sycophancy.md
  ├─ anti-sycophancy.design.md
  ├─ authority-and-scope.md
  ├─ authority-and-scope.design.md
  ├─ document-consistency.md
  ├─ document-consistency.design.md
  ├─ emergency-protocol.md
  ├─ emergency-protocol.design.md
  ├─ flow-diagram-no-frame.md
  ├─ flow-diagram-no-frame.design.md
  ├─ functional-intent-verification.md
  ├─ functional-intent-verification.design.md
  ├─ no-variable-guessing.md
  ├─ no-variable-guessing.design.md
  ├─ safe-file-reading.md
  ├─ safe-file-reading.design.md
  ├─ safe-terminal-output.md
  ├─ safe-terminal-output.design.md
  ├─ zero-hallucination.md
  └─ zero-hallucination.design.md
```

---

## 8. Usage Guidelines

### 8.1 For Claude Code

Copy rules to `~/.claude/rules/`:
```bash
cp *.md ~/.claude/rules/
```

### 8.2 For Project-Specific

Copy to project's `.claude/rules/`:
```bash
cp *.md /path/to/project/.claude/rules/
```

### 8.3 Scope Configuration

For global rules (no paths restriction):
```markdown
# Don't add paths: to make it global
```

For file-specific rules:
```yaml
paths:
  - src/**/*.ts
  - src/**/*.js
```

---

## 9. Maintenance

### 9.1 Version Management

- Each rule has its own version
- Master design tracks all changes
- Changelog in each file

### 9.2 Update Process

1. Update rule file
2. Update design doc
3. Update this master design
4. Commit with descriptive message
5. Push to GitHub

---

## 10. Version

| Version | Date | Notes |
|---------|------|-------|
| 1.0 | 2026-01-16 | Initial master design with 11 rules |
