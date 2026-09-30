---
type: Reference
title: "A2A-aligned agent platforms for RSGx: state of play, options and recommendation (28 Sep 2026, mirrored)"
description: "Full text of Claude's 28 Sep research report on organisation-wide agent platforms and A2A, mirrored so findings and assessments can cite it."
tags: [agent-platform, a2a, mcp, reference, research, time-sensitive]
status: draft
provenance: P
generated: { by: claude/claude-opus-5-5, at: 2026-09-30T02:00:00Z }
stale_after: 2027-03-01T00:00:00Z
sources:
  - id: s-0928
    resource: https://claude.ai/chat/c255f039-58a0-40b4-885a-63f1ede65e23
    title: Session 2026-09-28 — Agent platforms and A2A (original artifact with inline citations)
---

> **Editor's notes (30 Sep).**
> 1. The mirrored text below is unedited, except that inline citation markers are removed. The original artifact in the source session carries the full citation set.[^s-0928]
> 2. **Vocabulary warning:** *Sequenced plan aligned to the Three Horizons* uses time-bound "H1/H2/H3" labels. The programme has retired that vocabulary; horizons are held per function. Read them as Phase 1–3 ([assessment](/assessments/agent-platform-recommendation.md)).
> 3. The recommendations are Claude's proposals, not decisions ([open question](/open-questions/agent-platform-selection.md)).

# Organisation-wide A2A-aligned agent platforms for RSGx (as at 28 September 2026)

RSGx should not buy an "A2A platform". It should build a thin, vendor-neutral agent control plane: an A2A/MCP gateway, an agent registry, enterprise identity, and OpenTelemetry-based observability. Behind that sit one hyperscaler agent runtime (Microsoft Foundry or AWS Bedrock AgentCore in the Malaysia region) and Claude Enterprise as a governed peer. A2A is now a stable, neutrally governed standard. The weak points are Claude's lack of native A2A support and immature registry and delegation-chain standards. Those, not the protocol, should shape the design.

## TL;DR

- **A2A is real but young.** A2A v1.0 (the first stable spec, 12 March 2026) added signed Agent Cards, multi-tenancy and gRPC/REST bindings. Since August 2026 A2A has sat alongside MCP in the Linux Foundation's Agentic AI Foundation (AAIF), and IBM's ACP has merged into it. Most real A2A use still happens inside large vendor platforms (Microsoft, Google, AWS, Salesforce, ServiceNow, SAP), not between independent vendors, and Anthropic's Claude Enterprise does not support A2A natively. It speaks MCP.
- **Recommended shortlist.** Three options: (1) Microsoft Foundry Agent Service + Copilot Studio + Microsoft Agent Framework if RSGx runs on Microsoft 365/Entra; (2) AWS Bedrock AgentCore in Asia Pacific (Malaysia) where in-country hosting and model neutrality matter most; (3) either one fronted by the open-source Linux Foundation **agentgateway** (with IBM ContextForge or the cloud's own registry). Keep Claude Enterprise as the L1–L2 workspace and bridge it into the agent mesh through MCP.
- **Governance fit.** Governance depends more on your own control plane than on the vendor. Vendor ISO/IEC 42001 certificates (AWS, Google Cloud, Microsoft, Anthropic) cover *their* AI management systems, not RSGx's. Your AIMS evidence comes from agent identity, registry-based approval, gateway policy, end-to-end tracing and human-in-the-loop controls, tied to the autonomy ladder. Pace each rung to the OWASP Agentic Top 10 threats (goal hijack, identity/privilege abuse, insecure inter-agent communication).

## Key Findings

1. **Protocol convergence has largely happened.** The Linux Foundation now holds MCP (agent-to-tool) and A2A (agent-to-agent) under one foundation, the AAIF. ACP has folded into A2A. AGNTCY (Cisco-led) is positioned as supporting infrastructure (discovery, identity, secure messaging, observability) rather than a rival wire protocol. ANP (decentralised identifiers, open-internet focus) is the main remaining alternative and has little enterprise traction. *Shelf life: stable for 12–18 months; recheck after AAIF's next governing-board cycle.*
2. **A2A's own maintainers say the spec is stable.** In the AAIF application, the roadmap is "stability", with "no significant or breaking changes on the horizon". Named gaps remain: registry standardisation, token down-scoping for delegation chains, and per-skill schemas. The Linux Foundation roadmap lists "consolidation of efforts for registry" and "security and deployment best practices" as future work. Neither exists yet.
3. **Adoption figures are support figures, not production figures.** "150+ organisations" and "22,000+ GitHub stars" (Linux Foundation, 9 April 2026) measure endorsement and developer interest. For comparison, the MCP maintainers' 2026-07-28 specification post reports "close to half-a-billion downloads a month" across MCP's Tier 1 SDKs, although other outlets cite about 97 million a month for the Python and TypeScript SDKs alone. MCP is the de facto integration layer. A2A is the emerging delegation layer.
4. **Claude Enterprise is an MCP-native island.** Anthropic's documentation and release notes, checked to 24 September 2026, show MCP connectors, Agent Skills, plugins and a proprietary multi-agent coordinator in Claude Managed Agents. There is no native A2A. Claude joins an A2A mesh only through other stacks: Claude models inside Microsoft Foundry/Copilot Studio, Google's Agent Platform or Amazon Bedrock, the Claude Agent SDK paired with an A2A SDK, or a gateway that exposes A2A agents as MCP tools.
5. **The hyperscalers are the most mature A2A hosts.** Microsoft Foundry Agent Service lists A2A v1.0 as generally available, with Entra Agent ID for each agent. Copilot Studio lists A2A connections as GA. AWS Bedrock AgentCore Runtime has supported A2A since GA (October 2025) and is available in Asia Pacific (Malaysia) since June 2026. Google's Gemini Enterprise Agent Platform (formerly Vertex AI) and ADK have native A2A.
6. **The open-source control-plane layer is maturing quickly.** agentgateway (Linux Foundation, Rust, v1.0.0 in March 2026) and IBM ContextForge (v1.0.6, July 2026) are credible gateway/registry options. Low-code builders (Dify, n8n, Flowise) remain weak on A2A.
7. **No engineering or infrastructure firm has a documented A2A deployment.** KPMG, PwC and Deloitte have organisation-wide multi-agent platforms. In RSGx's own sector (WSP, Worley) the documented deployments are copilot and retrieval-heavy agentic assistants. That is itself a signal: RSGx would be early, and should plan for it.

## Details

### 1. A2A protocol: current state (as at September 2026)

**Timeline and governance** *(confirmed from primary sources unless noted)*

| Date | Event |
|---|---|
| 9 Apr 2025 | Google announces A2A with 50+ technology partners |
| 23 Jun 2025 | Google donates A2A to the Linux Foundation. Founding members: AWS, Cisco, Google, Microsoft, Salesforce, SAP, ServiceNow |
| 29 Jul 2025 | Linux Foundation welcomes AGNTCY (Cisco, Dell, Google Cloud, Oracle, Red Hat as formative members) |
| Late Aug 2025 | IBM's ACP formally merges into A2A. IBM (Kate Blair) joins the A2A Technical Steering Committee alongside Google, Microsoft, AWS, Cisco, Salesforce, ServiceNow and SAP |
| 9 Dec 2025 | Linux Foundation forms the Agentic AI Foundation (AAIF) with MCP, goose and AGENTS.md. Platinum members: AWS, Anthropic, Block, Bloomberg, Cloudflare, Google, Microsoft, OpenAI |
| 12 Mar 2026 | A2A v1.0, the first stable specification |
| 9 Apr 2026 | One-year mark: 150+ supporting organisations, 22,000+ stars, five SDKs (Python, JavaScript, Java, Go, .NET) |
| 17 Aug 2026 | A2A accepted as an AAIF "Growth Stage" project. AAIF reports 250+ members |

*Conflicts noted:* secondary sources variously date v1.0 to January, 12 March or 9 April 2026. The A2A project's own blog says 12 March, and 9 April was the anniversary press release. Dates for joining the AAIF range from 17 to 27 August 2026. The AAIF and Axios say 17 August. The A2A project blog post is dated 27 August.

**What v1.0 delivered**
- **Signed Agent Cards**: JWS signatures with JSON canonicalisation, so a client can verify that a card was issued by the domain owner. This is the main defence against card forgery.
- **Multi-tenancy**: one endpoint can host many agents, with native tenant scoping in gRPC.
- **Multi-protocol bindings**: JSON-RPC 2.0, gRPC and HTTP+JSON/REST, with formal equivalence guarantees and version negotiation through an `A2A-Version` header.
- **Security modernisation**: mutual TLS declarations, the OAuth 2.0 Device Code flow and PKCE. The deprecated implicit and password flows are removed.
- **Delivery options**: polling, streaming (SSE) or webhooks for long-running tasks.

**How A2A relates to MCP and adjacent efforts**
- **MCP (agent-to-tool, "vertical")** connects one agent to tools and data. The **2026-07-28** MCP specification is the largest revision since launch. It brings a stateless core (the initialise handshake and session IDs are removed), an extensions framework, Tasks, MCP Apps, authorisation aligned more closely with OAuth/OIDC, and a formal deprecation policy (at least 12 months' notice). Roots, Sampling, Logging, Dynamic Client Registration and legacy HTTP+SSE are deprecated. *Shelf life: next MCP revision likely within 6–9 months.*
- **A2A (agent-to-agent, "horizontal")** covers delegation between opaque agents across team, vendor or certification perimeters. The AAIF proposal notes "discussion regarding MCP officially supporting A2A tasks as an extension to encourage 'single gateway' implementations". Treat that as a possible future convergence point, not a commitment.
- **ACP** has merged into A2A and is no longer developed separately. The BeeAI platform now runs on A2A.
- **AGNTCY** provides complementary infrastructure (directory, identity, SLIM secure messaging with MLS encryption, observability) supporting both MCP and A2A. It is useful for design ideas. RSGx does not need it at present.
- **ANP** uses W3C decentralised identifiers and targets the open internet. It is not relevant to an internal enterprise mesh.
- **A2A extensions**: AP2 (agent payments; Google Cloud cited more than 60 supporting organisations, including Mastercard, American Express, PayPal and Salesforce, at its September 2025 launch), A2UI/AG-UI (agent-to-user interfaces) and AP3 (privacy-preserving computation). AP2 is not relevant to RSGx. A2UI/AG-UI may matter for front-ends.

**Critical view: where A2A adoption is overstated**
- The "production deployments across multiple industries" claim comes from the project's own press release and names only sectors (supply chain, financial services, insurance, IT operations), not verifiable deployments.
- Most "A2A support" is **inbound/outbound endpoints on vendor platforms**. Examples include an A2A endpoint on a Foundry agent or a Joule extensibility hook. Truly cross-vendor, multi-hop A2A chains in production are rarely documented.
- There is still no standard registry. Each vendor offers its own: Entra Agent Registry, Google's agent registry, AgentCore Gateway, ServiceNow AI Agent Fabric.
- Delegation-chain authority (who authorised which downstream action, with what scope) is handled by OAuth token exchange patterns and gateways, **not by A2A itself**.

### 2. Candidate platforms compared

Legend: **Native** = first-party, documented support; **Adapter** = plugin, community or bridge; **Unclear** = not confirmed in this research. *Shelf life for all feature claims: 6 months (review March 2027).*

#### 2a. Open-source frameworks and orchestration

| Framework | Licence | Self-host | A2A | MCP | Model-agnostic | Enterprise-relevant notes | Lock-in risk |
|---|---|---|---|---|---|---|---|
| **Microsoft Agent Framework** (successor to Semantic Kernel + AutoGen) | MIT | Yes | Native (Python and .NET). At 1.0 GA (3 Apr 2026) Microsoft said "A2A 1.0 support coming soon"; Foundry hosting now lists A2A v1.0 GA | Native | Yes: Foundry, Azure OpenAI, OpenAI, Anthropic, Bedrock, Ollama | Stable APIs with long-term support; workflow checkpointing; human approval nodes; migration tools from SK/AutoGen | Low (code), medium if paired with Foundry |
| **Google ADK** | Apache 2.0 | Yes | Native (`RemoteA2aAgent`, `to_a2a()`) | Native | Yes (Claude and others via Model Garden/LiteLLM) | Strongest A2A lineage; best on Google's Agent Runtime | Low (code), medium on Google Cloud |
| **LangGraph / LangSmith Deployment** | MIT (LangGraph); LangSmith is commercial | Yes (LangSmith self-host is commercial) | Native on deployed agents: `/a2a/{assistant_id}` with auto-generated Agent Card | Native | Yes | Graph state, interrupts for human-in-the-loop, distributed tracing across A2A calls | Medium (LangSmith for operations) |
| **CrewAI + AMP** | MIT (core); AMP is commercial | Yes | Native on AMP: OIDC/OAuth2/mTLS, REST/JSON-RPC/gRPC, signed webhooks | Native | Yes | Easiest to start; thinner on checkpointing and observability than MAF/LangGraph (per independent commentary) | Medium |
| **AWS Strands Agents** | Apache 2.0 | Yes | Native (wraps agents as A2A services) | Native | Yes | Pairs with AgentCore | Low–medium |
| **AG2 (formerly AutoGen community fork)** | Apache 2.0 | Yes | Native | Yes | Yes | Research-oriented | Low |
| **IBM BeeAI Framework** | Apache 2.0 | Yes | Native adapters (`A2AServer`, `A2AAgent`) | Yes | Yes | Became the ACP→A2A reference; small community | Low |
| **Pydantic AI** | MIT | Yes | Native via FastA2A (`.to_a2a()`) | Yes | Yes | Good for typed, well-tested agents | Low |
| **NVIDIA NeMo Agent Toolkit** | Apache 2.0 | Yes | Native server, client and auth (v1.6, April 2026) | Yes | Yes | Integrates ADK, LangChain, CrewAI, SK | Low |
| **OpenAI Agents SDK / Claude Agent SDK** | MIT | Yes | Adapter (call A2A peers as tools; pair with an A2A SDK) | Native | Mostly vendor-first | Claude Agent SDK is Anthropic's harness; no native A2A server | Medium |
| **Dify** | Dify licence (Apache 2.0-based with extra conditions; check multi-tenant terms) | Yes | Adapter: community Nacos "A2A Server" plugin (v0.0.4) | Yes | Yes | Strong visual RAG/app builder; A2A plugin immature | Medium |
| **n8n** | Sustainable Use Licence (fair-code, not OSI open source) | Yes | Unclear/adapter; no native A2A confirmed | Yes | Yes | Excellent for operations automation in which AI is one step | Medium (licence terms) |
| **Flowise** | Apache 2.0 | Yes | Unclear; no native A2A confirmed | Yes | Yes | Prototyping | Low |
| **Letta** | Apache 2.0 | Yes | Unclear | Yes | Yes | Stateful-memory agents; niche | Low |

**Reading the table.** For code-first agents that must be governed across 16 functional units, **Microsoft Agent Framework** and **LangGraph** are the most production-ready. **Google ADK** is the A2A reference if RSGx leans towards Google Cloud. The low-code tools (Dify, n8n, Flowise) suit L1–L2 departmental automation. They should not form the A2A backbone.

#### 2b. Open-source registries, gateways and control planes

| Component | Licence/stewardship | A2A | MCP | What it gives RSGx | Maturity |
|---|---|---|---|---|---|
| **agentgateway** | Linux Foundation (donated by Solo.io); contributors include AWS, Cisco, Huawei, IBM, Microsoft, Red Hat | Native A2A gateway (capability discovery, task routing) | Native MCP gateway (tool federation, OAuth) | Single policy enforcement point for agent→LLM, agent→tool and agent→agent traffic; LLM routing with budget/spend controls; Kubernetes Gateway API | v1.0.0 (March 2026). Best neutral choice |
| **IBM ContextForge** | Open source (IBM) | Registers A2A agents and **exposes them as MCP tools** | Native MCP gateway/registry | Useful bridge for Claude Enterprise (MCP-only) to reach A2A agents; OpenTelemetry; admin UI; air-gapped support; OAuth RFC 8693 token exchange and HashiCorp Vault per-user credentials (v1.0.6, 22 Jul 2026) | Earlier releases were explicitly "alpha/early beta"; now 1.0.x. Security-review before production |
| **Envoy AI Gateway** | CNCF | Native protocol deframing | Native | Zero-trust policy at the network layer, suited to Envoy/Istio users | Growing |
| **LiteLLM** | Open-core (BerriAI) | `/a2a` endpoint with providers for LangGraph, Vertex, Foundry, AgentCore | Yes | Unified LLM + MCP + A2A proxy; spend tracking | Widely used; the open-core boundary matters for SSO/audit |
| **Solace Agent Mesh** | Open source + commercial | A2A over an event broker | Yes | Asynchronous, event-driven topologies | Niche |
| **AGNTCY Directory/Identity/SLIM** | Linux Foundation | Supports | Supports | Reference designs for identity and secure messaging | Early |

#### 2c. Commercial / enterprise platforms

| Platform | A2A | MCP | Claude / multi-model | Self-host / residency | Enterprise controls | Lock-in |
|---|---|---|---|---|---|---|
| **Microsoft Foundry Agent Service** | Native. A2A v1.0 GA (v0.3 preview), as both incoming A2A endpoints and an outbound A2A Tool; hosted agents reach A2A via an MCP "Toolbox" (two-hop) | Native (MCP tool GA; Toolbox) | Yes: Claude via Foundry; any framework (MAF, LangGraph, custom) | Azure regions; Malaysia West exists (confirm per-feature availability) | Entra Agent ID for each agent, RBAC, OBO flows, Entra Agent Registry, XPIA/prompt-injection guardrails, private networking | Medium–high |
| **Microsoft Copilot Studio** | Native. A2A connections listed as GA | Yes | Claude Sonnet 4.5/4.6 and Opus GA globally (excluding GCC); Anthropic is off by default in EU/EFTA/UK, where it runs as a Microsoft subprocessor outside the EU Data Boundary | SaaS (Power Platform geographies) | Purview audit, DLP, environment controls; computer-use agents GA (May 2026) with human-in-the-loop review | High |
| **AWS Bedrock AgentCore** | Native in Runtime | Native (AgentCore Gateway) | Yes: "any framework, any model", including Claude on Bedrock and non-Bedrock models | **Available in Asia Pacific (Malaysia) since June 2026**; VPC/PrivateLink | AgentCore Identity, Policy, Observability (OTEL/CloudWatch), Evaluations, 8-hour session isolation | Medium |
| **Google Gemini Enterprise + Agent Platform** (formerly Agentspace + Vertex AI) | Native (A2A originator); ADK | Managed MCP servers (GA) | 200+ models, including Claude Opus/Sonnet/Haiku | Google says endpoints "don't guarantee data residency"; the global endpoint does not support residency. Malaysia in-country options **not confirmed** | Unified IAM, request/response logging for Claude, partner-agent ecosystem | Medium–high |
| **Salesforce Agentforce + MuleSoft Agent Fabric** | Native | Yes | Multi-model within Salesforce | SaaS | Trust layer, CRM-centric | High |
| **ServiceNow AI Agent Fabric** | Native (per A2A project) | Yes | Multi-model | SaaS | Strong ITSM/workflow governance | High |
| **SAP Joule** | A2A as the primary extensibility layer (plug in LangGraph/CrewAI agents) | Yes | SAP-managed | SaaS | ERP-context controls | High |
| **IBM watsonx Orchestrate** | IBM is on the A2A TSC; specific feature level **not verified here** | Via ContextForge lineage | Multi-model | Hybrid/on-premises options | Governance heritage (watsonx.governance) | Medium |
| **Atlassian Rovo, UiPath, Box, Workday** | A2A participants | Varies | Varies | SaaS | Domain-specific | High |

**Interpretation.** SaaS agent platforms (Agentforce, ServiceNow, SAP Joule, Rovo) should be **A2A peers**, meaning specialist agents that RSGx's orchestration layer calls. They should not be the organisation's hub. Making one of them the hub ties the whole programme to that system-of-record vendor.

### 3. Governance and assurance fit (ISO/IEC 42001 and ISO/IEC 27001:2022)

**Vendor certifications (confirmed):**
- AWS: accredited ISO/IEC 42001 certification on 25 Nov 2024, covering Bedrock, Q Business, Textract and Transcribe (Schellman). First surveillance audit in Nov 2025 had no findings.
- Google Cloud: 18 Dec 2024.
- Anthropic: 13 Jan 2025 (Schellman, ANAB-accredited).
- Microsoft: Azure AI Foundry Models and Security Copilot in July 2025, later extended to Copilot Studio, M365 Copilot and Foundry according to the Service Trust Portal.
- ISO/IEC 42006:2025 now sets requirements for the certification bodies themselves.

**What this means:** these certificates support RSGx's supplier assurance (42001 Annex A.10 third-party relationships; 27001:2022 controls 5.19–5.23, including 5.23 cloud services). They **do not** extend to RSGx's own agents, prompts, tool permissions or delegation chains. Those fall inside RSGx's AIMS scope.

**Control mapping for the agent platform**

| RSGx requirement | ISO anchor (indicative) | Platform mechanism |
|---|---|---|
| Every agent has an identity and an owner | 27001 5.16 identity management, 5.17 authentication information; 42001 A.3 roles/responsibilities | Entra Agent ID / AgentCore Identity / workload identity (SPIFFE); registry entry with a named accountable owner |
| Least privilege and "least agency" | 27001 5.15, 5.18, 8.2, 8.5 | Gateway policy (agentgateway/ContextForge), OAuth scopes, token exchange (RFC 8693) for down-scoped delegation; OWASP "Least Agency" principle |
| Tamper-evident audit trail across agent hops | 27001 8.15 logging, 8.16 monitoring; 42001 A.6.2.8 event logs | OpenTelemetry trace propagation through A2A task IDs; central SIEM; Purview/CloudWatch; retain Agent Card versions |
| Approved-agent inventory | 42001 A.4 resources, A.6 lifecycle; 27001 5.9 asset inventory | Registry as the single source of truth; signed Agent Cards; change control (27001 8.32) |
| Impact assessment before a rung promotion | 42001 6.1.4 / A.5 impact assessment | Forum gate: an autonomy-level change requires a documented AI system impact assessment and evaluation evidence |
| Human oversight | 42001 A.9 use of AI systems | HITL approval nodes; A2A `input-required` task state; MCP elicitation |
| Data residency and transfer | 27001 5.34 PII; Malaysia PDPA (as amended 2024) cross-border provisions | Pin runtimes to Malaysia/Singapore regions; avoid global endpoints for sensitive workloads; check cross-region inference behaviour |
| Supplier monitoring | 42001 A.10; 27001 5.22 | Track vendor certificate scopes and subprocessors (e.g. Anthropic as a Microsoft subprocessor) |

**Data residency for Malaysia/APAC** *(shelf life: 3–6 months; verify at contract time)*
- **AWS**: Bedrock has been available in Asia Pacific (Malaysia) since Sept 2025 and AgentCore since June 2026. This is the strongest confirmed in-country option. *Caveat:* AgentCore features vary by region. At an earlier documentation snapshot, Singapore lacked Evaluations and Policy. AgentCore Memory, Policy and Evaluations may use cross-region inference, which can move prompts and outputs outside the primary region within a geography (or globally for some regions). Confirm the Malaysia feature list and routing in writing.
- **Microsoft**: an Azure Malaysia West region exists. Per-feature availability of Foundry Agent Service and the in-region location of Claude model processing are **not confirmed**. Anthropic models in Microsoft services run under subprocessor terms.
- **Google**: Gemini Enterprise offers in-country data residency only in listed regions, with limitations. Malaysia was not confirmed in this research. Google's own documentation warns that endpoints do not guarantee residency or in-region ML processing.
- **Claude Enterprise direct**: processing is Anthropic-hosted. Treat it as a cross-border transfer and put controls on what data classes may enter it.

**A2A and multi-agent security risks and mitigations**

| Threat | Source | Mitigation on RSGx's platform |
|---|---|---|
| **Agent Card spoofing / typosquatting**: forged card redirects tasks to a rogue server | arXiv 2504.16902 (MAESTRO analysis) | Require **signed Agent Cards** (v1.0); allow-list cards through the registry; never auto-discover from the open internet |
| **Agent Card content as an injection vector**: malicious descriptions steer the calling LLM | arXiv 2504.16902 | Treat card text as untrusted input; sanitise; pin card versions |
| **Cross-agent prompt injection**: poisoned artefacts propagate through the chain | arXiv 2506.23260; OWASP ASI01 Agent Goal Hijack | Content inspection at the gateway; XPIA guardrails (Foundry); separate "thinking" and "acting" agents; no auto-execution on untrusted outputs |
| **Task replay / duplicate actions** | arXiv 2504.16902 | Idempotency keys, nonce/timestamp checks, short-lived tokens |
| **Over-broad scopes and long token lifetimes; privilege escalation in delegation** | arXiv 2505.12490; OWASP ASI03 Identity and Privilege Abuse | Token exchange with down-scoping at each hop; maximum delegation depth; per-hop authorisation logs |
| **Insecure inter-agent communication** | OWASP ASI07 | mTLS inside the mesh, OAuth 2.0 with PKCE, no API-key-only agents |
| **Tool misuse via MCP** (and new MCP 2026-07-28 attack surfaces, e.g. unbound handles) | OWASP ASI02; Backslash Security analysis | MCP gateway allow-lists; bind handles to the user; expiry; human approval for write actions |
| **Unverified MCP servers / agents in public catalogues** | arXiv 2602.11327 | Internal-only catalogue; supply-chain review before registration |

The OWASP Top 10 for Agentic Applications 2026 (published 9 Dec 2025, ASI01–ASI10) should be the Forum's reference threat taxonomy for rung-promotion reviews.

### 4. Mapping to the RSGx autonomy ladder (L1 Assist → L4 Directed)

RSGx's intermediate rung names are internal. Below, L2 means "executes bounded tasks with approval" and L3 means "acts autonomously within guardrails, with exception escalation". Adjust to the Forum's definitions.

| Rung | Typical RSGx use | A2A needed? | Suitable platforms | Minimum controls (gate to next rung) |
|---|---|---|---|---|
| **L1 Assist** | Drafting, summarising specs, bid-document Q&A | No | Claude Enterprise; M365 Copilot; Gemini Enterprise | Data-class rules, usage logging, acceptable-use training; AIMS inventory entry |
| **L2 (bounded execution with approval)** | Read-only MCP tools (document management, project controls), draft RFIs for human sending | Rarely; MCP is enough | Claude Enterprise + governed MCP connectors via gateway; Copilot Studio; Dify/n8n for departmental flows | Every write action needs explicit approval (MCP elicitation / HITL node); tool allow-lists; per-agent identity |
| **L3 (supervised autonomy)** | Multi-step workflows across functions, e.g. a commercial agent delegating to a scheduling agent in another unit | **Yes**: this is where A2A earns its place | Foundry Agent Service / AgentCore Runtime / ADK/LangGraph/MAF, behind agentgateway | Signed cards, registry approval, delegation-depth limits, end-to-end tracing, evaluation suites, kill-switch; impact assessment signed off by the Forum |
| **L4 Directed** | Agents directed by goals, with humans setting objectives and reviewing outcomes (e.g. automated progress-claim assembly across partner systems) | Yes, possibly across organisations | Same as L3 plus cross-organisation A2A with mTLS and signed cards | Continuous monitoring, anomaly detection, AgentCore Policy / Foundry guardrails, periodic red-teaming, rollback plans; only after ISO/IEC 42001 certification milestone and ISMS controls are evidenced |

**Which platforms best support progressive autonomy:**
- **Microsoft Agent Framework** (workflow approval nodes, checkpointing), **LangGraph** (interrupts/resume) and **AgentCore** (Policy + Evaluations) offer the most explicit technical levers for raising autonomy gradually.
- **Copilot Studio** now includes configurable human-in-the-loop review for computer-use agents.
- **Claude Managed Agents** has permission policies (including an `auto` policy for agent/MCP tool calls, September 2026). Its multi-agent coordinator is limited to a single delegation level and 1–20 agents sharing one sandbox. It suits contained L2–L3 tasks. It is not a cross-platform mesh.

### 5. Reference architecture

```
┌──────────────────────────────────────────────────────────────────────┐
│ Experience layer: Claude Enterprise │ M365 Copilot/Teams │ Web apps   │
└───────────────▲───────────────────────────────▲──────────────────────┘
                │ MCP                           │ A2A / Activity
┌───────────────┴───────────────────────────────┴──────────────────────┐
│ CONTROL PLANE (RSGx-owned, vendor-neutral)                            │
│  • Agent & tool registry (approved Agent Cards, MCP servers, owners,   │
│    autonomy level, impact-assessment ref)                             │
│  • Gateway: agentgateway (A2A + MCP + LLM routing) / ContextForge     │
│    bridge (A2A agents → MCP tools for Claude)                         │
│  • Identity: Entra ID / IdP + workload/agent IDs, OAuth token exchange│
│  • Policy & guardrails: scopes, delegation depth, HITL rules, DLP     │
│  • Observability: OpenTelemetry → SIEM + evaluation store             │
└───────────────▲───────────────────────────────▲──────────────────────┘
                │ A2A                           │ A2A
┌───────────────┴────────────┐   ┌──────────────┴───────────────────────┐
│ Agent runtimes             │   │ SaaS peer agents                     │
│  Foundry Agent Service or  │   │  ServiceNow, SAP Joule, Salesforce,  │
│  Bedrock AgentCore (MY)    │   │  Atlassian Rovo, partner agents      │
│  Frameworks: MAF/LangGraph │   └──────────────────────────────────────┘
└───────────────▲────────────┘
                │ MCP
┌───────────────┴──────────────────────────────────────────────────────┐
│ Tools & data: EDMS, project controls, ERP, GIS/BIM, proprietary IP    │
│ (Pillar 1: Proprietary Intelligence)                                  │
└──────────────────────────────────────────────────────────────────────┘
```

Design principles:
1. **The control plane is owned by RSGx and is portable.** Registry records and gateway policies should be exportable, so the runtime vendor can be changed.
2. **MCP inward, A2A sideways.** Use MCP for tools and data. Use A2A only when delegating across perimeters (functional unit, vendor, partner).
3. **Claude as a governed peer.** Claude Enterprise reaches the mesh through MCP servers registered in the gateway. For A2A-exposed Claude agents, host them on Foundry/AgentCore/Agent Platform, or with the Claude Agent SDK plus an A2A server wrapper.
4. **Evidence by default.** Every hop emits a trace and every promotion has a Forum record, so ISO/IEC 42001 audit evidence is produced as a by-product.

### 6. Real-world case studies (closest analogues)

| Organisation | Platform | A2A/MCP | Scale / outcomes | Evidence quality |
|---|---|---|---|---|
| **KPMG Workbench** (June 2025) | Built on Microsoft Azure AI Foundry; "interoperable, agent to agent communications"; multi-model | Agent-to-agent capability claimed; A2A protocol not named (KPMG was an A2A launch partner) | 50 agents live, "nearly a thousand" in development; the firm's "single AI platform" for tax, advisory and audit | Primary press release; no outcome metrics |
| **PwC agent OS** (Aug 2025) | Google Agentspace, Vertex AI, ADK, Agent Engine and **A2A**; also runs over Microsoft Foundry and orchestrates Anthropic, AWS, OpenAI, CrewAI, LangGraph | A2A and MCP explicitly | "Over 120 AI agents… spanning 24 cross-functional workflows"; "integrated, governed and auditable" | Primary; no quantified outcomes. The "25,000 agents" figure seen elsewhere is unverified |
| **Deloitte Zora AI** (Mar 2025) | NVIDIA stack; later SAP Joule and Oracle integrations | Not stated | Deloitte's current release states "targets to reduce costs by 25% and increase productivity by 40%" for expense management. The 18 Mar 2025 PR Newswire wording ("reducing costs by 25%") was repeated by PYMNTS and AI Business as achieved results, which it was not | Primary; figures are aspirational |
| **WSP** (Jan 2026) | Microsoft 365 Copilot + Copilot Studio; seven-year, US$1bn Microsoft partnership; Microsoft's 21 Jan 2026 customer story says Copilot is expanding to "tens of thousands of engineers and scientists" in a 75,000-strong firm, and that 84% of surveyed Copilot users "confirm they are saving time every day" | None stated | Soft productivity reports; "potential" faster project validation from a pilot | Microsoft customer story (vendor-authored) |
| **Worley** | AI.Assist agentic framework on Azure + NVIDIA; WorleyIQ (with Bloomfire) | None stated | NVIDIA's customer story says AI.Assist supports "approximately 50,000 users" and over 100,000 documents, and projects search time falling from 15+ minutes to "just a few minutes". Worley told ENR that WorleyIQ, deployed April–December 2025, "now serves roughly 3,000 engineers, consultants and digital specialists" and has full adoption among target users | Vendor story + trade press; outcomes projected |

**What this tells RSGx:** the professional-services leaders built **one governed platform with a registry and many agents** before chasing cross-vendor A2A. Engineering peers (WSP, Worley) are at the copilot/retrieval stage. No primary-sourced organisation-wide agent platform was found for AECOM, Jacobs, Arup, Bechtel, Fluor or Mott MacDonald. RSGx's "AI-native by end-2027" goal is ahead of documented sector practice, which is a differentiator and also a delivery risk.

## Recommendations

**Shortlist (in priority order)**

1. **Control plane: agentgateway + registry (adopt now; open source, Linux Foundation).** It is neutral, supports A2A, MCP and LLM routing, and preserves portability. Add **IBM ContextForge** specifically to expose A2A agents as MCP tools for Claude Enterprise, but only after a security review. Its earlier releases were labelled alpha.
2. **Primary runtime: choose one, based on RSGx's identity estate and residency needs.**
   - **Option A: Microsoft Foundry Agent Service + Copilot Studio + Microsoft Agent Framework.** Choose this if RSGx is on Microsoft 365/Entra. It has the deepest confirmed A2A v1.0 GA support, per-agent Entra identity, Purview audit, Claude models available, and ISO/IEC 42001-certified services. *Trade-offs:* high lock-in at the Copilot Studio layer; Malaysia-region feature and Claude-processing locations need confirmation; A2A reaches hosted agents through an extra MCP Toolbox hop.
   - **Option B: AWS Bedrock AgentCore (Asia Pacific, Malaysia) + Strands/LangGraph/MAF.** Choose this if in-country hosting and model neutrality are critical. It is framework- and model-agnostic, has native A2A in Runtime, and offers Identity, Policy and Evaluations. *Trade-offs:* more engineering-heavy (no Copilot-grade low-code front-end); regional feature parity and cross-region inference behaviour must be verified.
   - **Option C (watch, don't lead): Google Gemini Enterprise + ADK.** It is the A2A originator with the most complete native tooling and hosts Claude. It ranks lower for RSGx because Malaysian in-country residency is unconfirmed and it would add a third ecosystem alongside Claude and M365.
3. **Frameworks:** standardise on **Microsoft Agent Framework** (Option A) or **LangGraph** (either option) for code-first agents. Allow **Dify or n8n** (self-hosted) only for L1–L2 departmental automation, registered in the same catalogue. Note n8n's fair-code licence.
4. **SaaS agents** (ServiceNow, SAP Joule, Salesforce, Rovo): integrate them as registered A2A peers where these systems are already in use. Do not make any of them the hub.
5. **Claude Enterprise:** keep it as the knowledge-work surface (L1–L2). Govern its MCP connectors through the gateway. Monitor Anthropic for native A2A. Its absence as at September 2026 is the biggest architectural constraint.

**Sequenced plan aligned to the Three Horizons** *(see vocabulary warning in the editor's notes)*
- **H1 Enablement (Q4 2026 – Q1 2027):** stand up the registry, gateway, identity and observability. Run a residency/feature proof-of-concept in the Malaysia region with Option A or B. Move all MCP connectors behind the gateway. Adopt OWASP ASI01–ASI10 as the Forum's review checklist.
- **H2 Automation (2027 H1):** two or three L3 cross-functional pilots using A2A across functional-unit boundaries (e.g. bid/commercial → planning → document control), with signed cards, delegation-depth limits and evaluation evidence recorded for ISO/IEC 42001.
- **H3 Reinvention (2027 H2):** L4 Directed only for units that have passed the 42001 milestone gates, with the ISMS controls (8.15/8.16 logging and monitoring, 5.23 cloud) evidenced. Consider cross-organisation A2A with clients or joint-venture partners.

## Caveats

- **Shelf life:** spec versions (A2A v1.0, MCP 2026-07-28), vendor feature states (GA/preview), regional availability and model line-ups change monthly. Revalidate everything in section 2 by **March 2027** and at every contract signature. No pricing was verified. Obtain quotes directly.
- **Vendor claims vs facts:** adoption counts (150+ A2A supporters, 250+ AAIF members) are self-reported by the foundations. "Native A2A" for ServiceNow, Salesforce, SAP, Atlassian and UiPath comes from the A2A project's own AAIF application, not independent testing. Microsoft Agent Framework's multi-provider list and CrewAI's relative weaknesses come partly from secondary commentary.
- **Unverified in this research:** IBM watsonx Orchestrate's specific A2A level; native A2A in n8n, Flowise and Letta; Gemini Enterprise and Foundry feature availability in Malaysia; the exact current AgentCore feature set in ap-southeast-5.
- **Finding of absence:** "no native A2A in Claude" is based on Anthropic's public documentation and release notes to 24 September 2026. It could change quickly given Anthropic's AAIF membership.
- **Sector evidence is thin:** no primary-sourced A2A deployment in engineering, infrastructure or construction was found. Deloitte's figures are targets, and several vendor case studies report projected rather than measured outcomes.
- **ISO alignment is indicative:** the clause mappings above are a design aid, not an audit opinion. Confirm with RSGx's certification body, particularly for how agent autonomy levels are treated within the 42001 AIMS scope.

[^s-0928]: Session 2026-09-28 — Agent platforms and A2A (original artifact with inline citations)
