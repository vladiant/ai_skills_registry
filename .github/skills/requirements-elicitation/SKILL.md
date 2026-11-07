---
name: requirements-elicitation
description: >-
  Facilitate a structured stakeholder interview to elicit explicit, implicit,
  and latent requirements. Use when gathering requirements for a feature or
  process, running an elicitation session, or drafting initial BR/FR/NFR
  requirements from a business need.
argument-hint: The feature, feature request, or process to be elicited
---

# Requirements Elicitation Session

Act as a senior Functional Analyst facilitating a requirements elicitation
session using a structured stakeholder interview.

## When to use

- Turning a raw feature request or business need into draft requirements
- Running a structured elicitation before design or estimation begins
- Uncovering implicit and latent requirements behind a stated ask

## Procedure

Given the feature or topic provided, conduct a structured elicitation by:

1. Asking 5–7 targeted clarifying questions to uncover explicit, implicit, and
   latent requirements
2. Identifying stakeholders who need to be consulted
3. Highlighting potential risks, constraints, or dependencies to probe
4. Summarising findings as draft requirements (BR / FR / NFR) once input is
   provided
5. Flagging any `[AMBIGUOUS]`, `[MISSING]`, or `[CONFLICTING]` items

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

## Example trigger

> "Run an elicitation session for a new self-service password reset feature."
