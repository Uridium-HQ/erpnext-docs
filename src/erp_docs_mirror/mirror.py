from __future__ import annotations

import json
import mimetypes
import time
from collections import deque
from pathlib import Path
from urllib.parse import urlparse

import requests
from bs4 import BeautifulSoup

from .config import MirrorConfig
from .extractors import extract_page
from .markdown_tools import html_to_markdown
from .utils import (
    is_http_url,
    make_relative_link,
    normalize_url,
    safe_asset_filename,
    url_to_markdown_relpath,
)


class DocsMirror:
    def __init__(self, config: MirrorConfig, seed_urls: list[str]):
        self.config = config
        self.seed_urls = [normalize_url(url) for url in seed_urls]
        self.session = requests.Session()
        self.session.headers.update({"User-Agent": config.user_agent})
        self.config.allowed_domains = {urlparse(url).netloc for url in self.seed_urls}
        self.config.seed_prefixes = [urlparse(url).path.rstrip("/") or "/" for url in self.seed_urls]

        self.visited: set[str] = set()
        self.discovered: deque[str] = deque(self.seed_urls)
        self.linkmap: dict[str, str] = {}
        self.index: list[dict] = []
        self.nav: dict[str, list[dict[str, str]]] = {}

        self.config.output_dir.mkdir(parents=True, exist_ok=True)
        (self.config.output_dir / "assets").mkdir(parents=True, exist_ok=True)

    def run(self) -> None:
        pages_processed = 0
        while self.discovered and pages_processed < self.config.max_pages:
            url = self.discovered.popleft()
            if url in self.visited:
                continue
            self.visited.add(url)
            try:
                self._process_page(url)
                pages_processed += 1
                time.sleep(self.config.delay_seconds)
            except Exception as exc:  # noqa: BLE001
                print(f"[WARN] failed: {url} -> {exc}")

        self._write_metadata_files()

    def _is_allowed_url(self, url: str) -> bool:
        if not is_http_url(url):
            return False
        parsed = urlparse(url)
        if parsed.netloc not in self.config.allowed_domains:
            return False
        if self.config.same_path_prefix_only:
            path = parsed.path.rstrip("/") or "/"
            return any(path.startswith(prefix) for prefix in self.config.seed_prefixes)
        return True

    def _fetch(self, url: str) -> requests.Response:
        resp = self.session.get(url, timeout=self.config.timeout_seconds)
        resp.raise_for_status()
        return resp

    def _process_page(self, url: str) -> None:
        resp = self._fetch(url)
        content_type = resp.headers.get("Content-Type", "")
        if "text/html" not in content_type:
            return

        extracted = extract_page(resp.text)
        markdown_path = self.config.output_dir / url_to_markdown_relpath(url)
        markdown_path.parent.mkdir(parents=True, exist_ok=True)
        self.linkmap[url] = str(markdown_path.relative_to(self.config.output_dir).as_posix())

        soup = BeautifulSoup(extracted.content_html, "html.parser")

        for asset_tag in soup.select("img[src], source[src], source[srcset]"):
            attr = "srcset" if asset_tag.has_attr("srcset") else "src"
            asset_url = asset_tag.get(attr, "").strip()
            if not asset_url:
                continue
            if attr == "srcset":
                asset_url = asset_url.split(",", 1)[0].strip().split(" ", 1)[0]
            asset_url = normalize_url(asset_url, base_url=url)
            if not self._is_allowed_asset(asset_url):
                continue
            local_asset = self._download_asset(asset_url, page_url=url)
            if local_asset:
                rel = make_relative_link(markdown_path, local_asset)
                asset_tag[attr] = rel

        all_links: set[str] = set()
        for a in soup.select("a[href]"):
            href = a.get("href", "").strip()
            if not href:
                continue
            abs_url = normalize_url(href, base_url=url)
            parsed_original = urlparse(href)
            fragment = parsed_original.fragment
            if self._is_allowed_url(abs_url):
                all_links.add(abs_url)
                target_relpath = self.config.output_dir / url_to_markdown_relpath(abs_url)
                new_href = make_relative_link(markdown_path, target_relpath)
                if fragment:
                    new_href = f"{new_href}#{fragment}"
                a["href"] = new_href
            elif href.startswith("#"):
                a["href"] = href

        for text, href in extracted.nav_links:
            abs_url = normalize_url(href, base_url=url)
            if self._is_allowed_url(abs_url):
                self.nav.setdefault(url, []).append({"text": text, "url": abs_url})
                all_links.add(abs_url)

        for next_url in sorted(all_links):
            if next_url not in self.visited:
                self.discovered.append(next_url)

        markdown = html_to_markdown(str(soup))
        final_text = f"# {extracted.title}\n\n{markdown}"
        markdown_path.write_text(final_text, encoding="utf-8")

        self.index.append(
            {
                "url": url,
                "title": extracted.title,
                "path": str(markdown_path.relative_to(self.config.output_dir).as_posix()),
            }
        )
        print(f"[OK] {url} -> {markdown_path}")

    def _is_allowed_asset(self, url: str) -> bool:
        if not is_http_url(url):
            return False
        parsed = urlparse(url)
        return parsed.netloc in self.config.allowed_domains

    def _download_asset(self, asset_url: str, page_url: str) -> Path | None:
        try:
            resp = self._fetch(asset_url)
        except Exception as exc:  # noqa: BLE001
            print(f"[WARN] asset failed: {asset_url} -> {exc}")
            return None

        page_rel = url_to_markdown_relpath(page_url).with_suffix("")
        asset_dir = self.config.output_dir / "assets" / page_rel
        asset_dir.mkdir(parents=True, exist_ok=True)

        filename = safe_asset_filename(asset_url)
        ext = Path(filename).suffix
        if not ext:
            guessed = mimetypes.guess_extension(resp.headers.get("Content-Type", "").split(";")[0].strip())
            if guessed:
                filename += guessed

        asset_path = asset_dir / filename
        asset_path.write_bytes(resp.content)
        return asset_path

    def _write_metadata_files(self) -> None:
        index_path = self.config.output_dir / "index.json"
        linkmap_path = self.config.output_dir / "linkmap.json"
        nav_path = self.config.output_dir / "nav.json"
        summary_path = self.config.output_dir / "SUMMARY.md"

        index_path.write_text(json.dumps(self.index, ensure_ascii=False, indent=2), encoding="utf-8")
        linkmap_path.write_text(json.dumps(self.linkmap, ensure_ascii=False, indent=2), encoding="utf-8")
        nav_path.write_text(json.dumps(self.nav, ensure_ascii=False, indent=2), encoding="utf-8")
        summary_path.write_text(self._build_summary(), encoding="utf-8")

    def _build_summary(self) -> str:
        lines = ["# Summary", ""]
        for item in sorted(self.index, key=lambda x: x["path"]):
            lines.append(f"- [{item['title']}]({item['path']})")
        lines.append("")
        return "\n".join(lines)
