# P002 — preview portal and sync wave

> **Summary File:** [SUMMARY.md](SUMMARY.md)
> **Phase ID:** P002
> **Status:** Completed in checked scope
> **Target Design:** [../design/design.md](../design/design.md) v0.1.0
> **Patch References:** [../patch/preview-portal-and-sync-wave.patch.md](../patch/preview-portal-and-sync-wave.patch.md)
> **Session:** b7f7ee85-27ec-467a-ba63-568c831fcd36
> **Full history:** [../changelog/changelog.md](../changelog/changelog.md)

---

## Design References

- [07-article-markdown-presentation.design.md](../design/07-article-markdown-presentation.design.md)
- [08-preview-portal-and-sync.design.md](../design/08-preview-portal-and-sync.design.md)
- [05-generated-artifacts-and-hook-posture.design.md](../design/05-generated-artifacts-and-hook-posture.design.md)

## Objective

Replace the current single-file article preview output with a root `preview/` portal and sync layer that can keep governed presentation pages aligned for `design/`, `changelog/`, `TODO.md`, `phase/`, and `patch/`.

## Why this was a new major phase

P001 closed the first governed-docs implementation program.

P002 was a distinct rollout family because it changed:
- the preview path contract
- the presentation architecture
- the operator command surface
- the rendered information architecture
- the sync model across multiple governed families

## Expected Output

- root `preview/` portal contract
- `present-md` refactored to the new path shape
- new `present-sync` command and inventory/manifest flow
- preview portal shell and helper subagents
- focused verification and governed-surface sync for the new wave

## Lane map

- **P002-01** — refactor present-md output path and single-doc contract
- **P002-02** — implement present-sync inventory + manifest + bounded site sync
- **P002-03** — add preview subagents and portal UI shell
- **P002-04** — verify, smoke-test, and sync governed surfaces

## Completion Gate

P002 closes only when all P002 subphases complete and the final proof route confirms:
- mutations stay inside `preview/**`
- source docs are not rewritten
- portal index and manifest exist
- all selected families are synced in checked scope

## Closeout Summary

Delivered result:
- governed-docs now has a root `preview/` portal model instead of the old `generated/article-preview/` output contract
- `present-md` remains the single-document renderer, while `present-sync` rebuilds the full preview portal in checked scope
- helper present-layer subagents and a readable portal shell now exist in checked scope

Impact:
- governed docs can now be presented as a family-aware web portal while keeping semantic authority in the source docs
- preview rebuilds are bounded to `preview/**` and are verified not to rewrite selected governed source docs

Verification basis:
- full suite passed with 45 tests
- `present-md` smoke check wrote to root `preview/`
- `present-sync` smoke check generated `preview/index.html` and `preview/manifest.json`
- hash comparison over selected governed sources stayed unchanged across `present-sync`
