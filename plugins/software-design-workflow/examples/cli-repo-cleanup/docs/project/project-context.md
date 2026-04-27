# Project Context

This example demonstrates a handoff-ready package for a local CLI target. The design package must be complete enough that an implementation agent can build the bounded target without inventing missing docs.

The central constraint is trust: every command remains read-only, path traversal stays within the repository root, and unsafe filesystem situations are reported instead of acted on.
