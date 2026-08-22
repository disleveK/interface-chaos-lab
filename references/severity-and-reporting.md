# Severity and Reporting

## Severity

| Severity | Definition | Examples |
|---|---|---|
| Critical | Can cause harm, irreversible action, security/privacy exposure, or silent loss | False payment success, exposed private data, lost journal entry |
| Dangerous | Blocks the critical journey or materially deceives the user | Save appears successful while offline, inaccessible submit action |
| Important | Major degradation with a workaround | Mobile overflow hiding secondary controls, unusable data flood |
| Minor | Polish issue that does not corrupt meaning or completion | Cosmetic clipping, awkward but readable wrapping |

## Status

- `PASS`: invariant verified with evidence.
- `FAIL`: invariant violated reproducibly.
- `WARN`: degraded or ambiguous; risk exists but the invariant was not fully violated.
- `BLOCKED`: environment prevented a valid test. Never convert BLOCKED to PASS.

## Survival score

Begin at 100 and subtract per finding:

- Critical: 25
- Dangerous: 15
- Important: 7
- Minor: 2
- Blocked: 0, but report test coverage separately

Clamp the score to 0–100. A high score with low coverage is not a strong result.

Suggested bands:

- 90–100: Storm ready
- 75–89: Weather resistant
- 50–74: Demo fragile
- 25–49: Reality vulnerable
- 0–24: Critical journey unsafe

## Report template

1. Survival score and band
2. Critical journey: pass/fail/blocked
3. Coverage: executed scenarios / planned scenarios
4. Top three findings
5. Scenario table with ID, status, severity, evidence, remediation
6. Exact replay seed and command
7. Before/after evidence when fixes were authorized

Use screenshots and logs as evidence where available. Avoid long generic checklists.

