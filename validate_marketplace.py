#!/usr/bin/env python3
from pathlib import Path
import json
import re
import subprocess
import sys

ROOT = Path(__file__).resolve().parent
SEMVER = re.compile(r'\d+\.\d+\.\d+')
KEBAB_CASE = re.compile(r'[a-z0-9]+(?:-[a-z0-9]+)*')
MARKETPLACE_PATH = ROOT / '.agents' / 'plugins' / 'marketplace.json'
REQUIRED_PLUGIN = 'software-design-workflow'
REMOVED_MANIFEST_DIR = '.' + 'claude-plugin'
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
    except JSONDecodeError as exc:
        errors.append(f'{label} is not valid JSON: {exc.msg} at line {exc.lineno} column {exc.colno}')
        return {}
    require(isinstance(data, dict), f'{label} must contain a JSON object')
    return data if isinstance(data, dict) else {}


try:
    JSONDecodeError = json.JSONDecodeError
except AttributeError:
    JSONDecodeError = ValueError


require(MARKETPLACE_PATH.exists(), '.agents/plugins/marketplace.json missing')
require(not (ROOT / REMOVED_MANIFEST_DIR).exists(), 'removed marketplace directory must not exist at repository root')

plugins: list[dict] = []
if MARKETPLACE_PATH.exists():
    data = load_json(MARKETPLACE_PATH, '.agents/plugins/marketplace.json')
    require(data.get('name') == 'agent-workflow', 'marketplace name must be agent-workflow')
    interface = data.get('interface')
    require(isinstance(interface, dict), 'marketplace interface must be an object')
    if isinstance(interface, dict):
        require_non_empty_string(interface.get('displayName'), 'marketplace interface.displayName')
    plugins_value = data.get('plugins')
    require(isinstance(plugins_value, list) and bool(plugins_value), 'marketplace must list at least one plugin')
    plugins = plugins_value if isinstance(plugins_value, list) else []
    require(
        any(isinstance(plugin, dict) and plugin.get('name') == REQUIRED_PLUGIN for plugin in plugins),
        f'marketplace must include {REQUIRED_PLUGIN}',
    )

for entry in plugins:
    require(isinstance(entry, dict), 'marketplace plugin entries must be JSON objects')
    if not isinstance(entry, dict):
        continue

    name = entry.get('name')
    require_non_empty_string(name, 'marketplace plugin entry name')
    if isinstance(name, str):
        require(KEBAB_CASE.fullmatch(name) is not None, f'{name} plugin name must be kebab-case')

    source = entry.get('source')
    require(isinstance(source, dict), f'{name} source must be an object')
    if not isinstance(source, dict):
        continue

    require(source.get('source') == 'local', f'{name} source.source must be local')
    expected_path = f'./plugins/{name}' if isinstance(name, str) else None
    source_path = source.get('path')
    require(source_path == expected_path, f'{name} source.path must be exactly {expected_path}')

    policy = entry.get('policy')
    require(isinstance(policy, dict), f'{name} policy must be an object')
    if isinstance(policy, dict):
        require(policy.get('installation') in {'NOT_AVAILABLE', 'AVAILABLE', 'INSTALLED_BY_DEFAULT'}, f'{name} policy.installation is invalid')
        require(policy.get('authentication') in {'ON_INSTALL', 'ON_USE'}, f'{name} policy.authentication is invalid')
    require_non_empty_string(entry.get('category'), f'{name} category')

    if not isinstance(name, str) or source_path != expected_path:
        continue

    plugins_root = (ROOT / 'plugins').resolve()
    plugin_dir = (ROOT / source_path.removeprefix('./')).resolve()
    require(plugin_dir.is_dir(), f'{name} source directory missing: {source_path}')
    require(plugin_dir.parent == plugins_root, f'{name} source must resolve directly under plugins/')
    require(not (plugin_dir / REMOVED_MANIFEST_DIR).exists(), f'{name} must not contain removed marketplace manifest directory')

    plugin_manifest = plugin_dir / '.codex-plugin' / 'plugin.json'
    require(plugin_manifest.exists(), f'{name} missing .codex-plugin/plugin.json')
    if plugin_manifest.exists():
        plugin_data = load_json(plugin_manifest, f'{name} plugin manifest')
        require(plugin_data.get('name') == name, f'{name} plugin manifest name mismatch')
        version = plugin_data.get('version')
        require(isinstance(version, str) and SEMVER.fullmatch(version) is not None, f'{name} plugin version must be semver')
        require_non_empty_string(plugin_data.get('description'), f'{name} plugin description')
        require(plugin_data.get('skills') == './skills/', f'{name} plugin skills path must be ./skills/')

    validator = plugin_dir / 'validate_plugin.py'
    require(validator.exists(), f'{name} missing validate_plugin.py')
    if validator.exists():
        result = subprocess.run([sys.executable, str(validator)], cwd=plugin_dir)
        require(result.returncode == 0, f'{name} validate_plugin.py failed')

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

for path in ROOT.rglob('*'):
    if '.git' in path.parts or '.worktrees' in path.parts:
        continue
    if path.is_dir() and path.name == REMOVED_MANIFEST_DIR:
        require(False, f'{path.relative_to(ROOT)} must not exist')
    if not path.is_file() or is_git_ignored(path):
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
