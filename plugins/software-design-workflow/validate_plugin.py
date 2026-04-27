#!/usr/bin/env python3
from pathlib import Path
import json
import re
import sys

ROOT = Path(__file__).resolve().parent
PLUGIN_NAME = 'software-design-workflow'
SEMVER = re.compile(r'\d+\.\d+\.\d+')
REQUIRED_SKILLS = [
    'software-design-workflow',
    'scope-control',
    'handoff-readiness',
]
REQUIRED_TEMPLATE_FILES = [
    'project/vision.md',
    'project/scope.md',
    'project/project-context.md',
    'analysis/project-classification.md',
    'analysis/domain-model.md',
    'analysis/workflows.md',
    'design/architecture.md',
    'design/interfaces.md',
    'design/data-and-state.md',
    'quality/quality-attributes.md',
    'quality/validation-strategy.md',
    'releases/current-target/scope-baseline.md',
    'releases/current-target/requirements.md',
    'releases/current-target/implementation-plan.md',
    'releases/current-target/risks.md',
    'releases/current-target/review-notes.md',
    'releases/current-target/change-log.md',
    'handoff/agent-entry.md',
    'handoff/execution-brief.md',
]
REQUIRED_SCRIPTS = [
    'init-docs.py',
    'validate-sdw-docs.py',
    'install-to-project.sh',
    'install-to-project.ps1',
]
REQUIRED_RUBRICS = [
    'anti-patterns.md',
    'completion-gates.md',
    'design-review-checklist.md',
]
REMOVED_DIRS = [
    '.' + 'claude-plugin',
    'commands',
    'agents',
    'examples',
    'type-' + 'specific-templates',
]
errors: list[str] = []


def require(condition: bool, message: str) -> None:
    if not condition:
        errors.append(message)


def require_non_empty_string(value: object, label: str) -> None:
    require(isinstance(value, str) and value.strip() != '', f'{label} must be a non-empty string')


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


def text_files() -> list[Path]:
    files: list[Path] = []
    for path in ROOT.rglob('*'):
        if not path.is_file() or '.git' in path.parts:
            continue
        try:
            path.read_text()
        except UnicodeDecodeError:
            continue
        files.append(path)
    return files


manifest_path = ROOT / '.codex-plugin' / 'plugin.json'
require(manifest_path.exists(), '.codex-plugin/plugin.json missing')
if manifest_path.exists():
    manifest = load_json(manifest_path, '.codex-plugin/plugin.json')
    require(manifest.get('name') == PLUGIN_NAME, f'plugin name must be {PLUGIN_NAME}')
    version = manifest.get('version')
    require(isinstance(version, str) and SEMVER.fullmatch(version) is not None, 'plugin version must be semver')
    require_non_empty_string(manifest.get('description'), 'plugin description')
    require(manifest.get('skills') == './skills/', 'plugin skills path must be ./skills/')
    author = manifest.get('author')
    require(isinstance(author, dict), 'plugin author must be an object')
    if isinstance(author, dict):
        require_non_empty_string(author.get('name'), 'plugin author.name')
    interface = manifest.get('interface')
    require(isinstance(interface, dict), 'plugin interface must be an object')
    if isinstance(interface, dict):
        for key in ['displayName', 'shortDescription', 'longDescription', 'developerName', 'category', 'brandColor']:
            require_non_empty_string(interface.get(key), f'plugin interface.{key}')
        prompts = interface.get('defaultPrompt')
        require(isinstance(prompts, list) and 1 <= len(prompts) <= 3, 'plugin interface.defaultPrompt must contain 1-3 prompts')
        if isinstance(prompts, list):
            for index, prompt in enumerate(prompts):
                require(isinstance(prompt, str) and 0 < len(prompt) <= 128, f'plugin interface.defaultPrompt[{index}] must be 1-128 chars')

for rel in REMOVED_DIRS:
    require(not (ROOT / rel).exists(), f'{rel} must not exist in simplified Codex plugin')

skills_dir = ROOT / 'skills'
require(skills_dir.is_dir(), 'skills directory missing')
if skills_dir.is_dir():
    actual_skill_dirs = sorted(path.name for path in skills_dir.iterdir() if path.is_dir())
    require(actual_skill_dirs == sorted(REQUIRED_SKILLS), f'skills must be exactly {sorted(REQUIRED_SKILLS)}')
    for skill_name in REQUIRED_SKILLS:
        skill_path = skills_dir / skill_name / 'SKILL.md'
        require(skill_path.exists(), f'skills/{skill_name}/SKILL.md missing')
        if skill_path.exists():
            fm = frontmatter(skill_path)
            require(fm.get('name') == skill_name, f'skills/{skill_name}/SKILL.md name must be {skill_name}')
            require_non_empty_string(fm.get('description'), f'skills/{skill_name}/SKILL.md description')
            require(skill_path.read_text().strip() != '', f'skills/{skill_name}/SKILL.md must not be empty')

adapters_index = ROOT / 'adapters' / 'index.md'
require(adapters_index.exists(), 'adapters/index.md missing')
if adapters_index.exists():
    require(adapters_index.read_text().strip() != '', 'adapters/index.md must not be empty')
for adapter_child in (ROOT / 'adapters').iterdir() if (ROOT / 'adapters').is_dir() else []:
    if adapter_child.is_dir():
        require(False, f'adapters must stay flat, unexpected directory: adapters/{adapter_child.name}')

for rel in REQUIRED_TEMPLATE_FILES:
    path = ROOT / 'docs-template' / rel
    require(path.exists(), f'docs-template/{rel} missing')
    if path.exists():
        require(path.read_text().strip() != '', f'docs-template/{rel} must not be empty')

for script in REQUIRED_SCRIPTS:
    path = ROOT / 'scripts' / script
    require(path.exists(), f'scripts/{script} missing')
    if path.exists():
        require(path.read_text().strip() != '', f'scripts/{script} must not be empty')

for rubric in REQUIRED_RUBRICS:
    path = ROOT / 'rubrics' / rubric
    require(path.exists(), f'rubrics/{rubric} missing')
    if path.exists():
        require(path.read_text().strip() != '', f'rubrics/{rubric} must not be empty')

for doc_name in ['README.md', 'USAGE.md', 'STARTER_PROMPT.md', 'workflow.md']:
    path = ROOT / doc_name
    require(path.exists(), f'{doc_name} missing')
    if path.exists():
        require(path.read_text().strip() != '', f'{doc_name} must not be empty')

fullwidth_punctuation = {chr(codepoint) for codepoint in [
    0xFF0C, 0x3002, 0xFF1B, 0xFF1A, 0xFF1F, 0xFF08, 0xFF09,
    0x3010, 0x3011, 0x3001, 0x201C, 0x201D, 0x2018, 0x2019, 0x300A, 0x300B,
    0xFF02, 0xFF07, 0x300C, 0x300D, 0x300E, 0x300F,
]}
local_path_patterns = [
    re.compile('/' + 'Users' + '/'),
    re.compile(r'(?:^|[\s\'"`(])/' + 'home' + r'/[^/\\\s]+(?:/|$)'),
    re.compile('/' + 'var' + '/' + 'folders' + '/'),
    re.compile('/' + 'private' + '/' + 'var' + '/' + 'folders' + '/'),
    re.compile(r'[A-Za-z]:[\\/]Users[\\/]'),
]
banned_text = ['Claude' + ' Code', '/' + 'sdw:', '/' + 'sdw', 'type-' + 'specific-templates']
for path in text_files():
    text = path.read_text()
    hits = ''.join(sorted(fullwidth_punctuation.intersection(text)))
    require(not hits, f'{path.relative_to(ROOT)} contains fullwidth punctuation: {hits}')
    for pattern in local_path_patterns:
        require(not pattern.search(text), f'{path.relative_to(ROOT)} contains local absolute path pattern {pattern.pattern}')
    if path.name == 'validate_plugin.py':
        continue
    for banned in banned_text:
        require(banned not in text, f'{path.relative_to(ROOT)} contains removed workflow text: {banned}')

if errors:
    print('Plugin validation failed:')
    for error in errors:
        print(f'- {error}')
    sys.exit(1)
print('Plugin validation passed')
