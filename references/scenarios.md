# Scenario Catalog

Use scenario IDs in reports and replay plans. Inject one scenario at a time unless explicitly testing compounded failure.

## Viewport and input

| ID | Storm | Injection | Required invariant |
|---|---|---|---|
| `viewport-320` | Pocket Squeeze | Set viewport to 320×700 | Primary action and essential content remain reachable |
| `zoom-200` | Magnification Mountain | Emulate or manually test 200% zoom | Content reflows without clipping or two-axis scrolling |
| `keyboard-only` | Mouse Extinction | Complete the journey with Tab, Shift+Tab, Enter, Space, Escape, arrows | Focus is visible, ordered, and never trapped |
| `rapid-clicks` | Button Stampede | Trigger the primary action five times quickly | One logical operation occurs and progress is clear |
| `reduced-motion` | Stillness Protocol | Enable `prefers-reduced-motion: reduce` | Meaning survives and nonessential motion stops |

## Content and localization

| ID | Storm | Injection | Required invariant |
|---|---|---|---|
| `long-identity` | Namezilla | Use a 45–70 character display name and email | Navigation and ownership remain understandable |
| `text-expansion` | German Expansion Pack | Expand labels and messages by roughly 40% | Controls reflow without truncating essential meaning |
| `rtl` | Direction Reversal | Set document direction to RTL using representative Arabic fixtures | Reading order, icons, and layout follow direction correctly |
| `missing-media` | Avatar Eclipse | Fail image requests and omit optional media | Meaning and layout survive with accessible fallbacks |

## Data

| ID | Storm | Injection | Required invariant |
|---|---|---|---|
| `empty-data` | Empty Planet | Return a valid empty collection | The user sees a useful empty state, not a broken chart |
| `data-flood` | Record Tsunami | Return 200–1,000 representative records | Navigation, rendering, and prioritization remain usable |
| `extreme-values` | Numberzilla | Use zero, negative, null, and very large values | Formatting preserves sign, magnitude, and meaning |
| `conflicting-status` | Status Civil War | Return credible but conflicting status fields | The UI exposes conflict instead of inventing certainty |
| `stale-data` | Time Warp | Set last-updated time 14 days in the past | The UI does not label stale information “Live” |

## Network and persistence

| ID | Storm | Injection | Required invariant |
|---|---|---|---|
| `slow-api` | Eight-Second Winter | Delay a critical response by 8 seconds | Progress, cancellation, and preserved context are clear |
| `partial-failure` | Half-Cloud Outage | Fail one secondary request while primary data succeeds | Partial state is explicit and useful content remains available |
| `offline-save` | Cable Cut | Drop the network immediately before save | The UI never claims durable success and input is preserved |
| `server-error` | Five-Hundred Storm | Return a deterministic 500 response | Recovery guidance and retry are truthful and accessible |
| `duplicate-submit` | Echo Chamber | Replay the same mutation or retry after timeout | Idempotency or UI locking prevents duplicates |

## Authentication and continuity

| ID | Storm | Injection | Required invariant |
|---|---|---|---|
| `expired-session` | Identity Vanishing Act | Return 401 during the critical journey | Reauthentication preserves intent and avoids false failure |
| `permission-loss` | Role Reversal | Remove permission between load and action | The action becomes unavailable with a clear explanation |
| `returning-user` | Six-Month Coma | Load old local state/schema or deep link | Migration or recovery avoids crashes and silent loss |

## Injection preference

Prefer, in order:

1. Existing test fixtures and documented mocks.
2. Browser request interception or route fulfillment.
3. Development-only feature flags or query parameters.
4. Temporary test harnesses isolated from production code.

Do not alter production databases or real accounts to manufacture chaos.

