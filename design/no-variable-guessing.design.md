# No Variable Guessing Policy

## 0) Document Control

> **Parent Scope:** Claude Code Rules System
> **Current Version:** 1.0
> **Session:** a77b77ae-ef2a-49f6-93d9-f78c8ac2d2f7 (2026-02-01)

---

## 1. Overview

### 1.1 Purpose

กำหนดนโยบายห้ามเดาค่าตัวแปร เพื่อ:

- ให้ใช้ค่าจริงจาก actual sources เสมอ
- ป้องกันการเดา paths, configs, variables
- verify ก่อน reference
- ถาม user เมื่อหาไม่เจอ

### 1.2 Problem Statement

| Issue | Impact | Solution |
|-------|--------|----------|
| Guessed paths | File not found errors | Verify with LS/Glob |
| Assumed config | Wrong configuration | Read config files |
| Made-up values | Code doesn't work | Ask user |
| Default assumptions | Environment mismatch | Check actual values |

### 1.3 Solution

สร้าง Verification Framework ที่:

1. verify ทุก path ก่อน reference
2. read config files ก่อนใช้ค่า
3. ถาม user เมื่อไม่แน่ใจ
4. อนุญาต standard conventions เท่านั้น

---

## 2. Verification Requirements

### 2.1 File Paths & Variables

**Required Actions:**
- Use Read tool to check actual file contents
- Use LS/Glob to verify paths exist
- Check .env, config files for actual values

**Verification Flow:**
```
Need to reference a path/variable?
  ↓
Use Read/LS/Glob to verify
  ↓
Found? → Use actual value
  ↓
Not found? → Ask user
```

### 2.2 Configuration Values

**Required Actions:**
- Read config files directly
- Don't assume default values
- Verify environment-specific settings

**Common Files to Check:**
- `.env`, `.env.local`, `.env.production`
- `package.json`, `tsconfig.json`
- `config.yaml`, `config.json`
- Docker/Kubernetes configs

### 2.3 API Endpoints & Parameters

**Required Actions:**
- Search documentation before recommending
- Verify endpoint structure from official sources
- Check actual API responses when possible

---

## 3. Flexibility Guidelines

### 3.1 Acceptable Assumptions

| Type | Example | Reason |
|------|---------|--------|
| Language defaults | Python indentation | Standard |
| Framework conventions | React component structure | Documented |
| Library behaviors | Well-documented APIs | Official docs |
| User-provided | Values in conversation | User said it |

### 3.2 Requires Verification

| Type | Example | Action |
|------|---------|--------|
| Project configs | Custom .env values | Read file |
| Environment vars | DATABASE_URL | Check .env |
| API keys/secrets | Never guess | Always ask |
| DB connections | Connection strings | Verify config |
| File paths | Project-specific | LS/Glob |

### 3.3 User Override

- User explicitly provides the value
- User says "assume X for now"
- User asks for template/example (labeled as such)

---

## 4. Quick Reference

| Item Type | Action Required |
|-----------|-----------------|
| File paths | LS/Glob to verify existence |
| Environment variables | Read .env files |
| Config values | Read config files |
| API endpoints | Search docs or ask user |
| Credentials | Always ask user |
| Port numbers | Check config or ask |

---

## 5. Exception Handling

### 5.1 File Not Found

```markdown
I couldn't find .env file. Could you tell me where
your environment configuration is located?
```

### 5.2 Multiple Possibilities

```markdown
I found both config.json and config.yaml.
Which one should I use?
```

### 5.3 Partial Information

```markdown
You mentioned the API is at /api/users.
What's the base URL? (e.g., http://localhost:3000)
```

---

## 6. Quality Metrics

| Metric | Target | Measurement |
|--------|--------|-------------|
| Path Verification | High | For project-specific paths |
| Config Reading | 100% | Before modification |
| Guessing Incidents | Minimize | Avoid assumptions |

---

## 7. Tool Usage

### 7.1 Verification Tools

| Tool | Use For |
|------|---------|
| Read | Check file contents |
| Glob | Find files by pattern |
| LS (Bash) | Check directory contents |
| Grep | Search for values |
| WebFetch | Verify API endpoints |

### 7.2 Verification Flow

```
Before Using Value
  ↓
Is it user-provided? → Use it
  ↓
Is it standard convention? → Use it
  ↓
Can I verify with tools? → Verify
  ↓
Can't verify? → Ask user
```

---

## 8. Integration

### 8.1 Related Rules

| Rule | Relationship |
|------|-------------|
| zero-hallucination | Don't make up values |
| document-consistency | Use verified references |
| anti-mockup | Use real values |

### 8.2 Combined Verification

```
Verify exists (Glob/LS)
  +
Verify content (Read)
  +
Verify format (check syntax)
  =
Fully verified value
```

---

> Full history: [../changelog/no-variable-guessing.changelog.md](../changelog/no-variable-guessing.changelog.md)
