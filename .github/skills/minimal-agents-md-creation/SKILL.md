---
name: minimal-agents-md-creation
description: >-
  Explore a repository and create a minimal AGENTS.md at the repo root with the
  essential project description, commands, stack, examples, and boundaries.
argument-hint: Optional repo focus or target language/framework
---

# Minimal AGENTS.md Creation

Explore this repository and create an `AGENTS.md` at the repo root.
Keep it minimal — the ideal `AGENTS.md` is as small as possible.

## Required content

Include only:

1. One-sentence project description (anchors every decision).
2. Package manager / build tool (if non-standard).
3. Commands to build, test, lint, and run the project (with full flags).
4. Tech stack with versions (read the dependency files).
5. One good and one bad code example matching this project's style.
6. Boundaries: what to always do, what to ask about, what to never do.

## Rules

- Do not include a full file tree.
- Describe architecture, not paths.
- Point to separate files for detailed conventions.
- Keep root guidance compact and high-signal.
- Use only evidence from the repository; do not invent commands or versions.
- Return only the final `AGENTS.md` content.
