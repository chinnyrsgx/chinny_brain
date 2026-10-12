---
type: Open Question
title: "Owner: record Australia as the governing jurisdiction, and confirm any offshore exposure"
description: "The owner confirmed in the 12 Oct session that RSGx is Australian, but only a person can record a confirmation. Until it is recorded, the bundle's platform concepts rest on a relayed instruction."
tags: [rsgx, jurisdiction, residency, privacy, agent-platform, decision-needed]
status: draft
provenance: P
owner: human:cchin
generated: { by: claude/claude-opus-5-5, at: 2026-10-12T02:40:00Z }
stale_after: 2027-01-12T00:00:00Z
sources:
  - id: s-1012
    resource: https://claude.ai/code/session_01UNvDLfsAuXMiT9kpdm7JP6
    title: Session 2026-10-12 — Paperclip, Dify, Microsoft Foundry and alternatives
  - id: platform-report
    resource: /references/agent-platform-report-2026-10-12.md
    title: Agent platform report, 12 Oct 2026 (mirrored)
---

# Why it matters

The 28 Sep platform report framed residency and law entirely around Malaysia: the Malaysian PDPA, Malaysia and Singapore regions, and an Option B in the Malaysia region. In the 12 Oct session the owner said that RSGx is Australian.[^s-1012] On that basis Claude superseded the 28 Sep report and recommendation. Australian law and residency now drive the platform gates: the Privacy Act (APP 8 and the automated decision-making duty from 10 Dec 2026), the ISM agent controls and IRAP.[^platform-report]

Claude cannot record that confirmation. Until the owner does, every platform concept that relies on it rests on an instruction relayed in session.

# Questions for the owner

1. **Record the jurisdiction.** Confirm, in a record you author, that Australia is the governing jurisdiction for the RSGx AI programme.
2. **Offshore exposure.** Does RSGx have clients, staff or operations in Malaysia, or elsewhere offshore, whose personal data its agents would process? If it does, that law applies to that data. Malaysia's PDPA as amended, for example, regulates cross-border transfers and has no in-country model inference from any hyperscaler today.
3. **APP entity status.** Is RSGx an APP entity under the Privacy Act, or within the small-business exemption? The threshold was not verified.
4. **Contractual flow-down.** Do any government, defence or critical-infrastructure clients pass ISM, IRAP or SOCI obligations down to RSGx?

# Dependencies

- **Gates:** the runtime choice in [agent platform selection](/open-questions/agent-platform-selection.md), and gate G4 in the [12 Oct recommendation](/assessments/agent-platform-recommendation-2026-10.md).

[^s-1012]: Session 2026-10-12 — Paperclip, Dify, Microsoft Foundry and alternatives
[^platform-report]: Agent platform report, 12 Oct 2026 (mirrored)
