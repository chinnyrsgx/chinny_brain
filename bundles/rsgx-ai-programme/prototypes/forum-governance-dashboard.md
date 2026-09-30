---
type: Prototype Candidate
title: "Forum governance dashboard: one view of every agent across runtimes [P]"
description: "A read-only Forum view of all registered agents, their owners, autonomy levels, impact-assessment status and incidents, built over the control plane's registry."
tags: [prototype, forum, governance, agent-platform, dashboard, claude-view]
status: draft
provenance: P
priority: "After T1. Buildable now against a stub schema; real data depends on the platform decision."
generated: { by: claude/claude-opus-5-5, at: 2026-09-30T02:00:00Z }
sources:
  - id: s-0928
    resource: https://claude.ai/chat/c255f039-58a0-40b4-885a-63f1ede65e23
    title: Session 2026-09-28 — Agent platforms and A2A
---

# Problem

No vendor offers a cross-runtime governance view, as the [UI gap assessment](/assessments/agent-platform-ui-gap.md) sets out. Without one, the Forum can't see, in one place, which agents run at which autonomy level and whether each has an approved impact assessment.[^s-0928]

# Proposed scope

- **Build it read-only**, over the control plane's registry and gateway telemetry, whichever runtime is chosen.
- **Stub the data first.** Build against a stub registry schema with seeded sample data, so work can start before [platform selection](/open-questions/agent-platform-selection.md).

# Acceptance criteria (proposed; Claude's drafting, for owner edit)

1. Lists every registered agent and MCP server, with accountable owner, functional unit, runtime, autonomy level (L1–L4) and lifecycle state.
2. Shows the impact-assessment reference and status for each agent. **Flags any agent at L3 or above without an approved assessment.**
3. Shows incidents per agent over the last 90 days, linked by agent ID.
4. Every displayed figure traces to a source record: a registry entry ID or a trace/incident ID.
5. Uses only current vocabulary:
   - five pillars;
   - Enablement/Automation/Reinvention, held per function;
   - L1–L4, held per solution.
   No H1–H4, six-pillar or readiness-level terms. See the [vocabulary drift finding](/findings/vocabulary-drift-artifacts.md).
6. Takes no write actions against any runtime.
7. Fixes the stub schema before build, and records it as a spec concept in this bundle.

# Sequencing

This candidate follows **T1**, the capability tilemap rebuild. T1 is unblocked and removes a known Forum credibility risk, so it stays first.

[^s-0928]: Session 2026-09-28 — Agent platforms and A2A
