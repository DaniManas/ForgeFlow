---
name: to-tickets
description: Break an approved Forgeflow implementation plan into small, ordered local task files with dependencies and acceptance criteria. Use after implementation-plan and before TDD.
---

# To Tickets

Turn the approved plan into local, tracer-bullet tasks. GitHub Issues are optional exports, never a prerequisite.

## Process

1. Read the approved spec, implementation plan, and workflow state.
2. Create small vertical slices: each task should deliver a testable user-facing behavior, fit in one focused session, and state only genuine blockers.
3. Present the numbered breakdown and ask the user to approve its granularity and dependency edges.
4. After approval, create one task file per item under `docs/forgeflow/tasks/<feature-slug>/`, in dependency order.
5. Update `docs/forgeflow/state.md` with the task directory, first ready task, and next approval.

Avoid horizontal tasks such as “build all APIs” or “write all tests.” Keep each task narrow but complete across the layers it actually needs.

## Task template

```markdown
# <NN> — <Task title>

**Status:** ready

**Blocked by:** None — can start immediately

## What this delivers

The end-to-end behavior a user can observe.

## Acceptance criteria

- [ ] Criterion 1
- [ ] Criterion 2

## TDD target

- Public seam:
- First behavior to test:

## Verification

- Relevant test command:
- Other checks:
```

## Choose execution mode

After creating approved task files, inspect the ready tasks for real independence: no blockers, no shared files, no shared API/type/schema/configuration/migration, and no shared test fixture or generated artifact. If any overlap is unclear, treat the tasks as dependent.

For dependent work, recommend the first task's TDD and stop.

Require: `Approve next: tdd <task reference>`.

For a batch of two or more truly independent tasks, list the exact task references and expected code areas, recommend `parallel-execution`, and stop.

Require: `Approve next: parallel execution <task references>`.
