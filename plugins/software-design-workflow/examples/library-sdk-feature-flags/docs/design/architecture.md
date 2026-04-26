# Architecture

A parser validates config, an evaluator applies targeting rules, and public API wrappers expose typed helpers.

Boundaries are kept in-process for the first target, with external dependencies isolated behind adapters.
