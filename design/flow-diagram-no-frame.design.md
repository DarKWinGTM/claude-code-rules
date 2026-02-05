# Flow Diagram No-Frame Rule

## 0) Document Control

> **Parent Scope:** Claude Code Rules System
> **Current Version:** 1.0
> **Session:** a77b77ae-ef2a-49f6-93d9-f78c8ac2d2f7 (2026-02-01)

---

## 1. Overview

### 1.1 Purpose

กำหนดมาตรฐานการวาด Flow Diagrams เพื่อ:

- ป้องกันปัญหา rendering ของ Unicode box characters
- ให้ diagrams แสดงผลถูกต้องทุก terminal/viewer
- ใช้ text-based approach ที่ reliable
- รักษา readability และ accuracy

### 1.2 Problem Statement

| Issue | Impact | Solution |
|-------|--------|----------|
| Font misalignment | Box ไม่ตรงกัน | No boxes |
| Copy/paste breaks | Format เสียหาย | Use arrows only |
| Terminal wrapping | Line ตัดผิดที่ | Max 80 chars |
| Inconsistent render | ดูต่างกันในแต่ละ viewer | Text-based only |

### 1.3 Solution

สร้าง Diagram Standard ที่:

1. ห้ามใช้ box-drawing characters ทุกชนิด
2. ใช้ arrows และ indentation แทน
3. จำกัด line width ไม่เกิน 80 characters
4. ใช้ text labels แทน boxes

---

## 2. Character Prohibitions

### 2.1 Banned Unicode Characters

| Category | Characters | Status |
|----------|------------|--------|
| Light Box | `┌ ┐ └ ┘ ─ │ ├ ┤ ┬ ┴ ┼` | ❌ BANNED |
| Heavy Box | `┏ ┓ ┗ ┛ ━ ┃ ┣ ┫ ┳ ┻ ╋` | ❌ BANNED |
| Double Box | `╔ ╗ ╚ ╝ ═ ║ ╠ ╣ ╦ ╩ ╬` | ❌ BANNED |
| Rounded | `╭ ╮ ╯ ╰` | ❌ BANNED |

### 2.2 Banned ASCII Patterns

```text
BANNED:
+----+    +======+    .-----.
|    |    |      |    |     |
+----+    +======+    '-----'
```

### 2.3 Banned Long Lines

```text
BANNED as borders:
═══════════════════════
───────────────────────
-----------------------
=======================
```

---

## 3. Allowed Symbols

### 3.1 Connector Symbols

| Symbol | Name | Usage |
|--------|------|-------|
| `→` | Arrow right | Flow direction |
| `↓` | Arrow down | Vertical flow |
| `├─` | Tree branch | Hierarchy (max 3 chars) |
| `└─` | Tree end | Last item |

### 3.2 Hard Requirements

1. Max line width: ≤ 80 characters
2. Use indentation for hierarchy
3. Use text labels instead of boxes
4. Use arrows only for real relationships

---

## 4. Canonical Patterns

### 4.1 Step Chain (Preferred)

```text
Authentication Flow

Step 1: User submits credentials
  → Step 2: Validate input format
  → Step 3: Check against database
  → Step 4: Generate JWT token
  → Step 5: Return response
```

### 4.2 Vertical Flow

```text
Startup Sequence

Initialize config
  ↓
Load environment variables
  ↓
Connect to database
  ↓
Start HTTP server
```

### 4.3 Hierarchy (Tree)

```text
Project Structure

src/
  ├─ components/
  ├─ services/
  └─ utils/
```

### 4.4 Decision Flow

```text
Request Handler

Receive request
  ↓
Check auth?
  → YES: Process request → Return 200
  → NO: Return 401 Unauthorized
```

---

## 5. Anti-Patterns

### 5.1 Box Around Content (WRONG)

```text
WRONG - DO NOT USE:
┌─────────────────┐
│  User Input     │
└─────────────────┘
```

### 5.2 Correct Alternative

```text
RIGHT - USE THIS:
User Input
  ↓
Validation
  ↓
Database
```

---

## 6. Fallback Rules

| Situation | Solution |
|-----------|----------|
| Complex flow | Numbered list with indentation |
| Wide diagram | Split into smaller diagrams |
| Need grouping | Headers and indentation |
| Need emphasis | **bold text** or CAPS |

---

## 7. Quality Metrics

| Metric | Target | Measurement |
|--------|--------|-------------|
| Box Characters | 0% | No box drawing |
| Line Width | ≤ 80 | All lines under limit |
| Rendering Consistency | 100% | Works in all viewers |
| Readability | High | Clear structure |

---

## 8. Detection Checklist

Before outputting diagram:

- [ ] No Unicode box characters
- [ ] No ASCII box patterns
- [ ] No long border lines
- [ ] All lines ≤ 80 characters
- [ ] Uses only allowed connectors
- [ ] Follows canonical patterns

---

## 9. Integration

### 9.1 Scope

Applies to ALL text-based diagrams:
- Flow diagrams
- Sequence diagrams
- Process diagrams
- Architecture diagrams
- System diagrams
- Any diagram in markdown code blocks

### 9.2 Related Rules

| Rule | Relationship |
|------|-------------|
| document-consistency | Diagrams must be consistent |
| safe-terminal-output | Output must be readable |

---

> Full history: [../changelog/flow-diagram-no-frame.changelog.md](../changelog/flow-diagram-no-frame.changelog.md)
