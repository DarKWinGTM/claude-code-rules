# Document Consistency and Cross-Reference Validation
> **Current Version:** 1.8
> **Design:** [design/document-consistency.design.md](design/document-consistency.design.md) v1.8
> **Session:** d42465eb-30a7-4bc8-b9d6-03e52306e9a5
> **Full history:** [changelog/document-consistency.changelog.md](changelog/document-consistency.changelog.md)
---
## Rule Statement
**Core Principle: Keep names, paths, identifiers, and cross-references consistent across checked scope while separating portable shared references, source-side references, source-owned active runtime files, shared runtime destinations, other-owner runtime files, checked local facts, and machine-scoped examples.**
This rule owns cross-reference consistency, change propagation, and reference verification across files, sections, symbols, commands, and config values.
---
## Core Contract
### Consistency requirements
Required guidance:
- keep names, paths, identifiers, and references consistent across the response or checked artifact set
- verify concrete references or mark them unknown/unverified, and verify impacted files/sections before sync/no-drift claims
- update or describe dependencies when a change impacts multiple files/sections
- separate portable shared references, checked local facts, machine-scoped examples, source-side install paths, destination/runtime paths, source-owned active runtime install scope, shared runtime destinations, other-owner runtime files, and local execution paths
- keep other-owner runtime files outside the current project's parity/install target set unless owner/project scope is explicitly selected or verified
- defer broader portability and anti-hardcoding to `portable-implementation-and-hardcoding-control.md`
### Reference roles and checks
| Type | Preferred form | Check |
|---|---|---|
| File/source path | `<workspace-root>/src/config.js`, `<repo-root>`, or repo-root `./`; exact path only as scoped local fact | Glob / Read / command context |
| Destination/runtime path | `<install-root>/skills`, `<user-runtime-rules>` | config/source contract check |
| Source-owned active runtime files | checked current-project install set, not every shared-destination file | checked source inventory |
| Shared destination / other-owner runtime file | destination may contain several owners; non-members need owner/project scope | source/destination contract + owner resolution |
| Local execution path | exact current-machine/harness path only | execution context |
| Symbol / command / config | `getUserById`, `npm run build`, `DATABASE_URL` | search, run when needed, or read config source |
### Verification triggers
Verify before asserting concrete references, cross-file sync/no-drift, rename/move/update impact, ambiguous references, mixed source/destination wording, parity scope vs shared-destination ownership, tool-path leakage into reusable source, or junk/disposal classification. If the checked scope is limited, report the non-finding as scoped rather than global absence.
---
## Verification Flow
```text
Create reference
  ↓
Does it exist or resolve?
  → YES: use precise reference
  → NO: mark unknown/unverified
  ↓
What role?
  → portable shared / source-side / source-owned active runtime / shared runtime destination / other-owner runtime / checked local fact / machine-scoped example
  ↓
Consistent with related references?
  → YES: continue
  → NO: fix inconsistency
```
Change impact flow: identify affected references → list dependencies → update related references → verify consistency.
---
## Output and Cross-Section Standards
Use precise portable placeholders for shared examples (`<workspace-root>/src/config.js`, `<repo-root>`, `<install-root>`, `<user-runtime-rules>`), exact values only as checked local facts, stable line/symbol references when useful (`config.js:42`, `getUserById()`), and explicit labels:
```markdown
✅ Verified: `<workspace-root>/src/config.js`
⚠️ Unverified: `api.endpoint.url` (not checked)
❌ Not Found In Checked Scope: `/missing/file.js`
```
Avoid vague references such as “the config file”, “that function”, “the variable somewhere”, or one workstation path acting as both source and destination/runtime path.
When exact local values are useful in a report, label them as checked local facts; when writing reusable source artifacts, prefer placeholders or env/config resolution. Source-owned active runtime install scope should point to the checked source inventory, not every file already present in a shared runtime destination. Other-owner runtime files stay outside parity/install claims unless their owner/project scope is explicitly selected or verified.
When modifying, scan related references, identify dependencies, update affected sections/imports/paths/symbols/config/install wording deterministically, and verify consistency.
Change-impact expectations:
- renaming or moving files updates imports, links, install examples, and dependent paths
- renaming symbols updates usages and references where the checked scope supports a sync claim
- changing config keys or commands updates related docs, examples, and verification instructions
- normalizing install docs keeps source-side, destination/runtime, source-owned active runtime install scope, shared destination, and other-owner runtime wording separate
When classifying a new file as junk/disposable/non-governed/safe-to-remove, first scan master surfaces and dependent history; resolve shared-destination owner scope; keep classification unresolved if checked scope is incomplete; and never treat missing recognition or co-location as disposal proof.
---
## Quality Metrics
| Metric | Target |
|---|---|
| Naming/reference consistency, verification, and dependency updates | High / 100% when claiming sync |
| Portable/local, source/destination, and source-owned/shared-destination/other-owner separation | High |
| Scoped non-finding and unresolved owner wording | High |
---
## Integration
Related rules:
- [no-variable-guessing.md](no-variable-guessing.md) - verify values, not only existence
- [zero-hallucination.md](zero-hallucination.md) - do not fabricate references
- [functional-intent-verification.md](functional-intent-verification.md) - verify execution intent when references affect actions
- [portable-implementation-and-hardcoding-control.md](portable-implementation-and-hardcoding-control.md) - portable/local and source/destination notation discipline
- [authority-and-scope.md](authority-and-scope.md) - runtime co-location is not ownership authority
---
