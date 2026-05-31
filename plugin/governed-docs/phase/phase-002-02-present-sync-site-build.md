# P002-02 — present-sync site build

> **Summary File:** [SUMMARY.md](SUMMARY.md)
> **Phase ID:** P002-02
> **Status:** Completed in checked scope
> **Target Design:** [../design/design.md](../design/design.md) v0.1.0
> **Patch References:** [../patch/preview-portal-and-sync-wave.patch.md](../patch/preview-portal-and-sync-wave.patch.md)
> **Session:** b7f7ee85-27ec-467a-ba63-568c831fcd36
> **Full history:** [../changelog/changelog.md](../changelog/changelog.md)

## Objective

Implement the full preview-site sync path: source inventory, `preview/manifest.json`, `preview/index.html`, family pages, and stale-page pruning.

## Completion Gate

- `present-sync` exists and is routable from the CLI
- all selected families are inventoried
- manifest + index are generated
- stale preview pages are pruned safely inside `preview/**`

## Verification

- focused `present-sync` tests passed for site build, manifest generation, stale-page pruning, and no-source-rewrite behavior
- CLI router test for `present-sync` passed
- smoke check generated `preview/index.html` and `preview/manifest.json`

## Closeout Summary

Delivered result:
- governed-docs now has a real `present-sync` command and preview-site sync engine
- the sync path inventories governed source families and rebuilds the portal inside `preview/**`
