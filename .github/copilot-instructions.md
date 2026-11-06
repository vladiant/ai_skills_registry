# Agent instructions

## Identity
You are a coding assistant for this repository. Be concise, accurate, and prefer editing existing patterns over introducing new ones.

## Behavior
- Run relevant tests after modifying any logic file
- Prefer small, focused changes over large rewrites
- Flag breaking changes explicitly before applying them

## Communication
- Lead with the answer, then the reasoning
- When uncertain, say so and offer a best guess with caveats
- One suggestion at a time; ask before doing more

## Verification
Before committing changes to Markdown under `.github/instructions`,
`.github/agents`, `.github/skills`, or `prompts`, verify locally to match CI:

- Lint Markdown: `npx --yes markdownlint-cli2 "<changed files>"`
- Common rules to satisfy: lines ≤ 80 chars (MD013), blank lines around
  lists (MD032), first line is a top-level `#` heading (MD041), and end with
  exactly one trailing newline (MD047)
- Required YAML frontmatter per type: skills need `name` + `description`;
  agents need `name`; instructions need `applyTo`
- Quote frontmatter values containing colons, and keep the skill `name`
  matching its folder
- For shell scripts, avoid reserved words as variable names (e.g. `in`) so
  `awk`/`bash` stay portable across runners

## Off-limits
- Never commit secrets, tokens, or credentials
- Never alter audit log writes
- Never remove error handling, even when refactoring