# Document Consistency Rule

## 0) Document Control

> **Parent Scope:** Claude Code Rules System
> **Current Version:** 1.5
> **Session:** dd0bf4af-a66b-4b07-bb9d-a90a0e57b54e (2026-04-02)

---

## 1. Overview

### 1.1 Purpose

Set document consistency standards to:

- maintain consistency of names, paths, identifiers
- make cross-references accurate and verifiable
- update references when changes are made
- use precise references instead of vague descriptions
- keep source-side references distinct from destination/runtime references in onboarding/install docs

### 1.2 Problem Statement

| Issue | Impact | Solution |
|-------|--------|----------|
| Inconsistent naming | Confused, can't find | Maintain consistency |
| Broken references | Links not working | Verify existence |
| Stale references | Outdated information | Update all affected |
| Vague descriptions | Don't know what this is referring to | Use precise refs |
| Source/destination blur | Readers cannot tell where an artifact comes from versus where it installs/runs | Separate reference roles explicitly |

### 1.3 Solution

Create a Consistency Framework that:

1. checks naming consistency
2. verifies references before use
3. updates dependencies when changing
4. always uses precise references
5. keeps portable shared references, source-side references, destination/runtime references, and checked local facts semantically distinct

---

## 2. Core Rules

### 2.1 Consistency Requirements

- Keep names, paths, identifiers consistent across the whole response
- When referencing, ensure it exists or mark as unknown/unverified
- If change impacts multiple sections/files, describe dependencies
- Keep portable shared references distinct from checked local facts or machine-scoped examples
- Keep source-side references distinct from destination/runtime references when both appear in onboarding/install docs
- Defer broader portable-default and anti-hardcoding ownership to `portable-implementation-and-hardcoding-control.md`

### 2.2 Reference Types

| Type | Example | Verification Method |
|------|---------|---------------------|
| File paths | `<workspace-root>/src/config.js` for portable examples, or exact checked local path when scoped | Glob / Read |
| Source-side install path | `<repo-root>` or `./` when the command is run from the repo root | Read / command-context verification |
| Destination/runtime path | `<install-root>`, `<user-runtime-rules>` | Read config/source contract when applicable |
| Symbols | `getUserById` | Grep |
| Commands | `npm run build` | Test execution |
| Config | `DATABASE_URL` | Read config source |

### 2.3 Shared Verification Trigger Model (WS-5)

Apply verification before finalizing references or consistency claims when triggers are present:

| Trigger | Typical Signal | Required Action |
|---------|----------------|-----------------|
| Concrete reference | file path, symbol, command, config key/value | verify existence/validity with tools before asserting |
| Cross-file consistency claim | "fully synchronized", "all references updated", "no drift" | verify all impacted files/sections before confirming |
| Rename/move/update impact | path or identifier changed in one place | trace and update dependent references deterministically |
| Ambiguous or unresolved reference | missing file/symbol or uncertain mapping | mark status explicitly and avoid unstated assumptions |
| Mixed source/destination wording | install docs blur clone/source path with installed/runtime path | separate the reference roles explicitly and normalize wording |

---

## 3. Implementation

### 3.1 Verification Flow

```text
Create Reference
  ↓
Does it exist or resolve?
  → YES: Use precise reference
  → NO: Mark as unknown/unverified
  ↓
What reference role is it?
  → portable shared reference
  → source-side reference
  → destination/runtime reference
  → checked local fact
  → machine-scoped example
  ↓
Is it consistent with other references?
  → YES: Continue
  → NO: Fix inconsistency
```

### 3.2 Change Impact Analysis

```text
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
- File paths: `<workspace-root>/src/config.js` for portable examples, or an exact path only when explicitly scoped as a checked local fact
- Source-side install guidance: `<repo-root>` or `./` when the command is explicitly intended for the repo root
- Destination/runtime guidance: `<install-root>`, `<user-runtime-rules>`, `<user-runtime-skills>`, `<user-runtime-agents>`
- Line numbers: `config.js:42`
- Symbols: `getUserById()` function in `user.service.ts`

**Avoid:**
- "The config file"
- "That function we created earlier"
- "The variable somewhere in the code"
- one exact workstation path acting as both source path and destination/runtime path without explanation

### 4.2 Verification Labels

```markdown
✅ Verified: `<workspace-root>/src/config.js` (portable example) or exact checked local path when scoped
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
| Portable-vs-local separation | High | Reference role stays explicit |
| Source-vs-destination separation | High | Install-doc roles stay explicit |

---

## 6. Cross-Section Validation

### 6.1 Document Scanning

When modifying:
1. scan entire document for related references
2. identify all cross-section dependencies
3. update affected sections
4. verify consistency throughout

### 6.2 Change Propagation

| Change Type | Required Actions |
|-------------|------------------|
| Rename file | Update all imports/references |
| Move file | Update all paths |
| Rename symbol | Update all usages |
| Change config | Update all references |
| Normalize install docs | Update source-side references and destination/runtime references separately |

---

## 7. Integration

### 7.1 Related Rules

| Rule | Relationship |
|------|-------------|
| no-variable-guessing | Verify values, not just existence |
| zero-hallucination | Don't fabricate references |
| functional-intent-verification | Verify intent of references |
| portable-implementation-and-hardcoding-control | Owns broader anti-hardcoding semantics and source-side versus destination/runtime notation discipline |

### 7.2 Tool Usage

- **Glob**: Find file references
- **Grep**: Find symbol references
- **Read**: Verify content references

---

> Full history: [../changelog/document-consistency.changelog.md](../changelog/document-consistency.changelog.md)
