# Repository instructions

You maintain a registry of AI skills, agents, and prompts. Be concise and
accurate, and prefer editing existing patterns over introducing new ones.

Commands, structure, boundaries, and the PR checklist are in `AGENTS.md`.
Authoring rules per file type are in `.github/instructions/`.

## Behavior

- Prefer small, focused changes over large rewrites.
- Flag breaking changes explicitly before applying them. Renaming or deleting
  a skill or agent changes its install name and is a breaking change.
- When adding, removing, or renaming a skill, agent, or prompt, update the
  repository root `README.md`: the `## Available skills`,
  `## Available agents`, and `## Available prompts` lists, and the
  `## Repository layout` tree (folders only, each with a short comment).
- Files in `prompts/` are generated. Change the skill, then run
  `python3 .github/scripts/sync_prompts.py`.
- Before committing, run `python3 .github/scripts/validate_registry.py`,
  `python3 .github/scripts/sync_prompts.py --check`, and markdownlint.

## Communication

- Lead with the answer, then the reasoning.
- When uncertain, say so and offer a best guess with caveats.
- Propose one change set at a time and ask before widening scope. This governs
  your own edits, not the output format of skills or agents.

## Off-limits

- Never commit secrets, tokens, or credentials.
- Never rename a skill folder without updating its `name` and the README.
