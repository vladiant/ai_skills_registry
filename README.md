# AI Skills Registry

This repository is a GitHub-hosted skill registry for AI coding agents.
It stores reusable skill definitions in a Git-native format so they can be
installed into local agent environments with the `skills` CLI.

## Installation

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
- the installation is reproducible and can be validated against a lock file;
- updates can be pulled with `npx skills update`.

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

- `readme-creation` — generate a production-ready repository `README.md`
  from real repository structure, metadata, and commands.
- `agents-md-creation` — generate a focused, best-practice `AGENTS.md`
  with progressive disclosure and repository-specific standards.

## Repository layout

```text
ai_skills_registry/
├── .github/                          # repository metadata, automation, and config
│   ├── agents/                      # agent definitions for the registry
│   ├── instructions/                # repo-level behavior and coding guidance
│   ├── skills/                      # reusable skill definitions
│   ├── actions/                     # shared workflow actions
│   ├── workflows/                   # CI validation workflows
│   └── mcp/                         # MCP integration configuration
├── .claude/                         # Claude project configuration
├── hooks/                           # git hooks and helper scripts
├── plugins/                         # plugin extensions and integrations
└── prompts/                        # reusable prompt templates
```

## Maintenance

```bash
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
