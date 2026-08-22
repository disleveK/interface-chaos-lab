# OncoSys AI launch audit

**Survival score: 91/100 — Storm ready, with limited coverage (4 of 7 scenarios executed).**

- Target: [oncosysai.com](https://oncosysai.com/)
- Audit date: 2026-08-22
- Critical journey: understand the product, assess a sample dataset, and find pilot access
- Replay seed: `oncosys-launch-v1`
- Browser: Chrome cloud session

This is a real production-site audit, so Interface Chaos Lab stayed inside its safety boundary: it did not mutate production data, submit contact forms, upload files, or manufacture server failures. Unsupported injections are reported as `BLOCKED`, never as passes.

## Results

| Scenario | Status | Severity | Observed evidence | Recommended fix |
|---|---|---:|---|---|
| `server-error` · Five-Hundred Storm proxy | PASS | — | A nonexistent route rendered a clear `404`, “Page not found,” and a working “Return to Home” link. | Preserve this recovery path. Add support/contact context if analytics show frequent 404s. |
| `duplicate-submit` · Echo Chamber | PASS | — | “Assess FDA readiness” changed immediately to disabled “Assessing…”. Four additional click attempts were blocked. | Keep the disabled state and add server-side idempotency if not already present. |
| `conflicting-status` · Status Civil War | FAIL | Important | The same page advertises a “Q2 2026 pilot,” says it is seeking Q3 2026 partners, and repeats Q2 in the footer. On the August 2026 audit date, the Q2 language was stale. | Store pilot cohort and availability copy in one source of truth and render it everywhere. |
| `keyboard-only` · Mouse Extinction | FAIL | Minor | Visible focus was present and the main navigation was reachable, but two identical “Skip to main content” links appeared as the first two tab stops. | Render one skip link at the app shell level. |
| `zoom-200` · Magnification Mountain | BLOCKED | — | The cloud browser did not expose a reliable zoom or viewport emulation control. | Replay locally at 200% zoom and attach screenshots. |
| `text-expansion` · German Expansion Pack | BLOCKED | — | Production-safe text replacement was unavailable. | Replay in preview with 40% expanded fixtures. |
| `extreme-values` · Numberzilla | BLOCKED | — | The public marketing page exposes fixed example values but no safe fixture injection. | Replay against preview fixtures containing null, negative, zero, and very large values. |

## Top findings

1. **Centralize pilot timing.** Conflicting Q2/Q3 language is a trust problem on a regulatory-facing product.
2. **Remove the duplicated skip link.** Keyboard support is otherwise solid in the sampled path.
3. **Preserve duplicate-submit locking.** The live readiness demo correctly prevented repeat activation while processing.

## Replay

```bash
python3 scripts/chaos_plan.py --count 5 --seed oncosys-launch-v1
python3 scripts/survival_score.py case-studies/oncosysai-findings.json
```

## Evidence boundary

Observed evidence came from rendered DOM state, focus traversal, button state transitions, URLs, and browser console output. No claim is made for the three blocked injections. The extension-level console error observed during the run was excluded because it originated from the browser environment rather than OncoSys.
