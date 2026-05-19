[CmdletBinding()]
param(
  [string]$ProjectRoot
)

$cliArgs = @($args)

Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'

function Show-LauncherUsage {
  @"
Usage:
  launcher.ps1 [-ProjectRoot <path>]

Primary operator path for Claude Code project-local RULES install.
- Run from a cloned RULES repo.
- Dispatches to script/setup-claude-code-rules.ps1.
- Installs into <project-root>/.claude/rules/.

If -ProjectRoot is omitted:
- when run outside the RULES repo root, the current directory is used
- when run from the RULES repo root, an explicit -ProjectRoot is required
"@ | Write-Host
}

if ($cliArgs -contains '-h' -or $cliArgs -contains '--help') {
  Show-LauncherUsage
  exit 0
}

$scriptDir = Split-Path -Parent $PSCommandPath
$repoRoot = (Resolve-Path -LiteralPath (Join-Path $scriptDir '..')).Path
$helper = Join-Path $repoRoot 'script/setup-claude-code-rules.ps1'

if (-not (Test-Path -LiteralPath $helper -PathType Leaf)) {
  throw "Helper script is missing: $helper"
}

if ([string]::IsNullOrWhiteSpace($ProjectRoot)) {
  $currentDir = (Get-Location).Path
  if ((Resolve-Path -LiteralPath $currentDir).Path -eq $repoRoot) {
    throw "When running launcher from the RULES repo root, pass -ProjectRoot <target-project>."
  }
  $ProjectRoot = $currentDir
}

& $helper -ProjectRoot $ProjectRoot -SourceRepo $repoRoot
