---
type: Finding
title: "BQE CORE public API: what it exposes, and the limits on it"
description: "As at 23 Oct 2026: BQE CORE offers a REST API over its practice-management records, with OAuth 2.0 (user-delegated only), 100 requests a minute and webhooks. Sign-in, the regional endpoint and the rate-limit headers were confirmed by one live read-only call. All 72 enumerations and 542 models were retrieved from BQE's documentation API."
tags: [bqe-core, integration, api, enumerations, oauth, time-sensitive]
status: draft
generated: { by: claude/claude-opus-5-5, at: 2026-10-23T03:00:00Z }
stale_after: 2027-01-31T00:00:00Z
sources:
  - id: bqe-enumerations
    resource: https://api-explorer.bqecore.com/docs/enumerations
    title: BQE CORE API Explorer — Enumerations (not fetched; see Evidence quality)
  - id: bqe-enum-help
    resource: https://corehelpcenter.bqe.com/hc/en-us/articles/28997574423319-Where-can-I-find-the-enum-values-used-by-CORE-Public-APIs
    title: BQE Help Center — Where can I find the enum values used by CORE Public APIs?
  - id: bqe-auth
    resource: https://api-explorer.bqecore.com/docs/authentication-authorization
    title: BQE CORE API Explorer — Authentication and Authorization
  - id: bqe-rate-limits
    resource: https://corehelpcenter.bqe.com/hc/en-us/articles/4412231930263-Do-BQE-CORE-APIs-impose-rate-limits
    title: BQE Help Center — Do BQE CORE APIs impose rate limits?
  - id: bqe-webhooks
    resource: https://api-explorer.bqecore.com/docs/webhooks
    title: BQE CORE API Explorer — Webhooks
  - id: bqe-changelog
    resource: https://api-explorer.bqecore.com/docs/support/changelog
    title: BQE CORE APIs Update Log
  - id: bqe-sample
    resource: https://github.com/BQEDeveloper/CoreApi-Asp.net-Sample
    title: BQEDeveloper — CoreApi ASP.NET sample app (last commit 29 Jul 2019)
  - id: bqe-docs-config
    resource: https://api-explorer.bqecore.com/assets/config.json
    title: BQE CORE API Explorer — published Postman environment (fetched 23 Oct 2026)
  - id: bqe-catalogue
    resource: https://github.com/rsgx-org-ai/bqe-data-platform/tree/claude/sleepy-carson-gqhs3s/docs/bqe-catalogue
    title: BQE CORE API catalogue snapshot (enumerations, models, APIs), 23 Oct 2026
  - id: smoke-test
    resource: https://github.com/rsgx-org-ai/bqe-data-platform/blob/claude/sleepy-carson-gqhs3s/docs/phase0/smoke-test-2026-10-23.md
    title: Phase 0 smoke test — one live read-only call, 23 Oct 2026
---

# Evidence quality: read this first

**Update, 23 Oct 2026 (later the same day).** The documentation hosts were then allowed, and the owner ran one live, read-only call against RSGx's CORE company.[^smoke-test] The section *Confirmed by live call* below supersedes the earlier secondary claims wherever they differ. Once `api-documentation.bqecore.com` was allowed, the full catalogue was retrieved: 72 enumerations with values, 542 models and 86 APIs. BQE publishes no OpenAPI file; this JSON catalogue is the equivalent. A snapshot is kept in `rsgx-org-ai/bqe-data-platform` under `docs/bqe-catalogue/`.[^bqe-catalogue] The enum table below predates it and is kept for the record.

The original note follows. At first, this session's network policy blocked every `*.bqecore.com` and `corehelpcenter.bqe.com` host. No BQE documentation page was fetched directly. Every claim below comes from search-engine extracts of BQE's own pages, or from BQE's public GitHub sample app, which was cloned and read.[^bqe-sample] Treat the whole finding as secondary evidence until someone re-reads the primary pages.

**The enumeration values were not obtained.** The [Enumerations page](https://api-explorer.bqecore.com/docs/enumerations) was the subject of the request. Only enum *names* surfaced, and the values of one enum. Do not code against any value listed here.

# Finding

## What the API covers

BQE CORE is practice-management and accounting software for professional-services firms. *(This summary of the product is general knowledge, not taken from a source in this session.)* Its public REST API is documented as a set of resource pages under `/docs/api/apis/`. The following resources were seen:

| Area | Resources |
|---|---|
| People and organisation | Employee, Group, Vendor, Client |
| Projects and resourcing | Project (referenced from other pages), Project Assignment, Allocation, Activity |
| Time and expense | Time Entry, Expense Entry |
| Billing and receivables | Invoice, Billing Schedule, Payment, Estimate |
| Payables | Bill (vendor invoices) |
| CRM | Lead Source, Follow-up, Email Template, Commission Profile |
| Other | Note |

- **Operations.** The Bill page documents retrieve, create, update and delete. Other resources are assumed to follow the same pattern, but this was not checked one by one. Payment was seen only as `GET` with `read:core`.
- **Querying.** List endpoints take `fields` (projection), `where` (filter expression), `orderBy` and `page` (page number and page size), plus documented filter operators.[^bqe-sample]
- **Recent change.** The changelog records an ePayment API and an `ePaymentLink` property on Invoice. That property returns null unless the token carries an additional scope.[^bqe-changelog]

## Enumerations

According to BQE's help centre, enum-typed properties link to their values from the Format column, and the Enumerations page lists them all. Individual enums can be reached by anchor, for example `/docs/enumerations#EmployeeStatus`.[^bqe-enum-help]

These enum names were seen on resource pages. Values are not verified.[^bqe-enumerations]

| Enum | Used by | Values seen |
|---|---|---|
| `EmployeeStatus` | Employee.status | Active, Inactive, Terminated (from the field's description; may not be the full list) |
| `DateFrequency` | Employee compensatory-time frequency | — |
| `BilledStatus` | Time Entry, Expense Entry (`billStatus`) | — |
| `ItemType` | Allocation, Project Assignment | — (it distinguishes activity from expense items) |
| `AssignedResourceType` | Project Assignment | — |
| `BudgetEstimateStatus` | Estimate.status | — |
| `BillPaymentStatus` | Bill payment state | — |
| `ClientType` | Client | — |
| `Status` | Client, Commission Profile, Lead Source | — |
| `ToDoPriority`, `ToDoStatus` | Follow-up | — |

## Access and limits

- **OAuth 2.0, user-delegated only.** Only the Authorization Code and Refresh Token grants are supported. Client Credentials, Implicit and Resource Owner Password are not.[^bqe-auth]
- **Scopes:** `read:core` (read only), `readwrite:core` (full access to company data), `offline_access` (refresh token) and `openid`/`profile` (user identity).[^bqe-auth][^bqe-sample]
- **Hosts:** production and sandbox are separate. The identity provider's discovery document is at `api-identity.bqecore.com/idp/.well-known/openid-configuration`, with a sandbox equivalent at `sandbox-api-identity.bqecore.com`. Apps are registered in the developer portal at `api-developer.bqecore.com`.[^bqe-sample] The production API base URL was not confirmed, because the docs use a `{base_url}` placeholder.
- **Rate limit:** 100 requests a minute, per app per user, for apps registered after 21 Feb 2023. Older apps should read the `X-Rate-Limit` headers.[^bqe-rate-limits] When the limit is exceeded the API returns `429` with a `Retry-After` header in seconds. `/version` and `/health` are exempt.
- **Webhooks:** each event is sent as a JSON `POST`. Any 2xx response counts as delivered. A failed delivery is attempted 5 times in total, 30 seconds apart. The payload is validated with the app's client secret, or the client ID if the app has no secret.[^bqe-webhooks]

# Confirmed by live call, 23 Oct 2026

One call was made from the owner's machine with a Native App (PKCE, no client secret) requesting `read:core` only. Only statuses, headers and field names were recorded; no record values.[^smoke-test]

- **Sign-in works as documented.** Discovery at `https://api-identity.bqecore.com/idp/.well-known/openid-configuration` returned 200. The token response granted exactly `read:core`, with `expires_in` 3600 seconds. No refresh token was issued: the docs say only Regular Web App and Web App (FAPI/PAR) types receive refresh tokens.
- **The API host is regional.** The token response's `endpoint` field returned `https://syd-api.bqecore.com.au/api/`, not the `https://api.bqecore.com/api/` in BQE's published Postman environment.[^bqe-docs-config] RSGx's CORE data appears to be hosted in Sydney. Clients must use the `endpoint` value, never a fixed host.
- **Version:** `GET /version` returned `2026.10.1.0`.
- **Rate-limit headers are present:** `X-Rate-Limit-Limit: 1m`, `X-Rate-Limit-Remaining: 99` after one call, and `X-Rate-Limit-Reset` as an ISO-8601 UTC time. This is consistent with 100 requests a minute.
- **Cloudflare blocks default HTTP client signatures.** The first run's calls returned 403, Cloudflare error 1010 ("blocked access based on your browser's signature"), for Python's default `Python-urllib` user agent. An honest, descriptive `User-Agent` passed. Every RSGx client must set one; do not imitate a browser.
- **`read:core` can reach personal and banking data.** Per the model catalogue, `Employee` carries `ssn`, `bankAccount`, `bankRouting`, `salary` and `dateOfBirth`, and `Vendor` all of those except `ssn`. Every request must name its fields, and the policy layer must deny these by default.[^bqe-catalogue]
- **`read:core` exposes commercial data.** The first `activity` record carried 32 fields, including `costRate`, `billRate` and `overTimeBillRate`, plus account and group IDs and audit fields (`lastUpdated`, `lastUpdatedById`, `version`, `objectState`). Read-only access is not low-sensitivity access, so field-level policy in the platform is essential.

Also confirmed from the documentation, now reachable:

- **No sandbox is published.** The current docs and their Postman environment describe production only. The 2019 sandbox hosts no longer answer.
- **Dates and times default to US Pacific time.** The `X-UTC-OFFSET` header (minutes) changes it.
- **App types:** Regular Web App (client secret, optional PKCE), Web App FAPI/PAR (secret, PKCE and PAR required), JavaScript App and Native App (no secret).

# Relevance to RSGx (challenge)

Nothing in this bundle yet says RSGx uses BQE CORE or plans an integration. That should be confirmed before any of this informs a design. If it does:

- **No machine identity.** Without a client-credentials grant, an agent can reach CORE only on a named user's delegated token. Every agent write is then attributed to that person, and a refresh token has to be held as a long-lived secret. Both points matter for the ISO 27001 baseline (blocker PR-17) and for any agent-platform design.
- **Bulk work is throttled.** 100 requests a minute per user rules out large synchronous back-fills. Use paging with `fields`, plus webhooks for change capture.
- **`readwrite:core` is all or nothing.** It grants full access to company data. Read-only use cases should request `read:core` only.

# Shelf life

These claims come from vendor documentation. The rate-limit article is roughly two years old. Re-verify against the primary pages by 31 Jan 2027, or before any build decision, whichever comes first.

[^bqe-enumerations]: BQE CORE API Explorer — Enumerations (not fetched; see Evidence quality)
[^bqe-enum-help]: BQE Help Center — Where can I find the enum values used by CORE Public APIs?
[^bqe-auth]: BQE CORE API Explorer — Authentication and Authorization
[^bqe-rate-limits]: BQE Help Center — Do BQE CORE APIs impose rate limits?
[^bqe-webhooks]: BQE CORE API Explorer — Webhooks
[^bqe-changelog]: BQE CORE APIs Update Log
[^bqe-sample]: BQEDeveloper — CoreApi ASP.NET sample app (last commit 29 Jul 2019)
[^bqe-docs-config]: BQE CORE API Explorer — published Postman environment (fetched 23 Oct 2026)
[^bqe-catalogue]: BQE CORE API catalogue snapshot (enumerations, models, APIs), 23 Oct 2026
[^smoke-test]: Phase 0 smoke test — one live read-only call, 23 Oct 2026
