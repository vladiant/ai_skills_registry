---
name: create-adr
description: >-
  Document a significant architectural decision as an Architecture Decision
  Record using the MADR (Markdown Any Decision Records) format. Use when asked
  to create, write, or record an ADR, to capture the rationale for a
  technology or design choice, or to document a hard-to-reverse decision.
argument-hint: The decision to record (e.g. "use Kafka over RabbitMQ")
---

# Create Architecture Decision Record (ADR)

Document a significant architectural decision using the MADR (Markdown Any
Decision Records) format.

## Input

$ARGUMENTS — the decision to record. If this is empty or shows as a literal
placeholder, use the user's message.

## Missing input

If the problem, drivers, or options are missing, ask up to 3 questions. If you
cannot ask (non-interactive run) or the user says to proceed, record what is
known and mark gaps `[ASSUMED]` or `Not specified`. Never invent decision
makers, dates, or options the user did not mention.

## Procedure

1. Gather the context: the problem being solved, why the decision is needed
   now, the decision drivers, and the options considered.
2. Find where ADRs live: look for an existing folder such as `docs/adr/`,
   `docs/decisions/`, or `adr/`. Continue its numbering and filename pattern
   (for example `0007-use-kafka.md`). If none exists, propose `docs/adr/` and
   start at `0001`. The number lives in the file name, not in the title.
3. Fill in the template below based on the provided context, keeping each
   section factual and tied to the stated drivers.
4. Set `date` to today's date. Set `status` to `proposed` unless the user says
   the decision is already accepted. Write `Not specified` for
   `decision-makers` if the user did not name them.
5. State the chosen option explicitly and justify it over the alternatives.
6. List both good and bad consequences — never omit the trade-offs.

## Output

Write the ADR to the chosen location, then reply with its path and a one-line
summary of the decision. If the user only wants a preview, print it instead.

## Template

This follows the MADR 4 layout. Drop the `consulted`, `informed`, and
`Confirmation` parts if the user gave nothing for them.

```markdown
---
status: "proposed | accepted | rejected | deprecated | superseded by ADR-NNNN"
date: YYYY-MM-DD
decision-makers: "names, or Not specified"
consulted: "optional"
informed: "optional"
---

# Short title that names the problem and the solution

## Context and Problem Statement

[Describe the context and the problem that needs to be solved.
Why is this decision needed now?]

## Decision Drivers

- [Driver 1 — e.g., scalability requirement]
- [Driver 2 — e.g., team expertise]
- [Driver 3 — e.g., cost constraint]

## Considered Options

- [Option A]
- [Option B]
- [Option C]

## Decision Outcome

Chosen option: "[Option X]", because [justification over the others].

### Consequences

- Good, because [positive consequence]
- Bad, because [negative consequence or trade-off]

### Confirmation

[How compliance with this decision will be verified, e.g. a review, a test,
or a fitness function. Optional.]

## Pros and Cons of the Options

### [Option A]

- Good, because [argument]
- Neutral, because [argument]
- Bad, because [argument]

### [Option B]

- Good, because [argument]
- Bad, because [argument]

## More Information

[Related ADRs, documents, or external references.]
```
