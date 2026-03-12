from __future__ import annotations

from markdownify import markdownify as md



def html_to_markdown(html: str) -> str:
    text = md(
        html,
        heading_style="ATX",
        bullets="-",
        strip=["script", "style"],
    )
    text = text.replace("\r\n", "\n").replace("\r", "\n")
    while "\n\n\n" in text:
        text = text.replace("\n\n\n", "\n\n")
    return text.strip() + "\n"
