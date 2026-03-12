from __future__ import annotations

import mimetypes
import time
from collections import deque
from pathlib import Path
from urllib.parse import urlparse

import httpx

from .converters import MarkdownConverter
from .exporters import Exporter
from .extractor import PageExtractor
from .link_rewriter import LinkRewriter
from .models import CrawlConfig, PageRecord, State
from .storage import Storage
from .utils import normalize_url, sha256_bytes, url_to_local_relpath


class CrawlError(Exception):
    pass


class DocsCrawler:
    def __init__(self, config: CrawlConfig):
        self.config = config
        self.storage = Storage(config.output_dir)
        self.extractor = PageExtractor()
        self.converter = MarkdownConverter()
        self.exporter = Exporter(Path(config.output_dir))
        self.assetmap: dict[str, str] = self.storage.read_json("assetmap.json", {})
        self.linkmap: dict[str, str] = self.storage.read_json("linkmap.json", {})
        self.index: list[dict] = self.storage.read_json("index.json", [])
        existing_state = self.storage.read_json("state.json", {"queued": [], "visited": [], "failed": []})
        self.state = State(**existing_state)
        self.client = httpx.Client(
            headers={"User-Agent": "ERPDocsMirror/0.1"},
            timeout=config.timeout,
            follow_redirects=True,
        )

    def _is_allowed(self, url: str) -> bool:
        parsed = urlparse(url)
        if parsed.scheme not in {"http", "https"}:
            return False
        if self.config.allowed_hosts and parsed.netloc not in self.config.allowed_hosts:
            return False
        if self.config.allowed_prefixes:
            return any(parsed.path.startswith(prefix) for prefix in self.config.allowed_prefixes)
        return True

    def _queue_from_state(self) -> deque[str]:
        if self.config.resume and self.state.queued:
            return deque(self.state.queued)
        return deque([normalize_url(seed) for seed in self.config.seeds])

    def _save_state(self, queue: deque[str]) -> None:
        self.state.queued = list(queue)
        self.storage.write_json("state.json", self.state.to_dict())

    def _download_asset(self, url: str) -> str | None:
        normalized = normalize_url(url)
        if normalized in self.assetmap:
            return self.assetmap[normalized]
        response = self.client.get(normalized)
        response.raise_for_status()
        data = response.content
        digest = sha256_bytes(data)[:12]
        extension = Path(urlparse(normalized).path).suffix.lower()
        if not extension:
            extension = mimetypes.guess_extension(response.headers.get("content-type", "").split(";")[0] or "") or ".bin"
        filename = f"assets/{digest}{extension}"
        self.storage.write_bytes(filename, data)
        self.assetmap[normalized] = filename
        return filename

    def _build_record(self, url: str, page_data: dict, status_code: int, markdown_relpath: str, content_hash: str) -> PageRecord:
        return PageRecord(
            url=url,
            title=page_data["title"],
            local_path=markdown_relpath,
            status_code=status_code,
            content_hash=content_hash,
            discovered_links=page_data["links"],
            assets=[self.assetmap.get(normalize_url(u), "") for u in page_data["assets"] if normalize_url(u) in self.assetmap],
            anchors=page_data["anchors"],
        )

    def crawl(self) -> dict:
        queue = self._queue_from_state()
        visited = set(self.state.visited)
        failed = set(self.state.failed)
        records: list[PageRecord] = []

        while queue and len(visited) < self.config.max_pages:
            current = normalize_url(queue.popleft())
            self._save_state(queue)
            if current in visited:
                continue
            if not self._is_allowed(current):
                continue
            try:
                response = self.client.get(current)
                response.raise_for_status()
                page_data = self.extractor.parse(response.text, current)
                markdown = self.converter.convert(page_data["content_html"])
                local_relpath = url_to_local_relpath(current)
                self.linkmap[current] = local_relpath

                if self.config.download_assets:
                    for asset_url in page_data["assets"]:
                        try:
                            self._download_asset(asset_url)
                        except Exception:
                            pass

                rewriter = LinkRewriter(Path(self.config.output_dir), self.linkmap, self.assetmap)
                rewritten = rewriter.rewrite_markdown(local_relpath, markdown, current_url=current)
                content_hash = sha256_bytes(rewritten.encode("utf-8"))
                self.storage.write_text(local_relpath, f"# {page_data['title']}\n\n{rewritten}")

                record = self._build_record(current, page_data, response.status_code, local_relpath, content_hash)
                records.append(record)
                self.index.append(record.to_dict())
                visited.add(current)

                for link in page_data["links"]:
                    normalized = normalize_url(link)
                    if normalized not in visited and normalized not in queue and self._is_allowed(normalized):
                        queue.append(normalized)

                if self.config.delay:
                    time.sleep(self.config.delay)
            except Exception as exc:
                failed.add(current)
                self.state.failed = sorted(failed)
                self._save_state(queue)
                print(f"[WARN] {current}: {exc}")

        self.state.visited = sorted(visited)
        self.state.failed = sorted(failed)
        self.state.queued = list(queue)
        self.storage.write_json("state.json", self.state.to_dict())
        self.storage.write_json("index.json", self.index)
        self.storage.write_json("linkmap.json", self.linkmap)
        self.storage.write_json("assetmap.json", self.assetmap)

        unique_pages = {}
        for item in self.index:
            unique_pages[item["url"]] = item
        page_records = [PageRecord(**item) for item in unique_pages.values()]
        self.exporter.write_summary(page_records)
        self.exporter.write_mkdocs(page_records)

        return {
            "visited": len(visited),
            "failed": len(failed),
            "queued": len(queue),
            "output_dir": self.config.output_dir,
        }
