#!/usr/bin/env python3
"""Validate registry structure, frontmatter, and README consistency.

Uses only the Python standard library. Run from anywhere:

    python3 .github/scripts/validate_registry.py

Exits with status 1 and prints GitHub Actions error annotations when any
check fails.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
NAME_RE = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
TRIGGER_RE = re.compile(r"\bUse (only )?when\b")
FORBIDDEN_SKILL_HEADINGS = ("## When to use", "## Example trigger")
BLOCK_SCALARS = {">", ">-", ">+", "|", "|-", "|+"}

errors: list[str] = []


def fail(path: Path | str, message: str) -> None:
    """Record a problem and print it as a GitHub Actions annotation."""
    rel = path.relative_to(ROOT).as_posix() if isinstance(path, Path) else path
    errors.append(f"{rel}: {message}")
    print(f"::error file={rel}::{message}")


def parse_frontmatter(path: Path) -> tuple[dict[str, str] | None, list[str]]:
    """Return (fields, problems). Fields is None without valid frontmatter.

    Handles `key: value`, quoted values, and folded/literal block scalars,
    which is all this registry uses. Block scalars are joined with spaces.
    """
    lines = path.read_text(encoding="utf-8").split("\n")
    if not lines or lines[0].rstrip("\r") != "---":
        return None, []

    fields: dict[str, str] = {}
    problems: list[str] = []
    i = 1
    while i < len(lines):
        line = lines[i].rstrip("\r")
        if line == "---":
            return fields, problems
        match = re.match(r"^([A-Za-z][\w-]*):[ \t]*(.*)$", line)
        if not match:
            i += 1
            continue
        key, value = match.group(1), match.group(2).strip()
        if value in BLOCK_SCALARS:
            i += 1
            block: list[str] = []
            while i < len(lines) and lines[i].startswith((" ", "\t")):
                block.append(lines[i].strip())
                i += 1
            fields[key] = " ".join(part for part in block if part)
            continue
        if value and value[0] not in "\"'" and ": " in value:
            problems.append(
                f"frontmatter value for '{key}' contains ': ' and must be quoted"
            )
        fields[key] = value.strip("\"'")
        i += 1
    return None, ["frontmatter is not closed with '---'"]


def load(path: Path, required: tuple[str, ...]) -> dict[str, str] | None:
    """Parse frontmatter and report missing or empty required fields."""
    fields, problems = parse_frontmatter(path)
    if fields is None:
        fail(path, problems[0] if problems else "missing YAML frontmatter")
        return None
    for problem in problems:
        fail(path, problem)
    for key in required:
        if not fields.get(key):
            fail(path, f"missing or empty frontmatter field '{key}'")
    return fields


def check_stem_name(path: Path, fields: dict[str, str]) -> None:
    stem = path.name.removesuffix(".md").removesuffix(".agent")
    if fields.get("name") and fields["name"] != stem:
        fail(path, f"name '{fields['name']}' must equal file name '{stem}'")


def check_skills() -> set[str]:
    skills_dir = ROOT / ".github" / "skills"
    names: set[str] = set()
    if not skills_dir.is_dir():
        return names
    for folder in sorted(p for p in skills_dir.iterdir() if p.is_dir()):
        skill_file = folder / "SKILL.md"
        if not skill_file.is_file():
            fail(folder, "skill folder has no SKILL.md")
            continue
        names.add(folder.name)
        fields = load(skill_file, ("name", "description"))
        if fields is None:
            continue
        name = fields.get("name", "")
        if name and name != folder.name:
            fail(skill_file, f"name '{name}' must equal folder '{folder.name}'")
        if name and (not NAME_RE.match(name) or len(name) > 64):
            fail(skill_file, "name must be lowercase-hyphenated, max 64 chars")
        description = fields.get("description", "")
        if len(description) > 1024:
            fail(skill_file, f"description is {len(description)} chars (max 1024)")
        if description and not TRIGGER_RE.search(description):
            fail(skill_file, "description needs a 'Use when ...' trigger phrase")
        body = skill_file.read_text(encoding="utf-8")
        for line in body.splitlines():
            if line.strip() in FORBIDDEN_SKILL_HEADINGS:
                fail(skill_file, f"remove '{line.strip()}'; put triggers in description")
        if fields.get("argument-hint") and "$ARGUMENTS" not in body:
            fail(skill_file, "has argument-hint but never uses $ARGUMENTS; add '## Input'")
    return names


def check_flat_dir(directory: Path, required: tuple[str, ...]) -> set[str]:
    names: set[str] = set()
    if not directory.is_dir():
        return names
    for path in sorted(directory.glob("*.md")):
        names.add(path.name.removesuffix(".md").removesuffix(".agent"))
        fields = load(path, required)
        if fields is not None:
            check_stem_name(path, fields)
    return names


def check_instructions() -> None:
    directory = ROOT / ".github" / "instructions"
    if not directory.is_dir():
        return
    for path in sorted(directory.rglob("*.md")):
        fields = load(path, ("applyTo",))
        if fields is None:
            continue
        for pattern in filter(None, (p.strip() for p in fields.get("applyTo", "").split(","))):
            if not any(ROOT.glob(pattern)):
                fail(path, f"applyTo '{pattern}' matches no files")


def readme_section(readme: str, title: str) -> str | None:
    match = re.search(rf"^## {re.escape(title)}[ \t]*$", readme, re.M)
    if not match:
        return None
    rest = readme[match.end():]
    following = re.search(r"^## ", rest, re.M)
    return rest[: following.start()] if following else rest


def check_readme(skills: set[str], agents: set[str], prompts: set[str]) -> None:
    readme_path = ROOT / "README.md"
    readme = readme_path.read_text(encoding="utf-8")

    for title, actual in (
        ("Available skills", skills),
        ("Available agents", agents),
        ("Available prompts", prompts),
    ):
        section = readme_section(readme, title)
        if section is None:
            fail(readme_path, f"missing section '## {title}'")
            continue
        listed = set(re.findall(r"^- `([^`]+)`", section, re.M))
        for name in sorted(actual - listed):
            fail(readme_path, f"'{name}' exists but is not listed under '{title}'")
        for name in sorted(listed - actual):
            fail(readme_path, f"'{name}' is listed under '{title}' but does not exist")

    layout = readme_section(readme, "Repository layout")
    if layout is None:
        fail(readme_path, "missing section '## Repository layout'")
        return
    block = re.search(r"```[^\n]*\n(.*?)```", layout, re.S)
    if not block:
        return
    stack: list[str] = []
    for line in block.group(1).splitlines():
        match = re.match(r"^((?:│   |    )*)[├└]── ([^\s#]+)", line)
        if not match:
            continue
        depth = len(match.group(1)) // 4
        entry = match.group(2)
        if not entry.endswith("/"):
            fail(readme_path, f"layout must list folders only, found '{entry}'")
            continue
        stack = stack[:depth] + [entry.rstrip("/")]
        if not ROOT.joinpath(*stack).is_dir():
            fail(readme_path, f"layout lists '{'/'.join(stack)}/' which does not exist")


def main() -> int:
    skills = check_skills()
    agents = check_flat_dir(ROOT / ".github" / "agents", ("name", "description"))
    prompts = check_flat_dir(ROOT / "prompts", ("name", "description"))
    check_instructions()
    check_readme(skills, agents, prompts)

    if errors:
        print(f"\n{len(errors)} problem(s) found.")
        return 1
    print(
        f"OK: {len(skills)} skills, {len(agents)} agents, {len(prompts)} prompts."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
