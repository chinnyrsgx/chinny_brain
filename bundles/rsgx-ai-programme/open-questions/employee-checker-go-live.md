---
type: Open Question
title: "What must be true before the Employee Checker reads live HR data?"
description: "The A2A pilot runs on SAMPLE data until an HR owner is named, a privacy impact assessment is done, and the minimised dataSights view and its scoped login exist."
tags: [agent-platform, a2a, pilot, hr, privacy, decision-needed, time-sensitive]
status: draft
provenance: P
owner: human:cchin
generated: { by: claude/claude-opus-5-5, at: 2026-10-12T00:30:00Z }
stale_after: 2027-01-31T00:00:00Z
sources:
  - id: pilot
    resource: /decisions/a2a-pilot-employee-checker.md
    title: First A2A pilot [P]
---

# Question

Who signs off live HR data flowing to the Employee Checker, and on what evidence?[^pilot]

# Needed before go-live

1. **An HR owner**, named in the agent's manifest. An agent never owns itself.
2. **A privacy impact assessment** for employment-status data used for seat hygiene.
3. **The minimised view** `AI_EmployeeStatus` created in dataSights by a person, and a **read-only login scoped to that one view**, requested from dataSights. Never the shared database login.
4. **A reference list from HR** to measure the checker's inactive verdicts against before anyone acts on them.
5. **Where the register lives.** A register page in the AI Hub that reads each agent's card is proposed but not built.

# Shelf life

Revisit by 31 Jan 2027, or sooner if the Forum chooses an agent platform.

[^pilot]: First A2A pilot [P]
