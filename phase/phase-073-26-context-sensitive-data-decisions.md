# P073-26: Context-Sensitive Data Decisions

> **Summary File:** [SUMMARY.md](SUMMARY.md)
> **Phase ID:** 073-26
> **Current Version:** 10.82
> **Status:** Source and guided synthetic interpretation verified-in-scope; source commit, actual installation/publication and receipts pending
> **Target Design:** [System design](../design/design.md) v10.82
> **Design References:** [Coding](../design/coding-discipline.design.md) v1.14; [Runtime inventory](../design/design/runtime-architecture.design.md)
> **Patch References:** none; approved research-backed plan and scoped source diff supply the review boundary
> **Full history:** [v10.82](../changelog/changelog/v10.82-context-sensitive-data-decisions.changelog.md)
> **Session:** 08244912-a195-4926-84e6-8c202c667ba5

## Objective and Lineage

Choose data representations, persistence and hash/computation strategies from purpose, meaning, lifecycle, consumers and guarantees, rather than a universal hash/copy/loop ban. Preserve legitimate projections, immutable history, security work, fresh validation and user-approved refactoring boundaries.

Completed [P073-25](phase-073-25-approved-refactoring-and-repository-review.md) owns refactor consent, AGENTS review and Skill-path acceptance, not this new data-decision contract. P073-26 is its sibling in the existing Runtime-owner/install/publication family, not a reopened slice or new major. Research refined the original proposal before implementation; no new Runtime owner or Product architecture is selected.

## Selected Semantics and Scope

- Purpose/meaning → lifecycle/constraints → alternatives/trade-offs → simplest complete choice → revisit when assumptions change. Consumers include checked protocol/operator/privacy/audit/history/recovery contracts; unknown purpose calls for bounded diagnosis, not speculative creation/deletion.
- Compare reuse/derive/transform/copy/snapshot/persist by validity, isolation, consistency and carrying cost. Read-heavy projections can justify refresh/storage overhead; historical truth is not a disposable cache. One semantic owner need not mean one object/format, and rebuildability grants no deletion authority.
- Select hash guarantees/input domains before primitives. Distinguish exact bytes, deterministic serialization, domain equality and operation intent; preserve precision, input binding, identity and applicable security requirements. No universal algorithm/canonicalizer/direct-comparison mandate.
- Trace computation/invalidation and loop frequency/cardinality/per-item/downstream work. Avoid unchanged discarded work and unintended volatile-input self-invalidation while preserving nonce uniqueness, salt/freshness, isolation and failure ordering. No automatic cache/pipeline, invented cryptography or hash-search.
- Primitive benchmarks and fewer hashes do not establish workflow CPU/memory benefit. Research/source/virtual/guided evidence does not prove historical cause, future model compliance or benefit.
- Main edits in the canonical source root. Other18 Runtime Rules, AGENTS, source Skills, installers/Main19 membership and unrelated modified/untracked work remain unchanged. No Product edits/benchmarks, plugin/Skill deployment, config/hook, session reload, hosted review or RAM/OOM resumption.

## Execution Gates

- [x] Research-backed approved route, checked source/namespace and retained private pre-edit baseline.
- [x] Normalize Coding target, observe five focused missing-contract REDs, implement existing-owner guidance and observe focused GREEN5/5.
- [x] Finish Case07/guided interpretation, final selected regressions and exact source/link/version/preservation postflight. Task39 owns this gate.
- [ ] Commit selected source, then fresh Main19/manifest recovery; actual existing-launcher installation and parity/other-owner preservation. Task39 hands source evidence to Task40, which owns installation/publication.
- [ ] Atomic non-force source/master/tag, immutable annotated v10.82, latest non-draft/non-prerelease Release and bounded fresh public source/readback.
- [ ] Six-owner docs-only receipts, separate commit/push/readback without retagging; Task41 closes last after evidence handoff.

## Development Verification / TestKit Coverage

Routes: `new_focused_test`, `existing_test`, one fresh guided interpretation/selected-delta review, native fixture `smoke_check`, explicitly selected actual installation and publication readback. Reuse [Case07](../playground/cases/case-07-coding-change-with-verification-discipline.md), `source()`/`requiresClause()` and existing Node/Bash checks; no new runner, benchmark or evaluation framework.

Five focused written-contract checks failed for the missing incremental carrying-cost, purpose/representation, hash/input/intent, computation-ordering and loop/nonce clauses, then passed5/5 after the Runtime edit. Final `node --test --test-concurrency=1 script/test-runtime-safety.mjs script/test-skill-library.mjs` passed65/65; `bash script/test-setup-claude-code-rules.sh` passed native Linux isolated fixtures. Both terminal exits were0; inventory parity is not Windows execution and fixtures are not the actual installation.

One fresh reader loaded full final Coding and the relevant unchanged Execution scope/consent clauses before answering S1–S7, then inspected the selected design/test/Case07 anchors. All seven guided synthetic interpretations match the selected decisions; bounded review found no material contradiction/unsafe omission. Main checked the decisive representation/hash/loop and preserved-refactor anchors. These are guided synthetic answers and written-policy/source review, not a blind evaluation, historical cause or causal benefit.

Source postflight found1,092 protected tracked files byte/mode unchanged,473 selected local path links resolving, exact ordered Bash/PowerShell Main19 membership and clean selected whitespace. The exact staged allowlist contains13 selected files; other18 Runtime Rules, AGENTS, Skills, installers and unrelated work are unchanged. An initial standalone inventory probe failed on an indented PowerShell closing-parenthesis matcher; correcting that probe from inspected source passed. No Product/test failure or source correction followed from that probe error.

Dense overview/design/changelog/summary parents receive only bounded current navigation/status; substantive contracts remain at Coding and execution/history detail in this child/version shard. Broader preservation-first rollover remains deferred to those owners before broad absorption, with history retained. No whole-project/untracked-tree convergence claim.

## Installation and Publication Receipt

Pending actual installation/publication. Source-tag and later docs-only receipt identities will remain distinct; no tag movement or advance success claim.

## Stop and Recovery

Selected completion includes source proof, actual Main19 installation, scoped source/tag/latest Release/public payload readback and receipts. A required blocked gate stays blocked, not an optional successor. Unknown consequential outcomes require same-operation reconciliation before replay; retain independently completed effects. Unexpected installer retirement/quarantine, other-owner overwrite, concurrent selected-source changes, remote divergence/tag collision or material contract/scope change stops the affected action.

Retained private baseline/recovery evidence is not an automatic restoration source or alternate development root. Restore only through separately approved exact replacement. Current-session adoption, native Windows execution, hosted review, repeated stability and measured model/CPU/RAM benefit are excluded. No successor selected.
