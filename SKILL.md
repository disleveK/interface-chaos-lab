---
name: interface-chaos-lab
description: Stress-test web interfaces against realistic user, data, device, network, accessibility, localization, authentication, and persistence failures. Use when asked to unleash UI chaos, audit frontend resilience, test edge cases, run Disaster Roulette, find brittle UX, produce a survival report, fix critical UI failures, or prove that a frontend survives real-world conditions. Works with React, Next.js, Vue, Svelte, and plain HTML/CSS/JavaScript.
---

# Interface Chaos Lab

Treat the interface as a system under stress. Break assumptions safely, capture reproducible evidence, repair the highest-risk failures, and rerun the identical scenarios.

## Safety boundary

- Operate only against local development, preview, or explicitly authorized test environments.
- Never unleash destructive scenarios against production data or real customer accounts.
- Prefer reversible interception, fixtures, feature flags, browser emulation, and test doubles.
- Never submit payments, messages, applications, deletions, or other consequential external actions.
- Preserve existing user changes. Isolate mutations in test fixtures or a dedicated branch/worktree when available.

## Modes

Infer the mode from the request:

- **audit**: inspect and report without modifying product code.
- **unleash**: run a seeded Disaster Roulette selection across several categories.
- **focused storm**: target `mobile`, `accessibility`, `localization`, `data`, `network`, `auth`, or `persistence`.
- **fix-critical**: implement only Critical and Dangerous findings, then rerun the same seed.
- **prove-the-fix**: replay recorded scenarios and compare evidence before versus after.

If the target app or runnable URL is missing, inspect the workspace first. Ask one concise question only when the target cannot be resolved safely.

## Workflow

1. **Reconnaissance**
   - Identify framework, package manager, dev command, important routes, authentication boundary, data layer, and existing test tools.
   - Read project instructions and preserve the current working state.
   - Define the critical journey: the smallest path whose failure would materially harm the user.

2. **Select chaos**
   - Read `references/scenarios.md` for scenario definitions and injection guidance.
   - For Disaster Roulette, run `scripts/chaos_plan.py --count 5 --seed <stable-seed>`.
   - Include at least one scenario from usability/accessibility and one from state/network/data.
   - Record the seed, route, fixture, viewport, browser preference, and expected invariant.

3. **Establish baseline**
   - Start the local or preview app using the project’s documented command.
   - Capture baseline screenshots and observable behavior for the critical journey.
   - Do not call a static page “working” when its persistence or network behavior has not been exercised.

4. **Inject one failure at a time**
   - Use browser emulation, request interception, deterministic fixtures, locale settings, keyboard navigation, or CSS/media preferences.
   - Keep each scenario independently reproducible.
   - Capture screenshot, console/network evidence, exact reproduction steps, and violated invariant.

5. **Classify**
   - Read `references/severity-and-reporting.md`.
   - Distinguish visual breakage from dangerous deception. False success, silent data loss, inaccessible primary actions, and unsupported consequential actions are Critical or Dangerous.
   - Calculate the survival score with `scripts/survival_score.py` when structured findings are available.

6. **Report**
   - Lead with the survival score, critical journey result, and the three most important failures.
   - Provide a compact scenario table: scenario, status, severity, evidence, fix.
   - Separate observed evidence from inference.
   - Include the exact replay command and seed.

7. **Repair and replay**
   - In audit mode, stop after the report.
   - In fix mode, implement the smallest systemic correction, not scenario-specific hacks.
   - Rerun the same seed and critical journey. Report before/after results and any remaining risk.

## Survival invariants

- The primary action remains perceivable and operable.
- The interface never claims success before the underlying operation succeeds.
- Loading, empty, partial, stale, offline, unauthorized, and failure states are distinguishable.
- User input is not silently lost.
- Content remains understandable at 320px width and 200% zoom.
- Keyboard focus is visible and follows a logical order.
- Reduced-motion preferences are respected.
- Long, translated, missing, zero, negative, and high-volume data do not corrupt meaning.
- Retrying does not create duplicate consequential actions.
- Evidence labels, timestamps, and status language match actual system state.

## Output voice

Be energetic but precise. Use playful storm names in headings, never in place of evidence. Do not shame teams or real products. Treat failures as system findings, not designer failures.

## Commands users may request

- `@interface-chaos-lab audit`
- `@interface-chaos-lab unleash`
- `@interface-chaos-lab mobile-apocalypse`
- `@interface-chaos-lab accessibility-storm`
- `@interface-chaos-lab data-flood`
- `@interface-chaos-lab network-nightmare`
- `@interface-chaos-lab fix-critical`
- `@interface-chaos-lab prove-the-fix`
