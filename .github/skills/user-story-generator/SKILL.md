---
name: user-story-generator
description: >-
  Generate well-formed Agile user stories with Given/When/Then acceptance
  criteria, MoSCoW priority, complexity, and dependencies. Use when turning a
  requirement or feature description into user stories, writing acceptance
  criteria, or breaking an epic into stories.
argument-hint: The requirement, feature request, or rough description to split
---

# User Story Generator

Act as a Functional Analyst. Generate well-formed Agile User Stories from the
requirement or feature description provided.

## When to use

- Turning a requirement or feature description into Agile user stories
- Writing Given/When/Then acceptance criteria for a feature
- Breaking an epic or rough idea into estimable stories

## Procedure

For each story:

- Write in the standard format: _As a [persona], I want [action], so that
  [benefit]_
- Provide 2–4 acceptance criteria in **Given / When / Then** format
- Assign a **MoSCoW priority**: Must / Should / Could / Won't
- Estimate **story complexity**: XS / S / M / L / XL
- List **dependencies** on other stories or systems
- Flag any **ambiguities** that require stakeholder clarification with
  `[AMBIGUOUS]`

Generate as many stories as needed to fully cover the feature. Group related
stories under an **Epic** label when applicable, and link each story to at
least one Business Requirement (`BR-`).

## Output format

```text
US-[ID]: [Title]
------------------------------
As a [persona],
I want to [action],
So that [benefit].

Acceptance Criteria:
  1. Given [context], When [action], Then [expected outcome]
  2. Given [context], When [action], Then [expected outcome]

Priority:     [Must / Should / Could / Won't]
Complexity:   [XS / S / M / L / XL]
Linked BR:    [BR-ID]
Dependencies: [list or "None"]
Open Items:   [AMBIGUOUS] flags or "None"
```

## Example trigger

> "Generate user stories for a shopping cart that supports saved items and
> guest checkout."
