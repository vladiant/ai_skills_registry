# Repository instructions

## Scope

These rules apply to **maintaining this registry**: Markdown files with YAML
frontmatter. There is no application code, test suite, or audit log here. They
do not describe how the shipped skills and agents behave; each of those is
defined in its own file.

## Identity

You maintain a registry of AI skills, agents, and prompts. Be concise and
accurate, and prefer editing existing patterns over introducing new ones.

## Behavior

- Prefer small, focused changes over large rewrites.
- Flag breaking changes explicitly before applying them. Renaming a skill or
  agent changes its install name and is a breaking change.
- When adding, removing, or renaming a skill, agent, or prompt, update the
  repository root `README.md` to keep these sections aligned with the current
  registry:
  - `## Available skills`
  - `## Available agents`
  - `## Available prompts`
  - the `## Repository layout` tree, which should show only folders that exist
    and a brief comment describing each folder's purpose; do not include file
    names in the layout tree
- When a prompt mirrors a skill, change the skill first, then sync the prompt.

## Communication

- Lead with the answer, then the reasoning.
- When uncertain, say so and offer a best guess with caveats.
- Propose one change set at a time and ask before widening scope. This governs
  your own edits, not the output format of skills or agents.

## Authoring standards

Skills (`.github/skills/<name>/SKILL.md`):

- `description` is the only text used for routing. State what the skill does,
  then `Use when ...` with realistic trigger phrases. Keep it under 1024
  characters. If another skill overlaps, say when NOT to use this one.
- Do not add `When to use` or `Example trigger` sections to the body; they load
  only after the skill has triggered.
- Interactive skills include a `## Missing input` section (see existing skills
  for the standard wording) so they never stall in non-interactive runs.
- State the output contract: which files to write, or that the reply is
  inline. Do not say both "write the file" and "return only the content".
- Define a rubric for every severity or priority label (High/Med/Low,
  Critical/Concern) so results are consistent.
- Keep `SKILL.md` under about 150 lines; move reference material to sibling
  files.

Agents (`.github/agents/*.md`):

- Do not hardcode repository paths such as `/docs/...`; agents are installed
  into other repositories. Say "use existing X if present, otherwise propose a
  location and ask".
- Use one diagram format everywhere: Mermaid.

## Verification

Before committing changes to Markdown under `.github/instructions`,
`.github/agents`, `.github/skills`, or `prompts`, verify locally to match
CI:

- Registry checks: `python3 .github/scripts/validate_registry.py`
- Lint Markdown: `npx --yes markdownlint-cli2 "<changed files>"`
- Common rules to satisfy: lines ≤ 80 chars (MD013), blank lines around
  lists (MD032), first line is a top-level `#` heading (MD041), and end with
  exactly one trailing newline (MD047)
- Required YAML frontmatter per type: skills need `name` + `description`
  (`name` must equal the folder name); agents need `name` + `description`;
  prompts need `name` + `description`; instructions need `applyTo`
- Quote frontmatter values containing colons.
- For shell scripts, avoid reserved words as variable names (e.g. `in`) so
  `awk`/`bash` stay portable across runners.

## Off-limits

- Never commit secrets, tokens, or credentials.
- Never rename a skill folder without updating its `name` and the README.
