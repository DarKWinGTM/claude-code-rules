# 📖 Safe File Reading Guide (Plan-Before-Read)

## 🎯 Core Philosophy

**Reading is always allowed. Planning makes it efficient.**

This guide helps you plan file reading to ensure smooth, responsive sessions. The goal is efficient work - not blocking your progress.

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
| < 50KB | > 100 | Read tool (full file) |
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

### Read Tool (Best for normal files)
- Use for files < 256KB with many lines
- Supports offset/limit for partial reading
- Best for source code files

### head Command (Best for large/unknown files)
```bash
head -c 2000 <file>     # First 2000 bytes
head -100 <file>        # First 100 lines
head -c 4000 <file> | fold -w 80  # With line wrapping
```

### grep Command (Best for searching)
```bash
grep -n "pattern" <file> | head -20      # Search with line numbers
grep -n -C 3 "pattern" <file> | head -50 # With context
```

### tail Command (Best for logs)
```bash
tail -100 <file>        # Last 100 lines
tail -c 2000 <file>     # Last 2000 bytes
```

---

## ✅ Best Practices Summary

### Before Reading:
1. **Quick check** - `ls -lh && wc -l`
2. **Choose method** - Based on size/type
3. **Read efficiently** - Use appropriate tool

### Efficient Reading Tips:
- Small files (< 50KB, many lines) → Read tool
- Large files (> 256KB) → `head -c 2000`
- Minified files (few lines, large size) → `head -c 2000`
- Searching specific content → `grep` with `head`
- Log files → `tail` for recent entries

### Why Check Size?
- Ensures responsive session
- Helps choose optimal reading method
- Prevents unnecessary large reads
- Maintains smooth workflow

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
PLAN BEFORE READ

Step 1: Check size
  ls -lh <file> && wc -l <file>

Step 2: Choose method
  - Small file, many lines → Read tool
  - Large file → head -c 2000
  - Searching → grep | head

RECOMMENDED PRACTICES

- Check file size before reading
- Use Read tool for normal source files
- Use head -c for large/minified files
- Use grep for searching specific content
- Use tail for log files
```

---

## Version

| Version | Date | Notes |
|---------|------|-------|
| 3.0 | 2026-01-14 | Redesigned as Plan-Based Guide |
| | | Focus on guidance, not restriction |
