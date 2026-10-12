---
type: Decision Record
title: "First A2A pilot: the AI Hub asks HR's Employee Checker which Claude seat holders have left"
description: "Proposed first agent-to-agent pilot. A deterministic HR-perimeter agent answers active, inactive or unknown per work email over A2A v1.0, so the AI team can find Claude seats held by leavers. Nothing else leaves HR."
tags: [agent-platform, a2a, pilot, hr, claude-seats, guardrails, time-sensitive]
status: draft
decision_status: proposed
provenance: P
provenance_basis: "The owner described the use case and asked to start it on 12 Oct 2026, choosing its own repository and service, dataSights as the source, and a new playbook repository. Claude drafted the design; the owner has not confirmed it, and no HR owner has been named."
generated: { by: claude/claude-opus-5-5, at: 2026-10-12T00:30:00Z }
stale_after: 2027-03-01T00:00:00Z
sources:
  - id: s-1012
    resource: https://claude.ai/code/session_01HhrEPxj25FbpUK9wusNn7a
    title: Session 2026-10-12 — A2A orchestration, agent standard and Employee Checker pilot
  - id: a2a-state
    resource: /findings/a2a-protocol-state-2026-09.md
    title: A2A is stable and neutrally governed, but young
  - id: standard
    resource: /decisions/agent-standard-v1.md
    title: Agent standard v1 [P]
---

> **Proposed, not decided.** The owner's go-ahead to build was given in session. Going live needs the items in the [open question](/open-questions/employee-checker-go-live.md).

# Proposal

**The use case (owner's words):**[^s-1012] the AI RSGx Hub asks for updates on active employees to check Claude membership. It sends the request to the Employee Checker, which replies with the data. A guardrail prevents any sensitive detail from being exposed.

**Why A2A here.** The data belongs to HR, a different perimeter from the AI team. This is the case the integration rule reserves A2A for. If the Hub could read the HR record directly, A2A would add ceremony and nothing else.[^a2a-state]

**Shape:**

| Part | Choice |
|---|---|
| Caller | AI Hub, a read-only owner tool `find_leavers_with_seats` |
| Callee | Employee Checker in its own repository and service (`rsgx-org-ai/employee-checker-agent`, to be created). No LLM. |
| Protocol | A2A v1.0, JSON-RPC binding, method `SendMessage`, one data part; header `A2A-Version: 1.0` |
| Source | One minimised dataSights view (email, active flag, sync time) behind a read-only login scoped to that view only |
| Answer | Email and status (active, inactive or unknown), dataset sync time, and counts. Nothing else. |
| Action | The Hub proposes. The owner deprovisions through the existing confirm-token tool. Unknown is never proposed, and owners are never proposed. |

**Guardrails, each enforced in code with a named test**[^standard]**:** caller token checked by hash; skill and purpose bound to the caller; data parts only, so there is no free text to inject; 1 to 500 emails on an allowed domain; answer built from an allow-list (canary-tested); no match returns unknown, never inactive; rate limit; audit records counts only; kill switch. A tenth guardrail sits in the platform: the source login can read one view only.

# Challenges (Claude)

- **"Unknown" will be common.** Many Employment Hero records carry no work email. Treating "not found" as "left" would wrongly remove seats, which is why rule 8 of the standard exists.
- **Status data is sensitive even when minimised.** A leaver's status can reveal a departure that has not been announced. A privacy impact assessment and an HR owner are needed before live data flows.
- **⚠️ Legal/Commercial review recommended before external release.**

[^s-1012]: Session 2026-10-12 — A2A orchestration, agent standard and Employee Checker pilot
[^a2a-state]: A2A is stable and neutrally governed, but young
[^standard]: Agent standard v1 [P]
