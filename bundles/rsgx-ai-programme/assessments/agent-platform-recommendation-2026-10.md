---
type: Assessment
title: "Agent platform: decide by layer, and choose Foundry (Australia East) or AgentCore (Sydney) by proof of concept [P]"
description: "Claude's 12 Oct recommendation, superseding the 28 Sep one. Keep the RSGx-owned control plane. Choose the runtime between Microsoft Foundry in Australia East and AWS Bedrock AgentCore in Sydney against six gates. Use Dify only for L1–L2 departmental work. Keep Paperclip to an isolated evaluation."
tags: [agent-platform, a2a, mcp, architecture, claude-view, time-sensitive, australia, residency]
status: draft
provenance: P
generated: { by: claude/claude-opus-5-5, at: 2026-10-12T02:40:00Z }
stale_after: 2026-12-12T00:00:00Z
sources:
  - id: platform-report
    resource: /references/agent-platform-report-2026-10-12.md
    title: Agent platform report, 12 Oct 2026 (mirrored)
  - id: prior-recommendation
    resource: /assessments/agent-platform-recommendation.md
    title: Agent platform recommendation, 28 Sep 2026 (superseded)
  - id: s-1012
    resource: https://claude.ai/code/session_01UNvDLfsAuXMiT9kpdm7JP6
    title: Session 2026-10-12 — Paperclip, Dify, Microsoft Foundry and alternatives
---

> **This is Claude's recommendation. It is not a decision.** It has not been reviewed by the owner or put to the Forum, and a lack of objection does not change that. The Forum selection is tracked in [agent platform selection](/open-questions/agent-platform-selection.md).

# Recommendation

This recommendation comes from the 12 Oct report.[^platform-report] It replaces the 28 Sep recommendation,[^prior-recommendation] which the owner asked Claude to supersede after confirming in session that RSGx is Australian.[^s-1012] Australia is therefore the governing jurisdiction for residency and law. That confirmation still has to be recorded by the owner ([governing jurisdiction](/open-questions/governing-jurisdiction.md)).

The three products the owner asked about sit at different layers. Paperclip is an agent-company control plane. Dify is an LLM app and workflow builder. Microsoft Foundry is a hyperscaler model and agent platform. Decide each layer on its own terms:

1. **RSGx-owned control plane: keep the 28 Sep pattern.** That means a gateway (agentgateway), an agent and tool registry, enterprise identity and OpenTelemetry tracing, with "MCP inward, A2A sideways". Neither Paperclip nor Foundry's preview Control Plane substitutes for it. Every agent registers in the RSGx registry, including Dify apps and any agents Paperclip manages. The ContextForge security review remains open.
2. **Runtime: choose between two options by a one-to-two-week proof of concept** against gates G1–G6 (below):
   - **Option A: Microsoft Foundry Agent Service in Australia East**, with Microsoft Agent Framework. It is stronger if RSGx runs on Microsoft 365 and Entra and if GPT-family models are acceptable for personal-information workloads.
   - **Option B: AWS Bedrock AgentCore in Sydney**, with Agent Framework, LangGraph or Strands. It is stronger on Australian residency for current Claude models (the `au.` Sydney–Melbourne routing) and on deterministic tool-call policy. AgentCore holds an IRAP assessment at PROTECTED.
   - **Google's Agent Platform remains a watch item.** It fails Australian residency today. Re-assess it when it offers a Sydney runtime and Australian processing for Claude.
3. **Builder: Dify only for L1–L2 departmental solutions.** Self-host it in an Australian region with one workspace per instance, or buy Enterprise if several workspaces are needed. Its licence counts each workspace as a tenant. Test n8n (internal use only), Sim and Activepieces in the same proof of concept. Exclude Flowise, which was archived in August 2026. Confine Langflow to developer sandboxes.
4. **Agent-company orchestration: do not adopt Paperclip** for production, personal information or client data. As shipped it fails G3, because deleting an agent deletes its audit history, and G6, because it has no supported-version or response-time policy despite five Critical advisories. At most, allow an isolated evaluation on non-sensitive coding work, behind the compensating controls listed in the report. Re-assess it in April 2027.
5. **Workspace: unchanged.** Claude Enterprise stays the workspace for L1–L2 solutions, limited by data class, because Anthropic's first-party inference runs in `global` or `us` only.

# Evaluation gates (proposed)

A candidate that fails a gate is out unless the Forum funds a compensating control, with a named owner and a stated cost.[^platform-report]

| Gate | Pass test |
|---|---|
| G1 | A distinct, independently revocable identity for each agent |
| G2 | Enforced human approval before sensitive actions, with the approver and rationale logged |
| G3 | A central, exportable audit trail that cannot be deleted at source |
| G4 | An Australian processing path for storage *and* inference for personal information and client-confidential data, or a documented APP 8 analysis with an exception approved by the owner |
| G5 | A licence that permits the intended pattern, confirmed in writing |
| G6 | Credible security maintenance: a disclosure policy, fix times and a supported upgrade path |

The report adds a 100-point weighted rubric, with customisability at 35 points. Its desk scores are indicative only and must be replaced by proof-of-concept evidence.

# What changed from 28 Sep

- **Option B moved from Malaysia to Sydney.** The 28 Sep framing (Malaysian PDPA, Malaysia and Singapore regions) does not fit an Australian organisation. Parts of its Malaysian facts are also wrong: Foundry is not offered in Malaysia, and every current Claude and GPT model is reachable from AWS Malaysia only through global routing. **This changes the meaning of the A/B framing, so the owner must approve it before it goes to the Forum.**
- **Residency is now about inference, not hosting.** Agent data can be kept in Australia on both runtimes. Inference location for the exact models RSGx will use is the binding constraint.
- **Paperclip and Dify have been assessed.** Paperclip was not in the bundle before. Dify's licence terms, Enterprise-only governance features and advisory record are now documented.
- **List prices are now available** for Foundry, AgentCore, Dify Cloud and the SaaS suites. Vendor quotes are still needed.

# Challenges and caveats (Claude)

- **Desk evidence only.** No criterion has been tested in a proof of concept. The ranking of the two runtimes depends on two facts the bundle does not yet record: the identity estate, and whether GPT-family models are acceptable for personal information.
- **Bedrock IRAP scope is unclear for Claude.** The IRAP scope excludes "Amazon Bedrock Marketplace", yet Claude 5.5 on Bedrock is billed through AWS Marketplace. Resolve this before relying on IRAP for Claude on Bedrock.
- **AgentCore cross-region routing from Sydney is unverified** for Memory and natural-language Policy. Verify it before enabling them for personal information.
- **The ISM agent control IDs** come from a consultancy summary. Check them against the official ISM changes document before citing them to the Forum.
- **APP 8 is unresolved** for offshore model inference. Get counsel's view before go-live.

# Dependencies

- **Blocker PR-17** (the ISMS baseline) gates L3 cross-functional pilots whichever runtime is chosen ([PR-17](/open-questions/pr-17-iso-27001-baseline.md)). Nothing here brings L3 or L4 autonomy forward.
- The Privacy Act automated decision-making transparency duty commences on 10 Dec 2026. Decide which data classes may reach each runtime and Claude Enterprise before then.

[^platform-report]: Agent platform report, 12 Oct 2026 (mirrored)
[^prior-recommendation]: Agent platform recommendation, 28 Sep 2026 (superseded)
[^s-1012]: Session 2026-10-12 — Paperclip, Dify, Microsoft Foundry and alternatives
