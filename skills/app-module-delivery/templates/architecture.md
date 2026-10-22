# Architecture template

Replace the example with the actual architecture. Logical layers do not prescribe separate deployments.

## 1. Baseline and constraints

- Source/runtime versions, uncommitted changes, environments, existing failures: [fill]
- Targets, capabilities, data/deployment/performance limits: [fill]
- Preserved/changed contracts, ownership and integration route: [fill]

## 2. Logical view

Example responsibility flow:

~~~mermaid
flowchart LR
    A[Target entry and presentation] --> B[Business use case]
    B --> C[Owning module rules and authorization]
    C --> D[Persistence contract]
    D --> E[Actual storage implementation]
    C --> F[Platform or external contract]
    F --> G[Applicable adapter]
~~~

Explain code dependency and runtime call directions. Retain separate layers/adapters only when justified.

| Module | Responsibility/limits | Public contract/callers | Private implementation | Data ownership | Dependencies |
| --- | --- | --- | --- | --- | --- |
| [fill] | [fill] | [fill] | [fill] | [fill] | [fill] |

## 3. Runtime view

Draw actual clients, servers, background processes, and external systems. Identify module locations and assembly, local/network/IPC calls, identity propagation, authorization and trust, physical storage/cache, configuration, and resource lifecycle.

## 4. Data and state

| Entity/file | Fields/relations/constraints | Authority/writer | Access | Transactions/version/concurrency | Retention/recovery |
| --- | --- | --- | --- | --- | --- |
| [fill] | [fill] | [fill] | [fill] | [fill] | [fill] |

| State category | Owning module | Initial/transitions/terminal | Conditions/actor | Persistence/cache | Observation/recovery |
| --- | --- | --- | --- | --- | --- |
| [fill] | [fill] | [fill] | [fill] | [fill] | [fill] |

## 5. Core data flows

For each scenario:

- Requirement/scenario, role, entry: [fill]
- Input, validation/access, rules, persistence/effect, commit, receipt, later query: [fill]
- Correlation identifier: [fill]
- Atomic changes, partial success, audit/notification and independent outcomes: [fill]
- Failure, unknown result, retry, cancellation, recovery: [fill]
- Acceptance and actual evidence: [fill; retain NOT_RUN until executed]

## 6. Dependencies and platforms

| Dependency | Code/runtime/data/sequence | Source/version | Ready condition | Failure behavior | Affected flows |
| --- | --- | --- | --- | --- | --- |
| [fill] | [fill] | [fill] | [fill] | [fill] | [fill] |

| Capability | Desktop | Mobile/tablet | Web | CLI | Shared contract/specific implementation | Actual test environment |
| --- | --- | --- | --- | --- | --- | --- |
| [fill] | [support/limit/reason] | [fill] | [fill] | [fill] | [fill] | [fill] |

## 7. Compatibility and change

| Change | Caller/data impact | Compatibility/migration/coexistence | Cutover condition | Rollback/irreversibility | Decision/source |
| --- | --- | --- | --- | --- | --- |
| [fill] | [fill] | [fill] | [fill] | [fill] | [fill] |

## 8. Decision and implementation entry

Recommendation, alternatives, tradeoffs, unresolved assumptions, exact blockers, and next ready increment: [fill].
