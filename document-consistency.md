# Document consistency and cross-reference validation

> **Current Version:** 1.1
> **Design:** [design/document-consistency.design.md](design/document-consistency.design.md) v1.0

## Rules
- Keep names, paths, identifiers, and terminology consistent across the whole response.
- When you reference something (file, symbol, command, config), ensure it exists or mark it as unknown/unverified using appropriate tools (Read/Ls/Grep).
- If a change impacts multiple sections/files, describe the dependencies and update all affected references.

## Verification Standards (Mandatory)
When referencing files, symbols, or configs, use these status labels:
- ✅ **Verified:** Confirmed existence via tool execution.
- ⚠️ **Unverified:** Not checked or uncertain.
- ❌ **Not Found:** Confirmed missing.

## Output standard
- Prefer precise references (file paths, identifiers) over vague descriptions.

> Full history: [changelog/document-consistency.changelog.md](changelog/document-consistency.changelog.md)
