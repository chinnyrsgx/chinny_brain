---
type: Open Question
title: "What does rsgx-okf require beyond OKF v0.2?"
description: "Claude could not read rsgx-org-ai/rsgx-okf, so this bundle conforms to the public OKF v0.2 spec plus house rules. Any RSGx-specific profile is unverified."
tags: [rsgx, okf, conformance, repository, verification]
status: draft
provenance: I
owner: human:cchin
generated: { by: claude/claude-opus-5-5, at: 2026-09-30T02:00:00Z }
sources:
  - id: s-0930
    resource: "PLACEHOLDER: replace with the claude.ai URL of the 2026-09-30 session"
    title: Session 2026-09-30 — chinny_brain repository and handover
  - id: s-0925
    resource: https://claude.ai/chat/f584a4ef-4bd0-48fd-8ad7-cb25ac4ed23c
    title: Session 2026-09-25 — OKF v0.2 bundle build
---

# What is known

- On 30 Sep, `git clone` of `rsgx-org-ai/rsgx-okf` and of `chinnyrsgx/chinny_brain` failed without credentials. Both repositories are private.[^s-0930]
- This bundle was built on 25 Sep against the public OKF v0.2 spec and the house rules. The house-rule reference file and validator script that session looked for (`okf-quickref.md`, `validate_okf.py`) were not in its environment. `tools/validate_okf.py` was therefore written from the spec and the stated house rules, not copied from an RSGx original.[^s-0925]

# Inference [I]

rsgx-okf is probably the RSGx profile of OKF v0.2 and the home of the original house-rule files. If that's right, it may hold a canonical validator that differs from this bundle's rewrite. **Verify this before relying on it.**

# Question

Where does rsgx-okf differ from what this bundle assumes? Check at least:

- required frontmatter keys;
- type names;
- folder conventions;
- the provenance encoding (`provenance: C|P|I`, `provenance_basis`, `decision_status`, `legacy_id`);
- actor IDs;
- the validator's rules.

# Resolution path

A Claude Code session with repository access diffs rsgx-okf against this bundle and **reports** the differences before changing anything. The owner then decides:

- **New work** follows rsgx-okf.
- **Existing concepts** migrate only through a separate, reviewed PR, never silently during the upload.
- **Canonical validator:** if rsgx-okf ships one, CI runs it next to this bundle's validator until the two agree.

[^s-0930]: Session 2026-09-30 — chinny_brain repository and handover
[^s-0925]: Session 2026-09-25 — OKF v0.2 bundle build
