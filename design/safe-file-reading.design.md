# Safe File Reading Guide

## 0) Document Control

> **Parent Scope:** Claude Code Rules System
> **Current Version:** 1.2
> **Session:** f19e8a67-d3c2-4c85-aa11-4db6949e61f8 (2026-02-21)

---

## 1. Overview

### 1.1 Purpose

Set standards for secure file reading to:

- Prevents terminal flooding from large output
- Make the session work smoothly
- Use the UOLF framework to cover all reading methods.
- Always plan before reading.

### 1.2 Problem Statement

| Issue | Impact | Solution |
|-------|--------|----------|
| Large file read | Terminal flood | Size check first |
| Long lines | 500KB+ on 1 line | Character limit |
| Minified files | Entire file = 1 line | head -c 3000 |
| Base64 content | Massive output | Character limit |

### 1.3 Solution

Create a UOLF (Universal Output Limit Framework) that:

1. Set clear output limits
2. Covers all reading methods (CLI, Tools, Languages)
3. Use Double Limit Pattern
4. Plan before reading (Evaluate → Plan → Read)

---

## 2. UOLF Framework

### 2.1 Output Limit Constants

| Constant | Value | Purpose |
|----------|-------|---------|
| MAX_OUTPUT_CHARS | 5000 | Hard limit in all cases |
| MAX_OUTPUT_LINES | 100 | Soft limit (if chars OK) |
| RISKY_FILE_CHARS | 3000 | .min.js, .html, .json, .svg |
| PREVIEW_CHARS | 2000 | Quick preview / unknown files |

### 2.2 Double Limit Pattern (Deterministic Default)

```bash
# ALWAYS enforce deterministic capped output (line + character)
<command> | head -100 | head -c 5000

# Character-first variant for risky/unknown long-line files
<command> | head -c 3000
```

**Why?** `head -100` alone is NOT safe - one line can contain 500KB+

---

## 3. Reading Methods

### 3.1 Claude Tools

| Tool | Safe Pattern | Notes |
|------|-------------|-------|
| **Read** | `limit: 200` | ~5000 chars, use offset for large files |
| **Grep** | `head_limit: 100` | Always review result size |
| **Glob** | No limit needed | Results are file paths only |

### 3.2 CLI Commands

| Command | ❌ Unsafe | ✅ Safe Pattern |
|---------|----------|----------------|
| head | `head -100` | `head -100 \| head -c 5000` |
| tail | `tail -100` | `tail -100 \| head -c 5000` |
| grep | `grep pattern` | `grep pattern \| head -c 5000` |
| cat | `cat file` | ❌ Do not use → `head -c 5000` instead |

### 3.3 Programming Languages

| Language | Safe Pattern |
|----------|-------------|
| Python | `content[:5000]` or `file.read(5000)` |
| Node.js | `content.substring(0, 5000)` |
| Bash | `${var:0:5000}` |

---

## 4. Decision Matrix

### 4.1 By File Size

| File Size | Lines | Recommended Method |
|-----------|-------|-------------------|
| < 50KB | > 100 | Read tool with limit (`limit: 200`) (replaces ambiguous full-read wording) |
| < 50KB | < 10 | `head -c 2000` first |
| 50-256KB | > 100 | Read tool with offset/limit |
| 50-256KB | < 10 | `head -c 2000` (likely minified) |
| > 256KB | Any | `head -c 2000` or `grep` |

### 4.2 By File Type

| File Pattern | Recommended Approach |
|--------------|---------------------|
| `*.min.js` | `head -c 2000` |
| `*.bundle.js` | `head -c 2000` |
| `*.min.css` | `head -c 2000` |
| `*.map` | Check size first |
| `*.json` (unknown) | `head -c 3000` |
| Base64 content | `head -c 500` |

---

## 5. Implementation Flow

### 5.1 Evaluate Before Read

```bash
# Evaluate: Size, lines, and characters
ls -lh <file> && wc -lwc <file>
```

### 5.2 Reading Flow

```
Evaluate file metrics
  ↓
Plan reading method (internal decision)
  ↓
Execute read with chosen method
```

### 5.3 Method Selection

| Situation | Method |
|-----------|--------|
| Small files (< 50KB, many lines) | Read tool with limit |
| Large files (> 256KB) | `head -c 3000` |
| Minified files (few lines, large) | `head -c 3000` |
| Searching specific content | `grep \| head -100 \| head -c 5000` |
| Log files | `tail -100 \| head -c 5000` |
| Unknown files | `head -c 2000` (preview first) |

---

## 6. Quality Metrics

| Metric | Target | Measurement |
|--------|--------|-------------|
| Output Limit | ≤ 5000 chars | Every read operation |
| Size Check | Default | Before reading large files |
| Character Limit | 100% | Always applied |
| Session Responsiveness | Maintained | No flooding |

---

## 7. Error Recovery

### 7.1 Read Tool Size Limit

```bash
# If Read tool reports "exceeds maximum size"
head -c 2000 <file>

# Or search for specific content
grep -n "search_term" <file> | head -100 | head -c 5000
```

---

## 8. Integration

### 8.1 Related Rules

| Rule | Relationship |
|------|-------------|
| safe-terminal-output | Command output limits |
| no-variable-guessing | Verify file exists first |

### 8.2 Synergy with safe-terminal-output

- safe-file-reading: Focus on reading files
- safe-terminal-output: Focus on command output
- Both use UOLF constants
- Both use Double Limit Pattern

---

## 9. Quick Reference

```text
UOLF - UNIVERSAL OUTPUT LIMIT FRAMEWORK

All reading methods → output ≤ 5000 chars

CONSTANTS
  MAX_OUTPUT_CHARS = 5000 (hard limit)
  MAX_OUTPUT_LINES = 100 (soft limit)
  RISKY_FILE_CHARS = 3000
  PREVIEW_CHARS = 2000

SAFE PATTERNS

CLI Commands:
  head -100 file | head -c 5000    # Double limit
  tail -100 file | head -c 5000    # Double limit
  grep pattern file | head -100 | head -c 5000 # Search + limit
  head -c 3000 file                # Risky files

Claude Tools:
  Read tool: limit: 200
  Grep tool: head_limit: 100

RISKY FILES (use head -c 3000)
  .min.js, .min.css, .bundle.js
  .html, .svg, .json (unknown)
  base64 content, dist/*, build/*
```

---

> Full history: [../changelog/safe-file-reading.changelog.md](../changelog/safe-file-reading.changelog.md)
