---
name: readme-creation
description: "Generate a README.md for this repository. Use when asked to create, write, update, or improve a README, document a project, produce a project overview, or write repository documentation."
argument-hint: "Optional: path to a specific subdirectory or package to document"
---

# README Creation

You are a senior technical writer and software architect. Your task is to author a production-quality `README.md` for this repository by inspecting the actual codebase, configuration files, and project metadata before writing.

## When to use

- Creating or rewriting a project README from scratch
- Updating an outdated or incomplete README
- Producing a credible project overview for developers or evaluators
- Documenting a new repository for the first time

## Procedure

### 1. Inspect the repository

Before writing, read:
- Source folders and main entry points
- Package manifests (`package.json`, `pyproject.toml`, `go.mod`, `Cargo.toml`, etc.)
- Config and Docker files
- Existing tests and examples
- Any existing `README.md`, `CHANGELOG`, or `docs/` content
- The license file or repository metadata for the license name

### 2. Generate sections in this exact order

1. **Badges** — only badges provable from the repo (language, license, CI status, version). Omit if none are reliable.
2. **One-line value proposition** — a single sentence stating the project's purpose and who it helps.
3. **Quick start** — exact, working install/build/run commands from the repo's manifests and scripts.
4. **Architecture** — compact but accurate overview of the main components and how they interact.
5. **Key decisions** — 3–6 important design choices with rationale tied to the implementation.
6. **Benchmarks** — quantitative data only if the repo already contains benchmark results; otherwise state that no formal benchmark suite is documented.
7. **License** — the project's actual license sourced from the license file or metadata.

### 3. Apply the content template

Use this four-part writing pattern across the body:

- **Purpose paragraph**: open Overview with what the project is, what problem it solves, and who should use it.
- **Build/run commands**: populate Quick start with copy-pasteable shell commands grouped by action (install → build → run/test) in fenced code blocks.
- **What's demonstrated**: within Architecture, identify the concrete capabilities, techniques, or patterns the project showcases.
- **"Why this design" note**: for each Key decision, state the rationale — why this approach rather than a visible alternative — grounded in actual implementation choices.

### 4. Apply quality rules

- Be factual. Never invent features, commands, benchmarks, or architecture not present in the repo.
- If a fact is missing, write "Not yet documented" or omit rather than guessing.
- Use Markdown headings, fenced code blocks for all commands, and short descriptive bullets.
- Prefer clarity and accuracy over marketing language.
- Return only the final `README.md` content — no commentary, preambles, or meta-notes.
- Do not use placeholders (`TODO`, `TBD`, `[your-project-name]`) unless they reflect real repository state.

## Output template

````md
# Project Name

[Badges if available]

## Overview

<!-- Purpose paragraph -->
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

<!-- What's demonstrated: structural overview + concrete capabilities or patterns showcased -->
Brief description of the main components and how they interact.

## Key decisions

<!-- "Why this design": each bullet states the choice and its rationale over alternatives -->
- **Decision 1**: explanation — why this approach over alternatives.
- **Decision 2**: explanation — why this approach over alternatives.
- **Decision 3**: explanation — why this approach over alternatives.

## Benchmarks

If benchmark evidence exists, include it here with context and commands to reproduce.
Otherwise: No formal benchmark suite is documented in this repository yet.

## License

This project is licensed under the [License Name].
````
