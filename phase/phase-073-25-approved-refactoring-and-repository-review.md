# P073-25: Approved Refactoring and Repository Review

> **Summary File:** [SUMMARY.md](SUMMARY.md)
> **Phase ID:** 073-25
> **Current Version:** 10.81
> **Status:** Source/synthetic/installation/public-source verified-in-scope; docs-only receipts recorded outside the immutable tag
> **Target Design:** [System design](../design/design.md) v10.81
> **Design References:** [Coding](../design/coding-discipline.design.md) v1.13; [Execution](../design/execution-and-goal-frame.design.md) v1.41; [Repository model](../design/design/repository-model.design.md); [Skill library](../design/design/skill-library.design.md)
> **Patch References:** none; approved plan and scoped source diff supply the before/after boundary
> **Full history:** [v10.81](../changelog/changelog/v10.81-approved-refactoring-and-repository-review.changelog.md)
> **Session:** 08244912-a195-4926-84e6-8c202c667ba5

## Objective and Lineage

Assess affected structural health during coding without surprise refactoring: evidence and a concrete proportional plan precede explicit user approval, including local/low-risk transformations. Preserve approved continuation and bounded user-owned decisions. Add repository Codex review guidance and normalize the existing source-only Skill directory to `skills/`.

Completed [P073-24](phase-073-24-runtime-clarity-lifecycle-compaction.md) owns different communication/storage/compaction acceptance; it cannot absorb this new consent contract. P073-25 is its sibling in the existing Runtime-owner/install/publication family, not a new major. [P152](phase-152-portable-skill-library.md) remains completed original library provenance; this path-only maintenance adds no new Skill capability or deployment. No current child shares this selected output/approval/proof boundary.

## Selected Semantics and Scope

- Inspect affected structure before material additions, during cumulative growth and before closeout. Cohesion/coupling, responsibility, state/dependency lifecycle, callers, side effects and test boundaries matter; length alone does not force a split.
- Before any refactor present evidence/reason and the simpler sufficient alternative, before/after responsibilities/dependencies, scope/exclusions, protected behavior/callers/failures/side effects, ordered transformations, functional/structural proof and stop/recovery. Obtain explicit approval; small chat plans suffice. Reuse exact approved transformations without repeat questions; labels such as local/tiny/tactical do not bypass consent.
- A feature/fix request does not authorize restructuring. Inspect technical facts directly; ask a bounded question for material intent/output/scope/acceptance/trade-off ambiguity. Pause new material deviations, not independent authorized work. Optional unselected cleanup does not block a satisfied goal.
- Root `AGENTS.md` maps owners and limits review-only behavior. It does not schedule reviews, auto-fix, install or merge; missing private approval transcripts are not proof of unauthorized work. Severity and findings need concrete impact, not length/style/quotas.
- One source library at `skills/`, ten unchanged Markdown documents across six names, no former alias/fallback. Active references change; original-path publication literals remain history. Personal Skills differ and remain independently managed; no deployment, installer or background synchronization.
- Main owns edits in the canonical root. Preserve unrelated modified/untracked state, including the two existing TrialSource diagram additions; commit only selected diagram hunks. Main19 inventory and installer scripts stay unchanged. No RAM/OOM resumption, MCI/plugin update/release, config/hook, Memsearch/corpus or broad code refactor.

## Execution Gates

- [x] Lock approved scope, source/target baseline, owners and existing evidence location; preserve unrelated state.
- [x] Normalize target contracts, observe four new Runtime written-contract REDs and the plural-library packaging RED, then implement at existing owners.
- [x] Run the final selected Node regressions and native Bash installer fixtures.
- [x] Finish full-final-Main19 interpretation and separate AGENTS/source review, then selected links/versions/preservation and exact staged postflight.
- [x] Commit selected source, retain fresh pre-install recovery, install Main19 through the existing launcher and verify exact parity/manifest/other-owner preservation.
- [x] Atomic non-force master plus immutable annotated tag; Main latest non-draft/non-prerelease Release; bounded fresh public commit/tag/Release/selected byte/Git-mode readback.
- [x] Record actual receipts in the selected six owners without changing Runtime/Skills or retagging. Finalizer37 owns this docs-only follow-up push/readback and records its terminal witness in the live task and retained evidence.

## Development Verification / TestKit Coverage

Routes: `new_focused_test`, `existing_test`, full-guidance synthetic interpretation, native fixture `smoke_check`, and explicitly selected actual install/publication readback. Reuse [Case07](../playground/cases/case-07-coding-change-with-verification-discipline.md), [Case08](../playground/cases/case-08-execution-continuity-and-worker-routing.md) and existing runners; no new TestKit or evaluation framework.

Four focused Runtime assertions failed on the missing assessment/plan/approval/clarification contracts, then passed4/4. The plural-source/catalog check failed against the original singular root before the move. Final `node --test --test-concurrency=1 script/test-runtime-safety.mjs script/test-skill-library.mjs` passed61/61. `bash script/test-setup-claude-code-rules.sh` passed native Linux fixtures, including expected test-owned quarantine/preservation cases. Inventory comparison covers Bash/PowerShell payload parity, not Windows execution. Static clauses and authored virtual cases are not model-compliance or historical-cause proof.

The fresh Main19 reader loaded all nineteen complete bodies across four bound parts before no-tool interpretation; S1-S8 match the predeclared decisions, including normal-coding, local-extraction, existing-approval and material-deviation controls. A separate actual AGENTS/source packet reader matches R1-R4 for safe changes, hypothetical lost contracts, instruction-as-data and review-only scope; selected-delta review found no material defect. These are guided synthetic interpretation and source review, not blind evaluation, actual hosted Codex execution or causal benefit. An unintended additional review-skill dispatch was asked to stop; its later empty-finding receipt is not counted as corroboration or selected proof.

Main verified ten moved Skill documents byte/mode-exact, seventeen other Runtime Rules unchanged,1,070 protected tracked source files unchanged,539 selected file links resolving, both original owner-history suffixes exact, aligned nineteen-owner arrays and scoped whitespace. Only the two original TrialSource diagram additions remain unstaged. One workspace-local settings fingerprint changed before any installation; no cause is attributed and no restoration is selected. The original private baseline remains retained separately from the current install-window prestate; whole-wave config preservation is not claimed.

Actual Main19 installation and public-source readback passed in the selected scope. Existing dense overview/design/changelog/summary bodies receive only bounded current navigation and owner-specific contracts; broader preservation-first rollover stays deferred to those owners, with history retained. No whole-project/untracked-tree convergence claim.

## Installation and Publication Receipt

- **Source:** exact33-file commit `f6b003ccb30bf1f910f1dee549d104b212e70ca5`, parent `cef9b7ccffc83070530a8a01ff0ccb259da87da9`. Main19 membership/installer sources and all ten moved Skill bodies/modes remain unchanged outside the selected two Runtime owners.
- **Installation:** the existing launcher exited0 for the selected project target. All nineteen substantive bodies, bytes, Git blobs, filesystem modes and ordered ownership-manifest rows match the source commit. Fresh nineteen-file plus manifest recovery was retained before dispatch. The344 install-window protected fingerprints and six other-owner target entries stayed unchanged, with no quarantine or Skill/plugin deployment. The earlier unattributed workspace-settings drift remains a distinct whole-wave preservation limit, not an installer change or selected restoration.
- **Publication:** fresh ancestry/tag/Release-availability checks preceded an atomic non-force master/tag push. Immutable annotated `v10.81` object `8b2afd269826eaad6cb821f092f926623239225e` peels to the source commit. [Main Release](https://github.com/DarKWinGTM/claude-code-rules/releases/tag/v10.81), published `2026-11-13T10:59:07Z`, is latest, non-draft and non-prerelease; its reviewed body and target were read back.
- **Public payload:** fresh commit/parent/master/tag/peel/Release checks plus50 selected file bodies, Git modes and blob identities passed, covering646,071 bytes. The former `skill/` source is absent from the bound public tree; no downloaded code was executed. This is selected source/Runtime proof, not whole-project convergence.
- **Receipt boundary:** this later docs-only follow-up touches only README, TODO, phase summary/this phase and master/version-detail changelogs. These six updated document bodies are outside source-tag document parity; Runtime, AGENTS and Skill source remain at the immutable source commit. Tasks34/35/36 handed completed proof to finalizer37, which owns the receipt push/readback terminal witness and closes last. No successor selected.

## Publication, Stop and Recovery

Selected completion requires all four source outcomes plus actual Main19 installation and scoped source/tag/GitHub Release/readback, then receipts. Retain independent completed proof if one gate blocks; do not demote required publication to an optional successor. Unknown consequential dispatch requires same-operation reconciliation before replay. Remote divergence/tag collision, unexpected installer cleanup/quarantine, changed ownership/scope or failed proof stops the affected action.

Retained baseline and pre-install recovery are private run evidence, not an automatic restoration source or another development root. Restore only through deliberately approved exact replacement. Current-session adoption, causal benefit/stability and actual hosted Codex PR execution/settings are excluded. No successor selected.
