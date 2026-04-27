# Architecture

A command parser invokes scanner, rule engine, classifier, and report writer components in one local process.

Boundaries are kept in-process for the first target, with external dependencies isolated behind adapters.
