from __future__ import annotations

import html2text


class MarkdownConverter:
    def __init__(self) -> None:
        self.converter = html2text.HTML2Text()
        self.converter.ignore_images = False
        self.converter.ignore_tables = False
        self.converter.body_width = 0
        self.converter.protect_links = True
        self.converter.mark_code = True
        self.converter.single_line_break = False

    def convert(self, html: str) -> str:
        markdown = self.converter.handle(html)
        return markdown.strip() + "\n"
