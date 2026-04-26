# Application adapter

## Layer

Kind

## Applies when

Use when the product is an end-user application with workflows, screens, permissions, and product-facing outcomes.

## Design focus

Clarify users, jobs-to-be-done, primary workflows, state ownership, UX boundaries, and release scope. Pair with web-ui, desktop-ui, mobile-ui, cli, or tui surfaces as appropriate.

## Expected artifacts

User journeys, navigation or interaction model, state model, permissions, acceptance boundaries.

## Legacy migration

Legacy `frontend-spa` maps to `application + web-ui + browser`. Reuse page, component, routing, and state-management templates as web application surface details rather than as a standalone project type.
