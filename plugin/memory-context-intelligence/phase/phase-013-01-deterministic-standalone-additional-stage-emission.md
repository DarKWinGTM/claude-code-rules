# Phase 013-01 — Deterministic Standalone Additional-Stage Emission

> **Summary File:** [SUMMARY.md](SUMMARY.md)
> **Phase ID:** 013-01
> **Current Version:** 0.1.78
> **Status:** Clean plugin-only release candidate verified; external-action confirmation pending
> **Target Design:** [../design/design.md](../design/design.md) v0.1.78
> **Design References:** [../design/02-topic-list-and-choice-flow.design.md](../design/02-topic-list-and-choice-flow.design.md), [../design/05-additional-staging-and-promotion.design.md](../design/05-additional-staging-and-promotion.design.md), [../design/08-memory-evidence-source-model.design.md](../design/08-memory-evidence-source-model.design.md)
> **Patch Reference:** [../patch/deterministic-standalone-additional-stage-emission.patch.md](../patch/deterministic-standalone-additional-stage-emission.patch.md)
> **Changelog Reference:** [../changelog/v0.1.78-deterministic-standalone-additional-stage-emission.changelog.md](../changelog/v0.1.78-deterministic-standalone-additional-stage-emission.changelog.md)
> **Session:** 48a3ef9b-50cf-4574-8f00-4f6b6e28f76e (2026-08-09)

---

## Goal

Implement the approved post-presentation selected-topic workflow so explicit user selection produces one collision-safe, rich, standalone additional-stage rule per topic without changing the initial read-only analysis behavior or approving Main RULES promotion.

## Architecture

Extend the existing signal → orchestration → packet → emitter chain in place.

- raw evidence anchors remain internal audit context
- emitted doctrine uses a semantic entailment and normalized-evidence layer
- multiple selected topics remain independent but pass one full-set preflight
- exclusive writes occur only under `additional/memory-context-intelligence/`
- replay, trial, readiness, skill, CLI, and package-facing surfaces converge on the same contract
- release staging uses a clean temporary clone based on `memory-context-intelligence--v0.9.29`, preventing unrelated working-tree changes from entering v0.9.30

## Strategic target and convergence

**Strategic target:** explicit user-selected analysis topics converge into independently reviewable additional-stage doctrine, with one safe source path and no automatic Main RULES promotion.

**Tactical now:** extend the completed Phase 013 implementation in place rather than creating a parallel emitter.

**Convergence path:** replace thin/overwrite-capable selected-topic behavior, update all active consumers, verify the single active path, sync package version 0.9.30, then execute the approval-gated plugin release.

**Closure trigger:** source, focused/full tests, isolated smoke, release-clone tests, exact release scope, remote branch, tag, GitHub Release, and fresh-tag verification all pass at their declared evidence level.

## Global constraints

- Initial `/memory-context-intelligence:analysis` stays read-only, advisory, historical-first, and no-write.
- Initial presentation and ordinary `choose` keep `selected_for_additional_trial=False` and `main_rules_promotion_approved=False`.
- Only a later explicit user instruction may set `selected_for_additional_trial=True`; Main RULES promotion remains false.
- `trace_evidence` remains the live pattern anchor.
- One topic maps to one packet/artifact; combined multi-topic output remains forbidden.
- The complete selected set is preflighted before the first write.
- Any duplicate/existing destination rejects the entire set and preserves existing bytes.
- No active overwrite parameter, flag, compatibility branch, merge, reuse, or replacement path remains.
- Emitted doctrine has no semantic dependency on memory shards, transcript/JSONL files, temporary paths, absolute analysis-only paths, raw `path:line`, or `content_preview` reconstruction.
- Writes remain under `<additional-root>/memory-context-intelligence/`; traversal and symlink escape fail closed.
- Existing fifteen runtime trial artifacts remain untouched.
- Main RULES bodies and Phases 017-018 remain unchanged.
- `lib/analysis_surface.py`, selected-topic config persistence, public `review`/`packet`, bare `/analysis`, auto flow, external agent spawning, and live-web defaults remain outside scope.
- Governed version is `0.1.78`; package version becomes `0.9.30` only after runtime verification.
- Canonical repository is `/home/node/workplace/AWCLOUD/TEMPLATE/RULES`; the active working tree contains extensive unrelated changes and is not the release staging tree.
- Release base/tag: `memory-context-intelligence--v0.9.29` at `a70970c`.
- Release branch/tag/title: `mci-release-v0.9.30`, `memory-context-intelligence--v0.9.30`, `memory-context-intelligence v0.9.30`.
- Push, tag, and GitHub Release require action-and-scope confirmation after tests and staged-scope verification.

## Child phase map

| Child | Output | Gate | Status |
|---|---|---|---|
| [013-01-01](phase-013-01-01-evidence-normalization-and-standalone-rendering.md) | Fresh baseline, signal/topic entailment linkage, selection-state separation, normalized evidence, rich standalone renderer | focused signals/orchestration/packet/renderer tests pass | Completed / verified in focused source scope |
| [013-01-02](phase-013-01-02-atomic-emission-runtime-verification-and-version-sync.md) | Atomic batch preflight, exclusive writes, path/symlink containment, public follow-up state, replay/trial/readiness alignment, isolated smoke, version sync | focused/full tests and temporary-HOME smoke pass; Main RULES unchanged | Completed / verified in local source/test/smoke scope |
| [013-01-03](phase-013-01-03-plugin-release-and-fresh-tag-verification.md) | Clean plugin-only release candidate, push, annotated tag, GitHub Release, fresh-tag verification | explicit external-action confirmation plus remote/tag/release parity | Active / clean 37-path candidate verified; external-action confirmation pending |

## Dependency order

```text
013-01-01 evidence and standalone body
→ 013-01-02 safe emission and runtime proof
→ 013-01-03 clean release and public verification
```

Do not begin release staging from the dirty main working tree. Do not bump package version before the implementation and full source suite pass.

## Selected design coverage

The phase remains open until each item receives a terminal disposition:

- [x] initial analysis remains read-only/no-write — verified in presentation/skill and full-suite scope
- [x] explicit later selection uses additional-only authorization — verified in packet, skill, presentation, and trial scopes
- [x] Main RULES promotion remains false — verified in packet, presentation, replay, trial, and readiness scopes
- [x] trace-to-candidate entailment is checked before emission — focused tests passed
- [x] partial support narrows the mechanism; context-only/reject cannot emit — focused tests passed
- [x] normalized evidence is standalone and excludes transient dependencies — validator tests passed
- [x] rich artifact schema is complete — renderer/readiness validation passed
- [x] one topic per packet/artifact remains enforced — focused and batch smoke checks passed
- [x] multi-topic selection performs independent packetization and one full-set preflight — focused and CLI tests passed
- [x] collision/duplicate handling creates zero files and preserves bytes — focused tests and smoke passed
- [x] overwrite path is absent from Python, CLI, help, reports, replay, trial, and readiness — checked implementation/test scope passed
- [x] root/namespace/traversal/symlink containment passes — focused tests and smoke passed
- [x] isolated smoke does not touch the real runtime additional directory — controlled temporary root verified
- [x] Main RULES before/after digest is equal — controlled smoke verified the checked 24-file scope
- [ ] source and clean release-clone full suites pass — source suite passed (`132 passed`); clean release-clone suite remains pending
- [x] package/governed versions align at `0.9.30` / `0.1.78` — manifest, skill, README, design, changelog, phase, and test surfaces aligned in checked scope
- [ ] plugin-only staged scope is exact — pending clean release candidate
- [ ] remote branch, tag, GitHub Release, and fresh tag clone are verified — pending external-action confirmation and release

## Verification route

- `new_focused_test` for implementation contracts
- `smoke_check` under temporary HOME/additional root
- full plugin suite in source and clean release clone
- fresh tagged-clone verification after release
- no installed marketplace/runtime claim unless separately checked

## Release boundary

The release child uses:

```text
repository: DarKWinGTM/claude-code-rules
base tag: memory-context-intelligence--v0.9.29
branch: mci-release-v0.9.30
tag: memory-context-intelligence--v0.9.30
release title: memory-context-intelligence v0.9.30
```

The release commit contains the exact plugin allowlist declared in 013-01-03. Root `TODO.md`, Main RULES, other plugins, and unrelated working-tree files are excluded.

## Completion gate

Phase 013-01 closes only when:
- all three child gates pass
- selected design coverage has no unclassified material obligation
- package 0.9.30 is verified in a fresh tagged clone
- GitHub Release identity is checked directly
- Main RULES and all pre-existing additional-stage artifacts remain unchanged in checked scope
- verification wording does not exceed the evidence reached

## Verification record fields

At execution closeout, record observed values for:
- baseline command/result
- RED missing-mechanism failures
- focused GREEN commands/results
- temporary single/batch/collision/symlink/Main RULES digest smoke results
- full source-suite and clean release-clone results
- release commit SHA and exact staged scope
- verified remote branch SHA
- annotated tag and peeled commit
- GitHub Release URL/status
- fresh-tag clone result
- checked coverage, explicit exclusions, and evidence-calibrated confidence

Do not prefill these fields from planned or worker-reported results.

## Rollback / containment

Before release, revert only Phase 013-01 plugin-local changes in the clean release candidate. Do not reset or clean the main RULES working tree.

After branch push but before tag/release, use a corrective commit or remove only the dedicated unreleased branch after explicit confirmation.

After published tag/release, do not force-move the tag or silently replace the release. A runtime defect requires a corrective plugin version; release/tag deletion remains a separate destructive action.

Existing additional-stage artifacts, Main RULES, other plugins, unrelated repository state, and Phases 017-018 remain protected.
