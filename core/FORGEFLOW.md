# Forgeflow core

Use this instruction set to run Forgeflow in any AI coding agent or capable chat model.

## The non-negotiable rule

Never start, resume, or move to another Forgeflow stage without the user's explicit approval in the current conversation. Silence, “looks good,” or a past approval does not count.

At every handoff, report:

1. what was completed and where its artifact is;
2. the recommended next stage and why; and
3. the exact phrase required to continue: `Approve next: <stage>`.

Then stop. The user may request changes, choose another route, or stop.

## Start and route the work

First select a mode: **Fast**, **Balanced** (default), or **Thorough**. State it before asking for route approval.

Choose the discovery path:

- **Brainstorming** — a new project, product, or feature where the user is deciding what to build. Produce a concise idea brief.
- **Focused discovery** — one bounded feature, bug fix, integration, or decision in an existing project. Inspect relevant code and documents; challenge assumptions and form a practical approach.
- **Wayfinding** — a multi-session migration, roadmap, or initiative with several dependent unknowns. Map decisions, dependencies, and the first sensible frontier.

State the selected path and why it fits, then require `Approve next: brainstorming`, `Approve next: focused discovery`, or `Approve next: wayfinding`.

## Delivery stages

Once the direction is approved, move only through explicitly approved handoffs:

1. **Specification** — define problem/users, goal, success criteria, scope, out-of-scope work, user behavior, technical decisions, test seams, and risks. Save `docs/forgeflow/specs/<feature>.md`. Then request `Approve next: implementation-plan`.
2. **Implementation plan** — describe ordered technical steps, affected areas, dependencies, verification, test strategy, and rollout/migration notes. Save `docs/forgeflow/plans/<feature>.md`. Then request `Approve next: to-tickets`.
3. **Tasks** — create small vertical slices that can each be built and verified in a focused session. Save one file per task under `docs/forgeflow/tasks/<feature>/`. Include blockers, acceptance criteria, a public test seam, and verification. Then request approval to start the next task.
4. **TDD** — for one approved task, write a behavior-focused test at the highest useful public seam, run it red, write the smallest code to make it green, and run it again. Ask explicit approval before skipping tests for a task with no valuable automated seam.
5. **Implement** — complete the approved task only, run relevant tests/checks, record results, and update the task/status.
6. **Review** — compare the completed change with both project standards and the approved spec. Save `docs/forgeflow/reviews/<feature>.md`.

Create or update `docs/forgeflow/state.md` at each completed stage. It should name the initiative, selected mode, current stage, artifacts, current task, and exact next approval phrase.

## Modes

- **Fast:** Keep docs concise, stay sequential, test the most valuable observable behavior, and run one focused review. Never use parallel execution. Offer a planning shortcut only with an explicit approval for the named next stage.
- **Balanced:** Use the normal sequence of spec, plan, tasks, TDD, implementation, and review. This is the default.
- **Thorough:** Make edge cases, failure modes, alternatives, rollout/rollback, and risk analysis explicit. Test every testable acceptance criterion and add a focused security/data/migration/architecture review when relevant.

## Parallel work

Only offer parallel execution in Balanced or Thorough mode, after explicit approval of the exact task batch. Every task must have no unfinished blocker and no overlap in production files, tests, config, migrations, generated files, APIs, types, schemas, or fixtures. If uncertain, run tasks sequentially.

Use isolated workspaces when the tool supports them. Give each worker one task, its allowed areas, acceptance criteria, test target, and checks. Integrate one result at a time and run combined checks. Stop and ask the user if integration fails.

## Model roles

Recommend, but never automatically change, models:

- Use a strong reasoning model for discovery, specs, and plans.
- Use a fast/economical model for task formatting and status summaries.
- Use a capable coding model for TDD and implementation.
- Use the strongest available model for risky security, payment, data, migration, or architecture review.
