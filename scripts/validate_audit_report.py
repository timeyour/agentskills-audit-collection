#!/usr/bin/env python3
"""Validate audit report JSON against schemas/audit-report.schema.json."""

from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCHEMA_PATH = ROOT / "schemas" / "audit-report.schema.json"
DEFAULT_REPORT = ROOT / "validation" / "golden" / "audit-report.example.json"

REQUIRED_TOP = [
    "schemaVersion",
    "scope",
    "target",
    "evidence",
    "featureInventory",
    "flowExecutionLog",
    "visualFindings",
    "deploymentReadiness",
    "issueCards",
    "copyableFixPack",
    "regressionChecks",
    "lessons",
    "finalVerdict",
]


def validate_required(data: dict, path: Path) -> list[str]:
    errors: list[str] = []
    for key in REQUIRED_TOP:
        if key not in data:
            errors.append(f"{path}: missing required field '{key}'")
    if data.get("schemaVersion") != "0.1.0":
        errors.append(f"{path}: schemaVersion must be '0.1.0'")
    for card in data.get("issueCards") or []:
        for field in ("id", "title", "severity", "problem", "fix", "regressionCheck"):
            if field not in card:
                errors.append(f"{path}: issue card missing '{field}'")
    return errors


def validate_jsonschema(data: dict, schema: dict, path: Path) -> list[str]:
    try:
        import jsonschema
    except ImportError:
        return []

    validator = jsonschema.Draft202012Validator(schema)
    return [f"{path}: {e.message}" for e in validator.iter_errors(data)]


def main(argv: list[str]) -> int:
    paths = [Path(p) for p in argv[1:]] if len(argv) > 1 else [DEFAULT_REPORT]
    schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
    errors: list[str] = []

    for path in paths:
        if not path.is_file():
            errors.append(f"{path}: file not found")
            continue
        data = json.loads(path.read_text(encoding="utf-8"))
        errors.extend(validate_required(data, path))
        errors.extend(validate_jsonschema(data, schema, path))

    if errors:
        for err in errors:
            print(err, file=sys.stderr)
        return 1

    for path in paths:
        print(f"OK: {path}")
    if not __import__("importlib").util.find_spec("jsonschema"):
        print("Note: install jsonschema for full schema validation (pip install jsonschema)", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
