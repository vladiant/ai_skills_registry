---
name: agends-md-refactor
description: >-
  Refactor an AGENTS.md into a minimal root file with progressive disclosure,
  contradiction checks, and supporting docs grouped by topic. Use when an
  existing AGENTS.md is bloated, contradictory, or too long, or when asked to
  split agent instructions into topic docs. To create a new AGENTS.md use
  agents-md-creation instead.
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
reference files. No rule is lost: every rule is kept, moved, or explicitly
proposed for deletion.

## Procedure

### 0. Locate the file

Use the path argument if given. Otherwise use the root `AGENTS.md`; if absent,
check `CLAUDE.md` and `.github/copilot-instructions.md`, and say which file
you refactored.

### 1. Find contradictions

- Read the current file and identify any conflicting rules.
- Flag contradictions explicitly and ask the user which version to keep.
- If the user does not choose, or you cannot ask (non-interactive run), keep
  both in separate reference files and note the conflict for later
  resolution.

### 2. Identify the essentials for the root file

Keep only instructions that are truly relevant to every task, such as:

- one-sentence project description
- package manager (if non-standard)
- non-standard build or typecheck commands
- anything directly relevant to all tasks

Move anything that is only useful in a subset of work.

### 3. Group the rest into separate files

Organize remaining instructions into logical categories such as:

- language conventions
- testing patterns
- API design
- Git workflow
- security or deployment rules
- architecture boundaries

Create a separate markdown file for each category. Use the repository's
existing docs folder if there is one; otherwise propose one and say so.

### 4. Flag instructions for deletion

Identify instructions that are:

- redundant
- already obvious to modern agents
- too vague to be actionable
- over-generalized or not project-specific
- examples of bad guidance such as "write clean code"

Do not delete them. Keep each in its topic file under a
`Proposed for deletion` heading with a one-line reason, until the user
confirms.

### 5. Write the new structure

- a minimal root `AGENTS.md` with references to the supporting files
- one or more topic-specific markdown files

The root file references the detailed docs instead of duplicating them.

## Output

Write the files, then reply with: the files created or changed, how many rules
moved, the contradictions found, and the proposed deletions. If the user asks
for a plan only, return the proposed structure without writing files.

## Rules

- Keep the root `AGENTS.md` as small as possible.
- Keep rules actionable and tied to this repository.
- Do not invent file paths; use the repository's existing structure.
- Never resolve a contradiction yourself; ask, or keep both.
