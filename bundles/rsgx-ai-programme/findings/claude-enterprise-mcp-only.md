---
type: Finding
title: "Claude Enterprise speaks MCP only; it has no native A2A"
description: "As at 24 Sep 2026, Claude joins an A2A mesh only through another stack or an A2A-to-MCP bridge. This is a finding of absence, so it can change quickly."
tags: [agent-platform, claude-enterprise, a2a, mcp, time-sensitive]
status: draft
generated: { by: claude/claude-opus-5-5, at: 2026-09-30T02:00:00Z }
stale_after: 2026-12-31T00:00:00Z
sources:
  - id: platform-report
    resource: /references/agent-platform-report-2026-09-28.md
    title: Agent platform report, 28 Sep 2026 (mirrored)
  - id: claude-release-notes
    resource: https://platform.claude.com/docs/en/release-notes/overview.md
    title: Claude Platform release notes (checked to 24 Sep 2026)
  - id: claude-multi-agent
    resource: https://platform.claude.com/docs/en/managed-agents/multi-agent
    title: Claude Managed Agents — multi-agent sessions
  - id: contextforge-a2a
    resource: https://ibm.github.io/mcp-context-forge/using/agents/a2a/
    title: ContextForge — A2A integration
---

# Finding

- **No native A2A.** Anthropic's documentation and release notes, checked to 24 Sep 2026, show MCP connectors, Agent Skills, plugins and a proprietary multi-agent coordinator in Claude Managed Agents. None of these is A2A.[^claude-release-notes]
- **Limited multi-agent coordinator.** The Managed Agents coordinator allows one delegation level and 1–20 agents sharing a sandbox, as reported on 28 Sep.[^claude-multi-agent] It suits contained tasks. It is not a cross-platform mesh.
- **Routes for Claude into an A2A mesh:**
  - Claude models hosted inside Microsoft Foundry/Copilot Studio, Google's Agent Platform or Amazon Bedrock;
  - the Claude Agent SDK paired with an A2A server wrapper;
  - a gateway that exposes A2A agents as MCP tools, such as IBM ContextForge.[^contextforge-a2a][^platform-report]

# Relevance to RSGx

This is the largest single architectural constraint on the agent platform. It is why the [recommendation](/assessments/agent-platform-recommendation.md) keeps Claude Enterprise as the L1–L2 workspace and bridges it into the mesh through MCP.

It does not change the data-retention position recorded in [Anthropic compliance and retention](/findings/anthropic-compliance-and-retention.md). That finding stands on its own.

# Shelf life

This is a finding of absence, and Anthropic is an AAIF member, so it could change within months. Its re-verification date (31 Dec 2026) is deliberately earlier than the March 2027 date used for the platform report as a whole.

[^platform-report]: Agent platform report, 28 Sep 2026 (mirrored)
[^claude-release-notes]: Claude Platform release notes (checked to 24 Sep 2026)
[^claude-multi-agent]: Claude Managed Agents — multi-agent sessions
[^contextforge-a2a]: ContextForge — A2A integration
