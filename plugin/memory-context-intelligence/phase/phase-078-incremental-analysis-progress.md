# Phase 078 — Incremental Analysis Progress

> **Summary File:** [SUMMARY.md](SUMMARY.md)
> **Phase ID:** 078
> **Current Version:** 0.1.88
> **Status:** completed at selected source/local, documentation/package and plugin release/public-readback gates; installation/reload/native model proof excluded
> **Target Design:** [../design/design.md](../design/design.md) v0.1.88
> **Design References:** [07 scope/progress](../design/07-recall-scoping-and-time-window.design.md); [08 evidence](../design/08-memory-evidence-source-model.design.md); [02 flow](../design/02-topic-list-and-choice-flow.design.md); [09 config](../design/09-init-configuration-surface.design.md)
> **Patch References:** none — approved implementation plan and bounded source diff supply the review boundary; no separate Patch required
> **Full history:** [../changelog/changelog.md](../changelog/changelog.md)
> **Session:** 08244912-a195-4926-84e6-8c202c667ba5 (2026-11-10)

## Objective and lineage

Stop losing old work history when analysis is not invoked for a long interval. Resume oldest-unprocessed records in bounded batches, persist only caller-acknowledged semantic completion, and offer explicit checkpoint-to-endpoint catch-up. Preserve strict candidate eligibility and explicit narrow inspection.

Phase077 is completed discovery/sampling, with no durable completion writer. Phase076 owns stateless supplemental discovery, not progress. Neither the current phase nor a child in those rollout families fits a new persistence/completion/output/recovery boundary, so this opens major078, checked unused. No phase-per-file or new design shard is introduced. The user explicitly selected Main-only editing, source first and docs sync after implementation; the approved plan supplied the upfront contract. No plugin TODO or new Patch is needed.

## Selected behavior and ownership

- `lib/intake.py`: chronological complete-record acquisition, within-day byte-prefix/opaque key positions, exact consumed-byte hashes, bounded partial-day continuation, same-day/backdated append detection and source-rewrite refusal. Direct intake/replay/trial remain stateless.
- `lib/analysis_checkpoint.py`: separate user-scope MCI pending/completed state; schema validation, native nonblocking lock, expected version/position, atomic owner-only replace, zero-topic success, failed/no-ack preservation and duplicate idempotence. No raw trace/transcript/topic ledger or Memsearch write.
- `lib/analysis_surface.py`/wrapper: one batch preparation, payload-bound `complete`, fixed catch-up endpoint, continuation only after acknowledgement, explicit/configured scope isolation and structured blockers. Old input is intentionally eligible; freshness remains metadata.
- `skills/analysis/SKILL.md`: caller semantic discovery and eligibility precede completion, no completion inference from preprocessing, no unread/truncated/error acknowledgement, one-batch incremental default or explicit catch-up. Topic/additional/Main approval stays separate.
- Startup is fileless until the caller binds actual slash arguments. Official Skills docs document text argument substitution rather than a guaranteed exported shell variable. User text is passed as one caller-quoted literal, never inserted into an eager executable fence.
- No cross-run signal accumulation; recurrence is judged within supplied batches. A record exceeding a bounded budget blocks at that record until an adequate deliberate budget/source completion is available. Prefix rewrites/corrupt state block, never auto-reset or skip.

## Execution and disposition

- [x] Canonical root/branch/HEAD/index and existing64 MCI +76 other status rows classified; tracked protected hashes/modes captured. Preserve inherited runtime/docs/test dependencies; exclude visual/preview changes.
- [x] Focused REDs for missing checkpoint/reader/mode, zero-topic completion contract, age-only confidence suppression and scope-safe startup observed before corresponding changes.
- [x] Main implemented sequential reader, separate progress owner, completion/catch-up and explicit-scope compatibility.
- [x] One bounded read-only safety review: malformed nested state could raise an uncaught error; Main reproduced and repaired validation RED→GREEN. No repeated broad review.
- [x] Main reproduced a post-read hash race and bound the cursor digest to the exact consumed bytes; matching RED→GREEN.
- [x] Focused local workflow and final package regression passed; design/docs sync began only afterward.
- [x] Package0.9.40 and all three public Skill versions aligned; manifest/init/analysis Skill checks passed1/1/32 cases. Plugin validator passed with optional `ICON_MISSING` warning, not catalog policy/safety approval. All265 selected relative file links resolved, with preserved snapshot body links interpreted at their documented original base; external URLs/heading fragments excluded. Scoped whitespace and Bash syntax passed. All838 non-MCI tracked and three excluded visual paths retained their baseline bytes/modes.
- [x] Exact67-path source commit `6d7c5074b1f50a62ab4ad9c16802a16befb3003f`, atomic non-force master/tag push and non-draft/non-prerelease GitHub Release; Main Rules `v10.79` remains latest.
- [x] Fresh GitHub tree/archive matched all67 selected bytes/modes and commit/tag/Release identities. Receipt records observed results in this documentation-only follow-up without moving the source tag.

## Development Verification / TestKit Coverage

Routes: `new_focused_test` for progress/cursor/completion gaps; `existing_test` for intake, signals, surface, Skill/manifest and package regression; local real-wrapper workflow with synthetic source and explicit fake caller outcomes. No new runner, browser/provider/model/live corpus campaign or installation gate.

Final source regression: `python3 -B -m unittest discover -s <MCI>/tests -q` under temporary HOME passed **204 tests** in15.940s; Python AST checks passed. An earlier202-test run passed before the admitted startup/hash/schema corrections. Matching focused controls cover oldest-first resume,30-day10/10/10 batches, no-ack/zero-topic/stale/duplicate/failed-replace behavior, multibyte/byte/character tails, same-day/backdated append, source rewrite before completion, exact parsed-byte binding, corrupt nested state, explicit-inspection no-state and fixed endpoint exclusion of later input.

A final schema check added rejection of a missing canonical position field; its existing corruption case failed before the correction, then all five checkpoint cases and four progressive-wrapper cases passed. This affected rerun follows the204-test package run; no second broad regression was needed. After version sync, package/Skill contract checks and plugin validation passed.

The inherited balanced-wrapper expectation was updated for the intentionally changed oldest-first default while preserving canonical late-text, references, candidate no-selection and explicit supplemental-inspection proof. Tests simulate caller acknowledgement; they do not prove a model actually finished reasoning or found better topics. No source-parity claim for installed0.9.38, current-session reload, native slash execution, performance or stability.

## Publication scope and recovery

Publish package0.9.40/governed0.1.88 through the canonical RULES source root. Include inherited source0.9.32–0.9.39 runtime/tests/linked governed history required by current source; preserve and exclude `img/MCI.png`, `index.html`, `preview/**` and all non-MCI changes. Do not promote a clean clone/worktree into implementation or publication authority. Source commit/tag/Release identity and post-publication receipt remain distinct. Immutable tag `memory-context-intelligence--v0.9.40` (annotated object `80c59cbbb479fc9e04b9a944ef6fd16ce485ff2f`) points to source `6d7c5074b1f50a62ab4ad9c16802a16befb3003f`. [Release440250600](https://github.com/DarKWinGTM/claude-code-rules/releases/tag/memory-context-intelligence--v0.9.40) was published2026-11-10T11:01:36Z; fresh public bytes/modes and refs matched. The tag retains truthful pre-publication status text; this later receipt changes documentation only, not runtime payload or tag identity.

No reset/clean/delete, force push, tag move, default-latest replacement, settings/marketplace change, Memsearch mutation, installation/reload or additional/Main promotion is selected. A source defect is repaired in place; no automatic restore or checkpoint reset. Any publication outcome unknown must be reconciled before replay. Old versions/tags and unrelated local work remain preserved. No unselected successor opened.
