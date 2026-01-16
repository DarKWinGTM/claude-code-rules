# Document Consistency Rule

## Rule Design Document

---

## Changelog

| Date | Change |
|------|--------|
| 2026-01-16 | สร้าง design document สำหรับ Document Consistency Rule |
| 2026-01-15 | Initial version from Principle IV |

---

## 1. Overview

### 1.1 Purpose

กำหนดมาตรฐานความสอดคล้องของเอกสาร เพื่อ:

- รักษา consistency ของ names, paths, identifiers
- ให้ cross-references ถูกต้องและ verifiable
- update references เมื่อมีการเปลี่ยนแปลง
- ใช้ precise references แทน vague descriptions

### 1.2 Problem Statement

| Issue | Impact | Solution |
|-------|--------|----------|
| Inconsistent naming | สับสน, หาไม่เจอ | Maintain consistency |
| Broken references | Links ไม่ทำงาน | Verify existence |
| Stale references | ข้อมูลล้าสมัย | Update all affected |
| Vague descriptions | ไม่รู้ว่าอ้างถึงอะไร | Use precise refs |

### 1.3 Solution

สร้าง Consistency Framework ที่:

1. ตรวจสอบ naming consistency
2. verify references ก่อนใช้
3. update dependencies เมื่อเปลี่ยน
4. ใช้ precise references เสมอ

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

## 8. Version

| Version | Date | Notes |
|---------|------|-------|
| 1.0 | 2026-01-15 | Initial version |
| 1.1 | 2026-01-16 | Added design document |
