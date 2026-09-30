---
type: Open Question
title: "Forum: adopt the control-plane pattern and select Option A or Option B?"
description: "The platform recommendation needs a Forum decision, and the decision needs four pieces of evidence the 28 Sep research could not supply."
tags: [agent-platform, forum, decision-needed, time-sensitive]
status: draft
provenance: P
owner: human:cchin
decision_body: AI Steering Committee (Forum)
generated: { by: claude/claude-opus-5-5, at: 2026-09-30T02:00:00Z }
stale_after: 2027-03-01T00:00:00Z
sources:
  - id: platform-report
    resource: /references/agent-platform-report-2026-09-28.md
    title: Agent platform report, 28 Sep 2026 (mirrored)
---

# Question for the Forum

1. Adopt the vendor-neutral control-plane pattern described in the [recommendation](/assessments/agent-platform-recommendation.md)?
2. Select **Option A** (Microsoft Foundry) or **Option B** (AWS Bedrock AgentCore, Malaysia) as the primary runtime?

# Evidence needed before deciding

The 28 Sep research could not establish any of these:[^platform-report]

1. **Identity estate.** Is RSGx on Microsoft 365/Entra? That largely decides Option A.
2. **Malaysia-region facts, in writing from the vendor:**
   - per-feature availability in-region;
   - cross-region inference behaviour, since AgentCore Memory, Policy and Evaluations may route out of region;
   - where Claude processing takes place under Microsoft's subprocessor terms.
3. **ContextForge security review.** Its earlier releases were labelled alpha.
4. **Pricing and UI cost.** No pricing was verified. The [UI gap](/assessments/agent-platform-ui-gap.md) cost for Option B needs estimating.

# Dependencies

- **Blocked by:** nothing. The Forum can adopt the pattern now and defer the runtime choice until the evidence arrives.
- **Gates:** L3 pilots, which are also gated by blocker [PR-17](/open-questions/pr-17-iso-27001-baseline.md); and real data for the [Forum governance dashboard](/prototypes/forum-governance-dashboard.md).

# Shelf life

All vendor feature and regional claims must be re-verified by 1 Mar 2027 and at contract signature.

[^platform-report]: Agent platform report, 28 Sep 2026 (mirrored)
