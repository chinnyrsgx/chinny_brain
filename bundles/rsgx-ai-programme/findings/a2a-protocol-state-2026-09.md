---
type: Finding
title: "A2A is stable and neutrally governed, but young; adoption figures measure support, not production"
description: "A2A v1.0 shipped 12 Mar 2026 and joined MCP in the Linux Foundation's AAIF in Aug 2026. Registry and delegation-chain standards are still missing."
tags: [agent-platform, a2a, mcp, standards, time-sensitive]
status: draft
generated: { by: claude/claude-opus-5-5, at: 2026-09-30T02:00:00Z }
stale_after: 2027-03-01T00:00:00Z
sources:
  - id: platform-report
    resource: /references/agent-platform-report-2026-09-28.md
    title: Agent platform report, 28 Sep 2026 (mirrored)
  - id: a2a-v1
    resource: https://a2a-protocol.org/latest/blog/2026/03/12/a2a-protocol-ships-v10-production-ready-standard-for-agent-to-agent-communication/
    title: A2A Protocol ships v1.0
  - id: aaif-a2a
    resource: https://aaif.io/blog/a2a-joins-aaif
    title: A2A joins AAIF's open agentic stack
  - id: aaif-proposal
    resource: https://github.com/aaif/project-proposals/issues/37
    title: AAIF project proposal — Agent2Agent Protocol
  - id: lf-150
    resource: https://www.linuxfoundation.org/press/a2a-protocol-surpasses-150-organizations-lands-in-major-cloud-platforms-and-sees-enterprise-production-use-in-first-year
    title: Linux Foundation — A2A surpasses 150 organisations
  - id: mcp-2026-07-28
    resource: https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/
    title: The 2026-07-28 MCP specification
---

# Finding

- **Stable spec.** A2A v1.0 is the first stable specification, released 12 Mar 2026.[^a2a-v1] It adds signed Agent Cards, multi-tenancy, JSON-RPC/gRPC/REST bindings and modernised OAuth.
- **Neutral governance.** A2A joined MCP in the Linux Foundation's Agentic AI Foundation (AAIF) as a Growth Stage project in August 2026.[^aaif-a2a] IBM's ACP has merged into A2A.[^platform-report] Sources disagree on the exact date (17 or 27 Aug), so cite it as "August 2026".
- **Known gaps, stated by the maintainers:** no standard agent registry, no token down-scoping for delegation chains, and no per-skill schemas.[^aaif-proposal] Delegation authority is handled by OAuth token exchange and gateways, not by A2A itself.
- **Adoption is overstated.** Figures like "150+ organisations" measure endorsement, not verified production deployments.[^lf-150] Most "A2A support" means an endpoint on a vendor platform. Cross-vendor, multi-hop chains in production are rarely documented.[^platform-report]
- **MCP is the integration layer.** MCP remains the de facto agent-to-tool standard. Its 2026-07-28 revision is the largest since launch, with a stateless core, Tasks and a formal deprecation policy.[^mcp-2026-07-28]

# Relevance to RSGx

Use MCP for connecting agents to tools and data, and A2A for delegating across perimeters (functional unit, vendor, partner). Design around the missing registry and delegation-chain standards, not around the protocol. The consequences are in the [platform recommendation](/assessments/agent-platform-recommendation.md).

# Shelf life

Spec versions and adoption figures change monthly. Re-verify against primary sources by 1 Mar 2027 and before any contract signature.

[^platform-report]: Agent platform report, 28 Sep 2026 (mirrored)
[^a2a-v1]: A2A Protocol ships v1.0
[^aaif-a2a]: A2A joins AAIF's open agentic stack
[^aaif-proposal]: AAIF project proposal — Agent2Agent Protocol
[^lf-150]: Linux Foundation — A2A surpasses 150 organisations
[^mcp-2026-07-28]: The 2026-07-28 MCP specification
