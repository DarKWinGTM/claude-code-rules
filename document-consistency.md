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
- verify concrete references or mark them unknown/unverified
- update or describe dependencies when a change impacts multiple files/sections
- keep portable shared references distinct from checked local facts and machine-scoped examples
- keep source-side references distinct from destination/runtime references in install/onboarding guidance
- keep current source-owned active runtime install scope distinct from the shared runtime destination directory
- keep other-owner runtime files distinct from the current project's parity/install target set unless their owner/project is explicitly selected or verified
- keep local execution paths for current tool/runtime operation distinct from reusable source-artifact references
- defer broader portability and anti-hardcoding to `portable-implementation-and-hardcoding-control.md`
### Reference types
| Type | Preferred example | Verification |
|---|---|---|
| File path | `<workspace-root>/src/config.js`, or exact path only as scoped local fact | Glob / Read |
| Source-side install path | `<repo-root>` or `./` from repo root | Read / command-context check |
| Destination/runtime path | `<install-root>/skills`, `<user-runtime-rules>` | config/source contract check |
| Source-owned active runtime files | the current project install set such as a README-listed active rule set | checked source inventory |
| Shared runtime destination | destination directory that may contain several owners' runtime files | source/destination contract check |
| Other-owner runtime file | a runtime-destination file outside the current source-owned install set | owner/project scope resolution |
| Local execution path | exact current-machine/harness path only | execution context |
| Symbol | `getUserById` | Grep |
| Command | `npm run build` | test/run when needed |
| Config | `DATABASE_URL` | read config source |
### Verification triggers
| Trigger | Required action |
|---|---|
| concrete reference | verify before asserting |
| cross-file consistency claim | verify impacted files/sections before sync/no-drift claim |
| rename/move/update impact | trace and update dependent references deterministically |
| ambiguous reference | mark status; avoid unstated assumptions |
| mixed source/destination wording | separate roles and normalize wording |
| parity scope blurred with destination ownership | distinguish source-owned install set, shared destination, and other-owner runtime files |
| tool-path leakage into reusable source | relabel local execution context or replace with placeholder/runtime variable |
| disposal/junk classification | check master surfaces, dependent references, and owner/project scope before cleanup classification |
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
## Output Standards
Preferred references:
- file paths: `<workspace-root>/src/config.js` for portable examples; exact paths only as checked local facts
- source-side install guidance: `<repo-root>` or `./` when command is intended for repo root
- destination/runtime guidance: `<install-root>`, `<user-runtime-rules>`, `<user-runtime-skills>`, `<user-runtime-agents>`
- source-owned runtime install scope: the checked source inventory, not every file in the shared destination
- other-owner runtime files: destination files outside the current source-owned install set until owner/project scope is explicitly selected or verified
- line numbers: `config.js:42`
- symbols: `getUserById()` in `user.service.ts`
Avoid vague references such as “the config file”, “that function we created earlier”, “the variable somewhere”, or one workstation path acting as both source and destination/runtime path.
Labels:
```markdown
✅ Verified: `<workspace-root>/src/config.js`
⚠️ Unverified: `api.endpoint.url` (not checked)
❌ Not Found In Checked Scope: `/missing/file.js`
```
---
## Cross-Section Validation
When modifying:
1. scan the document or checked scope for related references
2. identify cross-section/file dependencies
3. update affected sections deterministically
4. verify consistency throughout
When classifying a newly encountered file as junk, disposable, non-governed, or safe to remove:
1. scan master repo surfaces that could assign governed meaning
2. identify whether dependent references/history already explain the file
3. if the file is in a shared runtime destination but outside the current source-owned install set, resolve owner/project scope first
4. keep classification unresolved if checked scope is incomplete
5. do not treat missing immediate recognition or destination co-location as disposal proof
| Change type | Required action |
|---|---|
| Rename file | update imports/references |
| Move file | update paths |
| Rename symbol | update usages |
| Change config | update references |
| Normalize install docs | update source-side, source-owned install scope, shared destination, and other-owner runtime wording separately |
---
## Quality Metrics
| Metric | Target |
|---|---|
| Naming consistency | 100% |
| Reference verification | High |
| Dependency updates | 100% |
| Reference precision | 100% |
| Portable-vs-local separation | High |
| Source-vs-destination separation | High |
| Source-owned/shared-destination/other-owner separation | High |
---
## Integration
Related rules:
- [no-variable-guessing.md](no-variable-guessing.md) - verify values, not only existence
- [zero-hallucination.md](zero-hallucination.md) - do not fabricate references
- [functional-intent-verification.md](functional-intent-verification.md) - verify execution intent when references affect actions
- [portable-implementation-and-hardcoding-control.md](portable-implementation-and-hardcoding-control.md) - portable/local and source/destination notation discipline
- [authority-and-scope.md](authority-and-scope.md) - runtime co-location is not ownership authority
---
