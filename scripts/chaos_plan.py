#!/usr/bin/env python3
"""Generate a deterministic Interface Chaos Lab scenario plan."""

import argparse
import json
import random

SCENARIOS = [
    {"id": "viewport-320", "category": "viewport", "storm": "Pocket Squeeze"},
    {"id": "zoom-200", "category": "accessibility", "storm": "Magnification Mountain"},
    {"id": "keyboard-only", "category": "accessibility", "storm": "Mouse Extinction"},
    {"id": "rapid-clicks", "category": "input", "storm": "Button Stampede"},
    {"id": "reduced-motion", "category": "accessibility", "storm": "Stillness Protocol"},
    {"id": "long-identity", "category": "content", "storm": "Namezilla"},
    {"id": "text-expansion", "category": "localization", "storm": "German Expansion Pack"},
    {"id": "rtl", "category": "localization", "storm": "Direction Reversal"},
    {"id": "missing-media", "category": "content", "storm": "Avatar Eclipse"},
    {"id": "empty-data", "category": "data", "storm": "Empty Planet"},
    {"id": "data-flood", "category": "data", "storm": "Record Tsunami"},
    {"id": "extreme-values", "category": "data", "storm": "Numberzilla"},
    {"id": "conflicting-status", "category": "data", "storm": "Status Civil War"},
    {"id": "stale-data", "category": "data", "storm": "Time Warp"},
    {"id": "slow-api", "category": "network", "storm": "Eight-Second Winter"},
    {"id": "partial-failure", "category": "network", "storm": "Half-Cloud Outage"},
    {"id": "offline-save", "category": "persistence", "storm": "Cable Cut"},
    {"id": "server-error", "category": "network", "storm": "Five-Hundred Storm"},
    {"id": "duplicate-submit", "category": "persistence", "storm": "Echo Chamber"},
    {"id": "expired-session", "category": "auth", "storm": "Identity Vanishing Act"},
    {"id": "permission-loss", "category": "auth", "storm": "Role Reversal"},
    {"id": "returning-user", "category": "continuity", "storm": "Six-Month Coma"},
]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--count", type=int, default=5)
    parser.add_argument("--seed", default="interface-chaos-lab")
    parser.add_argument("--category", action="append", dest="categories")
    args = parser.parse_args()
    pool = [s for s in SCENARIOS if not args.categories or s["category"] in args.categories]
    if not pool:
        parser.error("no scenarios match the requested categories")
    count = max(1, min(args.count, len(pool)))
    selected = random.Random(args.seed).sample(pool, count)
    print(json.dumps({"seed": args.seed, "count": count, "scenarios": selected}, indent=2))


if __name__ == "__main__":
    main()
