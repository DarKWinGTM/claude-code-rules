# Phase 041-02 - Sync session coordination skill surfaces

> **Summary File:** [SUMMARY.md](SUMMARY.md)
> **Phase ID:** 041-02
> **Status:** Completed
> **Design References:** [../design/design.md](../design/design.md), [../design/rules-plugin-extension.design.md](../design/rules-plugin-extension.design.md)
> **Patch References:** [../patch/session-coordination-bridge-skill-rollout.patch.md](../patch/session-coordination-bridge-skill-rollout.patch.md)

---

## Objective

Synchronize master RULES surfaces and release/update flow after adding the optional session coordination support skill to the plugin companion.

## Why this phase exists

The skill rollout only becomes operationally coherent when the master design, README, TODO, changelog, and phase summary all describe the same plugin identity, support-skill boundary, and migration path from the older compact-only package label.

## Entry conditions / prerequisites

- `041-01` is materially complete
- the bounded patch artifact for this rollout already exists
- the active root runtime rule count should remain unchanged at 40

## Action points / execution checklist

- [x] update `design/design.md`
- [x] update `README.md`
- [x] update `TODO.md`
- [x] update `changelog/changelog.md`
- [x] update `phase/SUMMARY.md`
- [x] update `changelog/rules-plugin-extension.changelog.md`
- [x] perform final consistency sweep for plugin identity + skill boundary wording
- [x] verify install/update/uninstall guidance before release

## Out of scope

- changing the active root runtime rule count
- creating another first-class rule chain
- activating peer signaling as required infrastructure
- moving compact semantics out of the existing hook path

## Affected artifacts

- `design/design.md`
- `README.md`
- `TODO.md`
- `changelog/changelog.md`
- `phase/SUMMARY.md`
- `changelog/rules-plugin-extension.changelog.md`
- release/update workflow notes for the plugin companion

## Verification

- [x] master surfaces record wave `041` coherently
- [x] plugin companion wording now includes both compact hooks and the session coordination support skill
- [x] install/update guidance now uses `claude-code-rules@claude-code-rules`
- [x] migration guidance for older installs is visible where needed
- [x] root docs still keep the plugin in the optional support layer rather than semantic authority

## Risks / rollback notes

- sync drift can survive even when the plugin files themselves are correct
- rollback should restore wording carefully without losing the recorded rollout history
- preserve the bounded phase/patch history instead of silently erasing wave `041`

## Next possible phases

- none required once sync, audit, and release are complete

## Exit criteria

- [x] repository-level governance reflects the session coordination skill rollout coherently
- [x] plugin identity and migration wording are synchronized across source surfaces
- [x] the `041` phase family is visible and reviewable from `phase/SUMMARY.md`
