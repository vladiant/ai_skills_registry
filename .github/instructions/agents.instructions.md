---
applyTo: ".github/agents/*.md"
---

# Agent authoring rules

- Frontmatter needs `name` (equal to the file name) and `description` that
  says what the agent does and when to use it.
- Agents are installed into other repositories. Do not hardcode paths such as
  `/docs/...` and do not say "this repository"; say "use existing X if
  present, otherwise propose a location and ask".
- Include a `## Missing input` section with the same non-blocking rule the
  skills use.
- Use Mermaid for every diagram.
- Do not add persona claims ("15+ years") or lists of tool names; they cost
  tokens and change no behavior.
- Keep output formats consistent with the matching skill (for example the
  gap analysis columns), and say which skill defines the rubric.
- Link at most a handful of references, and only ones the agent relies on.
