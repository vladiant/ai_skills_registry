---
name: create-adr
description: >-
  Document a significant architectural decision as an Architecture Decision
  Record using the MADR (Markdown Any Decision Records) format. Use when asked
  to create, write, or record an ADR, or to capture the rationale for a
  technology or design choice.
argument-hint: The decision to record (e.g. "use Kafka over RabbitMQ")
---

# Create Architecture Decision Record (ADR)

Document a significant architectural decision using the MADR (Markdown Any
Decision Records) format.

## When to use

- Recording a significant or hard-to-reverse architectural decision
- Capturing the rationale for a technology, pattern, or design choice
- Giving future maintainers the context behind a decision

## Procedure

1. Gather the context: the problem being solved, why the decision is needed
   now, the decision drivers, and the options considered.
2. Assign the next sequential ADR number and a short, descriptive title.
3. Fill in the template below based on the provided context, keeping each
   section factual and tied to the stated drivers.
4. State the chosen option explicitly and justify it over the alternatives.
5. List both positive and negative consequences — never omit the trade-offs.

## Template

Fill in the following template based on the context provided:

```markdown
# ADR-[NUMBER]: [Short Title of Decision]

- **Date:** [YYYY-MM-DD]
- **Status:** [Proposed | Accepted | Deprecated | Superseded]
- **Deciders:** [List of people involved]

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

## Example trigger

> "Create an ADR for our decision to use Kafka over RabbitMQ for event
> streaming."
