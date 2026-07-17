---
name: implementation-plan
description: Turn an approved Forgeflow spec into a local, ordered technical implementation plan. Use after to-spec and before to-tickets.
---

# Implementation Plan

Create the bridge between an approved spec and small build tasks. Do not write production code or create tickets in this skill.

## Process

1. Read the approved spec in `docs/forgeflow/specs/` and inspect relevant code, conventions, tests, and ADRs.
2. List the implementation steps in dependency order. Explain the purpose, likely modules or boundaries, data/API changes, risks, migrations, and verification for each step.
3. Keep the plan technical but durable: describe responsibilities and interfaces rather than brittle line-by-line edits.
4. Save it as `docs/forgeflow/plans/<feature-slug>.md`.
5. Update `docs/forgeflow/state.md` with the plan path and status `plan approved` only after the user approves it.

## Plan template

```markdown
# <Feature> implementation plan

## Goal

## Preconditions and risks

## Ordered steps

### 1. <Step>
- Purpose:
- Areas affected:
- Dependencies:
- Verification:

## Test strategy

## Rollout or migration notes
```

## Approval gate

Present the plan for review. After the user approves it, recommend `to-tickets` and stop.

Require: `Approve next: to-tickets`.
