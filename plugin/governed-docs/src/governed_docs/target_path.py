from pathlib import Path
from typing import Optional, Union


class TargetPathError(ValueError):
    """Raised when governed-docs target path input is missing or invalid."""


def resolve_target_workspace_path(target_path: Optional[Union[str, Path]]) -> Path:
    if target_path is None or str(target_path).strip() == "":
        raise TargetPathError("An explicit target workspace path is required.")

    resolved_path = Path(target_path).expanduser().resolve()
    if not resolved_path.exists():
        raise TargetPathError(f"Target workspace path does not exist: {resolved_path}")

    if not resolved_path.is_dir():
        raise TargetPathError(f"Target workspace path must be a directory: {resolved_path}")

    return resolved_path
