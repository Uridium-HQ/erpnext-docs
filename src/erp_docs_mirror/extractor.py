from __future__ import annotations

import json
from pathlib import Path
from typing import Any
from urllib.parse import urljoin

from bs4 import BeautifulSoup

from .utils import safe_slug


class PageExtractor:
    def __init__(self, config_path: Path | None = None):
        if config_path is None:
            config_path = Path(__file__).with_name("default_config.json")
        self.config: dict[str, Any] = json.loads(config_path.read_text(encoding="utf-8"))

    def _first(self, soup: BeautifulSoup, selectors: list[str]):
        for selector in selectors:
            node = soup.select_one(selector)
            if node is not None:
                return node
        return None

    def parse(self, html: str, base_url: str) -> dict[str, Any]:
        soup = BeautifulSoup(html, "html.parser")

        nav_root = self._first(soup, self.config.get("nav_selectors", []))
        nav_items = []
        if nav_root is not None:
            for a in nav_root.select("a[href]"):
                href = a.get("href", "").strip()
                text = a.get_text(" ", strip=True)
                if href and text:
                    nav_items.append({"title": text, "url": urljoin(base_url, href)})

        for selector in self.config.get("remove_selectors", []):
            for node in soup.select(selector):
                node.decompose()

        title_node = self._first(soup, self.config.get("title_selectors", []))
        title = title_node.get_text(" ", strip=True) if title_node else base_url

        content_node = self._first(soup, self.config.get("content_selectors", [])) or soup.body or soup

        links: list[str] = []
        assets: list[str] = []
        anchors: list[str] = []

        for heading in content_node.select("h1, h2, h3, h4, h5, h6"):
            hid = heading.get("id") or safe_slug(heading.get_text(" ", strip=True))
            heading["id"] = hid
            anchors.append(hid)

        for a in content_node.select("a[href]"):
            href = a.get("href", "").strip()
            if href:
                links.append(urljoin(base_url, href))

        for img in content_node.select("img[src]"):
            src = img.get("src", "").strip()
            if src:
                assets.append(urljoin(base_url, src))

        return {
            "title": title,
            "content_html": str(content_node),
            "links": list(dict.fromkeys(links)),
            "assets": list(dict.fromkeys(assets)),
            "anchors": list(dict.fromkeys(anchors)),
            "nav_items": nav_items,
        }
