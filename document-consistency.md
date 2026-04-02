# Document Consistency and Cross-Reference Validation

> **Current Version:** 1.4
> **Design:** [design/document-consistency.design.md](design/document-consistency.design.md) v1.4
> **Session:** dd0bf4af-a66b-4b07-bb9d-a90a0e57b54e
> **Full history:** [changelog/document-consistency.changelog.md](changelog/document-consistency.changelog.md)

---

## Rule Statement

**Core Principle: Keep names, paths, identifiers, and cross-references consistent across the checked scope, while clearly separating portable shared references from checked local facts and machine-scoped examples.**

This rule governs cross-reference consistency, change-propagation discipline, and reference verification across files, sections, symbols, commands, and configuration values.

---

## Core Rules

### 1) Consistency Requirements
- keep names, paths, identifiers, and references consistent across the whole response
- when referencing, ensure it exists or mark it as unknown or unverified
- if a change impacts multiple sections/files, describe or update the dependencies
- keep portable shared references distinct from checked local facts or machine-scoped examples
- defer broader portable-default and anti-hardcoding ownership to `portable-implementation-and-hardcoding-control.md`

### 2) Reference Types

| Type | Example | Verification Method |
|------|---------|---------------------|
| File paths | `<workspace-root>/src/config.js` for portable examples, or exact path only when scoped as a checked local fact | Glob / LS / Read |
| Symbols | `getUserById` | Grep |
| Commands | `npm run build` | Test execution when needed |
| Config | `DATABASE_URL` | Read config source |

### 3) Shared Verification Trigger Model
Apply verification before finalizing references or consistency claims when triggers are present:

| Trigger | Typical Signal | Required Action |
|---------|----------------|-----------------|
| Concrete reference | file path, symbol, command, config key/value | verify existence/validity with tools before asserting |
| Cross-file consistency claim | "fully synchronized", "all references updated", "no drift" | verify all impacted files/sections before confirming |
| Rename/move/update impact | path or identifier changed in one place | trace and update dependent references deterministically |
| Ambiguous or unresolved reference | missing file/symbol or uncertain mapping | mark status explicitly and avoid unstated assumptions |

---

## Implementation

### Verification Flow
```text
Create reference
  ↓
Does it exist?
  → YES: use precise reference
  → NO: mark as unknown/unverified
  ↓
Is it consistent with related references?
  → YES: continue
  → NO: fix inconsistency
```

### Change Impact Analysis
```text
Making a change
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

## Output Standards

### Preferred references
- file paths: `<workspace-root>/src/config.js` for portable examples, or an exact path only when explicitly scoped as a checked local fact
- line numbers: `config.js:42`
- symbols: `getUserById()` function in `user.service.ts`

### Avoid
- "The config file"
- "That function we created earlier"
- "The variable somewhere in the code"

### Verification labels
```markdown
✅ Verified: `<workspace-root>/src/config.js` (portable example) or exact checked local path when scoped
⚠️ Unverified: `api.endpoint.url` (not checked)
❌ Not Found: `/missing/file.js`
```

---

## Cross-Section Validation

When modifying:
1. scan the entire document or checked scope for related references
2. identify all cross-section or cross-file dependencies
3. update affected sections deterministically
4. verify consistency throughout

| Change Type | Required Actions |
|-------------|------------------|
| Rename file | update all imports/references |
| Move file | update all paths |
| Rename symbol | update all usages |
| Change config | update all references |

---

## Quality Metrics

| Metric | Target |
|--------|--------|
| Naming consistency | 100% |
| Reference verification | High |
| Dependency updates | 100% |
| Reference precision | 100% |
| Portable-vs-local reference separation | High |

---

## Integration

Related rules:
- [no-variable-guessing.md](no-variable-guessing.md) - verify values, not just existence
- [zero-hallucination.md](zero-hallucination.md) - do not fabricate references
- [functional-intent-verification.md](functional-intent-verification.md) - verify intent of references when execution matters
- [portable-implementation-and-hardcoding-control.md](portable-implementation-and-hardcoding-control.md) - keep portable references distinct from local or machine-scoped values

---
