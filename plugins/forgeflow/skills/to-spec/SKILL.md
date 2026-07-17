---
name: to-spec
description: Turn an agreed Forgeflow idea or change into a local specification with scope, success criteria, testing decisions, and constraints. Use after brainstorming, grill-with-docs, or wayfinder.
---

# To Spec

Synthesize the approved conversation and project context into one durable, local spec. Do not interview the user again unless a required decision is genuinely missing.

## Process

1. Inspect the project, its vocabulary, relevant ADRs, and existing test patterns.
2. Identify the highest public test seams. Confirm them with the user if they were not agreed already.
3. Write `docs/forgeflow/specs/<feature-slug>.md` using the template below.
4. Create or update `docs/forgeflow/state.md` using `../forgeflow/references/state-template.md`; record the spec path and current decision.
5. Present the spec for approval. Do not create the implementation plan yet.

## Mode depth

- **Fast:** Write a concise, buildable spec: goal, scope, observable behavior, acceptance criteria, test seam, and material risk. Do not omit a constraint that could change implementation.
- **Balanced:** Use the full template below.
- **Thorough:** Use the full template and make edge cases, failure modes, rollout concerns, assumptions, and unresolved decisions explicit.

## Spec template

```markdown
# <Feature> specification

## Problem and users

## Goal and success criteria

## In scope

## Out of scope

## User-facing behavior

## Technical and architectural decisions

## Data, API, and error-handling decisions

## Testing decisions
- Public seams:
- Behaviors that require tests:
- Existing testing patterns to follow:

## Risks, assumptions, and open questions
```

## Approval gate

After the user approves the spec, update state to `spec approved` and stop. In Fast mode, if the change is genuinely small and already has an obvious technical path, explain why an implementation plan would add little value and offer the explicit shortcut to `to-tickets`; otherwise recommend `implementation-plan`. Balanced and Thorough recommend `implementation-plan`.

Require: `Approve next: implementation-plan`.

For an approved Fast-mode shortcut, require: `Approve next: to-tickets`.
