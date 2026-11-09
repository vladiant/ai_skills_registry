# AGENTS.md

You maintain a registry of AI skills, agents, and prompts. Every artifact is
a Markdown file with YAML frontmatter; there is no application code.

## Commands

```bash
# Structure, frontmatter, README consistency (use before commits)
python3 .github/scripts/validate_registry.py

# Prompts are generated from skills: rewrite them, then check
python3 .github/scripts/sync_prompts.py
python3 .github/scripts/sync_prompts.py --check

# Lint one file while editing
npx --yes markdownlint-cli2@0.23.2 ".github/skills/<name>/SKILL.md"

# Lint everything (use before commits, not after every edit)
npx --yes markdownlint-cli2@0.23.2 ".github/**/*.md" "prompts/**/*.md" \
  "README.md" "AGENTS.md"
```

CI runs the same three checks on every PR and on pushes to `main`.

## Tech stack

- Markdown with YAML frontmatter, linted by markdownlint-cli2 0.23.2
- Python 3, standard library only, for `.github/scripts/`
- GitHub Actions: `actions/checkout@v7`, `gitleaks/gitleaks-action@v3`
- Skills install with the `skills` CLI (`npx skills add`)

## Project structure

| Area                             | Purpose                                   |
|----------------------------------|-------------------------------------------|
| `.github/skills/<name>/SKILL.md` | One reusable skill per folder             |
| `.github/agents/*.md`            | Agent definitions                         |
| `prompts/*.md`                   | Generated skill copies; never hand-edited |
| `.github/instructions/`          | Authoring rules, scoped by file path      |
| `.github/scripts/`               | Validation and prompt generation          |

Skills are the source of truth. A prompt exists only if a skill of the same
name is listed in `PROMPTS` in `sync_prompts.py`.

## Code style

Descriptions route the skill, so they say what it does and when to use it.

```markdown
✅ description: >-
     Review an architecture for risk. Use when asked to review, audit,
     or critique a system design before a launch.

❌ description: Reviews architecture.
```

Skills must not stall in non-interactive runs.

```markdown
✅ If you cannot ask, list assumptions as `[ASSUMED]` and continue.

❌ Always ask the user clarifying questions before starting.
```

Per-type rules are in `.github/instructions/`.

## Testing

There is no test suite. `validate_registry.py` and
`sync_prompts.py --check` are the tests. After changing either script, break a
scratch copy of the repo on purpose (empty description, wrong `name`, skill
missing from the README, hand-edited prompt) and confirm the check fails.

## Boundaries

- ✅ Always: update `README.md` when adding, removing, or renaming a skill,
  agent, or prompt; run the validator before committing
- ⚠️ Ask first: renaming or deleting a skill or agent (it changes the install
  name); adding a dependency or a CI action
- 🚫 Never: edit `prompts/*.md` by hand; commit secrets; hardcode `/docs/...`
  paths in agents; add `When to use` or `Example trigger` sections to skills

## When stuck

Ask a clarifying question, or propose a plan and open a draft PR with notes.
Do not make large speculative rewrites.

## PR checklist

- `validate_registry.py` and `sync_prompts.py --check` pass
- markdownlint reports 0 issues
- `README.md` matches the directories
- Diff is focused; breaking changes are called out in the description

## Progressive disclosure

- Authoring rules: `.github/instructions/*.instructions.md`
- Assistant behavior in this repo: `.github/copilot-instructions.md`
- Installing and consuming artifacts: `README.md`
