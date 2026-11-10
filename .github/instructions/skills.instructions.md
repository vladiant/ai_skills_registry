---
applyTo: ".github/skills/**/SKILL.md"
---

# Skill authoring rules

- `name` must equal the folder name: lowercase, hyphenated, at most 64 chars.
- `description` is the only text used for routing. State what the skill does,
  then `Use when ...` with realistic trigger phrases. Keep it under 1024
  characters. If another skill overlaps, say when NOT to use this one.
- Do not add `When to use` or `Example trigger` sections to the body; they
  load only after the skill has triggered.
- A skill with an `argument-hint` uses it in an `## Input` section through
  `$ARGUMENTS`, with a fallback to the user's message.
- Interactive skills include a `## Missing input` section so they never stall
  in non-interactive runs: ask only about what is missing, otherwise list
  assumptions as `[ASSUMED]` and continue. Never invent stakeholders,
  deciders, dates, or IDs.
- State the output contract: which files to write, or that the reply is
  inline. Do not say both "write the file" and "return only the content".
  Never overwrite an existing file silently.
- Define a rubric for every severity or priority label (High/Med/Low,
  Critical/Concern) so results are consistent.
- Skills that list commands or versions include a verify step: confirm each
  one appears in a manifest, script, or CI file.
- Keep `SKILL.md` under about 150 lines; move reference material to sibling
  files.
- Changing a skill that has a prompt means running
  `python3 .github/scripts/sync_prompts.py` and committing the result.
