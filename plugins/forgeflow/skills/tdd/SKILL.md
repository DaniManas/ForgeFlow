---
name: tdd
description: Build one approved Forgeflow task using test-driven development. Use when a task is ready to implement, the user asks for test-first work, or they mention red-green-refactor.
---

# Test-Driven Development

Use TDD for one concrete behavior from an approved local task. It is not a planning stage and it does not write every test for the whole feature in advance.

## Before coding

1. Read the task, its acceptance criteria, the linked spec, and `docs/forgeflow/state.md` when present.
2. Find the highest public seam through which the behavior can be observed. Follow existing project test patterns.
3. State the seam and the one behavior for this cycle. If the seam is uncertain, ask one question and stop.

## Red → green

For each small behavior:

1. Write one behavior-focused test using an independently known expected result.
2. Run it and confirm that it fails for the expected reason.
3. Write only enough production code to make it pass.
4. Run the focused test again. Keep it green before starting another behavior.

Test public behavior, not private methods or implementation details. Do not mock internal collaborators merely to make a test convenient.

## Completion gate

When the task's relevant behaviors are covered and passing, report the tests added and the commands run. Update the local task and workflow state to `tdd complete`. Then recommend `implement` and stop.

Require: `Approve next: implement <task reference>`.

For a copy-only, visual-only, or configuration-only task where an automated test would not add useful confidence, explain why and ask whether to skip TDD. Never skip it silently.
