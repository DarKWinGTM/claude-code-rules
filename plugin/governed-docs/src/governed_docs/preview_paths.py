from dataclasses import dataclass
from pathlib import PurePosixPath


@dataclass(frozen=True)
class PreviewTarget:
    family: str
    slug: str
    output_rel_path: PurePosixPath


KNOWN_SUFFIXES = (
    '.design.md',
    '.changelog.md',
    '.patch.md',
    '.md',
)


def strip_known_suffix(filename: str) -> str:
    for suffix in KNOWN_SUFFIXES:
        if filename.endswith(suffix):
            return filename[: -len(suffix)]
    return filename



def resolve_preview_target(source_rel_path: str) -> PreviewTarget:
    source_path = PurePosixPath(source_rel_path)
    parts = source_path.parts
    filename_slug = strip_known_suffix(source_path.name)

    if source_path == PurePosixPath('TODO.md'):
        return PreviewTarget(
            family='todo',
            slug='todo',
            output_rel_path=PurePosixPath('preview/todo/index.html'),
        )

    if source_path == PurePosixPath('phase/SUMMARY.md'):
        return PreviewTarget(
            family='phase',
            slug='phase',
            output_rel_path=PurePosixPath('preview/phase/index.html'),
        )

    if parts and parts[0] == 'design':
        return PreviewTarget(
            family='design',
            slug=filename_slug,
            output_rel_path=PurePosixPath('preview') / 'design' / filename_slug / 'index.html',
        )

    if parts and parts[0] == 'changelog':
        return PreviewTarget(
            family='changelog',
            slug=filename_slug,
            output_rel_path=PurePosixPath('preview') / 'changelog' / filename_slug / 'index.html',
        )

    if parts and parts[0] == 'phase':
        return PreviewTarget(
            family='phase',
            slug=filename_slug,
            output_rel_path=PurePosixPath('preview') / 'phase' / filename_slug / 'index.html',
        )

    if parts and parts[0] == 'patch':
        return PreviewTarget(
            family='patch',
            slug=filename_slug,
            output_rel_path=PurePosixPath('preview') / 'patch' / filename_slug / 'index.html',
        )

    return PreviewTarget(
        family='docs',
        slug=filename_slug,
        output_rel_path=PurePosixPath('preview') / 'docs' / filename_slug / 'index.html',
    )
