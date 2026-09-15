from __future__ import annotations

from pathlib import Path


def repo_root(start: Path | None = None) -> Path:
    """Walk up from start (or this file) until plugin.json or testpacks/ is found."""
    cur = (start or Path(__file__)).resolve()
    if cur.is_file():
        cur = cur.parent
    for candidate in [cur, *cur.parents]:
        if (candidate / "plugin.json").is_file() or (candidate / "testpacks").is_dir():
            return candidate
    raise FileNotFoundError("Could not locate repo root (plugin.json or testpacks/)")


def testpacks_dir(root: Path | None = None) -> Path:
    return (root or repo_root()) / "testpacks"


def skills_dir(root: Path | None = None) -> Path:
    return (root or repo_root()) / "skills"


def pack_dir(bot_id: str, root: Path | None = None) -> Path:
    path = testpacks_dir(root) / bot_id
    if not path.is_dir():
        raise FileNotFoundError(f"Unknown testpack: {bot_id} ({path})")
    return path
