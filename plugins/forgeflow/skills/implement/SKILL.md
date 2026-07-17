---
name: implement
description: Implement one approved local Forgeflow task after its TDD cycle is complete. Use after tdd to finish the task, verify it, and prepare the next approved handoff.
---

# Implement

Implement one task only. Read its task file, linked spec, workflow state, and the tests created during TDD. Keep work within the approved acceptance criteria.

## Process

1. Confirm the TDD cycle for this task is complete. If it was explicitly skipped, record the user's approval and reason in the task file.
2. Finish the task using the smallest maintainable change. Do not add speculative features.
3. Run the focused tests, project typecheck/lint as applicable, and relevant integration checks. Run the full suite when practical before the final task of the feature.
4. Mark completed acceptance criteria and record commands/results in the task file. Update `docs/forgeflow/state.md`.
5. Commit the task when the repository uses git and the user has not asked to defer commits.

## Approval gate

If another unblocked task remains, reassess the ready tasks. Recommend `parallel-execution` only in Balanced or Thorough mode and only when two or more tasks are demonstrably independent; otherwise report the completed task and recommend TDD for the next task. In Fast mode, remain sequential.

Require: `Approve next: tdd <next task reference>`.

For an eligible independent batch, instead require: `Approve next: parallel execution <task references>`.

If every task is complete, report the implementation and verification summary, recommend `code-review`, and stop.

Require: `Approve next: code-review`.
