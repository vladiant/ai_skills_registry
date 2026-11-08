---
name: design-new-service
description: >-
  Design a new service or system from scratch as a Solution Architect. Use
  when starting a greenfield service, turning a business capability into an
  architecture proposal, or producing first design artifacts: a context
  diagram, component breakdown, technology recommendations, an initial ADR,
  and a risk register.
argument-hint: The service or system to design
---

# Design New Service Architecture

Act as a Solution Architect designing a new service or system from scratch.

## Missing input

Check which of these the user has already answered, and ask only about the
rest (at most 5 questions):

1. The **primary business capability** this service is responsible for
2. The expected **load** (requests/sec, data volume, concurrency)
3. The **SLA/SLO requirements** (uptime, latency targets)
4. The **existing systems** it must integrate with
5. Any **compliance requirements** (GDPR, HIPAA, PCI-DSS, SOC2)
6. The **team size and cloud preference**

If you cannot ask (non-interactive run) or the user says to proceed, list
every unanswered item as an `[ASSUMED]` value and continue. Never invent SLAs
or compliance obligations without marking them.

## Procedure

Produce the design as a single response with these parts:

1. **Assumptions & open questions** — every `[ASSUMED]` item
2. **Context diagram** — a Mermaid `flowchart` showing the system boundary,
   users, and external systems
3. **Component breakdown** — each component with its responsibility and the
   data it owns
4. **Technology recommendations** — with rationale tied to the stated
   requirements, not trends
5. **Initial ADR** for the top 1–2 decisions, using the `create-adr` skill
   template
6. **Risk register** — risk, likelihood, impact, mitigation

## Output

Reply inline. Write the ADR as a file only if the user asks for files; in that
case follow the `create-adr` skill for location and numbering.
