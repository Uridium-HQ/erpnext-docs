from __future__ import annotations

from dataclasses import dataclass, field, asdict
from typing import Any


@dataclass
class CrawlConfig:
    seeds: list[str]
    output_dir: str
    allowed_hosts: list[str]
    allowed_prefixes: list[str] = field(default_factory=list)
    max_pages: int = 200
    timeout: float = 20.0
    delay: float = 0.0
    download_assets: bool = True
    resume: bool = True


@dataclass
class PageRecord:
    url: str
    title: str
    local_path: str
    status_code: int | None = None
    content_hash: str | None = None
    discovered_links: list[str] = field(default_factory=list)
    assets: list[str] = field(default_factory=list)
    anchors: list[str] = field(default_factory=list)

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


@dataclass
class NavNode:
    title: str
    url: str | None = None
    local_path: str | None = None
    children: list["NavNode"] = field(default_factory=list)

    def to_dict(self) -> dict[str, Any]:
        return {
            "title": self.title,
            "url": self.url,
            "local_path": self.local_path,
            "children": [child.to_dict() for child in self.children],
        }


@dataclass
class State:
    queued: list[str] = field(default_factory=list)
    visited: list[str] = field(default_factory=list)
    failed: list[str] = field(default_factory=list)

    def to_dict(self) -> dict[str, Any]:
        return {"queued": self.queued, "visited": self.visited, "failed": self.failed}
