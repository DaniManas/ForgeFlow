---
name: wayfinder
description: Map a large, multi-session initiative as local decision files, resolving uncertainty until one bounded change is ready for specification.
---

# Wayfinder

Use Wayfinder when the destination spans several systems or sessions and important decisions depend on one another. Wayfinder maps the route; it does not implement the destination.

Everything is local by default. Do not require GitHub Issues, another tracker, unavailable slash commands, or permanent agents. Export to an external tracker only when the user asks.

## Artifacts

For initiative `<initiative-slug>`, maintain:

```text
docs/forgeflow/wayfinding/<initiative-slug>/
├── map.md
└── decisions/
    ├── 01-<decision>.md
    └── 02-<decision>.md
```

Update `docs/forgeflow/state.md` with the map path, current decision, and pending stage.

## Map format

```markdown
# <Initiative> wayfinding map

## Destination
<What becomes possible when the route is clear.>

## Constraints

## Decisions resolved
- [Decision name](decisions/NN-name.md) — one-line outcome

## Ready frontier
- [ ] [Decision name](decisions/NN-name.md)

## Blocked decisions
- [ ] [Decision name](decisions/NN-name.md) — blocked by: <name>

## Not yet clear enough to decide

## Out of scope
```

The map is an index. Keep the reasoning and final answer in the corresponding decision file rather than duplicating it in the map.

## Decision format

```markdown
# <Decision name>

**Status:** ready | claimed | resolved | out of scope
**Blocked by:** None | <decision names>
**Worked in:** <session or agent label, if useful>

## Question

## Why it matters

## Evidence and constraints

## Options considered

## Decision

## Consequences

## Newly visible decisions
```

## Chart the map

1. Inspect the project and existing documentation.
2. Ask one question at a time to name a concrete destination and its boundaries.
3. Identify decisions that can be stated precisely now. Put vague future areas under “Not yet clear enough to decide.”
4. Create decision files, then record genuine dependency edges.
5. Mark unblocked decisions as the ready frontier.
6. Present the map for review and update it until the user confirms it.
7. Stop after charting. Do not resolve a decision or begin delivery automatically.

If the entire route is already clear and fits one focused conversation, recommend `grill-with-docs` instead and ask whether to switch.

## Work through the map

Resolve one decision per normal session:

1. Read the map and choose one ready, unclaimed decision.
2. Mark it `claimed` before working so another session can avoid it.
3. Gather evidence from the codebase and local documentation. If external research or a prototype would help, explain the bounded action and obtain any permission the environment requires.
4. Present meaningful options with trade-offs and a recommendation.
5. Record the user's decision and consequences, then mark the file `resolved`.
6. Update the map: move the result to “Decisions resolved,” unblock newly ready decisions, and turn newly visible questions into files only when they are precise.

Independent research decisions may be offered as a parallel batch only when the environment supports isolated subagents and the user explicitly approves that exact batch. Otherwise, work sequentially.

## Completion gate

The map is complete when the destination is bounded and no unresolved decision blocks a formal specification.

Summarize the resolved route and identify the first buildable change. Ask the user to review the completed map. Once they confirm it, recommend `to-spec`, ask whether to start it, and stop.

A clear affirmative reply to the most recent pending confirmation is sufficient. Do not invoke `to-spec`, create implementation tasks, or begin coding automatically.
