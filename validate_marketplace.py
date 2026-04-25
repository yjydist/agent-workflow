#!/usr/bin/env python3
from pathlib import Path
import json
import re
import subprocess
import sys

ROOT = Path(__file__).resolve().parent
errors: list[str] = []


def require(condition: bool, message: str) -> None:
    if not condition:
        errors.append(message)


marketplace_path = ROOT / '.claude-plugin' / 'marketplace.json'
require(marketplace_path.exists(), '.claude-plugin/marketplace.json missing')
require(not (ROOT / '.claude-plugin' / 'plugin.json').exists(), 'marketplace root must not contain .claude-plugin/plugin.json')

plugins: list[dict] = []
if marketplace_path.exists():
    data = json.loads(marketplace_path.read_text())
    require(data.get('name') == 'agent-workflow', 'marketplace name must be agent-workflow')
    plugins = data.get('plugins', [])
    require(isinstance(plugins, list) and plugins, 'marketplace must list at least one plugin')

for entry in plugins:
    name = entry.get('name')
    source = entry.get('source')
    require(name, 'marketplace plugin entry missing name')
    expected_source = f'./plugins/{name}' if name else None
    require(isinstance(source, str) and source == expected_source, f'{name} source must be exactly {expected_source}')
    if not name or not isinstance(source, str) or source != expected_source:
        continue
    plugins_root = (ROOT / 'plugins').resolve()
    plugin_dir = (ROOT / source.removeprefix('./')).resolve()
    require(plugin_dir.is_dir(), f'{name} source directory missing: {source}')
    require(plugin_dir.parent == plugins_root, f'{name} source must resolve directly under plugins/')
    plugin_manifest = plugin_dir / '.claude-plugin' / 'plugin.json'
    require(plugin_manifest.exists(), f'{name} missing plugin manifest')
    if plugin_manifest.exists():
        plugin_data = json.loads(plugin_manifest.read_text())
        require(plugin_data.get('name') == name, f'{name} plugin manifest name mismatch')
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
    re.compile('/' + 'home' + '/'),
    re.compile('/' + 'var' + '/' + 'folders' + '/'),
    re.compile('/' + 'private' + '/' + 'var' + '/' + 'folders' + '/'),
    re.compile(r'[A-Za-z]:[\\/]Users[\\/]'),
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
            require(not pattern.search(text), f'{path.relative_to(ROOT)} contains local absolute path pattern {pattern.pattern}')

if errors:
    print('Marketplace validation failed:')
    for error in errors:
        print(f'- {error}')
    sys.exit(1)
print('Marketplace validation passed')
