#!/usr/bin/env python3
"""Validate Claude skill frontmatter, markdown metadata, and local references."""

from __future__ import annotations

import re
import sys
from collections import defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILLS_DIR = ROOT / ".claude" / "skills"


REFERENCE_RE = re.compile(r"(?<![\w./-])(?:\.\./)?[\w.-]+/references/[\w.-]+\.md|(?<![\w./-])references/[\w.-]+\.md")


def has_quoted_value(value: str) -> bool:
    return (
        (value.startswith('"') and value.endswith('"') and len(value) >= 2)
        or (value.startswith("'") and value.endswith("'") and len(value) >= 2)
    )


def validate_markdown_frontmatter(path: Path) -> list[str]:
    lines = path.read_text(encoding="utf-8").splitlines()
    errors: list[str] = []

    if not lines or lines[0].strip() != "---":
        return errors

    try:
        end = next(i for i, line in enumerate(lines[1:], start=1) if line.strip() == "---")
    except StopIteration:
        return [f"{path}: missing closing YAML frontmatter delimiter ---"]

    for line_number, line in enumerate(lines[1:end], start=2):
        if not line.strip() or line.startswith((" ", "\t", "#")):
            continue

        match = re.match(r"^([A-Za-z_][A-Za-z0-9_-]*):(?:\s*(.*))?$", line)
        if not match:
            errors.append(f"{path}:{line_number}: invalid top-level frontmatter line: {line!r}")
            continue

        key, value = match.group(1), (match.group(2) or "").strip()
        if not value or value in {">", "|", ">-", "|-", ">+", "|+"}:
            continue
        if ": " in value and not has_quoted_value(value):
            errors.append(
                f"{path}:{line_number}: unquoted frontmatter value for {key!r} contains ': '; "
                "use quotes or a block scalar"
            )

    return errors


def parse_frontmatter(path: Path) -> tuple[dict[str, str], list[str]]:
    lines = path.read_text(encoding="utf-8").splitlines()
    errors: list[str] = []

    if not lines or lines[0].strip() != "---":
        return {}, [f"{path}: SKILL.md must start with YAML frontmatter delimiter ---"]

    try:
        end = next(i for i, line in enumerate(lines[1:], start=1) if line.strip() == "---")
    except StopIteration:
        return {}, [f"{path}: missing closing YAML frontmatter delimiter ---"]

    meta_lines = lines[1:end]
    meta: dict[str, str] = {}
    i = 0
    while i < len(meta_lines):
        line = meta_lines[i]
        if not line.strip():
            i += 1
            continue
        if line.startswith((" ", "\t")):
            errors.append(f"{path}: unexpected indented frontmatter line: {line!r}")
            i += 1
            continue

        match = re.match(r"^([A-Za-z_][A-Za-z0-9_-]*):(?:\s*(.*))?$", line)
        if not match:
            errors.append(f"{path}: invalid frontmatter line: {line!r}")
            i += 1
            continue

        key, value = match.group(1), (match.group(2) or "")
        if value in {">", "|", ">-", "|-", ">+", "|+"}:
            block: list[str] = []
            i += 1
            while i < len(meta_lines) and (meta_lines[i].startswith(" ") or not meta_lines[i].strip()):
                block.append(meta_lines[i].strip())
                i += 1
            meta[key] = " ".join(part for part in block if part).strip()
            continue

        if has_quoted_value(value):
            value = value[1:-1]
        elif ": " in value:
            errors.append(
                f"{path}: unquoted frontmatter value for {key!r} contains ': '; use quotes or a block scalar"
            )
        meta[key] = value.strip()
        i += 1

    return meta, errors


def validate_references(path: Path) -> list[str]:
    text = path.read_text(encoding="utf-8")
    errors: list[str] = []
    for raw_ref in sorted(set(REFERENCE_RE.findall(text))):
        candidate = (path.parent / raw_ref).resolve()
        try:
            candidate.relative_to(ROOT)
        except ValueError:
            errors.append(f"{path}: reference escapes repository: {raw_ref}")
            continue
        if not candidate.exists():
            errors.append(f"{path}: missing referenced file: {raw_ref}")
    return errors


def validate_skill(path: Path) -> list[str]:
    errors: list[str] = []
    meta, frontmatter_errors = parse_frontmatter(path)
    errors.extend(frontmatter_errors)

    name = meta.get("name", "").strip()
    description = meta.get("description", "").strip()
    expected_name = path.parent.name

    if not name:
        errors.append(f"{path}: missing required frontmatter field 'name'")
    elif name != expected_name:
        errors.append(f"{path}: frontmatter name {name!r} must match directory {expected_name!r}")

    if not description:
        errors.append(f"{path}: missing required frontmatter field 'description'")

    errors.extend(validate_references(path))
    return errors


def validate_duplicate_references() -> list[str]:
    errors: list[str] = []
    by_name: dict[str, list[Path]] = defaultdict(list)
    for path in SKILLS_DIR.glob("*/references/*.md"):
        by_name[path.name].append(path)

    for name, paths in sorted(by_name.items()):
        if len(paths) < 2:
            continue
        contents = {path.read_text(encoding="utf-8") for path in paths}
        if len(contents) > 1:
            locations = ", ".join(str(path.relative_to(ROOT)) for path in paths)
            errors.append(f"duplicate reference {name!r} has divergent content: {locations}")

    return errors


def main() -> int:
    skill_files = sorted(SKILLS_DIR.glob("*/SKILL.md"))
    if not skill_files:
        print("No skill files found.", file=sys.stderr)
        return 1

    errors: list[str] = []
    frontmatter_files = sorted(path for path in ROOT.rglob("*.md") if ".git" not in path.parts)
    for path in frontmatter_files:
        errors.extend(validate_markdown_frontmatter(path))

    for path in skill_files:
        errors.extend(validate_skill(path))
    errors.extend(validate_duplicate_references())

    if errors:
        print("Repository validation failed:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1

    checked_frontmatter = sum(
        1
        for path in frontmatter_files
        if path.read_text(encoding="utf-8").splitlines()
        and path.read_text(encoding="utf-8").splitlines()[0].strip() == "---"
    )
    print(f"Validated {len(skill_files)} skills and {checked_frontmatter} markdown frontmatter blocks.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
