---
type: Finding
title: "OKF v0.2 spec: canonical home and the conformance facts this bundle depends on"
description: "Re-verified 30 Sep 2026 from the canonical repository: still v0.2, three conformance rules, absent status means stable, and no official validator."
tags: [okf, conformance, reference, time-sensitive]
status: draft
generated: { by: claude/claude-opus-5-5, at: 2026-09-30T02:00:00Z }
stale_after: 2027-03-31T00:00:00Z
sources:
  - id: okf-repo
    resource: https://github.com/GoogleCloudPlatform/open-knowledge-format
    title: GoogleCloudPlatform/open-knowledge-format (cloned 2026-09-30, HEAD ad30107)
    last_modified: 2026-08-21T20:08:36Z
  - id: okf-spec
    resource: https://github.com/GoogleCloudPlatform/open-knowledge-format/blob/main/SPEC.md
    title: Open Knowledge Format v0.2 specification
---

# Finding

- **Version.** `SPEC.md` still declares **Version 0.2**.[^okf-spec] The latest change, merged 21 Aug 2026 (commit `ad30107`), made every timestamp an ISO 8601 datetime with an explicit offset. It also removed the duplicated timestamp wording from §5 and §11.[^okf-repo]
- **Conformance (§11).** OKF has only three rules: every non-reserved `.md` has parseable frontmatter; every frontmatter block has a non-empty `type`; and `index.md`/`log.md` follow §8/§9. Consumers MUST NOT reject a bundle for broken links, unknown keys, unknown types or missing indexes.[^okf-spec]
- **Absent `status` means `stable` (§5.4).**[^okf-spec] This is why [P] and [I] items must carry `status: draft` explicitly. Otherwise any OKF tool presents them as current and approved.
- **`verified` by a `human:` actor gives the "human-reviewed" trust tier (§5.3).**[^okf-spec] That means someone checked the content against its sources. **It is not Forum ratification**, which this bundle records separately.
- **No official validator.** The canonical repository ships a reference *producer* agent and sample bundles, but no validator.[^okf-repo] This bundle's `tools/validate_okf.py` is the only automated conformance check available.

# Consequence

Checks that go beyond OKF are RSGx profile rules: broken-link failures, the provenance/status coupling and ratification. They are stricter than the spec, and that is allowed. External OKF tools will not enforce them, so this repository's CI must.

[^okf-spec]: Open Knowledge Format v0.2 specification
[^okf-repo]: GoogleCloudPlatform/open-knowledge-format (cloned 2026-09-30, HEAD ad30107)
