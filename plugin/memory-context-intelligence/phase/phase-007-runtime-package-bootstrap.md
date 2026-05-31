# Phase 007 - Runtime package bootstrap

> **Summary File:** [SUMMARY.md](SUMMARY.md)
> **Phase ID:** 007
> **Status:** Completed
> **Design References:** [../design/design.md](../design/design.md), [../design/00-core-concept.design.md](../design/00-core-concept.design.md)
> **Patch References:** [../patch/memory-context-intelligence-design-only-baseline.patch.md](../patch/memory-context-intelligence-design-only-baseline.patch.md); runtime package patch: `<repo-root>/plugin/memory-context-intelligence/patch/runtime-package-bootstrap.patch.md`

---

## Objective

Create the isolated runtime package scaffold for `memory-context-intelligence` without installing it into main RULES or creating main-rule mutations.

## Why this phase exists

The capsule had defined the concept only. Before any memsearch intake, topic generation, research enrichment, or `/additional/` emission can run, the runtime needs a bounded package shape with clear command, config, and authority boundaries.

## Goal

Move from documentation-only capsule planning to an isolated runtime package scaffold that can be invoked and checked locally in harmless mode.

## Output

Phase 007 created the package scaffold under `<repo-root>/plugin/memory-context-intelligence/`.

Concrete package file map:
- `README.md` — scaffold status, package map, local no-op command, and separation boundary
- `.claude-plugin/plugin.json` — plugin metadata only, with no hooks or install automation
- `design/design.md` — package-local scaffold design using the generic parent model
- `changelog/changelog.md` — package-local scaffold changelog
- `phase/SUMMARY.md` — package-local execution map
- `patch/runtime-package-bootstrap.patch.md` — package-local before/after bootstrap patch
- `skills/memory-context-intelligence/SKILL.md` — package-local operator support skill
- `agents/trace-scout.md` — future trace-scout lane definition
- `agents/research-scout.md` — future research-scout lane definition
- `agents/source-trust-reviewer.md` — future source-trust-reviewer lane definition
- `agents/synthesis-lead.md` — future synthesis-lead lane definition
- `bin/memory-context-intelligence` — local no-op/help command

The scaffold keeps configuration late-bound and does not hardcode machine-specific memsearch paths as shared defaults.

## Gate

Completed for the phase-007 historical scaffold scope. At phase-007 closeout, the local no-op/help command ran and reported that the package was scaffold-only, with no memsearch analysis, no `/additional/` emission, and no main RULES mutation.

This evidence is not a current package capability snapshot. Later phases 008-016 intentionally superseded the scaffold-only runtime state by adding bounded intake, signal/topic analysis, presentation, choose flow, controlled enrichment, runtime-local orchestration, packet/emission paths, replay, live trial, and checked-scope readiness reporting.

## Owner

Future implementation owner for the package runtime. Main RULES owner remains outside this phase.

## Files

Created runtime package files under `<repo-root>/plugin/memory-context-intelligence/` only.

Updated capsule governance docs after scaffold creation:
- `phase/phase-007-runtime-package-bootstrap.md`
- `phase/SUMMARY.md`
- `changelog/changelog.md`
- `changelog/v0.1.13-completed-runtime-package-bootstrap.changelog.md`
- `README.md`
- `design/design.md`
- `patch/memory-context-intelligence-design-only-baseline.patch.md`
- `<repo-root>/TODO.md` compact deferred-tracking note

## Verification

Ran:

```bash
bash "<repo-root>/plugin/memory-context-intelligence/bin/memory-context-intelligence" --help
```

Result:

```text
memory-context-intelligence local status
mode: scaffold only
memsearch analysis: not run
/additional/ emission: not performed
main RULES mutation: not performed
runtime install/publication: not performed
configuration: late-bound; no machine-specific memsearch paths are package defaults
```

Additional-write boundary check:

```bash
if [ -d "<user-runtime-rules>/additional" ]; then find "<user-runtime-rules>/additional" -newer "/tmp/mci-phase007-start-d42465eb.timestamp" -print; else printf '%s\n' "<user-runtime-rules>/additional: directory not present"; fi
```

Result:

```text
<user-runtime-rules>/additional: directory not present
```

## Risks / rollback notes

The main risk remains accidentally reviving an unbounded plugin/runtime owner. Phase 007 contains that risk by creating only a scaffold and by keeping analysis, emission, install, and main RULES mutation out of scope.

Rollback should remove only the runtime package scaffold under `<repo-root>/plugin/memory-context-intelligence/` and preserve the governed capsule chain unless the user explicitly selects a broader rollback.
