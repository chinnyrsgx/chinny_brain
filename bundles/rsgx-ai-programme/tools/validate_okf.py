#!/usr/bin/env python3
"""OKF v0.2 conformance check for a bundle: python validate_okf.py <bundle-dir>

Vendored from rsgx-org-ai/rsgx-okf-indexer @ 33ba2e8, src/okf_indexer/validate/gates.py
(the indexer's "Phase 4 validation gates 1-5"), copied 14/10/2026 because no validate_okf.py
exists in rsgx-org-ai/rsgx-okf or anywhere else in the org. One change from the original: the
Anthropic key pattern is built by concatenation so this file, which sits inside the bundle and
is scanned too, does not flag itself. Everything else is verbatim; re-copy rather than edit.

Gates: 1 conformance (parseable frontmatter with a non-empty `type` on every non-reserved .md),
2 reserved files (bundle-root index.md frontmatter is exactly {okf_version}; log.md and other
index.md files have none), 3 secrets (regex scan, plus gitleaks when installed), 4 provenance
(`sources` entries have a resource; every cited footnote is defined), 5 actor syntax. Broken
bundle-relative links are notes, never failures. House governance rules (provenance C/P/I,
ratification, shelf life) are check_governance.py's job, not this file's.

Exit status: 0 when every gate passes, 1 on any violation, 2 on bad arguments.
"""

from __future__ import annotations

import json
import re
import shutil
import subprocess
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import yaml

RESERVED_NAMES = {"index.md", "log.md"}

SECRET_PATTERNS: list[tuple[str, re.Pattern[str]]] = [
    ("anthropic_api_key", re.compile("sk" + "-ant-")),  # split so this file does not match itself
    ("github_pat", re.compile(r"ghp_[A-Za-z0-9]")),
    ("github_oauth_token", re.compile(r"gho_[A-Za-z0-9]")),
    ("aws_access_key_id", re.compile(r"AKIA[0-9A-Z]{16}")),
    ("private_key_pem", re.compile(r"-----BEGIN (?:[A-Z ]+ )?PRIVATE KEY-----")),
    ("dsn_with_credentials", re.compile(r"://[^/\s:]+:[^/\s@]+@")),
]

ACTOR_RE = re.compile(
    r"^(?:human:[^\s]+|process:[^\s]+|[A-Za-z0-9._-]+/[A-Za-z0-9._+-]+)$"
)

_INLINE_FOOTNOTE = re.compile(r"\[\^([^\]]+)\](?!:)")
_FOOTNOTE_DEF = re.compile(r"^\[\^([^\]]+)\]:\s*(.*)$", re.MULTILINE)
_LINK_RE = re.compile(r"\[[^\]]*\]\(([^)]+)\)")


@dataclass(frozen=True)
class Violation:
    gate: str
    path: str
    message: str

    def __str__(self) -> str:
        return f"[{self.gate}] {self.path}: {self.message}"


@dataclass
class Report:
    violations: list[Violation]
    notes: list[str]
    files_checked: int

    @property
    def ok(self) -> bool:
        return not self.violations


def iter_files(root: Path) -> list[Path]:
    return sorted(p for p in root.rglob("*") if p.is_file())


def split_frontmatter(text: str) -> tuple[str | None, str]:
    """Return ``(frontmatter_yaml_or_None, body)``."""
    normalised = text.replace("\r\n", "\n")
    if not normalised.startswith("---\n"):
        return None, normalised
    end = normalised.find("\n---", 3)
    if end == -1:
        return None, normalised
    return normalised[4:end], normalised[end + 4 :].lstrip("\n")


# --------------------------------------------------------------------------
# Gate 1 + 2: conformance and reserved files
# --------------------------------------------------------------------------


def gate_conformance(root: Path) -> tuple[list[Violation], dict[Path, dict[str, Any]]]:
    violations: list[Violation] = []
    parsed: dict[Path, dict[str, Any]] = {}
    for path in iter_files(root):
        if path.suffix != ".md" or path.name in RESERVED_NAMES:
            continue
        rel = path.relative_to(root).as_posix()
        raw, _ = split_frontmatter(path.read_text(encoding="utf-8"))
        if raw is None:
            violations.append(Violation("1-conformance", rel, "missing YAML frontmatter block"))
            continue
        try:
            data = yaml.safe_load(raw)
        except yaml.YAMLError as exc:
            violations.append(
                Violation("1-conformance", rel, f"frontmatter is not valid YAML: {exc}")
            )
            continue
        if not isinstance(data, dict):
            violations.append(
                Violation("1-conformance", rel, "frontmatter must parse to a mapping")
            )
            continue
        parsed[path] = data
        type_value = data.get("type")
        if not isinstance(type_value, str) or not type_value.strip():
            violations.append(
                Violation("1-conformance", rel, "frontmatter 'type' is missing or empty")
            )
    return violations, parsed


def gate_reserved(root: Path) -> list[Violation]:
    violations: list[Violation] = []
    for path in iter_files(root):
        if path.name not in RESERVED_NAMES:
            continue
        rel = path.relative_to(root).as_posix()
        raw, _ = split_frontmatter(path.read_text(encoding="utf-8"))
        is_bundle_root_index = rel == "index.md"
        if is_bundle_root_index:
            if raw is None:
                violations.append(
                    Violation("2-reserved", rel, "bundle-root index.md must have frontmatter")
                )
                continue
            try:
                data = yaml.safe_load(raw)
            except yaml.YAMLError as exc:
                violations.append(Violation("2-reserved", rel, f"invalid YAML: {exc}"))
                continue
            if not isinstance(data, dict) or set(data) != {"okf_version"}:
                keys = sorted(data) if isinstance(data, dict) else []
                violations.append(
                    Violation(
                        "2-reserved",
                        rel,
                        f"bundle-root index.md frontmatter must be exactly {{okf_version}}, got {keys}",
                    )
                )
        elif raw is not None:
            violations.append(
                Violation("2-reserved", rel, f"reserved file '{path.name}' must have no frontmatter")
            )
    return violations


# --------------------------------------------------------------------------
# Gate 3: secrets (hard fail)
# --------------------------------------------------------------------------


def gate_secrets(root: Path) -> tuple[list[Violation], list[str]]:
    violations: list[Violation] = []
    notes: list[str] = []
    for path in iter_files(root):
        rel = path.relative_to(root).as_posix()
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            notes.append(f"gate 3: skipped non-UTF-8 file {rel}")
            continue
        for lineno, line in enumerate(text.splitlines(), start=1):
            for name, pattern in SECRET_PATTERNS:
                if pattern.search(line):
                    violations.append(
                        Violation(
                            "3-secrets",
                            rel,
                            f"line {lineno} matches secret pattern '{name}' (HARD FAIL)",
                        )
                    )

    if shutil.which("gitleaks"):
        result = _run_gitleaks(root)
        violations.extend(result[0])
        notes.extend(result[1])
    else:
        notes.append(
            "gate 3: gitleaks binary not found on PATH -- reported as a coverage gap, "
            "not a failure; the regex scan above is the mandatory minimum."
        )
    return violations, notes


def _run_gitleaks(root: Path) -> tuple[list[Violation], list[str]]:
    report_path = root.parent / ".gitleaks-report.json"
    cmd = [
        "gitleaks",
        "detect",
        "--no-git",
        "--source",
        str(root),
        "--report-format",
        "json",
        "--report-path",
        str(report_path),
        "--exit-code",
        "0",
    ]
    try:
        subprocess.run(cmd, capture_output=True, check=False, timeout=300)
    except (OSError, subprocess.SubprocessError) as exc:
        return [], [f"gate 3: gitleaks invocation failed ({exc}); regex scan still applied"]

    violations: list[Violation] = []
    notes = ["gate 3: gitleaks scan ran"]
    if report_path.exists():
        try:
            findings = json.loads(report_path.read_text(encoding="utf-8") or "[]")
        except json.JSONDecodeError:
            findings = []
            notes.append("gate 3: gitleaks report was unparseable")
        for finding in findings or []:
            file_ref = str(finding.get("File", "?"))
            violations.append(
                Violation(
                    "3-secrets",
                    file_ref,
                    f"gitleaks rule '{finding.get('RuleID', '?')}' "
                    f"at line {finding.get('StartLine', '?')} (HARD FAIL)",
                )
            )
        report_path.unlink()
    return violations, notes


# --------------------------------------------------------------------------
# Gate 4: provenance
# --------------------------------------------------------------------------


def gate_provenance(root: Path, parsed: dict[Path, dict[str, Any]]) -> list[Violation]:
    violations: list[Violation] = []
    for path in sorted(parsed):
        rel = path.relative_to(root).as_posix()
        data = parsed[path]
        _, body = split_frontmatter(path.read_text(encoding="utf-8"))

        source_ids: set[str] = set()
        sources = data.get("sources")
        if sources is not None:
            if not isinstance(sources, list):
                violations.append(Violation("4-provenance", rel, "'sources' must be a list"))
            else:
                for index, entry in enumerate(sources):
                    if not isinstance(entry, dict):
                        violations.append(
                            Violation("4-provenance", rel, f"sources[{index}] is not a mapping")
                        )
                        continue
                    resource = entry.get("resource")
                    if not isinstance(resource, str) or not resource.strip():
                        violations.append(
                            Violation(
                                "4-provenance",
                                rel,
                                f"sources[{index}] (id={entry.get('id')!r}) "
                                "has an empty or missing 'resource'",
                            )
                        )
                    identifier = entry.get("id")
                    if isinstance(identifier, str) and identifier:
                        source_ids.add(identifier)

        defined = {m.group(1) for m in _FOOTNOTE_DEF.finditer(body)}
        for match in _FOOTNOTE_DEF.finditer(body):
            if not match.group(2).strip():
                violations.append(
                    Violation(
                        "4-provenance",
                        rel,
                        f"footnote definition '[^{match.group(1)}]' has an empty target",
                    )
                )
        for ref in sorted({m.group(1) for m in _INLINE_FOOTNOTE.finditer(body)}):
            if ref not in source_ids and ref not in defined:
                violations.append(
                    Violation(
                        "4-provenance",
                        rel,
                        f"cited footnote '[^{ref}]' is in neither the sources list "
                        "nor a References definition",
                    )
                )
    return violations


# --------------------------------------------------------------------------
# Gate 5: actor syntax
# --------------------------------------------------------------------------


def gate_actors(root: Path, parsed: dict[Path, dict[str, Any]]) -> list[Violation]:
    violations: list[Violation] = []
    for path in sorted(parsed):
        rel = path.relative_to(root).as_posix()
        data = parsed[path]

        def check(value: Any, field: str, rel: str = rel) -> None:
            if not isinstance(value, str) or not ACTOR_RE.match(value):
                violations.append(
                    Violation(
                        "5-actors",
                        rel,
                        f"{field} value {value!r} is not human:<id>, process:<id> "
                        "or <producer>/<version>",
                    )
                )

        if "owner" in data:
            check(data["owner"], "owner")
        contributors = data.get("contributors")
        if contributors is not None:
            if not isinstance(contributors, list):
                violations.append(Violation("5-actors", rel, "'contributors' must be a list"))
            else:
                for index, value in enumerate(contributors):
                    check(value, f"contributors[{index}]")
        generated = data.get("generated")
        if isinstance(generated, dict) and "by" in generated:
            check(generated["by"], "generated.by")
    return violations


# --------------------------------------------------------------------------
# Non-fatal: bundle-relative links
# --------------------------------------------------------------------------


def check_links(root: Path) -> list[str]:
    """Broken bundle-relative links are explicitly non-fatal: notes only."""
    notes: list[str] = []
    for path in iter_files(root):
        if path.suffix != ".md":
            continue
        rel = path.relative_to(root).as_posix()
        text = path.read_text(encoding="utf-8")
        for match in _LINK_RE.finditer(text):
            target = match.group(1).split("#", 1)[0].strip()
            if not target or "://" in target or target.startswith(("mailto:", "/")):
                continue
            if not (path.parent / target).resolve().exists():
                notes.append(f"note (non-fatal): {rel} links to missing '{target}'")
    return notes


# --------------------------------------------------------------------------
# Runner
# --------------------------------------------------------------------------


def validate_bundle(root: Path) -> Report:
    if not root.exists():
        return Report([Violation("0-bundle", str(root), "bundle directory does not exist")], [], 0)

    violations: list[Violation] = []
    notes: list[str] = []

    conformance, parsed = gate_conformance(root)
    violations.extend(conformance)
    violations.extend(gate_reserved(root))
    secret_violations, secret_notes = gate_secrets(root)
    violations.extend(secret_violations)
    notes.extend(secret_notes)
    violations.extend(gate_provenance(root, parsed))
    violations.extend(gate_actors(root, parsed))
    notes.extend(check_links(root))

    violations.sort(key=lambda v: (v.gate, v.path, v.message))
    return Report(violations, notes, len(iter_files(root)))


def format_report(report: Report, root: Path) -> str:
    lines = [f"OKF bundle validation: {root}", f"Files checked: {report.files_checked}", ""]
    if report.violations:
        lines.append(f"FAIL -- {len(report.violations)} violation(s):")
        lines.extend(f"  {v}" for v in report.violations)
    else:
        lines.append("PASS -- gates 1-5 clean (gate 6 determinism is a pytest-only check).")
    if report.notes:
        lines.extend(["", "Notes:"])
        lines.extend(f"  {n}" for n in report.notes)
    return "\n".join(lines)


__all__ = [
    "ACTOR_RE",
    "SECRET_PATTERNS",
    "Report",
    "Violation",
    "format_report",
    "gate_actors",
    "gate_conformance",
    "gate_provenance",
    "gate_reserved",
    "gate_secrets",
    "split_frontmatter",
    "validate_bundle",
]


def main(argv: list[str]) -> int:
    if len(argv) != 2:
        print("usage: python validate_okf.py <bundle-dir>")
        return 2
    root = Path(argv[1]).resolve()
    report = validate_bundle(root)
    print(format_report(report, root))
    return 0 if report.ok else 1


if __name__ == "__main__":
    import sys

    sys.exit(main(sys.argv))
