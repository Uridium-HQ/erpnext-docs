from __future__ import annotations

import os
import re
import shutil
from dataclasses import dataclass
from pathlib import Path
import httpx


FENCED_BLOCK_RE = re.compile(r"```[\s\S]*?```", re.MULTILINE)
INLINE_CODE_RE = re.compile(r"`[^`\n]+`")
HTML_COMMENT_RE = re.compile(r"<!--.*?-->", re.DOTALL)
LINK_TARGET_RE = re.compile(r"(\!?)\[([^\]]*)\]\(([^)]+)\)")
AUTOLINK_RE = re.compile(r"<(https?://[^>]+)>")


@dataclass
class TranslationConfig:
    language: str = "sr-Latn"
    provider: str = "openai"
    model: str = "gpt-4o-mini"
    api_base: str = "https://api.openai.com/v1"
    api_key: str | None = None
    max_chars_per_chunk: int = 6000
    overwrite: bool = False


class TranslationError(Exception):
    pass


class OpenAICompatibleTranslator:
    def __init__(self, config: TranslationConfig):
        self.config = config
        self.api_key = config.api_key or os.getenv("OPENAI_API_KEY")
        self.api_base = (os.getenv("OPENAI_API_BASE") or config.api_base).rstrip("/")
        self.model = os.getenv("OPENAI_MODEL") or config.model
        if not self.api_key:
            raise TranslationError("Nedostaje API ključ. Postavi OPENAI_API_KEY ili prosledi api_key.")
        self.client = httpx.Client(
            headers={
                "Authorization": f"Bearer {self.api_key}",
                "Content-Type": "application/json",
            },
            timeout=90.0,
        )

    def translate_text(self, text: str, language: str) -> str:
        if not text.strip():
            return text
        payload = {
            "model": self.model,
            "messages": [
                {
                    "role": "system",
                    "content": (
                        "You are a precise technical documentation translator. "
                        "Translate the user's text into the requested target language. "
                        "Preserve Markdown structure, headings, list markers, placeholders like @@TOKEN_1@@, "
                        "URLs, file paths, anchor fragments, HTML comments, and code-like syntax exactly. "
                        "Do not add commentary. Return only the translated text."
                    ),
                },
                {
                    "role": "user",
                    "content": f"Target language: {language}\n\n{text}",
                },
            ],
            "temperature": 0.1,
        }
        response = self.client.post(f"{self.api_base}/chat/completions", json=payload)
        response.raise_for_status()
        data = response.json()
        try:
            return data["choices"][0]["message"]["content"]
        except Exception as exc:
            raise TranslationError(f"Neočekivan odgovor translation API-ja: {data}") from exc


class MarkdownTranslator:
    def __init__(self, translator: OpenAICompatibleTranslator, config: TranslationConfig):
        self.translator = translator
        self.config = config

    def _mask(self, text: str) -> tuple[str, dict[str, str]]:
        tokens: dict[str, str] = {}
        counter = 0

        def put(match: re.Match[str]) -> str:
            nonlocal counter
            key = f"@@TOKEN_{counter}@@"
            counter += 1
            tokens[key] = match.group(0)
            return key

        text = FENCED_BLOCK_RE.sub(put, text)
        text = HTML_COMMENT_RE.sub(put, text)
        text = INLINE_CODE_RE.sub(put, text)

        def mask_link(match: re.Match[str]) -> str:
            nonlocal counter
            bang, label, target = match.groups()
            key = f"@@TOKEN_{counter}@@"
            counter += 1
            tokens[key] = target
            return f"{bang}[{label}]({key})"

        text = LINK_TARGET_RE.sub(mask_link, text)
        text = AUTOLINK_RE.sub(put, text)
        return text, tokens

    def _unmask(self, text: str, tokens: dict[str, str]) -> str:
        for key, value in sorted(tokens.items(), key=lambda item: -len(item[0])):
            text = text.replace(key, value)
        return text

    def _split_chunks(self, text: str) -> list[str]:
        limit = max(1000, self.config.max_chars_per_chunk)
        if len(text) <= limit:
            return [text]
        parts: list[str] = []
        current: list[str] = []
        current_len = 0
        for block in re.split(r"(\n\s*\n)", text):
            if current_len + len(block) > limit and current:
                parts.append("".join(current))
                current = [block]
                current_len = len(block)
            else:
                current.append(block)
                current_len += len(block)
        if current:
            parts.append("".join(current))
        return parts

    def translate_markdown(self, markdown: str) -> str:
        masked, tokens = self._mask(markdown)
        translated_parts: list[str] = []
        for chunk in self._split_chunks(masked):
            translated_parts.append(self.translator.translate_text(chunk, self.config.language))
        translated = "".join(translated_parts)
        translated = self._unmask(translated, tokens)
        return translated

    def translate_tree(self, input_root: Path, output_root: Path) -> dict[str, int]:
        pages_dir = input_root / "pages"
        target_pages = output_root / "pages"
        target_pages.mkdir(parents=True, exist_ok=True)
        translated = 0
        skipped = 0

        for src in sorted(pages_dir.rglob("*.md")):
            rel = src.relative_to(input_root)
            dst = output_root / rel
            dst.parent.mkdir(parents=True, exist_ok=True)
            if dst.exists() and not self.config.overwrite:
                skipped += 1
                continue
            content = src.read_text(encoding="utf-8")
            translated_text = self.translate_markdown(content)
            dst.write_text(translated_text, encoding="utf-8")
            translated += 1

        summary_src = input_root / "SUMMARY.md"
        if summary_src.exists():
            summary_dst = output_root / "SUMMARY.md"
            if not summary_dst.exists() or self.config.overwrite:
                text = summary_src.read_text(encoding="utf-8")
                summary_dst.write_text(self.translate_markdown(text), encoding="utf-8")

        mkdocs_src = input_root / "mkdocs.yml"
        if mkdocs_src.exists() and (not (output_root / "mkdocs.yml").exists() or self.config.overwrite):
            shutil.copy2(mkdocs_src, output_root / "mkdocs.yml")

        if (input_root / "assets").exists() and not (output_root / "assets").exists():
            shutil.copytree(input_root / "assets", output_root / "assets")
        if (input_root / "meta").exists() and not (output_root / "meta").exists():
            shutil.copytree(input_root / "meta", output_root / "meta")
        return {"translated": translated, "skipped": skipped}
