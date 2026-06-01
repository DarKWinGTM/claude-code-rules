# P129 — Kroki-Compatible Governed Diagram Doctrine

> **Summary File:** [SUMMARY.md](SUMMARY.md)
> **Phase ID:** P129
> **Status:** Completed / Released
> **Target Release:** v10.37
> **Design References:**
> - [../docs/superpowers/specs/2026-06-01-rules-diagram-companion-pattern-design.md](../docs/superpowers/specs/2026-06-01-rules-diagram-companion-pattern-design.md)
> - [../design/document-governance.design.md](../design/document-governance.design.md)
> - [../design/project-documentation-standards.design.md](../design/project-documentation-standards.design.md)
> - [../design/explanation-and-presentation.design.md](../design/explanation-and-presentation.design.md)
> **Patch References:** [../patch/rules-kroki-compatible-governed-diagram-doctrine.patch.md](../patch/rules-kroki-compatible-governed-diagram-doctrine.patch.md)
> **Session:** 1f1873d2-0feb-485f-a5ff-d383254590dd
> **Full history:** [../changelog/changelog.md](../changelog/changelog.md)

---

## Objective

Strengthen the RULES diagram lane so governed `diagram/` source becomes mandatory Kroki-compatible, allowed breadth is defined as Kroki-compatible + governance-suitable, and `diagram/STRUCTURE.md` becomes the bodyful whole-project detailed visual structure authority for understanding the repo through diagram-first structure.

---

## Why This Phase Exists

P128 opened the dedicated `diagram/` lane and separated it from inline answer/phase-local text-diagram behavior, but it did not yet define a mandatory rendering/source contract.

P129 exists to close that gap. The goal is not governed-docs implementation. The goal is RULES doctrine: make the governed visual lane enforceable, keep `design/` as semantic authority, and raise `diagram/STRUCTURE.md` from a generic anchor into the detailed whole-project structural understanding surface.

---

## Expected Output

- active RULES doctrine says governed `diagram/` source is mandatory Kroki-compatible
- active doctrine defines supported breadth as all formats that are both Kroki-compatible and governance-suitable
- `diagram/STRUCTURE.md` is a bodyful whole-project detailed visual structure authority
- subject diagrams are positioned as zoom-in / decomposition views of the global structure
- inline answer/phase-local text diagrams remain outside governed source truth unless explicitly promoted
- active TODO/phase/changelog/patch surfaces close `v10.37 / P129` consistently
- branch/push/release surfaces are updated in the selected outward-facing scope

---

## Action Checklist

- [x] Add the mandatory Kroki-compatible contract to active diagram doctrine owners.
- [x] Define allowed breadth as Kroki-compatible + governance-suitable rather than as one fixed DSL.
- [x] Strengthen `diagram/STRUCTURE.md` into a bodyful whole-project detailed visual structure authority.
- [x] Keep subject diagrams framed as zoom-in / decomposition views under the global structure.
- [x] Keep inline answer/phase-local text diagrams outside governed source truth unless explicitly promoted.
- [x] Sync touched README/design/TODO/phase/patch/changelog surfaces.
- [x] Run focused diff hygiene and ship the release wave.

---

## Out of Scope

- governed-docs implementation changes
- making Kroki optional or best-effort for governed `diagram/` source
- reducing `design/` semantic authority below `diagram/`
- auto-promoting inline explanatory text diagrams into governed source truth
- touching unrelated waves

---

## Completion Gate

- touched active-owner surfaces make governed `diagram/` source mandatory Kroki-compatible
- touched active-owner surfaces define supported breadth as Kroki-compatible + governance-suitable
- `diagram/STRUCTURE.md` is bodyful and clearly whole-project/detail oriented rather than index/router shaped
- touched active surfaces preserve `design/` semantic authority over `diagram/`
- touched active surfaces keep inline answer/phase-local text diagrams outside governed source truth unless explicitly promoted
- touched TODO/phase/changelog/patch surfaces align to `v10.37 / P129`
- `git diff --check` passes
- branch/default-branch/tag/release evidence align for the promoted `v10.37` state

---

## Current Status

P129 is completed.

Current checked result:
- active RULES doctrine now makes governed `diagram/` source mandatory Kroki-compatible
- allowed breadth is now defined as all formats that are both Kroki-compatible and governance-suitable
- `diagram/STRUCTURE.md` is now written as the bodyful whole-project detailed visual structure authority and includes Kroki-compatible source
- subject diagrams are positioned as zoom-in / decomposition views under the global structure
- inline answer/phase-local text diagrams remain outside governed source truth unless explicitly promoted
- `git diff --check` passed
- the branch was pushed, the promoted state was mirrored to the remote default branch, and GitHub release `v10.37` was created for the promoted state
- Release URL: https://github.com/DarKWinGTM/claude-code-rules/releases/tag/v10.37
