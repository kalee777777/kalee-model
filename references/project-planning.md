# Project planning — trial playbook

Turn a selected direction into work that can be verified. If the direction remains undecided, plan the validation phase. If the user has authorized implementation, proceed within that scope.

## Read the existing work first

Inspect the user's project records, task system and relevant decision log. Reuse existing milestones, identify duplicate work, unresolved commitments and resource conflicts. New ideas belong in the backlog unless the user chooses to prioritize them. Do not silently replace committed work with a new initiative.

Prepare a short project charter: beneficiary, business result, scope, exclusions, reusable assets, constraints, dependencies, owner and acceptance authority. Unknown budget or capacity calls for a conditional plan, not an invented deadline.

## Plan work around evidence of completion

For each work package, specify:

| Field | What it establishes |
|---|---|
| Deliverable | A concrete artifact, tested workflow or observable result |
| Owner | Agent execution, human judgment, or an external dependency; do not assign unconfirmed collaborators |
| Dependencies | Prerequisites and the condition that unblocks the work |
| Effort and timing | Supported estimates or explicit unknowns; dates follow dependencies and real capacity |
| Acceptance | Who checks what evidence before the work is considered complete |
| Failure response | Rework, reduced scope, pause or exit condition |

Distinguish delivery acceptance (a workflow runs) from business success (it creates the intended value). The agent owns coordination and verification; the human owns consequential tradeoffs and the existing high-stakes decisions.

Use stages such as problem validation, minimum delivery, real pilot and outcome review when useful. Mature projects need not repeat every stage. Identify the critical path and shared-resource conflicts rather than treating parallel work as unlimited capacity.

## Connect to the user's actual task system

This repository provides a protocol, not a scheduler or task-service adapter. Discover the available tools and inspect their schema before writing tasks. Do not assume a specific API, project identifier, status enumeration or notification mechanism exists.

- Map work packages to existing project/task identifiers and check for duplicates before creating anything.
- Store dependencies, owners, deliverable links and acceptance criteria in fields the system supports; use its description field when necessary.
- Use the system's actual lifecycle states. A communication state such as “sent” does not prove project completion.
- Date only work that has a real schedule. Keep unselected options in the backlog.
- Read back each write to verify identity, state, dates and acceptance details. Report “plan prepared; tasks not created” if only a document was produced.
- When no task system is available, use a user-approved local task file and state the limitation. Do not claim reminders are active.

Add an outcome-review checkpoint for work entering execution. Use the existing scheduling mechanism if a date is known; otherwise record the trigger and its review owner. Creating this plan does not authorize outbound communication, purchases or commitments beyond the user's instructions.

At completion, attach acceptance evidence and run [outcome review](outcome-review.md). If business results are still pending, report successful delivery and an open business-validation checkpoint separately.
