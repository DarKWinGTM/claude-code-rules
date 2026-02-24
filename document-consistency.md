# Document Consistency and Cross-Reference Validation

> **Current Version:** 1.2
> **Based on:** [design/document-consistency.design.md](design/document-consistency.design.md) v1.2
> **Session:** f19e8a67-d3c2-4c85-aa11-4db6949e61f8
>
> **Full history:** [changelog/document-consistency.changelog.md](changelog/document-consistency.changelog.md)

---

## Rule Statement

**Core Principle: Keep references deterministic, verified, and cross-file consistent.**

---

## Core Rules

- Keep names, paths, identifiers, and terminology consistent across the whole response.
- When referencing file paths, symbols, commands, or config keys, verify existence/validity before asserting.
- If a change impacts multiple sections/files, trace dependencies and update affected references deterministically.

---

## Shared Verification Trigger Model (WS-5)

Apply verification before finalizing references or consistency claims when one or more triggers are present:

| Trigger | Typical Signal | Required Action |
|---------|----------------|-----------------|
| Concrete reference | File path, symbol, command, config key/value | Verify existence/validity with tools before asserting |
| Cross-file consistency claim | "fully synchronized", "all references updated", "no drift" | Verify all impacted files/sections before confirming |
| Rename/move/update impact | Path or identifier changed in one place | Trace and update dependent references deterministically |
| Ambiguous or unresolved reference | Missing file/symbol or uncertain mapping | Mark status explicitly and avoid unstated assumptions |

---

## Verification Labels (Mandatory)

When referencing files, symbols, or configs, use these labels:

- ✅ **Verified:** Confirmed existence via tool execution
- ⚠️ **Unverified:** Not checked or uncertain
- ❌ **Not Found:** Confirmed missing

---

## Output Standard

- Prefer precise references (file paths, symbols, line locations) over vague descriptions.
- Do not present unresolved assumptions as verified facts.

---

## Quality Metrics

| Metric | Target |
|--------|--------|
| Naming consistency | 100% |
| Reference verification coverage | 100% on triggered references |
| Dependency update coverage | 100% |
| Vague/unqualified references | 0 critical cases |

---

> **Full history:** [changelog/document-consistency.changelog.md](changelog/document-consistency.changelog.md)
