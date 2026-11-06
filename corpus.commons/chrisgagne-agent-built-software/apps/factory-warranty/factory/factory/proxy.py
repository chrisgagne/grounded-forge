"""A loopback HTTPS proxy that tunnels only to named hosts.

A process under `sandbox-exec` with the network off can still reach loopback.
Pointing its `HTTPS_PROXY` here gives it its provider and nothing else: the
proxy accepts only `CONNECT host:port` for an allowed host on the allowed
port, and refuses every other request. It sees host names, not traffic (TLS
runs end to end through the tunnel).

The proxy itself runs in the factory's process, outside the sandbox.
"""
from __future__ import annotations

import re
import select
import socket
import socketserver
import threading

HOST_RE = re.compile(r"[A-Za-z0-9.-]+")
IDLE_S = 600


class _Handler(socketserver.BaseRequestHandler):
    def handle(self):
        p: AllowlistProxy = self.server.owner  # type: ignore[attr-defined]
        c = self.request
        c.settimeout(30)
        buf = b""
        try:
            while b"\r\n\r\n" not in buf and len(buf) < 8192:
                d = c.recv(4096)
                if not d:
                    return
                buf += d
        except OSError:
            return
        parts = buf.split(b"\r\n", 1)[0].decode("latin-1").split()
        method, target = (parts + ["", ""])[:2]
        host, _, port = target.rpartition(":")
        ok = (method == "CONNECT" and HOST_RE.fullmatch(host or "") is not None and host.lower() in p.hosts
              and port == str(p.port))
        with p.lock:
            (p.allowed if ok else p.denied).add(target if method == "CONNECT" else f"{method} {target}")
        if not ok:
            c.sendall(b"HTTP/1.1 403 Forbidden\r\nContent-Length: 0\r\n\r\n")
            return
        try:
            up = socket.create_connection((host, int(port)), timeout=30)
        except OSError:
            c.sendall(b"HTTP/1.1 502 Bad Gateway\r\nContent-Length: 0\r\n\r\n")
            return
        c.sendall(b"HTTP/1.1 200 Connection established\r\n\r\n")
        c.settimeout(None)
        try:
            pair = (c, up)
            while True:
                ready, _, _ = select.select(pair, [], [], IDLE_S)
                if not ready:
                    return
                for s in ready:
                    data = s.recv(65536)
                    if not data:
                        return
                    (up if s is c else c).sendall(data)
        except OSError:
            return
        finally:
            up.close()


class _Server(socketserver.ThreadingTCPServer):
    daemon_threads = True
    allow_reuse_address = True


class AllowlistProxy:
    """Context manager: a proxy on 127.0.0.1 (an ephemeral port) for the duration of the block. `url` is what goes in
    HTTPS_PROXY; `allowed` and `denied` are the targets it saw, for the ledger."""

    def __init__(self, hosts, port: int = 443):
        self.hosts = {h.lower() for h in hosts}
        self.port = port
        self.allowed: set[str] = set()
        self.denied: set[str] = set()
        self.lock = threading.Lock()
        self.server: _Server | None = None
        self.url = ""

    def __enter__(self):
        self.server = _Server(("127.0.0.1", 0), _Handler)
        self.server.owner = self  # type: ignore[attr-defined]
        threading.Thread(target=self.server.serve_forever, daemon=True).start()
        self.url = f"http://127.0.0.1:{self.server.server_address[1]}"
        return self

    def __exit__(self, *exc):
        if self.server:
            self.server.shutdown()
            self.server.server_close()

    def env(self) -> dict:
        return {k: self.url for k in ("HTTPS_PROXY", "https_proxy", "HTTP_PROXY", "http_proxy", "ALL_PROXY",
                                      "all_proxy")}
