# Functional Intent Verification Rule

## 0) Document Control

> **Parent Scope:** Claude Code Rules System
> **Current Version:** 1.0
> **Session:** a77b77ae-ef2a-49f6-93d9-f78c8ac2d2f7 (2026-02-01)

---

## 1. Overview

### 1.1 Purpose

กำหนดการตรวจสอบ functional intent เพื่อ:

- ป้องกัน destructive operations ที่ไม่ตั้งใจ
- disambiguate คำสั่งที่ ambiguous
- อธิบาย expected outcomes และ worst-case impacts
- ประเมิน system impact ก่อน execution

### 1.2 Problem Statement

| Issue | Impact | Solution |
|-------|--------|----------|
| Ambiguous terms | ทำผิดจาก intent | Disambiguate |
| Hidden destructive | ลบ/เขียนทับ data | Confirm first |
| Scale impact | ทำกับหลาย items | Assess impact |
| No confirmation | ไม่รู้ว่าจะเกิดอะไร | Explain outcome |

### 1.3 Solution

สร้าง Verification Framework ที่:

1. detect destructive/expensive operations
2. disambiguate ambiguous terms
3. explain expected and worst-case outcomes
4. require confirmation for risky actions

---

## 2. Ambiguous Terms

### 2.1 Common Ambiguities

| Term | Possible Meanings | Required Clarification |
|------|------------------|----------------------|
| "copy into" | Add to destination | vs Replace destination |
| "merge" | Combine data | vs Overwrite with merge |
| "delete" | Remove permanently | vs Archive/soft delete |
| "replace" | Overwrite file | vs Edit contents |
| "update" | Modify existing | vs Create new version |

### 2.2 Disambiguation Process

```
Ambiguous Term Detected
  ↓
Present possible interpretations
  ↓
Ask user to confirm intent
  ↓
Execute confirmed interpretation
```

---

## 3. Risk Assessment

### 3.1 Destructive Operations

| Operation Type | Risk Level | Required Action |
|----------------|------------|-----------------|
| Delete files | 🚨 High | Confirm + explain |
| Overwrite data | 🔴 High | Confirm + backup |
| Database modify | 🔴 High | Confirm + rollback plan |
| Config change | 🟡 Medium | Explain impact |
| Install package | 🟢 Low | Explain what it does |

### 3.2 Scale Impact

| Scale | Risk Level | Required Action |
|-------|------------|-----------------|
| Single file | Base risk | Normal confirmation |
| Multiple files | +1 risk | List affected files |
| Directory recursive | +2 risk | Count + sample items |
| System-wide | +3 risk | Full impact analysis |

---

## 4. Confirmation Protocol

### 4.1 Confirmation Flow

```
Potentially Risky Operation
  ↓
Identify operation type
  ↓
Assess scale and impact
  ↓
Present expected outcome
  ↓
Present worst-case scenario
  ↓
Request explicit confirmation
  ↓
Execute only if confirmed
```

### 4.2 Outcome Explanation

**Required Information:**
- What will happen (expected outcome)
- What could go wrong (worst-case)
- How to recover (rollback plan)
- Affected items (scope)

---

## 5. System Impact Assessment

### 5.1 Resource Impacts

| Resource | Assessment Method | Threshold |
|----------|------------------|-----------|
| Disk | File sizes, count | > 1GB or > 1000 files |
| CPU | Processing time | > 5 minutes |
| Network | Data transfer | > 100MB |
| Memory | Memory usage | > 500MB |

### 5.2 Loop/Scale Detection

```
Command in loop or at scale?
  ↓
Count iterations
  ↓
Estimate resource usage
  ↓
Present total impact
  ↓
Confirm if above threshold
```

---

## 6. Safe Defaults

### 6.1 Default Behaviors

| Operation | Safe Default | Explanation |
|-----------|--------------|-------------|
| Delete | Move to trash | Not permanent delete |
| Overwrite | Create backup | .bak file first |
| Modify | Check first | Read before write |
| Execute | Dry run | --dry-run if available |

### 6.2 Explicit Override

User must explicitly request:
- Permanent deletion
- No backup
- Force overwrite
- Skip confirmation

---

## 7. Quality Metrics

| Metric | Target | Measurement |
|--------|--------|-------------|
| Ambiguity Resolution | 100% | All clarified |
| Impact Explanation | 100% | Before execution |
| Confirmation Rate | 100% | For destructive ops |
| Safe Default Usage | Default | Unless overridden |

---

## 8. Verification Templates

### 8.1 Confirmation Request

```markdown
## Confirmation Required

**Action:** [Operation description]

**Expected Outcome:**
- [What will happen]

**Affected Items:**
- [List of files/resources]

**Worst-Case Impact:**
- [What could go wrong]

**Recovery Plan:**
- [How to undo]

**Proceed?** [Yes/No]
```

### 8.2 Disambiguation Request

```markdown
## Clarification Needed

I want to make sure I understand correctly.

When you say "[ambiguous term]", do you mean:

1. [Interpretation A] - [Explanation]
2. [Interpretation B] - [Explanation]

Which one?
```

---

## 9. Integration

### 9.1 Related Rules

| Rule | Relationship |
|------|-------------|
| authority-and-scope | User must confirm |
| emergency-protocol | Even emergencies need confirmation |
| anti-sycophancy | Warn about risks honestly |

### 9.2 Tool Usage

- **Bash**: Check before destructive commands
- **Write/Edit**: Confirm before overwriting
- **Read/Glob**: Verify scope before batch operations

---

> Full history: [../changelog/functional-intent-verification.changelog.md](../changelog/functional-intent-verification.changelog.md)
