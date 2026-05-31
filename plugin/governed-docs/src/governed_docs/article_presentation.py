import hashlib
import html
import re
from dataclasses import dataclass, field
from typing import Dict, List, Tuple
from urllib.parse import urlparse


@dataclass(frozen=True)
class TocItem:
    level: int
    title: str
    anchor: str


@dataclass(frozen=True)
class RenderedArticle:
    doc_key: str
    slug: str
    title: str
    summary: str
    updated_at: str
    published_at: str
    references: List[str]
    content_html: str
    content_toc: List[str]
    full_html: str
    source_rel_path: str


STYLE_BLOCK = """
<style>
.gd-article-layout { display: grid; grid-template-columns: minmax(0, 1fr) 18rem; gap: 2rem; max-width: 1100px; margin: 0 auto; padding: 2rem; font-family: Inter, Arial, sans-serif; color: #e7ecf4; background: #0f172a; }
.gd-article-main { min-width: 0; }
.gd-article-sidebar { position: sticky; top: 1rem; align-self: start; border-left: 1px solid #334155; padding-left: 1rem; }
.gd-article-header h1 { margin-bottom: 0.5rem; }
.gd-article-summary { color: #cbd5e1; margin-bottom: 1rem; }
.gd-article-meta { color: #94a3b8; font-size: 0.95rem; margin-bottom: 1.5rem; }
.gd-article-content { line-height: 1.7; }
.gd-article-content h1, .gd-article-content h2, .gd-article-content h3 { scroll-margin-top: 1rem; }
.gd-article-content pre { background: #111827; padding: 1rem; border-radius: 0.75rem; overflow-x: auto; }
.gd-article-content code { background: rgba(148, 163, 184, 0.15); padding: 0.15rem 0.35rem; border-radius: 0.35rem; }
.gd-article-content table { width: 100%; border-collapse: collapse; margin: 1rem 0; }
.gd-article-content th, .gd-article-content td { border: 1px solid #334155; padding: 0.6rem; text-align: left; }
.gd-article-content blockquote, .gd-callout { border-left: 4px solid #38bdf8; margin: 1rem 0; padding: 0.75rem 1rem; background: rgba(56, 189, 248, 0.08); }
.gd-article-content a { color: #7dd3fc; }
.gd-article-content img { max-width: 100%; border-radius: 0.75rem; }
.gd-toc-title { font-weight: 600; margin-bottom: 0.75rem; }
.gd-toc-list { list-style: none; padding-left: 0; margin: 0; }
.gd-toc-item-level-3 { padding-left: 0.8rem; }
.gd-reference-list { margin-top: 2rem; }
</style>
"""


def safe_url(url: str) -> str:
    parsed = urlparse(url)
    if parsed.scheme in ("", "http", "https", "mailto"):
        lowered = url.strip().lower()
        if lowered.startswith("javascript:") or lowered.startswith("data:"):
            return "#"
        return html.escape(url, quote=True)
    return "#"



def slugify(text: str) -> str:
    base = re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")
    if base:
        return base
    digest = hashlib.sha1(text.encode("utf-8")).hexdigest()[:8]
    return f"section-{digest}"



def parse_frontmatter(markdown_text: str) -> Tuple[Dict[str, str], List[str]]:
    lines = markdown_text.splitlines()
    if len(lines) >= 3 and lines[0].strip() == "---":
        metadata = {}
        body_index = None
        for idx in range(1, len(lines)):
            line = lines[idx]
            if line.strip() == "---":
                body_index = idx + 1
                break
            if ":" in line:
                key, value = line.split(":", 1)
                metadata[key.strip()] = value.strip()
        if body_index is not None:
            return metadata, lines[body_index:]
    return {}, lines



def render_inline(text: str) -> str:
    escaped = html.escape(text)
    escaped = re.sub(r"`([^`]+)`", lambda m: f"<code>{m.group(1)}</code>", escaped)

    def replace_link(match):
        label = match.group(1)
        url = safe_url(match.group(2))
        return f'<a href="{url}">{html.escape(label)}</a>'

    escaped = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", replace_link, escaped)
    return escaped



def build_toc_html(items: List[TocItem]) -> str:
    if not items:
        return '<div class="gd-toc-title">On this page</div><p>No section headings</p>'
    lines = ['<div class="gd-toc-title">On this page</div>', '<ul class="gd-toc-list">']
    for item in items:
        lines.append(
            f'<li class="gd-toc-item-level-{item.level}"><a href="#{item.anchor}">{html.escape(item.title)}</a></li>'
        )
    lines.append('</ul>')
    return ''.join(lines)



def render_markdown_article(markdown_text: str, source_rel_path: str) -> RenderedArticle:
    metadata, lines = parse_frontmatter(markdown_text)
    body_parts: List[str] = []
    toc: List[TocItem] = []
    paragraph_buffer: List[str] = []
    list_buffer: List[str] = []
    quote_buffer: List[str] = []
    code_buffer: List[str] = []
    table_buffer: List[str] = []
    in_code = False

    def flush_paragraph():
        nonlocal paragraph_buffer
        if paragraph_buffer:
            body_parts.append(f"<p>{render_inline(' '.join(paragraph_buffer))}</p>")
            paragraph_buffer = []

    def flush_list():
        nonlocal list_buffer
        if list_buffer:
            items = ''.join(f'<li>{render_inline(item)}</li>' for item in list_buffer)
            body_parts.append(f'<ul>{items}</ul>')
            list_buffer = []

    def flush_quote():
        nonlocal quote_buffer
        if quote_buffer:
            joined = ' '.join(quote_buffer)
            match = re.match(r'^(NOTE|TIP|WARNING):\s*(.*)$', joined, re.IGNORECASE)
            if match:
                body_parts.append(
                    f'<aside class="gd-callout"><strong>{match.group(1).upper()}</strong>: {render_inline(match.group(2))}</aside>'
                )
            else:
                body_parts.append(f'<blockquote>{render_inline(joined)}</blockquote>')
            quote_buffer = []

    def flush_code():
        nonlocal code_buffer
        if code_buffer:
            body_parts.append(
                '<pre><code>' + html.escape('\n'.join(code_buffer)) + '</code></pre>'
            )
            code_buffer = []

    def flush_table():
        nonlocal table_buffer
        if table_buffer:
            header = [cell.strip() for cell in table_buffer[0].strip('|').split('|')]
            rows = [
                [cell.strip() for cell in row.strip('|').split('|')]
                for row in table_buffer[2:]
            ]
            table_html = '<table><thead><tr>' + ''.join(
                f'<th>{render_inline(cell)}</th>' for cell in header
            ) + '</tr></thead><tbody>'
            for row in rows:
                table_html += '<tr>' + ''.join(
                    f'<td>{render_inline(cell)}</td>' for cell in row
                ) + '</tr>'
            table_html += '</tbody></table>'
            body_parts.append(table_html)
            table_buffer = []

    idx = 0
    while idx < len(lines):
        line = lines[idx]
        stripped = line.strip()

        if stripped.startswith('```'):
            flush_paragraph(); flush_list(); flush_quote(); flush_table()
            if in_code:
                flush_code()
                in_code = False
            else:
                in_code = True
            idx += 1
            continue

        if in_code:
            code_buffer.append(line)
            idx += 1
            continue

        if not stripped:
            flush_paragraph(); flush_list(); flush_quote(); flush_table()
            idx += 1
            continue

        heading_match = re.match(r'^(#{1,3})\s+(.*)$', stripped)
        if heading_match:
            flush_paragraph(); flush_list(); flush_quote(); flush_table()
            level = len(heading_match.group(1))
            title = heading_match.group(2).strip()
            anchor = slugify(title)
            body_parts.append(f'<h{level} id="{anchor}">{render_inline(title)}</h{level}>')
            if level in (2, 3):
                toc.append(TocItem(level=level, title=title, anchor=anchor))
            idx += 1
            continue

        if stripped.startswith('- '):
            flush_paragraph(); flush_quote(); flush_table()
            list_buffer.append(stripped[2:])
            idx += 1
            continue

        if stripped.startswith('> '):
            flush_paragraph(); flush_list(); flush_table()
            quote_buffer.append(stripped[2:])
            idx += 1
            continue

        if stripped.startswith('![') and '](' in stripped and stripped.endswith(')'):
            flush_paragraph(); flush_list(); flush_quote(); flush_table()
            alt, url = re.match(r'^!\[([^\]]*)\]\(([^)]+)\)$', stripped).groups()
            body_parts.append(
                f'<figure><img src="{safe_url(url)}" alt="{html.escape(alt)}" />'
                + (f'<figcaption>{html.escape(alt)}</figcaption>' if alt else '')
                + '</figure>'
            )
            idx += 1
            continue

        if '|' in stripped and idx + 1 < len(lines) and re.match(r'^\s*\|?\s*:?-{3,}', lines[idx + 1]):
            flush_paragraph(); flush_list(); flush_quote(); flush_table()
            table_buffer.append(lines[idx])
            table_buffer.append(lines[idx + 1])
            idx += 2
            while idx < len(lines) and '|' in lines[idx]:
                table_buffer.append(lines[idx])
                idx += 1
            flush_table()
            continue

        paragraph_buffer.append(stripped)
        idx += 1

    flush_paragraph(); flush_list(); flush_quote(); flush_table(); flush_code()

    title = metadata.get('title') or 'Untitled governed document'
    summary = metadata.get('summary', '')
    updated_at = metadata.get('updatedAt', '')
    published_at = metadata.get('publishedAt', '')
    references = [item.strip() for item in metadata.get('references', '').split(',') if item.strip()]
    content_html = '\n'.join(body_parts)
    toc_html = build_toc_html(toc)
    source_slug = slugify(source_rel_path.rsplit('/', 1)[-1].replace('.md', ''))
    full_html = f"""<!doctype html>
<html lang=\"en\">
<head>
  <meta charset=\"utf-8\" />
  <meta name=\"viewport\" content=\"width=device-width, initial-scale=1\" />
  <title>{html.escape(title)}</title>
  {STYLE_BLOCK}
</head>
<body>
  <div class=\"gd-article-layout\">
    <main class=\"gd-article-main\">
      <header class=\"gd-article-header\">
        <h1>{html.escape(title)}</h1>
        <p class=\"gd-article-summary\">{html.escape(summary)}</p>
        <div class=\"gd-article-meta\">Updated: {html.escape(updated_at)} Published: {html.escape(published_at)}</div>
      </header>
      <article class=\"gd-article-content\">{content_html}</article>
    </main>
    <aside class=\"gd-article-sidebar\">{toc_html}</aside>
  </div>
</body>
</html>"""
    return RenderedArticle(
        doc_key=f'governed-docs:{source_slug}',
        slug=source_slug,
        title=title,
        summary=summary,
        updated_at=updated_at,
        published_at=published_at,
        references=references,
        content_html=content_html,
        content_toc=[item.title for item in toc],
        full_html=full_html,
        source_rel_path=source_rel_path,
    )
