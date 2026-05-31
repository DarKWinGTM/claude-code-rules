# Stale-session diagnostic safeguard patch

> **Current Version:** 0.1.67
> **Session:** d42465eb-30a7-4bc8-b9d6-03e52306e9a5 (2026-05-30)
> **Status:** Phase 063 completed stale-session diagnostic safeguard in checked scope
> **Target Design:** [../design/design.md](../design/design.md) v0.1.67
> **Full history:** [../changelog/changelog.md](../changelog/changelog.md)

---

## 1) Context

The checked diagnosis after phase 062 showed that the strongest remaining reading was a freshness mismatch between a long-lived session and a newer installed plugin update. The operator contract still lacked a dedicated diagnostic path that could tell the user this session may be stale without treating restart as the actual fix.

## 2) Analysis

The repair needed here is additive, not structural. The existing historical-first analysis flow, repeated topic-card output, slash-request contract, and `Next action options` bridge all stay valid. The missing piece is one bounded advisory warning that appears only when checked freshness evidence supports a mismatch.

## 3) Change items

### 3.1 Advisory stale-session warning
- **Target artifact:** `../lib/analysis_surface.py`, `../tests/test_analysis_surface.py`
- **Change type:** additive
- **Before:** the runtime payload had no dedicated stale-session safeguard; long-lived freshness mismatch could not be surfaced directly to the operator
- **After:** the runtime payload can append one advisory `stale_long_lived_session` warning when checked transcript/session freshness evidence shows the current session predates the installed plugin update

### 3.2 Manifest registration repair
- **Target artifact:** `../.claude-plugin/plugin.json`, `../tests/test_plugin_manifest.py`
- **Change type:** replacement/additive
- **Before:** the source manifest became invalid JSON after the version bump to `0.9.22`, the active installed cache mirrored the malformed manifest, and fresh installed-local slash proof regressed to `Unknown command`
- **After:** the source manifest is valid JSON again, the manifest-validity test guards the file directly, and fresh installed-local slash registration can succeed again after plugin refresh

### 3.3 Public contract update
- **Target artifact:** `../skills/analysis/SKILL.md`
- **Change type:** additive
- **Before:** the skill contract described slash-request hardening and post-topic options, but not the temporary stale-session warning path
- **After:** the skill contract now says the operator may see `possible stale long-lived session`, restart is diagnostic only, and session-dependent no-response remains a bug rather than acceptable normal behavior

### 3.4 Governed sync
- **Target artifact:** `../README.md`, `../design/design.md`, `../design/02-topic-list-and-choice-flow.design.md`, `../phase/SUMMARY.md`, `../phase/phase-063-stale-session-diagnostic-safeguard.md`, `../changelog/changelog.md`, `../changelog/v0.1.67-completed-stale-session-diagnostic-safeguard.changelog.md`, `/home/node/workplace/AWCLOUD/TEMPLATE/RULES/TODO.md`, and `../.claude-plugin/plugin.json`
- **Change type:** replacement/additive
- **Before:** active docs stopped at phase 062 slash-request hardening and did not describe the additive stale-session safeguard wave or the manifest-registration repair that was required to restore fresh installed-local slash proof
- **After:** active docs now describe phase 063 as a separate temporary diagnostic wave, record the manifest-registration repair, and bump the source package to `0.9.22`

## 4) Verification

- focused RED/GREEN proof for advisory `stale_long_lived_session` emission when checked freshness evidence shows the current session predates the installed plugin update
- focused RED/GREEN proof that missing freshness evidence does not fabricate the warning
- focused RED/GREEN proof that the warning does not normalize status or replace topic-card / `Next action options` output
- focused RED/GREEN proof that the source manifest is valid JSON again at `0.9.22`
- focused skill-contract proof that restart remains a temporary diagnostic step and not the final fix
- focused suite passed with `35` checks
- full runtime/source suite passed with `86` tests
- fresh installed-local `/memory-context-intelligence:analysis` registration was reproved after the manifest repair
- targeted installed-cache `analysis-surface --session-id d42465eb-30a7-4bc8-b9d6-03e52306e9a5` proof showed the advisory stale-session warning while preserving normal output

## 5) Rollback approach

If this safeguard is rolled back, remove the additive stale-session warning path only while keeping historical-first scope, repeated topic cards, slash-request hardening, and the advisory post-topic action bridge intact unless a broader rollback is explicitly selected.
