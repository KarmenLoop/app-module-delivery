# Architecture and module design

Use the [Architecture template](../templates/architecture.md) and [Module template](../templates/module-design.md). Explain responsibility and actual execution before choosing code organization. Logical layers need not become separate processes or services.

## Three entry paths

| Assignment | Inspect first | Define | Exit condition |
| --- | --- | --- | --- |
| Greenfield | Core tasks, targets, system capabilities, data, runtime constraints | Technical route, business core, authoritative data, first complete flow, startup baseline | The first real increment can start in dependency order |
| Extension | Existing entry points, public interfaces, identity, storage, lifecycle, build/test rules | Reuse, new responsibility, integration points, contracts, regression impact | Host integration and affected regression cases are executable |
| Module change | Callers, behavior, formats, dependencies, existing failures, uncommitted work | Preserved/changed contracts, compatibility, migration, cutover, rollback conditions | Old and new behavior and data have explicit validation paths |

For narrow repairs, update only affected design. Preserve the baseline and previous failures. Adjust related structure within scope, but prepare concrete impact and alternatives before breaking compatibility, irreversible migration, or material expansion. Existing ownership and integration rules continue to apply.

## Logical architecture and runtime deployment

Produce two views:

1. Logical: module responsibilities, public contracts, dependencies, and data ownership.
2. Runtime: where code executes, how it communicates, how identity is checked, where data is stored, and where trust changes.

Distinguish presentation, business use cases, module rules, persistence, platform adaptation, and external integration where useful. A module may span screens or have no UI. Accounts, synchronization, backends, and microservices are requirements-driven choices.

Share business meaning, data contracts, and acceptance scenarios. Reuse code when languages and runtimes allow it. When separate implementations are needed, define a common contract and compatibility cases.

## Module, Interface, Implementation, Seam, Adapter

A Module exposes an Interface and contains an Implementation. The Interface includes everything callers need to use it correctly: types, prerequisites, invariants, ordering, errors, side effects, configuration, and relevant performance characteristics.

Provide complete capabilities behind a clear, reasonably small Interface. Keep related validation, transactions, concurrency, and recovery knowledge in the responsible Implementation. Do not obtain apparent simplicity by hiding essential semantics or combining unrelated responsibilities.

A Seam is a location where an implementation can be substituted. An Adapter is a concrete implementation satisfying that contract. Real platform variation, controlled external calls, or useful test stand-ins can justify a seam; avoid speculative forwarding layers. Test observable outcomes through public contracts without exposing all internals.

## Dependencies

| Kind | Record |
| --- | --- |
| Code | Public contracts used and any inappropriate private coupling |
| Runtime | Identity, database, network, processes, devices, permissions, configuration |
| Data | Required entities, owners, versions, and valid states |
| Implementation order | Contracts, capabilities, migrations, and access that must exist first |

Resolve cycles by examining responsibility and genuinely shared concepts. Ask the owning module to enforce its rules when changing its data. Shared storage still needs write ownership and transaction coordination.

Test local computation directly. Use suitable isolated real storage for integration. Check transport and business semantics for owned remote modules. Inject external or system dependencies where useful. A mock proves its covered contract, not live connectivity.

## Interfaces and data flow

For functions, HTTP, IPC, commands, or events, specify:

- Input/output semantics, constraints, identifiers, versions, and compatibility.
- Actor identity, resource ownership, and authorization at the actual execution point.
- Business steps, state changes, authoritative data, and persistence timing.
- Atomicity, partial success, concurrent edits, idempotency, and event ordering.
- Distinct errors for validation, identity/access, conflict, unsupported capability, temporary failure, and unknown outcome.
- Timeout, original-result lookup, retry, cancellation, undo, and compensation behavior.
- External side effects, confirmation, and where users inspect the result.

Trace each core scenario from entry to validation/authorization, rules, commit or external effect, receipt, and later query. Commit related atomic changes together. Track notification and synchronization outcomes separately when they can finish later. Reconcile unknown outcomes before repeating non-idempotent actions.

A cancellation request is not proof that work stopped. Specify termination, resource release, and recovery conditions.

## State and lifecycle

| State | Ownership |
| --- | --- |
| Presentation | Tabs, selections, dialogs, drafts; persist only when recovery requires it |
| Business | Entity state and invariants controlled by the responsible module |
| Task | Queueing, execution, cancellation, terminal outcome, progress, release |
| Synchronization | Pending transfer, reconciliation, conflict, failure; distinct from business commit |
| Session/access | Trusted identity and authorization, including expiry and revocation |

For important state, define initial/allowed/terminal states, conditions, actor, persistence, observation, failure, and recovery. A cache is not automatically a second authority. Define conflicts where multiple writers exist. Persist execution state for tasks that actually need restart recovery.

Address construction, assembly, startup, subscriptions, suspension/resumption, closure, and release as applicable. Assign ownership of files, devices, connections, timers, and tasks. Check behavior after module unload and identity changes.

## Platforms and migration

Create a capability matrix for the actual targets: tasks, implementation location, shared contracts, platform adapters, permission needs, limitations, alternatives, and acceptance environments. A smaller window changes presentation, not the underlying capability contract. Unsupported targets need explicit limits.

For changes, identify callers and data, compatibility policy, old-format handling, coexistence, migration, cutover, and rollback prerequisites. An older binary does not necessarily understand newly migrated data. Validate data before and after migration.

## Architecture exit

Explain which module owns every requirement, where data originates and persists, who may operate on it, how failure/restart behaves, how each target uses it, and which ready increment is next. Keep diagrams, contracts, inventories, and unresolved dependencies consistent.
