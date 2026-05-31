# P002-01 — preview path and present-md refactor

> **Summary File:** [SUMMARY.md](SUMMARY.md)
> **Phase ID:** P002-01
> **Status:** Completed in checked scope
> **Target Design:** [../design/design.md](../design/design.md) v0.1.0
> **Patch References:** [../patch/preview-portal-and-sync-wave.patch.md](../patch/preview-portal-and-sync-wave.patch.md)
> **Session:** b7f7ee85-27ec-467a-ba63-568c831fcd36
> **Full history:** [../changelog/changelog.md](../changelog/changelog.md)

## Objective

Change `present-md` from `generated/article-preview/<slug>.html` to the new root `preview/` family-aware path contract.

## Completion Gate

- `present-md` writes to `preview/<family>/<slug>/index.html` or the selected single-page family path
- docs/tests are updated
- `.gitignore` no longer relies on `generated/` alone for preview output
- command remains explicit-path only and fail-closed

## Verification

- focused tests passed for design preview path and TODO preview path
- CLI router test for `present-md` passed
- smoke check wrote `preview/design/07-article-markdown-presentation/index.html`

## Closeout Summary

Delivered result:
- `present-md` now writes to root `preview/` instead of `generated/article-preview/`
- path mapping is family-aware through preview-target resolution
