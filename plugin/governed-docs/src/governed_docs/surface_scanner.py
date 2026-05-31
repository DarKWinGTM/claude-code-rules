from pathlib import Path

from governed_docs.scan_result import DiscoveredSurface, ScanResult
from governed_docs.target_path import resolve_target_workspace_path


ACTIVE_AUTHORITY_SURFACES = (
    ("README.md", "readme"),
    ("TODO.md", "todo"),
    ("phase/SUMMARY.md", "phase-summary"),
    ("design/design.md", "design-parent"),
    ("changelog/changelog.md", "changelog-parent"),
)

ACTIVE_FILE_PATTERNS = (
    ("patch/*.patch.md", "patch"),
)

INACTIVE_SURFACE_PATTERNS = (
    ("todo/history/**/*.md", "todo-history"),
    ("phase/done/**/*.md", "phase-done"),
)


def build_surface_record(
    workspace_path: Path,
    surface_path: Path,
    surface_family: str,
    inventory_class: str,
) -> DiscoveredSurface:
    return DiscoveredSurface(
        path=surface_path,
        relative_path=surface_path.relative_to(workspace_path).as_posix(),
        surface_family=surface_family,
        inventory_class=inventory_class,
    )



def scan_governed_surfaces(target_workspace_path: Path) -> ScanResult:
    workspace_path = resolve_target_workspace_path(target_workspace_path)
    discovered_surfaces = []
    missing_expected_top_level_surfaces = []

    for relative_path, surface_family in ACTIVE_AUTHORITY_SURFACES:
        surface_path = workspace_path / relative_path
        if surface_path.exists():
            discovered_surfaces.append(
                build_surface_record(
                    workspace_path,
                    surface_path,
                    surface_family,
                    "active authority surface",
                )
            )
        else:
            missing_expected_top_level_surfaces.append(relative_path)

    for pattern, surface_family in ACTIVE_FILE_PATTERNS:
        for surface_path in sorted(workspace_path.glob(pattern)):
            if surface_path.is_file():
                discovered_surfaces.append(
                    build_surface_record(
                        workspace_path,
                        surface_path,
                        surface_family,
                        "active authority surface",
                    )
                )

    for pattern, surface_family in INACTIVE_SURFACE_PATTERNS:
        for surface_path in sorted(workspace_path.glob(pattern)):
            if surface_path.is_file():
                discovered_surfaces.append(
                    build_surface_record(
                        workspace_path,
                        surface_path,
                        surface_family,
                        "inactive history/done surface",
                    )
                )

    return ScanResult(
        target_workspace_path=workspace_path,
        checked_scope=str(workspace_path),
        discovered_surfaces=discovered_surfaces,
        missing_expected_top_level_surfaces=missing_expected_top_level_surfaces,
        skipped_surfaces=[],
        scanner_warnings=[],
        mutated=False,
    )
