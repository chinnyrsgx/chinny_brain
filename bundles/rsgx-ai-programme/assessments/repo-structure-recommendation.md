---
type: Assessment
title: "Repository structure for chinny_brain [P]"
description: "Claude's proposal: host this bundle unchanged under bundles/rsgx-ai-programme/, keep governance files at the repo root, and enforce provenance in CI."
tags: [rsgx, repository, okf, structure, governance, claude-view]
status: draft
provenance: P
generated: { by: claude/claude-opus-5-5, at: 2026-09-30T02:00:00Z }
sources:
  - id: s-0930
    resource: "PLACEHOLDER: replace with the claude.ai URL of the 2026-09-30 session"
    title: Session 2026-09-30 — chinny_brain repository and handover
  - id: okf-spec
    resource: https://github.com/GoogleCloudPlatform/open-knowledge-format/blob/main/SPEC.md
    title: Open Knowledge Format v0.2 specification
---

> **This is Claude's recommendation, not a decision.** It needs the owner's explicit acceptance before it is recorded as one.

# Recommendation

```
chinny_brain/
├── README.md, CLAUDE.md, CONTRIBUTING.md   # repo governance: outside any bundle
├── .github/                                 # CODEOWNERS, PR template, CI workflows
├── .pre-commit-config.yaml, .gitleaks.toml
└── bundles/
    └── rsgx-ai-programme/                   # this bundle, folder names unchanged
```

1. **Host the bundle unchanged.** A concept's ID is its path within the bundle.[^okf-spec] Renaming folders would change the identity of all 75 existing concepts and break every citation of them. The `bundles/<name>/` layout mirrors the canonical OKF repository and leaves room for further bundles.
2. **Keep governance files outside the bundle.** OKF requires every non-reserved `.md` file in a bundle to carry frontmatter with a `type`.[^okf-spec] A README, CLAUDE.md or PR template inside the bundle would break conformance.
3. **Enforce provenance mechanically.** `tools/check_governance.py` runs in CI next to `validate_okf.py`. [P] and [I] items can never be stable. An item becomes confirmed only through a `ratification` block that is affirmative, signed by a person and cites a record, so a lack of objection never counts.
4. **Make shelf life visible.** A weekly workflow maintains a "Shelf-life register" issue. CI fails any PR that edits a concept past its `stale_after`.

# Correction to Claude's own earlier output

The research report produced earlier in the 30 Sep session proposed a different tree: `questions/`, `domain/`, `deliverables/`, `archive/` and `evidence/`. It was drawn without sight of this bundle, and **it is superseded here** for three reasons:[^s-0930]

- It would have renamed every concept ID (see point 1 above).
- This bundle already archives superseded material correctly: `references/` holds Programme Record v0.1 and the retired HANDOFF.md as `deprecated`. A separate `archive/` folder would duplicate that mechanism.
- An ISO `evidence/` folder is premature until [PR-17](/open-questions/pr-17-iso-27001-baseline.md) settles which documented-information controls apply.

# Smaller recommendations

- **Write "blocker PR-16", not "PR-16".** On GitHub a bare "PR-16" reads as pull request #16. Keep the ID, which is cited throughout, but qualify it in prose.
- **Tag each Forum meeting.** Date-tag the merge commit that reflects each Forum meeting (e.g. `forum-2026-10-06`). That gives auditors a fixed snapshot of what the Forum saw.

[^okf-spec]: Open Knowledge Format v0.2 specification
[^s-0930]: Session 2026-09-30 — chinny_brain repository and handover
