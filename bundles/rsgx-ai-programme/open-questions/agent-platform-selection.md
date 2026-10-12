---
type: Open Question
title: "Forum: adopt the control-plane pattern and select Option A or Option B?"
description: "The platform recommendation needs a Forum decision. Since 12 Oct both options are Australian (Foundry in Australia East, AgentCore in Sydney), and the decision needs evidence that desk research could not supply."
tags: [agent-platform, forum, decision-needed, time-sensitive, australia]
status: draft
provenance: P
owner: human:cchin
decision_body: AI Steering Committee (Forum)
generated: { by: claude/claude-opus-5-5, at: 2026-10-12T02:40:00Z }
stale_after: 2026-12-12T00:00:00Z
sources:
  - id: platform-report
    resource: /references/agent-platform-report-2026-10-12.md
    title: Agent platform report, 12 Oct 2026 (mirrored)
  - id: prior-report
    resource: /references/agent-platform-report-2026-09-28.md
    title: Agent platform report, 28 Sep 2026 (mirrored; superseded)
---

> **Revised 12 Oct 2026.** This question was first raised against the 28 Sep report,[^prior-report] which framed Option B in the Malaysia region. The owner confirmed in session that RSGx is Australian ([governing jurisdiction](/open-questions/governing-jurisdiction.md)), so both options and the evidence list now use Australian regions and law.[^platform-report] Redefining Option B changes what the Forum would be choosing, so the owner should approve this revision before it goes to the Forum.

# Question for the Forum

1. Adopt the vendor-neutral control-plane pattern described in the [recommendation](/assessments/agent-platform-recommendation-2026-10.md)?
2. Select **Option A** (Microsoft Foundry, Australia East) or **Option B** (AWS Bedrock AgentCore, Sydney) as the primary runtime, after a one-to-two-week proof of concept against gates G1–G6?

# Evidence needed before deciding

The 12 Oct desk research could not establish any of these:[^platform-report]

1. **Identity estate.** Is RSGx on Microsoft 365/Entra? That largely decides Option A.
2. **Australian-region facts, in writing from the vendors:**
   - AgentCore: where Memory and natural-language Policy route requests from Sydney (Australia only, or wider Asia Pacific);
   - Bedrock: whether the IRAP scope's exclusion of "Amazon Bedrock Marketplace" covers Claude, which is billed through AWS Marketplace;
   - Foundry: the Australia East model list by deployment type, and minimum PTU sizes for the models RSGx would use.
3. **Model policy for personal information.** Are GPT-family models acceptable for personal-information workloads? Foundry cannot process any Claude model in Australia.
4. **APP 8 position.** Counsel's view on whether sending prompts to a model endpoint outside Australia is a cross-border disclosure.
5. **ContextForge security review.** Its earlier releases were labelled alpha.
6. **Pricing and UI cost.** List prices are now recorded in the report; vendor quotes are still needed. The [UI gap](/assessments/agent-platform-ui-gap.md) cost for Option B needs estimating.

# Dependencies

- **Blocked by:** nothing. The Forum can adopt the pattern now and defer the runtime choice until the evidence arrives.
- **Gates:** L3 pilots, which are also gated by blocker [PR-17](/open-questions/pr-17-iso-27001-baseline.md); and real data for the [Forum governance dashboard](/prototypes/forum-governance-dashboard.md).

# Shelf life

Open-source facts in the evidence must be re-verified by 12 Dec 2026, and hyperscaler prices, regions and GA status by 12 Jan 2027. All vendor claims must be re-verified again at contract signature.

[^platform-report]: Agent platform report, 12 Oct 2026 (mirrored)
[^prior-report]: Agent platform report, 28 Sep 2026 (mirrored; superseded)
