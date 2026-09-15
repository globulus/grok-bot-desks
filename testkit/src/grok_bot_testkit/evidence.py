from __future__ import annotations

import json
import re
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


MANIFEST_NAME = "manifest.json"


def utc_now_iso() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def new_manifest(
    *,
    bot_id: str,
    skills_run: list[str] | None = None,
    urls_hit: list[str] | None = None,
    pack_version: str = "1",
    extra: dict[str, Any] | None = None,
) -> dict[str, Any]:
    manifest: dict[str, Any] = {
        "bot_id": bot_id,
        "pack_version": pack_version,
        "skills_run": skills_run or [],
        "urls_hit": urls_hit or [],
        "started_at": utc_now_iso(),
        "finished_at": None,
    }
    if extra:
        manifest.update(extra)
    return manifest


def write_manifest(run_dir: Path, manifest: dict[str, Any]) -> Path:
    run_dir.mkdir(parents=True, exist_ok=True)
    path = run_dir / MANIFEST_NAME
    path.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    return path


def read_manifest(run_dir: Path) -> dict[str, Any]:
    path = run_dir / MANIFEST_NAME
    with path.open(encoding="utf-8") as f:
        data = json.load(f)
    if not isinstance(data, dict):
        raise ValueError(f"{path}: manifest must be a JSON object")
    return data


def validate_manifest_shape(manifest: dict[str, Any], path: Path | str = "manifest") -> list[str]:
    errors: list[str] = []
    for key in ("bot_id", "skills_run", "urls_hit", "started_at", "pack_version"):
        if key not in manifest:
            errors.append(f"{path}: missing '{key}'")
    if "bot_id" in manifest and not isinstance(manifest["bot_id"], str):
        errors.append(f"{path}: bot_id must be a string")
    if "skills_run" in manifest and not isinstance(manifest["skills_run"], list):
        errors.append(f"{path}: skills_run must be a list")
    if "urls_hit" in manifest and not isinstance(manifest["urls_hit"], list):
        errors.append(f"{path}: urls_hit must be a list")
    return errors


def ensure_run_layout(run_dir: Path) -> None:
    (run_dir / "artifacts").mkdir(parents=True, exist_ok=True)
    (run_dir / "logs").mkdir(parents=True, exist_ok=True)


PHONE_RE = re.compile(
    r"(?<!\d)(?:\+?\d{1,3}[-.\s]?)?(?:\(?\d{3}\)?[-.\s]?)\d{3}[-.\s]?\d{4}(?!\d)"
)


def find_phone_like(text: str) -> list[str]:
    return PHONE_RE.findall(text)
