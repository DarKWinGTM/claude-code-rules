# Phase 042-01 - Correct plugin topology

> **Summary File:** [SUMMARY.md](SUMMARY.md)
> **Phase ID:** 042-01
> **Status:** Completed
> **Design References:** [../design/rules-plugin-extension.design.md](../design/rules-plugin-extension.design.md)
> **Patch References:** [../patch/plugin-topology-correction.patch.md](../patch/plugin-topology-correction.patch.md)

---

## Objective

Correct the plugin split so `claude-code-rules` becomes the session-coordination skill plugin and `rules-compact-extension` remains the compact/context helper.

## Why this phase exists

The earlier skill rollout expanded the RULES plugin package into a broader companion that overlapped the already-active compact helper. This phase removes that overlap and restores a cleaner two-plugin topology.

## Entry conditions / prerequisites

- the shared `darkwingtm` marketplace already exists for the active plugin family
- `rules-compact-extension` is already active and intentionally focused on compact/context continuity
- the bounded patch artifact for this correction already exists

## Action points / execution checklist

- [x] narrow the RULES plugin docs and metadata to skill-only wording
- [x] keep compact-helper ownership with `rules-compact-extension`
- [x] update public install guidance to `claude-code-rules@darkwingtm`
- [x] keep package-local `@claude-code-rules` as local development/testing only
- [x] preserve the two-plugin boundary explicitly in the design/docs layer

## Out of scope

- replacing `rules-compact-extension`
- merging the two plugins into one package in this wave
- activating `claude-peers-mcp` as required infrastructure
- creating a new root runtime rule chain

## Affected artifacts

- `plugin/README.md`
- `plugin/.claude-plugin/plugin.json`
- `plugin/.claude-plugin/marketplace.json`
- `design/rules-plugin-extension.design.md`

## Verification

- [x] `claude-code-rules` is now described as the skill plugin only
- [x] compact-helper ownership remains with `rules-compact-extension`
- [x] public install target is documented as `claude-code-rules@darkwingtm`
- [x] local development path remains explicit and bounded

## Risks / rollback notes

- wording drift could accidentally bring compact-helper claims back into the skill plugin
- rollback should preserve the restored marketplace/plugin family resolution while narrowing wording if needed

## Next possible phases

- `042-02` sync governance/install/release surfaces

## Exit criteria

- [x] the two-plugin topology is clear in the checked source surfaces
- [x] `claude-code-rules` no longer claims compact-helper ownership
- [x] the corrected install target is visible
