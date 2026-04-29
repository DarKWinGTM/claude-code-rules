# Portable Implementation and Hardcoding Control
> **Current Version:** 1.2
> **Design:** [design/portable-implementation-and-hardcoding-control.design.md](design/portable-implementation-and-hardcoding-control.design.md) v1.2
> **Session:** 11c4bd2f-216e-4779-81bf-26d34a4fcaeb
> **Full history:** [changelog/portable-implementation-and-hardcoding-control.changelog.md](changelog/portable-implementation-and-hardcoding-control.changelog.md)
---
## Rule Statement
**Core Principle: Keep shared implementation artifacts and public onboarding/install guidance portable by default, bind environment-specific values late, and treat exact local values as scoped observations rather than reusable defaults.**
This rule owns environment-binding discipline for shared artifacts and public install/onboarding examples: paths, install locations, hostnames, ports, and other machine- or environment-specific values.
---
## Core Principles
### 1) Portable core
Shared rules, design docs, templates, reusable code, support/package content, and generalized examples should describe portable behavior first.
Required guidance:
- prefer portable contracts over workstation literals
- keep core logic independent from machine-specific assumptions
- treat local machine structure as one observed environment, not the default system model
### 2) Late binding
Environment-specific values should resolve at the edge through configuration, environment variables, CLI arguments, adapters, or runtime settings.
Required guidance:
- bind environment details at the edge, not in the portable core
- prefer config/env resolution over literals embedded in shared logic
- keep one explicit resolution model instead of many ad hoc overrides
### 3) Observed-local-fact separation
A checked local value is not a reusable implementation contract.
Required guidance:
- separate local observations from portable defaults
- label exact local values as checked local facts when used in reports or audits
- do not let observed machine state silently become architecture truth
### 4) Adapter boundary
Machine-scoped behavior belongs in adapters, launchers, bootstrap layers, or deployment-specific configuration.
Required guidance:
- keep host-specific details at the edge
- keep reusable code and governance artifacts free of machine-local assumptions by default
- isolate unavoidable machine-scoped contracts explicitly
### 5) Canonical notation
Portable path/location notation should use one small vocabulary.
Required guidance:
- use semantic placeholders in shared documentation
- use env/config notation in executable configuration
- avoid mixing placeholder dialects without a clear contract
### 6) Public onboarding and install guidance
Public onboarding/install guidance should default to portable source guidance and clearly separate destination/runtime notation.
Required guidance:
- use repo-root-relative or portable source guidance when an artifact can be cloned or installed from repo root
- use placeholders or explicit labels for destination/runtime paths
- do not present a workstation absolute path or internal umbrella workspace root as the public default
- if exact local absolute paths appear as examples, mark them as local examples rather than portable defaults
### 7) Example portability
Examples should be portable by default unless their purpose is explicitly machine-scoped.
Required guidance:
- use placeholder examples in shared docs/templates
- use exact absolute paths only for explicitly local or machine-scoped examples
- do not teach bad defaults through convenient non-portable examples
---
## Classification Model
| Class | Meaning | Preferred form |
|---|---|---|
| Portable authority | shared contract in rules/design/templates/reusable docs | semantic placeholder |
| Portable execution | executable config or runtime contract | env/config variable |
| Observed local fact | checked current-machine value | exact value with scope note |
| Machine-scoped contract | intentionally host-specific requirement | exact value with explicit machine scope |
---
## Default Contract
Shared authority artifacts should use semantic placeholders in runtime rules, design docs, README guidance, templates, phase docs, patch docs, reusable examples, and support/package artifacts.
Preferred semantic placeholders: `<workspace-root>`, `<repo-root>`, `<install-root>`, `<user-runtime-agents>`, `<user-runtime-skills>`, `<user-runtime-rules>`, `<service-base-url>`.
Public onboarding/install guidance must separate where the artifact comes from from where it lives or executes.
Preferred source-side forms: `<repo-root>`, `<workspace-root>` when the workspace is the portable contract, or `./` when the command is run from repo root.
Preferred destination/runtime forms: `<install-root>`, `<user-runtime-agents>`, `<user-runtime-skills>`, `<user-runtime-rules>`.
Required guidance:
- source-side guidance answers where the user clones from or which repo-root context a command uses
- destination/runtime guidance answers where the installed/runtime artifact belongs
- one exact workstation path must not silently play both roles
Executable configuration and runtime contracts should use env/config-style resolution in scripts, launchers, bootstrap code, runtime config, and reusable automation: `${WORKSPACE_ROOT}`, `${REPO_ROOT}`, `${INSTALL_ROOT}`, `${USER_RUNTIME_AGENTS}`, `${USER_RUNTIME_SKILLS}`, `${USER_RUNTIME_RULES}`, `${SERVICE_BASE_URL}`.
Local inspection/debugging may use exact values in tool execution, debug snapshots, audits, and local verification notes, but they should be framed as checked local fact, observed current-machine value, or machine-scoped contract when intentionally host-specific.
---
## Allowed Exceptions
Exact environment-specific values are acceptable when a tool requires the exact local path/value now, the user explicitly asks for it, a debug/audit report needs the checked local fact, an operational contract is intentionally machine-scoped, or a forensic/incident record needs exact preservation.
In those cases, keep scope explicit and do not silently upgrade the value into a portable default.
---
## Trigger Model
| Trigger | Required action |
|---|---|
| machine-local path in shared artifact | replace with placeholder/env/config resolution unless explicitly machine-scoped |
| environment default in shared logic | move to config/env/adapter unless true domain data |
| reusable template/example | make portable by default |
| support/package source artifact | avoid baked workstation paths in reusable content |
| public onboarding/install example | use repo-root-relative source guidance and separate destination/runtime notation |
| checked local value | keep scoped as local fact |
| mixed notation drift | normalize to the canonical model |
---
## Forbidden Anti-Patterns
| Anti-pattern | Better behavior |
|---|---|
| developer-machine-as-default | use placeholders or env/config resolution |
| observed-value-becomes-contract | label it as observed local fact only |
| home-directory-as-architecture | use semantic placeholder or env binding |
| temp-dir-as-authority | bind temp paths late and keep non-authoritative |
| localhost-default-for-shared-system | move host/port to config/env |
| single-machine install assumption | use install-root or runtime-resolved paths |
| internal-umbrella-root-as-public-default | use repo-root-relative portable source guidance |
| support-source-hardcodes-workstation-path | use placeholders, context variables, or late-bound config |
| source-destination-blur | separate source-side and destination/runtime notation |
| mixed resolution model drift | use one canonical model |
| silent machine-scoped example | mark local-only examples explicitly |
---
## Validation Checklist
- [ ] Is this value a portable contract or only a local observation?
- [ ] If shared, does it avoid machine-specific literals by default?
- [ ] If executable, does it resolve through env/config or adapter?
- [ ] If exact local values appear, are they explicitly scoped?
- [ ] Does public onboarding/install guidance separate source path from destination/runtime path?
- [ ] If source is repo-local, can it use `<repo-root>` or `./` instead of a workstation literal?
- [ ] Would this still work after moving machines, users, or workspace locations?
- [ ] Is the notation model consistent?
---
## Quality Metrics
| Metric | Target |
|---|---|
| Shared-artifact portability | High |
| Public onboarding/install portability | High |
| Hardcoded environment assumptions in shared artifacts | 0 critical cases |
| Workstation-specific absolute paths as public defaults | 0 critical cases |
| Local fact vs portable contract separation | High |
| Source-vs-destination notation clarity | High |
| Canonical notation consistency | High |
| Machine-scoped exception labeling | High |
---
## Integration
Related rules:
- [no-variable-guessing.md](no-variable-guessing.md) - local values still require checked-scope verification
- [accurate-communication.md](accurate-communication.md) - exact local values need correct evidence strength and scope wording
- [project-documentation-standards.md](project-documentation-standards.md) - shared docs and onboarding/install guidance remain portable
- [document-consistency.md](document-consistency.md) - source-side and destination/runtime references stay distinct
- [strict-file-hygiene.md](strict-file-hygiene.md) - reusable artifacts should not accumulate machine-local junk assumptions
- [tactical-strategic-programming.md](tactical-strategic-programming.md) - tactical convenience must not become hidden long-term authority
---
