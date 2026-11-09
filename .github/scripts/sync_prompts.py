#!/usr/bin/env python3
"""Generate prompts/<name>.md from the skill of the same name.

Skills are the canonical source. A prompt is a copy-paste version of a skill
for tools that cannot load skills. This script rebuilds each prompt from its
skill, so the two cannot drift.

    python3 .github/scripts/sync_prompts.py          # rewrite prompts
    python3 .github/scripts/sync_prompts.py --check  # fail if out of date

Transformation, per skill:
  - description: the sentences before "Use when" / "Use only when"
  - title: the skill's H1 plus " Prompt"
  - body: the skill body without its `## Input` and `## Output` sections
  - an `## Output rules` section replaces `## Output`, telling the model to
    return only the file content
  - a closing line asks the model to generate the file

Add an entry to PROMPTS to publish another skill as a prompt.
"""

from __future__ import annotations

import re
import sys
import textwrap
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]

# prompt/skill name -> file the prompt produces
PROMPTS = {
    "agents-md-creation": "AGENTS.md",
    "readme-creation": "README.md",
}
DROPPED_SECTIONS = {"Input", "Output"}


def read_skill(name: str) -> tuple[str, str, str]:
    """Return (description, title, body_after_h1) for a skill."""
    text = (ROOT / ".github" / "skills" / name / "SKILL.md").read_text("utf-8")
    match = re.match(r"^---\n(.*?)\n---\n(.*)$", text, re.S)
    if not match:
        raise SystemExit(f"{name}: SKILL.md has no frontmatter")
    front, rest = match.groups()
    desc = re.search(r"^description:\s*>-?\n((?:[ \t]+.*\n?)+)", front + "\n", re.M)
    if not desc:
        raise SystemExit(f"{name}: description must be a folded block (>-)")
    description = " ".join(part.strip() for part in desc.group(1).splitlines())
    title_match = re.match(r"\n*# (.+)\n", rest)
    if not title_match:
        raise SystemExit(f"{name}: SKILL.md has no H1 heading")
    return description, title_match.group(1).strip(), rest[title_match.end():]


def prompt_description(skill_description: str) -> str:
    sentence = re.split(r"\s+Use (?:only )?when\b", skill_description)[0].strip()
    return sentence if sentence.endswith(".") else sentence + "."


def split_sections(body: str) -> list[str]:
    """Split on `## ` headings that are not inside a fenced code block."""
    parts: list[str] = [""]
    fence = 0  # length of the open fence, 0 when outside a fence
    for line in body.splitlines(keepends=True):
        ticks = re.match(r"^(`{3,})", line)
        if ticks:
            if not fence:
                fence = len(ticks.group(1))
            elif len(ticks.group(1)) >= fence and not line.strip("`\n"):
                fence = 0
        elif line.startswith("## ") and not fence:
            parts.append("")
        parts[-1] += line
    return [part for part in parts if part]


def transform_body(body: str, filename: str) -> str:
    """Drop Input/Output sections; put the prompt output rules in place."""
    parts = split_sections(body.lstrip("\n"))
    out: list[str] = []
    inserted = False
    for part in parts:
        heading = re.match(r"## (.+)", part)
        title = heading.group(1).strip() if heading else None
        if title in DROPPED_SECTIONS:
            if title == "Output" and not inserted:
                out.append(output_rules(filename))
                inserted = True
            continue
        out.append(part.rstrip("\n") + "\n\n")
    if not inserted:
        out.append(output_rules(filename))
    return "".join(out).rstrip("\n") + "\n"


def output_rules(filename: str) -> str:
    return (
        "## Output rules\n\n"
        f"- Return only the final `{filename}` content.\n"
        "- Do not include commentary, preambles, analysis, or meta-notes outside\n"
        "  the file body.\n"
        "- Do not mention that you inspected files or are following\n"
        "  instructions.\n\n"
    )


def build_prompt(name: str, filename: str) -> str:
    description, title, body = read_skill(name)
    wrapped = textwrap.fill(
        prompt_description(description),
        width=78,
        initial_indent="  ",
        subsequent_indent="  ",
        break_long_words=False,
        break_on_hyphens=False,
    )
    return (
        f"---\nname: {name}\ndescription: >-\n{wrapped}\n---\n\n"
        f"# {title} Prompt\n\n"
        f"{transform_body(body, filename)}\n"
        f"Now generate the final `{filename}` for this repository.\n"
    )


def main(argv: list[str]) -> int:
    check = "--check" in argv
    stale: list[str] = []
    for name, filename in PROMPTS.items():
        target = ROOT / "prompts" / f"{name}.md"
        expected = build_prompt(name, filename)
        current = target.read_text("utf-8") if target.is_file() else None
        if current == expected:
            continue
        if check:
            stale.append(target.relative_to(ROOT).as_posix())
            print(f"::error file={stale[-1]}::out of date with its skill; "
                  "run python3 .github/scripts/sync_prompts.py")
        else:
            target.parent.mkdir(exist_ok=True)
            target.write_text(expected, "utf-8")
            print(f"updated prompts/{name}.md")
    if check:
        if stale:
            return 1
        print(f"OK: {len(PROMPTS)} prompts match their skills.")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
