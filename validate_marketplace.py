#!/usr/bin/env python3
from pathlib import Path
import json
import re
import subprocess
import sys

ROOT = Path(__file__).resolve().parent
SEMVER = re.compile(r'\d+\.\d+\.\d+')
KEBAB_CASE = re.compile(r'[a-z0-9]+(?:-[a-z0-9]+)*')
errors: list[str] = []


def is_git_ignored(path: Path) -> bool:
    result = subprocess.run(
        ['git', 'check-ignore', '-q', str(path.relative_to(ROOT))],
        cwd=ROOT,
    )
    return result.returncode == 0


def require(condition: bool, message: str) -> None:
    if not condition:
        errors.append(message)


def require_non_empty_string(value: object, label: str) -> None:
    require(isinstance(value, str) and value.strip() != '', f'{label} must be a non-empty string')


def load_json(path: Path, label: str) -> dict:
    try:
        data = json.loads(path.read_text())
    except json.JSONDecodeError as exc:
        errors.append(f'{label} is not valid JSON: {exc.msg} at line {exc.lineno} column {exc.colno}')
        return {}
    require(isinstance(data, dict), f'{label} must contain a JSON object')
    return data if isinstance(data, dict) else {}


marketplace_path = ROOT / '.claude-plugin' / 'marketplace.json'
require(marketplace_path.exists(), '.claude-plugin/marketplace.json missing')
require(not (ROOT / '.claude-plugin' / 'plugin.json').exists(), 'marketplace root must not contain .claude-plugin/plugin.json')

plugins: list[dict] = []
if marketplace_path.exists():
    data = load_json(marketplace_path, '.claude-plugin/marketplace.json')
    require_non_empty_string(data.get('name'), 'marketplace name')
    require(data.get('name') == 'agent-workflow', 'marketplace name must be agent-workflow')
    plugins_value = data.get('plugins', [])
    require(isinstance(plugins_value, list) and bool(plugins_value), 'marketplace must list at least one plugin')
    plugins = plugins_value if isinstance(plugins_value, list) else []
    require(
        any(isinstance(plugin, dict) and plugin.get('name') == 'software-design-workflow' for plugin in plugins),
        'marketplace must include software-design-workflow during migration',
    )

for entry in plugins:
    require(isinstance(entry, dict), 'marketplace plugin entries must be JSON objects')
    if not isinstance(entry, dict):
        continue

    name = entry.get('name')
    source = entry.get('source')
    require_non_empty_string(name, 'marketplace plugin entry name')
    require_non_empty_string(entry.get('description'), f'{name} description')
    require_non_empty_string(entry.get('category'), f'{name} category')
    require_non_empty_string(source, f'{name} source')
    if isinstance(name, str):
        require(KEBAB_CASE.fullmatch(name) is not None, f'{name} plugin name must be kebab-case')

    expected_source = f'./plugins/{name}' if isinstance(name, str) else None
    require(isinstance(source, str) and source == expected_source, f'{name} source must be exactly {expected_source}')
    if not isinstance(name, str) or not isinstance(source, str) or source != expected_source:
        continue

    plugins_root = (ROOT / 'plugins').resolve()
    plugin_dir = (ROOT / source.removeprefix('./')).resolve()
    require(plugin_dir.is_dir(), f'{name} source directory missing: {source}')
    require(plugin_dir.parent == plugins_root, f'{name} source must resolve directly under plugins/')

    plugin_manifest = plugin_dir / '.claude-plugin' / 'plugin.json'
    require(plugin_manifest.exists(), f'{name} missing plugin manifest')
    if plugin_manifest.exists():
        plugin_data = load_json(plugin_manifest, f'{name} plugin manifest')
        require(plugin_data.get('name') == name, f'{name} plugin manifest name mismatch')
        version = plugin_data.get('version')
        require(isinstance(version, str) and SEMVER.fullmatch(version) is not None, f'{name} plugin version must be semver')
        require_non_empty_string(plugin_data.get('description'), f'{name} plugin description')
        author = plugin_data.get('author')
        if author is not None:
            require(isinstance(author, dict), f'{name} plugin author must be an object')
            if isinstance(author, dict):
                require_non_empty_string(author.get('name'), f'{name} plugin author.name')

    validator = plugin_dir / 'validate_plugin.py'
    require(validator.exists(), f'{name} missing validate_plugin.py')
    if validator.exists():
        result = subprocess.run([sys.executable, str(validator)], cwd=plugin_dir)
        require(result.returncode == 0, f'{name} validate_plugin.py failed')

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
for path in ROOT.rglob('*'):
    if path.is_file() and '.git' not in path.parts:
        if is_git_ignored(path):
            continue
        try:
            text = path.read_text()
        except UnicodeDecodeError:
            continue
        hits = ''.join(sorted(fullwidth_punctuation.intersection(text)))
        require(not hits, f'{path.relative_to(ROOT)} contains fullwidth punctuation: {hits}')
        for pattern in local_path_patterns:
            require(not pattern.search(text), f'{path.relative_to(ROOT)} contains local absolute path pattern {pattern.pattern}')

if errors:
    print('Marketplace validation failed:')
    for error in errors:
        print(f'- {error}')
    sys.exit(1)
print('Marketplace validation passed')
