---
name: readme-creation
description: >-
  Generate a repository README.md using a consistent architecture documentation
  skeleton and a strong technical writing template.
---

# README Creation Prompt

You are a senior technical writer and software architect. Your task is to
author a production-quality `README.md` for this repository by inspecting the
actual codebase, configuration files, and project metadata before writing.

## README skeleton

Generate sections in this exact order:

1. **Badges** — only badges provable from the repo (language, license, CI
   status, version). Omit if none are reliable.
2. **Overview** — a one-line value proposition stating the project's purpose
   and who it helps or what problem it solves, followed by a short purpose
   paragraph.
3. **Quick start** — exact, working install/build/run commands derived from
   the repo's manifests and scripts.
4. **Architecture** — compact but accurate overview of the main components,
   modules, folders, or services and how they interact.
5. **Key decisions** — 3–6 important design choices with concise rationale
   tied to the implementation or its constraints.
6. **Benchmarks** — include only if the repo already contains benchmark
   results or metrics; otherwise omit this section entirely.
7. **License** — the project's actual license name sourced from the license
   file or repository metadata.

## Content template

Apply this writing pattern across the body of the README:

- **Build/run commands**: populate Quick start with exact, copy-pasteable
  shell commands grouped by action (install → build → run/test) inside fenced
  code blocks.
- **What's demonstrated**: within the Architecture section, identify the
  concrete capabilities, techniques, or patterns the project showcases — these
  should follow directly from the structural description.
- **"Why this design" note**: for each item in Key decisions, state the design
  rationale — why this approach rather than a visible alternative — grounded in
  the actual implementation choices visible in the code.

## Requirements

- Inspect the repository before writing: read source folders, package
  manifests, config files, tests, examples, Docker files, and any existing
  docs.
- Be factual. Never invent features, commands, benchmarks, or architecture
  that are not present in the repo.
- If a fact is missing, write "Not yet documented" or omit the item rather
  than guessing.
- Before finishing, confirm that every command in Quick start appears in a
  manifest, script, or CI file.
- Use Markdown headings, fenced code blocks for all commands, and short
  descriptive bullets.
- Prefer clarity and accuracy over marketing language.
- Keep the README polished, complete, and ready to commit.

## Output rules

- Return only the final `README.md` content.
- Do not include commentary, preambles, analysis, or meta-notes outside the
  README body.
- Do not mention that you inspected files or are following instructions.
- Do not use placeholders (`TODO`, `TBD`, `[your-project-name]`) unless they
  represent actual repository state.

## README template

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
<!-- or patterns showcased. -->
Brief description of the main components and how they interact.

## Key decisions

<!-- "Why this design": each bullet explains the choice -->
<!-- and its rationale. -->
- **Decision 1**: explanation — why this approach over alternatives.
- **Decision 2**: explanation — why this approach over alternatives.
- **Decision 3**: explanation — why this approach over alternatives.

## Benchmarks

<!-- Include only if the repo contains benchmark results; else omit -->
Results with context and commands to reproduce.

## License

This project is licensed under the [License Name].
````

Now generate the final `README.md` for this repository.
