from __future__ import annotations

import json
import re
from pathlib import Path


LINK_RE = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")


class Validator:
    def __init__(self, output_root: Path):
        self.output_root = output_root

    def validate(self) -> dict:
        problems: list[dict] = []
        for md_path in self.output_root.rglob("*.md"):
            text = md_path.read_text(encoding="utf-8")
            for match in LINK_RE.finditer(text):
                target = match.group(1).strip()
                if target.startswith(("http://", "https://", "mailto:", "tel:", "#")):
                    continue
                target_base = target.split("#", 1)[0]
                resolved = (md_path.parent / target_base).resolve()
                if not resolved.exists():
                    problems.append({
                        "file": md_path.relative_to(self.output_root).as_posix(),
                        "target": target,
                    })
        return {"ok": not problems, "problems": problems, "count": len(problems)}

    def print_text_report(self, result: dict) -> str:
        if result["ok"]:
            return "Validacija uspešna: nema polomljenih lokalnih linkova."
        lines = [f"Pronađeno problema: {result['count']}"]
        for problem in result["problems"][:100]:
            lines.append(f"- {problem['file']} -> {problem['target']}")
        if result["count"] > 100:
            lines.append("- ...")
        return "\n".join(lines)
