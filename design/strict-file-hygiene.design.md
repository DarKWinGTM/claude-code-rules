# Strict File Hygiene Design

## 0) Document Control

> **Parent Scope:** Claude Code Rules System
> **Current Version:** 1.0
> **Session:** a77b77ae-ef2a-49f6-93d9-f78c8ac2d2f7 (2026-02-01)

---

## 1. Overview

### 1.1 Purpose

กำหนดนโยบาย Strict File Hygiene เพื่อ:

- ป้องกันการสร้างไฟล์ขยะ (junk files) ที่ไม่จำเป็น
- ลดความซ้ำซ้อนของไฟล์ (duplicate files)
- รักษาความสะอาดของ Project structure
- ให้ AI สร้างไฟล์เฉพาะเมื่อจำเป็นหรือได้รับคำสั่งเท่านั้น

### 1.2 Problem Statement

| Issue | Impact | Solution |
|-------|--------|----------|
| Duplicate versions | สับสนว่าไฟล์ไหนล่าสุด | Edit existing file |
| Unrequested docs | รก project, ไม่ได้ใช้ | Ask before create |
| Junk files | เปลือง space, จัดการยาก | Only functional files |
| Suffix versions | Git history ไม่ถูกใช้ | Use Git for history |

### 1.3 Solution

สร้าง Hygiene Framework ที่:

1. บังคับ Edit แทน Create หากไฟล์มีอยู่แล้ว
2. ห้ามสร้าง version suffixes (v1, v2, final)
3. ต้องได้รับคำสั่งชัดเจนสำหรับ non-functional files
4. ใช้ Git ในการจัดการ version history

---

## 2. Core Principles

### 2.1 Allowed vs Not Allowed

**Allowed:**
- Functional code/config required for system operation
- Documents explicitly requested by user
- Temporary files in `/tmp` (should clean up when done)

**Not Allowed:**
- Versioned copies such as `file-v2`, `_final`, `plan-2026`
- Checkpoint/summary/plan files not requested by user
- Proactive docs (README/PLAN/TODO) without asking
- "Work summary/Change summary" files not requested

### 2.2 Operational Rules

1. **Existing file first**: If file exists, edit it only
2. **Ask when unclear**: If document necessity is unclear, always ask first
3. **Exception handling**: If new file is necessary, state brief reason before creating

---

## 3. Implementation

### 3.1 Decision Flow

```
AI wants to create a file
  ↓
Does file already exist?
  → YES: Edit the existing file
  → NO: Continue
  ↓
Is it a functional file (code/config)?
  → YES: Create allowed
  → NO: Continue
  ↓
Did user explicitly ask for it?
  → YES: Create allowed
  → NO: DO NOT CREATE
```

### 3.2 Naming Conventions

**Prohibited Suffixes:**
- `-v1`, `-v2`, etc.
- `_final`, `_draft`
- `_backup`, `_old`
- `.bak` (unless specifically requested for safety)

**Correct Approach:**
- Use the standard filename (e.g., `script.py`)
- Rely on Git for versioning and backups

---

## 4. Quality Metrics

| Metric | Target | Measurement |
|--------|--------|-------------|
| Duplicate Files | 0% | No versioned copies |
| Unrequested Docs | 0% | Only requested docs |
| File Relevance | 100% | All files serve purpose |
| Git Usage | Default | For history/versioning |

---

## 5. Integration

### 5.1 Related Rules

| Rule | Relationship |
|------|-------------|
| document-consistency | Reduce duplicates, consistent naming |
| no-variable-guessing | Don't guess file requirements |
| authority-and-scope | Follow user commands |

### 5.2 Conflict Resolution

If user asks to create a file that violates hygiene (e.g., "create version 2"):
- **Follow User Authority**: User command overrides hygiene rule.
- **Suggestion**: Can politely suggest using Git, but must obey command.

---

> Full history: [../changelog/strict-file-hygiene.changelog.md](../changelog/strict-file-hygiene.changelog.md)
