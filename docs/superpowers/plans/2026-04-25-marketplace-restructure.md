# Marketplace Restructure Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Convert the repository from a single Claude Code plugin into a personal Claude Code marketplace containing the `project-spec` plugin.

**Architecture:** The repository root becomes the marketplace root with `.claude-plugin/marketplace.json`, root README, `plugins/README.md`, and `validate_marketplace.py`. The existing plugin files move under `plugins/project-spec/`, keeping `/project:*` slash commands unchanged while renaming the plugin manifest to `project-spec`.

**Tech Stack:** Claude Code plugin marketplace layout, JSON manifests, Python validation scripts, Markdown commands, agents, and skills.

---

### Task 1: Convert repository root into marketplace root

**Files:**
- Modify: `.claude-plugin/plugin.json` -> `.claude-plugin/marketplace.json`
- Create: `plugins/project-spec/`
- Move: current plugin files into `plugins/project-spec/`

- [ ] Move existing plugin directories and docs under `plugins/project-spec/`.
- [ ] Replace root plugin manifest with marketplace manifest named `agent-workflow`.
- [ ] Rename plugin manifest inside `plugins/project-spec/.claude-plugin/plugin.json` to `project-spec`.
- [ ] Keep slash command namespace `/project:*` unchanged.

### Task 2: Add marketplace docs and validator

**Files:**
- Modify: `README.md`
- Create: `plugins/README.md`
- Create: `validate_marketplace.py`
- Modify: `plugins/project-spec/README.md`
- Modify: `plugins/project-spec/USAGE.md`

- [ ] Root README documents the marketplace, install commands, plugin list, and validation.
- [ ] `plugins/README.md` documents plugin naming and current plugin index.
- [ ] `validate_marketplace.py` validates marketplace manifest, all plugin sources, plugin manifest name consistency, and runs each plugin validator.
- [ ] Plugin README and USAGE say the plugin root is `plugins/project-spec/`.

### Task 3: Verify migration

**Files:**
- Modify: `validate_marketplace.py`
- Modify: `plugins/project-spec/validate_plugin.py` only if path assumptions fail.

- [ ] Run `python3 validate_marketplace.py` and expect pass.
- [ ] Run `python3 plugins/project-spec/validate_plugin.py` and expect pass.
- [ ] Run `git status --short` to inspect moved and new files.
