# Article Markdown Presentation

## 0) Document Control

> **Parent Scope:** governed-docs plugin-local governed design chain
> **Current Version:** 0.1.0
> **Session:** b7f7ee85-27ec-467a-ba63-568c831fcd36 (2026-06-01)
> **Parent Design:** [design.md](design.md)

---

## 1) Goal

Define a governed-docs-owned Markdown-to-HTML article-style presentation path that makes governed Markdown easier to read without transferring ownership to NodeClaw.

## 2) Ownership boundary

The NodeClaw article system is a checked reference input only.

It informs:
- safe Markdown rendering ideas
- article presentation structure
- TOC and metadata contracts
- separation between source ownership and presentation shell

It does **not** transfer ownership of:
- route names
- backend endpoints
- content trees
- database schemas
- CSS class names
- branding
- article identifiers

The implementation owner for this feature remains `plugin/governed-docs`.

## 3) Minimal v1 presentation contract

The smallest useful governed-docs-owned presentation contract should include:
- `docKey`
- `slug`
- `title`
- `summary`
- `updatedAt`
- optional `publishedAt`
- `references`
- `contentHtml`
- `contentToc`

This is enough to present a readable article-style page without inheriting the larger NodeClaw catalog/discovery system.

## 4) Safe rendering boundary

The rendering path should keep a bounded Markdown subset.

Required safe baseline:
- escaped raw HTML by default
- unsafe `javascript:` and `data:` links rejected
- heading anchors generated deterministically
- h2/h3 TOC support
- paragraphs, lists, links, images, code blocks, tables, blockquotes/callouts, and references supported in the initial presentation path

Deferred by default:
- DB catalog sync
- search/filter/pagination
- multi-surface discovery pages
- NodeClaw-specific continuation rails
- marketing/article ownership features unrelated to governed-doc readability

## 5) Frontend/presentation contract

The first governed-docs-owned presentation shell should provide:
- article header with title, summary, and metadata
- article body container fed from `contentHtml`
- sticky or clearly separated TOC area from `contentToc`
- readable typography, code, table, image, and callout styling
- local CSS class namespace that belongs to governed-docs

A single generated article page or preview shell is acceptable for the first implementation. A full app/router is not required.

## 6) Command and path safety

Any user-facing presentation command must still require:
- one explicit target workspace path
- one explicit Markdown source path or selected governed-doc source inside that target
- fail-closed behavior when either path is missing, invalid, or escapes the intended boundary

Ambient cwd must not become article source selection authority.

## 7) Verification orientation

The presentation slice should be considered complete only when:
- governed-docs-owned rendering exists in checked scope
- safe subset behavior is tested
- generated or returned HTML is more readable than raw Markdown
- TOC and article body contract are both present
- no NodeClaw-owned path or owner surface is silently reused as implementation authority

---

> Presentation rule: borrow structure and safety ideas from NodeClaw, but keep rendering ownership, naming, and runtime scope inside governed-docs.
