# Safe Terminal Output Guide

## 0) Document Control

> **Parent Scope:** Claude Code Rules System
> **Current Version:** 1.1
> **Session:** a77b77ae-ef2a-49f6-93d9-f78c8ac2d2f7 (2026-02-01)

---

## 1. Overview

### 1.1 Purpose

Standardize terminal output management to:

- Prevent terminal flooding from command output
- Use session isolation with `$$` (PID).
- Use UOLF framework to cover all commands.
- Always plan before executing.

### 1.2 Problem Statement

| Issue | Impact | Solution |
|-------|--------|----------|
| Large command output | Terminal flood | Redirect + limit |
| Multi-session collision | File overwrite | $$ (PID) isolation |
| Long lines | 500KB+ on 1 line | Double limit |
| Heredoc $$ issue | $$ not expanded | Correct quoting |

### 1.3 Solution

Create a UOLF + Session Isolation Framework that:

1. Set clear output limits
2. Use `$$` (PID) for unique filenames.
3. Use Double Limit Pattern
4. Supports Heredoc and Multi-Language.

---

## 2. UOLF Framework

### 2.1 Output Limit Constants

| Constant | Value | Purpose |
|----------|-------|---------|
| MAX_OUTPUT_CHARS | 5000 | Hard limit in all cases |
| MAX_OUTPUT_LINES | 100 | Soft limit (if chars OK) |
| RISKY_FILE_CHARS | 3000 | .min.js, .html, .json, .svg |

### 2.2 Universal Pattern

```bash
<command> | head -c 5000          # Character limit
<command> | head -100 | head -c 5000  # Double limit
```

---

## 3. Session Isolation

### 3.1 Using `$$` (PID)

```bash
# ✅ CORRECT: Session-isolated files
/tmp/claude-$$-output.txt    # e.g., /tmp/claude-12345-output.txt

# ❌ WRONG: Shared files (can be overwritten)
/tmp/claude-output.txt
```

### 3.2 Multi-Language PID Patterns

| Language | Session-Isolated Pattern |
|----------|-------------------------|
| **Bash** | `/tmp/claude-$$-output.txt` |
| **Python** | `f'/tmp/claude-{os.getpid()}-output.txt'` |
| **Node.js** | `` `/tmp/claude-${process.pid}-output.txt` `` |
| **Ruby** | `"/tmp/claude-#{Process.pid}-output.txt"` |
| **Perl** | `"/tmp/claude-$$-output.txt"` |

---

## 4. Heredoc Patterns

### 4.1 Heredoc Quoting Rules

| Pattern | `$$` Expansion | Example |
|---------|----------------|---------|
| `<<DELIM` (unquoted) | ✅ Expanded | `python <<PY > /tmp/claude-$$-out.txt` |
| `<<'DELIM'` (single-quoted) | ❌ NOT expanded | Literal `$$` |
| `<<"DELIM"` (double-quoted) | ❌ NOT expanded | Literal `$$` |

### 4.2 Correct Heredoc Patterns

```bash
# Option 1: Unquoted delimiter
python <<PY > /tmp/claude-$$-output.txt 2>&1
print("hello")
PY

# Option 2: Bash variable before heredoc
OUTPUT_FILE="/tmp/claude-$$-output.txt"
python <<'PY' > "$OUTPUT_FILE" 2>&1
print("hello")
PY
```

---

## 5. Command Patterns

### 5.1 Standard Output Locations

| Command Type | Recommended Output File |
|--------------|------------------------|
| General commands | `/tmp/claude-$$-output.txt` |
| Build output | `/tmp/claude-$$-build.log` |
| API responses | `/tmp/claude-$$-api.json` |
| Search results | `/tmp/claude-$$-search.txt` |
| Base64 encoding | `/tmp/claude-$$-base64.txt` |
| Log viewing | `/tmp/claude-$$-logs.txt` |

### 5.2 High-Risk Commands

| Command | Risk Level | Recommended Pattern |
|---------|------------|---------------------|
| `base64 <file>` | 🚨 High | `> /tmp/claude-$$-base64.txt 2>&1` |
| `curl <url>` | 🔴 Medium-High | `> /tmp/claude-$$-api.json 2>&1` |
| `find <path>` | 🔴 Medium-High | `> /tmp/claude-$$-search.txt 2>&1` |
| `grep -r` | 🔴 Medium-High | `> /tmp/claude-$$-search.txt 2>&1` |
| `docker logs` | 🔴 Medium-High | `> /tmp/claude-$$-logs.txt 2>&1` |

---

## 6. Workflow

### 6.1 Evaluate → Plan → Execute

```
Step 1: Evaluate command output potential
  ↓
Step 2: Plan output destination (/tmp/claude-$$-*)
  ↓
Step 3: Execute command with redirect
  ↓
Step 4: Evaluate output file (size, lines, chars)
  ↓
Step 5: Read with appropriate method
```

### 6.2 Complete Pattern

```bash
# Execute with redirect (session-isolated)
<command> > /tmp/claude-$$-output.txt 2>&1

# Evaluate (internal planning)
ls -lh /tmp/claude-$$-output.txt && wc -lwc /tmp/claude-$$-output.txt

# Read based on evaluation
head -100 /tmp/claude-$$-output.txt | head -c 5000
```

---

## 7. Reading Methods

### 7.1 By File Type

| File Type | Recommended Pattern |
|-----------|---------------------|
| `.html` with images | `head -c 3000` |
| `.min.js` / `.min.css` | `head -c 2000` |
| `.json` (unknown) | `head -c 3000` |
| `.svg` | `head -c 2000` |
| Normal source code | `head -100 \| head -c 5000` |

### 7.2 By Output Size

| Output File Size | Lines | Recommended Read Method |
|------------------|-------|------------------------|
| < 10KB | > 50 | `head -100 \| head -c 5000` |
| < 10KB | < 10 | `head -c 2000` |
| 10-50KB | > 100 | `head -100 \| head -c 5000` |
| > 50KB | Any | `head -100 \| head -c 5000` or `head -c 2000` |

---

## 8. Quality Metrics

| Metric | Target | Measurement |
|--------|--------|-------------|
| Output Limit | ≤ 5000 chars | Every command |
| Session Isolation | 100% | All temp files use $$ |
| Double Limit | Default | For all reads |
| Plan Before Execute | Default | Evaluate first |

---

## 9. Cleanup

```bash
# Clean up current session's output files
rm -f /tmp/claude-$$-*.txt /tmp/claude-$$-*.log /tmp/claude-$$-*.json

# Clean up ALL claude output files (use with caution)
rm -f /tmp/claude-*-*.txt /tmp/claude-*-*.log /tmp/claude-*-*.json
```

---

## 10. Integration

### 10.1 Related Rules

| Rule | Relationship |
|------|-------------|
| safe-file-reading | File reading limits |
| no-variable-guessing | Verify before execute |

### 10.2 Synergy with safe-file-reading

- safe-terminal-output: Focus on command output
- safe-file-reading: Focus on reading files
- Both use UOLF constants
- Both use Double Limit Pattern

---

## 11. Quick Reference

```text
UOLF - UNIVERSAL OUTPUT LIMIT FRAMEWORK

Every output → ≤ 5000 chars

CONSTANTS
  MAX_OUTPUT_CHARS = 5000 (hard limit)
  MAX_OUTPUT_LINES = 100 (soft limit)
  RISKY_FILE_CHARS = 3000

SAFE PATTERN (Double Limit)

Step 1: Redirect (with $$ for session isolation)
  <command> > /tmp/claude-$$-output.txt 2>&1

Step 2: Check size
  ls -lh /tmp/claude-$$-output.txt && wc -l

Step 3: Read with double limit
  head -100 /tmp/claude-$$-output.txt | head -c 5000

READING PATTERNS

Normal files:    head -100 file | head -c 5000
Logs:            tail -100 file | head -c 5000
Risky files:     head -c 3000 file
Search:          grep pattern file | head -c 5000
Base64:          head -c 500 file

SESSION ISOLATION

- Always use $$ in filenames
- /tmp/claude-$$-output.txt → /tmp/claude-12345-output.txt
```

---

> Full history: [../changelog/safe-terminal-output.changelog.md](../changelog/safe-terminal-output.changelog.md)
