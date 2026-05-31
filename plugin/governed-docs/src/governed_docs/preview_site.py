import html
import json
import shutil
from dataclasses import asdict, dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, List

from governed_docs.article_presentation import render_markdown_article
from governed_docs.preview_paths import resolve_preview_target


@dataclass(frozen=True)
class PreviewDocumentRecord:
    family: str
    source_rel_path: str
    slug: str
    title: str
    summary: str
    updated_at: str
    output_rel_path: str
    status: str


@dataclass(frozen=True)
class PreviewSyncResult:
    preview_root: Path
    manifest_path: Path
    index_path: Path
    documents: List[PreviewDocumentRecord]



def _sorted_unique_paths(paths: List[Path], workspace_path: Path) -> List[Path]:
    seen = set()
    unique: List[Path] = []
    for path in paths:
        rel = path.relative_to(workspace_path).as_posix()
        if rel in seen:
            continue
        seen.add(rel)
        unique.append(path)
    return sorted(unique, key=lambda item: item.relative_to(workspace_path).as_posix())



def collect_preview_sources(workspace_path: Path) -> List[Path]:
    sources: List[Path] = []

    design_root = workspace_path / 'design'
    if design_root.exists():
        sources.extend(path for path in design_root.glob('*.design.md') if path.is_file())

    changelog_root = workspace_path / 'changelog'
    if (changelog_root / 'changelog.md').exists():
        sources.append(changelog_root / 'changelog.md')
    if changelog_root.exists():
        sources.extend(path for path in changelog_root.glob('*.changelog.md') if path.is_file())
        sources.extend(
            path for path in changelog_root.rglob('*.changelog.md')
            if path.is_file() and 'done' not in path.parts
        )

    todo_path = workspace_path / 'TODO.md'
    if todo_path.exists():
        sources.append(todo_path)

    phase_root = workspace_path / 'phase'
    if (phase_root / 'SUMMARY.md').exists():
        sources.append(phase_root / 'SUMMARY.md')
    if phase_root.exists():
        sources.extend(path for path in phase_root.glob('phase-*.md') if path.is_file())

    patch_root = workspace_path / 'patch'
    if patch_root.exists():
        sources.extend(path for path in patch_root.glob('*.patch.md') if path.is_file())

    return _sorted_unique_paths(sources, workspace_path)



def build_preview_manifest(workspace_path: Path, documents: List[PreviewDocumentRecord]) -> Dict[str, object]:
    return {
        'workspacePath': str(workspace_path),
        'generatedAt': datetime.now(timezone.utc).isoformat(),
        'portalTitle': 'governed-docs preview portal',
        'documents': [asdict(document) for document in documents],
    }



def render_preview_index_html(documents: List[PreviewDocumentRecord], manifest: Dict[str, object]) -> str:
    grouped: Dict[str, List[PreviewDocumentRecord]] = {}
    for document in documents:
        grouped.setdefault(document.family, []).append(document)

    nav_items = ''.join(
        f'<li><a href="#family-{html.escape(family)}">{html.escape(family.title())}</a></li>'
        for family in grouped.keys()
    )

    section_html = []
    for family, items in grouped.items():
        cards = []
        for item in items:
            summary = html.escape(item.summary or 'No summary provided yet.')
            cards.append(
                '<article class="gd-preview-card">'
                f'<h3><a href="{html.escape(item.output_rel_path)}">{html.escape(item.title)}</a></h3>'
                f'<p class="gd-preview-summary">{summary}</p>'
                f'<div class="gd-preview-meta">{html.escape(item.source_rel_path)}</div>'
                '</article>'
            )
        section_html.append(
            f'<section id="family-{html.escape(family)}" class="gd-preview-section">'
            f'<h2>{html.escape(family.title())}</h2>'
            '<div class="gd-preview-grid">' + ''.join(cards) + '</div>'
            '</section>'
        )

    generated_at = html.escape(str(manifest['generatedAt']))
    document_count = len(documents)

    return f"""<!doctype html>
<html lang=\"en\">
<head>
  <meta charset=\"utf-8\" />
  <meta name=\"viewport\" content=\"width=device-width, initial-scale=1\" />
  <title>governed-docs preview portal</title>
  <style>
    :root {{
      color-scheme: light dark;
      --bg: #f8fafc;
      --panel: #ffffff;
      --border: #dbe4f0;
      --text: #1e293b;
      --muted: #64748b;
      --link: #2563eb;
      --accent: #f97316;
      --shadow: 0 10px 30px rgba(15, 23, 42, 0.08);
    }}
    body {{ margin: 0; font-family: Inter, Arial, sans-serif; background: var(--bg); color: var(--text); }}
    a {{ color: var(--link); text-decoration: none; }}
    a:hover {{ text-decoration: underline; }}
    .gd-skip {{ position: absolute; left: -999px; top: 0; }}
    .gd-skip:focus {{ left: 1rem; top: 1rem; background: #fff; border: 1px solid var(--border); padding: 0.75rem 1rem; z-index: 100; }}
    .gd-shell {{ display: grid; grid-template-columns: 17rem minmax(0, 1fr); min-height: 100dvh; }}
    .gd-sidebar {{ position: sticky; top: 0; align-self: start; height: 100dvh; padding: 1.5rem; border-right: 1px solid var(--border); background: rgba(255,255,255,0.88); backdrop-filter: blur(10px); }}
    .gd-brand {{ font-size: 1.1rem; font-weight: 700; margin-bottom: 0.5rem; }}
    .gd-tag {{ display: inline-block; margin-bottom: 1rem; color: var(--accent); font-size: 0.9rem; font-weight: 600; }}
    .gd-search {{ width: 100%; box-sizing: border-box; padding: 0.85rem 0.95rem; border-radius: 0.8rem; border: 1px solid var(--border); background: #fff; margin-bottom: 1rem; }}
    .gd-nav {{ list-style: none; padding: 0; margin: 0; display: grid; gap: 0.55rem; }}
    .gd-content {{ padding: 2rem; }}
    .gd-hero {{ background: linear-gradient(180deg, #ffffff 0%, #f8fafc 100%); border: 1px solid var(--border); border-radius: 1.25rem; padding: 1.5rem; box-shadow: var(--shadow); margin-bottom: 1.5rem; }}
    .gd-hero h1 {{ margin: 0 0 0.5rem; font-size: 2rem; }}
    .gd-hero p {{ margin: 0; max-width: 70ch; line-height: 1.6; color: var(--muted); }}
    .gd-status {{ margin-top: 1rem; display: flex; flex-wrap: wrap; gap: 0.75rem; color: var(--muted); font-size: 0.95rem; }}
    .gd-preview-section {{ margin-top: 2rem; }}
    .gd-preview-grid {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(240px, 1fr)); gap: 1rem; }}
    .gd-preview-card {{ background: var(--panel); border: 1px solid var(--border); border-radius: 1rem; padding: 1rem; box-shadow: var(--shadow); }}
    .gd-preview-card h3 {{ margin-top: 0; margin-bottom: 0.5rem; }}
    .gd-preview-summary {{ color: var(--muted); line-height: 1.55; min-height: 3rem; }}
    .gd-preview-meta {{ color: var(--muted); font-size: 0.9rem; margin-top: 0.75rem; }}
    @media (max-width: 960px) {{
      .gd-shell {{ grid-template-columns: 1fr; }}
      .gd-sidebar {{ position: static; height: auto; border-right: 0; border-bottom: 1px solid var(--border); }}
      .gd-content {{ padding: 1rem; }}
    }}
  </style>
</head>
<body>
  <a class=\"gd-skip\" href=\"#main-content\">Skip to main content</a>
  <div class=\"gd-shell\">
    <aside class=\"gd-sidebar\">
      <div class=\"gd-brand\">governed-docs</div>
      <div class=\"gd-tag\">Preview portal</div>
      <input class=\"gd-search\" type=\"search\" placeholder=\"Search is reserved for a later wave\" aria-label=\"Reserved search field\" />
      <ul class=\"gd-nav\">{nav_items}</ul>
    </aside>
    <main id=\"main-content\" class=\"gd-content\">
      <section class=\"gd-hero\">
        <h1>governed-docs preview portal</h1>
        <p>Readable web presentation for governed documentation families. This portal is a support surface only; source authority remains in the governed Markdown and document files.</p>
        <div class=\"gd-status\">
          <span>Documents: {document_count}</span>
          <span>Synced at: {generated_at}</span>
        </div>
      </section>
      {''.join(section_html)}
    </main>
  </div>
</body>
</html>"""



def sync_preview_site(workspace_path: Path) -> PreviewSyncResult:
    preview_root = workspace_path / 'preview'
    if preview_root.exists():
        shutil.rmtree(preview_root)

    documents: List[PreviewDocumentRecord] = []
    for source_path in collect_preview_sources(workspace_path):
        source_rel_path = source_path.relative_to(workspace_path).as_posix()
        rendered = render_markdown_article(
            source_path.read_text(encoding='utf-8'),
            source_rel_path=source_rel_path,
        )
        preview_target = resolve_preview_target(source_rel_path)
        output_path = workspace_path / preview_target.output_rel_path
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(rendered.full_html, encoding='utf-8')

        documents.append(
            PreviewDocumentRecord(
                family=preview_target.family,
                source_rel_path=source_rel_path,
                slug=preview_target.slug,
                title=rendered.title,
                summary=rendered.summary,
                updated_at=rendered.updated_at,
                output_rel_path=preview_target.output_rel_path.as_posix(),
                status='synced',
            )
        )

    manifest = build_preview_manifest(workspace_path, documents)
    manifest_path = preview_root / 'manifest.json'
    manifest_path.parent.mkdir(parents=True, exist_ok=True)
    manifest_path.write_text(json.dumps(manifest, indent=2, ensure_ascii=False), encoding='utf-8')

    index_path = preview_root / 'index.html'
    index_path.write_text(render_preview_index_html(documents, manifest), encoding='utf-8')

    return PreviewSyncResult(
        preview_root=preview_root,
        manifest_path=manifest_path,
        index_path=index_path,
        documents=documents,
    )
