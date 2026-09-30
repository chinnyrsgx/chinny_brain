# chinny_brain

This is the private, company-owned knowledge repository for the **RSGx AI transformation programme**. The programme's goal is that RSGx operates materially as an AI-native delivery group by end-2027, governed by the AI Steering Committee (the Forum).

The content is held as **Open Knowledge Format (OKF) v0.2 bundles**: plain markdown files with YAML frontmatter. The repository must conform to the RSGx OKF framework (`rsgx-org-ai/rsgx-okf`). All changes arrive by pull request and pass automated checks.

## Start here

| You are… | Read |
|---|---|
| Forum / steer-co | [`bundles/rsgx-ai-programme/overview.md`](bundles/rsgx-ai-programme/overview.md), then `open-questions/` |
| Continuing the work (a person or Claude) | [`CLAUDE.md`](CLAUDE.md), then [`bundles/rsgx-ai-programme/handoff/`](bundles/rsgx-ai-programme/handoff/) |
| Auditing | [`bundles/rsgx-ai-programme/log.md`](bundles/rsgx-ai-programme/log.md), `decisions/`, git history and the `forum-*` tags |

## Read provenance before you read anything else

Every decision carries a provenance marker, and the marker decides whether you can act on it.

| Marker | Meaning | OKF `status` | Can you act on it? |
|---|---|---|---|
| **[C] Confirmed** | Decided explicitly by the owner in session | `draft` until ground-truthed; `stable` only with a `ratification` block | Yes, within the owner's authority; Forum-level only once ratified |
| **[P] Proposed** | Put forward by Claude and not confirmed, even if nobody objected | always `draft` | No. It's a proposal |
| **[I] Inferred** | Reconstructed from context | always `draft` | No. Verify it first |

Two traps to avoid:

- **"Human-reviewed" is not "ratified".** OKF's trust tier (`verified` by a `human:` actor) means someone checked the content against its sources. Forum ratification is recorded separately, in an affirmative `ratification` block, and nowhere else.
- **Silence never ratifies.** Proposals received without objection stay [P]. CI enforces this.

## Current-state warnings (as at 30 Sep 2026)

- **There is no ratified strategy.** Strategy v0.2 forked into two branches. The v0.3 merge is a proposal.
- **All three visual artifacts are stale.** They use superseded vocabulary. Do not present them to the Forum until T1 is rebuilt.
- **The agent platform is a recommendation, not a decision.** Its vendor and regional claims must be re-verified by 1 Mar 2027.
- **Live blockers:** blocker PR-16 (legal method-IP) and blocker PR-17 (ISO 27001 ISMS baseline).

## Layout

```
chinny_brain/
├── README.md               ← you are here
├── CLAUDE.md               ← operating rules for Claude Code sessions
├── CONTRIBUTING.md         ← how changes are made, reviewed and ratified
├── .github/                ← CODEOWNERS, PR template, CI (validate + weekly shelf-life sweep)
├── .pre-commit-config.yaml ← local checks (convenience; CI is the control)
└── bundles/
    └── rsgx-ai-programme/  ← the programme bundle (OKF v0.2)
        ├── index.md · log.md · overview.md · brief.md
        ├── handoff/        how to resume work
        ├── decisions/      decision records, with provenance in each file
        ├── open-questions/ blockers, ratification requests, unresolved items
        ├── findings/       sourced claims with shelf-life dates
        ├── assessments/    Claude's views, kept separate from decisions
        ├── specs/          domain model, vocabulary crosswalk, schemas, backlog
        ├── prototypes/     build candidates with acceptance criteria
        ├── references/     mirrored sources, and superseded records (deprecated)
        └── tools/          validator, index builder, governance checker
```

Bundle folder names are fixed. A concept's ID is its path, so renaming a folder changes the identity of every concept inside it.

## Rules of the road

- **Everything goes through a PR into `main`.** No long-lived content branches: parallel drafts live as open PRs, where everyone can see them.
- **Nothing is deleted.** Superseded concepts are set to `status: deprecated` and point to their replacement with `superseded_by`.
- **ISO language is exact:** "aligned to" or "being built to", never "certified to", until a certificate exists.
- **Time-sensitive claims carry `stale_after`.** The weekly *Shelf-life register* issue lists what is due for re-verification.
- **House style is Australian/British spelling.**

## Checks

```bash
pip install pyyaml
B=bundles/rsgx-ai-programme
python $B/tools/validate_okf.py $B          # OKF v0.2 conformance + house format rules
python $B/tools/build_index.py $B            # regenerate index.md files (commit the result)
python $B/tools/check_governance.py $B       # provenance, ratification, shelf life, placeholders
python $B/tools/check_governance.py $B --stale-report
```
