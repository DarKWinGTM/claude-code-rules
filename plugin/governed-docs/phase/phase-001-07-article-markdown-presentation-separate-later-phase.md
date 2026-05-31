# P001-07 — article Markdown presentation separate later phase

> **Summary File:** [SUMMARY.md](SUMMARY.md)
> **Phase ID:** P001-07
> **Status:** Completed in checked scope
> **Target Design:** [../design/design.md](../design/design.md) v0.1.0
> **Patch References:** [../patch/article-markdown-presentation.patch.md](../patch/article-markdown-presentation.patch.md)
> **Session:** b7f7ee85-27ec-467a-ba63-568c831fcd36
> **Full history:** [../changelog/changelog.md](../changelog/changelog.md)

---

## Design References

- [07-article-markdown-presentation.design.md](../design/07-article-markdown-presentation.design.md)
- [04-skills-and-agent-system.design.md](../design/04-skills-and-agent-system.design.md)
- [05-generated-artifacts-and-hook-posture.design.md](../design/05-generated-artifacts-and-hook-posture.design.md)

## Reference Basis

This slice used checked NodeClaw article behavior as reference input only.

Preserved boundary:
- ownership of the current implementation stays inside `governed-docs`
- NodeClaw was not treated as a source-owned implementation surface for this plugin-local chain

## Objective

Implement a governed-docs-owned Markdown → article-style HTML presentation path so governed sources can be rendered as easier-to-read article previews without collapsing presentation logic into semantic-governance authority.

## Why this stayed separate

This work adds rendering, sanitization, metadata, TOC generation, preview output, and operator-facing presentation concerns. Keeping it separate from the earlier maintenance-runtime layers preserved a cleaner boundary between doctrine maintenance and presentation behavior.

## Expected Output

- governed-docs-specific article presentation design
- safe Markdown subset and sanitizer behavior
- content metadata contract
- TOC / heading / link / image / code-block rendering behavior
- operator command surface for preview generation
- focused tests for unsafe links, unsupported path escape, and preview output

## Completion Gate

- a checked governed-docs-specific presentation design exists
- the render path is clearly separated from semantic-governance authority
- security-sensitive Markdown handling has an explicit bounded policy
- focused tests and a real command smoke check prove the local preview path works in checked scope

## Out of Scope

- reuse of NodeClaw ownership surfaces as implementation owner
- public hosting or deployment of rendered article pages
- a full content-management workflow
- hidden mutation of governed sources during preview generation

## Affected Artifacts

Design and implementation surfaces created or updated:
- `design/07-article-markdown-presentation.design.md`
- `src/governed_docs/article_presentation.py`
- `src/governed_docs/commands/present_md.py`
- `src/governed_docs/cli.py`
- `skills/present-md/SKILL.md`
- `tests/test_article_presentation.py`
- `tests/test_present_md_command.py`
- `tests/test_cli_router.py`

Generated runtime output verified in checked local scope:
- `generated/article-preview/07-article-markdown-presentation-design.html`

Governed sync surfaces updated:
- `README.md`
- `TODO.md`
- `phase/SUMMARY.md`
- `changelog/changelog.md`
- `patch/article-markdown-presentation.patch.md`

## Development Verification / TestKit Coverage

Verification route used: `new_focused_test`

Verification record:
- Ran: `python3 -m unittest discover -s tests -v`
- Ran: `./bin/governed-docs present-md /home/node/workplace/AWCLOUD/TEMPLATE/RULES/plugin/governed-docs design/07-article-markdown-presentation.design.md`
- Result: 40 tests passed; the command generated `generated/article-preview/07-article-markdown-presentation-design.html` and reported `No governed files were edited.`
- Covers: safe-link blocking, TOC generation, full HTML rendering, preview output writing, source-path containment, and command routing in checked local scope
- Does not cover: public deployment, browser hosting, or broader editorial workflows outside the local preview path
- Confidence: verified in checked scope for the article-presentation slice

## Risks / Rollback Notes

Contained risks:
- unsafe Markdown/HTML handling
- mixing presentation logic into governance authority
- drifting from governed-docs ownership into borrowed product ownership

Containment used:
- unsafe schemes such as `javascript:` and `data:` are blocked in rendered links
- the preview command accepts only sources inside the named target workspace
- output is written as a generated preview artifact, not as a silent rewrite of governed sources

## Closeout Summary

Delivered result:
- governed-docs now has its own article-style Markdown presentation design, renderer, and `present-md` operator path in checked scope
- the preview path produces local generated HTML with TOC support and bounded sanitization behavior

Impact:
- governed documents can now be previewed in a more readable article form without changing semantic ownership of the governed source set

Next phase state:
- no open phase remains in the current P001 program
