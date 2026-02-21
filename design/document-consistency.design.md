# Document Consistency Rule

## 0) Document Control

> **Parent Scope:** Claude Code Rules System
> **Current Version:** 1.0
> **Session:** a77b77ae-ef2a-49f6-93d9-f78c8ac2d2f7 (2026-02-01)

---

## 1. Overview

### 1.1 Purpose

Set document consistency standards to:

- Maintain consistency of names, paths, identifiers
- Make cross-references accurate and verifiable
- update references when changes are made
- Use precise references instead of vague descriptions.

### 1.2 Problem Statement

| Issue | Impact | Solution |
|-------|--------|----------|
| Inconsistent naming | Confused, can't find | Maintain consistency |
| Broken references | Links not working | Verify existence |
| Stale references | Outdated information | Update all affected |
| Vague descriptions | Don't know what this is referring to | Use precise refs |

### 1.3 Solution

Create a Consistency Framework that:

1. Check naming consistency
2. verify references before use
3. update dependencies when changing
4. Always use precise references.

---

## 2. Core Rules

### 2.1 Consistency Requirements

- Keep names, paths, identifiers consistent across the whole response
- When referencing, ensure it exists or mark as unknown/unverified
- If change impacts multiple sections/files, describe dependencies

### 2.2 Reference Types

| Type | Example | Verification Method |
|------|---------|---------------------|
| File paths | `/src/config.js` | Glob/LS |
| Symbols | `getUserById` | Grep |
| Commands | `npm run build` | Test execution |
| Config | `DATABASE_URL` | Read .env |

---

## 3. Implementation

### 3.1 Verification Flow

```
Create Reference
  ↓
Does it exist?
  → YES: Use precise reference
  → NO: Mark as unknown/unverified
  ↓
Is it consistent with other references?
  → YES: Continue
  → NO: Fix inconsistency
```

### 3.2 Change Impact Analysis

```
Making a Change
  ↓
Identify all affected references
  ↓
List dependencies
  ↓
Update all references
  ↓
Verify consistency
```

---

## 4. Output Standards

### 4.1 Precise References

**Preferred:**
- File paths: `/home/user/project/src/config.js`
- Line numbers: `config.js:42`
- Symbols: `getUserById()` function in `user.service.ts`

**Avoid:**
- "The config file"
- "That function we created earlier"
- "The variable somewhere in the code"

### 4.2 Verification Labels

```markdown
✅ Verified: `/src/config.js` (exists)
⚠️ Unverified: `api.endpoint.url` (not checked)
❌ Not Found: `/missing/file.js`
```

---

## 5. Quality Metrics

| Metric | Target | Measurement |
|--------|--------|-------------|
| Naming Consistency | 100% | Same thing = same name |
| Reference Verification | High | Check before referencing |
| Dependency Updates | 100% | All affected updated |
| Reference Precision | 100% | Specific, not vague |

---

## 6. Cross-Section Validation

### 6.1 Document Scanning

When modifying:
1. Scan entire document for related references
2. Identify all cross-section dependencies
3. Update affected sections
4. Verify consistency throughout

### 6.2 Change Propagation

| Change Type | Required Actions |
|-------------|------------------|
| Rename file | Update all imports/references |
| Move file | Update all paths |
| Rename symbol | Update all usages |
| Change config | Update all references |

---

## 7. Integration

### 7.1 Related Rules

| Rule | Relationship |
|------|-------------|
| no-variable-guessing | Verify values, not just existence |
| zero-hallucination | Don't fabricate references |
| functional-intent-verification | Verify intent of references |

### 7.2 Tool Usage

- **Glob**: Find file references
- **Grep**: Find symbol references
- **Read**: Verify content references

---

> Full history: [../changelog/document-consistency.changelog.md](../changelog/document-consistency.changelog.md)
