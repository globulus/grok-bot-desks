from __future__ import annotations

import json
import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

from grok_bot_testkit.evidence import read_manifest
from grok_bot_testkit.pack import load_yaml
from grok_bot_testkit.paths import pack_dir, repo_root


@dataclass
class RuleResult:
    name: str
    severity: str  # hard | soft
    ok: bool
    message: str


@dataclass
class ScoreReport:
    bot_id: str
    run_dir: Path
    results: list[RuleResult] = field(default_factory=list)

    @property
    def hard_failures(self) -> list[RuleResult]:
        return [r for r in self.results if r.severity == "hard" and not r.ok]

    @property
    def soft_warnings(self) -> list[RuleResult]:
        return [r for r in self.results if r.severity == "soft" and not r.ok]

    @property
    def ok(self) -> bool:
        return not self.hard_failures


def _read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def _resolve_in_run(run_dir: Path, rel: str) -> Path:
    path = (run_dir / rel).resolve()
    if not str(path).startswith(str(run_dir.resolve())):
        raise ValueError(f"path escapes run dir: {rel}")
    return path


def _json_path(data: Any, dotted: str) -> Any:
    cur = data
    for part in dotted.split("."):
        if isinstance(cur, dict) and part in cur:
            cur = cur[part]
        else:
            raise KeyError(dotted)
    return cur


def _eval_rule(
    rule: dict[str, Any],
    *,
    run_dir: Path,
    pack_path: Path,
    manifest: dict[str, Any] | None,
) -> RuleResult:
    name = rule.get("name") or rule.get("type", "rule")
    severity = rule.get("severity", "hard")
    rtype = rule["type"]

    try:
        if rtype == "file_exists":
            path = _resolve_in_run(run_dir, rule["path"])
            ok = path.is_file()
            return RuleResult(name, severity, ok, f"file_exists {rule['path']}: {ok}")

        if rtype == "heading_present":
            path = _resolve_in_run(run_dir, rule["path"])
            text = _read_text(path)
            heading = rule["heading"]
            # Match ## Heading or # Heading at line start
            pattern = re.compile(
                rf"^#{{1,6}}\s+{re.escape(heading)}\s*$", re.MULTILINE
            )
            ok = bool(pattern.search(text)) or (f"# {heading}" in text) or (
                f"## {heading}" in text
            )
            return RuleResult(
                name, severity, ok, f"heading_present {heading!r} in {rule['path']}: {ok}"
            )

        if rtype == "regex_present":
            path = _resolve_in_run(run_dir, rule["path"])
            text = _read_text(path)
            ok = bool(re.search(rule["pattern"], text, re.MULTILINE | re.IGNORECASE))
            return RuleResult(
                name, severity, ok, f"regex_present {rule['pattern']!r}: {ok}"
            )

        if rtype == "regex_absent":
            path = _resolve_in_run(run_dir, rule["path"])
            text = _read_text(path)
            ok = not bool(re.search(rule["pattern"], text, re.MULTILINE | re.IGNORECASE))
            return RuleResult(
                name, severity, ok, f"regex_absent {rule['pattern']!r}: {ok}"
            )

        if rtype == "json_equals":
            path = _resolve_in_run(run_dir, rule["path"])
            data = json.loads(_read_text(path))
            actual = _json_path(data, rule["json_path"]) if "json_path" in rule else data
            expected = rule["equals"]
            ok = actual == expected
            return RuleResult(
                name, severity, ok, f"json_equals {rule.get('json_path', '.')}: {actual!r} == {expected!r}"
            )

        if rtype == "json_path":
            # alias: require path exists
            path = _resolve_in_run(run_dir, rule["path"])
            data = json.loads(_read_text(path))
            try:
                _json_path(data, rule["json_path"])
                ok = True
                msg = f"json_path {rule['json_path']} present"
            except KeyError:
                ok = False
                msg = f"json_path {rule['json_path']} missing"
            return RuleResult(name, severity, ok, msg)

        if rtype == "log_count":
            path = _resolve_in_run(run_dir, rule["path"])
            if not path.is_file():
                count = 0
            else:
                lines = [
                    ln
                    for ln in _read_text(path).splitlines()
                    if ln.strip() and not ln.strip().startswith("#")
                ]
                count = len(lines)
            expected = rule.get("equals", 0)
            ok = count == expected
            return RuleResult(
                name, severity, ok, f"log_count {rule['path']}: {count} == {expected}"
            )

        if rtype == "status_in":
            path = _resolve_in_run(run_dir, rule["path"])
            text = _read_text(path)
            allowed = set(rule["allowed"])
            # Find status-like tokens after | or : Status
            found: set[str] = set()
            for token in allowed:
                if re.search(rf"\b{re.escape(token)}\b", text):
                    found.add(token)
            # Also check explicit status column values
            if rule.get("require_any"):
                ok = bool(found & set(rule["require_any"]))
                return RuleResult(
                    name,
                    severity,
                    ok,
                    f"status_in require_any {rule['require_any']}: found {sorted(found)}",
                )
            # Default: every status-looking value in file must be allowed — use require_any for tracker
            ok = bool(found)
            return RuleResult(
                name, severity, ok, f"status_in allowed={sorted(allowed)} found={sorted(found)}"
            )

        if rtype == "strings_subset_of_fixture":
            path = _resolve_in_run(run_dir, rule["path"])
            text = _read_text(path)
            fixture = pack_path / rule["fixture"]
            if not fixture.is_file():
                # also try repo-relative
                alt = repo_root() / rule["fixture"]
                fixture = alt if alt.is_file() else fixture
            allow_source = _read_text(fixture)
            needles = rule.get("strings") or []
            # If extract_pattern given, pull candidates from artifact
            if "extract_pattern" in rule:
                needles = re.findall(rule["extract_pattern"], text)
            bad = [n for n in needles if n and n not in allow_source]
            ok = not bad
            return RuleResult(
                name,
                severity,
                ok,
                f"strings_subset_of_fixture bad={bad[:5]}" if bad else "strings_subset_of_fixture ok",
            )

        if rtype == "manifest_skills_include":
            if manifest is None:
                return RuleResult(name, severity, False, "manifest missing")
            required = set(rule["skills"])
            have = set(manifest.get("skills_run") or [])
            missing = sorted(required - have)
            ok = not missing
            return RuleResult(
                name, severity, ok, f"manifest_skills_include missing={missing}"
            )

        if rtype == "no_phone_like":
            path = _resolve_in_run(run_dir, rule["path"])
            text = _read_text(path)
            # Ignore known fixture placeholder language
            if "do not use" in text.lower() and "fixture" in text.lower():
                return RuleResult(name, severity, True, "no_phone_like skipped fixture note")
            from grok_bot_testkit.evidence import find_phone_like

            hits = find_phone_like(text)
            # Filter obvious non-phones (years ranges etc.) — keep simple
            ok = len(hits) == 0
            return RuleResult(name, severity, ok, f"no_phone_like hits={hits[:3]}")

        return RuleResult(name, severity, False, f"unknown rule type: {rtype}")
    except Exception as exc:  # noqa: BLE001 — surface as rule failure
        return RuleResult(name, severity, False, f"{rtype} error: {exc}")


def _rubric_path(pack_path: Path, rubric: str | Path | None) -> Path:
    if rubric is None:
        return pack_path / "rubric.yaml"
    given = Path(rubric)
    if given.is_file():
        return given
    under_pack = pack_path / given
    if under_pack.is_file():
        return under_pack
    return given


def score_run(
    bot_id: str,
    run_dir: Path,
    root: Path | None = None,
    rubric: str | Path | None = None,
) -> ScoreReport:
    run_dir = run_dir.resolve()
    pack_path = pack_dir(bot_id, root)
    rubric_file = _rubric_path(pack_path, rubric)
    rubric_data = load_yaml(rubric_file)
    if not isinstance(rubric_data, dict) or "rules" not in rubric_data:
        raise ValueError(f"{rubric_file}: must contain 'rules' list")

    manifest = None
    manifest_path = run_dir / "manifest.json"
    if manifest_path.is_file():
        manifest = read_manifest(run_dir)

    report = ScoreReport(bot_id=bot_id, run_dir=run_dir)
    for rule in rubric_data["rules"]:
        report.results.append(
            _eval_rule(rule, run_dir=run_dir, pack_path=pack_path, manifest=manifest)
        )
    return report


def print_report(report: ScoreReport) -> None:
    print(f"Score pack={report.bot_id} run={report.run_dir}")
    for r in report.results:
        mark = "PASS" if r.ok else ("WARN" if r.severity == "soft" else "FAIL")
        print(f"  [{mark}] ({r.severity}) {r.name}: {r.message}")
    if report.ok:
        print("Result: PASS")
    else:
        print(f"Result: FAIL ({len(report.hard_failures)} hard failure(s))")
