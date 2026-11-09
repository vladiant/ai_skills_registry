# AI Skills Registry

This repository is a GitHub-hosted registry for AI coding agents. It stores
reusable skills, agent definitions, and prompts in a Git-native format.
Skills install with the `skills` CLI; agents and prompts are plain Markdown
files you copy into place (see [Installation](#installation)).

## Installation

### Skills

Use the `skills` CLI to install skills from this repository:

```bash
# List available skills in this registry
npx skills add https://github.com/vladiant/ai_skills_registry.git --list

# Install one skill explicitly
npx skills add https://github.com/vladiant/ai_skills_registry.git \
  --skill readme-creation

# Install a skill for a specific agent
npx skills add https://github.com/vladiant/ai_skills_registry.git \
  --skill readme-creation \
  --agent claude-code \
  --agent cursor

# Install all skills available in the repository
npx skills add https://github.com/vladiant/ai_skills_registry.git \
  --skill '*' \
  --agent '*'
```

This repo follows the standard GitHub/GitLab + `npx skills` pattern:

- the source of truth lives in Git;
- the installer computes a checksum of the installed skill files;
- installs are recorded in `skills-lock.json`, so they are reproducible and
  can be validated against it;
- updates can be pulled with `npx skills update`.

### Agents

The `skills` CLI installs skills only. Agents are single Markdown files with
`name` and `description` frontmatter, so copy them into the folder your tool
reads. Replace `solution-architect` with the agent you want.

```bash
RAW=https://raw.githubusercontent.com/vladiant/ai_skills_registry/main

# GitHub Copilot custom agent, for this repository
mkdir -p .github/agents
curl -fsSL "$RAW/.github/agents/solution-architect.md" \
  -o .github/agents/solution-architect.agent.md

# Claude Code subagent, for this project (use ~/.claude/agents for all)
mkdir -p .claude/agents
curl -fsSL "$RAW/.github/agents/solution-architect.md" \
  -o .claude/agents/solution-architect.md
```

For Copilot, an organization can share agents by putting them in the root
`agents/` folder of its `.github` repository.

Each agent calls skills from this registry, so install those too:

| Agent                | Skills it relies on                    |
|----------------------|----------------------------------------|
| `solution-architect` | `create-adr`                           |
| `functional-analyst` | `gap-analysis`                         |

### Prompts

Prompts are for assistants that cannot load skills. They are plain Markdown
with no tool-specific format: paste the text below the frontmatter into a
chat, or save it wherever your tool keeps reusable prompts. They are
generated from the skill of the same name, so the skill is always the
up-to-date version.

## Available skills

- `readme-creation` — generate or improve a repository `README.md` using
  the repository's actual structure and project metadata.
- `create-adr` — document a significant architectural decision as an
  Architecture Decision Record using the MADR format.
- `architecture-review` — review an existing architecture across
  reliability, scalability, security, observability, cost, and operability.
- `design-new-service` — design a new service from scratch, gathering
  requirements then producing diagrams, component breakdown, and an ADR.
- `requirements-elicitation` — facilitate a structured stakeholder interview
  to elicit explicit, implicit, and latent requirements as draft BR/FR/NFR.
- `gap-analysis` — perform a structured AS-IS → TO-BE gap analysis with
  classified, prioritized gaps and remediation actions.
- `user-story-generator` — generate Agile user stories with Given/When/Then
  acceptance criteria, MoSCoW priority, complexity, and dependencies.
- `agents-md-creation` — create a concise, repository-specific `AGENTS.md`
  using progressive disclosure and practical agent-governance rules.
- `minimal-agents-md-creation` — create a very small `AGENTS.md` covering
  only the essentials: project description, commands, stack, examples, and
  boundaries.
- `agent-definition-creator` — create specialized `.github/agents/*.md`
  files for QA, docs, and lint work using repository-specific commands and
  boundaries.
- `agends-md-refactor` — refactor an existing `AGENTS.md` into a minimal root
  file plus separate topic docs following progressive disclosure.

## Available agents

- `solution-architect` — expert Solution Architect for designing scalable,
  resilient, cost-effective systems and evaluating architectural trade-offs.
- `functional-analyst` — experienced Functional Analyst that elicits,
  analyzes, documents, and validates requirements across the lifecycle.

## Available prompts

Prompts are generated from the skill of the same name. Do not edit them by
hand; see [Maintenance](#maintenance).

- `readme-creation` — generate a production-ready repository `README.md`
  from real repository structure, metadata, and commands.
- `agents-md-creation` — generate a focused, best-practice `AGENTS.md`
  with progressive disclosure and repository-specific standards.

## Repository layout

```text
ai_skills_registry/
├── .github/               # repository metadata, automation, and config
│   ├── agents/            # agent definitions for the registry
│   ├── instructions/      # authoring rules scoped by file path
│   ├── skills/            # reusable skill definitions
│   ├── scripts/           # validation and prompt-generation scripts
│   └── workflows/         # CI validation and secret-scan workflows
└── prompts/               # reusable prompt templates
```

## Maintenance

```bash
# Validate the registry locally (the same checks run in CI)
python3 .github/scripts/validate_registry.py

# Regenerate prompts after changing a skill (CI runs this with --check)
python3 .github/scripts/sync_prompts.py

# Refresh installed skills
npx skills update

# Refresh a specific skill
npx skills update readme-creation
```

## References

- [A practical guide to structuring an AI agent repository — and why every
  folder matters](https://medium.com/@iduryodhanrao/a-practical-guide-to-structuring-an-ai-agent-repository-and-why-every-folder-matters-d1627a6dd022)
- <https://github.com/iduryodhanrao/agent-repo-template>
- [Централизованные хранилища скиллов (Skill registries)](https://habr.com/ru/articles/1087464/)
- <https://github.com/alex-lib/skills-registries>
- <https://github.com/vercel-labs/skills>
