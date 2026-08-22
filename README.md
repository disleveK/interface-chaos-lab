# Interface Chaos Lab ⚡

[![Validate skill](https://github.com/disleveK/interface-chaos-lab/actions/workflows/validate.yml/badge.svg)](https://github.com/disleveK/interface-chaos-lab/actions/workflows/validate.yml)

**Your UI looks perfect. Now let reality use it.**

Interface Chaos Lab is an open-source Codex/ChatGPT skill that stress-tests web interfaces against the failures polished demos rarely show: tiny screens, keyboard-only navigation, stale data, slow APIs, expired sessions, duplicate submissions, offline saves, localization, and more.

It runs deterministic **Disaster Roulette** scenarios, captures reproducible evidence, assigns severity, calculates a survival score, and—when authorized—repairs the highest-risk failures before replaying the exact same storm.

## Real-world proof

The first production-safe audit tested [OncoSys AI](https://oncosysai.com/) and scored **91/100**, with 4 of 7 planned scenarios executed. It caught conflicting pilot dates and duplicated skip navigation while proving the live demo blocks duplicate submissions. Read the [full evidence-first case study](case-studies/oncosysai.com.md).

## What it tests

- 📱 Mobile layouts and 200% zoom
- ⌨️ Keyboard and accessibility behavior
- 🌍 Long text, RTL, and localization expansion
- 🌊 Empty, extreme, stale, conflicting, and high-volume data
- 📴 Offline saves, slow APIs, partial failures, and retries
- 🔐 Expired sessions and permission changes
- 💾 Returning-user and persistence failures

## Install

Copy this repository into your skills directory, then invoke it by name:

```text
@interface-chaos-lab unleash
```

The only required skill file is `SKILL.md`; the bundled scripts and references make plans and scoring deterministic.

## Try it

```text
Use @interface-chaos-lab to unleash Disaster Roulette on my local app.
Use @interface-chaos-lab to run an accessibility storm without changing code.
Use @interface-chaos-lab to find and fix only critical UI failures, then replay the same seed.
```

Generate a repeatable five-scenario storm:

```bash
python3 scripts/chaos_plan.py --count 5 --seed launch-day
```

Score structured findings:

```bash
python3 scripts/survival_score.py findings.json
```

## Safety

Run chaos only against local, preview, or explicitly authorized test environments. The skill avoids production data, real customer accounts, payments, messages, deletions, and other consequential external actions.

## Survival bands

| Score | Result |
|---:|---|
| 90–100 | Storm ready |
| 75–89 | Weather resistant |
| 50–74 | Demo fragile |
| 25–49 | Reality vulnerable |
| 0–24 | Critical journey unsafe |

## Why this exists

Most interface reviews ask, “Does it look good?” Interface Chaos Lab asks, **“Can it still tell the truth when everything goes wrong?”**

Built by [Disleve Kanku](https://github.com/disleveK). Contributions and new storm scenarios are welcome.

## License

[MIT](LICENSE)
