# 📋 Safe Terminal Output Guide (Plan-Before-Execute)

## 🎯 Core Philosophy

**Reading is always allowed. Planning makes it safe.**

This guide helps you plan output handling BEFORE executing commands to prevent terminal flooding. The goal is smooth, efficient work - not blocking your progress.

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
head -100 /tmp/claude-$$-output.txt
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
head -100 /tmp/claude-$$-output.txt
```

### Pattern 2: Base64 Encoding

```bash
# Plan: Base64 can be very large
base64 image.png > /tmp/claude-$$-base64.txt 2>&1
ls -lh /tmp/claude-$$-base64.txt
head -c 500 /tmp/claude-$$-base64.txt
```

### Pattern 3: API/Curl Responses

```bash
# Plan: API responses vary in size
curl -s https://api.example.com/data > /tmp/claude-$$-api.json 2>&1
ls -lh /tmp/claude-$$-api.json
head -c 3000 /tmp/claude-$$-api.json
```

### Pattern 4: Find/Search Commands

```bash
# Plan: Search results can be extensive
find / -name "*.js" > /tmp/claude-$$-search.txt 2>&1
ls -lh /tmp/claude-$$-search.txt && wc -l /tmp/claude-$$-search.txt
head -50 /tmp/claude-$$-search.txt
```

### Pattern 5: Build/Compile Output

```bash
# Plan: Build logs can be long
npm run build > /tmp/claude-$$-build.log 2>&1
ls -lh /tmp/claude-$$-build.log && wc -l /tmp/claude-$$-build.log
tail -100 /tmp/claude-$$-build.log  # Usually want to see end for errors
```

### Pattern 6: Log Viewing

```bash
# Plan: Logs are often very large
docker logs container_name > /tmp/claude-$$-logs.txt 2>&1
ls -lh /tmp/claude-$$-logs.txt && wc -l /tmp/claude-$$-logs.txt
tail -100 /tmp/claude-$$-logs.txt
```

### Pattern 7: Database Queries

```bash
# Plan: Query results can be massive
mysql -e "SELECT * FROM large_table" > /tmp/claude-$$-output.txt 2>&1
ls -lh /tmp/claude-$$-output.txt && wc -l /tmp/claude-$$-output.txt
head -50 /tmp/claude-$$-output.txt
```

### Pattern 8: Directory Listings

```bash
# Plan: Recursive listings can be huge
ls -laR / > /tmp/claude-$$-output.txt 2>&1
ls -lh /tmp/claude-$$-output.txt && wc -l /tmp/claude-$$-output.txt
head -100 /tmp/claude-$$-output.txt
```

---

## 📊 Safe Reading Decision Matrix

After redirecting output, choose your reading method based on file size:

| Output File Size | Lines | Recommended Read Method |
|------------------|-------|------------------------|
| < 10KB | > 50 | `head -100` or `cat` |
| < 10KB | < 10 | `head -c 2000` |
| 10-50KB | > 100 | `head -100` |
| 10-50KB | < 10 | `head -c 2000` |
| > 50KB | Any | `head -100` or `head -c 2000` |
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

### When Executing Commands:
1. **Plan first** - Decide where output goes
2. **Redirect** - Send output to `/tmp/claude-$$-*.txt` (session-isolated)
3. **Check size** - `ls -lh && wc -l`
4. **Read safely** - Use `head` with appropriate limits

### Recommended Reading Methods:
- `head -100 <file>` - First 100 lines
- `head -c 2000 <file>` - First 2000 bytes
- `tail -100 <file>` - Last 100 lines (good for logs)
- `grep -n "pattern" <file> | head -20` - Search with context

### Why Plan Output?
- Prevents terminal flooding
- Keeps session responsive
- Allows controlled inspection of large outputs
- Maintains smooth workflow

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
PLAN BEFORE EXECUTE (Session-Isolated)

Step 1: Redirect (with $$ for unique files)
  <command> > /tmp/claude-$$-output.txt 2>&1

Step 2: Check size
  ls -lh /tmp/claude-$$-output.txt && wc -l /tmp/claude-$$-output.txt

Step 3: Read safely
  head -100 /tmp/claude-$$-output.txt
  # OR
  head -c 2000 /tmp/claude-$$-output.txt

RECOMMENDED PRACTICES

- Always use $$ in filenames for session isolation
- Plan output destination before executing
- Redirect to /tmp/claude-$$-*.txt
- Check size before reading
- Use head/tail with limits for large files
```

---

## Version

| Version | Date | Notes |
|---------|------|-------|
| 3.1 | 2026-01-15 | Added session isolation with `$$` (PID) |
| 3.0 | 2026-01-14 | Redesigned as Plan-Based Guide |
| | | Focus on guidance, not restriction |
