# UI/UX and interaction design

Read requirements, current design rules, and core tasks. Extend an existing host coherently without redesigning unrelated areas. Headless modules still need invocation, observation, and recovery; CLI tools need usable text contracts.

## Translate relevant references

1. Choose a few mature products handling comparable industry tasks, users, and content scale.
2. Study entry, navigation, action, waiting, results, and recovery.
3. Consult relevant Apple principles and the target platform's own guidance.
4. Select implementation resources last, distinguishing inspiration, copied code, dependencies, and complete projects.

Record URL, date, documentation/screenshot/actual-operation scope, relevant task, adopted principle, necessary changes, project implementation, and license considerations. Do not claim market leadership without evidence or pretend to have operated inaccessible screens.

Useful entry examples include VS Code for professional workspaces, Notion for content navigation, and Linear for task views. Select other references for the actual industry rather than reusing one visual pattern everywhere.

## Navigation and workspace

Design application navigation, module-level location, current task steps, search, and quick entry points separately. Explain current location, destination labels, return paths, and deep links after sign-in, denied access, or missing content. Preserve agreed filters, ordering, scroll position, selections, and drafts on return.

Distinguish navigation from actions. Back, closing a view, leaving editing, canceling a task, and ending a process have separate meanings. Whether background work continues is a business contract.

| Primary task | Workspace priorities |
| --- | --- |
| Find and process records | Search/filter, results, detail, contextual actions |
| Edit content | Main content, tools, properties, preview, save state |
| Approve or decide | Evidence, differences, history, decision actions |
| Execute work | Queue, current task, progress, results, recovery |
| Create media | Assets, preview, editing controls, output settings |

Define emphasis, density, pane sizes, scrolling ownership, resize behavior, focus, and layout reset when useful. Use panes because the task benefits from them, not because every application needs the same shell.

## Visual system and representative flow

Define coherent type hierarchy, semantic colors, spacing, icons, component states, density, themes, assets, and motion. Brand, industry, content, readability, and operating context drive the choices. Apple principles do not require a glass appearance on every platform.

After delivering the plan, implement one representative core flow using realistic content lengths, normal/loading/error/recovery states, and important target platforms. Check:

- Visual quality: reading order, hierarchy, spacing, alignment, density, asset purpose, readability.
- Task quality: discoverability, state comprehension, completing the action, understanding results, recovering mistakes.

Extend the system after these checks. Continue autonomous authorized work unless the user explicitly requested a gate. Label self-review, independent review, and human design confirmation separately.

## Action contracts and feedback

Use the [Interaction contract](../templates/interaction-contract.md) for consequential actions: goal, location, trigger, prerequisites, access, real call, state, result, recovery, focus, return path, and platform differences.

Batch actions define selection scope, cross-page selection, partial success, cancellation, and result detail. Shortcuts, gestures, and context menus supplement suitable visible paths. Explain disabled actions and a useful next step; presentation does not replace execution-side authorization.

| State | Explain |
| --- | --- |
| First use/empty data | Purpose and a useful start |
| No search results | Applied conditions and how to adjust them |
| Loading | What is being retrieved; unknown totals are not zero |
| Saving | Unsaved, saving, saved, failed, conflicted |
| Execution | Accepted, queued, running, canceling, actual terminal outcome |
| Success/partial success | Completed scope, result location, outstanding work |
| Failure/unknown outcome | Known facts, impact, recovery |
| Offline/access/capability limits | Available work and applicable alternatives |

Use percentages only when supported by real progress. Keep local status near the relevant item. Transient notifications supplement results that remain findable. Match interruption to consequence.

## Motion and input

Decide purpose and frequency first. Give immediate press feedback and use platform-appropriate activation semantics. Frequent keyboard and repetitive work should not wait for decorative motion. Preserve spatial relationships for menus, panes, and detail. Gesture tracking, release, interruption, reversal, and cancellation should remain continuous; use springs where appropriate.

Define enter/exit, repeated activation, interruption, reversal, and reduced-motion behavior. Animation should not block useful interaction or be the only carrier of important information. Respect sound/haptic capability and settings.

## Errors and recovery

Explain what happened, what it affects, and what can happen next. Preserve input, locate field errors, provide readable asynchronous errors, and move focus to a useful result or next field. Closing overlays returns focus to a valid trigger or sensible replacement.

Distinguish known failure from unknown outcome after timeouts. Query the operation before retrying when needed. Show partial results, offer agreed conflict decisions, and recover permitted context after expiry or revocation. Retry, restore, undo, and cancel controls require real implementations.

## Adapt tasks across platforms

| Target | Priorities |
| --- | --- |
| Desktop | Resizable windows, keyboard/pointer, panes, menus, applicable multi-window work |
| Phone | Clear task progression, reachability, touch, keyboard, safe areas, system back, backgrounding |
| Tablet/foldable | Single/multiple panes based on available window space while preserving context |
| Web | History, refresh, deep links, zoom, browser permissions |
| CLI | Arguments/prompts, stable output, errors, exit status, progress, cancellation, optional machine-readable output |

A desktop record workflow may show list, evidence, and actions together; a phone may use list-to-detail-to-action navigation. Business meaning and permissions remain consistent. Do not merely shrink typography or hide critical actions where people cannot find them.

Check actual window space, text scaling, long content, language, contrast, accessible names, focus, screen readers, and gesture alternatives. Follow the target platform's units and interaction guidance. Verify screenshot viewport and scale; absence of overflow does not establish mobile task usability. Distinguish browser emulation, simulators, and physical devices.

## Outputs and sources

Deliver research decisions, navigation/workspace, key flows, visual system, component states, interaction/motion contracts, recovery, platform differences, and separate visual/task results.

Official reference entry points checked on October 22, 2026; recheck applicable guidance for each project:

- [Apple Layout](https://developer.apple.com/design/human-interface-guidelines/layout)
- [Apple Feedback](https://developer.apple.com/design/human-interface-guidelines/feedback)
- [Apple Motion](https://developer.apple.com/design/human-interface-guidelines/motion)
- [Apple Accessibility](https://developer.apple.com/design/human-interface-guidelines/accessibility)
- [Windows navigation](https://learn.microsoft.com/windows/apps/design/basics/navigation-basics)
- [Android adaptation](https://developer.android.com/develop/adaptive-apps/guides/adaptive-dos-and-donts)
- [VS Code layout](https://code.visualstudio.com/docs/configure/custom-layout)
- [Notion navigation](https://www.notion.com/help/navigate-with-the-sidebar)
- [Linear views](https://linear.app/docs/board-layout)
