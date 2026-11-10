# Portable Implementation and Hardcoding Control
> **Current Version:** 1.7
> **Design:** [design/portable-implementation-and-hardcoding-control.design.md](design/portable-implementation-and-hardcoding-control.design.md) v1.7
> **Session:** 08244912-a195-4926-84e6-8c202c667ba5
> **Full history:** [changelog/portable-implementation-and-hardcoding-control.changelog.md](changelog/portable-implementation-and-hardcoding-control.changelog.md)

## Rule Statement

**Core Principle: Shared rules/design/templates/code/support/packages/onboarding are portable by default. Bind environment values at the edge through one model; checked local facts are not reusable defaults.**

## Representation and Binding

| Class | Meaning / form |
|---|---|
| Portable authority | shared contract/docs: semantic placeholder |
| Portable execution | runtime/config/scripts: env/config resolution |
| Observed local fact | checked machine value: exact, with scope |
| Machine-scoped contract | deliberately host-specific: exact, with declared scope |

Use stable vocabulary across README/rules/templates/support, not ad hoc aliases. Resolve paths/hosts/ports/install locations late through config/env/CLI/adapter/launcher/bootstrap/deploy, not workstation literals in core. Domain data need not become environment config.

Shared notation: `<workspace-root>`, `<repo-root>`, `<install-root>`, `<user-runtime-agents>`, `<user-runtime-skills>`, `<user-runtime-rules>`, `<service-base-url>`. Executable equivalents: `${WORKSPACE_ROOT}`, `${REPO_ROOT}`, `${INSTALL_ROOT}`, `${USER_RUNTIME_AGENTS}`, `${USER_RUNTIME_SKILLS}`, `${USER_RUNTIME_RULES}`, `${SERVICE_BASE_URL}`.

Public source guidance uses repo-relative `./`, `<repo-root>` or a portable `<workspace-root>` contract; destination/runtime uses install/user-runtime notation. Explain clone/command source separately from installation. One local path cannot silently mean both. No workstation/home/tmp/internal umbrella root as shared default, or unbound hardcoded host/port.

## Local Exceptions and Drift

Exact values fit tool requirements, explicit requests, checked diagnosis/audit/verification, deliberate machine scope or forensic/incident preservation. Label their scope; never promote them to reusable defaults. A local run does not justify embedding its values in shared artifacts.

Repair selected shared owners with placeholders for authority, env/config/adapter binding for execution and scoped exact facts for local reports. Keep genuine domain literals and deliberate machine contracts concrete.

## Integration and Boundaries

[Evidence](evidence-discipline.md)/[wording](accurate-communication.md) qualify local facts; [governance](document-governance.md)/[integrity](document-integrity.md) own onboarding/references/install scope; [coding](coding-discipline.md) owns boundary resolution/convergence. Portability never authorizes overwriting/replacing checked local state.
