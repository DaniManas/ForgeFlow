---
name: parallel-execution
description: Execute a user-approved batch of truly independent local Forgeflow tasks with isolated subagents, then integrate and verify their combined work. Use only after to-tickets identifies two or more independent tasks and the user approves parallel execution.
---

# Parallel Execution

Create temporary, task-specific subagents only after the user explicitly approves the exact task batch. Do not create permanent agents in advance.

Do not recommend or run parallel execution in **Fast** mode. It can shorten elapsed time, but it consumes more total tokens. In Balanced and Thorough modes, it remains an opt-in path subject to every eligibility rule below.

## Eligibility check

Before recommending this skill, verify every task in the batch:

- has no unfinished blockers;
- has no overlapping production files, test files, configuration, migrations, or generated artifacts;
- does not define an API, type, schema, or shared fixture that another batch task consumes; and
- can be tested without relying on another batch task's changes.

If any condition is uncertain, recommend sequential execution instead. Two tasks that merely sound separate are not enough.

## Approval gate

Show the exact task references, files/areas expected to change, and the integration check. Then require:

`Approve next: parallel execution <task references>`

That approval authorizes only the named batch and its task-local TDD → implementation loop. It does not authorize another task, a later batch, or code review.

## Dispatch

For each approved task:

1. Create an isolated git worktree and branch. If isolation is unavailable, do not run concurrent edits in one checkout; fall back to sequential execution.
2. Give one subagent only its task file, linked spec section, acceptance criteria, TDD target, allowed files/areas, test commands, and completion-report format.
3. Require the subagent to use TDD, make no out-of-scope changes, run its focused checks, and commit its work in its own worktree.

Never assign the same file or shared contract to two subagents.

## Integrate

The main agent integrates subagent branches one at a time, resolves any conflict deliberately, and runs the combined typecheck, tests, and relevant integration checks. Update every task file and `docs/forgeflow/state.md` with outcomes.

If integration fails, stop, explain the failure, and ask the user whether to repair sequentially. Do not silently retry by changing scope.

## Completion gate

If more ready tasks remain, reassess their dependencies and recommend either another explicitly named parallel batch or the next sequential TDD task. If no tasks remain, recommend `code-review`.
