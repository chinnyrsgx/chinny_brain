# CLAUDE.md: operating rules for Claude Code in chinny_brain

This repository is the RSGx AI programme's system of record. It holds OKF v0.2 bundles under `bundles/`, and must conform to `rsgx-org-ai/rsgx-okf`. Read `README.md`, then `bundles/rsgx-ai-programme/overview.md`, then the handoff guide in `bundles/rsgx-ai-programme/handoff/`, before changing anything.

The owner is Chris Chin, AI Governance Lead (`human:cchin`). The decision body is the Forum.

## Working posture

- **Challenge, don't validate.** The owner has asked explicitly to be challenged. Surface risks, inconsistencies and weak evidence directly.
- **Australian/British spelling** throughout.
- **Match the bundle.** Before writing a concept, copy the conventions of its neighbours: `type` strings, key names, provenance encoding. If new work diverges from existing work, change the new work.

## Hard rules: never break these

1. **Never set `provenance: C`, and never write or edit a `ratification` block.** Only a person records a confirmation or a ratification.
2. **Never promote a [P] or [I] item.** A proposal received without objection is still a proposal. It stays `status: draft`.
3. **Never write `human:` in `generated.by`** for content you authored. Use `claude/<model-id>`, and leave your concepts `draft` and unverified.
4. **Never rename or move a merged concept.** Its path is its ID. To replace a concept, supersede it.
5. **Never delete a concept.** Set `status: deprecated`, add `superseded_by`, and log it.
6. **Never edit the body of a deprecated concept.** Frontmatter only.
7. **Never use retired vocabulary:** H1–H4, six-pillar names, M1–M20, or L1–L4 as readiness levels. See `specs/` for the vocabulary crosswalk.
8. **Never write "certified to" about RSGx.** Use "aligned to" or "being built to".
9. **Never publish a time-sensitive claim without a `stale_after`,** and never publish one past its date without re-verifying it against a primary source.
10. **Never push to `main`.** Work on a short-lived branch and open a PR.

## Stop and ask the owner when

- two sources conflict (report the conflict; don't resolve it silently);
- a check fails on content you didn't write;
- a change would alter a decision's meaning, a blocker's status, or anything client-facing;
- rsgx-okf and this repository disagree on a rule.

## Workflow

```bash
git switch -c content/<short-description>
# ... make changes ...
B=bundles/rsgx-ai-programme
python $B/tools/build_index.py $B
python $B/tools/validate_okf.py $B
python $B/tools/check_governance.py $B --changed-from origin/main
# add a dated entry at the top of $B/log.md (## YYYY-MM-DD, newest first)
git add -A && git commit -m "<type>: <what and why>"
git push -u origin HEAD && gh pr create --fill
```

Commit types: `content`, `fix`, `tools`, `chore`, `archive`, `index`.

## Session close

Before ending any session that changed content:

1. Add a `log.md` entry dated today, listing what was created, updated or deprecated.
2. Add or update open questions for anything left unresolved.
3. List any claims whose `stale_after` falls within 90 days (`--stale-report`).
4. State in the PR description which items are [P]/[I] and so need the owner's attention.
