---
name: agents-md-creation
description: >-
  Create an AGENTS.md file for a repository using best practices from GitHub
  Copilot guidance and progressive-disclosure principles. Use when asked to
  create, rewrite, or improve AGENTS.md for agent behavior and contribution
  rules.
argument-hint: Optional scope focus (e.g. "backend service" or "full monorepo")
---

# AGENTS.md Creation

Create a concise, high-signal `AGENTS.md` that is specific to the target
repository and optimized for daily agent use.

## When to use

- Creating `AGENTS.md` from scratch
- Rewriting a bloated or generic `AGENTS.md`
- Standardizing agent guidance across teams and tools
- Improving agent reliability with clearer boundaries and command references

## Procedure

### 1. Inspect repository evidence

Before writing, inspect:

- Build/test/lint/format/run/deploy commands in scripts and CI
- Dependency manifests for concrete technology versions
- Testing setup, fixtures, and utilities
- Coding style and linter/formatter configuration
- Existing contribution workflow, versioning, and changelog practices

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
7. **Changelog**: require `CHANGELOG.md` with Keep a Changelog 1.1.0 and
   SemVer. Keep entries in `## [Unreleased]` under standard categories and
   move them to `## [x.y.z] - YYYY-MM-DD` at release.
8. **When stuck**: ask clarifying questions, propose a plan, or open a draft
   PR with notes instead of speculative rewrites.
9. **PR checklist**: define ready criteria (lint/typecheck/tests green,
   focused diff, no debug artifacts, changelog and SemVer review done).
10. **Cross-tool compatibility** (optional): if `CLAUDE.md` or `.cursorrules`
    exist, make them point to `./AGENTS.md`.

### 4. Apply formatting and quality constraints

- Open with a one-line persona.
- Use real command/code examples from this repository.
- Add config/environment guidance if env vars drive behavior.
- Add git workflow guidance if the repository defines one.
- End with a **Progressive Disclosure** section linking deeper references.
- Keep total instructions in root `AGENTS.md` under roughly 150.

## Output rules

- Produce only the final `AGENTS.md` content.
- Do not include analysis, preambles, or placeholders unless they reflect
  true repository state.
- If evidence is missing, prefer "Not yet documented" over guessing.
