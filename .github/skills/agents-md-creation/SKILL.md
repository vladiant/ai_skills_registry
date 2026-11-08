---
name: agents-md-creation
description: >-
  Create an AGENTS.md file for a repository using best practices from GitHub
  Copilot guidance and progressive-disclosure principles. Use when asked to
  create, write, or improve AGENTS.md, or to standardize agent guidance and
  contribution rules. For a very small file use minimal-agents-md-creation; to
  restructure an existing bloated AGENTS.md use agends-md-refactor.
argument-hint: Optional scope focus (e.g. "backend service" or "full monorepo")
---

# AGENTS.md Creation

Create a concise, high-signal `AGENTS.md` that is specific to the target
repository and optimized for daily agent use.

## Procedure

### 1. Inspect repository evidence

Before writing, inspect:

- Build/test/lint/format/run/deploy commands in scripts and CI
- Dependency manifests for concrete technology versions
- Testing setup, fixtures, and utilities
- Coding style and linter/formatter configuration
- Existing contribution workflow, versioning, and changelog practices

Do not ask the user for facts the repository already contains. If evidence is
missing, write "Not yet documented" instead of guessing.

### 2. Keep root AGENTS.md small and focused

- Treat root `AGENTS.md` as high-priority instruction budget.
- Avoid vague instructions like "write clean code".
- Use progressive disclosure: keep details in referenced docs/config files.
- Prefer capability and domain descriptions over brittle file-path maps.

### 3. Generate required sections in this order

1. **Commands** (first): list executable commands with full flags/options.
   Prefer file-scoped forms first. Mark project-wide commands as "use before
   commits, not after every edit".
2. **Tech stack**: list concrete technologies and versions from manifests.
3. **Project structure**: describe architecture pattern, dependency rule, and
   domain concepts (not full path trees).
4. **Code style**: include 1-2 **✅ Good** and 1-2 **❌ Bad** examples based on
   real repository patterns; reference linter/formatter conventions.
5. **Testing**: explain full and targeted test runs, coverage, fixtures, and
   mocking conventions; clarify external-service requirements.
6. **Boundaries**: define three tiers:
   - ✅ Always do
   - ⚠️ Ask first
   - 🚫 Never do
7. **Changelog** (only if the repository has a `CHANGELOG.md` or the user asks
   for one): point to it and state its format, that entries go under
   `## [Unreleased]`, and the MAJOR/MINOR/PATCH bump rule. Do not restate the
   Keep a Changelog or SemVer specifications.
8. **When stuck**: ask clarifying questions, propose a plan, or open a draft
   PR with notes instead of speculative rewrites.
9. **PR checklist**: define ready criteria (lint/typecheck/tests green,
   focused diff, no debug artifacts; add changelog and SemVer review if
   item 7 applies).
10. **Cross-tool compatibility** (optional): if `CLAUDE.md` or `.cursorrules`
    exist, make them point to `./AGENTS.md`.

### 4. Apply formatting and quality constraints

- Open with a one-line persona.
- Use real command/code examples from this repository.
- Add config/environment guidance if env vars drive behavior.
- Add git workflow guidance if the repository defines one.
- End with a **Progressive Disclosure** section linking deeper references.
- Keep the root `AGENTS.md` under about 150 lines.

## Output

- Write the result to `AGENTS.md` at the repository root. If one already
  exists, do not overwrite it silently: for "improve" requests edit it in
  place and summarize the changes; for restructuring use `agends-md-refactor`.
- Then reply with the path and a one-line summary. Print the full content only
  if the user asks for a preview.
- The file itself contains no analysis, preambles, or placeholders unless they
  reflect true repository state.
