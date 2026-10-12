---
type: Decision Record
title: "Every RSGx agent is built to one standard: a manifest, guardrails in code, MCP inward and A2A sideways"
description: "Proposed agent standard v1: one manifest per agent, every guardrail enforced in code with a named test, no model where a lookup will do, and the manifest published in the agent's A2A Agent Card for a register to read."
tags: [agent-platform, agent-standard, guardrails, a2a, mcp, governance]
status: draft
decision_status: proposed
provenance: P
provenance_basis: "The owner asked on 12 Oct 2026 that all agents be built the same way, that guardrails be visible, and for a playbook and an agent that builds agents. The rules below are Claude's drafting of that ask; the owner has not confirmed them."
generated: { by: claude/claude-opus-5-5, at: 2026-10-12T00:30:00Z }
sources:
  - id: s-1012
    resource: https://claude.ai/code/session_01HhrEPxj25FbpUK9wusNn7a
    title: Session 2026-10-12 — A2A orchestration, agent standard and Employee Checker pilot
  - id: a2a-state
    resource: /findings/a2a-protocol-state-2026-09.md
    title: A2A is stable and neutrally governed, but young
  - id: mcp-only
    resource: /findings/claude-enterprise-mcp-only.md
    title: Claude Enterprise speaks MCP only
  - id: platform-rec
    resource: /assessments/agent-platform-recommendation.md
    title: "Agent platform: build a vendor-neutral control plane, pick one runtime [P]"
---

> **Proposed, not decided.** It needs the owner's explicit confirmation. Forum ratification is a separate step.

# Proposal

The owner's ask, as given:[^s-1012] "all agents will need to be built the same", "where do we visibly see the guardrails?", and "we need an agent to build agents".

The proposal is a single **agent standard v1**. It is held in the agent-build playbook (`rsgx-org-ai/agent-build-playbook`, to be created) and has twelve rules. The six that carry the weight:

1. **One manifest per agent.** `agent.manifest.json` names the human owner, the perimeter whose data it guards, risk tier, HITL tier, autonomy, callers and their purposes, the tools it may touch, the fields that may leave it, and its guardrails. A JSON Schema validates it.
2. **Guardrails are code, not prompts.** Every guardrail names what enforces it (`code`, `platform`, `config` or `prompt`) and the test that proves it. A medium- or high-risk agent may not rely on a prompt alone, and the validator fails the build if one does.
3. **The output is built from an allow-list.** The answer is built from scratch from `data.out.fields`, never by deleting fields from a source record. A canary test feeds in the forbidden fields and checks that none leave.
4. **No model where a lookup will do.** A deterministic agent is still an agent on the register.
5. **MCP inward, A2A sideways.** This applies the integration rule in the platform recommendation[^platform-rec]: an agent reaches its own perimeter's tools over MCP, and asks another perimeter over A2A.
6. **Visible guardrails.** The manifest is published inside the agent's A2A Agent Card as an extension. A register in the AI Hub reads every card, so guardrails are shown by the register rather than by each build tool.

# Challenges (Claude)

- **Dify is not where guardrails become visible.** It shows one app's settings, and the Dify Expert app's moderation is switched off; its guardrails are prompt lines only. Under rule 2 that app would not pass for a medium-risk use.
- **The standard is untested at scale.** It has been applied to one agent, the Employee Checker pilot ([decision](/decisions/a2a-pilot-employee-checker.md)). Expect revisions after the second and third agents.
- **The register does not exist yet.** Until the Hub reads cards, "visible" means reading the manifest in each repository.
- **This does not choose a platform.** The standard is written so that it survives either runtime option in the [open question](/open-questions/agent-platform-selection.md).[^a2a-state][^mcp-only]

# The agent that builds agents

Version 1 is a Claude skill, `build-agent`, in the playbook. One message (purpose, perimeter, owner, callers, source) produces a scaffolded agent: manifest, A2A card, guardrail tests and a pull request that a person merges. The Hub's existing Build Agent proof of concept could later dispatch it from an approved funnel idea. Building the standard before the builder is deliberate: a builder without a standard produces inconsistent agents faster.

[^s-1012]: Session 2026-10-12 — A2A orchestration, agent standard and Employee Checker pilot
[^a2a-state]: A2A is stable and neutrally governed, but young
[^mcp-only]: Claude Enterprise speaks MCP only
[^platform-rec]: Agent platform: build a vendor-neutral control plane, pick one runtime [P]
