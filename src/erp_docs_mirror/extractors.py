from __future__ import annotations

from bs4 import BeautifulSoup, Tag


MAIN_SELECTORS = [
    "main",
    "article",
    "div.prose",
    "div.markdown-body",
    "div.docs-content",
    "section.content",
]

NAV_SELECTORS = [
    "nav",
    "aside nav",
    "aside",
    "div.sidebar",
]


class ExtractedPage:
    def __init__(self, title: str, content_html: str, nav_links: list[tuple[str, str]]):
        self.title = title
        self.content_html = content_html
        self.nav_links = nav_links



def _first_matching_element(soup: BeautifulSoup, selectors: list[str]) -> Tag | None:
    for selector in selectors:
        node = soup.select_one(selector)
        if node:
            return node
    return None



def extract_page(html: str) -> ExtractedPage:
    soup = BeautifulSoup(html, "html.parser")

    title = "Untitled"
    h1 = soup.find("h1")
    if h1 and h1.get_text(strip=True):
        title = h1.get_text(" ", strip=True)
    elif soup.title and soup.title.get_text(strip=True):
        title = soup.title.get_text(" ", strip=True)

    main_node = _first_matching_element(soup, MAIN_SELECTORS)
    if main_node is None:
        body = soup.body or soup
        main_node = body

    nav_links: list[tuple[str, str]] = []
    nav_node = _first_matching_element(soup, NAV_SELECTORS)
    if nav_node is not None:
        seen: set[tuple[str, str]] = set()
        for a in nav_node.select("a[href]"):
            href = a.get("href", "").strip()
            text = a.get_text(" ", strip=True)
            pair = (text, href)
            if href and text and pair not in seen:
                seen.add(pair)
                nav_links.append(pair)

    return ExtractedPage(title=title, content_html=str(main_node), nav_links=nav_links)
