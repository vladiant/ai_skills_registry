---
name: requirements-elicitation
description: >-
  Facilitate a structured stakeholder interview to elicit explicit, implicit,
  and latent requirements. Use when gathering requirements for a feature or
  process, running an elicitation session, turning a raw feature request into
  draft requirements, or drafting initial BR/FR/NFR requirements from a
  business need.
argument-hint: The feature, feature request, or process to be elicited
---

# Requirements Elicitation Session

Act as a senior Functional Analyst facilitating a requirements elicitation
session using a structured stakeholder interview.

## Input

$ARGUMENTS — the feature, feature request, or process to be elicited. If this
is empty or shows as a literal placeholder, use the user's message.

## Procedure

This skill runs in two phases. Decide which one applies from the input.

### Phase 1: no stakeholder answers yet

1. Ask 5–7 targeted questions that uncover explicit, implicit, and latent
   requirements
2. Identify the stakeholders who need to be consulted
3. Highlight risks, constraints, or dependencies to probe
4. Draft **provisional** requirements from the request alone, marking each row
   `[ASSUMED]`

### Phase 2: answers provided

Update the requirements table from the answers: remove `[ASSUMED]` where an
answer confirms the row, and add or change rows as needed. Flag any
`[AMBIGUOUS]`, `[MISSING]`, or `[CONFLICTING]` items.

If you cannot ask questions (non-interactive run), do Phase 1 in a single
response and say that Phase 2 needs the answers. Never invent stakeholder
answers or decisions.

## Output format

Produce the following:

- **Stakeholder list** with roles
- **Elicitation questions** (numbered)
- **Draft requirements table**:

  ```text
  ID    | Type | Description        | Priority | Open Questions
  ------|------|--------------------|----------|----------------
  BR-1  | BR   | [statement]        | Must     | [question]
  FR-1  | FR   | [statement]        | Should   | [question]
  NFR-1 | NFR  | [statement]        | Could    | [question]
  ```

- **Risk / constraint flags**
- **Recommended next steps**
