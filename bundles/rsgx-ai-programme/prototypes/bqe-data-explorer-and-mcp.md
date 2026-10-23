---
type: Prototype Candidate
title: "BQE CORE data explorer, admin console and MCP server on Azure [P]"
description: "Handoff plan for a build agent: a shared BQE CORE connector, an admin console that controls which data points are exposed, a visual query builder for users, and a read-only MCP server deployed on Azure."
tags: [prototype, bqe-core, integration, mcp, azure, data-access, handoff]
status: draft
provenance: P
owner: human:cchin
priority: "Phase 0 can start now. No build starts before the Phase 0 owner decisions and BQE app approval."
generated: { by: claude/claude-opus-5-5, at: 2026-10-23T04:00:00Z }
stale_after: 2027-01-31T00:00:00Z
sources:
  - id: bqe-finding
    resource: /findings/bqe-core-api-capabilities-2026-10.md
    title: BQE CORE public API finding, 23 Oct 2026
  - id: bqe-scope
    resource: /open-questions/bqe-core-integration-scope.md
    title: "BQE CORE: integration scope and verification"
  - id: platform-rec
    resource: /assessments/agent-platform-recommendation.md
    title: Agent platform recommendation (proposal)
  - id: bqe-api-agreement
    resource: https://www.bqe.com/agreements/customer-api-use-agreement
    title: BQE Customer API Use Agreement
  - id: mcp-spec
    resource: https://modelcontextprotocol.io/specification
    title: Model Context Protocol specification
---

> **This is a proposal drafted by Claude, at the owner's request on 23 Oct 2026. It is not a decision.** Every BQE fact it relies on comes from secondary evidence. See the [BQE finding](/findings/bqe-core-api-capabilities-2026-10.md), which must be re-verified in Phase 0.[^bqe-finding]

# Brief for the build agent

Read this section in full before writing code.

**Goal.** Give RSGx staff governed, self-service access to BQE CORE data in three ways:

1. a **visual data explorer**, where users pick a resource and its fields, filter, preview and export, without writing queries;
2. an **admin console**, where administrators connect BQE and decide which resources and fields ("data points") each role may see;
3. an **MCP server** on Azure, so AI clients (Claude Enterprise, Copilot Studio, Foundry agents) can query the same data under the same rules.

**The one rule that shapes everything.** All three surfaces go through **one connector and one policy layer**. Neither the console, the explorer nor the MCP server calls BQE directly. If the field allowlist could be bypassed through any surface, the design has failed.

**Read-only in v1.** Request `read:core`, never `readwrite:core`. Writing to BQE is out of scope until the owner says otherwise.

**Where the code lives.** Not in this repository: chinny_brain holds knowledge, not application code. The owner must name the target repository (decision D6). Do not start a repository on your own initiative.

# Known BQE constraints (verify in Phase 0)

| Constraint | Design consequence |
|---|---|
| OAuth 2.0 Authorization Code and Refresh Token only; no client-credentials grant | Every call acts as a named CORE user. See decision D1. |
| 100 requests a minute, per app per user; `429` with `Retry-After` | Per-user token bucket, queueing, honouring `Retry-After`, and showing the remaining budget in the console |
| Query parameters `fields`, `where`, `orderBy`, `page` | The visual builder compiles to these, so there is no client-side filtering of large sets |
| Webhooks: JSON `POST`, 5 attempts 30 s apart, signed with the client secret | Optional change feed for cache invalidation (Phase 3+) |
| BQE may accept or deny developer access, and integrated apps must be approved by BQE[^bqe-api-agreement] | Start the approval in Phase 0. It is on the critical path. |
| No published sandbox (current docs show production only; the 2019 sandbox hosts no longer answer) | CI uses a recorded mock only. Ask BQE for a sandbox or trial company before Phase 1. |
| The API host is regional: the token response's `endpoint` gave `syd-api.bqecore.com.au` for RSGx (confirmed 23 Oct 2026) | Store the `endpoint` per BQE connection; never hard-code a host. It also informs D4: the data appears to be hosted in Sydney. |
| Cloudflare blocks default HTTP client signatures (error 1010; confirmed 23 Oct 2026) | Every client sets an honest, descriptive `User-Agent`. Never imitate a browser. |
| Dates and times default to US Pacific time | Send `X-UTC-OFFSET` on every request; test date boundaries |
| Only Regular Web App and Web App (FAPI/PAR) types get refresh tokens; the Phase 0 test used a Native App | The platform registers a Regular Web App (client secret in Key Vault, PKCE on) or FAPI/PAR |

# Proposed architecture

```
                    ┌──────────────── Entra ID (SSO, app roles) ────────────────┐
                    │                                                            │
 Users ──► Data explorer (web) ─┐                                                │
 Admins ─► Admin console (web) ─┼──► API service ──► Policy layer ──► BQE connector ──► BQE CORE API
 AI clients ─► APIM ─► MCP server┘        │              │                 │
                                          ▼              ▼                 ▼
                                    PostgreSQL     Audit log       Key Vault (BQE tokens,
                                (config, saved    (append-only)     client secret)
                                 queries, catalogue)
```

**Proposed stack.** The agent may challenge any of these choices, with reasons.

- **Language:** TypeScript monorepo (pnpm workspaces). Packages: `connector`, `policy`, `catalogue`, `api`, `web`, `mcp-server`, `infra`.
- **Web:** Next.js (App Router), one app with `/admin` and `/explore` route groups, gated by Entra ID app roles.
- **API:** Node (Fastify) as the only service the web app talks to.
- **MCP:** the official TypeScript SDK (`@modelcontextprotocol/sdk`), Streamable HTTP transport.[^mcp-spec]
- **Azure:** Container Apps (web, api and mcp-server as separate apps), Azure Database for PostgreSQL Flexible Server, Key Vault, managed identities, Application Insights, and API Management in front of the MCP server.
- **Infrastructure as code:** Bicep. Deploy through GitHub Actions with OIDC federation, with no stored Azure secrets.
- **Region:** an owner decision (D4). Do not default it.

Fit with the programme: the [agent platform recommendation](/assessments/agent-platform-recommendation.md) lists Microsoft Foundry as one runtime option, and keeps Claude Enterprise connected through MCP.[^platform-rec] An MCP server behind APIM serves both. The recommendation is itself a proposal, so this plan does not depend on it.

# Owner decisions needed before build (Phase 0)

| ID | Decision | Claude's recommendation (proposal) |
|---|---|---|
| D1 | **Whose BQE identity do queries run as?** (a) Each user connects their own CORE account. (b) One integration account for everyone. | **(a) by default.** It preserves BQE's own permissions and gives each user their own rate budget. Option (b) means anyone with console access sees what the integration account sees, so BQE's permission model is bypassed and the platform's allowlist becomes the only control. If (b) is needed for scheduled jobs, use a dedicated, named, least-privilege CORE user, and record that use separately. |
| D2 | **Store BQE data, or pass it through?** | **Pass-through in v1**, with a short-lived per-user in-memory cache (minutes). A persistent copy of client financial data is a new data store in ISO 27001 scope (PR-17), and needs its own classification, retention and access review. |
| D3 | **Exports allowed?** Which formats, and to whom? | CSV and XLSX, limited to a role, with each export written to the audit log. |
| D4 | **Azure tenant, subscription and region** | Use the RSGx tenant. The region follows the data-residency position for client financial data, which is the owner's call. |
| D5 | **Which AI clients may connect to the MCP server?** | Start with one (for example Claude Enterprise), authenticated through Entra ID. |
| D6 | **Target repository** for the code | A new private repository under `rsgx-org-ai`, with the same branch protection as chinny_brain |
| D7 | **Is BQE in scope at all?** See the [open question](/open-questions/bqe-core-integration-scope.md).[^bqe-scope] | Confirm it before any spend. |

# Phases

## Phase 0: verify and unblock (no application code)

1. Re-read the BQE pages directly: the enumerations, every resource page, authentication, filtering, rate limits, webhooks and the changelog. This needs network access to `api-explorer.bqecore.com` and `corehelpcenter.bqe.com`. Mirror them into `references/` and update the [finding](/findings/bqe-core-api-capabilities-2026-10.md). Find out whether BQE publishes an OpenAPI/Swagger document. If it does, the catalogue is generated from it, and the generated catalogue replaces any hand-built one.
2. Confirm the production API base URL, the scopes needed per resource (including the additional `ePaymentLink` scope), and whether the rate limit applies per app per user to every endpoint.
3. Create the BQE developer account, register an app, make one read-only call, and start BQE's application approval. Record the approval's status and dates.
   *Done in part on 23 Oct 2026:* a Native App made one live `read:core` call from the owner's machine. See the [finding](/findings/bqe-core-api-capabilities-2026-10.md). BQE's approval process has not been started.
4. Record decisions D1–D7.

**Exit:** the finding is re-verified from primary sources, a sandbox app exists and has made one successful call, and D1–D7 are recorded.

## Phase 1: connector and catalogue

- **OAuth.** Authorisation-code flow with PKCE, refresh rotation, revocation, and tokens held in Key Vault. No token ever reaches the browser or the logs.
- **HTTP client.** A per-user token bucket at 100 requests a minute, with a safety margin. On `429` it backs off and honours `Retry-After`. Requests are paged and the page size is bounded. Every response is validated against its schema.
- **Catalogue.** A machine-readable description of each resource: its fields, types, enum references with values, which fields can be filtered and sorted, and the scope required. Generated from OpenAPI if one exists, otherwise hand-built from the Phase 0 mirror, with its provenance noted.
- **Query model.** A typed `Query` object `{resource, fields[], filters[], orderBy, limit}` that compiles to `fields`/`where`/`orderBy`/`page`. Unknown resources, fields and operators are rejected.
- **Testing.** A mock BQE server built from recorded sandbox responses. Production BQE is never called from CI.

**Acceptance:** the connector's unit tests cover the compiled queries, the rate limiter under burst, the refresh flow and the `429` handling. One end-to-end sandbox test passes for each catalogue resource.

## Phase 2: policy layer and admin console

- **Policy model.** Role → allowed resources → allowed fields, optionally with row filters (for example "own projects only"). Deny by default. The same policy object is enforced in the API **and** the MCP server, from one package.
- **Console features:**
  - connect and disconnect BQE (sandbox or production), and show token health;
  - a catalogue browser with a tick-box per field, per role, so admins choose the exposed data points;
  - user and role mapping from Entra ID app roles;
  - the rate-budget view, recent errors and webhook status;
  - an audit log viewer: who queried what, which fields, how many rows, and whether it was exported;
  - the change history of the policy itself, with who changed it and when.
- **Audit.** Append-only. Policy changes and exports are always logged.

**Acceptance:** a field removed from a role disappears from the explorer and from the MCP server, with no redeploy, within one minute. Every policy change appears in the audit log.

## Phase 3: visual data explorer

- **Flow:** pick a resource, tick fields (only the allowed ones are shown, with friendly names), add filters (enum fields as drop-downs from the catalogue, dates as date pickers), sort, preview the first page, run the query, then export.
- **Saved queries:** private or shared within a role, re-runnable, with a "copy as MCP call" option so users can hand a query to an AI client.
- **Feedback:** the row-count and rate-budget cost is estimated before a run. Long pulls run as background jobs, with progress shown.
- **Accessibility:** WCAG 2.2 AA, keyboard-operable.

**Acceptance:** a non-technical user, unaided, builds and exports "billable time entries for project X last month, by employee". No field outside the user's policy can be requested, even by hand-editing the API call.

## Phase 4: MCP server on Azure

- **Tools (read-only):**
  - `list_resources`: what the caller may query;
  - `describe_resource`: the allowed fields, their types and the enum values;
  - `query`: the typed `Query` object, with the result capped in rows and response size;
  - `run_saved_query`: a saved query, by ID, with parameters.
- **Prompts or resources (optional):** the catalogue exposed as MCP resources, so clients can ground themselves before querying.
- **Authentication:** OAuth 2.1 as the MCP specification requires, with Entra ID as the authorisation server, fronted by API Management for rate limiting, IP policy and logging. The MCP caller's Entra identity maps to the same role policy and, under D1(a), to that user's BQE connection.
- **Safety:** tool output is data, so no free-text field from BQE is interpreted as instructions. Pagination is server-side, and result sizes are bounded for model context limits.
- **Deployment:** a Container App with a managed identity and private access to Key Vault and PostgreSQL. The server is listed in the agent registry, if the control plane exists by then.

**Acceptance:** an MCP client connected as user A cannot see a field denied to A's role. Every MCP call appears in the same audit log as explorer queries. The server passes the MCP Inspector checks.

## Phase 5: hardening and go-live

- A threat model (STRIDE) covering token theft, policy bypass, prompt injection through BQE text fields, and export leakage.
- Dependency and secret scanning in CI, plus an infrastructure-as-code security lint.
- A load test against the mock server at the rate limit.
- Runbooks: rotating the BQE client secret, revoking a user's BQE connection, disabling the MCP server.
- An impact assessment, under the programme's governance, before production data is connected.
- Production cut-over only after BQE approves the production app.

# Out of scope for v1

- Writing to BQE (`readwrite:core`).
- A persistent data warehouse of BQE data (see D2).
- Joins across resources beyond what one BQE call returns. Note this as a likely v2 request.
- Any data source other than BQE. The connector interface should still allow for more.

# Risks (challenge)

1. **BQE approval is on the critical path, and out of RSGx's control.** BQE's terms say it may accept or deny access at its sole discretion.[^bqe-api-agreement]
2. **Decision D1 decides the security model.** A shared integration account quietly turns this platform into the access-control system for BQE data.
3. **100 requests a minute per user** makes large interactive pulls slow. Users will ask for a warehouse. Make that a deliberate decision (D2), not drift.
4. **The evidence is secondary.** If Phase 0 finds BQE's documentation differs from the [finding](/findings/bqe-core-api-capabilities-2026-10.md), update this plan before building.
5. **Scope.** This is three products. If time is short, build Phases 1, 2 and 4 (connector, policy and MCP) before the visual explorer. The governed access is the hard part. The explorer is the most replaceable part.

[^bqe-finding]: BQE CORE public API finding, 23 Oct 2026
[^bqe-scope]: BQE CORE: integration scope and verification
[^platform-rec]: Agent platform recommendation (proposal)
[^bqe-api-agreement]: BQE Customer API Use Agreement
[^mcp-spec]: Model Context Protocol specification
