# 🧭 Flow Diagram Rule: No Frame / No Box (Strict)

## Rule Statement

When writing Flow Diagrams (ASCII diagrams inside markdown/code blocks), **NEVER draw frames, boxes, or rectangles** around content. Unicode box-drawing characters render inconsistently across terminals and viewers.

## Rationale

Unicode box-drawing characters (┌ ─ ┐ │ etc.) have inconsistent rendering:
- Different font metrics cause misalignment
- Copy/paste breaks formatting
- Terminal width causes wrapping
- Markdown viewers render differently

**Priority: Accuracy and readability over visual aesthetics**

## Scope

Applies to ALL text-based diagrams:
- Flow diagrams, sequence diagrams, process diagrams
- Architecture diagrams, system diagrams
- Any diagram in markdown code blocks

## ABSOLUTE PROHIBITIONS (NEVER USE)

### 1. Unicode Box-Drawing Characters (ALL BANNED)

**Light Box (BANNED)**:
`┌ ┐ └ ┘ ─ │ ├ ┤ ┬ ┴ ┼`

**Heavy Box (BANNED)**:
`┏ ┓ ┗ ┛ ━ ┃ ┣ ┫ ┳ ┻ ╋`

**Double Box (BANNED)**:
`╔ ╗ ╚ ╝ ═ ║ ╠ ╣ ╦ ╩ ╬`

**Rounded Corners (BANNED)**:
`╭ ╮ ╯ ╰`

**Mixed/Other (BANNED)**:
`╒ ╓ ╘ ╙ ╛ ╜ ╞ ╟ ╡ ╢ ╤ ╥ ╧ ╨ ╪ ╫`

### 2. ASCII Box Characters (ALL BANNED)

```
BANNED patterns:
+----+    +======+    .-----.
|    |    |      |    |     |
+----+    +======+    '-----'
```

### 3. Long Horizontal Lines (BANNED as borders)

```
BANNED:
═══════════════════════
───────────────────────
-----------------------
=======================
```

## ALLOWED Connectors (Use These Only)

| Symbol | Name | Usage |
|--------|------|-------|
| `→` | Arrow right | Flow direction |
| `↓` | Arrow down | Vertical flow |
| `├─` | Tree branch | Hierarchy (short only, max 3 chars) |
| `└─` | Tree end | Last item in hierarchy |

## Hard Requirements

1. **Max line width**: ≤ 80 characters
2. **Use indentation** for hierarchy (not boxes)
3. **Use text labels** instead of boxes around content
4. **Use arrows** only for real relationships

## Canonical Patterns (USE THESE)

### 1) Step chain (PREFERRED)

```text
Authentication Flow

Step 1: User submits credentials
  → Step 2: Validate input format
  → Step 3: Check against database
  → Step 4: Generate JWT token
  → Step 5: Return response
```

### 2) Vertical flow with arrows

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

### 3) Hierarchy with tree branches

```text
Project Structure

src/
  ├─ components/
  ├─ services/
  └─ utils/
```

### 4) Parallel processes (no frames)

```text
Background Workers

Worker A → process queue → save results
Worker B → process queue → save results
Worker C → process queue → save results
```

### 5) Decision flow (text-based)

```text
Request Handler

Receive request
  ↓
Check auth?
  → YES: Process request → Return 200
  → NO: Return 401 Unauthorized
```

## ANTI-PATTERNS (NEVER USE)

### ❌ BANNED: Box around content

```text
WRONG - DO NOT USE:
┌─────────────────┐
│  User Input     │
└─────────────────┘
        ↓
┌─────────────────┐
│  Validation     │
└─────────────────┘
```

### ❌ BANNED: Double-line boxes

```text
WRONG - DO NOT USE:
╔═══════════════╗
║   Database    ║
╚═══════════════╝
```

### ❌ BANNED: ASCII art boxes

```text
WRONG - DO NOT USE:
+---------------+
|   Component   |
+---------------+
```

### ✅ CORRECT: Same content without boxes

```text
RIGHT - USE THIS:
User Input
  ↓
Validation
  ↓
Database
```

## Fallback Rules

1. **Complex flow?** → Use numbered list with indentation
2. **Wide diagram?** → Split into multiple smaller diagrams
3. **Need grouping?** → Use headers and indentation, NOT boxes
4. **Need emphasis?** → Use **bold text** or CAPS, NOT frames
