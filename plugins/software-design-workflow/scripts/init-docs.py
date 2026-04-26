#!/usr/bin/env python3
from pathlib import Path
import argparse
import shutil
import sys

PLUGIN_ROOT = Path(__file__).resolve().parents[1]
TEMPLATE_DIR = PLUGIN_ROOT / 'docs-template'


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description='Initialize software-design-workflow docs in a project.')
    parser.add_argument('project_dir', nargs='?', default='.', help='Project directory to initialize. Default: current directory')
    parser.add_argument('--docs-dir', default='docs', help='Docs directory name inside the project. Default: docs')
    parser.add_argument('--overwrite', action='store_true', help='Overwrite existing files')
    return parser.parse_args()


def copy_tree(source: Path, destination: Path, overwrite: bool) -> list[Path]:
    written: list[Path] = []
    for source_path in sorted(source.rglob('*')):
        relative = source_path.relative_to(source)
        destination_path = destination / relative
        if source_path.is_dir():
            destination_path.mkdir(parents=True, exist_ok=True)
            continue
        if destination_path.exists() and not overwrite:
            continue
        destination_path.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source_path, destination_path)
        written.append(destination_path)
    return written


def main() -> int:
    args = parse_args()
    project_dir = Path(args.project_dir).resolve()
    docs_dir = project_dir / args.docs_dir

    if not project_dir.exists() or not project_dir.is_dir():
        print(f'Project directory does not exist: {project_dir}', file=sys.stderr)
        return 1
    if not TEMPLATE_DIR.is_dir():
        print(f'Docs template directory missing: {TEMPLATE_DIR}', file=sys.stderr)
        return 1

    written = copy_tree(TEMPLATE_DIR, docs_dir, args.overwrite)
    print(f'Initialized software design docs at {docs_dir}')
    print(f'Files written: {len(written)}')
    print(f'Agent entry point: {args.docs_dir}/handoff/agent-entry.md')
    return 0


if __name__ == '__main__':
    sys.exit(main())
