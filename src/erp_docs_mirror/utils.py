from __future__ import annotations

import hashlib
import json
import posixpath
import re
from pathlib import Path
from urllib.parse import urljoin, urlparse, urlunparse


INVALID_PATH_CHARS = re.compile(r"[^a-zA-Z0-9._/-]+")
MULTI_DASH = re.compile(r"-{2,}")
HEADING_STRIP = re.compile(r"[^a-z0-9\- ]+")


def load_json(path: Path, default: object) -> object:
    if not path.exists():
        return default
    return json.loads(path.read_text(encoding="utf-8"))



def dump_json(path: Path, payload: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")



def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()



def normalize_url(url: str, base: str | None = None) -> str:
    if base:
        url = urljoin(base, url)
    parsed = urlparse(url)
    normalized_path = posixpath.normpath(parsed.path or "/")
    if parsed.path.endswith("/") and not normalized_path.endswith("/"):
        normalized_path += "/"
    return urlunparse((parsed.scheme.lower(), parsed.netloc.lower(), normalized_path, "", parsed.query, ""))



def strip_fragment(url: str) -> tuple[str, str | None]:
    parsed = urlparse(url)
    base = urlunparse((parsed.scheme, parsed.netloc, parsed.path, parsed.params, parsed.query, ""))
    return base, parsed.fragment or None



def safe_slug(text: str) -> str:
    text = text.strip().lower().replace("_", "-").replace(" ", "-")
    text = HEADING_STRIP.sub("", text)
    text = MULTI_DASH.sub("-", text).strip("-")
    return text or "section"



def url_to_local_relpath(url: str) -> str:
    parsed = urlparse(url)
    path = parsed.path.strip("/")
    if not path:
        path = "index"
    if path.endswith("/"):
        path += "index"
    if path.endswith(".html"):
        path = path[:-5]
    clean = INVALID_PATH_CHARS.sub("-", path)
    clean = MULTI_DASH.sub("-", clean)
    return f"pages/{clean}.md"



def ensure_parent(path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)



def relativize_path(from_path: Path, to_path: Path) -> str:
    return posixpath.relpath(to_path.as_posix(), start=from_path.parent.as_posix())
