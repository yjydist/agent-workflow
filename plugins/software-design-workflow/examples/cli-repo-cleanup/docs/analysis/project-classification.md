# Project classification

## Classification summary

- Classification model: Adapter-first software design classification
- Overall confidence: High

## Kind adapters

- automation, CLI tool

## Surface adapters

- CLI commands, text report, JSON report

## Runtime adapters

- local developer workstation process

## Domain adapters

- repository maintenance, generated artifact review

## Concern adapters

- safety, explainability, dry-run behavior, filesystem permissions

## Optional legacy compatibility labels

- Legacy labels are not required for this example beyond informal search compatibility.

## Implications and rationale

A local CLI scans a repository, identifies generated or stale artifacts, and writes a reviewable cleanup plan without deleting files. The selected adapters drive discovery, design boundaries, validation strategy, and handoff tasks.
