# Document Consistency and Cross-Reference Validation

> **Current Version:** 1.6
> **Design:** [design/document-consistency.design.md](design/document-consistency.design.md) v1.6
> **Session:** 11c4bd2f-216e-4779-81bf-26d34a4fcaeb
> **Full history:** [changelog/document-consistency.changelog.md](changelog/document-consistency.changelog.md)

---

## Rule Statement

**Core Principle: Keep names, paths, identifiers, and cross-references consistent across the checked scope, while clearly separating portable shared references, source-side references, destination/runtime references, checked local facts, and machine-scoped examples.**

This rule governs cross-reference consistency, change-propagation discipline, and reference verification across files, sections, symbols, commands, and configuration values.

---

## Core Rules

### 1) Consistency Requirements
- keep names, paths, identifiers, and references consistent across the whole response
- when referencing, ensure it exists or mark it as unknown or unverified
- if a change impacts multiple sections/files, describe or update the dependencies
- keep portable shared references distinct from checked local facts or machine-scoped examples
- keep source-side references distinct from destination/runtime references when both appear in install or onboarding guidance
- keep local execution paths used only for tool/runtime operation distinct from reusable source-artifact references so tool-local paths do not silently become skill/plugin/source contracts
- defer broader portable-default and anti-hardcoding ownership to `portable-implementation-and-hardcoding-control.md`

### 2) Reference Types

| Type | Example | Verification Method |
|------|---------|---------------------|
| File paths | `<workspace-root>/src/config.js` for portable examples, or exact path only when scoped as a checked local fact | Glob / LS / Read |
| Source-side install path | `<repo-root>` or `./` when a command is run from the repo root | Read / command-context verification |
| Destination/runtime path | `<install-root>/skills` or `<user-runtime-rules>` | Read config/source contract when applicable |
| Local execution path | exact tool/runtime path used only for the current machine or harness turn | Read / execution context |
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
| Mixed source/destination wording | install docs blur clone/source path with installed/runtime path | separate the reference roles explicitly and normalize wording |
| Tool-path leakage into reusable source | a local tool/runtime path is copied into skill/plugin/source content as if it were a shared contract | relabel it as local execution context or replace it with a portable placeholder / runtime variable |

---

## Implementation

### Verification Flow
```text
Create reference
  ↓
Does it exist or resolve?
  → YES: use precise reference
  → NO: mark as unknown/unverified
  ↓
What reference role is it?
  → portable shared reference
  → source-side reference
  → destination/runtime reference
  → checked local fact
  → machine-scoped example
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
- source-side install guidance: `<repo-root>` or `./` when the command is explicitly intended for the repo root
- destination/runtime guidance: `<install-root>`, `<user-runtime-rules>`, `<user-runtime-skills>`, `<user-runtime-agents>`
- line numbers: `config.js:42`
- symbols: `getUserById()` function in `user.service.ts`

### Avoid
- "The config file"
- "That function we created earlier"
- "The variable somewhere in the code"
- one exact workstation path acting as both the source path and the destination/runtime path without explanation

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
| Normalize install docs | update source-side references and destination/runtime references separately |

---

## Quality Metrics

| Metric | Target |
|--------|--------|
| Naming consistency | 100% |
| Reference verification | High |
| Dependency updates | 100% |
| Reference precision | 100% |
| Portable-vs-local reference separation | High |
| Source-vs-destination reference separation | High |

---

## Integration

Related rules:
- [no-variable-guessing.md](no-variable-guessing.md) - verify values, not just existence
- [zero-hallucination.md](zero-hallucination.md) - do not fabricate references
- [functional-intent-verification.md](functional-intent-verification.md) - verify intent of references when execution matters
- [portable-implementation-and-hardcoding-control.md](portable-implementation-and-hardcoding-control.md) - keep portable references distinct from local or machine-scoped values and keep source-side versus destination/runtime notation legible

---
