# Project Documentation Index

## Current Status

- Project type: TODO
- Current stage: idea / classified / interviewed / docs-generated / docs-reviewed / v1-frozen / implementation-planned / ready-for-coding
- V1 status: not frozen / frozen

## Required Reading Order for Coding Agent

1. `meta/project-context.md`
2. `product/overview.md`
3. `product/scope.md`
4. `requirements/functional-requirements.md`
5. `requirements/business-rules.md`
6. `design/domain-model.md`
7. `design/architecture.md`
8. `design/data-design.md`
9. `design/interface-contracts.md`
10. `design/security-and-permissions.md`
11. `design/error-handling.md`
12. `delivery/implementation-plan.md`
13. `delivery/acceptance-criteria.md`

## Directory Responsibilities

- `meta/`: project context, decisions, change log
- `product/`: product goal, scope, users and scenarios
- `requirements/`: functional and non-functional requirements, business rules
- `design/`: domain model, architecture, data, interfaces, security, errors
- `type-specific/`: project-type-specific docs
- `delivery/`: implementation plan, test plan, acceptance criteria
- `review/`: review notes, risks, open questions

## Coding Rules

- Before writing code, `Current stage` 必须是 `ready-for-coding`.
- Before writing code, `V1 status` 必须是 `frozen`.
- Before writing code, review `Blocking Issues` and blocking open questions must be resolved or explicitly moved out of V1.
- Before writing code, implementation plan must be reviewed and confirmed by the user.
- Do not implement features outside V1 scope.
- If docs conflict, stop and report the conflict.
- If a required behavior is TODO, ask for clarification or move it out of V1.
- Implement one phase at a time.
