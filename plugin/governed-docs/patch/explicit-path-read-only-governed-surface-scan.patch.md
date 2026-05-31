# governed-docs explicit-path read-only governed surface scan patch

> **Current Version:** 0.1.0
> **Session:** b7f7ee85-27ec-467a-ba63-568c831fcd36
> **Status:** Implemented / Checked-scope verified
> **Target Design:** [../design/design.md](../design/design.md) v0.1.0
> **Full history:** [../changelog/changelog.md](../changelog/changelog.md)

---

## Context

This patch captures the first real implementation slice for `governed-docs` after the design-chain bootstrap.

The selected bounded slice is: explicit target-path validation plus a read-only governed-surface scan foundation.

## Analysis

Before this slice:
- the plugin had only design-time governed docs
- no runtime code existed for path validation, scan models, scanner behavior, or command entry
- the explicit target-path doctrine existed only in design text

After this slice:
- the doctrine now exists as checked runtime behavior in a local read-only scan foundation
- the first runtime path remains intentionally narrow and non-mutating
- later evaluator / repair / normalize / release-gate work can build on stable inventory output instead of chat-only design intent

## Change Items

### 1) Add explicit target-path validation
- **Target artifact:** `src/governed_docs/target_path.py`
- **Change type:** additive
- **Before state:** no runtime path gate existed
- **After state:** missing, non-existent, and file-path targets hard-stop before any scan begins

### 2) Add scan result and surface scanner foundation
- **Target artifact:** `src/governed_docs/scan_result.py`, `src/governed_docs/surface_scanner.py`
- **Change type:** additive
- **Before state:** no runtime inventory model or read-only governed surface scan existed
- **After state:** the plugin can inventory the named target path and classify the current minimal governed surface foundation without mutating files

### 3) Add report-only command entry point
- **Target artifact:** `src/governed_docs/commands/scan.py`
- **Change type:** additive
- **Before state:** no executable scan command contract existed
- **After state:** a report-only internal command can run with one explicit target path and clearly state that no files were edited

### 4) Add focused tests for the first slice
- **Target artifact:** `tests/test_target_path.py`, `tests/test_surface_scanner.py`, `tests/test_scan_command.py`
- **Change type:** additive
- **Before state:** no regression or contract tests existed for the target-path and scanner boundary
- **After state:** focused tests prove the hard-stop boundary, no ambient-cwd fallback, inactive history/done classification, and report-only command behavior

## Verification

Checked verification for this patch:
- `python3 -m unittest discover -s tests -v` → 9 tests passed
- `PYTHONPATH=src python3 -m governed_docs.commands.scan /home/node/workplace/AWCLOUD/TEMPLATE/RULES/plugin/governed-docs` → report-only scan output, no file edits
- `PYTHONPATH=src python3 -m governed_docs.commands.scan` → exit code 1 and explicit target-path error

Covers:
- explicit target path hard-stop behavior
- read-only governed-surface inventory foundation
- no ambient-cwd fallback in checked scope
- report-only command wording in checked scope

Does not cover:
- deep doctrine evaluation
- repair planning
- normalization/executor behavior
- hook wiring
- skill/manifest installation
- article-style Markdown HTML presentation

## Rollback approach

If this slice needs containment or partial rollback:
- keep the design-chain governance docs as the stronger semantic source of truth
- retain the explicit target-path gate even if scanner scope needs narrowing
- reduce the scanner back to top-level governed surface inventory only rather than widening into mutation behavior
- do not promote any rollback into evaluator / normalize / hook work inside this patch
