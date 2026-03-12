from __future__ import annotations

from pathlib import Path

import yaml

from .models import PageRecord


class Exporter:
    def __init__(self, output_root: Path):
        self.output_root = output_root

    def write_summary(self, pages: list[PageRecord]) -> None:
        lines = ["# Summary", ""]
        for page in sorted(pages, key=lambda p: p.local_path):
            title = page.title.replace("[", "\\[").replace("]", "\\]")
            lines.append(f"- [{title}]({page.local_path})")
        (self.output_root / "SUMMARY.md").write_text("\n".join(lines) + "\n", encoding="utf-8")

    def write_mkdocs(self, pages: list[PageRecord]) -> None:
        nav = [{page.title: page.local_path} for page in sorted(pages, key=lambda p: p.local_path)]
        payload = {
            "site_name": "ERP Docs Mirror",
            "docs_dir": ".",
            "nav": nav,
        }
        (self.output_root / "mkdocs.yml").write_text(yaml.safe_dump(payload, sort_keys=False, allow_unicode=True), encoding="utf-8")
