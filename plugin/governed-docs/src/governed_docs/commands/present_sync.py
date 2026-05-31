from pathlib import Path
from typing import Optional, Union

from governed_docs.preview_site import sync_preview_site
from governed_docs.target_path import resolve_target_workspace_path



def run_present_sync_command(target_path: Optional[Union[str, Path]], *_extra_args) -> str:
    workspace_path = resolve_target_workspace_path(target_path)
    result = sync_preview_site(workspace_path)
    return '\n'.join(
        [
            'Preview site synced',
            f'Preview root: {result.preview_root}',
            f'Index: {result.index_path}',
            f'Manifest: {result.manifest_path}',
            f'Documents: {len(result.documents)}',
            'Source governed docs were not rewritten.',
        ]
    )
