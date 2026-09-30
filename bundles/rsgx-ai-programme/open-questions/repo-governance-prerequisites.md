---
type: Open Question
title: "Repository governance prerequisites: can the controls actually be enforced?"
description: "Plan tier, account model, second approver and Forum-minute storage decide whether chinny_brain's single-source-of-truth controls are real or advisory."
tags: [rsgx, repository, governance, iso-27001, audit, blocker-candidate]
status: draft
provenance: P
owner: human:cchin
generated: { by: claude/claude-opus-5-5, at: 2026-09-30T02:00:00Z }
sources:
  - id: s-0930
    resource: "PLACEHOLDER: replace with the claude.ai URL of the 2026-09-30 session"
    title: Session 2026-09-30 — chinny_brain repository and handover
  - id: gh-protected
    resource: https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches
    title: GitHub Docs — About protected branches
---

# Why it matters

The v0.2 [document fork](/findings/document-fork-v0-2.md) happened because nothing structurally prevented two parallel "current" versions. The repository fixes that only if its controls are enforced. If they aren't, "single source of truth" is a convention again.

# Questions for the owner

1. **Plan tier.** Protected branches and required code-owner review on a *private* repository need a paid GitHub plan (Pro, Team or Enterprise).[^gh-protected] Which plan is chinnyrsgx on?
2. **Account model.** Is chinnyrsgx a GitHub organisation whose people use named accounts, or one login shared by the team? A shared login makes every commit look like the same person. That destroys the attribution the audit audience relies on, and runs against ISO/IEC 27001:2022 expectations on access control and change management (indicatively A.5.15, A.8.32). This is not an audit opinion.
3. **Second approver.** GitHub doesn't let authors approve their own pull requests. With the owner as sole code owner, required review makes merging impossible. Who is the second approver, and which Forum role may sign a `ratification` block?
4. **Forum minutes.** A `ratification.ref` has to resolve to something an auditor can open. Where do Forum minutes live: in this repository or in a linked system of record?
5. **Long-term home.** Should chinny_brain later move under `rsgx-org-ai`, next to rsgx-okf? That would put ownership and access under the organisation's own controls.

# Recommendation

Resolve questions 1–3 before the migration PR is merged, and question 4 before the first ratification is recorded. Question 5 can wait.[^s-0930]

[^gh-protected]: GitHub Docs — About protected branches
[^s-0930]: Session 2026-09-30 — chinny_brain repository and handover
