from dataclasses import dataclass, field
from pathlib import Path
from typing import List


@dataclass(frozen=True)
class DiscoveredSurface:
    path: Path
    relative_path: str
    surface_family: str
    inventory_class: str


@dataclass(frozen=True)
class ScanResult:
    target_workspace_path: Path
    checked_scope: str
    discovered_surfaces: List[DiscoveredSurface]
    missing_expected_top_level_surfaces: List[str] = field(default_factory=list)
    skipped_surfaces: List[str] = field(default_factory=list)
    scanner_warnings: List[str] = field(default_factory=list)
    mutated: bool = False
