# Project Documentation Index

## Current Status

- Project type: TODO
- Current stage: idea / classified / interviewed / docs-generated / docs-reviewed / v1-frozen / implementation-planned / ready-for-coding
- V1 status: not frozen / frozen

## Required Reading Order for Coding Agent

1. `meta/project-context.md`
2. `product/overview.md`
3. `product/users-and-scenarios.md`
4. `product/scope.md`
5. `requirements/functional-requirements.md`
6. `requirements/non-functional-requirements.md`
7. `requirements/business-rules.md`
8. `design/domain-model.md`
9. `design/architecture.md`
10. `design/data-design.md`
11. `design/interface-contracts.md`
12. `design/security-and-permissions.md`
13. `design/error-handling.md`
14. `review/review-notes.md`
15. `review/open-questions.md`
16. `type-specific/<project-type>/...` for all docs generated for the active project type. When generating a concrete project, expand this into explicit file entries.
17. `delivery/implementation-plan.md`
18. `delivery/test-plan.md`
19. `delivery/acceptance-criteria.md`

## Directory Responsibilities

- `meta/`: project-spec context, decisions, change log
- `product/`: product goal, scope, users and scenarios
- `requirements/`: functional and non-functional requirements, business rules
- `design/`: domain model, architecture, data, interfaces, security, errors
- `review/`: review notes, risks, open questions
- `type-specific/`: project-type-specific docs that must be expanded into the reading order for the active project type
- `delivery/`: implementation plan, test plan, acceptance criteria

## Coding Rules

- Before writing code, `Current stage` 必须是 `ready-for-coding`.
- Before writing code, `V1 status` 必须是 `frozen`.
- Before writing code, review `Blocking Issues` and blocking open questions must be resolved or explicitly moved out of V1.
- Before writing code, all docs for the active project type under `type-specific/` must be read.
- Before writing code, implementation plan must be reviewed and confirmed by the user.
- Do not implement features outside V1 scope.
- If docs conflict, stop and report the conflict.
- If a required behavior is TODO, ask for clarification or move it out of V1.
- Implement one phase at a time.
