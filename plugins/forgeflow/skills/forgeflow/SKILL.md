---
name: forgeflow
description: Start an engineering workflow and route the work to product brainstorming, focused planning, or large-scale wayfinding. Use when a user wants to turn an idea into reviewed code but is unsure which path fits.
---

# Forgeflow

Forgeflow is the front door to this plugin. It chooses the right discovery path, keeps a local record of the work, and moves through the delivery flow only with explicit approval.

## Strict approval rule

Never start, resume, or transition to another skill without the user's explicit approval in the current conversation. Silence, a vague “looks good”, or an earlier approval does not count.

At every handoff, state:

1. the completed stage and its artifact or decision;
2. the recommended next skill and why it is next; and
3. the exact approval phrase the user must send, in the form `Approve next: <skill-name>`.

Stop after that message. Do not invoke, simulate, or begin the next skill until the user sends the requested approval phrase. A user can instead ask for changes, choose a different route, or stop the workflow.

## Local-first artifacts

Use local files by default. Never require GitHub Issues or another tracker.

- Idea briefs: `docs/forgeflow/briefs/`
- Specs: `docs/forgeflow/specs/`
- Implementation plans: `docs/forgeflow/plans/`
- Tasks: `docs/forgeflow/tasks/<feature-slug>/`
- Reviews: `docs/forgeflow/reviews/`
- Current workflow state: `docs/forgeflow/state.md`

Create or update the state file at each completed stage using `references/state-template.md`. Offer exporting tasks to an external tracker only when the user asks.

## Model playbook

Model selection remains the user's choice in Codex; do not claim to switch it automatically. Recommend these settings before a stage begins:

- **Sol, medium:** brainstorming, grill-with-docs, wayfinder, specs, and implementation plans.
- **Luna, medium:** task formatting, state updates, summaries, and documentation cleanup.
- **Terra, medium:** TDD, implementation, and normal code review.
- **Sol, high:** optional review of risky changes involving security, auth, payments, sensitive data, migrations, or major architecture.

When the user requests a fast path, recommend fewer planning artifacts. When they request a thorough path, retain every stage and propose risk review where relevant. Default to **Balanced**.

## Route the work

Inspect the user's request and, when relevant, the project context.

Choose **brainstorming** when the user is deciding *what to build*. This includes a new project or product idea, a new application whose direction is unclear, or a request to compare alternative product or architecture approaches. Brainstorming explores options, presents a design for approval, and creates an idea brief before the formal spec.

Choose **grill-with-docs** when the user has a bounded change they want to understand and shape now. This is the default for an existing project. It works best for one feature, bug fix, integration, or decision that can be clarified in the current conversation.

Choose **wayfinder** when the destination is broad or unclear enough that the work will probably span multiple sessions. Route here when two or more of these are true:

- It affects several systems, teams, or major modules.
- Important decisions are still unknown and depend on one another.
- The user asks for a roadmap, migration, programme, or long-running initiative.
- A sensible plan cannot yet fit in one session.

If the request is on the boundary, ask one question: “Are we deciding what to build, defining one change to start now, or mapping delivery for a larger initiative that will take several sessions?” Recommend the route you think fits.

State the choice plainly: “Forgeflow route: brainstorming”, “Forgeflow route: grill-with-docs”, or “Forgeflow route: wayfinder.” Explain why it fits, then stop and request `Approve next: <selected-skill>`. Only after that approval may you follow the selected skill's instructions.

## Continue after planning

After **brainstorming**, recommend `to-spec` when its idea brief is approved. Do not continue automatically.

Once **grill-with-docs** or **wayfinder** produces a clear, bounded change, recommend this sequence as appropriate, one explicitly approved stage at a time:

1. `to-spec` to capture the agreed work and success criteria.
2. `implementation-plan` to map the technical delivery steps.
3. `to-tickets` to create small, ordered local tasks.
4. `tdd` for the specific behavior in each approved task.
5. `implement` to finish that task and verify it.
6. `code-review` to check the complete change against standards and the original spec.

Do not force every step: short changes may not need tickets, and Wayfinder should remain in planning mode until the route is clear. In every case, stop for approval before the next stage.
