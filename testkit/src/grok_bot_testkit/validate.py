from __future__ import annotations

import re
from dataclasses import dataclass, field
from pathlib import Path

from grok_bot_testkit.pack import (
    REQUIRED_PACK_FILES,
    list_pack_ids,
    load_bot_yaml,
    load_yaml,
    validate_bot_yaml_shape,
)
from grok_bot_testkit.paths import pack_dir, repo_root, skills_dir


FRONTMATTER_RE = re.compile(r"^---\s*\n(.*?)\n---\s*\n", re.DOTALL)

REQUIRED_SKILL_SECTIONS = (
    "When to use",
    "Approval bar",
)


@dataclass
class ValidationReport:
    errors: list[str] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)

    @property
    def ok(self) -> bool:
        return not self.errors


def _parse_frontmatter(text: str) -> dict[str, str]:
    m = FRONTMATTER_RE.match(text)
    if not m:
        return {}
    data: dict[str, str] = {}
    for line in m.group(1).splitlines():
        if ":" not in line:
            continue
        key, val = line.split(":", 1)
        data[key.strip()] = val.strip()
    return data


def validate_skills(root: Path | None = None) -> ValidationReport:
    report = ValidationReport()
    base = skills_dir(root)
    if not base.is_dir():
        report.errors.append(f"skills/ missing at {base}")
        return report
    for skill_dir in sorted(p for p in base.iterdir() if p.is_dir()):
        skill_md = skill_dir / "SKILL.md"
        if not skill_md.is_file():
            report.errors.append(f"{skill_dir.name}: missing SKILL.md")
            continue
        text = skill_md.read_text(encoding="utf-8")
        fm = _parse_frontmatter(text)
        if "name" not in fm:
            report.errors.append(f"{skill_md}: frontmatter missing name")
        elif fm["name"] != skill_dir.name:
            report.warnings.append(
                f"{skill_md}: name {fm['name']!r} != directory {skill_dir.name!r}"
            )
        if "description" not in fm:
            report.errors.append(f"{skill_md}: frontmatter missing description")
        for section in REQUIRED_SKILL_SECTIONS:
            if f"## {section}" not in text:
                report.errors.append(f"{skill_md}: missing section '## {section}'")
        if (
            "## Sequence" not in text
            and "## File format" not in text
            and "## Required sections" not in text
            and "## Output format" not in text
        ):
            report.warnings.append(
                f"{skill_md}: no Sequence / File format / Required sections / Output format"
            )
    return report


def validate_testpacks(root: Path | None = None) -> ValidationReport:
    report = ValidationReport()
    root = root or repo_root()
    ids = list_pack_ids(root)
    if not ids:
        report.errors.append("no testpacks found")
        return report

    ports: dict[int, str] = {}
    for bot_id in ids:
        path = pack_dir(bot_id, root)
        for req in REQUIRED_PACK_FILES:
            if not (path / req).is_file():
                report.errors.append(f"{bot_id}: missing {req}")

        try:
            bot = load_bot_yaml(bot_id, root)
        except Exception as exc:  # noqa: BLE001
            report.errors.append(f"{bot_id}: bot.yaml load error: {exc}")
            continue

        report.errors.extend(validate_bot_yaml_shape(bot, path / "bot.yaml"))

        if bot.get("id") != bot_id:
            report.errors.append(
                f"{bot_id}: bot.yaml id {bot.get('id')!r} must match directory name"
            )

        port = bot.get("port")
        if isinstance(port, int):
            if port in ports:
                report.errors.append(
                    f"{bot_id}: port {port} already used by {ports[port]}"
                )
            else:
                ports[port] = bot_id

        for skill in bot.get("skills") or []:
            if not (skills_dir(root) / skill / "SKILL.md").is_file():
                report.errors.append(f"{bot_id}: skill '{skill}' not found under skills/")

        for key, rel in (bot.get("artifacts") or {}).items():
            if not isinstance(rel, str):
                report.errors.append(f"{bot_id}: artifact {key} path must be string")

        for route in bot.get("routes") or []:
            if route.get("handler") == "static" and route.get("file"):
                site = path / "sites" / route["file"]
                if not site.is_file():
                    report.errors.append(
                        f"{bot_id}: route {route.get('path')} file missing: sites/{route['file']}"
                    )
            if route.get("handler") == "login_wall" and route.get("file"):
                site = path / "sites" / route["file"]
                if not site.is_file():
                    report.errors.append(
                        f"{bot_id}: login_wall file missing: sites/{route['file']}"
                    )

        fixtures = path / "fixtures"
        if not fixtures.is_dir():
            report.warnings.append(f"{bot_id}: no fixtures/ directory")

        try:
            rubric = load_yaml(path / "rubric.yaml")
        except Exception as exc:  # noqa: BLE001
            report.errors.append(f"{bot_id}: rubric.yaml error: {exc}")
            continue
        if not isinstance(rubric, dict) or not isinstance(rubric.get("rules"), list):
            report.errors.append(f"{bot_id}: rubric.yaml must have rules: list")
            continue
        for i, rule in enumerate(rubric["rules"]):
            if not isinstance(rule, dict) or "type" not in rule:
                report.errors.append(f"{bot_id}: rules[{i}] needs type")
                continue
            if rule["type"] == "strings_subset_of_fixture":
                fix = rule.get("fixture")
                if fix and not (path / fix).is_file() and not (root / fix).is_file():
                    report.errors.append(
                        f"{bot_id}: rules[{i}] fixture not found: {fix}"
                    )

    return report


def validate_all(root: Path | None = None) -> ValidationReport:
    root = root or repo_root()
    combined = ValidationReport()
    for part in (validate_skills(root), validate_testpacks(root)):
        combined.errors.extend(part.errors)
        combined.warnings.extend(part.warnings)
    return combined


def print_validation(report: ValidationReport) -> None:
    for w in report.warnings:
        print(f"WARN: {w}")
    for e in report.errors:
        print(f"ERROR: {e}")
    if report.ok:
        print("Validation: PASS")
    else:
        print(f"Validation: FAIL ({len(report.errors)} error(s))")
