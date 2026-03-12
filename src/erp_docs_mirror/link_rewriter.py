from __future__ import annotations

import re
from pathlib import Path
from urllib.parse import urlparse

from .utils import normalize_url, relativize_path, strip_fragment


MARKDOWN_LINK_RE = re.compile(r"\[([^\]]+)\]\(([^)]+)\)")
IMAGE_LINK_RE = re.compile(r"!\[([^\]]*)\]\(([^)]+)\)")


class LinkRewriter:
    def __init__(self, root: Path, linkmap: dict[str, str], assetmap: dict[str, str]):
        self.root = root
        self.linkmap = {normalize_url(k): v for k, v in linkmap.items()}
        self.assetmap = {normalize_url(k): v for k, v in assetmap.items()}
        self.reverse_linkmap = {v: k for k, v in self.linkmap.items()}

    @staticmethod
    def _unwrap_target(target: str) -> str:
        target = target.strip()
        if len(target) >= 2 and target.startswith("<") and target.endswith(">"):
            return target[1:-1].strip()
        return target

    def _normalize_target(self, target: str, current_url: str | None) -> str:
        target = self._unwrap_target(target)
        return normalize_url(target, base=current_url) if current_url else normalize_url(target)

    def _rewrite_target(self, current_relpath: str, target: str, current_url: str | None = None) -> str:
        target = self._unwrap_target(target)
        if target.startswith("mailto:") or target.startswith("tel:"):
            return target
        if target.startswith("#"):
            return target
        normalized_target = self._normalize_target(target, current_url)
        base_target, fragment = strip_fragment(normalized_target)
        current_abs = self.root / current_relpath

        if base_target in self.linkmap:
            local_abs = self.root / self.linkmap[base_target]
            rel = relativize_path(current_abs, local_abs)
            return f"{rel}#{fragment}" if fragment else rel

        if base_target in self.assetmap:
            local_abs = self.root / self.assetmap[base_target]
            rel = relativize_path(current_abs, local_abs)
            return rel
        parsed = urlparse(base_target)
        if parsed.scheme in {"http", "https"}:
            return f"{base_target}#{fragment}" if fragment else base_target
        return target

    def rewrite_markdown(self, current_relpath: str, markdown: str, current_url: str | None = None) -> str:
        current_url = current_url or self.reverse_linkmap.get(current_relpath)
        def image_repl(match: re.Match[str]) -> str:
            alt, target = match.group(1), match.group(2)
            return f"![{alt}]({self._rewrite_target(current_relpath, target, current_url=current_url)})"

        markdown = IMAGE_LINK_RE.sub(image_repl, markdown)

        def link_repl(match: re.Match[str]) -> str:
            text, target = match.group(1), match.group(2)
            return f"[{text}]({self._rewrite_target(current_relpath, target, current_url=current_url)})"

        return MARKDOWN_LINK_RE.sub(link_repl, markdown)
