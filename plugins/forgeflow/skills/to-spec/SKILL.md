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

After the user approves the spec, update state to `spec approved`, recommend `implementation-plan`, and stop.

Require: `Approve next: implementation-plan`.
