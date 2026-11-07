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

## Repository layout

```text
ai_skills_registry/
├── .github/
│   ├── copilot-instructions.md
│   ├── skills/
│   │   └── readme-creation/
│   │       └── SKILL.md
│   └── workflows/
├── prompts/
├── README.md
├── LICENSE
└── .github/skills/.../SKILL.md
```

## Maintenance

```bash
# Refresh installed skills
npx skills update

# Refresh a specific skill
npx skills update readme-creation
```

## References

* [A practical guide to structuring an AI agent repository — and why every
  folder matters](https://medium.com/@iduryodhanrao/a-practical-guide-to-structuring-an-ai-agent-repository-and-why-every-folder-matters-d1627a6dd022)
* <https://github.com/iduryodhanrao/agent-repo-template>
* [Централизованные хранилища скиллов (Skill registries)](https://habr.com/ru/articles/1087464/)
* <https://github.com/alex-lib/skills-registries>
* <https://github.com/vercel-labs/skills>