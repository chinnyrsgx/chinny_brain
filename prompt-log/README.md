# Prompt log

A personal, dated record of every prompt Chris Chin ("Chinny") types into Claude Code, each framed as a problem, a solution and what changed. It is kept so the prompts can be searched, compared over time and later vector-indexed.

This folder is **not OKF content**. It sits outside `bundles/`, so the OKF validators, index builder and governance checker never read it.

## Layout

One Markdown file per day, by **AWST** date (Australia/Perth, UTC+8, no daylight saving):

```
prompt-log/
├── README.md
└── YYYY/
    └── MM/
        └── YYYY-MM-DD.md
```

A prompt typed at 07:36 AWST on 13/10/2026 is 23:36 UTC on 12/10/2026. It goes in `2026/10/2026-10-13.md`. The UTC time in an entry's header can therefore fall on the previous calendar day.

## Entry format

Each day file starts with frontmatter and a title, then one `## ` entry per prompt, oldest first:

```markdown
---
date: 2026-10-13
type: prompt-log
owner: human:cchin
tags: []
---

# Prompt log, 13/10/2026

## 07:36 AWST (23:36 UTC) · rsgx-ai-hub · session 01Jc16cD

**Prompt:**
> First line of the prompt
>
> Every line is prefixed with "> ", blank lines with ">"

**Problem:** _to fill at session close_
**Solution:** _to fill at session close_
**Changed:** _to fill at session close_
```

- **Header:** time in AWST and UTC, the repo folder the prompt was typed in, and the first 8 characters of the session id.
- **Prompt:** the text exactly as typed, apart from redaction (see Privacy).
- **Problem / Solution / Changed:** one or two plain lines each, filled in at session close. Problem is what was wanted and why. Solution is what was decided or done. Changed is the files, PRs and links touched, or "Nothing". Where something is unknown, say "not confirmed" rather than guess.
- **Attachments:** never stored. Where one mattered, add a line after the prompt by hand: `**Attachments (named, not stored):** <names>`.
- **Tags:** add a few lowercase, hyphenated topic tags to the day file's `tags:` list (for example `presentation`, `template`, `physical-ai`).

An entry whose time carries a leading `~` was reconstructed afterwards (the backfill), not captured live.

## How capture works

`.claude/settings.json` registers a **UserPromptSubmit** hook, which Claude Code runs every time a prompt is submitted. The hook is `.claude/hooks/log_prompt.py`:

1. Reads the hook JSON from stdin (`prompt`, `session_id`, `cwd`).
2. Redacts obvious secrets.
3. Appends an entry to `prompt-log/YYYY/MM/YYYY-MM-DD.md`, creating the file if needed.

It writes into `PROMPT_LOG_DIR` if set, else `CLAUDE_PROJECT_DIR`, else the repo root above the script. It never blocks or slows a prompt: it prints nothing (UserPromptSubmit output is injected into Claude's context), swallows every error and always exits 0. It uses the standard library only (Python 3.8+).

### Limits

- **Only prompts, only in Claude Code.** Claude's replies and tool output are not captured, nor is anything typed in claude.ai or Claude Desktop chat.
- **It fails silently.** A missing Python or a wrong path means missing entries and no warning. After installing, send a prompt and check that today's file appeared.
- **It writes to the working copy it runs in.** In a Claude Code session on the web or on another machine, the entries sit in that copy until `prompt-log/` is committed and pushed with the session's branch.
- **Problem / Solution / Changed are not automatic.** They stay as placeholders until someone fills them in at session close. The root `CLAUDE.md` tells Claude to do this.
- **Redaction is best effort,** pattern matching only. It is not a guarantee.
- **The log is in git history once committed,** and removing something from history is hard. Treat every prompt as permanent.

## Capturing prompts from every repo (user level)

The project-level hook only fires in sessions opened in this repo. To capture prompts from every repo, register the same script at user level, pointing at a local clone of chinny_brain.

For example, with a clone at `C:/dev/chinny_brain` on Windows, put this in `~/.claude/settings.json` (merge it with what is already there):

```json
{
  "env": {
    "PROMPT_LOG_DIR": "C:/dev/chinny_brain"
  },
  "hooks": {
    "UserPromptSubmit": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "python3 \"$PROMPT_LOG_DIR/.claude/hooks/log_prompt.py\" --user || python \"$PROMPT_LOG_DIR/.claude/hooks/log_prompt.py\" --user"
          }
        ]
      }
    ]
  }
}
```

Adjust the path to wherever your clone actually lives; this repo does not assume one exists. Then:

- Keep `PROMPT_LOG_DIR` and the path in `command` pointing at the same clone, and keep the clone on a branch you are happy to commit to.
- `--user` makes the hook skip a prompt typed inside the clone itself, because the project-level hook there has already logged it. Without it, those prompts would be logged twice.
- The `||` is for Windows Git Bash, where only `python` exists. The hook always exits 0, so the second command runs only when `python3` is missing.
- Entries from other repos land in the clone's working tree. Commit and push them from there.

## Privacy

- **Never paste secrets, client documents or personal data into a prompt** you expect to be logged. Describe them, or name the file.
- The hook replaces these with `[REDACTED]`: Anthropic keys (`sk-ant-…`), GitHub tokens (`ghp_…`, `github_pat_…` and the other `gh?_` forms), `Bearer` tokens, AWS keys (`AKIA…`, `ASIA…`), Slack tokens, JSON Web Tokens, PEM private keys, RSGx Steer Co tokens (`rsgx_sc_…`) and the value in `password=…`, `secret=…`, `token=…` or `api_key=…`. It errs towards over-redacting.
- **Attachments are never stored,** only named (screenshots, PDFs, Word files). Do not name a client document if its title is itself sensitive.
- This repository is private and company-owned. Anything committed here follows the repository's own rules: nothing is deleted, and the secret scan runs over the full history.

## Vector-ready notes

- **One `## ` entry is one chunk.** The `> ` prefix stops a line inside a prompt from starting a heading, so splitting on lines that start with `## ` is always safe.
- **Chunk metadata** comes from outside the chunk. Take `date` from the day file's frontmatter (or its path), and `time`, `repo` and `session` from the entry header.
- **File metadata:** the frontmatter carries `date`, `type: prompt-log`, `owner` and a `tags` list.
- **Embed Prompt, Problem and Solution together.** Prompts are often short or dictated, and the framing makes them findable.
- **Skip placeholders.** An entry whose Problem still reads `_to fill at session close_` has not been framed yet.
- **Paths are stable.** A file's path is its identity; later edits only fill in the framing lines, add tags or add entries.
