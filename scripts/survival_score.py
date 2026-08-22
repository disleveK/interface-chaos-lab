#!/usr/bin/env python3
"""Score structured Interface Chaos Lab findings from a JSON file or stdin."""

import argparse
import json
import sys

DEDUCTIONS = {"critical": 25, "dangerous": 15, "important": 7, "minor": 2}


def band(score):
    if score >= 90:
        return "Storm ready"
    if score >= 75:
        return "Weather resistant"
    if score >= 50:
        return "Demo fragile"
    if score >= 25:
        return "Reality vulnerable"
    return "Critical journey unsafe"


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("path", nargs="?", help="JSON findings file; omit to read stdin")
    args = parser.parse_args()
    stream = open(args.path, encoding="utf-8") if args.path else sys.stdin
    try:
        payload = json.load(stream)
    finally:
        if args.path:
            stream.close()
    findings = payload.get("findings", []) if isinstance(payload, dict) else payload
    deductions = []
    for finding in findings:
        if str(finding.get("status", "")).lower() != "fail":
            continue
        severity = str(finding.get("severity", "important")).lower()
        points = DEDUCTIONS.get(severity, DEDUCTIONS["important"])
        deductions.append({"id": finding.get("id", "unknown"), "severity": severity, "points": points})
    score = max(0, 100 - sum(item["points"] for item in deductions))
    planned = len(findings)
    executed = sum(str(f.get("status", "")).lower() != "blocked" for f in findings)
    print(json.dumps({"score": score, "band": band(score), "coverage": {"executed": executed, "planned": planned}, "deductions": deductions}, indent=2))


if __name__ == "__main__":
    main()
