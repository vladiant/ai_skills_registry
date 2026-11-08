---
name: minimal-agents-md-creation
description: >-
  Explore a repository and create a minimal AGENTS.md at the repo root with the
  essential project description, commands, stack, examples, and boundaries. Use
  only when the user asks for a minimal, tiny, or short AGENTS.md. For a full
  AGENTS.md with testing, changelog, and PR sections use agents-md-creation.
argument-hint: Optional repo focus or target language/framework
---

# Minimal AGENTS.md Creation

Explore this repository and create an `AGENTS.md` at the repo root.
Keep it minimal — the ideal `AGENTS.md` is as small as possible.

## Input

$ARGUMENTS — optional repo focus or target language/framework. If this is empty
or shows as a literal placeholder, use the user's message or cover the whole
repository.

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
  Write "Not yet documented" for anything you cannot find.
- Before writing, confirm every command and version appears in a manifest,
  script, or CI file; remove any that does not.

## Output

Write the result to `AGENTS.md` at the repository root. If one already exists,
do not overwrite it silently; show what would change and ask first. Then reply
with the path and a one-line summary. Print the content only if the user asks
for a preview.
