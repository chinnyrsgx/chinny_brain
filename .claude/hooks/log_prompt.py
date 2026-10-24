#!/usr/bin/env python3
"""Claude Code UserPromptSubmit hook: append every prompt to a daily Markdown log.

Writes to  <dir>/prompt-log/YYYY/MM/YYYY-MM-DD.md  using the AWST (Australia/Perth,
UTC+8, no daylight saving) date. See prompt-log/README.md for the entry format.

Target directory <dir>, first that is set and non-empty:
  1. env PROMPT_LOG_DIR      (a local clone of chinny_brain; used by the user-level hook)
  2. env CLAUDE_PROJECT_DIR  (set by Claude Code; used by the project-level hook)
  3. the repo root two levels above this script

Options:
  --user   Registered at user level. Do nothing when the current project IS the log
           repo, because that repo's own project-level hook already logs the prompt
           (otherwise every prompt typed inside chinny_brain would be logged twice).

Rules this hook keeps:
  * It must never block or slow a prompt: everything is wrapped, it always exits 0.
  * It prints nothing. UserPromptSubmit stdout is injected into Claude's context.
  * Obvious secrets are redacted before anything is written (best effort, see REDACTIONS).
  * Standard library only, Python 3.8+.

Testing only: env PROMPT_LOG_NOW=<ISO 8601 UTC time>, e.g. 2026-10-12T23:36:00Z, fixes the clock.
"""
import json
import os
import re
import sys
from datetime import datetime, timedelta, timezone

AWST = timedelta(hours=8)  # Australia/Perth has no daylight saving, so a fixed offset is exact.
PLACEHOLDER = "_to fill at session close_"

# Order matters: whole-token patterns first, then the generic key=value rule.
# Over-redacting is preferred to leaking.
_TOKEN_CHARS = r"[A-Za-z0-9_\-]"
REDACTIONS = [
    # PEM private keys (header to footer, or to the end of the prompt if truncated)
    (re.compile(r"-----BEGIN [A-Z ]*PRIVATE KEY-----.*?(?:-----END [A-Z ]*PRIVATE KEY-----|\Z)", re.S), "[REDACTED]"),
    # Anthropic API keys
    (re.compile(r"(?<![A-Za-z0-9])sk-ant-" + _TOKEN_CHARS + r"+"), "[REDACTED]"),
    # GitHub tokens: fine-grained PATs, then ghp_/gho_/ghu_/ghs_/ghr_
    (re.compile(r"(?<![A-Za-z0-9])github_pat_[A-Za-z0-9_]+"), "[REDACTED]"),
    (re.compile(r"(?<![A-Za-z0-9])gh[pousr]_[A-Za-z0-9]{16,}"), "[REDACTED]"),
    # RSGx Steer Co MCP personal access tokens
    (re.compile(r"(?<![A-Za-z0-9])rsgx_sc_" + _TOKEN_CHARS + r"+"), "[REDACTED]"),
    # AWS access key ids (long-lived AKIA, temporary ASIA)
    (re.compile(r"(?<![A-Za-z0-9])(?:AKIA|ASIA)[0-9A-Z]{16}(?![A-Za-z0-9])"), "[REDACTED]"),
    # Slack tokens and JSON Web Tokens
    (re.compile(r"(?<![A-Za-z0-9])xox[abposr]-[A-Za-z0-9\-]{10,}"), "[REDACTED]"),
    (re.compile(r"(?<![A-Za-z0-9])eyJ[A-Za-z0-9_\-]{8,}\.[A-Za-z0-9_\-]{8,}\.[A-Za-z0-9_\-]{8,}"), "[REDACTED]"),
    # Authorization headers: keep the word Bearer, drop the token
    (re.compile(r"\b[Bb]earer\s+[A-Za-z0-9._~+/=\-]{12,}"), "Bearer [REDACTED]"),
    # password=..., secret: ..., "token": "...", api_key=... (key kept, value dropped)
    (
        re.compile(
            r"(?i)\b(password|passwd|secret|token|api[_-]?key|client[_-]?secret)"
            r"([\"']?\s*[=:]\s*)"
            r"(?:\"[^\"\n]*\"|'[^'\n]*'|[^\s\"',;&]+)"
        ),
        r"\1\2[REDACTED]",
    ),
]


def redact(text):
    for pattern, replacement in REDACTIONS:
        text = pattern.sub(replacement, text)
    return text


def now_utc():
    forced = os.environ.get("PROMPT_LOG_NOW", "").strip()
    if forced:
        try:
            parsed = datetime.fromisoformat(forced.replace("Z", "+00:00"))
            if parsed.tzinfo is None:
                parsed = parsed.replace(tzinfo=timezone.utc)
            return parsed.astimezone(timezone.utc)
        except ValueError:
            pass
    return datetime.now(timezone.utc)


def clean_label(value, limit=80):
    """One short, single-line, header-safe label."""
    value = re.sub(r"[\x00-\x1f\x7f]+", " ", str(value)).replace("·", "-").strip()
    return value[:limit]


def repo_name(cwd):
    """Name of the repo folder containing cwd (nearest ancestor with .git), else cwd's own name."""
    if not cwd:
        cwd = os.getcwd()
    cwd = str(cwd)
    try:
        probe = cwd if os.path.isabs(cwd) else ""  # a path from another OS is not walked
        for _ in range(25 if probe else 0):
            if os.path.exists(os.path.join(probe, ".git")):
                return clean_label(os.path.basename(probe) or probe)
            parent = os.path.dirname(probe)
            if parent == probe:
                break
            probe = parent
    except Exception:
        pass
    parts = [p for p in re.split(r"[\\/]+", cwd) if p]
    return clean_label(parts[-1]) if parts else "unknown"


def script_root():
    here = os.path.dirname(os.path.abspath(__file__))
    return os.path.dirname(os.path.dirname(here))  # .claude/hooks -> .claude -> repo root


def target_dir():
    for name in ("PROMPT_LOG_DIR", "CLAUDE_PROJECT_DIR"):
        value = os.environ.get(name, "").strip()
        if value:
            return os.path.expanduser(os.path.expandvars(value))
    return script_root()


def same_dir(a, b):
    def norm(p):
        return os.path.normcase(os.path.realpath(os.path.expanduser(p)))
    return norm(a) == norm(b)


def read_payload():
    stream = sys.stdin
    if stream is None or stream.isatty():
        return {}
    raw = stream.buffer.read()
    try:
        data = json.loads(raw.decode("utf-8-sig", "replace"))
    except ValueError:
        return {}
    return data if isinstance(data, dict) else {}


def day_file_header(local):
    return (
        "---\n"
        "date: " + local.strftime("%Y-%m-%d") + "\n"
        "type: prompt-log\n"
        "owner: human:cchin\n"
        "tags: []\n"
        "---\n"
        "\n"
        "# Prompt log, " + local.strftime("%d/%m/%Y") + "\n"
        "\n"
    )


def build_entry(prompt, repo, session, utc, local):
    quoted = "\n".join(
        (">" if line == "" else "> " + line) for line in re.split(r"\r\n|\r|\n", prompt)
    )
    return (
        "## {lh}:{lm} AWST ({uh}:{um} UTC) · {repo} · session {session}\n"
        "\n"
        "**Prompt:**\n"
        "{quoted}\n"
        "\n"
        "**Problem:** {ph}\n"
        "**Solution:** {ph}\n"
        "**Changed:** {ph}\n"
        "\n"
    ).format(
        lh=local.strftime("%H"), lm=local.strftime("%M"),
        uh=utc.strftime("%H"), um=utc.strftime("%M"),
        repo=repo, session=session, quoted=quoted, ph=PLACEHOLDER,
    )


def separator(path):
    """Newlines needed so a new entry starts after exactly one blank line."""
    try:
        with open(path, "rb") as handle:
            handle.seek(0, os.SEEK_END)
            size = handle.tell()
            handle.seek(max(0, size - 2))
            tail = handle.read()
    except OSError:
        return ""
    if tail.endswith(b"\n\n"):
        return ""
    return "\n" if tail.endswith(b"\n") else "\n\n"


def log_prompt(data, user_level):
    prompt = data.get("prompt")
    if not isinstance(prompt, str) or not prompt.strip():
        return
    base = target_dir()
    project = os.environ.get("CLAUDE_PROJECT_DIR", "").strip()
    if user_level and project and same_dir(project, base):
        return  # the project-level hook of the log repo handles this prompt

    utc = now_utc()
    local = utc + AWST
    session = re.sub(r"[^A-Za-z0-9_\-]", "", str(data.get("session_id") or ""))[:8] or "unknown"
    repo = repo_name(data.get("cwd") if isinstance(data.get("cwd"), str) else "")
    entry = build_entry(redact(prompt), repo, session, utc, local)

    folder = os.path.join(base, "prompt-log", local.strftime("%Y"), local.strftime("%m"))
    os.makedirs(folder, exist_ok=True)
    path = os.path.join(folder, local.strftime("%Y-%m-%d") + ".md")
    try:
        with open(path, "x", encoding="utf-8", newline="\n") as handle:
            handle.write(day_file_header(local))
    except FileExistsError:
        pass
    prefix = separator(path)
    with open(path, "a", encoding="utf-8", newline="\n") as handle:
        handle.write(prefix + entry)


def main():
    try:
        sys.stdout = open(os.devnull, "w")  # nothing may reach Claude's context
        sys.stderr = open(os.devnull, "w")
    except Exception:
        pass
    try:
        log_prompt(read_payload(), "--user" in sys.argv[1:])
    except BaseException:  # never block or slow a prompt, whatever goes wrong
        pass
    sys.exit(0)


if __name__ == "__main__":
    main()
