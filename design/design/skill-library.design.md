# Portable Skill Library - RULES System Design

> **Parent Design:** [../design.md](../design.md)
> **Current Version:** 10.81
> **Session:** 08244912-a195-4926-84e6-8c202c667ba5
> **Section:** Repository-owned on-demand procedures
> **Full history:** [../../changelog/changelog.md](../../changelog/changelog.md)
> **Status:** Selected source and publication target

## Purpose and Selection

Maintain six reusable work procedures under `skills/<name>/SKILL.md`. Rules retain behavioral authority; Skills explain how to perform a selected task. General means usable across projects, languages and business domains, not an instruction to run every procedure on every task.

The user selected this portable source library and its GitHub publication. The earlier archive-directory example illustrates placement, not selection of archive tooling. Browser CLIs, archive commands, storage providers, cross-language bridge recipes, UI-specific features and application-specific billing policy are outside this library.

## Source and Runtime Boundaries

- The Active Project Root owns the curated repository versions. Existing personal Skills are extraction inputs, not a second writer or automatic synchronization source. Import reusable meaning; do not claim byte parity, lossless migration or replacement of the personal library.
- Ship `SKILL.md` plus only linked portable procedural references. Exclude evidence captures, sidecars, ledgers, transcripts, credentials, personal identifiers and machine-specific paths. Do not ingest archived Skills or bundled plugin Skills.
- Root `skills/` is authoring/release source, not an automatic discovery path. Claude Code discovers a separately selected deployment under `<project-root>/.claude/skills/<name>/SKILL.md` or the user's runtime Skill directory. Names should remain stable; inspect existing destinations and resolve ownership/collisions before any future deployment.
- This wave does not deploy or overwrite personal/project Skills, change plugin configuration, introduce an installer, create a runtime entity or expand permissions. There is no background sync, fallback to personal Skills, or automatic archive restoration.
- The existing launcher and its ownership manifest continue to install exactly nineteen root Rules to `.claude/rules/`. Skills do not enter that payload. The maintainer gate installs/checks the unchanged Main19 through the existing installer.

## Procedure Owners

| Skill | Selected procedure | Boundary |
|---|---|---|
| `evidence-based-diagnosis-and-remediation` | Symptom, competing causes, discriminating evidence, remedy and mechanism-backed feasibility comparison | Does not invent Product policy, architecture, live approval or verified historical cause |
| `software-test-validation` | Select useful proof, reuse the fitting harness, execute, discriminate failures and report limits | Does not impose a particular runner, browser, suite, project-wide core-only policy or live gate |
| `workflow-continuity` | Recover checked state, resume runnable selected work, preserve passed gates and hand off blockers | Does not manufacture tasks, choose a task backend, or weaken an explicitly required terminal gate |
| `technical-communication` | Explain checked meaning, causal mechanism, results and next actions at the requested depth | Does not establish business semantics, diagnosis, approval or completion by wording |
| `validating-agent-guidance` | Validate the actual instruction draft and extract transferable, provenance-bound history lessons | Does not require unavailable model calls, a named proposal tool, or claim causal benefit from synthetic tests |
| `coverage-receipt-reconciliation` | Bind, deduplicate and reconcile existing test results against selected coverage | Does not admit new tests, create a report authority or set persistent task status |

Use names to route only when the neighboring procedure is needed; loading one Skill does not mandate loading all six. Main Rules remain the authority for safety, scope, evidence thresholds, worker permission, artifact initiation and closure. Do not reproduce their full doctrine inside each Skill.

## Curation and Failure Semantics

Preserve generalizable processes from the installed parents and their non-evidence references. Generalize examples that expose a transferable mechanism; omit supplier, pricing, framework, native task/API, command-schema and user-preference assumptions. Heavy independent research/history procedures may remain linked references when that reduces ordinary read cost.

A missing tool or reference is a specific capability gap, not permission to add infrastructure or bypass an execution restriction. An unavailable optional observation does not block a satisfied source gate; explicitly selected terminal proof stays pending with its enabling condition. Queued changes, model responses and source edits must remain distinct from landed files, real operation and measured benefit.

## Verification and Recovery

Select `new_focused_test` for exact six-Skill payload, required metadata, linked-reference closure, portable-content exclusions and selected written procedures. Reuse the native Node test runner and existing Rules/installer regressions; do not add an evaluation framework or install service. Test changed guidance with bounded paired allowed/stop scenarios in an authorized read-only context. Synthetic interpretation and static contracts do not establish runtime discovery, causality, repeated reliability or user benefit.

Before publication, verify source/target parity for the selected nineteen Rule bytes/modes and aligned installer payload lists, plus preservation of personal extraction inputs and unrelated dirty state. Runtime changes are owned by their selected Rule chains, not this source-path maintenance. Commit only selected source/document/test/diagram hunks. Publish a new immutable version, verify remote tag/commit and selected public bytes/modes, then record actual results without moving the tag.

Before any destructive recovery, inspect the current selected files and obtain exact action/scope approval. Recover deliberately from independently verified recorded source; do not automatically restore archived/private Skills, replace the workspace, delete unrelated state or force-move a public tag.
