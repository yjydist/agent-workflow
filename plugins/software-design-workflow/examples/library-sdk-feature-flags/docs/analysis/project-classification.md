# Project classification

## Classification summary

- Classification model: Adapter-first software design classification
- Overall confidence: High

## Kind adapters

- library, SDK

## Surface adapters

- public API, typed return values, examples

## Runtime adapters

- embedded in application process

## Domain adapters

- feature flag evaluation, local configuration

## Concern adapters

- API stability, type safety, deterministic evaluation, versioning

## Optional legacy compatibility labels

- Legacy labels are not required for this example beyond informal search compatibility.

## Implications and rationale

A small SDK evaluates local JSON feature flag configuration through a stable synchronous public API. The selected adapters drive discovery, design boundaries, validation strategy, and handoff tasks.
