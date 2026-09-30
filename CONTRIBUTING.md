# Contributing to chinny_brain

This repository is an audit trail, not just documentation. These rules protect three things:

- **Provenance:** who decided what.
- **Lifecycle:** what is current.
- **Freshness:** what is still true.

## 1. How every change lands

1. Branch from `main` with a short-lived branch (`content/…`, `fix/…`, `forum/…`).
2. Change the concepts. Regenerate the indexes with `tools/build_index.py`. Add a `log.md` entry.
3. Open a PR. The PR template's checklist is required.
4. CI must pass: OKF validation, index freshness, governance checks and secret scan.
5. A code owner other than the author approves. Merge with a **merge commit**, so history keeps its shape for audit.

Parallel drafts of the same document exist only as open PRs against one `main`. That is the structural fix for the v0.2 strategy fork.

## 2. Provenance and how an item gets promoted

| From | To | What must happen | Who |
|---|---|---|---|
| [I] Inferred | [C] or [P] | Verify against a source; record `verified` | The owner |
| [P] Proposed | [C] Confirmed | The owner states the decision **explicitly**; record `decided_by: human:<id>` | The owner |
| [C] (draft) | [C] stable, Forum-ratified | An affirmative Forum decision, recorded as a `ratification` block | Forum chair or delegate |

The only accepted form of a `ratification` block:

```yaml
ratification:
  mode: affirmative               # anything else fails CI
  by: human:<forum-chair-id>
  body: AI Steering Committee (Forum)
  at: 2026-10-06T06:00:00Z
  ref: <link or path to the minute that records it>
```

A lack of objection never promotes anything. A `verified` event means "content checked against sources". It does not mean "decided".

## 3. Supersession

Never delete a concept, and never rename a merged one. To replace a concept:

1. Create the new concept.
2. On the old one, set `status: deprecated` and `superseded_by: /<path-to-new>.md`.
3. Leave the old body untouched.
4. Log it with a `**Deprecation**:` entry.

## 4. Shelf life

- Give every time-sensitive claim a `stale_after`: ISO editions, vendor features and regions, commercial terms, survey figures.
- To re-verify a claim, check it against a primary source. Then add a `verified` event and set a new `stale_after`, both in one PR.
- CI fails any PR that edits a concept past its `stale_after` without resetting it.

## 5. ISO claim language

"Certified to" is reserved for a certificate that exists. Otherwise use "aligned to" or "being built to", exactly as recorded in the bundle's ISO language decision. Softened wording is deliberate: don't "correct" it.

## 6. Tags

Tag the merge commit that reflects each Forum meeting `forum-YYYY-MM-DD`. That gives auditors a fixed snapshot of what the Forum saw.
