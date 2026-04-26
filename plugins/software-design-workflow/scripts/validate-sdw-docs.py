#!/usr/bin/env python3
from pathlib import Path
import argparse
import sys

REQUIRED_LONG_LIVED_DOCS = [
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

REQUIRED_CURRENT_TARGET_DOCS = [
    'scope-baseline.md',
    'requirements.md',
    'constraints.md',
    'milestones.md',
    'implementation-plan.md',
    'task-breakdown.md',
    'risks.md',
    'open-questions.md',
    'review-notes.md',
    'change-log.md',
]

REQUIRED_HANDOFF_DOCS = [
    'handoff/agent-entry.md',
    'handoff/execution-brief.md',
    'handoff/openspec-handoff.md',
]

MIN_NON_EMPTY_CHARS = 20


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description='Validate software-design-workflow docs in a project.')
    parser.add_argument('docs_dir', nargs='?', default='docs', help='Path to the generated docs directory. Default: docs')
    parser.add_argument('--target', default='current-target', help='Target directory under releases. Default: current-target')
    return parser.parse_args()


def check_file(path: Path, label: str, errors: list[str]) -> None:
    if not path.exists():
        errors.append(f'{label} missing: {path}')
        return
    if not path.is_file():
        errors.append(f'{label} is not a file: {path}')
        return
    text = path.read_text(errors='replace').strip()
    if len(text) < MIN_NON_EMPTY_CHARS:
        errors.append(f'{label} is obviously empty: {path}')


def main() -> int:
    args = parse_args()
    docs_dir = Path(args.docs_dir).resolve()
    errors: list[str] = []

    if not docs_dir.exists():
        errors.append(f'docs directory missing: {docs_dir}')
    elif not docs_dir.is_dir():
        errors.append(f'docs path is not a directory: {docs_dir}')

    for rel in REQUIRED_LONG_LIVED_DOCS:
        check_file(docs_dir / rel, 'required long-lived doc', errors)

    target_dir = docs_dir / 'releases' / args.target
    if not target_dir.is_dir():
        errors.append(f'required current-target docs directory missing: {target_dir}')
    for rel in REQUIRED_CURRENT_TARGET_DOCS:
        check_file(target_dir / rel, 'required current-target doc', errors)

    for rel in REQUIRED_HANDOFF_DOCS:
        check_file(docs_dir / rel, 'required handoff doc', errors)

    agent_entry = docs_dir / 'handoff' / 'agent-entry.md'
    check_file(agent_entry, 'agent entry point', errors)
    if agent_entry.exists():
        agent_entry_text = agent_entry.read_text(errors='replace').lower()
        if 'required reading order' not in agent_entry_text:
            errors.append('docs/handoff/agent-entry.md must include Required Reading Order')

    if errors:
        print('Software design docs validation failed:')
        for error in errors:
            print(f'- {error}')
        return 1

    print('Software design docs validation passed')
    return 0


if __name__ == '__main__':
    sys.exit(main())
