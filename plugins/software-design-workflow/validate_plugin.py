#!/usr/bin/env python3
from pathlib import Path
import json
import re
import sys

ROOT = Path(__file__).resolve().parent
PLUGIN_NAME = 'software-design-workflow'
SEMVER = re.compile(r'\d+\.\d+\.\d+')

REQUIRED_COMMANDS = [
    'start.md',
    'classify.md',
    'discover.md',
    'model.md',
    'design.md',
    'quality.md',
    'target.md',
    'freeze-target.md',
    'plan.md',
    'review.md',
    'handoff.md',
    'change.md',
    'status.md',
    'full.md',
]

CANONICAL_STAGES = [
    'intake',
    'classified',
    'discovered',
    'modeled',
    'designed',
    'qualified',
    'planned',
    'reviewed',
    'handoff-ready',
]

REQUIRED_DOC_SUBTREES = [
    'project',
    'analysis',
    'design',
    'quality',
    'releases',
    'handoff',
]

REQUIRED_LONG_LIVED_TEMPLATE_FILES = [
    'project/vision.md',
    'project/scope.md',
    'project/project-context.md',
    'project/glossary.md',
    'analysis/project-classification.md',
    'analysis/domain-model.md',
    'analysis/workflows.md',
    'analysis/state-model.md',
    'analysis/information-model.md',
    'design/solution-strategy.md',
    'design/architecture.md',
    'design/components.md',
    'design/interfaces.md',
    'design/data-and-state.md',
    'design/deployment-runtime.md',
    'quality/quality-attributes.md',
    'quality/validation-strategy.md',
    'quality/security-privacy.md',
    'quality/observability-operability.md',
]

REQUIRED_CURRENT_TARGET_TEMPLATE_FILES = [
    'releases/current-target/scope-baseline.md',
    'releases/current-target/requirements.md',
    'releases/current-target/constraints.md',
    'releases/current-target/milestones.md',
    'releases/current-target/implementation-plan.md',
    'releases/current-target/task-breakdown.md',
    'releases/current-target/risks.md',
    'releases/current-target/open-questions.md',
    'releases/current-target/review-notes.md',
    'releases/current-target/change-log.md',
]

REQUIRED_HANDOFF_TEMPLATE_FILES = [
    'handoff/agent-entry.md',
    'handoff/execution-brief.md',
    'handoff/openspec-handoff.md',
]

REQUIRED_TEMPLATE_FILES = [
    *REQUIRED_LONG_LIVED_TEMPLATE_FILES,
    *REQUIRED_CURRENT_TARGET_TEMPLATE_FILES,
    *REQUIRED_HANDOFF_TEMPLATE_FILES,
]

ADAPTER_GROUPS = [
    'kinds',
    'surfaces',
    'runtimes',
    'concerns',
    'domains',
]

ADAPTER_REQUIRED_FILES = {
    'kinds': ['application.md', 'service.md', 'library-sdk.md', 'agent-system.md'],
    'surfaces': ['web-ui.md', 'http-api.md', 'cli.md', 'agent-tools.md'],
    'runtimes': ['browser.md', 'server.md', 'local-machine.md', 'cloud-platform.md'],
    'concerns': ['security-privacy.md', 'performance.md', 'observability.md', 'compatibility.md'],
    'domains': ['developer-tools.md', 'knowledge-management.md'],
}

errors: list[str] = []


def require(condition: bool, message: str) -> None:
    if not condition:
        errors.append(message)


def load_json(path: Path, label: str) -> dict[str, object]:
    try:
        data = json.loads(path.read_text())
    except json.JSONDecodeError as exc:
        errors.append(f'{label} is not valid JSON: {exc.msg} at line {exc.lineno} column {exc.colno}')
        return {}
    require(isinstance(data, dict), f'{label} must contain a JSON object')
    return data if isinstance(data, dict) else {}


def frontmatter(path: Path) -> dict[str, str]:
    text = path.read_text()
    if not text.startswith('---\n'):
        errors.append(f'{path.relative_to(ROOT)} missing YAML frontmatter')
        return {}
    end = text.find('\n---\n', 4)
    if end == -1:
        errors.append(f'{path.relative_to(ROOT)} has unterminated YAML frontmatter')
        return {}
    data: dict[str, str] = {}
    for line in text[4:end].splitlines():
        if ':' in line:
            key, value = line.split(':', 1)
            data[key.strip()] = value.strip().strip('"')
    return data


def require_non_empty_string(value: object, label: str) -> None:
    require(isinstance(value, str) and value.strip() != '', f'{label} must be a non-empty string')


def has_unrestricted_bash(value: str) -> bool:
    return any(tool.strip() == 'Bash' for tool in value.split(','))


def text_files() -> list[Path]:
    files: list[Path] = []
    for path in ROOT.rglob('*'):
        if path.is_file() and '.git' not in path.parts:
            try:
                path.read_text()
            except UnicodeDecodeError:
                continue
            files.append(path)
    return files


manifest_path = ROOT / '.claude-plugin' / 'plugin.json'
require(manifest_path.exists(), '.claude-plugin/plugin.json missing')
if manifest_path.exists():
    manifest = load_json(manifest_path, '.claude-plugin/plugin.json')
    require(manifest.get('name') == PLUGIN_NAME, f'plugin name must be {PLUGIN_NAME}')
    version = manifest.get('version')
    require(isinstance(version, str) and SEMVER.fullmatch(version) is not None, 'plugin version must be semver')
    require_non_empty_string(manifest.get('description'), 'plugin description')
    author = manifest.get('author')
    if author is not None:
        require(isinstance(author, dict), 'plugin author must be an object')
        if isinstance(author, dict):
            require_non_empty_string(author.get('name'), 'plugin author.name')

commands_dir = ROOT / 'commands'
require(commands_dir.is_dir(), 'commands directory missing')
for command_file in REQUIRED_COMMANDS:
    command_path = commands_dir / command_file
    require(command_path.exists(), f'commands/{command_file} missing')

if commands_dir.is_dir():
    actual_commands = {path.name for path in commands_dir.glob('*.md')}
    missing_commands = sorted(set(REQUIRED_COMMANDS) - actual_commands)
    require(not missing_commands, f'/sdw command set is incomplete: missing {missing_commands}')

    for command in sorted(commands_dir.glob('*.md')):
        fm = frontmatter(command)
        for key in ['description', 'argument-hint', 'allowed-tools']:
            require(key in fm, f'{command.relative_to(ROOT)} missing {key}')
            require_non_empty_string(fm.get(key), f'{command.relative_to(ROOT)} {key}')
        require(not has_unrestricted_bash(fm.get('allowed-tools', '')), f'{command.relative_to(ROOT)} must not allow unrestricted Bash')
        rel = command.relative_to(commands_dir)
        require(len(rel.parts) == 1, f'{command.relative_to(ROOT)} must be a flat command file')
        expected_title = f'# /sdw:{command.stem}'
        require(expected_title in command.read_text(), f'{command.relative_to(ROOT)} title must include {expected_title}')

agents_dir = ROOT / 'agents'
require(agents_dir.is_dir(), 'agents directory missing')
if agents_dir.is_dir():
    for agent in sorted(agents_dir.glob('*.md')):
        fm = frontmatter(agent)
        require(fm.get('name') == agent.stem, f'{agent.relative_to(ROOT)} name must be {agent.stem}')
        for key in ['description', 'tools', 'model', 'color']:
            require(key in fm, f'{agent.relative_to(ROOT)} missing {key}')
            require_non_empty_string(fm.get(key), f'{agent.relative_to(ROOT)} {key}')
        require(not has_unrestricted_bash(fm.get('tools', '')), f'{agent.relative_to(ROOT)} must not allow unrestricted Bash')

stage_source_paths = [
    ROOT / 'README.md',
    ROOT / 'USAGE.md',
    ROOT / 'STARTER_PROMPT.md',
    ROOT / 'workflow.md',
    ROOT / 'docs-template' / 'README.md',
]
stage_source_paths.extend(sorted((ROOT / 'commands').glob('*.md')))
stage_source_paths.extend(sorted((ROOT / 'rubrics').glob('*.md')) if (ROOT / 'rubrics').is_dir() else [])
stage_source_text = '\n'.join(path.read_text() for path in stage_source_paths if path.exists())
for stage in CANONICAL_STAGES:
    require(stage in stage_source_text, f'canonical stage term missing from workflow-facing docs: {stage}')

workflow_path = ROOT / 'workflow.md'
if workflow_path.exists():
    workflow_text = workflow_path.read_text()
    for earlier, later in zip(CANONICAL_STAGES, CANONICAL_STAGES[1:]):
        require(earlier in workflow_text and later in workflow_text, f'workflow.md must include stage transition {earlier} -> {later}')

for subtree in REQUIRED_DOC_SUBTREES:
    require((ROOT / 'docs-template' / subtree).is_dir(), f'docs-template/{subtree} directory missing')

for rel in REQUIRED_TEMPLATE_FILES:
    path = ROOT / 'docs-template' / rel
    require(path.exists(), f'docs-template/{rel} missing')
    if path.exists():
        require(path.read_text().strip() != '', f'docs-template/{rel} must not be empty')

require((ROOT / 'docs-template' / 'handoff' / 'agent-entry.md').exists(), 'docs-template/handoff/agent-entry.md missing')

adapters_dir = ROOT / 'adapters'
require(adapters_dir.is_dir(), 'adapters directory missing')
require((adapters_dir / 'index.md').exists(), 'adapters/index.md missing')
for group in ADAPTER_GROUPS:
    group_dir = adapters_dir / group
    require(group_dir.is_dir(), f'adapters/{group} directory missing')
    require((group_dir / 'index.md').exists(), f'adapters/{group}/index.md missing')
    require((group_dir / 'README.md').exists(), f'adapters/{group}/README.md missing')
    for file_name in ADAPTER_REQUIRED_FILES[group]:
        adapter_file = group_dir / file_name
        require(adapter_file.exists(), f'adapters/{group}/{file_name} missing')
        if adapter_file.exists():
            require(adapter_file.read_text().strip() != '', f'adapters/{group}/{file_name} must not be empty')

for script in ['validate-sdw-docs.py', 'init-docs.py', 'install-to-project.sh', 'install-to-project.ps1']:
    require((ROOT / 'scripts' / script).exists(), f'scripts/{script} missing')

for rubric in ['completion-gates.md', 'design-review-checklist.md', 'anti-patterns.md']:
    require((ROOT / 'rubrics' / rubric).exists(), f'rubrics/{rubric} missing')

fullwidth_punctuation = {chr(codepoint) for codepoint in [
    0xFF0C, 0x3002, 0xFF1B, 0xFF1A, 0xFF01, 0xFF1F, 0xFF08, 0xFF09,
    0x3010, 0x3011, 0x3001, 0x201C, 0x201D, 0x2018, 0x2019, 0x300A, 0x300B,
    0xFF02, 0xFF07, 0x300C, 0x300D, 0x300E, 0x300F,
]}
local_path_patterns = [
    re.compile('/' + 'Users' + '/'),
    re.compile(r'(?:^|[\s\'\"`(])/' + 'home' + r'/[^/\\\s]+(?:/|$)'),
    re.compile('/' + 'var' + '/' + 'folders' + '/'),
    re.compile('/' + 'private' + '/' + 'var' + '/' + 'folders' + '/'),
    re.compile(r'[A-Za-z]:[\\/]Users[\\/]'),
]
for path in text_files():
    text = path.read_text()
    hits = ''.join(sorted(fullwidth_punctuation.intersection(text)))
    require(not hits, f'{path.relative_to(ROOT)} contains fullwidth punctuation: {hits}')
    for pattern in local_path_patterns:
        require(not pattern.search(text), f'{path.relative_to(ROOT)} contains local absolute path pattern {pattern.pattern}')

if errors:
    print('Plugin validation failed:')
    for error in errors:
        print(f'- {error}')
    sys.exit(1)
print('Plugin validation passed')
