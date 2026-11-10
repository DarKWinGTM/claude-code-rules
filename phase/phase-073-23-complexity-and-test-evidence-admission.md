# Phase 073-23 - Complexity and Test-evidence Admission

> **Summary File:** [SUMMARY.md](SUMMARY.md)
> **Phase ID:** 073-23
> **Status:** complete in selected source/install/publication scope; fresh-public payload and isolated Main19 installation verified
> **Target Version:** 10.78
> **Session:** 08244912-a195-4926-84e6-8c202c667ba5
> **Full history:** [../changelog/changelog.md](../changelog/changelog.md)
> **Design References:** [Coding](../design/coding-discipline.design.md) v1.11; [Master](../design/design.md) v10.78
> **Patch References:** none; bounded final-form owner repair, with exact before/after in the scoped Git diff

## Objective and Lineage

Make overengineering decisions operational without another Rule or numerical score: compare added structure with a simpler complete alternative, and require a material evidence gap before expanding tests, fixtures or runners. The user explicitly selected actual Runtime installation, scoped commit/push and the matching GitHub Release.

The latest P073-22 slice is complete and owns a different platform-feasibility outcome; P073-21 and P073-18 likewise retain their prior caller/proof and contract-first outcomes. They cannot absorb this new acceptance gate without mixing completed scope. The existing P073 Runtime-owner/install/publication family fits, so this is sibling073-23, not a new major.

Startup uses the existing Coding semantic single-file design/changelog chains, master design and mapped master changelog with one new version shard. Three live tasks track source proof, actual install, and final document/publication reconciliation. Diagram is not required because structure/visual authority/topology is unchanged. A standalone plan, Patch, Rule, runner and framework are not required. Existing entrypoint density is kept bounded by concise current summaries; this wave does not select a historical rollover or unrelated cleanup.

## Selected Semantics

1. **Structure:** identify what a simpler complete alternative would lose; weigh supported benefit against state/transitions, paths, dependencies, indirection, change propagation and setup/runtime/maintenance burden.
2. **Self-created need:** support work created only by a proposal does not establish the proposal's necessity; passing tests proves only their checked correctness.
3. **Necessary engineering:** defer reversible hypothetical generalization, not hard-to-reverse contract analysis, security/integrity safeguards or useful clarity/change boundaries.
4. **Tests:** identify a material evidence gap and a fault existing proof cannot distinguish; reuse or extend the fitting owner. Distinct-fault layers remain valid even for the same headline behavior.
5. **Proportion:** a new helper/file/function, incidental coverage percentage or test-to-product LOC ratio alone justifies neither growth nor removal. Preserve selected acceptance/safety proof; no quotas, mandatory worksheet or universal helper-test rule.
6. **Authority:** Coding owns these two local admission criteria; existing Execution scope/closure and safety/approval owners remain unchanged. No CPU/RAM limit, hook, plugin, Product change or managed Skill update is selected.

## Execution and Completion Gate

- [x] Inspect canonical source, current owners and dirty/index state; preserve baseline bytes/modes and unrelated tracked changes.
- [x] Extend existing written-contract tests and observe two missing-clause failures before Runtime changes.
- [x] Update Coding design before its two Runtime paragraphs, align the triad and extend existing Case07 virtual boundaries.
- [x] Run written-contract/repository regressions and native installer fixtures.
- [x] Resolve the one bounded independent semantic review and final source-preservation checks.
- [x] Install the same Main19 from canonical source into the checked intended user Runtime target; verify payload, modes, bodies, manifest and other-owner preservation.
- [x] Reconcile affected README/master design/changelog/TODO/summary with actual evidence; commit only this wave.
- [x] Non-force push the scoped source commit to the checked existing default branch plus an immutable annotated tag; publish and read back the corresponding non-draft GitHub Release.
- [x] Verify fresh remote tag/commit, selected public payload and one isolated Main19 installation; record actual receipt without moving the release tag.

## Development Verification / TestKit Coverage

Selected routes: `new_focused_test` in existing `script/test-runtime-safety.mjs`; `existing_test` for repository Patch tooling and native installer fixtures; explicit actual install/publication checks. No new TestKit, runner or model-evaluation framework.

- Before Runtime edits, the two new focused checks failed for missing simpler-complete-alternative and distinct-evidence-gap clauses (2 failures, no setup error).
- `node --test --test-concurrency=1 script/test-runtime-safety.mjs script/test-patch-timeline.mjs`: 54/54 passed, including 22 written-contract/metadata checks and 32 Patch-tool tests.
- `bash script/test-setup-claude-code-rules.sh`: passed isolated Bash installer fixtures on Linux.
- `pwsh -NoLogo -NoProfile -NonInteractive -File script/test-setup-claude-code-rules.ps1`: passed isolated PowerShell installer fixtures on Linux, not Windows OS proof.
- Six Case07 variants specify interpretation boundaries; authoring them is not executed model coverage. The one bounded independent review found no material finding in the selected diff; Main verified safeguards, hard-to-reverse contracts, clarity boundaries and distinct-fault test layers against the owner text. This is source interpretation, not model behavior or measured engineering-cost improvement.
- Source preservation checked88 non-selected captured file fingerprints,140 unrelated Git-status rows and2 global files unchanged; all426 selected Markdown links resolve, including the aligned current Runtime inventory consumer and `git diff --check` exited0. Untracked directories remain status-only evidence, not recursively byte-certified.
- Actual-target preflight found the same ordered Main19, only Coding changed, existing ownership manifest matches and no quarantine candidates. Two preflight-checker assumptions failed before mutation: a universal0644 mode and a universal `## Integration` heading. Both were corrected against valid incumbent modes/bodies; no Runtime repair was needed. Original19 bodies plus manifest were captured with exact bytes/modes outside discovery before installation.
- `bash script/launcher.sh --project-root /home/node` exited0. Main19 installed bytes/modes/substantive bodies and ordered SHA256/Git-blob manifest match canonical source; the other18 Runtime owners,4 other-owner files and2 global files retain captured fingerprints. Runtime file names and external quarantine children are unchanged, with no new quarantine. This is installed-disk proof, not session reload.
- Read-only publication preflight found public `DarKWinGTM/claude-code-rules`, default `master` at baseline `b05fcae38381d9fa84bd3717c7577c91487c412e`, and no existing `v10.78` tag/Release in checked scope. The current local branch has no upstream; Main selects the documented existing `HEAD:master` publication route, not a new remote branch. Fresh exact ancestry/tag checks and the selected13-file staged set passed before the atomic non-force push.
- Source commit `59ae04bfb6627cbf4d796ff0140b83c017bfc1c7` has baseline parent `b05fcae38381d9fa84bd3717c7577c91487c412e`. Immutable annotated `v10.78` tag object `592e05f9dac9c5c3028aa34d04a086f1f5f240f7` peels to that source commit; `origin/master` and the tag were atomically fast-forward/non-force published. The non-draft/non-prerelease [Release](https://github.com/DarKWinGTM/claude-code-rules/releases/tag/v10.78), ID439822569, published at `2026-11-10T00:58:50Z`, was read back with exact notes. Source/install/tag proof remains distinct from the Release's `target_commitish: master` label.
- A fresh empty bare fetch recovered that exact public tag/commit. Public bytes and Git modes matched all13 changed paths plus the remaining Runtime payload and trusted installer pair (33 paths,506861 bytes). One empty-target install from that payload through canonical `script/setup-claude-code-rules.sh` exited0; exact Main19 bodies/bytes/modes/ordered SHA256+Git-blob manifest passed with no quarantine. No downloaded script/interpreter code was executed and the public copy was verification only, not a development authority.
- Tasks1/2 handed source/test/install/protection evidence to the same final task3 before closing. This later receipt reconciles the reached publication/public-proof gates; it does not move the immutable tag, reinstall Rules, rerun unchanged behavior or claim whole-project convergence. The tagged documents retain their truthful pre-publication snapshot.

## Preservation, Recovery and Limits

The Active Project Root remains canonical for edits/commits/release inputs. Initial index is empty; unrelated plugin/diagram/support dirty and untracked state is protected and excluded from selected publication. Source/runtime fingerprints and run outputs are owner-only outside source/discovery; untracked directories are status-observed, not exhaustively byte-certified.

Use only the existing owner-aware installer and ordered Main19 set. Inspect the target and preserve original Runtime bodies/manifest before mutation; no other-owner deletion/quarantine or automatic rollback source is selected. Deliberate recovery replaces exact approved files from recorded originals or a separately verified source revision; no alternate source authority, silent fallback, tag movement or force push.

Written guidance and install/publication proof do not establish active-session reload, causal AI benefit, runtime resource containment, repeated reliability or whole-project convergence. Close only the selected source/install/release scope; no successor is selected.
