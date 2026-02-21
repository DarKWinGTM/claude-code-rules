# 📋 Safe Terminal Output Guide (Plan-Before-Execute)

> **Current Version:** 1.1
> **Design:** [design/safe-terminal-output.design.md](design/safe-terminal-output.design.md) v1.1

## 🎯 Core Philosophy

**Reading is always allowed. Planning makes it safe.**

This guide helps you plan output handling BEFORE executing commands to prevent terminal flooding. The goal is smooth, efficient work - not blocking your progress.

---

## 🔒 Output Limits (UOLF - Universal Output Limit Framework)

**All commands with output must be limited to no more than these values:**

| Constant | Value | Purpose |
|----------|-------|---------|
| MAX_OUTPUT_CHARS | 5000 | Hard limit in all cases |
| MAX_OUTPUT_LINES | 100 | Soft limit (if chars OK) |
| RISKY_FILE_CHARS | 3000 | .min.js, .html, .json, .svg |

**Universal Pattern:**
```bash
<command> | head -c 5000          # Character limit
<command> | head -100 | head -c 5000  # Double limit (lines + chars)
```

**Why?** `head -100` alone is NOT safe - one line can contain 500KB+ (base64, minified JS)

---

## 🔑 Session Isolation: Use `$$` (PID) for Unique Files

**CRITICAL:** Always use `$$` (shell PID) in output filenames to prevent multi-session collisions.

```bash
# ✅ CORRECT: Session-isolated files
/tmp/claude-$$-output.txt    # e.g., /tmp/claude-12345-output.txt

# ❌ WRONG: Shared files (can be overwritten by other sessions)
/tmp/claude-output.txt
```

**Why `$$`?**
- `$$` = Shell Process ID (unique per session)
- Prevents file collisions when multiple Claude sessions run simultaneously
- Each session gets its own isolated output files

---

## ⚠️ Heredoc & Multi-Language Patterns (CRITICAL)

`$$` expansion depends on **how the heredoc delimiter is quoted**:

### Heredoc Quoting Rules

| Pattern | `$$` Expansion | Example |
|---------|----------------|---------|
| `<<DELIM` (unquoted) | ✅ Expanded by bash | `python <<PY > /tmp/claude-$$-out.txt` |
| `<<'DELIM'` (single-quoted) | ❌ **NOT expanded** | `python <<'PY' > /tmp/claude-$$-out.txt` |
| `<<"DELIM"` (double-quoted) | ❌ **NOT expanded** | `python <<"PY" > /tmp/claude-$$-out.txt` |

### ✅ Correct Heredoc Patterns

```bash
# Option 1: Unquoted delimiter (allows $$ expansion)
python <<PY > /tmp/claude-$$-output.txt 2>&1
print("hello")
PY

# Option 2: Use bash variable before heredoc
OUTPUT_FILE="/tmp/claude-$$-output.txt"
python <<'PY' > "$OUTPUT_FILE" 2>&1
print("hello")
PY

# Option 3: Inline Python with -c flag
python3 -c "
import os
output_file = f'/tmp/claude-{os.getpid()}-output.txt'
# ... your code ...
" > /tmp/claude-$$-output.txt 2>&1
```

### ❌ Wrong Heredoc Patterns

```bash
# WRONG: Quoted delimiter prevents $$ expansion
python <<'PY' > /tmp/claude-$$-output.txt 2>&1
# $$ will be literal "$$" not the PID!
PY
```

### Multi-Language Session Isolation

| Language | Session-Isolated Pattern |
|----------|-------------------------|
| **Bash** | `/tmp/claude-$$-output.txt` |
| **Python** | `f'/tmp/claude-{os.getpid()}-output.txt'` |
| **Node.js** | `` `/tmp/claude-${process.pid}-output.txt` `` |
| **Ruby** | `"/tmp/claude-#{Process.pid}-output.txt"` |
| **Perl** | `"/tmp/claude-$$-output.txt"` (works in Perl) |

### 🎯 Best Practice: Use Read Tool When Possible

For **reading files**, prefer the **Read tool** over bash/heredoc:

```text
✅ PREFERRED: Use Read tool directly
   Read tool with offset/limit parameters

❌ AVOID: Complex heredoc for file reading
   python <<'PY' > /tmp/output.txt
   # reading file with Python...
   PY
```

**When to use each approach:**

| Task | Recommended Approach |
|------|---------------------|
| Read specific lines from file | **Read tool** with offset/limit |
| Search in files | **Grep tool** or Read tool |
| Transform/process data | Bash with `$$` or Python with `os.getpid()` |
| Run system commands | Bash with `$$` redirect |

---

## 🚨 Long Line Problem: Base64 & Minified Content

**CRITICAL:** `head -<lines>` alone is NOT safe!

### The Problem

```text
head -100 file.html
  ↓
Line 1: normal HTML (100 chars)
Line 2: <img src="data:image/png;base64,iVBORw0KGgo..." (500,000+ chars!)
  ↓
Terminal flooded despite "only 100 lines"
```

**Files at risk:**
- HTML with embedded base64 images
- Minified JS/CSS (entire file on 1 line)
- JSON with base64 data
- SVG with embedded images

### ✅ Solution: Double Limit Pattern

**Always use BOTH line AND character limits:**

```bash
# ✅ SAFE: Double limit (lines + characters)
head -100 file.html | head -c 5000

# ✅ SAFER: Character limit only (recommended for HTML/JSON)
head -c 3000 file.html

# ✅ SAFEST: For unknown files
head -c 2000 file.html
```

### Quick Decision

| File Type | Recommended Pattern |
|-----------|---------------------|
| `.html` with images | `head -c 3000` |
| `.min.js` / `.min.css` | `head -c 2000` |
| `.json` (unknown) | `head -c 3000` |
| `.svg` | `head -c 2000` |
| Normal source code | `head -100 \| head -c 5000` |

### Why This Matters

```text
❌ WRONG: head -100 file.html
   → 1 line with 500KB base64 = flood

✅ RIGHT: head -c 3000 file.html
   → Maximum 3000 characters = safe
```

---

## 💡 The Golden Rule: Evaluate → Plan → Execute

Before running any command, perform a quick **internal evaluation** to plan output handling:

### Standard Workflow (Internal Process)

```text
Step 1: Evaluate command output potential
  ↓
Step 2: Plan output destination (redirect to /tmp/claude-$$-*)
  ↓
Step 3: Execute command with redirect
  ↓
Step 4: Evaluate output file (size, lines, chars)
  ↓
Step 5: Read with appropriate method
```

### Evaluation Commands (Internal Use)

```bash
# After redirect, evaluate output file metrics:
ls -lh /tmp/claude-$$-output.txt && wc -lwc /tmp/claude-$$-output.txt
```

**Output provides:**
- File size (bytes/KB/MB)
- Line count
- Word count
- Character count

**Use this data internally to plan reading method** - no need to display all details to user unless relevant.

### Complete Pattern

```bash
# Execute with redirect (session-isolated)
<command> > /tmp/claude-$$-output.txt 2>&1

# Evaluate (internal planning)
ls -lh /tmp/claude-$$-output.txt && wc -lwc /tmp/claude-$$-output.txt

# Read based on evaluation
head -100 /tmp/claude-$$-output.txt | head -c 5000
```

---

## 📁 Standard Output Locations (Session-Isolated)

| Command Type | Recommended Output File |
|--------------|------------------------|
| General commands | `/tmp/claude-$$-output.txt` |
| Build output | `/tmp/claude-$$-build.log` |
| API responses | `/tmp/claude-$$-api.json` |
| Search results | `/tmp/claude-$$-search.txt` |
| Base64 encoding | `/tmp/claude-$$-base64.txt` |
| Log viewing | `/tmp/claude-$$-logs.txt` |

**Note:** `$$` expands to the shell's PID at runtime (e.g., `claude-12345-output.txt`)

---

## 🔄 Recommended Patterns

### Pattern 1: General Commands

```bash
# Plan: Redirect then read safely (session-isolated)
<command> > /tmp/claude-$$-output.txt 2>&1
ls -lh /tmp/claude-$$-output.txt && wc -l /tmp/claude-$$-output.txt
head -100 /tmp/claude-$$-output.txt | head -c 5000  # Double limit
```

### Pattern 2: Base64 Encoding

```bash
# Plan: Base64 can be very large
base64 image.png > /tmp/claude-$$-base64.txt 2>&1
ls -lh /tmp/claude-$$-base64.txt
head -c 500 /tmp/claude-$$-base64.txt  # Character limit only
```

### Pattern 3: API/Curl Responses

```bash
# Plan: API responses vary in size
curl -s https://api.example.com/data > /tmp/claude-$$-api.json 2>&1
ls -lh /tmp/claude-$$-api.json
head -c 3000 /tmp/claude-$$-api.json  # Character limit only
```

### Pattern 4: Find/Search Commands

```bash
# Plan: Search results can be extensive
find / -name "*.js" > /tmp/claude-$$-search.txt 2>&1
ls -lh /tmp/claude-$$-search.txt && wc -l /tmp/claude-$$-search.txt
head -50 /tmp/claude-$$-search.txt | head -c 5000  # Double limit
```

### Pattern 5: Build/Compile Output

```bash
# Plan: Build logs can be long
npm run build > /tmp/claude-$$-build.log 2>&1
ls -lh /tmp/claude-$$-build.log && wc -l /tmp/claude-$$-build.log
tail -100 /tmp/claude-$$-build.log | head -c 5000  # Double limit
```

### Pattern 6: Log Viewing

```bash
# Plan: Logs are often very large
docker logs container_name > /tmp/claude-$$-logs.txt 2>&1
ls -lh /tmp/claude-$$-logs.txt && wc -l /tmp/claude-$$-logs.txt
tail -100 /tmp/claude-$$-logs.txt | head -c 5000  # Double limit
```

### Pattern 7: Database Queries

```bash
# Plan: Query results can be massive
mysql -e "SELECT * FROM large_table" > /tmp/claude-$$-output.txt 2>&1
ls -lh /tmp/claude-$$-output.txt && wc -l /tmp/claude-$$-output.txt
head -50 /tmp/claude-$$-output.txt | head -c 5000  # Double limit
```

### Pattern 8: Directory Listings

```bash
# Plan: Recursive listings can be huge
ls -laR / > /tmp/claude-$$-output.txt 2>&1
ls -lh /tmp/claude-$$-output.txt && wc -l /tmp/claude-$$-output.txt
head -100 /tmp/claude-$$-output.txt | head -c 5000  # Double limit
```

---

## 📊 Safe Reading Decision Matrix

After redirecting output, choose your reading method based on file size:

| Output File Size | Lines | Recommended Read Method |
|------------------|-------|------------------------|
| < 10KB | > 50 | `head -100 \| head -c 5000` |
| < 10KB | < 10 | `head -c 2000` |
| 10-50KB | > 100 | `head -100 \| head -c 5000` |
| 10-50KB | < 10 | `head -c 2000` |
| > 50KB | Any | `head -100 \| head -c 5000` or `head -c 2000` |
| > 256KB | Any | `head -c 2000` |

---

## 🚨 High-Risk Commands (Plan Carefully)

| Command | Risk Level | Recommended Pattern |
|---------|------------|---------------------|
| `base64 <file>` | 🚨 High | `> /tmp/claude-$$-base64.txt 2>&1` |
| `curl <url>` | 🔴 Medium-High | `> /tmp/claude-$$-api.json 2>&1` |
| `find <path>` | 🔴 Medium-High | `> /tmp/claude-$$-search.txt 2>&1` |
| `grep -r <pattern>` | 🔴 Medium-High | `> /tmp/claude-$$-search.txt 2>&1` |
| `ls -laR` | 🔴 Medium-High | `> /tmp/claude-$$-output.txt 2>&1` |
| `docker logs` | 🔴 Medium-High | `> /tmp/claude-$$-logs.txt 2>&1` |
| `npm run build` | 🟡 Medium | `> /tmp/claude-$$-build.log 2>&1` |
| `git log` | 🟡 Medium | `> /tmp/claude-$$-output.txt 2>&1` |

---

## ✅ Best Practices Summary

### Universal Rule (UOLF):
**Every output → ≤ 5000 chars (use double limit)**

### When Executing Commands:
1. **Plan first** - Decide where output goes
2. **Redirect** - Send output to `/tmp/claude-$$-*.txt` (session-isolated)
3. **Check size** - `ls -lh && wc -l`
4. **Read safely** - Use double limit: `head -100 | head -c 5000`

### Recommended Reading Methods (with character limit):
- `head -100 <file> | head -c 5000` - Double limit (default)
- `tail -100 <file> | head -c 5000` - For logs
- `head -c 3000 <file>` - For risky files (.min.js, .json, .html)
- `grep -n "pattern" <file> | head -c 5000` - Search with limit

### Why Double Limit?
- `head -100` alone is NOT safe
- One line can contain 500KB+ (base64, minified JS)
- Character limit = guaranteed safe output

### Why Use `$$` (PID)?
- Prevents file collisions between concurrent sessions
- Each session gets isolated output files
- No risk of overwriting another session's data

---

## 🧹 Cleanup (Optional)

```bash
# Clean up current session's output files
rm -f /tmp/claude-$$-*.txt /tmp/claude-$$-*.log /tmp/claude-$$-*.json

# Clean up ALL claude output files (use with caution)
rm -f /tmp/claude-*-*.txt /tmp/claude-*-*.log /tmp/claude-*-*.json
```

---

## ⚡ Quick Reference

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

> Full history: [changelog/safe-terminal-output.changelog.md](changelog/safe-terminal-output.changelog.md)
