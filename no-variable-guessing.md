# 🔍 No Variable Guessing Policy

## Rule Statement

**Core Principle: Read Before Reference**

Never guess or assume values for variables, paths, configurations, or settings. Always verify from actual sources first.

---

## Core Requirements

### 1. File Paths & Variables

**Required Actions:**
- Use Read tool to check actual file contents before referencing
- Use LS/Glob to verify paths exist before using them
- Check .env, config files for actual variable values

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

### 2. Configuration Values

**Required Actions:**
- Read config files directly (package.json, .env, config.yaml, etc.)
- Don't assume default values without checking
- Verify environment-specific settings

**Common Files to Check:**
- `.env`, `.env.local`, `.env.production`
- `package.json`, `tsconfig.json`
- `config.yaml`, `config.json`
- Docker/Kubernetes configs

### 3. API Endpoints & Parameters

**Required Actions:**
- Search documentation before recommending
- Verify endpoint structure from official sources
- Check actual API responses when possible

---

## Flexibility Guidelines

### Acceptable Assumptions:
- Standard language defaults (Python indentation, JS semicolons)
- Common framework conventions (React component structure)
- Well-documented library behaviors
- User-provided information in conversation

### Requires Verification:
- Project-specific configurations
- Custom environment variables
- API keys and secrets (never guess, always ask)
- Database connection strings
- File paths specific to user's project

### User Override:
- User explicitly provides the value
- User says "assume X for now"
- User asks for a template/example (clearly labeled as such)

---

## Practical Examples

### ✅ Good Practice:
```
User: "Update the database connection"

Response: "Let me check your current database configuration..."
[Uses Read tool on .env or config file]
"I found your DB_HOST is set to localhost:5432.
Do you want to change it to...?"
```

### ✅ Acceptable When Uncertain:
```
User: "Set up a new API endpoint"

Response: "I'll create the endpoint. I noticed your other
endpoints use '/api/v1/' prefix based on routes/api.js.
Should I follow the same pattern?"
```

### ❌ Avoid:
```
User: "Connect to the database"

Response: "I'll use DATABASE_URL=postgres://localhost:5432/mydb"
(without checking actual .env file)
```

---

## Quick Reference

| Item Type | Action Required |
|-----------|-----------------|
| File paths | LS/Glob to verify existence |
| Environment variables | Read .env files |
| Config values | Read config files |
| API endpoints | Search docs or ask user |
| Credentials | Always ask user |
| Port numbers | Check config or ask |

---

## Exception Handling

### When File Not Found:
```
✅ "I couldn't find .env file. Could you tell me where
   your environment configuration is located?"
```

### When Multiple Possibilities:
```
✅ "I found both config.json and config.yaml.
   Which one should I use?"
```

### When User Provides Partial Info:
```
✅ "You mentioned the API is at /api/users.
   What's the base URL? (e.g., http://localhost:3000)"
```

---

## Quality Metrics

| Metric | Target |
|--------|--------|
| Path Verification | High for project-specific paths |
| Config Reading | Always before modification |
| Guessing Incidents | Minimize |

---

## Version

| Version | Date | Notes |
|---------|------|-------|
| 1.0 | 2026-01-15 | Initial version - flexible approach |
