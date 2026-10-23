---
type: Open Question
title: "BQE CORE: is an integration in scope, and who verifies the enumerations?"
description: "The BQE CORE API finding rests on secondary evidence, and its enumeration values were not obtained. Its relevance to the programme is unconfirmed."
tags: [bqe-core, integration, api, verification]
status: draft
provenance: I
owner: human:cchin
generated: { by: claude/claude-opus-5-5, at: 2026-10-23T03:00:00Z }
sources:
  - id: bqe-finding
    resource: /findings/bqe-core-api-capabilities-2026-10.md
    title: BQE CORE public API finding, 23 Oct 2026
---

# Why it matters

The [BQE CORE finding](/findings/bqe-core-api-capabilities-2026-10.md) was written without direct access to BQE's documentation, because the session's network policy blocked `*.bqecore.com`. Its enum table holds names only.[^bqe-finding]

# Questions for the owner

1. **Scope.** Is BQE CORE RSGx's practice-management system of record, and is an agent integration intended? If not, should the finding be deprecated?
2. **Primary verification.** Who will read `https://api-explorer.bqecore.com/docs/enumerations` and the resource pages directly? This needs either a session whose network policy allows `api-explorer.bqecore.com` and `corehelpcenter.bqe.com`, or a person copying the pages into `references/`.
3. **Identity model.** CORE has no client-credentials grant. Any agent would act on a named user's delegated token. Is that acceptable under the ISO 27001 baseline (PR-17), and whose account would it be?

[^bqe-finding]: BQE CORE public API finding, 23 Oct 2026
