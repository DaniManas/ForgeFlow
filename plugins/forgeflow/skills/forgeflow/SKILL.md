---
name: forgeflow
description: Start an engineering workflow and route the work to product brainstorming, focused planning, or large-scale wayfinding. Use when a user wants to turn an idea into reviewed code but is unsure which path fits.
disable-model-invocation: true
---

# Forgeflow

Forgeflow is the front door to this plugin. It chooses the right discovery or planning path before work is specified or built.

## Strict approval rule

Never start, resume, or transition to another skill without the user's explicit approval in the current conversation. Silence, a vague “looks good”, or an earlier approval does not count.

At every handoff, state:

1. the completed stage and its artifact or decision;
2. the recommended next skill and why it is next; and
3. the exact approval phrase the user must send, in the form `Approve next: <skill-name>`.

Stop after that message. Do not invoke, simulate, or begin the next skill until the user sends the requested approval phrase. A user can instead ask for changes, choose a different route, or stop the workflow.

## Route the work

Inspect the user's request and, when relevant, the project context.

Choose **brainstorming** when the user is deciding *what to build*. This includes a new project or product idea, a new application whose direction is unclear, or a request to compare alternative product or architecture approaches. Brainstorming explores options, presents a design for approval, and creates a formal design document before implementation planning.

Choose **grill-with-docs** when the user has a bounded change they want to understand and shape now. This is the default for an existing project. It works best for one feature, bug fix, integration, or decision that can be clarified in the current conversation.

Choose **wayfinder** when the destination is broad or unclear enough that the work will probably span multiple sessions. Route here when two or more of these are true:

- It affects several systems, teams, or major modules.
- Important decisions are still unknown and depend on one another.
- The user asks for a roadmap, migration, programme, or long-running initiative.
- A sensible plan cannot yet fit in one session.

If the request is on the boundary, ask one question: “Are we deciding what to build, defining one change to start now, or mapping delivery for a larger initiative that will take several sessions?” Recommend the route you think fits.

State the choice plainly: “Forgeflow route: brainstorming”, “Forgeflow route: grill-with-docs”, or “Forgeflow route: wayfinder.” Explain why it fits, then stop and request `Approve next: <selected-skill>`. Only after that approval may you follow the selected skill's instructions.

## Continue after planning

After **brainstorming**, do not continue into this sequence automatically. It proposes its detailed implementation-planning handoff and waits for approval.

Once **grill-with-docs** or **wayfinder** produces a clear, bounded change, recommend this sequence as appropriate, one explicitly approved stage at a time:

1. `to-spec` to capture the agreed work.
2. `to-tickets` to break the work into small, ordered pieces.
3. `implement` to build the pieces.
4. `code-review` to check the result against standards and the original intent.

Do not force every step: short changes may not need tickets, and Wayfinder should remain in planning mode until the route is clear. In every case, stop for approval before the next stage.
