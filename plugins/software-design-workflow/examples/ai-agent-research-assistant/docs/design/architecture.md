# Architecture

An orchestrator coordinates planning, source retrieval, note extraction, synthesis, and validation passes.

Boundaries are kept in-process for the first target, with external dependencies isolated behind adapters.
