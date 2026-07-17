---
name: implement
description: "Implement a piece of work based on a spec or set of tickets."
disable-model-invocation: true
---

Implement the work described by the user in the spec or tickets.

Use /tdd where possible, at pre-agreed seams.

Run typechecking regularly, single test files regularly, and the full test suite once at the end.

Once done, do not start code review automatically. Summarize the implementation, commit, and verification results; recommend `code-review`; then stop and wait for the explicit message `Approve next: code-review`.

Commit your work to the current branch.
