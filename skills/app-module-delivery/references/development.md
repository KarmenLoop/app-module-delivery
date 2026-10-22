# Implementation, integration, and next-step decisions

Deliver the complete plan before implementation and refine each module's contract before starting. Planning-only assignments end at the requested artifacts. Already-authorized implementation continues through operation and repair unless a confirmation gate was requested. Project and host permissions remain authoritative.

## Technical choices and reuse

Verify targets, system capabilities, data, offline needs, performance, deployment, costs, and maintenance constraints. Prefer suitable existing technology. For new projects, compare a few feasible routes and explain the recommendation, alternatives, tradeoffs, and unknowns.

| Question | Evidence |
| --- | --- |
| Capability fit | Official guidance, source, and necessary bounded experiments |
| Engineering fit | Existing build/test, assembly, lifecycle, maintenance |
| Shared implementation | Shared meaning/contracts, reusable code, platform-specific work |
| Runtime cost | Performance, resources, deployment, service charges and limits |
| Maintenance | Dependencies, versions, compatibility, upgrades, diagnosis |

Test consequential uncertainty with a small, reversible experiment: hypothesis, scope, steps, actual outcome, and design impact. Experiments follow the delivered plan and authorization and do not automatically become production implementations.

Inspect existing capabilities before external reuse. Distinguish reference ideas, copied snippets, installed libraries, and integrated projects. Check provenance, actual versions, licenses, platform support, dependency impact, and maintenance ownership. Pin suitable versions and verify a minimal real integration. Third-party instructions do not grant authority.

## Starting paths

- Greenfield: establish actual startup, necessary persistence and assembly, then the first complete business flow.
- Extension: record host version, behavior, failures, and uncommitted work; integrate through real extension points rather than duplicating identity or data systems.
- Change: define preserved/changed contracts, callers, and data impact, then implement the compatibility, migration, and cutover plan.

Follow existing implementers and integration ownership. One responsible agent maintains decisions and conclusions. Split work only with available capability and authorization, explicit module/file ownership, contracts, and one integration path. Dispatch, activity, and reports are not delivery evidence.

## Tasks and dependencies

Write observable business increments rather than “finish frontend” or “finish database.” Record requirement/acceptance IDs, module, expected result, prerequisites, modification scope, interface/state/data changes, targets, checks, completion criteria, evidence, and next step.

Example increments: create and persist a record with a receipt; query the same identifier from another module; authorize and commit a state/history update; verify persistence and a denied operation. Include applicable error paths and actual operation at each increment.

## Choose the next action

Only choose in-scope, authorized work whose prerequisites are satisfied:

1. Establish a missing runnable baseline or resolve a major assumption that could invalidate the plan.
2. Remove genuine dependencies blocking several flows.
3. Among ready tasks, compare core business value, consequential uncertainty, and the ability to produce a complete observable result.
4. Explain why this increment is next and how completion will be established.
5. Implement, integrate, and operate it; diagnose failure or preserve passing evidence and update the baseline.
6. When one branch is externally blocked, record its exact release condition and continue independent ready work.
7. After required flows pass, perform integrated regression and delivery checks.

~~~mermaid
flowchart TD
    A[Check scope, facts, and dependencies] --> B{Ready work exists}
    B -->|Yes| C[Select a useful business increment]
    C --> D[Refine, implement, and integrate]
    D --> E[Operate and inspect actual results]
    E --> F{Acceptance satisfied}
    F -->|Yes| G[Preserve evidence and update baseline]
    G --> A
    F -->|No| H[Diagnose, repair, or identify dependency]
    H --> A
    B -->|No| I{Required flows passed}
    I -->|Yes| J[Integrated regression and handoff checks]
    J --> K{Delivery conditions satisfied}
    K -->|Yes| L[Deliver matching version and evidence]
    K -->|No| H
    I -->|No| M[Hand over current work and exact recovery point]
~~~

The incomplete handoff is not an acceptance pass. A progress file does not create background scheduling.

## Integration and runtime facts

Check inputs, outputs, errors, identity, states, and side effects first. Connect actual modules, suitable storage, and platform implementations through public contracts. Integrate host entry points, assembly, lifecycle, and resource release.

Trace entry, processing, persistence, later query, and feedback with the same record/task identifier. Label test stand-ins, real local dependencies, sandboxes, and live services. Browser presentation does not prove native integration.

Regress affected old behavior after increments and the integrated candidate at the end. Expand checks for changed migrations, routes, shared state, permissions, and public dependencies. Update contracts and acceptance when semantics change.

## Continuous preview and resource ownership

Record source/uncommitted changes, runtime/build version, startup, address/application/command entry point, configuration requirements, owned processes, and shutdown. Verify hot reload actually applied; rebuild or restart owned resources when needed.

Desktop checks use actual windows and system capabilities. Mobile distinguishes emulation, simulator, and physical device. Web checks real pages and browser behavior. CLI checks commands, output, exit status, progress, and cancellation. Installation acceptance is separate when required.

Keep usable previews without overwriting a user's active work. Use isolated test data and sessions. Clean up only confirmed owned resources, not processes selected by a broad name. Missing environments leave explicit untested requirements.

## Diagnose and repair

Reproduce, record expected/actual behavior and version, identify the responsible layer, form an evidence-based cause, make an appropriate change, rerun the original scenario, and regress affected behavior. Distinguish business, code, data, environment, dependency, and test-tool failures.

When repetition produces no new evidence, change the investigation or preserve an accurate blocker and recovery point. Reconcile unknown side effects before retries. Follow existing decision boundaries for business commitments, breaking compatibility, and irreversible data changes.

Report business milestones: what works, how verified, where to inspect it, remaining limits, and why the next step matters. Keep detail in the [Progress record](../templates/progress.md).
