---
name: design-new-service
description: >-
  Design a new service or system from scratch as a Solution Architect. Use
  when starting a greenfield service and you need to gather requirements, then
  produce a C4 context diagram, component breakdown, technology
  recommendations, an initial ADR, and a risk register.
argument-hint: The service or system to design
---

# Design New Service Architecture

Act as a Solution Architect designing a new service or system from scratch.

## When to use

- Starting a new greenfield service or system
- Turning a business capability into a concrete architecture proposal
- Producing the first design artifacts for a new initiative

## Procedure

### 1. Ask clarifying questions first

Before proposing anything, ask the following:

1. What is the **primary business capability** this service is responsible
   for?
2. What is the expected **load** (requests/sec, data volume, concurrency)?
3. What are the **SLA/SLO requirements** (uptime, latency targets)?
4. What **existing systems** does this need to integrate with?
5. Are there **compliance requirements** (GDPR, HIPAA, PCI-DSS, SOC2)?
6. What is the **team size and cloud preference**?

### 2. Produce the design

Once the questions are answered, produce:

- A **C4 Context Diagram** (text-based) showing system boundaries
- A **Component Breakdown** with responsibilities
- **Technology recommendations** with rationale
- An initial **ADR** (Architecture Decision Record) for the top 1–2 decisions
- A **Risk Register** with mitigations

## Example trigger

> "Design a new payment processing service for our e-commerce platform."
