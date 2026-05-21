# Claude Code Rules - TODO

> **Last Updated:** 2026-05-21
> **Current Release:** v10.27 / P119 active-exchange language alignment hardening follow-up
> **Active Wave:** none currently open
> **History:** [todo/history/2026-05-16.md](todo/history/2026-05-16.md); [todo/history/2026-05-08.md](todo/history/2026-05-08.md); [pre-rollover TODO snapshot](todo/history/2026-05-08-pre-rollover-TODO.md)
> **Done Detail:** [todo/done/rules-release-closeouts.md](todo/done/rules-release-closeouts.md); [todo/done/](todo/done/)

---

## ✅ Completed

- [x] P119 / v10.27 active-exchange language alignment hardening follow-up was completed, installed, pushed, mirrored to the remote default branch, and released.
  - Verified: touched language-alignment owners now make active-exchange language the default for goal-shaped output even without a direct language instruction, explicit language requests remain a stronger override, exact literals such as `/goal`, file paths, identifiers, version tags, and query parameters stay token-scoped instead of turning the whole block into an exact literal, and wrapper-only translation is explicitly rejected; the updated `case-16-end-to-end-language-aligned-goal-surface.md` is present; touched master/design/changelog/TODO/phase/patch sync is complete; `playground/` still stays outside the active runtime install payload; runtime install into `~/.claude/rules`, 18/18 source/runtime parity, source/destination body sufficiency, `git diff --check`, branch push, remote default-branch update, and GitHub release verification passed.
  - Release URL: https://github.com/DarKWinGTM/claude-code-rules/releases/tag/v10.27
  - Release tag `v10.27` resolves to commit `54943578d587b1a0deb4bdfda8d402ab065fe111`.
  - Published at `2026-05-21T02:15:51Z`.

- [x] P118 / v10.26 successor-surfacing bridge hardening follow-up was completed, installed, pushed, mirrored to the remote default branch, and released.
  - Verified: touched successor-surfacing bridge owners now reject generic future-note closeout when meaningful successor work is already visible, candidate goals surface more clearly when several successor directions remain live, and smaller bounded successor slices are derived from checked execution surfaces instead of echoing broad future labels; the updated `case-17-proactive-goal-surfacing-and-decision-ready-explanation.md` is present; touched master/design/changelog/TODO/phase/patch sync is complete; `playground/` still stays outside the active runtime install payload; runtime install into `~/.claude/rules`, 18/18 source/runtime parity, source/destination body sufficiency, `git diff --check`, branch push, remote default-branch update, and GitHub release verification passed.
  - Release URL: https://github.com/DarKWinGTM/claude-code-rules/releases/tag/v10.26
  - Release tag `v10.26` resolves to commit `b0b4b46fba2725b1abad4d6d4768647a897f2249`.
  - Published at `2026-05-20T17:54:46Z`.

- [x] P117 / v10.25 proactive goal surfacing and decision-ready response style refinement was completed, installed, pushed, mirrored to the remote default branch, and released.
  - Verified: touched owners now surface candidate goals more proactively at real decision boundaries when no one path clearly dominates; default non-trivial answers now encode plain-language summary first, small-table-when-useful, grouped explanation, identifier-meaning-first wording, visible verified/inference/hypothesis separation, and concise decision-ready close; `case-17-proactive-goal-surfacing-and-decision-ready-explanation.md` and the playground index update are present; touched master/design/changelog/TODO/phase/patch sync is complete; playground still stays outside the active runtime install payload; runtime install into `~/.claude/rules`, 18/18 source/runtime parity, source/destination body sufficiency, `git diff --check`, branch push, remote default-branch update, and GitHub release verification passed.
  - Release URL: https://github.com/DarKWinGTM/claude-code-rules/releases/tag/v10.25
  - Release tag `v10.25` resolves to commit `0a32fa1c81a81739094ab94c9e6e8627d024bc03`.
  - Published at `2026-05-20T13:05:37Z`.

- [x] P116 / v10.24 end-to-end language-aligned goal surface refinement was completed, installed, pushed, and released.
  - Verified: touched runtime owners teach end-to-end dominant-session-language behavior across candidate goals, advisory `/goal`, recommendation labels, and recap/closing lines; exact literals remain preservable where they should stay exact; `case-16-end-to-end-language-aligned-goal-surface.md` and the playground index update are present; touched master/design/changelog/TODO/phase/patch sync is complete; playground still stays outside the active runtime install payload; runtime install into `~/.claude/rules`, 18/18 source/runtime parity, source/destination body sufficiency, `git diff --check`, branch push, and GitHub release verification passed.
  - Release URL: https://github.com/DarKWinGTM/claude-code-rules/releases/tag/v10.24
  - Release tag `v10.24` resolves to commit `68f623e26d46e381fc098ff87f04daf99b3e7818`.
  - Published at `2026-05-20T09:53:32Z`.

- [x] P115 / v10.23 language-aware candidate-goal promotion playground case update was completed, installed, pushed, and released.
  - Verified: `case-15-language-aware-candidate-goal-promotion.md`, playground index update, touched master/design/changelog/TODO/phase/patch sync, playground still excluded from the active runtime install payload, runtime install into `~/.claude/rules`, 18/18 source/runtime parity, source/destination body sufficiency, `git diff --check`, branch push, and GitHub release verification passed.
  - Release URL: https://github.com/DarKWinGTM/claude-code-rules/releases/tag/v10.23
  - Release tag `v10.23` resolves to commit `f434a3b31baa3532d933687545ec3f2b3f229c60`.
  - Published at `2026-05-20T08:59:56Z`.
- [x] P114 / v10.22 language-aware candidate goal and goal-command doctrine was completed, installed, pushed, and released.
  - Verified: dominant-session-language ownership for candidate goals and promoted `/goal`, candidate-goal-first successor recommendation mode, selective promotion from candidate goal to governed `/goal`, two Thai-first governed examples, runtime install into `~/.claude/rules`, 18/18 source/runtime parity, source/destination body sufficiency, `git diff --check`, branch push, and GitHub release verification passed.
  - Release URL: https://github.com/DarKWinGTM/claude-code-rules/releases/tag/v10.22
  - Release tag `v10.22` resolves to commit `3313fb193f96d5f18c6a6d45c7864e9971c8569d`.
  - Published at `2026-05-20T08:24:10Z`.
- [x] P113 / v10.21 governed-work-only goal context sourcing doctrine was completed, installed, pushed, and released.
  - Verified: governed-work-only `/goal` trigger doctrine, exact mandatory governed-surface trigger conditions, design-first governed `/goal` sourcing order, material-only changelog/patch/README inclusion, compact advisory output guidance, two concrete `/goal` examples, runtime install into `~/.claude/rules`, 18/18 source/runtime parity, source/destination body sufficiency, `git diff --check`, branch push, and GitHub release verification passed.
  - Release URL: https://github.com/DarKWinGTM/claude-code-rules/releases/tag/v10.21
  - Release tag `v10.21` resolves to commit `53f80777bd3b0ec9d5ad84165bcd58e6e726c4f2`.
  - Published at `2026-05-20T07:54:14Z`.
- [x] P112 / v10.20 grounded playground transcript cases and realism upgrade was completed, installed, pushed, and released.
  - Verified: transcript-grounded observed entries with exact checked transcript paths plus anchor hints, richer multi-turn scenario traces, stronger flow explanations, two grounded new scenario families, README pointer-level integration, project-local 18/18 source/runtime parity, source/destination body sufficiency, `playground/` excluded from `.claude/rules/`, `master` push, and GitHub release verification passed.
  - Release URL: https://github.com/DarKWinGTM/claude-code-rules/releases/tag/v10.20
  - Release tag `v10.20` resolves to commit `4851338417501a391e7dc505d0b049d7fb6209db`.
  - Published at `2026-05-19T03:51:01Z`.
- [x] P111 / v10.19 RULES playground family behavior scenarios was completed, installed, pushed, and released.
  - Verified: governed non-runtime playground family baseline, 10 scenario-family case files, prompt/response examples, lightweight flow diagrams, full 18-rule coverage map, virtual-case matrix, README pointer-level integration, project-local 18/18 source/runtime parity, source/destination body sufficiency, `master` push, and GitHub release verification passed.
  - Release URL: https://github.com/DarKWinGTM/claude-code-rules/releases/tag/v10.19
  - Release tag `v10.19` resolves to commit `e3e0bdfe255c2370085abcfebbb25a6544de9a1b`.
  - Published at `2026-05-19T01:39:59Z`.
- [x] P110 / v10.18 project-local Claude Code install architecture and explanation clarity doctrine was completed, installed, pushed, and released.
  - Verified: launcher-first clone → project install UX, helper execution layer preservation, dedicated installer architecture design, meaning-first identifier explanation doctrine updates, launcher-driven Bash/PowerShell install proof, project-local 18/18 source/runtime parity, source/destination body sufficiency, `master` push, and GitHub release verification passed.
  - Release URL: https://github.com/DarKWinGTM/claude-code-rules/releases/tag/v10.18
  - Release tag `v10.18` resolves to commit `b1ee4100b471b96a975c22a480137b81fa5efc8a`.
  - Published at `2026-05-19T00:42:14Z`.
- [x] P109 / v10.17 lineage-first phase selection and subphase enforcement was completed, installed, pushed, and released.
  - Verified: strict current-phase → subphase → new-major fall-through enforcement, explicit why-not-current / why-not-subphase basis, touched companion/master-surface sync, README-driven runtime install, 18/18 source/runtime parity, source/destination body sufficiency, `master` push, and GitHub release verification passed.
  - Release URL: https://github.com/DarKWinGTM/claude-code-rules/releases/tag/v10.17
  - Release tag `v10.17` resolves to commit `a330d414c6fd20febf2222288651cc166d0c62b0`.
  - Published at `2026-05-18T14:01:40Z`.
- [x] P108 / v10.16 worker-routing runtime compaction and owner redistribution was completed, installed, pushed, and released.
  - Verified: worker-routing compaction below the performance threshold, owner redistribution into document-integrity/document-governance, runtime install, 18/18 source/runtime parity, source/destination body sufficiency, `master` push, and GitHub release verification passed.
  - Release URL: https://github.com/DarKWinGTM/claude-code-rules/releases/tag/v10.16
  - Release tag `v10.16` resolves to commit `731624622af67e68869469d74f419d5c67a6752d`.
  - Published at `2026-05-18T05:01:02Z`.
- [x] P107 / v10.15 explicit goal-command suggestion doctrine was completed, installed, pushed, and released.
  - Verified: `/goal` trigger doctrine, compact `/goal` output shape, `/goal` sourcing/writing doctrine, advisory/pruning guards, runtime install, 18/18 source/runtime parity, source/destination body sufficiency, `master` push, and GitHub release verification passed.
  - Release URL: https://github.com/DarKWinGTM/claude-code-rules/releases/tag/v10.15
  - Release tag `v10.15` resolves to commit `771a4769b65910cf28b9c7e6c30145551a88cec8`.
  - Published at `2026-05-18T02:34:32Z`.
- [x] P106 / v10.14 parent-model supersession and adherence validation was completed, installed, pushed, and released.
  - Verified: active-doctrine supersession precedence, selected historical guard wording, chronology/adherence verification hardening, runtime install, 18/18 source/runtime parity, source/destination body sufficiency, `master` push, and GitHub release verification passed.
  - Release URL: https://github.com/DarKWinGTM/claude-code-rules/releases/tag/v10.14
  - Release tag `v10.14` resolves to commit `3e163fc7be7922230155ef0f184f2484b73509a6`.
  - Published at `2026-05-17T23:36:10Z`.
- [x] P105 / v10.13 folder-scoped generic parent and single-parent authority was completed, installed, pushed, and released.
  - Verified: folder-scoped generic-parent allowance, single-parent-authority integrity, runtime install, 18/18 source/runtime parity, source/destination body sufficiency, `master` push, and GitHub release verification passed.
  - Release URL: https://github.com/DarKWinGTM/claude-code-rules/releases/tag/v10.13
  - Release tag `v10.13` resolves to commit `b1eba20b8c31041afd794625650a1107d8702e05`.
  - Published at `2026-05-17T13:43:03Z`.
- [x] P104 / v10.12 semantic parent naming and bootstrap-first design normalization was completed, installed, pushed, and released.
  - Verified: naming/bootstrap integrity in checked scope, runtime install, 18/18 source/runtime parity, source/destination body sufficiency, `master` push, and GitHub release verification passed.
  - Release URL: https://github.com/DarKWinGTM/claude-code-rules/releases/tag/v10.12
  - Release tag `v10.12` resolves to commit `a5dfb34ab7a26dc91bff3861ca3425bf00c99d8a`.
  - Published at `2026-05-17T09:16:12Z`.
- [x] P103 / v10.11 observed-shape, extracted-doctrine, and selected-target separation was completed, installed, pushed, and released.
  - Verified: wording/equivalence integrity in checked scope, runtime install, 18/18 source/runtime parity, source/destination body sufficiency, `master` push, and GitHub release verification passed.
  - Release URL: https://github.com/DarKWinGTM/claude-code-rules/releases/tag/v10.11
  - Release tag `v10.11` resolves to commit `a764f7aaa08a5d2193013d2fd6480f0bba3f88c6`.
  - Published at `2026-05-17T07:01:37Z`.
- [x] P102 / v10.10 chain-shape normalization and append-vs-shard gate was completed, installed, pushed, and released.
  - Verified: chain-shape doctrine consistency in checked scope, runtime install, 18/18 source/runtime parity, source/destination body sufficiency, `master` push, and GitHub release verification passed.
  - Release URL: https://github.com/DarKWinGTM/claude-code-rules/releases/tag/v10.10
  - Release tag `v10.10` resolves to commit `941fde875dedc2cede3db6f4bee2d144c4b029c3`.
  - Published at `2026-05-17T01:55:18Z`.
- [x] P101 / v10.09 governed path normalization and premise-separation was completed, installed, pushed, and released.
  - Verified: normalization integrity, touched-owner/companion consistency in checked scope, runtime install, 18/18 source/runtime parity, source/destination body sufficiency, `master` push, and GitHub release verification passed.
  - Release URL: https://github.com/DarKWinGTM/claude-code-rules/releases/tag/v10.09
  - Release tag `v10.09` resolves to commit `c883b8617ebfda89ff8dc288533dffe835d6785b`.
  - Published at `2026-05-17T00:52:06Z`.
- [x] P100 / v10.08 safe-first active runtime compression was completed, installed, pushed, and released.
  - Verified: preserve-mechanism review, 18/18 parity/body sufficiency, owner-link validation, runtime install, source/runtime parity, source/destination body sufficiency, and GitHub release verification passed.
  - Release URL: https://github.com/DarKWinGTM/claude-code-rules/releases/tag/v10.08
- [x] P099 / v10.07 proactive subagent efficiency and lane templates was completed, installed, pushed, and released.
  - Verified: 18/18 parity/body sufficiency, owner-link validation, runtime install, source/runtime parity, source/destination body sufficiency, and GitHub release verification passed.
  - Release URL: https://github.com/DarKWinGTM/claude-code-rules/releases/tag/v10.07
- [x] `memory-context-intelligence` phase 029 shared darkwingtm marketplace bridge design resolution was completed.
  - Selected design: keep active runtime marketplace `darkwingtm` mapped to `/home/node/workplace/AWCLOUD/TEMPLATE/PLUGIN`; do not use `/home/node/workplace/AWCLOUD/TEMPLATE/RULES/plugin` as the active runtime marketplace root; later add `memory-context-intelligence` as an extra entry inside `/home/node/workplace/AWCLOUD/TEMPLATE/PLUGIN/.claude-plugin/marketplace.json` with source `../RULES/plugin/memory-context-intelligence`; keep `/home/node/workplace/AWCLOUD/TEMPLATE/PLUGIN/memory-context-intelligence/` as deprecated historical docs only, not the active plugin package.
  - Rejected alternatives: remapping `darkwingtm` to `TEMPLATE/RULES/plugin` would break existing shared-marketplace plugins; creating a second active package under `TEMPLATE/PLUGIN` would create source drift and duplicate truth.
  - Boundary: docs-only; no plugin install state, settings, marketplace registry, installed plugins, cache, source package runtime contents, or `/additional/` material was intentionally mutated. Phase 030 remains planned / approval-sensitive for bridge-entry implementation plus marketplace availability / install / uninstall reproof after explicit approval.
- [x] `memory-context-intelligence` phase 028 restored darkwingtm shared-marketplace governance sync was completed.
  - Verified in governed docs scope: active source package remains `/home/node/workplace/AWCLOUD/TEMPLATE/RULES/plugin/memory-context-intelligence/`; active runtime marketplace mapping is restored to `darkwingtm` -> `/home/node/workplace/AWCLOUD/TEMPLATE/PLUGIN`; the restored shared marketplace does not include `memory-context-intelligence`; and `memory-context-intelligence@darkwingtm` is not currently installed/enabled there.
  - Reclassification: phases 025-027 remain completed historical checked evidence from the temporary/remapped `darkwingtm` state, not current runtime truth after the marketplace restore; retained cache/data from the old proof is evidence only, not active install state.
  - Boundary: docs-only; no plugin install state, settings, marketplace registry, cache, source package runtime contents, or `/additional/` material was intentionally mutated. Publication, external marketplace release, slash-command/chat invocation proof, stable/broad production readiness, main RULES promotion/mutation/merge, and current `memory-context-intelligence@darkwingtm` install/enablement remain unclaimed.
- [x] `memory-context-intelligence` phase 027 darkwingtm uninstall lifecycle closeout remains completed historical evidence.
  - Verified in historical checked local scope: `claude plugin uninstall --scope local --keep-data "memory-context-intelligence@darkwingtm"` succeeded from `/home/node/workplace/AWCLOUD/CLAUDE`; normal and bare plugin lists no longer included `memory-context-intelligence@darkwingtm`; bare details exited `1` with plugin not found.
  - Historical surfaces recorded: the then-effective `darkwingtm` marketplace registration remained retained, `/home/node/workplace/AWCLOUD/CLAUDE/.claude/settings.local.json` had no `memory-context-intelligence` reference, `/home/node/.claude/plugins/installed_plugins.json` no longer had the `memory-context-intelligence@darkwingtm` key, and `/home/node/.claude/plugins/cache/darkwingtm/memory-context-intelligence/0.9.0` remained present with `.orphaned_at` value `1779155486899`.
  - Current boundary: after the marketplace restore to `/home/node/workplace/AWCLOUD/TEMPLATE/PLUGIN`, this is not current target-state proof; retained cache/data is evidence only, not active install state. The source package and `/additional/` trial material remain preserved; slash-command/chat invocation, publication, external marketplace release, stable/broad production readiness, and main RULES promotion/mutation/merge remain unclaimed.
- [x] `memory-context-intelligence` phase 026 darkwingtm local-scope persistent install proof remains completed historical evidence.
  - Verified in historical checked local scope: `claude plugin install --scope local "memory-context-intelligence@darkwingtm"` succeeded from `/home/node/workplace/AWCLOUD/CLAUDE`; normal and bare CLI checks showed `memory-context-intelligence@darkwingtm` installed with `scope: "local"`, `enabled: true`, project path `/home/node/workplace/AWCLOUD/CLAUDE`, and cache path `/home/node/.claude/plugins/cache/darkwingtm/memory-context-intelligence/0.9.0`.
  - Historical surfaces recorded: `/home/node/workplace/AWCLOUD/CLAUDE/.claude/settings.local.json`, `/home/node/.claude/plugins/known_marketplaces.json`, `/home/node/.claude/plugins/installed_plugins.json`, `/home/node/.claude/plugins/cache/darkwingtm/memory-context-intelligence/0.9.0`, cached manifest identity, and `/home/node/workplace/AWCLOUD/TEMPLATE/RULES/plugin/.claude-plugin/marketplace.json`.
  - Current boundary: after the marketplace restore to `/home/node/workplace/AWCLOUD/TEMPLATE/PLUGIN`, this is not current installed/enabled state for `memory-context-intelligence@darkwingtm`; slash-command/chat invocation, publication, external marketplace release, stable/broad production readiness, main RULES promotion/mutation/merge, and `/additional/` behavior change remain unclaimed.
- [x] `memory-context-intelligence` phase 025 darkwingtm session split proof remains completed historical evidence.
  - Verified in historical recorded docs scope: `claude plugin list --available --json` proved marketplace-qualified availability for `memory-context-intelligence@darkwingtm` under the temporary/remapped `darkwingtm` state, while `claude --bare --plugin-dir "/home/node/workplace/AWCLOUD/TEMPLATE/RULES/plugin/memory-context-intelligence" plugin list --json` separately proved session-only disk loading as `memory-context-intelligence@inline` with `scope: "session"`.
  - Current boundary: after the marketplace restore to `/home/node/workplace/AWCLOUD/TEMPLATE/PLUGIN`, this no longer represents current runtime truth or current `memory-context-intelligence@darkwingtm` availability under the restored shared marketplace.
- [x] `memory-context-intelligence` phases 019-023 remain completed checked-local installability evidence, now reclassified as transitional namespace proof.
  - Verified: phase 019 planning/installability contract, phase 020 source-side manifest/local marketplace bootstrap, phase 021 session-only inline load proof, phase 022 local-scope persistent CLI install proof as `memory-context-intelligence@rules-local`, and phase 023 reload/new-process evidence reuse plus approved uninstall-only closeout are completed.
  - Reclassification: under the later selected namespace basis, phases 020-023 prove `@inline` / `rules-local` behavior only; they do not prove selected target install ID `memory-context-intelligence@darkwingtm` persistent install or uninstall lifecycle behavior.
  - Boundary: prior evidence is preserved as checked local lifecycle evidence only, not publication, external marketplace release, slash-command/chat invocation proof, stable/broad production readiness, main RULES promotion, main RULES mutation, main RULES merge, or final darkwingtm persistent install proof.
- [x] Earlier completed release closeout detail was compacted into [todo/done/rules-release-closeouts.md](todo/done/rules-release-closeouts.md).

---

## 📋 Tasks To Do

### Active / In Progress


### Deferred / Not Selected

- [ ] `memory-context-intelligence` phase 030 darkwingtm reproof after shared-marketplace resolution remains planned / approval-sensitive.
  - Scope: implement the selected shared-marketplace bridge entry, then reprove `memory-context-intelligence@darkwingtm` marketplace availability, install, and uninstall only after explicit action-and-scope approval.
  - Gate: recheck current runtime state, preserve other `darkwingtm` plugins or document an approved rollback/containment path, and avoid install/enable/registry/cache mutation until explicit action-and-scope approval exists.
- [ ] `memory-context-intelligence` phases 017-018 promotion and merge work remains deferred.
  - Scope: phases 001-016 remain completed concept/runtime/readiness work; phases 019-023 remain completed checked-local installability evidence but are transitional under the selected `darkwingtm` namespace basis; phase 024 completed docs-only namespace governance sync; phases 025-027 remain completed historical checked evidence from the temporary/remapped `darkwingtm` state; phase 028 completed docs-only restored shared-marketplace governance sync; phase 029 completed docs-only shared-marketplace bridge design selection; phase 030 remains separate approval-sensitive shared-marketplace bridge/reproof work; phases 017-018 remain separate main RULES promotion/merge work.
  - Gate: use `~/.claude/rules/additional/` as the trial stage before any main RULES merge, but treat phase-013 emission, phase-014 replay output, phase-015 live trial output, phase-016 readiness output, phase-019 planning, phase-020 source-side bootstrap, phase-021 session-only inline load proof, phase-022 local-scope persistent CLI install proof, phase-023 uninstall-only closeout, phase-024 namespace sync, phases 025-027 historical proof, phase-028 governance sync, phase-029 selected design, and phase-030 future bridge/reproof planning as trial material, validation evidence, checked-scope readiness evidence, planning evidence, transitional namespace evidence, historical lifecycle evidence, docs-only governance evidence, selected design evidence, or approval-sensitive future planning only; publication, external marketplace release, slash-command/chat invocation proof, stable or broad production readiness, main RULES promotion, main RULES mutation, and main RULES merge remain unperformed and unselected.
- [ ] Master governance density rollover remains deferred.
  - Scope: large active `changelog/changelog.md` history and release-history-heavy master README/design sections.
  - Gate: open a dedicated repair phase or patch before claiming full active-entrypoint God-document cleanup.
- [ ] Automated validation script for documentation compliance remains deferred by user.
- [ ] Integration testing for design/changelog/rule/TODO integration paths remains deferred by user.

---

## 📜 History

### Active history surfaces

- Daily movement: [todo/history/2026-05-16.md](todo/history/2026-05-16.md)
- Earlier daily movement: [todo/history/2026-05-08.md](todo/history/2026-05-08.md)
- Pre-rollover snapshot: [todo/history/2026-05-08-pre-rollover-TODO.md](todo/history/2026-05-08-pre-rollover-TODO.md)
- Large completed detail shards: [todo/done/rules-release-closeouts.md](todo/done/rules-release-closeouts.md); [todo/done/](todo/done/)
