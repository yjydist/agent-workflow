# Service adapter

## Layer

Kind

## Applies when

Use when the software runs as a networked or background capability for other clients, applications, or systems.

## Design focus

Define service responsibilities, API boundaries, persistence, authorization, failure behavior, scaling assumptions, and operational ownership.

## Expected artifacts

Service boundary, API contracts, data responsibilities, deployment-runtime, quality and observability notes.

## Legacy migration

Legacy `backend-api` maps to `service + http-api + server`. Reuse API, auth, database, and deployment templates as service design sections.
