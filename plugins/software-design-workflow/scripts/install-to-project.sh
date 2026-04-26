#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

print_help() {
  cat <<'EOF'
Usage: install-to-project.sh [project_dir] [--docs-dir <dir> | --docs-dir=<dir>] [--overwrite] [--help]

Initialize software-design-workflow docs into a project, then validate the generated docs directory.
EOF
}

PROJECT_DIR="."
DOCS_DIR="docs"
POSITIONAL_SET=false
INIT_ARGS=()

while [[ $# -gt 0 ]]; do
  case "$1" in
    --help|-h)
      print_help
      exit 0
      ;;
    --docs-dir)
      if [[ $# -lt 2 ]]; then
        echo "Error: --docs-dir requires a value." >&2
        exit 1
      fi
      DOCS_DIR="$2"
      INIT_ARGS+=("--docs-dir" "$DOCS_DIR")
      shift 2
      ;;
    --docs-dir=*)
      DOCS_DIR="${1#--docs-dir=}"
      if [[ -z "$DOCS_DIR" ]]; then
        echo "Error: --docs-dir requires a value." >&2
        exit 1
      fi
      INIT_ARGS+=("--docs-dir" "$DOCS_DIR")
      shift
      ;;
    --overwrite)
      OVERWRITE=true
      INIT_ARGS+=("--overwrite")
      shift
      ;;
    --*)
      echo "Error: unsupported option: $1" >&2
      print_help >&2
      exit 1
      ;;
    *)
      if [[ "$POSITIONAL_SET" == true ]]; then
        echo "Error: unexpected extra positional argument: $1" >&2
        print_help >&2
        exit 1
      fi
      PROJECT_DIR="$1"
      POSITIONAL_SET=true
      shift
      ;;
  esac
done

python3 "$SCRIPT_DIR/init-docs.py" "$PROJECT_DIR" "${INIT_ARGS[@]}"
RESOLVED_DOCS_DIR="$(python3 -c 'from pathlib import Path; import sys; print(Path(sys.argv[1]).resolve() / sys.argv[2])' "$PROJECT_DIR" "$DOCS_DIR")"
python3 "$SCRIPT_DIR/validate-sdw-docs.py" "$RESOLVED_DOCS_DIR"
