# Design review

Classification: SELF_REVIEW. This is a document and workflow review, not an independent agent trial or application runtime pass.

| Confirmed requirement | Reading path | Finding |
| --- | --- | --- |
| General application scope and selected targets | [Main](../SKILL.md), [Architecture](../references/architecture.md) | Shared meaning/contracts, target-appropriate interaction, no fixed framework |
| Complete discovery without repeated answers | [Discovery](../references/discovery.md) | 72 candidates; agent verifies technical facts |
| Plan first, module details before execution | [Plan](../templates/application-plan.md), [Module](../templates/module-design.md) | Planning-only boundaries and existing implementation authority retained |
| Greenfield, extension, change | [Architecture](../references/architecture.md), [Development](../references/development.md) | Host reuse, compatibility, migrations, scoped structural adjustment |
| Task-based design and representative flows | [UI/UX](../references/ui-ux.md), [Interactions](../templates/interaction-contract.md) | Separate visual and task checks; no invented screen approval gates |
| Ready-dependency decisions and real integration | [Development](../references/development.md) | Business increments, real operation, independent branches when blocked |
| Tests, evidence, repair, and acceptance | [Testing](../references/testing.md), [Acceptance](../templates/acceptance.md) | Required missing evidence keeps acceptance incomplete |
| Milestones and recovery | [Delivery](../references/delivery-recovery.md), [Progress](../templates/progress.md) | Actual versions/processes checked; no fictional scheduling |
| Seven host routes | [Platforms](../references/platforms.md) | Documented setup separate from native execution; Koder limits explicit |

[E01–E12](../references/behavior-evals.md) have explicit decision paths in the instructions. They have not been executed as real agent trials for this edition. The English edition retains the confirmed functional workflow while adding publication documentation and licensing.
