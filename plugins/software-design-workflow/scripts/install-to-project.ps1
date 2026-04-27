param(
    [Parameter(Position = 0)]
    [string]$ProjectDir = ".",

    [string]$DocsDir = "docs",

    [switch]$Overwrite,

    [Alias("h")]
    [switch]$Help
)

$ErrorActionPreference = "Stop"
$ScriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$InitScript = Join-Path $ScriptDir "init-docs.py"
$ValidateScript = Join-Path $ScriptDir "validate-sdw-docs.py"

if ($Help) {
    Get-Help -Detailed $MyInvocation.MyCommand.Path
    exit 0
}

$InitArgs = @($InitScript, $ProjectDir, "--docs-dir", $DocsDir)
if ($Overwrite) {
    $InitArgs += "--overwrite"
}

python3 @InitArgs
$ResolvedProjectDir = (Resolve-Path -LiteralPath $ProjectDir).Path
$ResolvedDocsDir = Join-Path $ResolvedProjectDir $DocsDir
python3 $ValidateScript $ResolvedDocsDir
