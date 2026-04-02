# Portable Implementation and Hardcoding Control

> **Current Version:** 1.0
> **Design:** [design/portable-implementation-and-hardcoding-control.design.md](design/portable-implementation-and-hardcoding-control.design.md) v1.0
> **Session:** dd0bf4af-a66b-4b07-bb9d-a90a0e57b54e
> **Full history:** [changelog/portable-implementation-and-hardcoding-control.changelog.md](changelog/portable-implementation-and-hardcoding-control.changelog.md)

---

## Rule Statement

**Core Principle: Keep shared implementation artifacts portable by default, bind environment-specific values late, and treat exact local values as scoped observations rather than reusable defaults.**

This rule owns environment-binding discipline for shared implementation artifacts, including path assumptions, install locations, hostnames, ports, and similar machine- or environment-specific defaults that should not be hardcoded into portable system behavior.

---

## Core Principles

### 1) Portable-Core Principle
Shared rules, design docs, templates, reusable code, and generalized examples should describe portable behavior first, not one machine's local environment.

Required guidance:
- prefer portable contracts over workstation literals
- keep core logic independent from machine-specific assumptions
- treat local machine structure as one observed environment, not the default system model

### 2) Late-Binding Principle
Environment-specific values should be resolved late through configuration, environment variables, CLI arguments, adapters, or runtime settings.

Required guidance:
- bind environment details at the edge, not inside the portable core
- prefer config/env resolution over literals embedded in shared logic
- keep one explicit resolution model rather than many ad hoc overrides

### 3) Observed-Local-Fact Separation Principle
A checked local value is not the same thing as a reusable implementation contract.

Required guidance:
- separate local observations from portable defaults
- label exact local values as checked local facts when they appear in reports or audits
- do not let observed machine state silently become architecture truth

### 4) Adapter-Boundary Principle
Machine-scoped behavior belongs in adapters, launchers, bootstrap layers, or deployment-specific configuration rather than in shared logic.

Required guidance:
- keep host-specific details at the edge
- keep reusable code and reusable governance artifacts free of machine-local assumptions by default
- isolate unavoidable machine-scoped contracts explicitly

### 5) Canonical-Notation Principle
Portable path and location notation should use one small canonical vocabulary.

Required guidance:
- use semantic placeholders in shared documentation
- use env/config notation in executable configuration
- avoid mixing many placeholder dialects without a clear contract

### 6) Example-Portability Principle
Examples should be portable by default unless the point of the example is specifically machine-scoped behavior.

Required guidance:
- use placeholder examples in shared docs/templates
- use exact absolute paths only when the example is explicitly local or machine-scoped
- do not teach bad defaults through convenient but non-portable examples

---

## Classification Model

| Class | Meaning | Preferred Form |
|------|---------|----------------|
| Portable authority | Shared contract in rules/design/templates/reusable docs | semantic placeholder |
| Portable execution | Executable config or runtime contract | env/config variable |
| Observed local fact | Checked current-machine value | exact local value with scope note |
| Machine-scoped contract | Intentionally host-specific requirement | exact value with explicit machine-scope label |

---

## Default Contract

### Shared authority artifacts
Use semantic placeholders in:
- runtime rules
- design docs
- README guidance
- templates
- phase docs
- patch docs
- reusable examples

Preferred forms:
- `<workspace-root>`
- `<repo-root>`
- `<install-root>`
- `<user-runtime-agents>`
- `<user-runtime-skills>`
- `<service-base-url>`

### Executable configuration and runtime contracts
Use env/config-style resolution in:
- scripts
- launcher/bootstrap code
- runtime config
- reusable automation

Preferred forms:
- `${WORKSPACE_ROOT}`
- `${REPO_ROOT}`
- `${INSTALL_ROOT}`
- `${USER_RUNTIME_AGENTS}`
- `${USER_RUNTIME_SKILLS}`
- `${SERVICE_BASE_URL}`

### Local inspection and debugging
Exact values are allowed in:
- tool execution
- debug snapshots
- audits
- local verification notes

But they should be framed as:
- checked local fact
- observed current-machine value
- machine-scoped contract when intentionally host-specific

---

## Allowed Exceptions

Exact environment-specific values are acceptable when:
- a tool requires the exact local path/value now
- the user explicitly asks for the exact local value
- a debug/audit report needs the checked local fact
- an operational contract is intentionally machine-scoped
- a forensic or incident record needs exact preservation

In those cases:
- keep the scope explicit
- do not silently upgrade the value into a portable shared default

---

## Trigger Model

Apply this rule strongly when one or more of these appear:

| Trigger | Typical Signal | Required Action |
|--------|-----------------|-----------------|
| machine-local path in shared artifact | `/home/...`, `/Users/...`, drive-letter paths | replace with placeholder or env/config resolution unless explicitly machine-scoped |
| environment default in shared logic | host, port, install dir, temp dir, username | move to config/env/adapter unless it is true domain data |
| reusable template/example | docs, templates, README examples, phase/patch examples | make the example portable by default |
| checked local value | tool output or runtime observation | keep it scoped as local fact |
| mixed notation drift | placeholders, literals, and env syntax mixed without contract | normalize to the canonical model |

---

## Forbidden Anti-Patterns

| Anti-Pattern | Why It Hurts | Better Behavior |
|--------------|--------------|-----------------|
| developer-machine-as-default | one machine becomes the accidental system model | use placeholders or env/config resolution |
| observed-value-becomes-contract | local fact quietly becomes shared truth | label it as observed local fact only |
| home-directory-as-architecture | user home layout becomes a fake portability contract | use semantic placeholder or env binding |
| temp-dir-as-authority | temporary paths become durable defaults | bind temp paths late and keep them non-authoritative |
| localhost-default-for-shared-system | local host/port assumptions leak into shared behavior | move host/port to config/env |
| single-machine install assumption | reusable logic depends on one workstation layout | use install-root or runtime-resolved paths |
| mixed resolution model drift | inconsistent notation makes systems fragile | use one canonical placeholder/env model |
| silent machine-scoped example | a local-only example looks like a universal default | mark machine-scoped examples explicitly |

---

## Validation Checklist

- [ ] Is this value a portable contract or only a local observation?
- [ ] If shared, does it avoid machine-specific literals by default?
- [ ] If executable, does it resolve through env/config or an adapter?
- [ ] If exact local values appear, are they explicitly scoped?
- [ ] Would this still work after moving machines, users, or workspace locations?
- [ ] Is the notation model consistent across the artifact?

---

## Quality Metrics

| Metric | Target |
|--------|--------|
| Shared-artifact portability | High |
| Hardcoded environment assumptions in shared artifacts | 0 critical cases |
| Local fact vs portable contract separation | High |
| Canonical notation consistency | High |
| Machine-scoped exception labeling | High |

---

## Integration

Related rules:
- [no-variable-guessing.md](no-variable-guessing.md) - local values still need checked-scope verification
- [accurate-communication.md](accurate-communication.md) - exact local values must be communicated with correct evidence strength and scope
- [project-documentation-standards.md](project-documentation-standards.md) - shared documents and templates should remain portable
- [strict-file-hygiene.md](strict-file-hygiene.md) - reusable artifacts should not accumulate machine-local junk assumptions
- [tactical-strategic-programming.md](tactical-strategic-programming.md) - tactical convenience should not become hidden long-term authority

---
