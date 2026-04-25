#!/usr/bin/env python3
from pathlib import Path
import json
import re
import sys

ROOT = Path(__file__).resolve().parent
PROJECT_TYPES = [
    'backend-api',
    'frontend-spa',
    'fullstack-web',
    'cli-tool',
    'desktop-app',
    'mobile-app',
    'library-sdk',
    'ai-agent',
    'rag-app',
    'data-pipeline',
]
REQUIRED_COMMANDS = [
    'project/new.md',
    'project/interview.md',
    'project/generate-docs.md',
    'project/review-docs.md',
    'project/freeze-v1.md',
    'project/plan-implementation.md',
    'project/ready-for-coding.md',
    'project/change.md',
    'project/status.md',
]
STATE_SEQUENCE = 'idea -> classified -> interviewed -> docs-generated -> docs-reviewed -> v1-frozen -> implementation-planned -> ready-for-coding'
errors: list[str] = []


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


def require(condition: bool, message: str) -> None:
    if not condition:
        errors.append(message)


manifest_path = ROOT / '.claude-plugin' / 'plugin.json'
require(manifest_path.exists(), '.claude-plugin/plugin.json missing')
if manifest_path.exists():
    manifest = json.loads(manifest_path.read_text())
    require(manifest.get('name') == 'agent-workflow', 'plugin name must be agent-workflow')

for rel in REQUIRED_COMMANDS:
    command_path = ROOT / 'commands' / rel
    require(command_path.exists(), f'commands/{rel} missing')

for command in sorted((ROOT / 'commands').rglob('*.md')):
    fm = frontmatter(command)
    for key in ['description', 'argument-hint', 'allowed-tools']:
        require(key in fm, f'{command.relative_to(ROOT)} missing {key}')
    tools = fm.get('allowed-tools', '')
    require('Bash' not in tools, f'{command.relative_to(ROOT)} should not allow unrestricted Bash')
    rel = command.relative_to(ROOT / 'commands')
    if len(rel.parts) == 2:
        expected_title = f'# /{rel.parts[0]}:{command.stem}'
        require(expected_title in command.read_text(), f'{command.relative_to(ROOT)} title must include {expected_title}')

for agent in sorted((ROOT / 'agents').glob('*.md')):
    fm = frontmatter(agent)
    expected = agent.stem
    require(fm.get('name') == expected, f'{agent.relative_to(ROOT)} name must be {expected}')
    for key in ['description', 'tools', 'model', 'color']:
        require(key in fm, f'{agent.relative_to(ROOT)} missing {key}')
    require('Bash' not in fm.get('tools', ''), f'{agent.relative_to(ROOT)} should not allow unrestricted Bash')

for skill_dir in sorted((ROOT / 'skills').iterdir() if (ROOT / 'skills').exists() else []):
    if not skill_dir.is_dir():
        continue
    skill_file = skill_dir / 'SKILL.md'
    require(skill_file.exists(), f'{skill_dir.relative_to(ROOT)} missing SKILL.md')
    if skill_file.exists():
        fm = frontmatter(skill_file)
        require(fm.get('name') == skill_dir.name, f'{skill_file.relative_to(ROOT)} name must be {skill_dir.name}')
        require('description' in fm, f'{skill_file.relative_to(ROOT)} missing description')

for project_type in PROJECT_TYPES:
    require((ROOT / 'skills' / project_type / 'SKILL.md').exists(), f'skill missing for {project_type}')
    require((ROOT / 'type-specific-templates' / project_type).is_dir(), f'template dir missing for {project_type}')
    skill_text = (ROOT / 'skills' / project_type / 'SKILL.md').read_text()
    require(f'docs/type-specific/{project_type}/' in skill_text, f'{project_type} skill must use canonical docs/type-specific/{project_type}/ path')

readme = ROOT / 'docs-template' / 'README.md'
if readme.exists():
    text = readme.read_text()
    require('implementation-planned' in text, 'docs-template/README.md must include implementation-planned')
    require('Current stage` 必须是 `ready-for-coding`' in text, 'docs-template/README.md must gate coding on ready-for-coding')
    require('V1 status` 必须是 `frozen`' in text, 'docs-template/README.md must gate coding on frozen V1')
    require('blocking open questions' in text, 'docs-template/README.md must gate coding on blocking open questions')

status_command = ROOT / 'commands' / 'project' / 'status.md'
if status_command.exists():
    fm = frontmatter(status_command)
    require(fm.get('allowed-tools') == 'Read', 'project status command must be read-only')

freeze_command = ROOT / 'commands' / 'project' / 'freeze-v1.md'
if freeze_command.exists():
    text = freeze_command.read_text()
    for needle in ['## Preconditions', '`docs-reviewed`', 'Blocking Issues', 'Blocking V1?', '停止']:
        require(needle in text, f'project freeze command missing gate text: {needle}')

plan_command = ROOT / 'commands' / 'project' / 'plan-implementation.md'
if plan_command.exists():
    text = plan_command.read_text()
    require('implementation-planned' in text, 'project plan command must mention implementation-planned')
    require('ready-for-coding' in text, 'project plan command must mention ready-for-coding')
    require('不要在同一次执行中更新为 `ready-for-coding`' in text, 'project plan command must not auto-advance to ready-for-coding')
    for needle in ['## Preconditions', '`v1-frozen`', 'V1 status', 'blocking TODO', 'blocking open question', 'docs/README.md 的 Required Reading Order']:
        require(needle in text, f'project plan command missing gate text: {needle}')

ready_command = ROOT / 'commands' / 'project' / 'ready-for-coding.md'
if ready_command.exists():
    text = ready_command.read_text()
    for needle in ['# /project:ready-for-coding', '`implementation-planned`', '`ready-for-coding`', 'V1 status', 'Blocking Issues', 'Blocking V1?', '用户确认']:
        require(needle in text, f'project ready command missing readiness text: {needle}')

for command_name, stage in [('new', 'classified'), ('interview', 'interviewed'), ('generate-docs', 'docs-generated'), ('review-docs', 'docs-reviewed'), ('freeze-v1', 'v1-frozen')]:
    command_path = ROOT / 'commands' / 'project' / f'{command_name}.md'
    if command_path.exists():
        require(stage in command_path.read_text(), f'project {command_name} command must update stage {stage}')

change_command = ROOT / 'commands' / 'project' / 'change.md'
if change_command.exists():
    text = change_command.read_text()
    for needle in ['Impact analysis', 'Apply change', '用户确认', 'impacted docs', 'implementation-plan.md', 'acceptance-criteria.md']:
        require(needle in text, f'project change command missing change workflow text: {needle}')

ai_safety = ROOT / 'type-specific-templates' / 'ai-agent' / 'safety-boundaries.md'
require(ai_safety.exists(), 'ai-agent safety-boundaries template missing')
if ai_safety.exists():
    text = ai_safety.read_text()
    for needle in ['禁止任意 shell', '删除文件', '外部写操作', 'secrets', '不得自行扩大工具权限']:
        require(needle in text, f'ai-agent safety template missing safety text: {needle}')

fullwidth_punctuation = {chr(codepoint) for codepoint in [
    0xFF0C, 0x3002, 0xFF1B, 0xFF1A, 0xFF01, 0xFF1F, 0xFF08, 0xFF09,
    0x3010, 0x3011, 0x3001, 0x201C, 0x201D, 0x2018, 0x2019, 0x300A, 0x300B,
    0xFF02, 0xFF07, 0x300C, 0x300D, 0x300E, 0x300F,
]}
local_path_patterns = [
    '/' + 'Users' + '/',
    '/' + 'home' + '/',
    '/' + 'var' + '/' + 'folders' + '/',
    'C:' + '\\' + 'Users' + '\\',
]
for path in ROOT.rglob('*'):
    if path.is_file() and '.git' not in path.parts:
        try:
            text = path.read_text()
        except UnicodeDecodeError:
            continue
        hits = ''.join(sorted(fullwidth_punctuation.intersection(text)))
        require(not hits, f'{path.relative_to(ROOT)} contains fullwidth punctuation: {hits}')
        for pattern in local_path_patterns:
            require(pattern not in text, f'{path.relative_to(ROOT)} contains local absolute path pattern {pattern}')

if errors:
    print('Plugin validation failed:')
    for error in errors:
        print(f'- {error}')
    sys.exit(1)
print('Plugin validation passed')
