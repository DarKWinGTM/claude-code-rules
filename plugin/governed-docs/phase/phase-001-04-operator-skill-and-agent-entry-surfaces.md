# P001-04 — operator skill and agent entry surfaces

> **Summary File:** [SUMMARY.md](SUMMARY.md)
> **Phase ID:** P001-04
> **Status:** Completed in checked scope
> **Target Design:** [../design/design.md](../design/design.md) v0.1.0
> **Patch References:** [../patch/operator-skill-and-agent-entry-surfaces.patch.md](../patch/operator-skill-and-agent-entry-surfaces.patch.md)
> **Session:** b7f7ee85-27ec-467a-ba63-568c831fcd36
> **Full history:** [../changelog/changelog.md](../changelog/changelog.md)

---

## Design References

- [04-skills-and-agent-system.design.md](../design/04-skills-and-agent-system.design.md)
- [01-architecture-layers.design.md](../design/01-architecture-layers.design.md)
- [06-action-policy-and-release-gate.design.md](../design/06-action-policy-and-release-gate.design.md)

## Objective

Open the operator-facing skill surfaces and custom-agent entry scaffolds so later runtime behavior can be reached through stable public contracts without widening authority prematurely.

## Why this phase existed

The runtime foundation was useful, but the public/operator entry surfaces were still only design text. This phase turned those entry surfaces into real plugin-owned manifests, skill wrappers, bin routing, and agent scaffolds while keeping the underlying mutation logic bounded by earlier phases.

## Expected Output

- plugin manifest and internal command router surfaces appropriate for the RULES plugin runtime
- skill wrappers for `scan`, `review`, `repair-plan`, `phase-audit`, `release-gate`, and `present-md`
- custom-agent markdown scaffolds for scout / evaluator / repair architect / normalizer / release auditor / phase-lineage auditor
- explicit operator-facing command contract that always requires a target workspace path
- focused verification for wrapper/entry behavior separate from release-ready claims

## Completion Gate

- public/operator entry surfaces exist for the designed commands without reintroducing ambient-cwd fallback
- skill surfaces preserve the explicit target-path requirement in their contract text and runtime invocation
- agent scaffolds keep responsibilities separated and do not imply that findings are proof by themselves
- focused checks prove the wrappers route into the intended internal implementation surfaces

## Out of Scope

- full autonomous agent orchestration
- hidden hook authority
- broad normalization behavior
- release-ready proof that exceeds checked local wrapper/runtime behavior

## Affected Artifacts

Implementation surfaces created:
- `.claude-plugin/plugin.json`
- `bin/governed-docs`
- `src/governed_docs/cli.py`
- `skills/scan/SKILL.md`
- `skills/review/SKILL.md`
- `skills/repair-plan/SKILL.md`
- `skills/phase-audit/SKILL.md`
- `skills/release-gate/SKILL.md`
- `skills/present-md/SKILL.md`
- `agents/governed-docs-scout.md`
- `agents/governed-docs-doctrine-evaluator.md`
- `agents/governed-docs-repair-architect.md`
- `agents/governed-docs-normalizer.md`
- `agents/governed-docs-release-auditor.md`
- `agents/governed-docs-phase-lineage-auditor.md`
- `tests/test_cli_router.py`
- `tests/test_entry_surfaces.py`

## Development Verification / TestKit Coverage

Verification route used: `new_focused_test`

Verification record:
- Ran: `python3 -m unittest discover -s tests -v`
- Result: passed in checked scope
- Covers: CLI routing for scan / repair-plan / present-md, manifest/skill/agent/bin surface existence, explicit operator entry contracts, bin routing to internal implementation surfaces
- Does not cover: executor mutation behavior, release-ready proof, autonomous agent orchestration
- Confidence: verified in checked scope for the operator entry-surface slice

## Risks / Rollback Notes

Contained risks:
- wrapper text drifting from actual runtime behavior
- agent scaffolds implying proof or authority they do not own
- operator entry surfaces introducing cwd fallback by convenience

Containment used:
- explicit path requirement remains visible in every operator-facing surface
- agent outputs remain advisory until the main controller verifies them
- bin router delegates to tested internal Python command surfaces

## Closeout Summary

Delivered result:
- governed-docs now has a plugin manifest, executable router, user-facing skill wrappers, and agent scaffolds in checked scope
- operator entry surfaces route into the intended internal implementation surfaces without ambient-cwd fallback

Impact:
- later policy, release-gate, and article presentation work can be surfaced through stable governed-docs-owned operator contracts

Next phase state:
- P001-05 is completed in checked scope as the bounded executor policy layer
- no later phase requires reopening P001-04
