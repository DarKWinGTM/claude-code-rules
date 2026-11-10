# Phase 077 — Parallel Topic Discovery

> **Summary File:** [SUMMARY.md](SUMMARY.md)
> **Phase ID:** 077
> **Current Version:** 0.1.87
> **Status:** Fresh-topic discovery correction for source `0.9.39` / governed `0.1.87` complete at the selected source/fixture/static skill-contract/document gate; installed `0.9.38` and its verified source/install gates remain unchanged historical baseline; model/native-slash behavior unverified; installation/publication unselected
> **Target Design:** [../design/design.md](../design/design.md) v0.1.87
> **Design References:** [Native Agent Orchestration](../design/04-native-agent-orchestration.design.md), [Topic List and Choice Flow](../design/02-topic-list-and-choice-flow.design.md), [Memory Evidence Source Model](../design/08-memory-evidence-source-model.design.md)
> **Patch References:** none — bounded same-owner caller-skill and payload contract without a separate review/rollback boundary
> **Full history:** [../changelog/changelog.md](../changelog/changelog.md)
> **Session:** 7194487f-fe8b-4383-8756-3db4c5612392 (2026-10-03)

## Goal and Lineage

Add optional caller-session parallel viewpoint discovery to `/memory-context-intelligence:analysis`, using actual bounded trace excerpts from the existing intake. This is a distinct candidate-discovery and proof outcome after completed Phase 076; it does not redefine Phase 012's deterministic in-process orchestration, Phase 069's post-eligibility deepening, Phase 075's eligibility gate, or Phase 076's explicit older-window scan.

## Selected Behavior and Invariants

- The analysis-surface pipeline runs once. Historical sampling is record-budget-aligned and balanced across days/sessions/entries; intake owns truthful selected/read/sampled coverage and truncation.
- `topic_discovery_evidence` projects policy-enabled trace records from that loaded intake's canonical minimized `content`, not `signals` previews. At most50 excerpts share intake's character budget and carry producer-owned refs/content-truncation state; signal/candidate/card refs resolve to the same evidence. Private metadata/context-only/generated text stays outside the projection, and caller sanitization/omit-before-worker-dispatch remains required.
- Main-session local semantic discovery runs before generated seeds even without workers. When independent axes and permitted caller tools justify optional workers, up to three lenses—Developer/process, Security, Architect—may add excerpt-only suggestions. Unavailable/skipped workers do not replace local discovery with a finite title catalog.
- Every worker may return zero candidates and is instructed to cite the supplied run-local excerpt reference, state the specific supported gap, and note material uncertainty or counterevidence. Worker suggestions do not determine eligibility, trigger deepening, or authorize web/file/shell/corpus access or writes.
- The main session verifies each citation against the same projection, combines worker suggestions with local candidates, and applies the unchanged Phase 075 gate—including semantic deduplication—to the full set before any deepening or presentation. Rejected candidates are not revived by new wording; agent discovery does not create `required_topic_ids`.
- Agent Teams are conditional caller-session tooling only when already available/enabled and materially useful; the package does not change settings or imply Teams are always available. Do not claim topic quality, diversity, speed, or cost improvement from source instructions alone.
- The flow remains read-only/advisory and does not add a public slash command, new evidence class, corpus scan, web research, additional-stage write, or Main RULES mutation.

## Scope and Owners

- Caller-facing instruction owner: `skills/analysis/SKILL.md`; same-intake projection owner: `lib/analysis_surface.py`.
- Design owners: `design/04-native-agent-orchestration.design.md` distinguishes in-process simulation, caller-session discovery, and post-eligibility deepening; `design/02-topic-list-and-choice-flow.design.md` owns ordering and eligibility; `design/08-memory-evidence-source-model.design.md` owns the projected trace-evidence fields and caps; `design/design.md` remains the active parent.
- Regression coverage: `tests/test_analysis_surface.py`, `tests/test_analysis_skill_contract.py`, `tests/test_plugin_manifest.py`; `tests/test_orchestration.py` continues to protect the Phase 012 in-process behavior.
- Synchronize source manifest/public skills at0.9.39 and affected governed owners at0.1.87; update existing README, summary, changelog and root TODO. Installed0.9.38 and original0.9.37/0.1.85 proof remain historical; neither proves the new source or its model effects.
- Preserve the completed Phase 075 and 076 outcomes and unrelated dirty/untracked work. Installation was excluded from the source/document implementation gate and was selected later as a separate native local-scope update; no direct cache/settings edit, model/provider call, corpus scan, commit, push, tag, release, or publication was selected.

## Fresh-topic discovery correction — source package0.9.39

The approved corrective slice stays in Phase077's evidence/discovery family. It replaces preview-bound discovery evidence with the existing intake's canonical bounded content, adds budget-aligned day/session sampling and truthful coverage, and requires main-session semantic discovery before generated seeds even without workers. Fresh supplemental discovery and matching completed-outcome checks retain the strict Phase075 gate. Installed0.9.38, original parallel/startup proof, and the prior scope incident remain preserved; no new phase, runtime owner, provider, persistent search state, install or release is selected.

Selected proof: `new_focused_test` plus isolated synthetic `smoke_check`; the corrective source/document gate is complete. Matching runtime/skill regressions were observed RED→GREEN. Final package `python3 -m unittest discover -s tests -q` passed187 tests under temporary HOME/cwd with PATH excluding real memsearch. The actual source wrapper verifies8-day canonical evidence, late-text preservation, card refs without selection, truthful coverage and the separate2-day supplemental window. Static skill tests protect local-discovery, fresh-pass and matching-outcome guidance, not generated-model output.

Source `claude plugin validate` passed;27 source/test files passed Python AST syntax checks; scoped `git diff --check` passed. All170 relative targets across11 selected documents exist; package/public-skill0.9.39 and selected governed0.1.87 metadata/maps/backlinks align. The finite protection baseline verifies1880 files/links unchanged, including Main RULES, unrelated dirty source, settings/registry and installed0.9.38. The admitted presentation delta is exactly one evidence-ref carrier line plus its test; `/init` and `/summary` bodies match installed0.9.38 except version metadata. No configured lint/type-checker was found in checked root/package config locations. Behavioral model/native-slash, performance and installed0.9.39 proof remain excluded; no successor phase or installation is opened. Existing design02/04/07/08 own target meaning; this phase owns execution/status only.

## Development Verification / TestKit Coverage

Original0.9.37 verification: `new_focused_test` plus fixture-backed payload and package checks.

- RED/GREEN contract tests cover the required parallel lenses, conditional skip/fallback, excerpt-only boundary, source-reference fan-in, privacy limits, Team capability boundary, and unchanged eligibility/deepening order.
- Payload tests use synthetic signal reports to prove the projection includes only trace-class excerpts, omits transcript/session/path/context-only values, supplies run-local refs, and enforces the 50-excerpt and 220-character bounds.
- The user supplied positive and near-boundary guidance reports from another Claude session. I checked their discovery/eligibility citations against the current skill and found both interpretations consistent with its text. This supports interpretation of those two written-guidance cases only; it does not prove runtime dispatch or generated-model behavior.
- Separately, during earlier work I inadvertently initiated four internal Claude subagent requests in this session contrary to the selected no-model-call restriction. The requests were stopped; whether processing began before termination is unknown. This scope violation is disclosed here and does not authorize further model-based checks. The supplied cross-session reports are not attributed to those requests.
- Verified on 2026-10-03: `python3 tests/test_analysis_skill_contract.py` (27), `python3 tests/test_analysis_surface.py` (18), `python3 tests/test_plugin_manifest.py` (1), and `python3 tests/test_orchestration.py` (6) passed; full `python3 -m unittest discover -s tests -q` passed (170); `claude plugin validate .` passed; package versions align; the selected document-link check found zero missing links; and `git diff --check` exited 0.
- These source, contract, fixture, and user-supplied scenario-interpretation checks do not prove actual caller-session dispatch, generated-model adherence, improved topic diversity/quality, speed, cost, installed behavior, or whole-project convergence. The original selected source/document gate is complete; the internal-agent scope violation is disclosed above, with no additional calls made.

## Analysis-startup correction — package 0.9.38

The user reported two plain slash invocations failing because the supplemental command passed the literal `<analysis_window.next_older_than_day>` to `--older-than-day`. Both source and installed `0.9.37` skills contained two executable context-injection fences. Running the exact second fence reproduced exit 2 and the reported date-format error before intake. Claude Code preprocesses these fences before receiving the surrounding conditional instructions; this is a skill startup defect, not missing corpus evidence or a stale-session workaround.

The bounded correction changes only the supplemental example to an ordinary `bash` fence and states that the caller substitutes the actual payload date after explicit-request/scope checks. The initial executable wrapper, strict date validator, one-pass supplemental policy, eligibility gate and parallel-discovery contract are preserved. This repair is absorbed into the existing Phase077 analysis-source/output family; no new major phase, transport or CLI route is opened.

Selected proof: `new_focused_test` plus an isolated `smoke_check`. The startup regression was observed RED against the two-fence skill, then GREEN after correction; it checks the actual emitted startup command and executes the real wrapper under temporary HOME/cwd without a memsearch root, producing the expected blocked payload rather than a parser failure. Existing valid-date, blocked-window, explicit-config and no-widening fixtures continue to cover supplemental behavior. Final proof passed: full suite `171` tests, source plugin validation, `161` relative targets across `11` selected documents, package/public-skill and affected governed-version alignment, protected CLI/runtime bytes/modes and `git diff --check`. This closes the bounded corrective source/document gate only.

The user subsequently selected the corrective local installation: native updater changed the existing `memory-context-intelligence@darkwingtm` local project row from `0.9.37` to `0.9.38`, and native version/path/enablement checks passed. Install-time parity covered all 340 source/cache files; installed validation and skill-contract/manifest checks passed28/1, including the real installed wrapper under isolated HOME/cwd without corpus input. Selected settings/marketplace/catalog fingerprints and 22 other registry entries stayed unchanged.

The pre-update339-file payload is preserved in the owner-only recovery snapshot recorded in [the corrective changelog](../changelog/v0.1.86-analysis-supplemental-command-startup.changelog.md). A post-update old-cache equality check initially failed because `.orphaned_at` was added during the native-update window; every original old-cache file and recovery byte/mode remained unchanged. No retry, restoration or direct cache edit occurred.

At the0.9.38 checkpoint, six package status/metadata files were edited after installation and excluded from its cache parity: manifest description, README, changelog parent/shard, phase summary and this phase. Root TODO is outside payload. Post-sync334-path parity, fresh source suite171, source validation,162 selected relative links and diff check passed; installed public skill/CLI bytes and modes matched source0.9.38 at that checkpoint. No real corpus/model/provider call, settings edit, current-session reload, commit, push, tag or publication occurred. Fresh-context model interpretation, native skill discovery and full native slash invocation remain unverified; the CLI reports restart is required. Source and selected installation gates are complete at their checked scopes.
