# Portable Implementation and Hardcoding Control
> **Current Version:** 1.6
> **Design:** [design/portable-implementation-and-hardcoding-control.design.md](design/portable-implementation-and-hardcoding-control.design.md) v1.6
> **Session:** adda8afb-6edf-466b-add9-b9649b718e01
> **Full history:** [changelog/portable-implementation-and-hardcoding-control.changelog.md](changelog/portable-implementation-and-hardcoding-control.changelog.md)

## Rule Statement

**Core Principle: Shared rules/design/templates/code/support/package/onboarding are portable by default. Bind environment values at the edge through one explicit model; exact checked local facts are not reusable defaults.**

## Representation and Binding

| Class | Meaning / form |
|---|---|
| Portable authority | shared contract/docs: semantic placeholder |
| Portable execution | config/runtime/scripts: env/config resolution |
| Observed local fact | checked current-machine value: exact with scope note |
| Machine-scoped contract | intentionally host-specific requirement: exact with declared scope |

Use a small stable vocabulary across README/rules/templates/support rather than ad hoc aliases. Paths/hosts/ports/install locations resolve late via config/env/CLI/adapter/launcher/bootstrap/deploy—not workstation literals in the core. True domain data need not become environment config.

Shared notation: `<workspace-root>`, `<repo-root>`, `<install-root>`, `<user-runtime-agents>`, `<user-runtime-skills>`, `<user-runtime-rules>`, `<service-base-url>`. Executable equivalents: `${WORKSPACE_ROOT}`, `${REPO_ROOT}`, `${INSTALL_ROOT}`, `${USER_RUNTIME_AGENTS}`, `${USER_RUNTIME_SKILLS}`, `${USER_RUNTIME_RULES}`, `${SERVICE_BASE_URL}`.

Public source guidance uses repo-relative `./`, `<repo-root>` or a genuinely portable `<workspace-root>` contract. Destination/runtime uses install/user-runtime notation. Explain clone/command source context separately from installed location; one local path cannot silently serve both roles. No workstation/home/tmp/internal umbrella root as a shared default or unbound hardcoded host/port.

## Local Exceptions and Drift

Exact local values are appropriate when required by the current tool, explicitly requested, needed in checked debug/audit/verification, intentionally machine-scoped operation, or forensic/incident preservation. Label scope; never promote them into reusable defaults. Local tool execution is not proof a shared artifact should embed that value.

If shared automation/docs carry machine defaults or mixed source/destination notation, repair in the selected owner: semantic placeholders for authority, env/config/adapter binding for execution, scoped exact facts for local reports. Do not force domain literals or deliberate machine contracts into abstract placeholders.

## Integration

[evidence-discipline.md](evidence-discipline.md)/[accurate-communication.md](accurate-communication.md) qualify local facts; [document-governance.md](document-governance.md)/[document-integrity.md](document-integrity.md) govern onboarding/refs/install scope; [coding-discipline.md](coding-discipline.md) keeps boundary resolution and convergence coherent. Portability is not permission to overwrite or replace checked local state.
