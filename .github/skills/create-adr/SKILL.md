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

## Missing input

If the problem, drivers, or options are missing, ask up to 3 questions. If you
cannot ask (non-interactive run) or the user says to proceed, record what is
known and mark gaps `[ASSUMED]` or `Not specified`. Never invent deciders,
dates, or options the user did not mention.

## Procedure

1. Gather the context: the problem being solved, why the decision is needed
   now, the decision drivers, and the options considered.
2. Find where ADRs live: look for an existing folder such as `docs/adr/`,
   `docs/decisions/`, or `adr/`. Continue its numbering and filename pattern
   (for example `0007-use-kafka.md`). If none exists, propose `docs/adr/` and
   start at `0001`.
3. Fill in the template below based on the provided context, keeping each
   section factual and tied to the stated drivers.
4. Set `Date` to today's date. Set `Status` to `Proposed` unless the user says
   the decision is already accepted. Write `Not specified` for `Deciders` if
   the user did not name them.
5. State the chosen option explicitly and justify it over the alternatives.
6. List both positive and negative consequences — never omit the trade-offs.

## Output

Write the ADR to the chosen location, then reply with its path and a one-line
summary of the decision. If the user only wants a preview, print it instead.

## Template

```markdown
# ADR-[NUMBER]: [Short Title of Decision]

- **Date:** [YYYY-MM-DD]
- **Status:** [Proposed | Accepted | Rejected | Deprecated | Superseded]
- **Deciders:** [List of people involved, or "Not specified"]

---

## Context and Problem Statement

[Describe the context and the problem that needs to be solved.
Why is this decision needed now?]

## Decision Drivers

- [Driver 1 — e.g., scalability requirement]
- [Driver 2 — e.g., team expertise]
- [Driver 3 — e.g., cost constraint]

## Considered Options

1. [Option A]
2. [Option B]
3. [Option C]

## Decision Outcome

**Chosen option:** [Option X]

**Rationale:** [Explain why this option was selected over the others]

### Positive Consequences

- [Benefit 1]
- [Benefit 2]

### Negative Consequences / Trade-offs

- [Risk or downside 1]
- [Risk or downside 2]

## Pros and Cons of the Options

### Option A — [Name]

- ✅ [Pro]
- ✅ [Pro]
- ❌ [Con]

### Option B — [Name]

- ✅ [Pro]
- ❌ [Con]
- ❌ [Con]

### Option C — [Name]

- ✅ [Pro]
- ❌ [Con]

## Links & References

- [Related ADR or doc]
- [External reference]
```
