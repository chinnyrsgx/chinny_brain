---
type: Reference
title: "Agent platforms for RSGx: Paperclip, Dify, Microsoft Foundry and alternatives against Australian requirements (12 Oct 2026, mirrored)"
description: "Full text of Claude's 12 Oct research report comparing Paperclip, Dify and Microsoft Foundry with other agent platforms, weighted on customisability, with Australia as the governing jurisdiction. Supersedes the 28 Sep report."
tags: [agent-platform, a2a, mcp, reference, research, time-sensitive, australia, residency]
status: draft
provenance: P
generated: { by: claude/claude-opus-5-5, at: 2026-10-12T02:40:00Z }
stale_after: 2026-12-12T00:00:00Z
sources:
  - id: s-1012
    resource: https://claude.ai/code/session_01UNvDLfsAuXMiT9kpdm7JP6
    title: Session 2026-10-12 — Paperclip, Dify, Microsoft Foundry and alternatives
  - id: page-1012
    resource: https://claude.ai/artifact/8w3x22k4XJvb1xhiXzaB17
    title: Published page of this report (private artifact; the owner controls sharing)
---

> **Editor's notes (12 Oct).**
> 1. The text below is the report as delivered on 12 Oct 2026. It is mirrored unedited, except that the author line names Claude without a model identifier. A published page carries the same text.[^page-1012]
> 2. **Jurisdiction.** The owner confirmed in session that RSGx is Australian and that Australia is the governing jurisdiction.[^s-1012] That confirmation is relayed here, not recorded. Only the owner can record it ([open question](/open-questions/governing-jurisdiction.md)).
> 3. **Supersession.** At the owner's request in the same session, this report supersedes the [28 Sep report](/references/agent-platform-report-2026-09-28.md), and its proposal is carried into a [new recommendation](/assessments/agent-platform-recommendation-2026-10.md). Where the text below says the owner should "revise or supersede" the 28 Sep draft, that request has now been made. The supersession itself is a draft change awaiting the owner's review.
> 4. The recommendation, gates, rubric and scores are Claude's proposals and desk estimates. They are not decisions ([open question](/open-questions/agent-platform-selection.md)).

# Choose the layer before the platform

*Proposal [P] for the owner (Chris Chin, AI Governance Lead) and the AI Steering Committee (the Forum). Drafted by Claude on 12 October 2026 from research notes of the same date. Revised the same day after the owner confirmed that Australia is the governing jurisdiction. This is not a decision. The owner has not reviewed it and the Forum has not ratified it. A lack of objection would not turn any part of it into a decision.*

**In one paragraph.** Paperclip, Dify and Microsoft Foundry do not answer the same question. **Paperclip is an agent-company control plane.** It assigns work, budgets and approvals to agent runtimes that it neither builds nor hosts. **Dify is an LLM application and workflow builder.** It runs its own visual workflows, RAG pipelines and plugins. **Foundry is a hyperscaler model and agent platform.** It hosts models, agent code, agent identities and Azure governance. The comparison is weighted mainly on customisability, and the evidence there runs against intuition. The open-source products give RSGx the right to edit their source. The hyperscaler runtimes give it more of the customisation a governed programme needs: the ability to bring its own code, models, tools and policy controls into a runtime that ties each agent to an identity and audits it. An indicative desk scoring against Australian requirements puts **AWS Bedrock AgentCore (about 72 of 100) and Foundry (about 68) ahead of Google's Agent Platform (about 63), Dify Community (about 52) and Paperclip (about 46)**, and the order holds under every weighting tested. Against the six must-pass gates, Paperclip as shipped fails two: it can delete its own audit trail, and it has no supported-version or response-time policy despite five Critical advisories in seven months. Dify passes only conditionally, because its licence counts each workspace as a tenant. Google fails the Australian residency gate. The owner confirmed on 12 Oct 2026 that Australia is the governing jurisdiction. That makes **where model inference runs the binding constraint**. Only AWS documents an Australia-only path for current Claude models. Foundry keeps agent data in Australia East, but processes current frontier models, and every Claude model, outside Australia. The proposal [P] is to decide layer by layer. Keep the RSGx-owned control-plane pattern. Choose between Foundry and AgentCore in Sydney through a short proof of concept. Confirm Dify only for departmental solutions at autonomy level L1–L2. Hold Paperclip to an isolated evaluation. Ask the owner to revise or supersede the 28 September draft, whose Malaysian framing does not fit an Australian organisation and whose Malaysian facts are partly wrong.

*Dating convention.* Every version, star count, issue count, price, GA or preview status and region fact below is **as at 12 Oct 2026** unless the claim says otherwise. Open-source project facts (versions, stars, issues, advisories, licence text) have a suggested **re-check date of 12 Dec 2026**, because these projects release weekly to monthly. Hyperscaler and SaaS facts (prices, regions, GA status) have a suggested **re-check date of 12 Jan 2027**. Regulatory items carry the dates given where they appear. The labels follow programme convention: [P] is a proposal by Claude, and [I] is an inference that needs verification. Nothing in this report is [C].

## Three products sit at three different layers, so the comparison is not like-for-like

It is tempting to treat this as a three-way contest. In fact each product answers a different question, and the programme's own [P] architecture already has a place for each kind of answer.

**Paperclip** describes itself as "a Node.js server and React UI that orchestrates a team of AI agents to run a business". It says plainly that it is "Not an agent framework" and "Not a prompt manager" ([Paperclip README](https://github.com/paperclipai/paperclip/blob/bfe7c6357d1e0c945c8cb84259153cb3b6542d28/README.md)). Its world is made of companies, an org chart in which "every agent reports to exactly one manager", issues that one agent at a time checks out, scheduled heartbeats, budgets and board approvals ([core concepts](https://github.com/paperclipai/paperclip/blob/bfe7c6357d1e0c945c8cb84259153cb3b6542d28/docs/start/core-concepts.md)). The agents themselves are external harnesses such as Claude Code, Codex, OpenClaw and Cursor, which Paperclip wakes through adapters ([adapter overview](https://github.com/paperclipai/paperclip/blob/bfe7c6357d1e0c945c8cb84259153cb3b6542d28/docs/adapters/overview.md)).

**Dify** is an LLM application and workflow builder. Its app types run from workflows and chatflows to a legacy ReAct agent and, since July 2026, a sandboxed "Dify Agent". Its visual editor offers 26 node types, from LLM calls and knowledge retrieval to code, HTTP, human input and triggers ([AppMode](https://github.com/langgenius/dify/blob/7068d0d60ab1408c2ca4066c05a6899fe9e4654c/api/models/model.py#L387); [workflow nodes](https://github.com/langgenius/dify/tree/7068d0d60ab1408c2ca4066c05a6899fe9e4654c/web/app/components/workflow/nodes)).

**Microsoft Foundry** is a hyperscaler model and agent platform. It is a single Azure resource that brings together a model catalogue, Agent Service (declarative prompt agents and containerised hosted agents), Toolboxes, Foundry IQ retrieval, evaluations and a governance Control Plane, all under one RBAC and networking boundary ([What is Microsoft Foundry?](https://learn.microsoft.com/en-us/azure/foundry/what-is-foundry)).

| | Paperclip | Dify | Microsoft Foundry |
|---|---|---|---|
| **Layer** | Agent-company control plane: the work, org-chart, budget and approval layer over external agent runtimes | LLM app and workflow builder: visual workflows, RAG, plugins | Hyperscaler model and agent platform: models, hosted agent runtime, identity, governance |
| **Core abstraction** | Company → org chart → issues → heartbeats → approvals | App → workflow graph → nodes, knowledge bases, plugins | Foundry resource → projects → prompt or hosted agents, model deployments, Toolboxes |
| **Who defines agent behaviour** | The external harness (Claude Code, Codex, OpenClaw and so on) | Dify's builder and its own agent runtimes | RSGx's code (any Python or C# framework) or a declarative prompt agent |
| **Hosts models?** | No; harnesses call their own providers | No; it calls providers through model plugins | Yes: serverless and provisioned deployments |
| **Where code executes** | Agent CLIs spawned on the Paperclip host, or on SSH, sandbox or Kubernetes targets | Separate sandbox containers behind an SSRF proxy | Microsoft-managed, per-session VM-isolated sandboxes |
| **Programme interface type** (UI-gap assessment) | A governance console for the agents it wakes; not a cross-runtime registry | Builder, plus embeddable end-user web apps | Runtime, builder (portal) and governance console (Control Plane, preview) |
| **Licence and commercial model** | MIT; no paid offer yet (Cloud waitlist only) | Modified Apache 2.0; Community, Cloud, Premium and Enterprise editions | Proprietary Azure service, billed on consumption |

The phrase **"control plane" means three different things** in this decision, and the Forum should keep them apart.

- **Paperclip's sense.** Paperclip calls itself one: "Control plane, not execution plane — Paperclip orchestrates agents; it doesn't run them" ([architecture](https://github.com/paperclipai/paperclip/blob/bfe7c6357d1e0c945c8cb84259153cb3b6542d28/docs/start/architecture.md)).
- **Foundry's sense.** Foundry has a product called "Control Plane". It is a preview, portal-only fleet inventory and compliance view, and it needs an AI gateway for advanced governance ([Foundry Control Plane](https://learn.microsoft.com/en-us/azure/foundry/control-plane/overview)).
- **The programme's sense.** The programme's 28 September [P] report proposes an **RSGx-owned control plane**: an A2A/MCP gateway (agentgateway), an agent registry, enterprise identity and OpenTelemetry tracing (`bundles/rsgx-ai-programme/references/agent-platform-report-2026-09-28.md`, line 247).

Paperclip cannot fill the programme's slot, for two reasons. First, it implements no A2A. The value `a2a` is only a reserved enum entry, and an internal ADR says such types "can be added" later ([constants.ts](https://github.com/paperclipai/paperclip/blob/bfe7c6357d1e0c945c8cb84259153cb3b6542d28/packages/shared/src/constants.ts); [ADR](https://github.com/paperclipai/paperclip/blob/bfe7c6357d1e0c945c8cb84259153cb3b6542d28/doc/plans/2026-06-05-agent-access-mcp-runtime-slots-adr.md)). Second, its activity log can be hard-deleted.

Foundry's Control Plane matters more. It claims to cover agents "from multiple platforms, including Foundry, Microsoft, and non-Microsoft sources". That partly answers the UI-gap assessment's finding that no vendor offers a cross-runtime Forum view, but it is still a preview.

Seen by layer, the three products complement each other more than they substitute for each other. [I] Paperclip could in principle wake a Dify workflow through its `http` adapter or over MCP, and both could call models deployed in Foundry. Nobody has tested this. It is mentioned only to show that "Paperclip or Dify or Foundry" is the wrong frame. The right questions are these:

- Which product, if any, should fill the **builder** layer for low-autonomy departmental work?
- Which should fill the **runtime** layer for governed, code-first agents?
- Does an **agent-company orchestration** layer belong in the architecture at all?

## Paperclip and Dify differ in what they let RSGx change, and in what breaks when it does

### Paperclip directs other people's agents; Dify runs its own

**How Paperclip runs agents.** On each heartbeat, Paperclip calls an adapter that "spawns the agent (e.g. Claude Code CLI) with Paperclip env vars and a prompt". The agent then calls Paperclip's REST API to check out work, and Paperclip parses the agent's output to record cost and usage ([architecture](https://github.com/paperclipai/paperclip/blob/bfe7c6357d1e0c945c8cb84259153cb3b6542d28/docs/start/architecture.md)). Twelve adapter packages ship in-tree, alongside generic `process` (shell) and `http` (webhook) adapters.

The slogan "control plane, not execution plane" is therefore true of models but not of processes. With the default local adapters, the Paperclip host is where agent CLIs execute, and they run with their own safeguards switched off:

- Claude Code receives `--dangerously-skip-permissions` by default ([claude-local](https://github.com/paperclipai/paperclip/blob/bfe7c6357d1e0c945c8cb84259153cb3b6542d28/packages/adapters/claude-local/src/index.ts)).
- Codex receives `--dangerously-bypass-approvals-and-sandbox` by default ([codex-args](https://github.com/paperclipai/paperclip/blob/bfe7c6357d1e0c945c8cb84259153cb3b6542d28/packages/adapters/codex-local/src/server/codex-args.ts)).
- Release v2026.1001.0 made "full auto" the default for every native harness ([release notes](https://github.com/paperclipai/paperclip/blob/bfe7c6357d1e0c945c8cb84259153cb3b6542d28/releases/v2026.1001.0.md)).

An earlier research thread said that Paperclip "relies on each runtime's own sandbox". **That claim is wrong.** Paperclip switches those sandboxes off by default. Isolation comes only from an environment the operator chooses: SSH targets, sandbox-provider plugins (E2B, Daytona, Modal, Kubernetes and others), or an experimental "managed sandbox only" flag that is off by default.

**How Dify runs code.** Dify makes its own LLM calls and runs its own code. Code nodes call a separate `sandbox` container whose outbound traffic is forced through a Squid SSRF proxy, and the new agent sandbox "has NO direct route to `api`" ([docker-compose](https://github.com/langgenius/dify/blob/7068d0d60ab1408c2ca4066c05a6899fe9e4654c/docker/docker-compose.yaml)). The design is sound, but self-hosters inherit weak defaults. The code sandbox has network access enabled by default. The shipped `.env.example` also contains hard-coded credentials that must all be rotated before production, including `DB_PASSWORD=difyai123456`, `SANDBOX_API_KEY=dify-sandbox` and `DIFY_AGENT_API_TOKEN=dify-agent-run-token-for-dev-only` ([.env.example](https://github.com/langgenius/dify/blob/7068d0d60ab1408c2ca4066c05a6899fe9e4654c/docker/.env.example)).

### Both are open at the edges and closed at the core, in different places

**Paperclip's extension points are broad:**

- **External adapters.** An adapter is an npm package that exports `createServerAdapter()` with one `execute()` function. It "can be installed from npm packages or local directories" without changing Paperclip's source ([external adapters](https://github.com/paperclipai/paperclip/blob/bfe7c6357d1e0c945c8cb84259153cb3b6542d28/docs/adapters/external-adapters.md)).
- **Plugins.** Each plugin runs in its own Node process over JSON-RPC. Plugins can add agent tools, event subscriptions, scheduled jobs, webhooks, UI slots and scoped API routes.
- **Tool gateway.** An MCP tool gateway can set each action to "Allowed, Ask first, or Off".
- **APIs and portability.** There is an MCP server, a REST API with an OpenAPI route, and import and export of whole companies.

**Paperclip's limits are structural:**

- **Plugins are trusted code.** Plugin UI runs "same-origin… Treat plugin UI as trusted code", and the plugin model assumes a "single-tenant, self-hosted, single-node" deployment.
- **Governance cannot be replaced by plugins.** "Board governance, approval gates, budget hard-stops, and core task invariants remain owned by Paperclip core" ([PLUGIN_SPEC](https://github.com/paperclipai/paperclip/blob/bfe7c6357d1e0c945c8cb84259153cb3b6542d28/doc/plugins/PLUGIN_SPEC.md)).
- **One approver only.** The execution policy states `approvalsNeeded: 1; // multi-approval is not supported yet` ([execution policy](https://github.com/paperclipai/paperclip/blob/bfe7c6357d1e0c945c8cb84259153cb3b6542d28/docs/guides/execution-policy.md)). Four-eyes approval or a custom approval type therefore means forking the core.
- **Forks are costly to maintain.** The core has shipped about 30 stable releases and 333 database migrations in roughly seven months, with breaking changes in most recent releases.

**Dify's extension points go deeper into how an LLM app behaves:**

- **Plugins.** There are six plugin categories (Tool, Model, Extension, AgentStrategy, Datasource, Trigger), shipped as signed `.difypkg` packages that can be signed with third-party keys ([plugin entities](https://github.com/langgenius/dify/blob/7068d0d60ab1408c2ca4066c05a6899fe9e4654c/api/core/plugin/entities/plugin.py#L61)).
- **Tools and MCP.** Tools can be built from OpenAPI specs. Dify is an MCP client (HTTP only) and, since v1.16.0, an MCP server supporting protocol 2025-06-18 ([release 1.16.0](https://github.com/langgenius/dify/releases/tag/1.16.0); [two-way MCP](https://dify.ai/blog/v1-6-0-built-in-two-way-mcp-support)).
- **Other interfaces.** There is an external knowledge API, a service API, embeddable web apps and a versioned YAML DSL (app DSL 0.7.0).

**Dify's limits sit in the engine and the edition:**

- **No custom node types.** There is no plugin type for workflow nodes, and the engine now lives in an external pinned package, `graphon==0.7.0`. A new node type therefore means forking both that engine and the React editor ([pyproject](https://github.com/langgenius/dify/blob/7068d0d60ab1408c2ca4066c05a6899fe9e4654c/api/pyproject.toml)).
- **Plugin trust controls are Enterprise-only.** The "official only" installation scope and marketplace-only installs are Enterprise switches in the code ([feature entities](https://github.com/langgenius/dify/blob/7068d0d60ab1408c2ca4066c05a6899fe9e4654c/api/services/entities/feature_entities.py)).

**The licences diverge sharply.**

**Paperclip** is MIT, with no CLA and no trademark policy ([LICENSE](https://github.com/paperclipai/paperclip/blob/bfe7c6357d1e0c945c8cb84259153cb3b6542d28/LICENSE)). There is no vendor contract, SLA or indemnity. The only official commercial path is a Paperclip Cloud waitlist with no published price ([paperclip.ing](https://paperclip.ing)). A similarly named third party, paperclip.inc, announced it would shut down on 2 October 2026 ([paperclip.inc](https://paperclip.inc/)). Any "hosted Paperclip" quote must therefore be traced back to Paperclip Labs.

**Dify** is "a modified version of the Apache License 2.0" with four additions ([LICENSE](https://github.com/langgenius/dify/blob/7068d0d60ab1408c2ca4066c05a6899fe9e4654c/LICENSE)):

- It bars any "multi-tenant environment" without written authorisation, and defines a tenant as follows: "one tenant corresponds to one workspace".
- It bars removing the logo from the bundled frontend.
- It lets the producer make the licence "more strict".
- It asserts an "appearance patent".

Every substantive revision since 2023 has broadened or clarified the restrictions ([LICENSE history](https://github.com/langgenius/dify/commits/main/LICENSE)). Dify's own pricing page positions Community as "Single workspace" ([pricing](https://dify.ai/pricing)). [I] Read literally, an organisation-wide Dify serving 16 functional units through separate workspaces is a licensed Enterprise deployment, not a free one. LangGenius has published nothing on whether workspaces used only internally count as tenants.

### Governance primitives exist in both, but neither is enterprise-ready as shipped

**What Paperclip has.** Its governance controls are real code under MIT:

- company-scoped RBAC with owner, admin, operator and viewer roles and 21 permission keys, enforced in route handlers ([constants.ts](https://github.com/paperclipai/paperclip/blob/bfe7c6357d1e0c945c8cb84259153cb3b6542d28/packages/shared/src/constants.ts));
- company, agent and project budgets, with an alert at 80% and a hard stop at 100% ([costs and budgets](https://github.com/paperclipai/paperclip/blob/bfe7c6357d1e0c945c8cb84259153cb3b6542d28/docs/guides/board-operator/costs-and-budgets.md));
- board approvals, and review and approval stages on individual issues.

**Where Paperclip falls short:**

- **No login by default.** The default `local_trusted` mode requires no login ([deployment modes](https://github.com/paperclipai/paperclip/blob/bfe7c6357d1e0c945c8cb84259153cb3b6542d28/docs/deploy/deployment-modes.md)).
- **No self-hosted SSO.** Self-hosted authentication is email and password only ([better-auth.ts](https://github.com/paperclipai/paperclip/blob/bfe7c6357d1e0c945c8cb84259153cb3b6542d28/server/src/auth/better-auth.ts)). The README's "SSO, GRC, RBAC & cost controls" therefore overstates the self-hosted code: SSO appears only on the Cloud side, and there is no GRC feature at all.
- **Weak approvals.** Agents can approve other agents' work, and only one approver is allowed.
- **A deletable audit trail.** Deleting an agent runs `tx.delete(activityLog)` and removes its decision rows ([agent-deletion.ts](https://github.com/paperclipai/paperclip/blob/bfe7c6357d1e0c945c8cb84259153cb3b6542d28/server/src/services/agent-deletion.ts)), while the website promises an "Immutable audit log… No edits, no deletions" ([paperclip.ing](https://paperclip.ing)).
- **Telemetry on by default.** Usage data goes to `telemetry.paperclip.ing`, with a fallback AWS API Gateway in us-east-1 ([telemetry client](https://github.com/paperclipai/paperclip/blob/bfe7c6357d1e0c945c8cb84259153cb3b6542d28/packages/shared/src/telemetry/client.ts)). For an Australian organisation, that is an offshore flow to switch off.
- **Limited secrets management.** Only the local store and AWS Secrets Manager work; Vault and GCP are stubs.

**What Dify Community has.** It provides five roles: owner, admin, editor, normal and dataset_operator ([account enums](https://github.com/langgenius/dify/blob/7068d0d60ab1408c2ca4066c05a6899fe9e4654c/api/enums/account.py)). It also has content-moderation hooks and tracing integrations for Langfuse, LangSmith, Phoenix, MLflow, Opik and others. Fine-grained RBAC, enforced SSO, plugin-installation policy, branding and enterprise OTLP export are Enterprise switches in the open code ([enterprise config](https://github.com/langgenius/dify/blob/7068d0d60ab1408c2ca4066c05a6899fe9e4654c/api/configs/enterprise/__init__.py)).

### The security records show two projects hardening in public

**Paperclip** has published **12 GitHub security advisories, five of them Critical**, all between April and July 2026 ([advisories](https://github.com/paperclipai/paperclip/security/advisories)). The Critical five are:

- unauthenticated remote code execution through an import authorisation bypass;
- OS command injection;
- two cross-tenant agent-key flaws;
- a drive-by DNS-rebinding remote code execution, rated CVSS 9.6, whose advisory lists **no patched version** ([GHSA-x8hx-rhr2-9rf7](https://github.com/paperclipai/paperclip/security/advisories/GHSA-x8hx-rhr2-9rf7)).

Until v2026.916.0 (16 Sep 2026), agent APIs echoed plaintext credentials to any caller that could read the agent ([release notes](https://github.com/paperclipai/paperclip/blob/bfe7c6357d1e0c945c8cb84259153cb3b6542d28/releases/v2026.916.0.md)). SECURITY.md states no supported versions and no response time ([SECURITY.md](https://github.com/paperclipai/paperclip/blob/bfe7c6357d1e0c945c8cb84259153cb3b6542d28/SECURITY.md)).

The project is both extremely popular and very young. It has **100,392 stars and 16,913 forks**, from a repository created on 2 Mar 2026. It has **2,946 open issues**, about 94% of them unlabelled ([GitHub repo](https://github.com/paperclipai/paperclip); [unlabelled open issues](https://github.com/paperclipai/paperclip/issues?q=is%3Aissue%20state%3Aopen%20no%3Alabel)). In the one page of merged PRs sampled, two maintainers dominated. A secondary profile reports a pseudonymous lead and no disclosed funding, and concludes that "Bus factor is the project's biggest structural risk" ([rywalker.com](https://rywalker.com/research/paperclip)).

**Dify** has published **21 advisories between April 2025 and August 2026: 8 High, 10 Moderate, 3 Low and none Critical** ([advisories](https://github.com/langgenius/dify/security/advisories)). About half are access-control, IDOR or cross-tenant flaws. Four of those, published in July and August 2026, hit multi-workspace isolation and the MCP server, which is exactly the multi-workspace deployment an organisation-wide rollout would need.

Dify is older and better funded than Paperclip. It has 158.2k stars and about 14,000 commits since April 2023 ([GitHub repo](https://github.com/langgenius/dify)). It shipped 11 releases in the past 12 months, several of which required database migrations ([releases](https://github.com/langgenius/dify/releases)). It raised a US$30M Series Pre-A in March 2026, led by HSG ([Dify blog](https://dify.ai/blog/dify-raises-30m-tomorrow-s-organizations-will-be-built-by-people-and-agents)). [I] HSG is very likely HongShan, formerly Sequoia China. That matters only to sovereignty screening, and it is unconfirmed by a primary source.

Dify says it has passed SOC 2 Type II and ISO 27001:2022 audits ([Dify blog](https://dify.ai/blog/dify-achieves-soc-2-iso-27001-gdpr-compliance-for-the-second-year-running)). Its own policy pages still say it is "in the process" of obtaining them, and no source states which editions the audits cover. Dify Cloud is US-hosted, and no source shows an Australian Cloud region. Australian residency for Dify therefore means self-hosting.

| As at 12 Oct 2026 (re-check 12 Dec 2026) | Paperclip | Dify (Community, self-hosted) |
|---|---|---|
| Latest stable release | v2026.1005.0 (5 Oct 2026); about 30 releases since March 2026 | 1.17.1 (10 Sep 2026); 11 releases in 12 months |
| Where customisation is strongest | Which agents it manages (any runtime that "can receive a heartbeat") | How an LLM app behaves (nodes, RAG, model providers, plugins) |
| Extension model | npm adapters and out-of-process plugins; plugins are trusted code | Six signed plugin types and OpenAPI tools; no custom workflow-node type |
| Can governance itself be customised? | Only by forking the core | Mostly only by buying Enterprise |
| MCP / A2A | MCP client and server; **no A2A** | MCP client (HTTP only) and server; A2A only through a community plugin (not re-verified) |
| Identity | Email and password; no self-hosted SSO | Email and password; SSO is Enterprise-only |
| Audit | Activity log, hard-deleted with the agent | Tracing integrations; operation logs and OTLP are Enterprise-only |
| Licence | MIT, unrestricted | Modified Apache 2.0: one workspace = one tenant, logo must be kept, producer may tighten |
| Advisories | 12, five Critical (Apr–Jul 2026) | 21, none Critical (Apr 2025–Aug 2026) |
| Backing | Paperclip Labs; no disclosed funding; repository seven months old | LangGenius; US$30M Series Pre-A (Mar 2026); repository 3.5 years old |

So which is more customisable? The honest answer has two halves. **Paperclip is broader and freer**: it can manage almost any agent, under the least restrictive licence there is. **Dify is deeper**: it controls more of how an application behaves and reaches far more model providers natively. Neither lets RSGx customise *governance* without paying for it. Paperclip keeps governance in a core RSGx would have to fork, and Dify keeps it in an edition RSGx would have to buy. [I] For an AI governance programme, that shared weakness matters more than the differences between them.

## Foundry offers governed customisation, but Australian residency limits it

### Customisation stops at the container boundary and the region list

Foundry's hosted agents let RSGx "Bring your own code – use any framework (Agent Framework, LangGraph, Semantic Kernel, or custom code)" ([hosted agents](https://learn.microsoft.com/en-us/azure/foundry/agents/concepts/hosted-agents)). The agent is packaged as a container image in Azure Container Registry. Foundry gives it a dedicated Entra agent identity and exposes it over several protocols: the OpenAI-compatible Responses API, free-form Invocations (including over WebSocket), the Activity protocol for Teams and Microsoft 365, and A2A (v1.0 GA, v0.3 preview).

Tools reach the agent through a Toolbox MCP endpoint. Toolboxes became GA on 9 Jul 2026 ([July–August 2026 roundup](https://devblogs.microsoft.com/foundry/whats-new-in-microsoft-foundry-july-august-2026/)). In Standard setup, agent state stays in RSGx's own Cosmos DB, Storage and AI Search, inside a customer VNet with no public egress ([Agent Service limits and regions](https://learn.microsoft.com/en-us/azure/foundry/agents/concepts/limits-quotas-regions)).

The native code path is Microsoft Agent Framework. It is MIT-licensed and reached 1.0 on 3 Apr 2026 with a commitment to long-term support. Its workflows support checkpointing and human-in-the-loop approval in every orchestration pattern ([Agent Framework 1.0](https://devblogs.microsoft.com/agent-framework/microsoft-agent-framework-version-1-0/)).

The limits are just as specific:

- **Hosted-agent constraints.** Python and C# only; at most 2 vCPU and 4 GiB per session; no traffic splitting between versions; a private registry only for projects created after 25 Jun 2026.
- **Own model weights.** Bringing your own weights needs "managed compute", which is still a preview and processes data globally only ([deployment overview](https://learn.microsoft.com/en-us/azure/foundry/concepts/deployments-overview)).
- **Fine-tuning.** From Australia East, fine-tuning is Global training only, which "doesn't offer data residency" ([fine-tuning](https://learn.microsoft.com/en-us/azure/foundry/fine-tuning/overview)).
- **Workflows retirement.** Foundry's own visual Workflows feature never reached GA and **retires on 1 Dec 2026**, with users told to "Use Microsoft Agent Framework for new development" ([GA overview](https://learn.microsoft.com/en-us/azure/foundry/concepts/general-availability)).

That last point is a lesson in itself. A declarative portal feature was replaced by code, which is a warning against building governed logic in any vendor's visual layer.

### Governance is the strongest of the three, but with a preview fringe and a Claude carve-out

**What Foundry inherits from Microsoft's security stack:**

- Entra ID is required for agents, and each hosted agent gets its own identity.
- Azure Policy guardrail policies can, for example, deny GlobalStandard deployments ([manage compliance and security](https://learn.microsoft.com/en-us/azure/foundry/control-plane/how-to-manage-compliance-security); [deployment types](https://learn.microsoft.com/en-us/azure/foundry/foundry-models/concepts/deployment-types)).
- Purview audit, DSPM and DLP apply, but DLP covers only calls made with user-context tokens, and Purview policies need pay-as-you-go billing ([Purview for Foundry](https://learn.microsoft.com/en-us/purview/ai-azure-foundry)).
- Defender AI threat protection is GA, but it scans text only ([Defender](https://learn.microsoft.com/en-us/azure/defender-for-cloud/ai-threat-protection)).
- Evaluations and red-teaming are GA, and MCP tool calls can be made to require approval ([MCP tool](https://learn.microsoft.com/en-us/azure/foundry/agents/how-to/tools/model-context-protocol)).

**What is still in preview.** Much of what the Forum would rely on has not reached GA: agent guardrails, "controls and intervention", monitoring, memory, the Control Plane's compliance and asset panes, and AI Gateway ([GA overview](https://learn.microsoft.com/en-us/azure/foundry/concepts/general-availability)). Microsoft itself lists "Treating Preview features as production dependencies without explicit approval" as a common pitfall.

**Two further caveats.** First, extending Entra security features to agents "requires Microsoft Agent 365", and Agent 365 needs "a Microsoft Agent 365 license for each user" ([Entra Agent ID](https://learn.microsoft.com/en-us/entra/agent-id/what-is-microsoft-entra-agent-id)). A secondary source reports a price of US$15 per user per month ([Licensing Guide](https://licensing.guide/may-1-ga-is-not-yet-the-final-frontier-for-agent-365/)). Second, Microsoft's data commitments, such as no training on customer data and no sharing with model providers, apply to "Models sold by Azure". For Claude, Anthropic is "seller of record", "operator" and "independent data processor" ([Claude hosting comparison](https://learn.microsoft.com/en-us/azure/foundry/foundry-models/concepts/claude-models-hosting-comparison)).

**Assurance.** Microsoft states that it **achieved ISO/IEC 42001:2023 certification for Azure AI Foundry Models** in July 2025 ([Azure blog](https://azure.microsoft.com/en-us/blog/microsoft-azure-ai-foundry-models-and-microsoft-security-copilot-achieve-iso-iec-420012023-certification/)). Azure OpenAI was **IRAP-assessed at PROTECTED** in the 2024 round ([Microsoft Australia](https://news.microsoft.com/en-au/features/microsofts-commitment-to-trust-in-australia-introducing-2024-azure-dynamics-365-and-microsoft-365-irap-assessments/)). The 2026 IRAP announcement names no AI services, and it reminds readers that "IRAP is not a certification" ([Microsoft Source Asia](https://news.microsoft.com/source/asia/2026/03/26/irap-au-2026/)). Whether Agent Service and hosted agents are in IRAP scope is **unverified**, because the scope list sits behind a sign-in on the Service Trust Portal.

These certificates and assessments support RSGx's supplier assurance only. They do not extend to RSGx's own agents or its AI management system, which is being built to ISO/IEC 42001.

### Australian residency is Foundry's weak point

**Australia East is the only Australian Foundry region.** It supports Agent Service, hosted agents and private networking, but not Computer Use. "Data is stored in the same region as the endpoint" ([Agent Service limits and regions](https://learn.microsoft.com/en-us/azure/foundry/agents/concepts/limits-quotas-regions)).

Inference is another matter. In Australia East, in-country pay-per-token processing is available only for gpt-4.1-mini, gpt-4o and the embedding models. GPT-5 to GPT-5.4 can be processed in-country only on Regional provisioned throughput (PTU), which means reserving capacity. Newer models are offered at best on the **APAC Data Zone**, which spans Australia, Japan, Korea, Singapore and India; Microsoft can add regions to it "without prior notice". **Claude is offered only as Global or US Data Zone** ([region availability](https://learn.microsoft.com/en-us/azure/foundry/foundry-models/concepts/models-sold-directly-by-azure-region-availability); [partner models](https://learn.microsoft.com/en-us/azure/foundry/foundry-models/concepts/models-from-partners)).

There is no second Australian Foundry region, so disaster recovery inside Australia is not possible. The practical enforcement control is an Azure Policy that denies Global (and, where needed, Data Zone) deployment types. Microsoft documents that pattern ([deployment types](https://learn.microsoft.com/en-us/azure/foundry/foundry-models/concepts/deployment-types)).

### Cost is consumption-based, and residency carries a premium

Foundry has no platform fee. Hosted agents cost **US$0.0994 per vCPU-hour and US$0.0118 per GiB-hour**, the same in Australia East as in East US ([Azure Retail Prices API](https://prices.azure.com/api/retail/prices)). [I] For example, 50 concurrent 1-vCPU sessions running eight hours a day for 22 days cost about US$1,080 a month in hosting, before tokens.

Residency costs show up in token and capacity prices. GPT-5.5 costs **US$5.00 per million input tokens and US$30.00 per million output tokens on Global Standard**, against **US$6.00 and US$36.00 on the APAC Data Zone**. That is a 20% premium, compared with 10% in the US and EU. A Regional PTU in Australia East costs US$2.28 an hour, against US$1.00 for Global ([Azure Retail Prices API](https://prices.azure.com/api/retail/prices)).

Claude is bought through the Azure Marketplace in "Claude Consumption Units". These count towards a Microsoft Azure Consumption Commitment (MACC), but **CSP subscriptions cannot buy it** ([Claude hosting comparison](https://learn.microsoft.com/en-us/azure/foundry/foundry-models/concepts/claude-models-hosting-comparison)). That matters for any Australian organisation that buys Azure through a CSP partner.

### Lock-in sits in the operational layer, not the code

The code layer is portable. Agent Framework is MIT. Hosted agents are ordinary containers. The Responses API is OpenAI-compatible. Tools speak MCP, OpenAPI and A2A, and traces are OpenTelemetry.

The operational layer is Azure-specific and would have to be rebuilt on exit. It includes prompt-agent definitions, Toolbox-held credentials, Foundry IQ, Entra agent identities, Azure Policy guardrails, Model Router and the Marketplace commercial wrapper.

[I] The most portable Foundry design writes agents in Agent Framework or LangGraph, calls models through the OpenAI SDK, keeps state in Standard setup and exports traces to a neutral store. The least portable design is a portal-built prompt agent that uses Foundry IQ, Toolbox credentials and Control Plane guardrails.

| Lens (as at 12 Oct 2026) | Paperclip | Dify | Microsoft Foundry |
|---|---|---|---|
| **Customisability** | Broad: any agent runtime, MIT fork rights; governance core closed | Deep in-app: nodes, RAG, six plugin types; no custom node type; branding and multi-workspace limited by licence | Bring your own code (Python or C#), tools and storage; no source access; hosting your own weights is preview and Global-only |
| **Governance and security** | RBAC, budgets and approvals in code; no SSO; deletable audit trail; permissive defaults; five Critical advisories | Basic roles; SSO, RBAC, plugin policy and audit are Enterprise-only; 21 advisories, none Critical | Per-agent Entra identity, Azure Policy, Purview, Defender; key controls still preview; Claude outside Microsoft's data commitments |
| **Capability and architecture** | Org, ticket and budget orchestration of coding and ops agents; single node; no RAG of its own | Strong RAG and app builder; agent runtime in beta since Jul 2026; 10+ containers to self-host | Full model and agent platform; hosted agents GA 9 Jul 2026; Workflows retire 1 Dec 2026 |
| **Cost and licensing** | Free; no commercial support exists | Community free (one workspace); Cloud US$590 or US$1,590 per workspace per year; Enterprise price not published | No platform fee; compute, tokens, PTUs, Agent 365 seats, Purview and Defender billed separately |
| **Deployment and lock-in (Australia)** | Self-host in an Australian region; low data lock-in (Postgres, export); telemetry to the US unless disabled | Self-host in an Australian region; Dify-specific DSL; Cloud is US-only | Australia East only; in-country inference limited; no Claude in Australia; Azure-specific operational layer |

## Three families of alternatives, of which only a handful matter to RSGx

### Open-source low-code builders: Dify's real rivals are n8n, Sim and Activepieces

Five products are realistic substitutes for Dify. Two more are specialist tools, and the rest are chat front ends.

**Flowise is no longer a candidate.** Workday acquired it in August 2025. Its repository was archived on 13 Aug 2026, and core-team support ended on 31 Aug 2026. Advisories were still being published on 7 Oct 2026 ([Flowise wind-down](https://github.com/FlowiseAI/Flowise/discussions/6727)). Acquisition by a large enterprise vendor is therefore a risk signal, not a safety signal.

**Langflow** gives the most code-level control of any builder: every component is editable Python, under MIT. It also has **six CISA KEV entries, one with known ransomware use**, and its documentation says it "provides no isolation between tenants" ([Langflow security](https://docs.langflow.org/security); [CISA KEV](https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json)).

**Sim** stands out on licence. It is Apache 2.0, and self-hosted deployments unlock SSO, audit logs and permission groups "through environment configuration instead of billing" ([Sim enterprise docs](https://docs.sim.ai/enterprise)). But it was founded in 2025 and had two unauthenticated Critical flaws in March 2026.

Against these, Dify's record is middling but defensible. It has **no KEV entry and no Critical GitHub advisory**, whereas most of its rivals have at least one Critical CVE. That confirms Dify as the stronger builder of record, if a builder is needed. None of these vendors documents an Australian cloud region, so every option below means self-hosting in an Australian region.

| Builder (re-check 12 Dec 2026) | Licence | Customisability | Governance: free vs paid | Security record (Apr 2025–Oct 2026) | Verdict for RSGx |
|---|---|---|---|---|---|
| **n8n** | Sustainable Use Licence (fair-code, not OSI); `.ee.` files under an enterprise licence | High: TypeScript nodes, code steps, MCP client and server | SSO and Git need Business (€667 a month); audit and log streaming need Enterprise ([pricing](https://n8n.io/pricing/)) | 1 KEV entry; 153 advisories, 24 Critical ([OSV](https://osv.dev/list?q=n8n&ecosystem=npm)) | Best for integration-heavy internal automation; never offer it to clients |
| **Langflow** | MIT | Very high | No real multi-tenancy | **6 KEV entries** | Developer sandbox only |
| **Sim** | Apache 2.0 | High; remote E2B or Daytona sandboxes | SSO and audit unlocked by a flag when self-hosted | 11 CVEs, 2 Critical (fixed Mar 2026) | Most promising permissive option, but unproven |
| **Activepieces** | MIT core plus a commercial `ee` licence | High for integrations; JSON export | SSO in Team (US$200 a month); audit and custom RBAC in Ultimate ([pricing](https://www.activepieces.com/pricing)) | 8 CVEs, 1 Critical | Viable automation tool; vendor states a SOC 2 Type 2 report ([security](https://www.activepieces.com/security)) |
| **RAGFlow** | Apache 2.0 | High for retrieval tuning | Not verified | 16 CVEs, 5 Critical | A retrieval engine to sit alongside a builder; Go rewrite at rc1 (29 Sep 2026) |
| **FastGPT** | Apache 2.0 plus conditions like Dify's ([LICENSE](https://github.com/labring/FastGPT/blob/main/LICENSE)) | Medium | Commercial edition | 33 CVEs, 6 Critical | No licence gain over Dify |
| **MaxKB** | GPL-3.0 | Medium | Paid X-Pack | 45 CVEs; 8 or more sandbox bypasses | Not recommended |
| **Coze Studio** | Apache 2.0 | Medium to high at source level | Not documented | 2 High CVEs (Sep 2026), possibly unpatched; last push 29 Jul 2026 | Stalling |
| **Flowise** | Apache 2.0 plus a commercial directory | Frozen | Enterprise only | 99 advisories, 26 Critical; no upstream patches | **Exclude** |
| **Open WebUI / AnythingLLM** | Branding clause above 50 users ([LICENSE](https://github.com/open-webui/open-webui/blob/main/LICENSE)) / MIT | Chat front ends, not builders | Open WebUI includes RBAC, LDAP and SCIM free | 1 Critical each | Candidate workspace front ends only |

### Agent-company orchestrators and code-first frameworks: Paperclip's job can be replicated

Paperclip's direct competitors fall into two groups.

**Open-source orchestrators of coding agents:**

- Gas Town, an alpha "multi-agent orchestration system for Claude Code, GitHub Copilot, and other AI agents" ([Gas Town](https://github.com/steveyegge/gastown));
- OpenAI Symphony, Apache 2.0, which turns "project work into isolated, autonomous implementation runs" ([Symphony](https://github.com/openai/symphony));
- Superset, under the Elastic License 2.0 ([LICENSE](https://github.com/superset-sh/superset/blob/main/LICENSE.md));
- Vibe Kanban and ruflo.

**Hosted vendor control planes:**

- GitHub Agent HQ's Mission Control ([GitHub blog](https://github.blog/news-insights/company-news/welcome-home-agents/));
- Claude Managed Agents, in beta since April 2026 ([Anthropic](https://claude.com/blog/claude-managed-agents));
- OpenAI Frontier, which has no confirmed GA.

The "AI software company" metaphor predates Paperclip. Both of its 2023 pioneers have moved away from it: MetaGPT last released on PyPI in March 2025 ([PyPI](https://pypi.org/project/metagpt/)), and ChatDev 2.0 is now a zero-code workflow platform.

Below these sit the frameworks from which a Paperclip-like layer could be built:

- **Microsoft Agent Framework:** 1.0, with long-term support, and human-in-the-loop approval across all patterns.
- **Google ADK:** version 2.0 reached GA on 19 May 2026 ([ADK 2.0](https://adk.dev/2.0/)).
- **LangGraph:** MIT, but self-hosted LangSmith needs an Enterprise plan ([LangSmith self-host](https://docs.langchain.com/langsmith/deploy-to-self-hosted-overview)), and a remote-code-execution flaw in checkpoint deserialisation was fixed in `langgraph-checkpoint` 3.0 ([advisory](https://advisories.gitlab.com/pkg/pypi/langgraph-checkpoint/CVE-2025-64439/)).
- **Strands:** lists token budgets as a lifecycle control and has "no hosted control plane" ([Strands](https://github.com/strands-agents/harness-sdk)).
- **Agno:** the closest buildable substitute. Under Apache 2.0 it ships a self-hosted AgentOS runtime and UI with RBAC, approvals, audit logs and scheduling, though it sends telemetry by default ([Agno](https://github.com/agno-agi/agno)).

Two licences need watching. Mastra's enterprise features prohibit production use without a commercial licence ([Mastra EE licence](https://github.com/mastra-ai/mastra/blob/main/ee/LICENSE)). The Claude Agent SDK is governed by Anthropic's Commercial Terms ([Agent SDK](https://code.claude.com/docs/en/agent-sdk/overview)).

The 2026 security pattern across this family is "approval or sandbox bypassed by prompt injection". CrewAI's four CVEs under CERT/CC VU#221883 allowed sandbox escape through prompt injection, and no complete patch existed as at 20 May 2026 ([CERT/CC](https://kb.cert.org/vuls/id/221883)). OpenClaw, the first runtime Paperclip lists, has a run of approval-bypass CVEs, although these are reported only by secondary aggregators ([CVE list](https://cve-dev.imfht.com/vendor/OpenClaw?lang=en)).

[I] An orchestrator's governance is only as strong as the enforcement in the weakest runtime it wakes. Paperclip's abstraction is therefore **differentiated in packaging, not in technology**. What it offers is speed to an operating model and vendor-neutral adapters. It does not offer capabilities that could not be rebuilt on Agent Framework or Agno behind A2A and MCP.

| Product (re-check 12 Dec 2026) | Job compared with Paperclip | Licence | Self-hostable control plane | Maturity signal |
|---|---|---|---|---|
| Gas Town | Direct (coding only) | MIT | Yes | Alpha (Jan 2026) |
| OpenAI Symphony | Direct (coding, centred on Codex) | Apache 2.0 | Yes | 27.6k stars; created Feb 2026 |
| Superset | Direct (coding) | ELv2 (not OSI) | Desktop IDE | 15.1k stars |
| GitHub Agent HQ | Direct for software organisations | Proprietary | No | Announced Oct 2025 |
| Claude Managed Agents | Hosted fleet, Claude only | Proprietary | Sandboxes only | Beta; multi-agent in research preview |
| CrewAI + AMP | Partial (agents run inside CrewAI) | MIT core; AMP commercial | Paid | CERT advisory 2026 |
| Agno (AgentOS) | Closest buildable substitute | Apache 2.0 | **Yes** (runtime and UI) | 42.7k stars; v3.1 |
| Microsoft Agent Framework | Building block | MIT | Yes | **1.0 GA, long-term support** |
| LangGraph | Building block | MIT; LangSmith commercial | Enterprise only | v1.2.x |
| Google ADK | Building block | Apache 2.0 | Yes | 2.0 GA (May 2026) |
| OpenAI Agents SDK / Claude Agent SDK | Building block | MIT / Anthropic Commercial Terms | Yes (in-process) | Both still 0.x ([PyPI](https://pypi.org/project/openai-agents/)) |

### Hyperscaler and enterprise platforms: AgentCore is the only like-for-like Foundry peer

**AWS Bedrock AgentCore** is the most customisable managed option documented ([AgentCore overview](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/what-is-bedrock-agentcore.html)):

- it runs "any open-source framework" and "any foundation model in or outside of Amazon Bedrock";
- its Policy service, GA since March 2026, uses a Cedar-compatible language and intercepts "every tool call before execution";
- it emits OpenTelemetry;
- it accepts any identity provider, including Entra ID.

AgentCore is strong on Australian residency. Every AgentCore feature is available in Sydney ([AgentCore regions](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/agentcore-regions.html)). Claude Sonnet 5.5 and Opus 5.5 can be called through `au.` geographic profiles that route only between Sydney and Melbourne ([Opus 5.5 model card](https://docs.aws.amazon.com/bedrock/latest/userguide/model-card-anthropic-claude-opus-5-5.html)). **AgentCore was IRAP-assessed at PROTECTED** in an assessment completed in June 2026 ([AWS Security Blog](https://aws.amazon.com/blogs/security/2026-phase-1a-irap-report-is-now-available-on-aws-artifact-for-australian-customers/)).

Its weaknesses are just as concrete:

- It is not offered in Melbourne, so there is no Australian disaster-recovery pair.
- OpenAI models reach Australia only through global profiles.
- The documentation says "AgentCore may use and store your content to improve your service experience".

**Google's Gemini Enterprise Agent Platform** (formerly Vertex AI) is AgentCore's technical peer, but it fails Australian residency today. Agent Runtime is listed in Melbourne only, Memory Bank is unavailable there, and partner models such as Claude have no Australian processing column ([agent locations](https://docs.cloud.google.com/gemini-enterprise-agent-platform/resources/agent-locations); [data residency](https://docs.cloud.google.com/gemini-enterprise-agent-platform/resources/data-residency)). Re-assess it in three to six months.

The SaaS-suite agents are best treated as A2A peers, not hubs:

- **Copilot Studio** is included for Microsoft 365 Copilot users' internal agents, and otherwise costs US$200 per 25,000 credits ([pricing](https://www.microsoft.com/en-us/microsoft-365-copilot/pricing/copilot-studio)).
- **Agentforce** costs AUD 0.14 per standard action ([pricing](https://www.salesforce.com/agentforce/pricing/)).
- **ServiceNow** delegates in both directions over A2A ([Action Fabric](https://www.servicenow.com/platform/action-fabric.html)).

This repeats the 28 September draft's principle that no SaaS agent platform should be the hub.

The model-vendor platforms are either churning or restricted. OpenAI's Agent Builder shuts down on **30 Nov 2026** ([OpenAI](https://developers.openai.com/api/docs/guides/agent-builder)). Anthropic's first-party API offers only `global` or `us` inference, and Managed Agents is "not currently eligible for Zero Data Retention" ([Anthropic data residency](https://platform.claude.com/docs/en/manage-claude/data-residency); [Managed Agents](https://platform.claude.com/docs/en/managed-agents/overview)).

| Platform (re-check 12 Jan 2027) | Bring your own framework or model | Australian runtime | Australian model processing | Assurance | Lock-in |
|---|---|---|---|---|---|
| **AWS AgentCore** | Any framework, any model, own containers | Sydney, all features; no Melbourne | Claude 5.5 through `au.` (Sydney↔Melbourne); OpenAI global only | IRAP-assessed PROTECTED (Jun 2026) | Low for the runtime; moderate for adjuncts |
| **Microsoft Foundry** | Python and C# containers; large catalogue | Australia East only | Older GPT pay-per-token; GPT-5 to GPT-5.4 on Regional PTU; no Claude | ISO/IEC 42001 certification stated for Foundry Models; Azure OpenAI IRAP-assessed (2024) | Moderate to high |
| **Google Agent Platform** | ADK, custom containers, 200+ models | Melbourne only; no Memory Bank | Gemini per model (unverified); no Claude | Google Cloud "strongly aligned" with PROTECTED; product scope not verified | Low to moderate |
| **Copilot Studio** | Low-code | Australia among the generative-AI regions | Depends on the cross-region data-movement setting | Not researched | High |
| **Salesforce Agentforce** | Low | Not verified | Not verified | PROTECTED-level IRAP assessment (Jun 2025) ([Salesforce](https://www.salesforce.com/au/news/stories/irap-assessment-agentforce-platform-2025/)) | High |
| **ServiceNow** | Low | IRAP-Protected data centres restrict AI features | Not verified | As noted | High |
| **IBM watsonx Orchestrate** | Moderate; on-premises option | Sydney in catalogue | Not verified | Not verified | Moderate |
| **Databricks Agent Bricks** | Data-platform-centric | Workspace geography | ANZ only with cross-geography processing ([Databricks](https://docs.databricks.com/aws/resources/designated-services)) | Not researched | Moderate to high |
| **OpenAI / Anthropic platforms** | Vendor-centred | Not confirmed / workspace geography `us` only | Not confirmed / `us` or `global` only | Not verified | High / moderate |

## Australian law sets the gates, and inference location is the binding constraint

The owner confirmed on 12 Oct 2026 that **RSGx is Australian and Australia is the governing jurisdiction**. The confirmation was relayed during the drafting session. Under the repository's rules, only a person records a confirmation, so the owner should record it in the bundle; until then, this report treats it as the owner's instruction. As a result, Australian law and residency are the basis for gate G4 and for every residency comparison in this report. The Malaysian material is confined to the section on the 28 September draft.

**No AI-specific statute binds a private engineering firm in Australia, so the Privacy Act is the practical law.**

- **Voluntary guidance.** The voluntary Guidance for AI Adoption sets out six practices aligned to ISO/IEC 42001 ([industry.gov.au](https://www.industry.gov.au/publications/guidance-for-ai-adoption)). The government chose not to proceed with mandatory guardrails ([consultation](https://consult.industry.gov.au/ai-regulatory-guardrails)).
- **The ADM transparency duty (APP 1.7–1.9) commences on 10 Dec 2026, about eight weeks from now** ([OAIC fact sheet](https://www.oaic.gov.au/__data/assets/pdf_file/0021/269013/APP-1.7-1.9-Transparency-Obligation-Fact-Sheet.PDF)). The OAIC reads it broadly. "Arranged for" includes procuring or configuring third-party software and relying on advisory outputs. Human review is not an exemption. Generative-AI outputs used in decisions that significantly affect individuals are in scope "unless subject to extensive human oversight and control".
- **Approval design becomes a privacy control.** The approval step must record who approved and why, not just that someone clicked. [I] Likely in-scope RSGx uses include HR screening, subcontractor prequalification and triage of safety incidents that name individuals.
- **Other privacy exposure.** The statutory tort for serious invasions of privacy has been in force since 10 Jun 2025 ([QLS Proctor](https://www.qlsproctor.com.au/2025/08/new-tort-serious-invasions-of-privacy/)). The Tranche 2 reforms remain an exposure draft, with consultation closed on 18 Sep 2026 ([HSF Kramer](https://www.hsfkramer.com/insights/2026-09/the-draft-tranche-2-privacy-act-reforms-whats-there-whats-new-and-whats-missing)).
- **APP 8 is unresolved for offshore inference.** It turns on whether personal information leaves RSGx's "effective control", and s16C keeps RSGx accountable for an overseas recipient ([APP 8 guidelines](https://www.oaic.gov.au/agencies-and-organisations/app-guidelines/chapter-8-app-8-cross-border-disclosure-of-personal-information)). The OAIC has not said whether sending prompts to a model endpoint outside Australia is a "use" or a "disclosure". The conservative course is to prefer Australian-region inference for personal-information workloads and to get counsel's view before go-live.

**Security expectations come from the ISM, and they reach RSGx by contract.** The September 2026 Information Security Manual treats agents as principals in their own right. It requires:

- a unique agent identity (ISM-2133);
- a verified agent register (ISM-2134/2135);
- effective permission equal to the minimum of the user's rights and a task-scoped grant (ISM-2156/2157);
- untrusted handling of retrieved content (ISM-2158);
- central logging of tool calls (ISM-2159);
- human approval before sensitive actions (ISM-2113).

These control IDs come from a consultancy summary and must be checked against the official changes document ([Cipher Projects](https://www.cipherprojects.com/blog/posts/asd-ism-september-2026-update/)). The ISM binds a private firm only through government, defence or critical-infrastructure contracts. Even so, it is the clearest Australian statement of good practice, and it is directly testable. The May 2026 Five Eyes guide *Careful Adoption of Agentic AI Services* points the same way ([A&O Shearman](https://www.aoshearman.com/en/insights/ao-shearman-on-data/cisa-and-asds-acsc-publish-joint-guidance-on-securing-agentic-ai-systems)).

The Essential Eight is still the November 2023 model. Its 48-hour clock for patching critical vulnerabilities becomes RSGx's own burden for anything it self-hosts ([iTWire](https://itwire.com/business-it-news/security/essential-eight-maturity-model-what-applies-now-and-what-asd-is-changing)). IRAP assessors "do not accredit, certify, endorse or register systems" ([cyber.gov.au](https://www.cyber.gov.au/business-government/protecting-devices-systems/assessment-evaluation-programs/irap)). The Forum should therefore ask for each vendor's IRAP report scope and date, not accept the label.

The ISM itself leaves gaps: agent-to-agent authentication, MCP hardening, a revocation SLA and red-teaming of the agent. Customisability pays off there. Criterion C3 rewards a platform that lets RSGx insert its own controls to close them.

**Residency has three layers, and only the first is easy.**

1. Where agent state, memory, logs and traces are stored.
2. Where inference runs for the exact models RSGx intends to use.
3. Which sub-processors handle the data, and who can be compelled to produce it.

The Australia–US CLOUD Act agreement has been in force since 31 Jan 2024 ([Senator Ciccone](https://senatorciccone.com.au/committee-to-review-international-production-order-scheme-for-sharing-electronic-information/); [Covington](https://www.insideprivacy.com/international/u-s-and-australia-sign-cloud-act-agreement/)). An Australian region is therefore necessary for residency but not sufficient for sovereignty with any US-headquartered provider.

| Platform (as at 12 Oct 2026; re-check 12 Jan 2027) | State and storage in Australia | Inference in Australia for current models | Caveats | G4 (desk) |
|---|---|---|---|---|
| **AWS AgentCore + Bedrock** | Sydney, all AgentCore features except the Web Search tool | Claude Sonnet 5.5 and Opus 5.5 through `au.` profiles (Sydney↔Melbourne); Opus 5.5 also in-region in Melbourne on the `bedrock-mantle` endpoint, which lacks Guardrails, Knowledge Bases, Agents and Flows | No Melbourne AgentCore. Cross-region destinations for Memory and Policy from Sydney unverified (APAC or Australia only?). IRAP scope excludes "Amazon Bedrock Marketplace", yet Claude 5.5 is billed through AWS Marketplace. AWS says to verify destinations with GetInferenceProfile from each source region ([inference profiles](https://docs.aws.amazon.com/bedrock/latest/userguide/inference-profiles-support.html)) | **Pass for Claude 5.5**; fail for OpenAI models |
| **Microsoft Foundry** | Australia East, with state in RSGx's own resources under Standard setup | gpt-4.1-mini, gpt-4o and embeddings pay-per-token; GPT-5 to GPT-5.4 on Regional PTU; newer models on APAC Data Zone; **no Claude in Australia** | No second Australian region; Computer Use unavailable; APAC Data Zone membership can change without notice | Conditional |
| **Google Agent Platform** | Melbourne only; no Memory Bank; Sydney not listed | Gemini per model unverified; no Claude | The current Gemini Enterprise page lists no Australian location; an older page did ([locations](https://docs.cloud.google.com/gemini/enterprise/docs/locations)) | Fail |
| **Anthropic first-party (Claude Enterprise, Managed Agents)** | Workspace geography `us` only | `global` or `us` only | A marketing FAQ claims Australian residency, which the API docs do not support | Fail for personal information |
| **Microsoft 365 Copilot / Copilot Studio** | Australia has a Product Terms residency commitment for Copilot data at rest ([M365 data residency](https://learn.microsoft.com/en-us/microsoft-365/enterprise/m365-dr-compare-offerings?view=o365-worldwide)) | In-country Copilot inferencing "expected" in Australia by end of 2026 ([Microsoft](https://www.microsoft.com/en-us/copilot/blog/2025/11/04/microsoft-offers-in-country-data-processing-to-15-countries-to-strengthen-sovereign-controls-for-microsoft-365-copilot/)) | Copilot Studio's cross-region data-movement setting can move prompts offshore | Conditional |
| **Self-hosted Dify or Paperclip** | Wherever RSGx hosts it (an Australian region) | Only as resident as the endpoint called (for example Bedrock `au.` or Foundry Australia East) | Paperclip telemetry goes to the US by default; Dify Cloud is US-hosted | Conditional |

The table points to one conclusion. Today, **AWS's `au.` route is the only verified Australia-resident path for current Claude models.** Foundry can keep agent data in Australia, but personal-information inference there must use older GPT models, reserved Regional PTU or the multi-country APAC Data Zone, and the last of these needs an APP 8 analysis. Self-hosting Dify or Paperclip controls storage, not inference.

[I] The cheapest control is a data-class gate in front of every model endpoint. Engineering content with no personal information can use broader endpoints, subject to client contracts. Personal information stays on Australian-resident inference.

**Open questions for the owner.** Five questions bear directly on the runtime choice:

1. Is RSGx's identity estate Microsoft 365 and Entra? This is evidence gap 1 in the existing open question, and it largely decides between Foundry and AgentCore.
2. Has RSGx confirmed that it is an APP entity? The small-business exemption threshold was not verified.
3. Do any government, defence or critical-infrastructure clients pass ISM, IRAP or SOCI obligations down to RSGx?
4. Which RSGx uses fall under the ADM transparency duty from 10 Dec 2026?
5. Does RSGx have clients or staff in Malaysia, or elsewhere offshore, whose personal data its agents would process? This last question is a separate open question, covered in the section on the 28 September draft below. It is not a premise of this report.

## Six gates and a 100-point rubric turn preferences into evidence

The programme has no ratified evaluation framework, so the criteria below are themselves a proposal [P]. **Stage 1 is a set of six must-pass gates.** They are drawn from the ISM's September 2026 agent controls, the OAIC's ADM guidance and APP 8. A candidate that fails a gate is out unless the Forum funds a compensating control, with a named owner and a stated cost. **Stage 2 is a 100-point weighted score.**

| Gate | Pass test (evidence to demand in a proof of concept) |
|---|---|
| **G1** Distinct non-human identity per agent | Two agents run under separate identities that can be revoked independently, with no shared service account (ISM-2133; OWASP ASI03). |
| **G2** Enforced human approval before sensitive actions | A tool call *cannot run* until a named person approves it, and the approver's identity, time and rationale are logged (ISM-2113; OAIC's "extensive human oversight" test for ADM). |
| **G3** Central, exportable audit trail | A full trace (invoker, agent identity, tool, arguments, output, approval) is exported to RSGx's SIEM in an open format and cannot be deleted at source (ISM-2159; ISO/IEC 42001 A.6). |
| **G4** Australian processing path for personal information and client-confidential data | Storage *and* inference for the intended models are pinned to Australian regions with no global or Data Zone fallback, supported by a sub-processor list. Otherwise, a documented APP 8 analysis and an exception approved by the owner. |
| **G5** Licence permits the intended pattern | A written vendor or legal position covering multi-workspace use, any client-facing use and branding. |
| **G6** Credible security maintenance | A published disclosure policy, a record of how long fixes take, and a supported upgrade path that lets RSGx meet the Essential Eight 48-hour clock for critical vulnerabilities. |

In the weighted rubric, customisability carries 35 points, which keeps it clearly the primary lens. It also adds a capability and architecture lens that the brief requires.

Each criterion is scored from 0 to 4:

- **0**: absent;
- **1**: possible only with a significant custom build;
- **2**: partial, or native with gaps;
- **3**: native and configurable;
- **4**: native, configurable and evidenced in a proof of concept.

The weighted score for a criterion is the score divided by 4, multiplied by the weight.

| Lens (weight) | ID | Criterion | Weight | Evidence to ask for |
|---|---|---|---|---|
| **Customisability (35)** | C1 | Agent and workflow extensibility: code-first SDK and visual builder; custom tools and nodes; ability to patch | 10 | Build one RSGx reference workflow (for example document-control triage); count the custom code and blocked features |
| | C2 | Model portability, including Australian-resident endpoints | 7 | Swap model provider in the proof of concept; list the Australian-resident models |
| | C3 | Policy-enforcement hooks: interceptors before and after tool calls, guardrails, approval nodes, kill switch | 8 | A policy written by RSGx blocks a tool call; an agent is disabled within an agreed time |
| | C4 | Open interoperability: MCP, A2A, OpenAPI, OpenTelemetry | 5 | Protocol versions supported; conformance demonstration |
| | C5 | Integration with the identity and data estate (IdP, document control, ERP) using delegated, scoped access | 5 | Connector list; OAuth scopes; admin-consent model |
| **Governance and security (25)** | S1 | Least privilege: task grant intersected with user rights; deny by default | 6 | Negative test: the agent attempts a tool outside its scope |
| | S2 | Defences against prompt injection and untrusted content; sandboxed execution | 5 | Red-team tests with a poisoned document and a poisoned memory (ASI01, ASI06) |
| | S3 | Agent register and inventory support (ISM-2134/2135) | 4 | An exportable register, or an API that populates RSGx's registry |
| | S4 | Evaluation, monitoring and red-team hooks | 4 | Evaluations, or OpenTelemetry export into RSGx tooling |
| | S5 | Data lifecycle: retention, no training on RSGx data, secrets, short-lived credentials | 4 | Data-flow diagram; a contractual no-training clause |
| | S6 | Assurance evidence: ISO/IEC 27001 and 42001 scope, IRAP report scope, SOC 2, SBOM | 2 | Certificates with scope statements; IRAP letter |
| **Capability and architecture (15)** | A1 | Fit to RSGx use cases (bid Q&A, EDMS retrieval, RFI drafting, multi-step agents) | 5 | Two use cases demonstrated end to end |
| | A2 | Multi-agent orchestration and durable execution (checkpointing, resuming after approval) | 4 | Kill and resume a long-running run |
| | A3 | Scalability and resilience, including disaster recovery within Australia | 3 | HA topology; disaster-recovery region |
| | A4 | Clean fit to one layer behind the RSGx control plane | 3 | Registers in the RSGx registry; traffic passes through the gateway |
| **Cost and licensing (10)** | K1 | Licence clarity and freedom | 3 | Licence text; legal opinion |
| | K2 | Three-year total cost of ownership, including operations staff, patching, penetration tests and residency premiums | 4 | Costed model |
| | K3 | Cost controls: per-agent budgets and quotas | 3 | Demonstrate a per-agent cap |
| **Deployment and lock-in (15)** | D1 | Australian residency and sovereignty depth beyond G4 | 6 | Feature-by-region matrix; sub-processor list |
| | D2 | Exit and portability in open formats | 5 | Export one agent and its history; re-import it elsewhere |
| | D3 | Viability of the project or vendor | 4 | Release history, maintainers, funding |

### Indicative desk outcome [P]

The tables below apply the gates and the rubric to five candidates, **from documentation only**. Because no criterion has been evidenced in a proof of concept, no score exceeds 3.5. The numbers show the shape of the field and how sensitive it is to the weights. They are not a basis for a decision, and they should be replaced with proof-of-concept evidence.

| Gate (desk view) | Paperclip | Dify Community | Microsoft Foundry | AWS AgentCore | Google Agent Platform |
|---|---|---|---|---|---|
| G1 Identity | Partial: per-agent run tokens inside Paperclip, but harness CLIs run as the server's OS user | Likely fail [I]: no per-agent identity found | Pass: a dedicated Entra identity per hosted agent (Entra protections need Agent 365 seats) | Likely pass: AgentCore Identity (per-agent identity not re-verified) | Likely pass: "unique identity per agent" (GA status unconfirmed) |
| G2 Approval | Partial: one approver; agents may approve; harness tools bypass the gateway | Partial: a human-input node exists; hard gating not verified | Pass: MCP approvals and Agent Framework HITL; agent guardrails in preview | Partial: Policy allows or denies every Gateway tool call deterministically; a human-approval step was not verified | Not verified |
| G3 Audit | **Fail as shipped**: deleting an agent deletes its history | Partial: OTLP export and operation logs are Enterprise-only | Pass: OpenTelemetry and Purview audit | Pass, but logs for Memory, Policy and Evaluations do not name the inference region | Likely pass |
| G4 Australian processing | Conditional on the model endpoint; disable telemetry | Conditional on the model endpoint | Conditional: in-country only for older GPT models or Regional PTU; Claude fails | **Pass for Claude 5.5** through `au.`; fails for OpenAI models | **Fail** |
| G5 Licence | Pass (MIT) | Conditional: multi-workspace use needs LangGenius's written position | Pass, subject to review of the Claude terms and the CSP exclusion | Pass, subject to review of the "may use and store your content" clause | Pass, subject to contract review |
| G6 Maintenance | **Fail as shipped**: no supported versions or response time; five Critical advisories | Conditional: no SLA or long-term-support line; no Critical advisories | Pass (vendor-managed); adopt a GA-only rule | Pass | Pass |

On customisability, the desk scores for each criterion (0–4) are as follows.

| Criterion (weight) | Paperclip | Dify Community | Foundry | AgentCore | Google |
|---|---|---|---|---|---|
| C1 Extensibility (10) | 2.5 | 3 | 3 | 2.5 | 3 |
| C2 Model portability (7) | 2.5 | 3 | 2 | 3 | 3 |
| C3 Policy hooks (8) | 2 | 2 | 2.5 | 3.5 | 2.5 |
| C4 Interoperability (5) | 2 | 2 | 3.5 | 3.5 | 3 |
| C5 Identity and data estate (5) | 1 | 1.5 | 3.5 | 2.5 | 2 |
| **Customisability total (of 35)** | **18.4** | **21.1** | **24.8** | **26.0** | **24.0** |

Applying the other lenses gives the totals below. Governance and security is scored as a whole lens: Paperclip 1, Dify 1.5, Foundry 3, AgentCore 3, Google 2.5. Deployment and lock-in is scored against Australian residency.

| Candidate | Customisability (35) | Governance and security (25) | Capability and architecture (15) | Cost and licensing (10) | Deployment and lock-in (15) | **Total** | Governance-led weights 25/30/15/10/20 | Customisability only |
|---|---|---|---|---|---|---|---|---|
| AWS AgentCore | 26.0 | 18.8 | 10.3 | 6.3 | 10.6 | **71.9** | 71.7 | 74.3 |
| Microsoft Foundry | 24.8 | 18.8 | 10.9 | 5.4 | 8.5 | **68.3** | 67.8 | 70.7 |
| Google Agent Platform | 24.0 | 15.6 | 10.1 | 5.4 | 7.6 | **62.8** | 61.6 | 68.6 |
| Dify Community | 21.1 | 9.4 | 9.5 | 3.9 | 8.5 | **52.4** | 51.1 | 60.4 |
| Paperclip | 18.4 | 6.3 | 6.6 | 6.8 | 7.8 | **45.8** | 44.3 | 52.5 |

Three readings follow.

**The ranking holds under every weighting tested, including customisability alone.** This challenges the assumption that weighting customisability favours open source. The criteria that matter most to a governed programme are policy hooks, open interoperability and identity integration, and the hyperscalers do those better. For Paperclip to win, the Forum would have to narrow "customisability" to agent extensibility, model portability and licence freedom. On those three alone, Paperclip scores about 0.75 of the maximum, against about 0.67 for AgentCore and 0.63 for Foundry and Dify. In effect, the Forum would have to value the right to modify above the ability to govern.

**Residency and policy, not features, separate the two leading runtimes.** AgentCore's lead of about 3.6 points comes mostly from Australian residency (D1, about 2 points, through the `au.` Claude path) and deterministic policy (C3, about 2 points). Foundry leads on identity and data-estate integration and on capability. [I] If RSGx turns out to run on Microsoft 365 and Entra, and GPT-family models are acceptable for personal-information workloads, Foundry's integration advantage could close the gap. That is exactly what a short proof of concept should settle.

**Dify Enterprise would score materially higher than Community.** [I] Adding SSO, RBAC, audit, high availability and a licence that authorises multiple workspaces would put Dify at roughly 62, at a price that is not published. Enterprise, not Community, is the real comparator if Dify is wanted at scale. Google fails gate G4, so it remains a watch item whatever its points.

## Proposal [P]: decide by layer, with the runtime chosen against Australian evidence

This is Claude's proposal, not a decision. It redefines the existing Option B from "AgentCore in the Malaysia region" to "AgentCore in Sydney", which changes the meaning of the A/B framing. Under the repository's "stop and ask" rule, the owner must see it before it goes to the Forum.

| Layer | Proposal [P] | Conditions before it could become a decision |
|---|---|---|
| **RSGx-owned control plane** | Keep the 28 September pattern: gateway, registry, enterprise identity and OpenTelemetry. Neither Paperclip nor Foundry's preview Control Plane substitutes for it. | Every agent, including Dify apps and any agents Paperclip manages, registers in the RSGx registry. The ContextForge security review remains open. |
| **Runtime** | Choose between **Option A, Foundry in Australia East**, and **Option B, AgentCore in Sydney**. On current desk evidence, AgentCore is stronger for Australian residency of Claude and holds an IRAP PROTECTED assessment for the runtime itself. Foundry is stronger if RSGx's estate is Microsoft 365 and Entra and GPT-family models are acceptable for personal-information workloads. Keep Google as a watch item; re-assess it when it offers a Sydney runtime and Australian processing for Claude. | The owner confirms the identity estate. Vendors confirm Australian facts in writing: AgentCore's cross-region destinations for Memory and Policy from Sydney; the Bedrock Marketplace IRAP exclusion as it applies to Claude; Foundry's Australia East model list and PTU minimums. Counsel gives a view on APP 8 for offshore inference. A one-to-two-week proof of concept tests G1–G6, as Microsoft's own CAF advises ([CAF](https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/ai-agents/technology-solutions-plan-strategy)). |
| **Builder** | Confirm Dify only for departmental solutions at autonomy level L1–L2: self-hosted in an Australian region with one workspace per instance, or Enterprise if several workspaces are needed. Test n8n (internal use only), Sim and Activepieces in the same proof of concept. Exclude Flowise. Confine Langflow to developer sandboxes. | A written position from LangGenius on internal multi-workspace use. Compensating controls: SSO through a reverse proxy, rotation of default secrets, egress control, marketplace off with signed packages only, and log shipping to the SIEM. |
| **Agent-company orchestration** | Do not adopt Paperclip for production, personal information or client data. At most, allow an isolated evaluation on non-sensitive coding work. Re-assess against G3 and G6 in April 2027. | Authenticated mode behind an IdP proxy; restrictive harness modes; a sandbox provider; telemetry off; the activity log streamed to an append-only SIEM; a plugin allow-list; pinned versions. |
| **Workspace** | No change to the existing [P]: Claude Enterprise as the workspace for L1–L2 solutions, but limited by data class, because Anthropic's first-party inference is `global` or `us` only. | Re-check the "MCP-only, no native A2A" finding by its 31 Dec 2026 date. Decide which data classes may enter Claude Enterprise before the ADM duty starts on 10 Dec 2026. |
| **28 September draft concepts** | The owner revises or supersedes the draft reference, and the Option B definition and "Malaysia-region facts" evidence gap in the linked assessment and open question (see the next section). | The owner decides. Under the repository's rules, a merged concept is never renamed, deleted or silently edited. A replacement is created, and the old concept is set to `deprecated` with `superseded_by` and a log entry. |

The reasoning is brief. The gates already rule out Paperclip as shipped and leave Dify conditional. Between Foundry and AgentCore, the evidence splits on two unrecorded facts: the identity estate, and whether GPT-family models are acceptable for personal information. Features cannot settle that, but a proof of concept can.

The Forum can act now. The existing open question records that the control-plane pattern is "Blocked by: nothing" and can be adopted while the runtime evidence arrives. **Blocker PR-17** (the ISMS baseline) still gates L3 pilots whichever runtime is chosen. Nothing in this report brings L3 or L4 autonomy forward.

## The 28 September draft survives in architecture but not in its Malaysian framing

### The Malaysian framing does not fit an Australian organisation, and parts of it are wrong

The draft proposal is `bundles/rsgx-ai-programme/references/agent-platform-report-2026-09-28.md` ([P], stale after 1 Mar 2027). It frames residency entirely around Malaysia:

- its control mapping cites "Malaysia PDPA (as amended 2024)" and says to "Pin runtimes to Malaysia/Singapore regions" (line 154);
- it defines Option B as "AWS Bedrock AgentCore in Asia Pacific (Malaysia)" (lines 28 and 250);
- it proposes a "residency/feature proof-of-concept in the Malaysia region" (line 257).

For an Australian organisation this framing misses the obligations that actually apply: APP 8, the ADM duty, the ISM agent controls and IRAP. The repository mentions none of them.

The draft's Malaysian facts are also wrong in places. As at 12 Oct 2026, primary sources show the following ([Foundry region support](https://learn.microsoft.com/en-us/azure/foundry/reference/region-support); [AgentCore regions](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/agentcore-regions.html); [AgentCore cross-region inference](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/cross-region-inference.html); [Bedrock regional availability](https://docs.aws.amazon.com/bedrock/latest/userguide/models-region-compatibility.html); [AWS announcement](https://aws.amazon.com/about-aws/whats-new/2026/06/amazon-bedrock-agentcore-four-additional-regions/)):

- **Foundry in Malaysia.** "Microsoft Foundry or AWS Bedrock AgentCore in the Malaysia region" (line 23) is not possible for Foundry. Azure Malaysia West is absent from Foundry's project, Agent Service and model deployment tables.
- **AgentCore as the in-country option.** Calling AgentCore Malaysia "the strongest confirmed in-country option" (line 158) holds only for hosting. Every current Claude and GPT model is reachable from Malaysia only through global cross-region inference. AgentCore Memory is not offered there, and Policy and Evaluations route their inference globally.
- **AgentCore launch date.** The AgentCore Malaysia launch, given as "June 2026" (lines 37, 123 and 158), was posted on 1 Jul 2026.
- **Singapore features.** The claim that "Singapore lacked Evaluations and Policy" is outdated.
- **Google's ranking.** The draft ranked Google lower because of Malaysian residency (line 251). Google has no Malaysian region at all, but it does commit in-country ML processing in Singapore for nine current Claude models ([Google data residency](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/learn/data-residency)).

**Proposal [P]: the owner should revise or supersede the draft reference.** The same applies to the linked assessment (`assessments/agent-platform-recommendation.md`, Option B) and to the open question (`open-questions/agent-platform-selection.md`, evidence gap 2, "Malaysia-region facts, in writing from the vendor"). Supersession should follow the repository's rules, with nothing edited silently. The draft's own residency section declares a shelf life of three to six months, so it is stale from 28 Dec 2026 at the latest regardless.

**Malaysian facts still matter in one case, which is an open question, not a premise: does RSGx have clients, staff or operations in Malaysia whose personal data its agents would process?** If it does, Malaysia's PDPA as amended would apply to that data. Cross-border transfers would need a transfer impact assessment for each named country, or s129(3) contractual clauses, with records kept per receiver and per country ([CBPDT Guideline](https://www.pdp.gov.my/ppdpv1/wp-content/uploads/2025/08/GP_CBPDT_EN-1.pdf)). The April 2026 guidelines on automated decision-making and DPIAs name AI explicitly ([ADMP](https://www.pdp.gov.my/ppdpv1/wp-content/uploads/2026/04/Automated-Decision-Making-And-Profiling-Guideline-ADMP.pdf)). No hyperscaler offers in-country model inference in Malaysia today, and Singapore is the practical fallback. The suggested re-check date for these Malaysian facts is 12 Jan 2027.

### What the evidence confirms, corrects and extends in the rest of the draft

| Draft position (line) | Verdict | What the new evidence shows |
|---|---|---|
| "Allow Dify or n8n (self-hosted) only for L1–L2 departmental automation" (252) | **Confirms, with conditions** | Licence that treats each workspace as a tenant; governance only in Enterprise; cross-tenant advisories in Jul–Aug 2026; Dify Agent in beta. n8n's fair-code licence confirmed for internal use. |
| Dify licence: "check multi-tenant terms" (99) | **Extends** | Exact terms are quoted above. Not an OSI licence. Six revisions, each broadening or clarifying. |
| Dify A2A through a community Nacos plugin, v0.0.4 (99) | **Not re-verified** | No A2A found in Dify's core. The plugin's status is unknown. |
| Paperclip: absent from the repository | **Extends** | Newly assessed as an agent-company control plane. Fails G3 and G6 as shipped. |
| Control-plane pattern; "MCP inward, A2A sideways" (225–229, 247) | **Confirms** | MCP and A2A both sit in the AAIF; A2A joined on 17 Aug 2026 ([AAIF](https://aaif.io/blog/a2a-joins-aaif)). Paperclip lacks A2A, so it cannot be a peer under this rule without a gateway. |
| Foundry A2A v1.0 GA; hosted agents reach A2A through an MCP Toolbox (121) | **Confirms and clarifies** | Hosted agents expose A2A v1.0 endpoints directly. Outbound calls to other agents still go through the Toolbox. |
| Option A: "Claude models available"; ISO/IEC 42001 certification for Microsoft services (249) | **Extends, with caveats** | Claude in Foundry is processed by Anthropic, Global or US Data Zone only, with no Australian processing, and CSP subscriptions cannot buy it. The 42001 certification is stated for Foundry Models; it was not verified for Agent Service. |
| Option B as the residency-strong runtime (250) | **Corrects the location, keeps the logic** | AgentCore's residency strength is real in **Sydney** (all features, `au.` Claude, IRAP-assessed PROTECTED), not in Malaysia. |
| "No pricing was verified" (263) | **Extends** | List prices are now available for Foundry, AgentCore, Dify Cloud and the SaaS suites. Quotes are still needed. |
| Standardise on Agent Framework or LangGraph (252) | **Confirms** | Agent Framework 1.0 is GA with long-term support. Foundry Workflows retire on 1 Dec 2026, which favours code over portal features. |
| UI gap: no vendor provides a cross-runtime Forum view (UI-gap assessment) | **Qualifies** | Foundry Control Plane (preview) claims an inventory of non-Microsoft agents, and AgentCore Registry catalogues agents "on any other Cloud". Neither is GA evidence yet. |
| Least agency attributed to OWASP | **Conflict** | Not found in the OWASP summary consulted. Verify against the OWASP text ([OWASP](https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/)). |
| Plan phased with time-bound horizon labels (256–259) | **Already flagged** | Use Phase 1–3, or Enablement, Automation and Reinvention held per function. |

## Conflicts, unverified items and claims due for re-check before 10 January 2027

The Forum should not rely on the following items until they are resolved.

| Item | Conflict or gap | Why it matters |
|---|---|---|
| Governing jurisdiction | Confirmed as Australia by the owner on 12 Oct 2026, relayed in session. The bundle still frames Malaysia. | The owner should record the confirmation; Claude cannot |
| Paperclip SSO and GRC | The README lists "SSO, GRC"; the self-hosted code has email and password only and no GRC feature | Identity and assurance scores |
| Paperclip audit immutability | The website promises "no deletions"; the code hard-deletes the log with the agent | Gate G3 |
| GHSA-x8hx-rhr2-9rf7 | No patched version is listed. A host guard at HEAD suggests a fix, but this is unconfirmed. | Gate G6 |
| Paperclip legal entity | LICENSE says "2025 Paperclip AI"; README says "2026 Paperclip Labs, Inc" | Contracting |
| Dify compliance status | The March 2026 blog claims SOC 2 Type II and ISO 27001; the User Agreement still says "in the process"; scope unstated | Criterion S6 |
| Dify internal multi-workspace use | No statement from LangGenius | Gate G5 |
| Dify funding total | US$30M, US$34.3M or US$41.5M, depending on the source | Viability |
| Foundry IRAP scope | The 2026 announcement names no AI services; the Service Trust Portal was not accessed | Do not call Agent Service IRAP-assessed |
| Foundry catalogue size | 10,000+ (Learn) vs 11,000+ (pricing page) | Minor |
| Entra Agent ID GA date and Agent 365 price | Secondary sources only; the GA date is given as April or 1 May 2026 | Cost (K2) |
| AgentCore cross-region inference from Sydney | One summary says requests stay within the source geography; another lists Sydney in APAC-wide Memory and Policy routing | Gate G4: verify before enabling Memory or natural-language Policy |
| Bedrock IRAP scope | Bedrock is in scope "excludes Amazon Bedrock Marketplace", yet Claude 5.5 is billed through AWS Marketplace | **Needs the owner's attention** before any IRAP-dependent claim about Claude on Bedrock |
| Google Australian residency | An older Gemini Enterprise page listed Australia; the current page does not | Watch item |
| Anthropic Australian residency | A marketing FAQ claims residency including Australia; the API docs offer `global` or `us` only | Workspace data classes |
| ISM control IDs | Taken from a consultancy summary, not the official changes document | Gates G1–G3 |
| APP 8 and offshore inference | The OAIC has no position on whether inference is a "use" or a "disclosure" | Gate G4 |
| APP entity status | Small-business exemption threshold not verified | Scope of the Privacy Act duties |
| Essential Eight successor | One source says no retirement date has been set; another quotes a two-year retirement | Patch clock |
| A2A date of joining the AAIF | 17 Aug (AAIF, Axios) vs 20 Aug (secondary); the repository also records 27 Aug | Minor |

The following claims fall due for re-check **within 90 days of 12 Oct 2026**, that is, on or before 10 Jan 2027.

| Claim | As at | Re-check by |
|---|---|---|
| AgentCore Runtime v2 committed baseline "launching by October 2026"; AgentCore Memory pricing change effective 6 Oct 2026 | 12 Oct 2026 | 31 Oct 2026 |
| OpenAI Agent Builder shutdown on 30 Nov 2026 | 3 Jun 2026 notice | 1 Dec 2026 |
| Salesforce long-horizon agents GA "November 2026" | 28 Sep 2026 | 1 Dec 2026 |
| Foundry Workflows retirement on 1 Dec 2026 | 14 Aug 2026 page | 2 Dec 2026 |
| Privacy Act ADM transparency duty commencing 10 Dec 2026 (fixed by statute; check for OAIC guidance updates, and the "about eight weeks away" framing lapses on that date) | 30 Sep 2026 | 10 Dec 2026 |
| All Paperclip facts: version, stars (100,392), open issues (2,946), 12 advisories, no self-hosted SSO, Cloud waitlist only | 12 Oct 2026 | 12 Dec 2026 |
| All Dify facts: version 1.17.1, 21 advisories, licence text, Dify Agent in beta | 12 Oct 2026 | 12 Dec 2026 |
| Other open-source facts: n8n and Langflow advisories and KEV entries, Sim, Coze Studio patch status, Agno telemetry, framework versions | 12 Oct 2026 | 12 Dec 2026 |
| Google agent-location and Gemini Enterprise residency tables (updated 9 Oct 2026) | 12 Oct 2026 | 12 Dec 2026 |
| ISM September 2026 agent control IDs | 7 Sep 2026 summary | Immediately, and again at the December 2026 ISM release |
| Residency section of the 28 September draft (by its own stated shelf life of three to six months) | 28 Sep 2026 | 28 Dec 2026, by which date it should be revised or superseded |
| Repository finding that Claude Enterprise is MCP-only, with no native A2A | 24 Sep 2026 | 31 Dec 2026 (existing `stale_after`) |
| In-country Microsoft 365 Copilot inferencing in Australia, "expected" by the end of 2026 | 3 Apr 2026 note | 31 Dec 2026 |

Hyperscaler prices, regions and GA statuses, the Tranche 2 privacy reforms and the Essential Eight successor fall just outside this window, with a re-check on 12 Jan 2027. The programme's own platform concepts expire on 1 Mar 2027. If this report is filed into the bundle, it needs a `stale_after` of **2026-12-12**, the earliest date of any class of claim in it.

## Conclusion

This research changes what "customisable" should mean for RSGx. The useful definition is not "can we edit the source". It is "can we insert our own code, models and controls into a runtime that enforces them, and leave without a rewrite".

Rights to fork are cheap to obtain and expensive to use. Paperclip ships breaking changes about every fortnight. Dify reserves the right to tighten its licence and keeps its governance features in a paid edition. An open-source core does not make a platform governable; the most open product reviewed here currently has the weakest controls. The customisability a governance programme can rely on is where the 28 September draft already put it: code-first agents on portable frameworks, behind a control plane that RSGx owns.

The second shift is that, with Australia confirmed as the governing jurisdiction, the binding constraint is no longer where the runtime sits but where inference happens. In Australia only one route is verified as Australia-resident for current Claude models. The runtime decision is therefore partly a decision about which models may touch personal information, ahead of an ADM duty that starts in eight weeks.

The market keeps proving the case for portability. In 2026 alone, OpenAI is retiring Agent Builder, Foundry is retiring Workflows, and Workday archived Flowise within a year of buying it. The most valuable next step is not to pick a winner. It is to adopt the control-plane pattern, record the jurisdiction decision, retire the draft's Malaysian premise properly, and make the two remaining runtimes earn their gates in a short proof of concept.

[^s-1012]: Session 2026-10-12 — Paperclip, Dify, Microsoft Foundry and alternatives
[^page-1012]: Published page of this report (private artifact; the owner controls sharing)
