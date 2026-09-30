---
type: Assessment
title: "Agent platform: build a vendor-neutral control plane, pick one runtime [P]"
description: "Claude's 28 Sep recommendation: agentgateway plus registry, fronting Microsoft Foundry or AWS Bedrock AgentCore (Malaysia), with Claude Enterprise kept as the L1–L2 workspace."
tags: [agent-platform, a2a, mcp, architecture, claude-view, time-sensitive]
status: draft
provenance: P
generated: { by: claude/claude-opus-5-5, at: 2026-09-30T02:00:00Z }
stale_after: 2027-03-01T00:00:00Z
sources:
  - id: platform-report
    resource: /references/agent-platform-report-2026-09-28.md
    title: Agent platform report, 28 Sep 2026 (mirrored)
  - id: s-0928
    resource: https://claude.ai/chat/c255f039-58a0-40b4-885a-63f1ede65e23
    title: Session 2026-09-28 — Agent platforms and A2A
---

> **This is Claude's recommendation, received without recorded objection. It is not a decision.** The Forum selection is tracked in [agent platform selection](/open-questions/agent-platform-selection.md).

# Recommendation

The recommendation comes from the 28 Sep report.[^platform-report] The owner confirmed the scope as organisation-wide, all 16 functional units, open to open-source and commercial options.[^s-0928]

1. **Don't buy an "A2A platform".** Build a thin control plane that RSGx owns and that stays portable:
   - an A2A/MCP gateway (**agentgateway**, Linux Foundation);
   - an agent and tool registry;
   - enterprise identity;
   - OpenTelemetry tracing.
   Add **IBM ContextForge** as the bridge that exposes A2A agents to Claude as MCP tools, but only after a security review.
2. **Pick one runtime behind it:**
   - **Option A: Microsoft Foundry Agent Service + Copilot Studio + Microsoft Agent Framework**, if RSGx's estate runs on Microsoft 365/Entra;
   - **Option B: AWS Bedrock AgentCore in Asia Pacific (Malaysia)**, if in-country hosting and model neutrality matter most.
   - **Google Gemini Enterprise** is a watch option. Malaysian in-country residency is unconfirmed.
3. **Keep Claude Enterprise as the L1–L2 knowledge-work surface**, connected through MCP. It has [no native A2A](/findings/claude-enterprise-mcp-only.md).
4. **Integration rule: MCP inward, A2A sideways.** Treat SaaS agents (ServiceNow, SAP Joule, Salesforce, Rovo) as registered A2A peers. None of them should be the hub.

# Challenges to the report (Claude, on review 30 Sep)

- **Vocabulary conflict.** The report's phased plan is labelled "H1 Enablement (Q4 2026 – Q1 2027)", "H2 Automation (2027 H1)" and "H3 Reinvention (2027 H2)". That is **time-bound horizon language**, which the programme has retired. Horizons are held **per function** ([decision](/decisions/mckinsey-three-horizons-full-replacement.md)), and H-numbering is banned vocabulary. Read those as Phase 1–3 of the platform rollout, and fix the wording before any Forum use.
- **Rung names.** The report invented L2/L3 descriptions and asked for them to be aligned with Forum definitions. Use the rung definitions in the [domain model](/specs/domain-model-v0-3.md) instead.
- **UI gap understated.** The report understated the cost and adoption risk of the missing end-user and governance interfaces, especially for Option B ([assessment](/assessments/agent-platform-ui-gap.md)).
- **Nothing priced.** No pricing was verified, and several adoption figures are self-reported by vendors or foundations.

# Dependencies

L3 cross-functional pilots rely on logging, monitoring and cloud-service controls from the ISMS baseline. They are therefore gated by blocker [PR-17](/open-questions/pr-17-iso-27001-baseline.md) whichever runtime is chosen.

[^platform-report]: Agent platform report, 28 Sep 2026 (mirrored)
[^s-0928]: Session 2026-09-28 — Agent platforms and A2A
