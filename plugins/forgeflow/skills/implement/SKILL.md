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
5. Do not create a commit unless the user explicitly asked Forgeflow to manage commits or approves a disclosed execution mode that requires task-local commits.

## Approval gate

If another unblocked task remains, reassess the ready tasks. Recommend `parallel-execution` only in Balanced or Thorough mode and only when two or more tasks are demonstrably independent; otherwise report the completed task and recommend TDD for the next task. In Fast mode, remain sequential.

Ask whether to start TDD for the named next task, then stop. A clear affirmative reply to that pending confirmation is sufficient.

For an eligible independent batch, disclose the exact batch and its worktree, branch, subagent, and commit side effects; ask whether to start `parallel-execution`; then stop. A clear affirmative reply authorizes only that batch.

If every task is complete, report the implementation and verification summary, recommend `code-review`, and stop.

Ask: “All implementation tasks are complete. May I start `code-review`?” Then stop. A clear affirmative reply to this pending confirmation is sufficient.
