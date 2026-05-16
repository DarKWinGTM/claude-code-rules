# Portable Implementation and Hardcoding Control
> **Current Version:** 1.3
> **Design:** [design/portable-implementation-and-hardcoding-control.design.md](design/portable-implementation-and-hardcoding-control.design.md) v1.3
> **Session:** 11c4bd2f-216e-4779-81bf-26d34a4fcaeb
> **Full history:** [changelog/portable-implementation-and-hardcoding-control.changelog.md](changelog/portable-implementation-and-hardcoding-control.changelog.md)
---
## Rule Statement
**Core Principle: Keep shared implementation artifacts and public onboarding/install guidance portable by default, bind environment-specific values late, and treat exact local values as scoped observations rather than reusable defaults.**
This rule owns environment-binding discipline for shared artifacts and install/onboarding examples: paths, install locations, hostnames, ports, and other machine/environment-specific values.
---
## Core Principles
- **Portable core:** shared rules, design docs, templates, reusable code, support/package content, and generalized examples describe portable behavior first; workstation layout is one observed environment, not the system model.
- **Late binding and adapters:** environment-specific paths, hosts, ports, and install locations resolve at the edge through config, env vars, CLI args, adapters, launchers, bootstrap layers, or deployment settings. Keep one explicit resolution model instead of ad hoc literals.
- **Observed-local separation:** checked local values may appear in reports/audits/tool execution, but must be labeled as scoped local facts or explicit machine-scoped contracts, not reusable defaults.
- **Canonical notation:** use semantic placeholders in shared docs and env/config notation in executable contracts; avoid mixed placeholder dialects without a clear contract. A small stable vocabulary is better than many equivalent local names because it keeps README, rules, templates, scripts, and support artifacts aligned.
- **Public onboarding and examples:** default to repo-root-relative or portable source guidance, separate destination/runtime notation, avoid workstation/internal umbrella roots as public defaults, and use exact absolute paths only for explicitly local or machine-scoped examples.
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
Shared authority artifacts should use semantic placeholders such as `<workspace-root>`, `<repo-root>`, `<install-root>`, `<user-runtime-agents>`, `<user-runtime-skills>`, `<user-runtime-rules>`, and `<service-base-url>`.
Public onboarding/install guidance separates source-side forms (`<repo-root>`, `<workspace-root>` when it is the portable contract, or repo-root `./`) from destination/runtime forms (`<install-root>`, `<user-runtime-agents>`, `<user-runtime-skills>`, `<user-runtime-rules>`). Source-side guidance answers where the user clones from or which repo-root context a command uses; destination/runtime guidance answers where the installed or runtime artifact belongs. One exact workstation path must not silently play both roles.
Executable configuration and runtime contracts should use env/config resolution in scripts, launchers, bootstrap code, runtime config, and reusable automation: `${WORKSPACE_ROOT}`, `${REPO_ROOT}`, `${INSTALL_ROOT}`, `${USER_RUNTIME_AGENTS}`, `${USER_RUNTIME_SKILLS}`, `${USER_RUNTIME_RULES}`, `${SERVICE_BASE_URL}`.
Local inspection/debugging may use exact values in tool execution, debug snapshots, audits, and local verification notes when framed as checked local fact, observed current-machine value, or intentionally machine-scoped contract.
---
## Allowed Exceptions
Exact environment-specific values are acceptable when a tool requires the exact local path/value now, the user explicitly asks for it, a debug/audit report needs the checked local fact, an operational contract is intentionally machine-scoped, or a forensic/incident record needs exact preservation.
In those cases, keep scope explicit and do not silently upgrade the value into a portable default. Exact local values may be used for current tool execution or local verification notes, but shared artifacts should still prefer placeholders, config, or late-bound resolution unless the artifact itself is deliberately machine-scoped.
---
## Drift response
Trigger when shared artifacts or reusable automation carry machine-local paths, hardcoded hosts/ports, environment defaults, internal umbrella roots, or mixed source-side versus destination/runtime notation.

Required response:
- replace shared machine-local values with placeholders or env/config binding unless the artifact is explicitly machine-scoped
- move shared runtime defaults to config/env/adapter layers unless the value is true domain data
- keep exact checked local values scoped as observed local facts rather than reusable defaults
- keep source-side and destination/runtime notation explicit and separate

Quick checks:
- no workstation/home/tmp path as shared default
- no hardcoded shared host/port without edge binding
- no exact local value presented as reusable default
- no source/destination blur
---
## Integration
Related rules:
- [evidence-discipline.md](evidence-discipline.md) - local values require checked-scope verification
- [accurate-communication.md](accurate-communication.md) - exact local values need correct evidence strength and scope wording
- [document-governance.md](document-governance.md) - shared docs and onboarding/install guidance stay portable
- [document-integrity.md](document-integrity.md) - source-side and destination/runtime references stay distinct
- [document-integrity.md](document-integrity.md) - reusable artifacts should not accumulate machine-local assumptions
- [coding-discipline.md](coding-discipline.md) - tactical convenience must not become hidden long-term authority
---
