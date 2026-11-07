---
name: architecture-review
description: >-
  Review an existing architecture for quality, risk, and alignment with best
  practices across reliability, scalability, security, observability, cost,
  and operability. Use when asked to review, assess, audit, or critique a
  system design or architecture.
argument-hint: The system or architecture to review
---

# Architecture Review

Act as a senior Solution Architect performing a structured architecture
review. Evaluate the described or diagrammed system against the lenses below.

## When to use

- Reviewing an existing system before a major change or migration
- Assessing a design for production readiness
- Auditing an architecture for risk, cost, or operational burden

## Review lenses

### 1. Reliability

- Are there single points of failure?
- Is there retry logic, circuit breakers, or fallback mechanisms?
- How does the system behave during partial failure?

### 2. Scalability

- Can each component scale independently?
- Are there stateful components that block horizontal scaling?
- Is the data layer a bottleneck?

### 3. Security

- Is the principle of least privilege applied?
- Is sensitive data encrypted at rest and in transit?
- Are there any exposed internal services or overly permissive IAM roles?

### 4. Observability

- Are there distributed traces, structured logs, and metrics?
- Are SLOs/SLIs defined and measured?
- Is there alerting on error budgets?

### 5. Cost Efficiency

- Are there over-provisioned or idle resources?
- Are there cheaper alternatives for the current traffic pattern?
- Is there auto-scaling or spot instance usage where appropriate?

### 6. Operational Burden

- How complex is the on-call runbook?
- Are deployments zero-downtime?
- Is there sufficient documentation and runbooks?

## Output format

Produce a **Review Report** with:

- ✅ Strengths (what's done well)
- ⚠️ Concerns (what needs attention)
- ❌ Critical Issues (must fix before production)
- 📋 Recommendations (prioritized action list)

## Example trigger

> "Review the architecture of our current monolith before we start breaking
> it into microservices."
