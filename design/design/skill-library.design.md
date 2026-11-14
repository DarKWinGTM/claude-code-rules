# Portable Skill Library - RULES System Design

> **Parent Design:** [../design.md](../design.md)
> **Current Version:** 10.83
> **Session:** 10d553c2-05c0-41bc-af76-96be83d99cfe
> **Section:** Repository-owned on-demand procedures
> **Full history:** [../../changelog/changelog.md](../../changelog/changelog.md)
> **Status:** Selected seven-Skill source, preservation-first adoption and publication target

## Purpose and Selection

Maintain seven reusable work procedures under `skills/<name>/SKILL.md`. Rules retain behavioral authority; Skills explain how to perform a selected task. General means usable across projects, languages and business domains, not an instruction to run every procedure on every task.

The user selected this portable source library and its GitHub publication. The earlier archive-directory example illustrates placement, not selection of archive tooling. Browser CLIs, archive commands, storage providers, cross-language bridge recipes, UI-specific features and application-specific billing policy are outside this library.

## Source and Runtime Boundaries

- The Active Project Root owns the curated repository versions. Existing personal Skills are extraction inputs, not a second writer or automatic synchronization source. Import reusable meaning; do not claim byte parity, lossless migration or replacement of the personal library.
- Ship `SKILL.md` plus only linked portable procedural references. Exclude evidence captures, sidecars, ledgers, transcripts, credentials, personal identifiers and machine-specific paths. Do not ingest archived Skills or bundled plugin Skills.
- Root `skills/` is authoring/release source, not an automatic discovery path. Claude Code discovers a separately selected deployment under `<project-root>/.claude/skills/<name>/SKILL.md` or the user's runtime Skill directory. Names should remain stable; inspect existing destinations and resolve ownership/collisions before any future deployment.
- Selected adoption installs the new procedure and reconciles only missing source-approved deltas into same-name managed Skills; already-covered target semantics remain unchanged. Never replace enriched installed trees with curated subsets. Plugin configuration, a new installer/runtime entity, expanded permissions, background sync, personal fallback and archive restoration remain excluded.
- The existing launcher and its ownership manifest continue to install exactly nineteen root Rules to `.claude/rules/`. Skills do not enter that payload. The maintainer gate installs/checks the unchanged Main19 through the existing installer.

## Skill-local Governance

Every existing or newly separated Skill owns a compact `single-file-bootstrap` design at `skills/<name>/design/<name>.design.md` and version history at `skills/<name>/changelog/<name>.changelog.md`. Its `SKILL.md` declares the matching version, design, authoring session and history. The design owns that procedure's target, invariants, boundaries and proof; history records changes rather than duplicating the target or becoming a task log. Linked `references/` remain operational detail. This library design owns the shared curation/deployment boundary, not a second copy of each procedure.

The local `1.0` baseline establishes governance for already-existing procedures; it is not evidence of their original creation or a new behavioral capability. Local Skill versions are independent of the repository release number. Update the fitting local design before or alongside a selected procedural change, then its source body/references, matching checks and local history. Update the library map when membership or ownership changes; do not create a phase or runtime deployment for every edit.

Develop repository-owned curated Skills here first. An installed same-name Skill can contain independently managed additions: inspect its owner and exact differences, preserve unrelated content, and select any reconciliation before deployment. Do not dual-edit source and runtime or use runtime as an automatic fallback/source. Maintainer design/history are source navigation, not instructions to load during every invocation; their library-owner backlinks are not runtime dependencies. A selected deployment must retain its operational reference closure and explicitly resolve any included maintainer-document navigation.

The initial six-Skill governance addition preserves operational text as a historical source baseline. The selected target adds maintainable-code design1.0 and refines diagnosis/continuity1.1; the other four procedures remain unchanged. Runtime adoption follows source proof and exact destination reconciliation, preserving independent additions. For a new standalone runtime payload, omit only the four maintainer version/design/session/history lines, retaining native metadata and operational content; do not ship dangling source-only navigation. Existing managed payloads receive only missing deltas, not a wholesale export. The main Rule installer remains unchanged; no Skill installation or synchronization service is introduced. Completed publication receipts retain their immutable tag identities.

## Procedure Owners

| Skill and local design | Selected procedure | Boundary |
|---|---|---|
| [designing-maintainable-code](../../skills/designing-maintainable-code/SKILL.md) · [design](../../skills/designing-maintainable-code/design/designing-maintainable-code.design.md) | Choose responsibility/dependency boundaries, semantic reuse and representation/computation lifecycles against a simpler complete alternative | Does not impose size quotas, patterns, caches, Product refactoring or unmeasured performance claims |
| [evidence-based-diagnosis-and-remediation](../../skills/evidence-based-diagnosis-and-remediation/SKILL.md) · [design](../../skills/evidence-based-diagnosis-and-remediation/design/evidence-based-diagnosis-and-remediation.design.md) | Symptom, competing causes, discriminating evidence, remedy and mechanism-backed feasibility comparison | Does not invent Product policy, architecture, live approval or verified historical cause |
| [software-test-validation](../../skills/software-test-validation/SKILL.md) · [design](../../skills/software-test-validation/design/software-test-validation.design.md) | Select useful proof, reuse the fitting harness, execute, discriminate failures and report limits | Does not impose a particular runner, browser, suite, project-wide core-only policy or live gate |
| [workflow-continuity](../../skills/workflow-continuity/SKILL.md) · [design](../../skills/workflow-continuity/design/workflow-continuity.design.md) | Recover checked state, resume runnable selected work, preserve passed gates and hand off blockers | Does not manufacture tasks, choose a task backend, or weaken an explicitly required terminal gate |
| [technical-communication](../../skills/technical-communication/SKILL.md) · [design](../../skills/technical-communication/design/technical-communication.design.md) | Explain checked meaning, causal mechanism, results and next actions at the requested depth | Does not establish business semantics, diagnosis, approval or completion by wording |
| [validating-agent-guidance](../../skills/validating-agent-guidance/SKILL.md) · [design](../../skills/validating-agent-guidance/design/validating-agent-guidance.design.md) | Validate the actual instruction draft and extract transferable, provenance-bound history lessons | Does not require unavailable model calls, a named proposal tool, or claim causal benefit from synthetic tests |
| [coverage-receipt-reconciliation](../../skills/coverage-receipt-reconciliation/SKILL.md) · [design](../../skills/coverage-receipt-reconciliation/design/coverage-receipt-reconciliation.design.md) | Bind, deduplicate and reconcile existing test results against selected coverage | Does not admit new tests, create a report authority or set persistent task status |

Use names to route only when the neighboring procedure is needed; loading one Skill does not mandate loading the others. Main Rules remain the authority for safety, scope, evidence thresholds, worker permission, artifact initiation and closure. Do not reproduce their full doctrine inside each Skill.

## Curation and Failure Semantics

Preserve generalizable processes from the installed parents and their non-evidence references. Generalize examples that expose a transferable mechanism; omit supplier, pricing, framework, native task/API, command-schema and user-preference assumptions. Heavy independent research/history procedures may remain linked references when that reduces ordinary read cost.

A missing tool or reference is a specific capability gap, not permission to add infrastructure or bypass an execution restriction. An unavailable optional observation does not block a satisfied source gate; explicitly selected terminal proof stays pending with its enabling condition. Queued changes, model responses and source edits must remain distinct from landed files, real operation and measured benefit.

## Verification and Recovery

Use the existing native Node Skill-library test owner for selected membership, metadata, linked-reference closure, portable-content exclusions and written procedures. A governance-only addition extends its focused metadata/link assertions and checks exact operational-text preservation; it does not require a new model scenario or application/installer campaign. A changed procedural decision needs bounded paired allowed/stop cases in an authorized context, not an evaluation framework or install service. Synthetic interpretation and static contracts do not establish runtime discovery, causality, repeated reliability or user benefit.

Before publication, verify source/target parity for the selected nineteen Rule bytes/modes and aligned installer payload lists, plus preservation of personal extraction inputs and unrelated dirty state. Runtime changes are owned by their selected Rule chains, not this source-path maintenance. Commit only selected source/document/test/diagram hunks. Publish a new immutable version, verify remote tag/commit and selected public bytes/modes, then record actual results without moving the tag.

Before any destructive recovery, inspect the current selected files and obtain exact action/scope approval. Recover deliberately from independently verified recorded source; do not automatically restore archived/private Skills, replace the workspace, delete unrelated state or force-move a public tag.
