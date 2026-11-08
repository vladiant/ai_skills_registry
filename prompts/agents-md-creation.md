---
name: agents-md-creation
description: >-
  Analyze a repository and produce a concise, high-signal AGENTS.md that
  follows best practices, progressive disclosure, and practical delivery
  standards.
---

# AGENTS.md Creation Prompt

You are an expert software architect and engineering enablement lead working
on a production software project.

Analyze this repository thoroughly and create an `AGENTS.md` file following
the best practices from:

- [How to write a great AGENTS.md: lessons from over 2,500
  repositories](https://github.blog/ai-and-ml/github-copilot/how-to-write-a-great-agents-md-lessons-from-over-2500-repositories/)
- [A complete guide to
  AGENTS.md](https://www.aihero.dev/a-complete-guide-to-agents-md)

## Core principles

- Keep the root `AGENTS.md` small and focused. Every token loads on every
  request. Frontier models can follow roughly 150-200 instructions
  consistently; do not waste this budget.
- Use progressive disclosure: put detailed rules in separate files and
  reference them.
- Describe capabilities and domain concepts, not exact file paths (paths go
  stale quickly).
- Never add vague or obvious instructions such as "write clean code".

## Required AGENTS.md sections

`AGENTS.md` must cover these areas:

1. **Commands** (first section)
   - Discover and list all executable commands: build, test, lint, format,
     run, deploy.
   - Include full flags and options, not only tool names.
   - Prefer file-scoped commands over project-wide commands.
   - Mark project-wide commands as: "use before commits, not after every
     edit".
   - Read `package.json` scripts, `Makefile` targets, `pyproject.toml`
     scripts, CI configs, Dockerfiles, and shell scripts to capture real
     commands used by this project.

2. **Tech stack**
   - List major technologies with concrete versions from dependency files.
   - Include language, framework, database, ORM, test runner, linter,
     formatter, bundler, and related tooling where present.
   - Be precise (for example: "FastAPI >=0.115 with Uvicorn").

3. **Project structure**
   - Describe architecture pattern (for example, Clean Architecture, MVC, or
     hexagonal) and dependency rule.
   - Use a table or concise descriptions for each layer or area.
   - Document domain concepts (entities, value objects, bounded contexts)
     instead of exact paths.
   - Focus on capabilities and rough location rather than brittle trees.

4. **Code style** (with real repository patterns)
   - Show 1-2 **✅ Good** snippets based on this codebase.
   - Show 1-2 **❌ Bad** counter-examples for this codebase.
   - Point to model files to emulate and legacy patterns to avoid.
   - State naming conventions, line length, and formatting rules.
   - Reference linter and formatter configuration.

5. **Testing**
   - Document test execution (full suite, targeted runs, coverage).
   - List shared fixtures and test utilities.
   - Define conventions: what to mock, how to mock, test naming, async
     patterns.
   - State whether tests are offline or require external services.

6. **Boundaries** (three-tier)
   - **✅ Always do**: mandatory behaviors.
   - **⚠️ Ask first**: actions requiring human approval.
   - **🚫 Never do**: hard prohibitions.

7. **Changelog**
   - Require `CHANGELOG.md` with [Keep a Changelog
     1.1.0](https://keepachangelog.com/en/1.1.0/) and [Semantic
     Versioning](https://semver.org/spec/v2.0.0.html).
   - Keep notable changes under `## [Unreleased]` with categories:
     `Added`, `Changed`, `Deprecated`, `Removed`, `Fixed`, `Security`.
   - Write entries for humans: what changed and why it matters.
   - At release time, move entries to `## [x.y.z] - YYYY-MM-DD`.
   - Use ISO 8601 dates (`YYYY-MM-DD`), latest version first.
   - Keep comparison links at the bottom.
   - Never paste raw git log output into `CHANGELOG.md`.
   - Apply version bump rules from diff review:
     - **MAJOR**: breaking API, removed endpoints, incompatible migrations.
     - **MINOR**: backward-compatible features or additions.
     - **PATCH**: fixes, refactors, docs, dependency/style updates.
   - Update manifest version and move `[Unreleased]` entries at release.

8. **When stuck**
   - Add a short escape hatch: ask a clarifying question, propose a plan, or
     open a draft PR with notes instead of making large speculative changes.

9. **PR checklist**
   - Define "ready": lint/typecheck/tests green, focused diff, concise summary
     of what changed and why, no debug artifacts.
   - Require `CHANGELOG.md` updates under `[Unreleased]`.
   - Require SemVer bump validation and corresponding manifest/changelog
     updates before merge.

10. **Cross-tool compatibility** (optional)
    - If tool-specific files exist (`CLAUDE.md`, `.cursorrules`), point them to
      `AGENTS.md` using:
      `Strictly follow the rules in ./AGENTS.md`.

## Format and style requirements

- Open with a one-line persona.
- Put commands first.
- Use code blocks with real repository examples.
- Keep content specific to this repository; avoid generic filler.
- Add configuration/environment variables guidance when env-based config
  exists.
- Include git workflow guidance when the repository defines one.
- Add a **Progressive Disclosure** section at the end that references detailed
  docs/configs.
- Add **When Stuck** and **PR Checklist** sections.
- If changelog is used, include a **Changelog** section with Keep a Changelog
  maintenance rules.
- Keep the file below roughly 150 instructions; move details to referenced
  files.
- Write `AGENTS.md` at the repository root.
