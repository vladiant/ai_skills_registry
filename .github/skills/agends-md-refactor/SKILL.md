---
name: agends-md-refactor
description: >-
  Refactor an AGENTS.md into a minimal root file with progressive disclosure,
  contradiction checks, and supporting docs grouped by topic.
argument-hint: Optional path to the AGENTS.md file to refactor
---

# AGENTS.md Refactor

Refactor an existing `AGENTS.md` to follow progressive-disclosure principles.
Keep the root file minimal and move detailed guidance into separate markdown
files grouped by topic.

## Goal

Reduce the root instructions to only the essentials while preserving the useful,
project-specific guidance that agents need often. The root `AGENTS.md` should be
small enough to load on every task, and detailed rules should live in focused
reference files.

## Procedure

### 1. Find contradictions

- Read the current `AGENTS.md` and identify any conflicting rules.
- Flag contradictions explicitly and ask the user which version to keep.
- If the user does not choose, keep both in separate reference files and note
  the conflict for later resolution.

### 2. Identify the essentials for the root file

Keep only instructions that are truly relevant to every task, such as:

- one-sentence project description
- package manager (if non-standard)
- non-standard build or typecheck commands
- anything directly relevant to all tasks

Remove or defer anything that is only useful in a subset of work.

### 3. Group the rest into separate files

Organize remaining instructions into logical categories such as:

- language conventions
- testing patterns
- API design
- Git workflow
- security or deployment rules
- architecture boundaries

Create a separate markdown file for each category.

### 4. Produce the new structure

Output:

- a minimal root `AGENTS.md` with references to the supporting files
- one or more topic-specific markdown files
- a suggested `docs/` folder structure, if useful

The root file should reference the detailed docs instead of duplicating them.

### 5. Flag instructions for deletion

Identify instructions that should be removed because they are:

- redundant
- already obvious to modern agents
- too vague to be actionable
- over-generalized or not project-specific
- examples of bad guidance such as "write clean code"

## Output rules

- Keep the root `AGENTS.md` as small as possible.
- Use progressive disclosure: move specifics into supporting markdown files.
- Keep rules actionable and tied to this repository.
- Do not invent file paths unless they fit the project structure.
- When contradictions are found, ask the user which version to keep before
  resolving them.
- Return the refactored documentation set or the proposed structure.
