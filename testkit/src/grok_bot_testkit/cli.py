from __future__ import annotations

import argparse
import sys
from pathlib import Path

from grok_bot_testkit import __version__
from grok_bot_testkit.paths import repo_root
from grok_bot_testkit.rubric import print_report, score_run
from grok_bot_testkit.server import serve_pack
from grok_bot_testkit.validate import print_validation, validate_all


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="grok-bot-testkit",
        description="Validate skills/testpacks, serve mock sites, score evidence packs",
    )
    parser.add_argument("--version", action="version", version=__version__)
    parser.add_argument(
        "--root",
        type=Path,
        default=None,
        help="Repo root (default: auto-detect from cwd / package location)",
    )

    sub = parser.add_subparsers(dest="command", required=True)

    sub.add_parser("validate", help="Validate skills/ and testpacks/")

    serve_p = sub.add_parser("serve", help="Serve a testpack mock HTTP server")
    serve_p.add_argument("--pack", required=True, help="Testpack id (directory name)")
    serve_p.add_argument("--host", default="127.0.0.1")

    score_p = sub.add_parser("score", help="Score an evidence run directory")
    score_p.add_argument("--pack", required=True, help="Testpack id")
    score_p.add_argument("run_dir", type=Path, help="Path to evidence run directory")

    list_p = sub.add_parser("list-packs", help="List testpack ids")
    list_p.add_argument("--quiet", action="store_true")

    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    root = args.root.resolve() if args.root else None
    # Prefer cwd if it looks like the plugin repo
    if root is None:
        cwd = Path.cwd()
        if (cwd / "testpacks").is_dir() or (cwd / "plugin.json").is_file():
            root = cwd
        else:
            root = repo_root()

    if args.command == "validate":
        report = validate_all(root)
        print_validation(report)
        return 0 if report.ok else 1

    if args.command == "serve":
        serve_pack(args.pack, root=root, host=args.host)
        return 0

    if args.command == "score":
        report = score_run(args.pack, args.run_dir, root=root)
        print_report(report)
        return 0 if report.ok else 1

    if args.command == "list-packs":
        from grok_bot_testkit.pack import list_pack_ids

        ids = list_pack_ids(root)
        for bot_id in ids:
            print(bot_id)
        return 0

    parser.error(f"unknown command {args.command}")
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
