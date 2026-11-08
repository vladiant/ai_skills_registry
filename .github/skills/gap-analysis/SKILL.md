---
name: gap-analysis
description: >-
  Perform a structured AS-IS → TO-BE gap analysis, classifying and prioritizing
  gaps with remediation actions. Use when comparing current and target state,
  planning a migration or change, or identifying missing capabilities between
  where a system is and where it needs to be.
argument-hint: The current (AS-IS) and target (TO-BE) states to compare
---

# Gap Analysis

Act as a Functional Analyst performing a structured gap analysis using
AS-IS → TO-BE state analysis.

## Missing input

If the AS-IS or TO-BE state is missing or too vague to compare, ask up to 5
questions. If you cannot ask (non-interactive run) or the user says to
proceed, describe what you assume as `[ASSUMED]` and continue. Never invent
facts about the current state.

## Procedure

Given the current state and target state provided:

1. Map the **AS-IS** process or system behaviour in detail
2. Define the **TO-BE** target state aligned with business objectives
3. Identify each **gap** (missing capability, changed behaviour, removed
   feature)
4. Classify each gap by **Type** (Process / Data / System / People) and
   **Priority** using the rubric below
5. Recommend remediation actions for each gap
6. Flag **risks** if gaps are not addressed

## Priority rubric

- **High** — blocks the TO-BE goal, or carries compliance, security, or
  data-loss risk
- **Med** — degrades the outcome but a workaround exists
- **Low** — cosmetic or nice-to-have; safe to defer

## Output format

Produce a Markdown table:

| # | Area | AS-IS | TO-BE | Gap | Type | Priority | Remediation |
|---|------|-------|-------|-----|------|----------|-------------|
| 1 | ...  | ...   | ...   | ... | ...  | ...      | ...         |

Followed by:

- **Summary** of critical gaps
- **Risk register** for unaddressed gaps
- **Recommended next steps**
