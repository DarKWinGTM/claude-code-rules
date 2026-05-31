from pathlib import Path
from typing import Optional, Union

from governed_docs.article_presentation import render_markdown_article
from governed_docs.target_path import resolve_target_workspace_path


class PresentMdPathError(ValueError):
    """Raised when the article Markdown source path is missing or escapes the workspace boundary."""



def resolve_markdown_source(workspace_path: Path, source_rel_path: str) -> Path:
    if not source_rel_path or not source_rel_path.strip():
        raise PresentMdPathError('An explicit Markdown source path is required.')

    candidate = Path(source_rel_path)
    if candidate.is_absolute() or '..' in candidate.parts:
        raise PresentMdPathError('Markdown source path must stay inside the target workspace.')

    source_path = (workspace_path / candidate).resolve()
    try:
        source_path.relative_to(workspace_path)
    except ValueError as exc:
        raise PresentMdPathError('Markdown source path escapes the target workspace.') from exc

    if not source_path.exists() or not source_path.is_file() or source_path.suffix != '.md':
        raise PresentMdPathError(f'Checked Markdown source was not found: {source_path}')

    return source_path



def run_present_md_command(
    target_workspace_path: Optional[Union[str, Path]], source_rel_path: str
) -> str:
    workspace_path = resolve_target_workspace_path(target_workspace_path)
    source_path = resolve_markdown_source(workspace_path, source_rel_path)
    markdown_text = source_path.read_text(encoding='utf-8')
    rendered = render_markdown_article(markdown_text, source_rel_path=source_rel_path)

    output_dir = workspace_path / 'generated' / 'article-preview'
    output_dir.mkdir(parents=True, exist_ok=True)
    output_path = output_dir / f'{rendered.slug}.html'
    output_path.write_text(rendered.full_html, encoding='utf-8')

    return (
        'Article preview generated\n'
        f'Source: {source_rel_path}\n'
        f'Output: {output_path}\n'
        'No governed files were edited.'
    )
