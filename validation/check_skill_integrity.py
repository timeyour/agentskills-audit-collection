#!/usr/bin/env python3
"""
Skill integrity checker for agentskills-audit-collection.

Validates:
1. Every skill directory under .claude/skills/ has a SKILL.md
2. Every SKILL.md has valid YAML frontmatter with `name` and `description`
3. SKILL.md `name` matches its parent directory name
4. All Markdown reference paths referenced in SKILL.md files exist on disk
5. README.md skill list matches actual .claude/skills/ directories
6. REQUIREMENTS.md Primary Requirements lists all skills
7. No bundled scripts exist inside .claude/skills/ (instruction-only rule)
"""

import os
import re
import sys
import yaml
from pathlib import Path


SKILLS_DIR = Path(".claude/skills")
README_PATH = Path("README.md")
REQUIREMENTS_PATH = Path("REQUIREMENTS.md")


def load_frontmatter(text: str) -> dict | None:
    """Extract YAML frontmatter from a Markdown file."""
    m = re.match(r"---\n(.*?)\n---", text, re.DOTALL)
    if not m:
        return None
    try:
        return yaml.safe_load(m.group(1))
    except yaml.YAMLError:
        return None


def find_md_references(content: str, skill_dir: Path) -> list[str]:
    """Extract Markdown reference paths from backtick-quoted strings.

    Only return paths that look like skill-relative references
    (contain '/' or '..'), not bare filenames or repo-root paths.
    """
    refs = []
    repo_root = Path.cwd().resolve()
    for m in re.finditer(r"`([^`]+\.md)`", content):
        ref = m.group(1)
        # Skip bare filenames that live at repo root (CLAUDE.md, README.md, etc.)
        if "/" not in ref and "\\" not in ref:
            continue
        # For paths starting with 'docs/', 'CLAUDE', 'REQUIREMENTS', 'PRODUCT', 'DESIGN'
        # resolve from repo root, not skill dir
        if ref.startswith("docs/") or ref.startswith(".."):
            refs.append(ref)
    return refs


def _resolve_ref(skill_dir: Path, ref: str) -> Path:
    """Resolve a reference path relative to skill dir or repo root."""
    repo_root = Path.cwd().resolve()
    # ../ relative to skill dir
    if ref.startswith(".."):
        return (skill_dir / ref).resolve()
    # docs/... relative to repo root
    if ref.startswith("docs/"):
        return (repo_root / ref).resolve()
    return (skill_dir / ref).resolve()


def check_skill(skill_dir: Path) -> list[str]:
    """Check a single skill directory. Returns list of error messages."""
    errors = []
    skill_name = skill_dir.name
    skill_md = skill_dir / "SKILL.md"

    # 1. SKILL.md exists
    if not skill_md.exists():
        errors.append(f"[{skill_name}] Missing SKILL.md")
        return errors

    text = skill_md.read_text(encoding="utf-8")

    # 2. Valid frontmatter with name + description
    fm = load_frontmatter(text)
    if fm is None:
        errors.append(f"[{skill_name}] SKILL.md missing or invalid YAML frontmatter")
        return errors

    if "name" not in fm:
        errors.append(f"[{skill_name}] SKILL.md frontmatter missing `name` field")
    elif fm["name"] != skill_name:
        errors.append(
            f"[{skill_name}] Frontmatter `name` ('{fm['name']}') does not match directory name ('{skill_name}')"
        )

    if "description" not in fm:
        errors.append(f"[{skill_name}] SKILL.md frontmatter missing `description` field")

    # 4. Referenced .md files exist (only skill-relative or repo-relative paths)
    refs = find_md_references(text, skill_dir)
    for ref in refs:
        target = _resolve_ref(skill_dir, ref)
        if not target.exists():
            errors.append(f"[{skill_name}] Reference not found on disk: `{ref}` (resolved to {target})")

    # 7. No bundled scripts inside skill dir (instruction-only rule)
    for p in skill_dir.rglob("*.py"):
        if p.name != "__init__.py":
            errors.append(f"[{skill_name}] Bundled script detected (violates instruction-only rule): {p.relative_to(skill_dir)}")
    for p in skill_dir.rglob("*.sh"):
        errors.append(f"[{skill_name}] Bundled script detected (violates instruction-only rule): {p.relative_to(skill_dir)}")
    for p in skill_dir.rglob("*.js"):
        errors.append(f"[{skill_name}] Bundled script detected (violates instruction-only rule): {p.relative_to(skill_dir)}")

    return errors


def check_readme_skills() -> list[str]:
    """Check README.md skill list matches actual directories."""
    errors = []
    if not README_PATH.exists():
        errors.append("[README.md] File not found")
        return errors

    readme_text = README_PATH.read_text(encoding="utf-8")

    actual_skills = {d.name for d in SKILLS_DIR.iterdir() if d.is_dir()}
    readme_skills = set()

    # Match `/skill-name` patterns in backticks (skill names contain hyphens or are multi-char)
    for m in re.finditer(r"`/([\w][\w-]+)`", readme_text):
        name = m.group(1)
        # Exclude single uppercase letters like S0, S1, S2, S3, S4
        if re.fullmatch(r"[A-Z]\d+", name):
            continue
        readme_skills.add(name)

    missing_from_readme = actual_skills - readme_skills
    extra_in_readme = readme_skills - actual_skills

    for s in sorted(missing_from_readme):
        errors.append(f"[README.md] Skill `{s}` exists on disk but is not listed in README.md")
    for s in sorted(extra_in_readme):
        errors.append(f"[README.md] Skill `{s}` listed in README.md but directory does not exist")

    return errors


def check_requirements_skills() -> list[str]:
    """Check REQUIREMENTS.md Primary Requirements lists all skills."""
    errors = []
    if not REQUIREMENTS_PATH.exists():
        errors.append("[REQUIREMENTS.md] File not found")
        return errors

    req_text = REQUIREMENTS_PATH.read_text(encoding="utf-8")
    actual_skills = {d.name for d in SKILLS_DIR.iterdir() if d.is_dir()}

    for skill in sorted(actual_skills):
        # Look for `/skill-name` pattern in REQUIREMENTS.md
        if f"/{skill}" not in req_text:
            errors.append(
                f"[REQUIREMENTS.md] Skill `/{skill}` not found in Primary Requirements section"
            )

    return errors


def main() -> int:
    if not SKILLS_DIR.exists():
        print("[ERROR] .claude/skills/ directory not found. Run from repo root.")
        return 1

    all_errors = []

    # Check each skill
    for skill_dir in sorted(SKILLS_DIR.iterdir()):
        if not skill_dir.is_dir():
            continue
        errors = check_skill(skill_dir)
        all_errors.extend(errors)

    # Check README.md consistency
    all_errors.extend(check_readme_skills())

    # Check REQUIREMENTS.md consistency
    all_errors.extend(check_requirements_skills())

    if all_errors:
        print(f"FAILED — {len(all_errors)} issue(s) found:\n")
        for err in all_errors:
            print(f"  - {err}")
        return 1
    else:
        print("PASSED — all skill integrity checks passed.")
        return 0


if __name__ == "__main__":
    sys.exit(main())
