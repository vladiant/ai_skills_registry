---
name: agent-definition-creator
description: >-
  Create specialized agent definition files under .github/agents/ for testing,
  documentation, and code-quality work using repository-specific commands,
  conventions, and boundaries. Use when asked to create QA/test, docs, or lint
  agents for a repository, or to generate focused .github/agents/*.md files
  that match project reality.
argument-hint: Optional target repo or domain (e.g. "backend service")
---

# Specialized Agent Definition Creator

Create three repository-specific agent definition files under `.github/agents/`.
Use the actual project structure, tooling, and conventions in this repository.

## Required output files

Create these files:

1. `.github/agents/test-agent.md`
   - QA engineer persona for writing tests
   - Include test framework, fixtures, conventions, and test commands
   - Boundary: write to `tests/` only, never remove failing tests

2. `.github/agents/docs-agent.md`
   - Technical writer persona for documentation
   - Include doc format, where docs live, doc build/lint commands
   - Boundary: write to `docs/` only, never modify source code

3. `.github/agents/lint-agent.md`
   - Code-quality specialist persona for style fixes
   - Include linter config, formatting rules, and auto-fix commands
   - Boundary: fix style only, never change logic

If the repository has no tests, docs, or linter, skip that agent and say why
instead of inventing tooling. Adjust the `tests/` and `docs/` boundaries to
the folders that actually exist.

## Procedure

### 1. Inspect repo evidence

Before writing any agent file, read:

- Test runner configuration and scripts
- Lint/format configuration and auto-fix commands
- Documentation layout and publishing/build commands
- Existing agent files and repo conventions
- Dependency manifests for framework and tooling versions

### 2. Write each file with the same structure

Each generated agent file should include:

- YAML frontmatter with `name` and `description` (the description says what
  the agent does and when to use it)
- A clear persona section
- Project knowledge or repository-specific context
- Executable commands relevant to that agent's role
- A three-tier boundaries section:
  - ✅ Always do
  - ⚠️ Ask first
  - 🚫 Never do

### 3. Use real repository conventions

- Match actual conventions and commands from the repo instead of generic advice.
- If a folder or command is not present, do not invent it.
- Prefer the repository's existing test, docs, and lint patterns.
- Keep examples anchored to actual project configuration and style.

### 4. Keep agent definitions focused

- Keep each agent file scoped to one responsibility.
- Do not add broad instructions like "write clean code".
- Focus on practical boundaries, commands, and project context.

## Output

- Write the files under `.github/agents/`. If a file already exists, edit it
  instead of overwriting it.
- Then reply with the files created and one line on each. Print file contents
  only if the user asks for a preview.
- Keep each file small, actionable, and specific.
