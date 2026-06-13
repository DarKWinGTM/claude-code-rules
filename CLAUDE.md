# CLAUDE.md — RULES Project Maintainer Contract

This file defines project-local working rules for `/home/node/workplace/AWCLOUD/TEMPLATE/RULES`.

## Core rule
For every RULES improvement wave, normal governed sync is not enough by itself. A wave is **not done** until all of the following are completed in checked scope:
1. **Update README** — sync current-state/version/install/release-facing README content with the shipped source truth.
2. **Install Rules** — install the active runtime rule set from the checked source repo into the intended runtime target and verify the installed result.
3. **Git push update** — commit the scoped source changes and push them to the source repository.
4. **Git repo release** — create the corresponding git tag / GitHub repo release for that pushed wave.

## Required interpretation
- Do not claim a RULES wave is complete if any of the four closeout steps above is missing.
- If push or release is blocked by auth, remote state, network, or branch safety, report the wave as blocked rather than done.
- Keep the usual RULES governance order active: design → runtime rule → changelog → TODO/phase/patch when those surfaces are in scope.
- The four closeout steps above are an additional maintainer completion gate, not a replacement for existing governed sync.
- When install is in scope, verify source/runtime parity and body sufficiency rather than assuming copied files are correct.
- Keep README current enough that the published repo front page matches the released runtime/install state.
