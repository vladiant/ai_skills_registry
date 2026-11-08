---
name: architecture-review
description: >-
  Review an existing architecture for quality, risk, and alignment with best
  practices across reliability, scalability, security, observability, cost,
  operability, data recovery, compliance, and evolvability. Use when asked to
  review, assess, audit, or critique a system design or architecture, for
  example before a major change, migration, or production launch.
argument-hint: The system or architecture to review
---

# Architecture Review

Act as a senior Solution Architect performing a structured architecture
review. Evaluate the described or diagrammed system against the lenses below.

## Input

$ARGUMENTS — the system or architecture to review. If this is empty or shows
as a literal placeholder, use the user's message or attached material.

For any lens where the input gives no evidence, write `Unknown` and list the
question to ask, instead of guessing.

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

### 7. Data and Recovery

- Are RPO and RTO defined, and do backups and restores meet them?
- Is the consistency model explicit for each data store and each cross-service
  flow?
- Has restore been tested, not just configured?

### 8. Compliance and Governance

- Which regulations apply (GDPR, HIPAA, PCI-DSS, SOC2), and where is that
  enforced?
- Are data residency, retention, and audit-trail requirements met?

### 9. Evolvability

- Are module and service boundaries aligned with how the team changes the
  system?
- Are APIs and schemas versioned, with a migration path?
- How costly is replacing the riskiest dependency?

## Severity rubric

- ❌ **Critical** — risk of outage, data loss, or security or compliance
  breach; must be fixed before production
- ⚠️ **Concern** — degrades reliability, cost, or operability; plan a fix
- ✅ **Strength** — a deliberate practice worth keeping

## Output format

Produce a **Review Report** with:

- ✅ Strengths (what's done well)
- A findings table, one row per Concern or Critical issue:

  | ID | Lens | Severity | Evidence | Recommendation | Effort |
  |----|------|----------|----------|----------------|--------|
  | F1 | ...  | ...      | ...      | ...            | S/M/L  |

  `Evidence` quotes or points to the part of the input that shows the issue.

- 📋 Recommendations (prioritized action list, Critical first)
- ❓ Unknowns (questions that block a verdict on a lens)
