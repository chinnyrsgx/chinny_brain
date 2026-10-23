# Log

Newest first.

## 2026-10-23

- **Updated** `findings/bqe-core-api-capabilities-2026-10.md` and `prototypes/bqe-data-explorer-and-mcp.md` with the results of one live read-only call made by the owner: regional endpoint `syd-api.bqecore.com.au`, rate-limit headers, Cloudflare user-agent blocking, `activity` field names, and no published sandbox. Enumeration values are still unverified.
- **Created** `prototypes/bqe-data-explorer-and-mcp.md` [P]: handoff plan for a BQE connector, admin console, visual data explorer and read-only MCP server on Azure. It needs owner decisions D1–D7 before build. `stale_after` 2027-01-31.
- **Created** `findings/bqe-core-api-capabilities-2026-10.md`: BQE CORE public API resources, querying, OAuth model, rate limits, webhooks and enumeration names. Secondary evidence only, because `*.bqecore.com` was blocked by the session's network policy. Enum values not obtained. `stale_after` 2027-01-31.
- **Created** `open-questions/bqe-core-integration-scope.md` [I]: whether a BQE integration is in scope, primary verification of the enumerations, and the delegated-identity constraint.
- **Created** this `log.md`. CLAUDE.md requires it, but it was not in the repository.
