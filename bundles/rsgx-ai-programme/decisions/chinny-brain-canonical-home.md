---
type: Decision Record
title: "chinny_brain is the canonical home of the programme brain, conforming to rsgx-okf"
description: "All programme context and outputs are published to the company team repository chinnyrsgx/chinny_brain and must conform to the rsgx-okf framework."
tags: [rsgx, repository, governance, okf, source-of-truth]
status: draft
decision_status: decided
provenance: C
decided_by: human:cchin
decided_at: 2026-09-30T02:00:00Z
provenance_basis: "Owner's explicit instructions in the 30 Sep session. Text drafted by Claude from those instructions; not yet ground-truthed by the owner."
generated: { by: claude/claude-opus-5-5, at: 2026-09-30T02:00:00Z }
sources:
  - id: s-0930
    resource: "PLACEHOLDER: replace with the claude.ai URL of the 2026-09-30 session"
    title: Session 2026-09-30 — chinny_brain repository and handover
---

# Decision

Three instructions from the owner, recorded as given:[^s-0930]

1. **All context and outputs from this project are to be uploaded** to `chinnyrsgx/chinny_brain`.
2. **They must conform to the OKF framework** held at `rsgx-org-ai/rsgx-okf`.
3. **`chinny_brain` is a company team account, not a personal one.** Placing RSGx-internal material there in full is therefore sanctioned.

# What this decision does not settle

Keep these separate. Each is a proposal or an open item, not part of the decision:

- **Folder structure.** This is Claude's proposal. See the [repo structure assessment](/assessments/repo-structure-recommendation.md).
- **Enforcement.** Branch protection, code owners, the second approver and attribution are unresolved. See [repo governance prerequisites](/open-questions/repo-governance-prerequisites.md).
- **Which rules rsgx-okf adds beyond OKF v0.2.** Claude could not read the repo. See [rsgx-okf profile reconciliation](/open-questions/rsgx-okf-profile-reconciliation.md).

# Implications (Claude's reading, not decided)

- The claude.ai project stops being the system of record. Session outputs become pull requests against this repository.
- This bundle's [supersession of Programme Record v0.1 and HANDOFF.md](/decisions/bundle-supersedes-record.md) carries over unchanged. The repository hosts that decision; it doesn't reopen it.

[^s-0930]: Session 2026-09-30 — chinny_brain repository and handover
