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

## When to use

- Comparing current behaviour against a desired future state
- Planning a migration, redesign, or capability upgrade
- Identifying and prioritizing missing or changed capabilities

## Procedure

Given the current state and target state provided:

1. Map the **AS-IS** process or system behaviour in detail
2. Define the **TO-BE** target state aligned with business objectives
3. Identify each **gap** (missing capability, changed behaviour, removed
   feature)
4. Classify each gap by **Type** (Process / Data / System / People) and
   **Priority** (High / Med / Low)
5. Recommend remediation actions for each gap
6. Flag **risks** if gaps are not addressed

## Output format

Produce a gap table:

```text
# | Area | AS-IS | TO-BE | Gap | Type | Priority | Remediation
--|------|-------|-------|-----|------|----------|------------
1 | ...  | ...   | ...   | ... | ...  | ...      | ...
```

Followed by:

- **Summary** of critical gaps
- **Risk register** for unaddressed gaps
- **Recommended next steps**

## Example trigger

> "Run a gap analysis between our manual invoice approval process and a fully
> automated TO-BE workflow."
