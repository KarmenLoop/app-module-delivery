# Module design template

A module may span screens or be headless. Combine short records and avoid speculative abstractions.

## Identity and responsibility

- Module ID/name, owner, requirements, acceptance: [fill]
- User/caller and business outcome: [fill]
- Owned rules and data: [fill]
- Excluded responsibilities and their providers/interfaces: [fill]
- Reuse/add/change, existing callers, compatibility constraints: [fill]

## Interface: everything callers must know

| Capability/entry | Input/validation | Actor/resource access | Output/completion | Errors/unknown outcomes | State/side effects | Concurrency/idempotency/cancellation |
| --- | --- | --- | --- | --- | --- | --- |
| [function/HTTP/IPC/event/command] | [fill] | [fill] | [fill] | [fill] | [fill] | [fill] |

Configuration, ordering, version, relevant performance, compatibility/deprecation: [fill]. Callers should not have to coordinate private internal steps.

## Implementation and dependencies

- Internal rules, structures, coordination: [fill]
- Substitution seams, actual adapters, justification: [fill]
- Code/runtime/data/sequence dependencies and failure behavior: [fill]
- Assembly, construction, start, subscribe, suspend, resume, close, release: [fill]
- Ownership of files, connections, tasks, devices, timers: [fill]

## Data, state, recovery

- Entities, fields, relationships, authority, constraints: [fill]
- Transactions, audit, concurrent edits, partial success: [fill]
- Presentation/business/task/sync/session ownership: [fill]
- Initial/allowed/terminal states, actor, persistence, observation: [fill]
- Timeout, failure, retry, cancel, undo, restart, data recovery: [fill]
- Migration, coexistence, cutover, rollback conditions: [fill]

## Targets and presentation

Per-target entry, shared contracts/code, specific implementation, permissions, limitations, alternatives: [fill]. Link an [Interaction contract](interaction-contract.md) where applicable; otherwise specify caller feedback, diagnostics, and operational observation.

## Implementation and acceptance

| Increment | Prerequisites | Change locations | Observable completion | Check/environment | Acceptance ID | Actual evidence |
| --- | --- | --- | --- | --- | --- | --- |
| [fill] | [fill] | [fill] | [fill] | [fill] | [fill] | [not executed] |

Existing failures, unresolved items, next step and rationale: [fill].
