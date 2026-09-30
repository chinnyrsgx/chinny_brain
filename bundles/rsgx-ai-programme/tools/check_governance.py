#!/usr/bin/env python3
"""RSGx governance checks for an OKF v0.2 bundle.

Complements validate_okf.py, which checks OKF v0.2 conformance and the house
format rules (actors, timestamps, footnotes, links, secrets). This script
checks the rules that make provenance load-bearing:

  G1  provenance, where present, is C, P or I (also accepts [C]/[P]/[I] and
      confirmed/proposed/inferred)
  G2  P and I items carry an explicit status of draft or deprecated. Under
      OKF v0.2 s5.4 an absent status means stable, so it must be written out.
  G3  a ratification block, where present, is affirmative, signed by a
      human: actor, timestamped with a UTC offset, and cites a record (ref)
  G4  WARN  C items marked stable with no ratification block: confirmed in
            session, but Forum ratification is not evidenced
  G5  WARN  deprecated items with no superseded_by pointer
  G6  stale_after has passed: ERROR for files in the change set, WARN otherwise
  G7  WARN  duplicate id / legacy_id values
  G8  unresolved PLACEHOLDER: markers (the handover leaves these on purpose,
      so nothing ships half-filled)

Usage:
  check_governance.py BUNDLE [--changed-from REF] [--today YYYY-MM-DD]
  check_governance.py BUNDLE --stale-report [--today YYYY-MM-DD]

Check mode exits 1 if any ERROR is reported. Report mode always exits 0 and
prints a markdown shelf-life register (expired, due in 30 days, due in 90).
"""
import argparse
import datetime as dt
import os
import re
import subprocess
import sys

try:
    import yaml
except ImportError:  # pragma: no cover
    sys.exit("PyYAML required: pip install pyyaml")

RESERVED = {"index.md", "log.md"}
PROV_MAP = {"C": "C", "CONFIRMED": "C", "P": "P", "PROPOSED": "P", "I": "I", "INFERRED": "I"}
TS_RE = re.compile(r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}(:\d{2}(\.\d+)?)?(Z|[+-]\d{2}:\d{2})$")
HUMAN_RE = re.compile(r"^human:[a-z0-9._-]+$")
PLACEHOLDER = "PLACEHOLDER:"


def parse(path):
    text = open(path, encoding="utf-8").read()
    if not text.startswith("---\n"):
        return None, text
    end = text.find("\n---\n", 4)
    if end == -1:
        return None, text
    try:
        return (yaml.safe_load(text[4:end]) or {}), text
    except yaml.YAMLError:
        return None, text


def to_dt(value):
    """Return an aware datetime for a YAML timestamp or ISO string, else None."""
    if isinstance(value, dt.datetime):
        return value if value.tzinfo else None
    if isinstance(value, str) and TS_RE.match(value.strip()):
        return dt.datetime.fromisoformat(value.strip().replace("Z", "+00:00"))
    return None


def norm_prov(value):
    return PROV_MAP.get(str(value).strip().strip("[]").upper())


def changed_files(bundle, ref):
    top = subprocess.run(["git", "-C", bundle, "rev-parse", "--show-toplevel"],
                         capture_output=True, text=True, check=True).stdout.strip()
    out = subprocess.run(["git", "-C", top, "diff", "--name-only", "--diff-filter=AMR", ref, "HEAD"],
                         capture_output=True, text=True, check=True).stdout
    return {os.path.realpath(os.path.join(top, p)) for p in out.splitlines() if p}


def concepts(bundle):
    for dp, dirs, files in os.walk(bundle):
        dirs[:] = sorted(d for d in dirs if not d.startswith(".") and d != "__pycache__")
        for f in sorted(files):
            if f.endswith(".md") and f not in RESERVED:
                p = os.path.join(dp, f)
                yield p, os.path.relpath(p, bundle)


def check(bundle, now, changed):
    errors, warns, seen = [], [], {}

    def err(code, rel, msg):
        errors.append(f"ERROR [{code}] {rel}: {msg}")

    def warn(code, rel, msg):
        warns.append(f"WARN  [{code}] {rel}: {msg}")

    n = 0
    for path, rel in concepts(bundle):
        fm, text = parse(path)
        if PLACEHOLDER in text:
            err("G8", rel, "unresolved PLACEHOLDER: marker; complete it before merging")
        if fm is None:
            continue  # frontmatter conformance is validate_okf.py's job
        n += 1
        status = fm.get("status", "stable")
        prov_raw = fm.get("provenance")
        prov = norm_prov(prov_raw) if prov_raw is not None else None

        if prov_raw is not None and prov is None:
            err("G1", rel, f"provenance `{prov_raw}` is not C, P or I")
        if prov in ("P", "I") and "status" not in fm:
            err("G2", rel, f"[{prov}] item has no explicit status; OKF reads absent status as stable")
        elif prov in ("P", "I") and status == "stable":
            err("G2", rel, f"[{prov}] item is marked stable; proposals and inferences must stay draft")

        rat = fm.get("ratification")
        if rat is not None:
            if not isinstance(rat, dict):
                err("G3", rel, "ratification must be a mapping")
            else:
                if rat.get("mode") != "affirmative":
                    err("G3", rel, "ratification.mode must be `affirmative`; silence or no-objection never ratifies")
                if not HUMAN_RE.match(str(rat.get("by", ""))):
                    err("G3", rel, "ratification.by must be a human:<id> actor")
                if to_dt(rat.get("at")) is None:
                    err("G3", rel, "ratification.at must be an ISO 8601 datetime with a UTC offset")
                if not str(rat.get("ref", "")).strip():
                    err("G3", rel, "ratification.ref must cite the minute or record that evidences it")
        elif prov == "C" and status == "stable":
            warn("G4", rel, "confirmed and stable, but no ratification block evidences Forum ratification")

        if status == "deprecated" and not fm.get("superseded_by"):
            warn("G5", rel, "deprecated without superseded_by; readers cannot find the replacement")

        sa = fm.get("stale_after")
        if sa is not None:
            sa_dt = to_dt(sa)
            if sa_dt is not None and now >= sa_dt:
                msg = f"past stale_after ({sa_dt.date()}); re-verify and reset, or deprecate"
                if changed is not None and os.path.realpath(path) in changed:
                    err("G6", rel, msg + " (edited in this change set)")
                else:
                    warn("G6", rel, msg)

        for key in ("id", "legacy_id"):
            v = fm.get(key)
            if v is not None:
                seen.setdefault((key, str(v)), []).append(rel)

    for (key, v), rels in sorted(seen.items()):
        if len(rels) > 1:
            warn("G7", ", ".join(rels), f"duplicate {key} `{v}`")

    for line in errors + warns:
        print(line)
    print(f"\n{n} concepts checked: {len(errors)} error(s), {len(warns)} warning(s)")
    return 1 if errors else 0


def stale_report(bundle, now):
    rows = []
    for path, rel in concepts(bundle):
        fm, _ = parse(path)
        if not fm or fm.get("status") == "deprecated":
            continue
        sa_dt = to_dt(fm.get("stale_after"))
        if sa_dt is None:
            continue
        days = (sa_dt - now).total_seconds() / 86400
        state = "EXPIRED" if days <= 0 else "Due ≤30 days" if days <= 30 else "Due ≤90 days" if days <= 90 else None
        if state:
            rows.append((days, state, rel, fm.get("type", ""), sa_dt.date().isoformat()))
    name = os.path.basename(os.path.normpath(bundle))
    print(f"## Shelf-life register: `{name}` (as at {now.date().isoformat()})\n")
    if not rows:
        print("No concepts expired or due for re-verification within 90 days.\n")
        return 0
    print("| State | Concept | Type | Re-verify by |\n|---|---|---|---|")
    for _, state, rel, typ, date in sorted(rows):
        print(f"| {state} | `{rel}` | {typ} | {date} |")
    print("\nRe-verify against primary sources, then record a new `verified` event and reset "
          "`stale_after` in a PR, or deprecate the concept with `superseded_by`.\n")
    return 0


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("bundle")
    ap.add_argument("--changed-from", metavar="REF", help="git ref; files changed since REF are held to G6 as errors")
    ap.add_argument("--stale-report", action="store_true", help="print the shelf-life register and exit 0")
    ap.add_argument("--today", metavar="YYYY-MM-DD", help="override the current date (testing)")
    a = ap.parse_args()
    now = (dt.datetime.fromisoformat(a.today).replace(tzinfo=dt.timezone.utc) if a.today
           else dt.datetime.now(dt.timezone.utc))
    if not os.path.isdir(a.bundle):
        sys.exit(f"not a directory: {a.bundle}")
    if a.stale_report:
        return stale_report(a.bundle, now)
    changed = changed_files(a.bundle, a.changed_from) if a.changed_from else None
    return check(a.bundle, now, changed)


if __name__ == "__main__":
    sys.exit(main())
