# 📖 Safe File Reading Guide (Plan-Before-Read)

> **Current Version:** 1.1
> **Design:** [design/safe-file-reading.design.md](design/safe-file-reading.design.md) v1.1

## 🎯 Core Philosophy

**Reading is always allowed. Planning makes it efficient.**

This guide helps you plan file reading to ensure smooth, responsive sessions. The goal is efficient work - not blocking your progress.

---

## 🔒 Output Limits (Universal)

**Whatever method is used to read, the output must not exceed these values:**

| Constant | Value | Purpose |
|----------|-------|---------|
| MAX_OUTPUT_CHARS | 5000 | Hard limit in all cases |
| MAX_OUTPUT_LINES | 100 | Soft limit (if chars OK) |
| RISKY_FILE_CHARS | 3000 | .min.js, .html, .json, .svg |
| PREVIEW_CHARS | 2000 | Quick preview / unknown files |

**Applies to:** CLI commands, Read tool, Grep tool, Redirect patterns, Programming languages

**Why?** `head -100` alone is NOT safe - one line can contain 500KB+ (base64, minified JS)

---

## 💡 The Golden Rule: Evaluate Before Read

Before reading any file, perform a quick **internal evaluation** to plan the best reading approach:

### Standard Evaluation (Internal Process)

```bash
# Evaluate: Size, lines, and characters
ls -lh <file> && wc -lwc <file>
```

**Output provides:**
- File size (bytes/KB/MB)
- Line count
- Word count
- Character count

**Use this data internally to plan** - no need to display all details to user unless relevant.

### Evaluation → Planning Flow

```text
Evaluate file metrics
  ↓
Plan reading method (internal decision)
  ↓
Execute read with chosen method
```

---

## 📊 Reading Method Decision Matrix

Based on file size, choose the most efficient reading approach:

| File Size | Lines | Recommended Method |
|-----------|-------|-------------------|
| < 50KB | > 100 | Read tool with limit (`limit: 200`) |
| < 50KB | < 10 | `head -c 2000` first (may be minified) |
| 50-256KB | > 100 | Read tool with offset/limit |
| 50-256KB | < 10 | `head -c 2000` (likely minified) |
| > 256KB | Any | `head -c 2000` or `grep` for specific content |

---

## 🔄 Recommended Patterns

### Pattern 1: Standard File Reading

```bash
# Step 1: Quick size check
ls -lh /path/to/file.js && wc -l /path/to/file.js

# Step 2: Choose method based on results
# If safe size: Use Read tool
# If large: Use head -c 2000
```

### Pattern 2: Large File Reading

```bash
# For files > 100KB
head -c 2000 large-file.js

# For readable output with line wrapping
head -c 4000 large-file.js | fold -w 80
```

### Pattern 3: Searching in Large Files

```bash
# Use grep instead of reading entire file
grep -n "function_name" large-file.js | head -30

# With context lines
grep -n -C 3 "pattern" large-file.js | head -50
```

### Pattern 4: node_modules Exploration

```bash
# Check size first
ls -lh /path/to/node_modules/package/index.js

# Use grep for searching exports/functions
grep -n "export\|function\|class" /path/to/file.js | head -30
```

---

## 🚨 File Types to Check Carefully

| File Pattern | Typical Size | Recommended Approach |
|--------------|--------------|---------------------|
| `*.min.js` | Often large | `head -c 2000` |
| `*.bundle.js` | Often large | `head -c 2000` |
| `*.min.css` | Often large | `head -c 2000` |
| `*.map` | Often large | Check size first |
| `*.json` (unknown) | Varies | Check size first |
| Base64 content | Often large | `head -c 500` |
| `dist/*` | Often large | Check size first |
| `build/*` | Often large | Check size first |

---

## 📋 Reading Methods Reference

### Universal Pattern (Apply to ALL methods)

```bash
# ALWAYS add character limit to prevent flooding
<any-command> | head -c 5000
```

### Claude Tools (Built-in limits)

| Tool | Safe Pattern | Notes |
|------|-------------|-------|
| **Read** | `limit: 200` | ~5000 chars, use offset for large files |
| **Grep** | `head_limit: 100` | Always review result size |
| **Glob** | No limit needed | Results are file paths only |

### CLI Commands (Must add character limit)

| Command | ❌ Unsafe | ✅ Safe Pattern |
|---------|----------|----------------|
| head | `head -100` | `head -100 \| head -c 5000` |
| tail | `tail -100` | `tail -100 \| head -c 5000` |
| grep | `grep pattern` | `grep pattern \| head -c 5000` |
| cat | `cat file` | ❌ Do not use → `head -c 5000` instead |
| less/more | interactive | ❌ Do not use → `head -c 5000` instead |

### Risky Files (Use character-first)

```bash
# For .min.js, .html, .json, .svg, base64 content
head -c 3000 <file>     # Character limit FIRST

# NOT: head -100 <file>  ← One line can be 500KB!
```

### Redirect Pattern (Unknown output)

```bash
# Step 1: Redirect to file
<command> > /tmp/claude-$$-output.txt 2>&1

# Step 2: Check size
wc -c /tmp/claude-$$-output.txt

# Step 3: Safe read with character limit
head -c 5000 /tmp/claude-$$-output.txt
```

### Programming Languages

| Language | Safe Pattern |
|----------|-------------|
| Python | `content[:5000]` or `file.read(5000)` |
| Node.js | `content.substring(0, 5000)` |
| Bash | `${var:0:5000}` |

---

## ✅ Best Practices Summary

### Universal Rule:
**All methods read → output ≤ 5000 chars**

### Before Reading:
1. **Quick check** - `ls -lh && wc -l`
2. **Choose method** - Based on size/type
3. **Add character limit** - `| head -c 5000` or Read tool limit
4. **Read efficiently** - Use appropriate tool

### Method Selection:
- **Small files** (< 50KB, many lines) → Read tool with limit
- **Large files** (> 256KB) → `head -c 3000`
- **Minified files** (few lines, large size) → `head -c 3000`
- **Searching specific content** → `grep | head -c 5000`
- **Log files** → `tail -100 | head -c 5000`
- **Unknown files** → `head -c 2000` (preview first)

### Why Character Limits?
- `head -100` can still output 500KB+ if lines are long
- Minified JS/CSS = entire file on 1 line
- Base64 images = massive single line
- Character limit = guaranteed safe output

---

## 🔄 Error Recovery

### If Read tool reports "exceeds maximum size":

```bash
# Use head for large files
head -c 2000 <file>

# Or search for specific content
grep -n "search_term" <file> | head -20
```

---

## ⚡ Quick Reference

```text
UNIVERSAL OUTPUT LIMIT (UOLF)

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
  grep pattern file | head -c 5000 # Search + limit
  head -c 3000 file                # Risky files

Claude Tools:
  Read tool: limit: 200
  Grep tool: head_limit: 100

Redirect:
  cmd > /tmp/file && head -c 5000 /tmp/file

RISKY FILES (use head -c 3000)
  .min.js, .min.css, .bundle.js
  .html, .svg, .json (unknown)
  base64 content, dist/*, build/*
```

---

> Full history: [changelog/safe-file-reading.changelog.md](changelog/safe-file-reading.changelog.md)
