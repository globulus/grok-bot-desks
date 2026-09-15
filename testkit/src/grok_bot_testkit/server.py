from __future__ import annotations

import json
import mimetypes
from datetime import datetime, timezone
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from typing import Any
from urllib.parse import urlparse

from grok_bot_testkit.pack import load_bot_yaml
from grok_bot_testkit.paths import pack_dir


def _utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


class HarnessState:
    def __init__(self, pack_path: Path, bot: dict[str, Any]):
        self.pack_path = pack_path
        self.bot = bot
        self.sites = pack_path / "sites"
        self.log_dir = pack_path / ".harness-logs"
        self.log_dir.mkdir(parents=True, exist_ok=True)
        self.requests: list[dict[str, Any]] = []

    def log_file(self, name: str) -> Path:
        return self.log_dir / name

    def reset(self) -> None:
        self.requests.clear()
        for path in self.log_dir.glob("*.log"):
            path.write_text("", encoding="utf-8")

    def append_log(self, name: str, line: str) -> None:
        path = self.log_file(name)
        with path.open("a", encoding="utf-8") as f:
            f.write(line.rstrip() + "\n")

    def evidence_snapshot(self) -> dict[str, Any]:
        logs = {}
        for path in sorted(self.log_dir.glob("*.log")):
            logs[path.name] = path.read_text(encoding="utf-8")
        return {
            "bot_id": self.bot.get("id"),
            "requests": list(self.requests),
            "logs": logs,
        }


def _match_route(routes: list[dict[str, Any]], path: str) -> dict[str, Any] | None:
    for route in routes:
        if route.get("path") == path:
            return route
    return None


def make_handler(state: HarnessState) -> type[BaseHTTPRequestHandler]:
    routes: list[dict[str, Any]] = list(state.bot.get("routes") or [])

    # Built-in harness routes always available
    builtin = [
        {"path": "/_harness/health", "handler": "health"},
        {"path": "/_harness/evidence", "handler": "evidence"},
        {"path": "/_harness/reset", "handler": "reset"},
    ]
    known_paths = {r["path"] for r in routes}
    for b in builtin:
        if b["path"] not in known_paths:
            routes.append(b)

    class Handler(BaseHTTPRequestHandler):
        def log_message(self, fmt: str, *args: Any) -> None:  # noqa: A003
            # quieter default; still record
            pass

        def _record(self, method: str) -> None:
            state.requests.append(
                {
                    "ts": _utc_now(),
                    "method": method,
                    "path": self.path,
                    "client": self.client_address[0],
                }
            )

        def _send(self, code: int, body: bytes, content_type: str) -> None:
            self.send_response(code)
            self.send_header("Content-Type", content_type)
            self.send_header("Content-Length", str(len(body)))
            self.send_header("Cache-Control", "no-store")
            self.end_headers()
            self.wfile.write(body)

        def _send_json(self, code: int, payload: Any) -> None:
            raw = json.dumps(payload, indent=2).encode("utf-8")
            self._send(code, raw, "application/json; charset=utf-8")

        def _read_body(self) -> bytes:
            length = int(self.headers.get("Content-Length", "0") or "0")
            if length <= 0:
                return b""
            return self.rfile.read(length)

        def _serve_static_file(self, rel: str) -> None:
            target = (state.sites / rel).resolve()
            if not str(target).startswith(str(state.sites.resolve())):
                self._send_json(403, {"error": "forbidden"})
                return
            if not target.is_file():
                self._send_json(404, {"error": "not found", "path": rel})
                return
            ctype = mimetypes.guess_type(str(target))[0] or "application/octet-stream"
            self._send(200, target.read_bytes(), ctype)

        def _dispatch(self, method: str) -> None:
            self._record(method)
            parsed = urlparse(self.path)
            path = parsed.path
            route = _match_route(routes, path)

            # Fallback: /sites/<file> or /<file> under sites/
            if route is None:
                if path.startswith("/sites/"):
                    self._serve_static_file(path[len("/sites/") :])
                    return
                if method == "GET" and (state.sites / path.lstrip("/")).is_file():
                    self._serve_static_file(path.lstrip("/"))
                    return
                self._send_json(404, {"error": "no route", "path": path})
                return

            handler = route["handler"]

            if handler == "health":
                self._send_json(
                    200,
                    {
                        "ok": True,
                        "bot_id": state.bot.get("id"),
                        "port": state.bot.get("port"),
                    },
                )
                return

            if handler == "evidence":
                self._send_json(200, state.evidence_snapshot())
                return

            if handler == "reset":
                if method not in ("POST", "GET"):
                    self._send_json(405, {"error": "use POST"})
                    return
                state.reset()
                self._send_json(200, {"ok": True, "reset": True})
                return

            if handler == "login_wall":
                html = (
                    "<!doctype html><html><head><title>Login required</title></head>"
                    "<body><h1>Sign in to view this posting</h1>"
                    "<p>Fixture login wall — no job content here.</p>"
                    "<form><input name='email' placeholder='email'/>"
                    "<input name='password' type='password'/>"
                    "<button type='submit'>Log in</button></form></body></html>"
                )
                file_override = route.get("file")
                if file_override:
                    target = state.sites / file_override
                    if target.is_file():
                        html = target.read_text(encoding="utf-8")
                self._send(401, html.encode("utf-8"), "text/html; charset=utf-8")
                return

            if handler == "static":
                rel = route.get("file") or path.lstrip("/")
                self._serve_static_file(rel)
                return

            if handler == "log_post":
                if method != "POST":
                    self._send_json(405, {"error": "POST required"})
                    return
                body = self._read_body()
                log_name = route.get("log") or "posts.log"
                state.append_log(
                    log_name,
                    json.dumps(
                        {
                            "ts": _utc_now(),
                            "path": path,
                            "body": body.decode("utf-8", errors="replace"),
                        }
                    ),
                )
                self._send_json(200, {"ok": True, "recorded": True})
                return

            self._send_json(500, {"error": f"unhandled handler {handler}"})

        def do_GET(self) -> None:  # noqa: N802
            self._dispatch("GET")

        def do_POST(self) -> None:  # noqa: N802
            self._dispatch("POST")

        def do_PUT(self) -> None:  # noqa: N802
            self._dispatch("PUT")

    return Handler


def serve_pack(bot_id: str, root: Path | None = None, host: str = "127.0.0.1") -> None:
    bot = load_bot_yaml(bot_id, root)
    path = pack_dir(bot_id, root)
    port = int(bot["port"])
    state = HarnessState(path, bot)
    state.reset()
    handler = make_handler(state)
    server = ThreadingHTTPServer((host, port), handler)
    print(f"Serving testpack '{bot_id}' on http://{host}:{port}")
    print(f"  health:   http://{host}:{port}/_harness/health")
    print(f"  evidence: http://{host}:{port}/_harness/evidence")
    print(f"  reset:    http://{host}:{port}/_harness/reset")
    print("Ctrl+C to stop")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nStopped")
    finally:
        server.server_close()
