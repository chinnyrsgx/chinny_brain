---
type: Assessment
title: "Agent platform UI gap: no vendor provides the Forum's governance view [P]"
description: "There are three interface types: workspace, builder and governance console. The hyperscaler runtimes differ sharply on the first, and no vendor fills the cross-runtime Forum dashboard."
tags: [agent-platform, ui, governance, forum, claude-view, time-sensitive]
status: draft
provenance: P
fidelity: "Compiled from the 28 Sep session summary, not the verbatim transcript. Verify specifics against the transcript before Forum use."
generated: { by: claude/claude-opus-5-5, at: 2026-09-30T02:00:00Z }
stale_after: 2027-03-01T00:00:00Z
sources:
  - id: s-0928
    resource: https://claude.ai/chat/c255f039-58a0-40b4-885a-63f1ede65e23
    title: Session 2026-09-28 — Agent platforms and A2A (follow-up on user-facing UI)
---

# Assessment

In the 28 Sep follow-up, the owner asked whether any platform has a user-facing UI. Claude separated three interface types:[^s-0928]

| Interface | Who uses it | Strongest options (as at 28 Sep) |
|---|---|---|
| **End-user workspace** | Staff working with agents day to day | Microsoft Copilot Studio; Google Gemini Enterprise. Claude Enterprise already covers the L1–L2 workspace. |
| **Builder** | People creating agents | Copilot Studio, Foundry, framework tooling |
| **Admin / governance console** | People approving and monitoring agents | Vendor consoles, each scoped to its own runtime only |

- **Option B has no workspace.** AWS AgentCore, agentgateway and ContextForge have no end-user UI at all. The 28 Sep report understated the cost and adoption risk this creates for Option B.
- **Unverified leads.** Self-hosted front-ends such as **LibreChat** and **Open WebUI** exist. They are leads only and haven't been evaluated.
- **No vendor fills the Forum's view.** Nothing on the market shows every registered agent, its owner, its autonomy level, its impact-assessment status and its incidents **across all runtimes**. Hence the [Forum governance dashboard](/prototypes/forum-governance-dashboard.md) prototype candidate.

# Why it matters

The Forum gates movement up the autonomy ladder. Without a cross-runtime view, it would be gating from vendor consoles that each show only part of the estate.

[^s-0928]: Session 2026-09-28 — Agent platforms and A2A (follow-up on user-facing UI)
