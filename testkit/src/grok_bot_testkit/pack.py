from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import yaml

from grok_bot_testkit.paths import pack_dir, testpacks_dir


REQUIRED_PACK_FILES = ("bot.yaml", "scenario.md", "rubric.yaml")


def load_yaml(path: Path) -> Any:
    with path.open(encoding="utf-8") as f:
        return yaml.safe_load(f)


def load_bot_yaml(bot_id: str, root: Path | None = None) -> dict[str, Any]:
    path = pack_dir(bot_id, root) / "bot.yaml"
    data = load_yaml(path)
    if not isinstance(data, dict):
        raise ValueError(f"{path}: bot.yaml must be a mapping")
    return data


def list_pack_ids(root: Path | None = None) -> list[str]:
    base = testpacks_dir(root)
    if not base.is_dir():
        return []
    return sorted(
        p.name for p in base.iterdir() if p.is_dir() and (p / "bot.yaml").is_file()
    )


def schema_path(name: str) -> Path:
    return Path(__file__).resolve().parent / "schema" / name


def load_json_schema(name: str) -> dict[str, Any]:
    with schema_path(name).open(encoding="utf-8") as f:
        return json.load(f)


def validate_bot_yaml_shape(data: dict[str, Any], path: Path) -> list[str]:
    """Lightweight required-field checks (full JSON Schema optional)."""
    errors: list[str] = []
    for key in ("id", "skills", "port", "evidence_root", "artifacts"):
        if key not in data:
            errors.append(f"{path}: missing required field '{key}'")
    if "id" in data and not isinstance(data["id"], str):
        errors.append(f"{path}: 'id' must be a string")
    if "skills" in data and not isinstance(data["skills"], list):
        errors.append(f"{path}: 'skills' must be a list")
    if "port" in data and not isinstance(data["port"], int):
        errors.append(f"{path}: 'port' must be an int")
    if "evidence_root" in data and not isinstance(data["evidence_root"], str):
        errors.append(f"{path}: 'evidence_root' must be a string")
    if "artifacts" in data and not isinstance(data["artifacts"], dict):
        errors.append(f"{path}: 'artifacts' must be a mapping of name -> relative path")
    if "routes" in data:
        if not isinstance(data["routes"], list):
            errors.append(f"{path}: 'routes' must be a list")
        else:
            for i, route in enumerate(data["routes"]):
                if not isinstance(route, dict):
                    errors.append(f"{path}: routes[{i}] must be a mapping")
                    continue
                if "path" not in route or "handler" not in route:
                    errors.append(f"{path}: routes[{i}] needs 'path' and 'handler'")
                handler = route.get("handler")
                if handler not in (
                    None,
                    "static",
                    "login_wall",
                    "log_post",
                    "health",
                    "evidence",
                    "reset",
                ):
                    errors.append(f"{path}: routes[{i}] unknown handler {handler!r}")
    return errors
