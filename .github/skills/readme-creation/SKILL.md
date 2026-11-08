---
name: readme-creation
description: >-
  Generate a README.md for this repository. Use when asked to create, write,
  update, or improve a README, document a project, produce a project overview,
  or write repository documentation.
argument-hint: Optional path to a specific subdirectory or package to document
---

# README Creation

You are a senior technical writer and software architect. Your task is to
author a production-quality `README.md` for this repository by inspecting the
actual codebase, configuration files, and project metadata before writing.

## Procedure

### 1. Inspect the repository

Before writing, read:

- Source folders and main entry points
- Package manifests (`package.json`, `pyproject.toml`, `go.mod`,
  `Cargo.toml`, etc.)
- Config and Docker files
- Existing tests and examples
- Any existing `README.md`, `CHANGELOG`, or `docs/` content
- The license file or repository metadata for the license name

### 2. Generate sections in this order

1. **Badges** — only badges provable from the repo (language, license, CI
   status, version). Omit if none are reliable.
2. **Overview** — a one-line value proposition stating the project's purpose
   and who it helps, followed by a short purpose paragraph (what it is, what
   problem it solves, who should use it).
3. **Quick start** — exact, working install/build/run commands from the repo's
   manifests and scripts.
4. **Architecture** — compact but accurate overview of the main components and
   how they interact.
5. **Key decisions** — 3–6 important design choices with rationale tied to the
   implementation.
6. **Benchmarks** — include only if the repo already contains benchmark
   results; otherwise omit this section entirely.
7. **License** — the project's actual license sourced from the license file or
   metadata.

### 3. Apply the content template

Use this writing pattern across the body:

- **Build/run commands**: populate Quick start with copy-pasteable shell
  commands grouped by action (install → build → run/test) in fenced code
  blocks.
- **What's demonstrated**: within Architecture, identify the concrete
  capabilities, techniques, or patterns the project showcases.
- **"Why this design" note**: for each Key decision, state the rationale —
  why this approach rather than a visible alternative — grounded in actual
  implementation choices.

### 4. Apply quality rules

- Be factual. Never invent features, commands, benchmarks, or architecture not
  present in the repo.
- If a fact is missing, write "Not yet documented" or omit rather than guessing.
- Before finishing, confirm that every command in Quick start appears in a
  manifest, script, or CI file.
- Use Markdown headings, fenced code blocks for all commands, and short
  descriptive bullets.
- Prefer clarity and accuracy over marketing language.
- The README itself contains no commentary, preambles, or meta-notes.
- Do not use placeholders (`TODO`, `TBD`, `[your-project-name]`) unless they
  reflect real repository state.

## Output

Write `README.md` at the repository root, or in the subdirectory given as the
argument. If one already exists, update it in place and keep accurate
existing content. Then reply with the path and a one-line summary. Print the
content only if the user asks for a preview.

## Output template

````md
# Project Name

[Badges if available]

## Overview

<!-- One-line value proposition, then the purpose paragraph -->
One-line value proposition followed by a concise description.

## Quick start

```bash
# install
...

# build
...

# run
...
```

## Architecture

<!-- What's demonstrated: structural overview + concrete capabilities -->
<!-- or patterns showcased -->
Brief description of the main components and how they interact.

## Key decisions

<!-- "Why this design": each bullet states the choice and its rationale -->
<!-- over alternatives -->
- **Decision 1**: explanation — why this approach over alternatives.
- **Decision 2**: explanation — why this approach over alternatives.
- **Decision 3**: explanation — why this approach over alternatives.

## Benchmarks

<!-- Include only if the repo contains benchmark results; else omit -->
Results with context and commands to reproduce.

## License

This project is licensed under the [License Name].
````
