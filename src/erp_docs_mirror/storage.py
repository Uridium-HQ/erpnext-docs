from __future__ import annotations

from pathlib import Path
from typing import Any

from .utils import dump_json, ensure_parent, load_json


class Storage:
    def __init__(self, root: str | Path):
        self.root = Path(root)
        self.pages_dir = self.root / "pages"
        self.assets_dir = self.root / "assets"
        self.meta_dir = self.root / "meta"
        self.pages_dir.mkdir(parents=True, exist_ok=True)
        self.assets_dir.mkdir(parents=True, exist_ok=True)
        self.meta_dir.mkdir(parents=True, exist_ok=True)

    def write_text(self, relpath: str, content: str) -> Path:
        path = self.root / relpath
        ensure_parent(path)
        path.write_text(content, encoding="utf-8")
        return path

    def write_bytes(self, relpath: str, content: bytes) -> Path:
        path = self.root / relpath
        ensure_parent(path)
        path.write_bytes(content)
        return path

    def read_json(self, name: str, default: Any) -> Any:
        return load_json(self.meta_dir / name, default)

    def write_json(self, name: str, payload: Any) -> None:
        dump_json(self.meta_dir / name, payload)
