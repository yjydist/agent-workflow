# Risks

## API drift

Small convenience changes could break the promised public result object. Mitigation: add compatibility fixtures and treat the documented result shape as a contract.

## Config ambiguity

Loose JSON rules may lead to inconsistent consumer expectations. Mitigation: validate schema during initialization and return structured errors.

## Scope expansion

Requests for hosted distribution or dashboards could pull the SDK into service territory. Mitigation: keep all network concerns out of the target.
