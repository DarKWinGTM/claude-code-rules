# Portable Implementation and Hardcoding Control

## 0) Document Control

> **Parent Scope:** RULES System Design
> **Current Version:** 1.1
> **Session:** dd0bf4af-a66b-4b07-bb9d-a90a0e57b54e (2026-04-02)

---

## 1) Goal

Define one first-class rule chain for preventing non-portable implementation behavior in shared artifacts.

The chain should ensure that:
- shared implementation artifacts stay portable by default
- public onboarding/install docs stay portable by default
- environment-specific values are bound late rather than embedded early
- local exact values remain scoped observations rather than portable defaults
- path hardcoding is treated as one case inside a broader hardcoding-control model rather than as the whole problem

---

## 2) Problem Statement

The system already has strong adjacent guidance for:
- local verification before reference
- evidence-honest communication
- document-role separation
- startup artifact governance

However, those adjacent rules do not by themselves give one explicit owner to the broader implementation-quality problem of hardcoded environment assumptions in shared artifacts and public onboarding/install docs.

Observed failure modes this design intends to close:
- absolute machine-local paths in shared docs/templates
- install locations treated as universal defaults
- public install examples centered on one workstation path or an internal umbrella workspace root
- localhost/port assumptions embedded into reusable examples
- local observations drifting into architecture truth
- source-path and destination/runtime-path notation being blurred together
- code and docs mixing portable and machine-scoped values without an explicit contract
- tactical convenience producing brittle long-term defaults

This is not only a path problem.
It is an environment-binding and public-portability problem.

---

## 3) Scope and Non-Goals

### 3.1 In Scope
- hardcoded path/location assumptions in shared artifacts
- public onboarding/install guidance that teaches non-portable defaults
- hardcoded host/port/install/runtime-target assumptions in shared artifacts
- separation between portable contract and observed local fact
- source-side versus destination/runtime-side notation expectations
- placeholder vocabulary and env/config resolution expectations
- machine-scoped exception handling
- validation/checklist expectations for detecting portability violations

### 3.2 Out of Scope
- local path lookup mechanics themselves (owned by `no-variable-guessing`)
- wording strength for local evidence reporting (owned by `accurate-communication`)
- refusal/recovery behavior when configuration is missing
- generic code-style questions unrelated to portability or environment binding

### 3.3 Boundary Principle
This chain owns **portable implementation defaults and environment-binding discipline** for shared artifacts, including public onboarding/install examples.
It does not replace adjacent owners for local lookup, communication wording, or runtime failure handling.

---

## 4) Classification Model

### 4.1 Portable authority values
These define reusable contracts in:
- rules
- design docs
- templates
- README guidance
- phase/patch examples

Preferred form:
- semantic placeholders

### 4.2 Portable execution values
These define executable contracts in:
- scripts
- runtime config
- launcher/bootstrap logic
- reusable automation

Preferred form:
- env/config-resolved variables

### 4.3 Observed local values
These are checked current-machine facts seen in:
- tool output
- audits
- debug notes
- local verification reports

Preferred form:
- exact values with scoped wording

### 4.4 Machine-scoped contracts
These are intentionally host-specific by design, such as:
- mount paths
- OS service locations
- machine-bound runtime integration points

Preferred form:
- exact values with explicit machine-scope labeling

---

## 5) Default Implementation Contract

### 5.1 Shared-artifact portability
By default, shared artifacts should not embed machine-specific literals.

Preferred examples:
- `<workspace-root>`
- `<repo-root>`
- `<install-root>`
- `<user-runtime-agents>`
- `<user-runtime-skills>`
- `<user-runtime-rules>`
- `<service-base-url>`

### 5.2 Public onboarding/install notation
Public onboarding/install docs should distinguish:
- where the source artifact comes from
- where the installed/runtime artifact lives

Preferred source-side forms:
- `<repo-root>`
- `<workspace-root>` when that workspace is itself the portable contract
- `./` when the command is explicitly run from the repo root

Preferred destination/runtime forms:
- `<install-root>`
- `<user-runtime-agents>`
- `<user-runtime-skills>`
- `<user-runtime-rules>`

Required guidance:
- public docs should not normalize one workstation absolute path or an internal umbrella workspace root as the default source path
- source-side and destination/runtime-side notation should not be collapsed into one exact local absolute path
- if an exact local path is intentionally shown, it must be framed as a local example or a machine-scoped contract

### 5.3 Late-bound execution model
By default, executable runtime assumptions should be resolved through:
- env vars
- config files
- CLI args
- adapter layers
- plugin settings or runtime settings where applicable

Preferred examples:
- `${WORKSPACE_ROOT}`
- `${REPO_ROOT}`
- `${INSTALL_ROOT}`
- `${USER_RUNTIME_AGENTS}`
- `${USER_RUNTIME_SKILLS}`
- `${USER_RUNTIME_RULES}`
- `${SERVICE_BASE_URL}`

### 5.4 Local observation contract
Exact local values may appear in:
- tool execution
- debug output
- audited snapshots
- machine-local incident records

But they must remain explicitly scoped and must not silently become the portable default.

---

## 6) Canonical Notation Model

### 6.1 Documentation notation
Shared documentation should use semantic placeholders.

### 6.2 Executable notation
Executable configuration should use env/config placeholders.

### 6.3 Source-vs-destination notation split
Public onboarding/install docs should keep source-side notation and destination/runtime notation legible as separate layers.

### 6.4 Consistency rule
One artifact or one document chain should not drift across many incompatible notation styles without a clear reason.

---

## 7) Exception Model

### 7.1 Allowed absolute-value exceptions
Exact environment-specific values are allowed when:
- a tool requires the exact local path/value
- the user explicitly asks for the exact local value
- a debug or audit report needs the checked local fact
- a machine-scoped contract is intentionally being described
- a forensic record needs exact preservation

### 7.2 Exception discipline
When an exception is used, the artifact should make clear whether the value is:
- observed local fact
- machine-scoped contract
- user-requested exact value
- explicitly local example rather than public default guidance

---

## 8) Validation Model

### 8.1 Review questions
- Is this a portable contract or only a local observation?
- If it is shared, why is this not a placeholder or env/config binding?
- If it is executable, why is this not resolved through config/env?
- If it is exact, is the exception class explicit?
- Does the onboarding/install wording separate source-side notation from destination/runtime notation?
- Would this still work after moving machines, users, or workspace locations?

### 8.2 Detection triggers
The system should treat these as high-suspicion patterns in shared artifacts:
- `/home/`
- `/Users/`
- drive-letter absolute paths
- temp-directory defaults
- localhost/port defaults presented as universal system truth
- internal umbrella workspace roots shown as public install defaults

### 8.3 Failure classes to catch
- developer-machine-as-default
- observed-value-becomes-contract
- home-directory-as-architecture
- temp-dir-as-authority
- localhost-default-for-shared-system
- internal-umbrella-root-as-public-default
- source-destination-blur
- mixed resolution model drift

---

## 9) Rollout Strategy

### Phase 1
Create the first-class design/runtime/changelog triad for the new chain.

### Phase 2
Integrate adjacent document-governance chains so public onboarding/install guidance is also enforced at the README/install-doc layer and the reference-consistency layer.

### Phase 3
Normalize affected shared/public docs that still teach workstation-specific absolute paths as defaults.

This keeps the semantic owner clear while still leaving application work available as a follow-on execution wave.

---

## 10) Integration

Related chains:
- [../no-variable-guessing.md](../no-variable-guessing.md)
- [../accurate-communication.md](../accurate-communication.md)
- [../project-documentation-standards.md](../project-documentation-standards.md)
- [../document-consistency.md](../document-consistency.md)
- [../strict-file-hygiene.md](../strict-file-hygiene.md)
- [../tactical-strategic-programming.md](../tactical-strategic-programming.md)

---
