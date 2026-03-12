from __future__ import annotations

import argparse
import json
from pathlib import Path
from urllib.parse import urlparse

from .crawler import DocsCrawler
from .models import CrawlConfig
from .translator import MarkdownTranslator, OpenAICompatibleTranslator, TranslationConfig
from .validator import Validator



def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Mirror docs.frappe.io u lokalni Markdown/wiki format")
    subparsers = parser.add_subparsers(dest="command", required=True)

    crawl = subparsers.add_parser("crawl", help="Pokreni crawl i mirror")
    crawl.add_argument("--seed", action="append", required=True, help="Početni URL, može više puta")
    crawl.add_argument("--output", required=True, help="Izlazni direktorijum")
    crawl.add_argument("--allowed-host", action="append", default=[], help="Dozvoljeni host, može više puta")
    crawl.add_argument("--allowed-prefix", action="append", default=[], help="Dozvoljeni path prefiks, može više puta")
    crawl.add_argument("--max-pages", type=int, default=200)
    crawl.add_argument("--timeout", type=float, default=20.0)
    crawl.add_argument("--delay", type=float, default=0.0)
    crawl.add_argument("--no-assets", action="store_true", help="Ne skidaj slike/GIF-ove")
    crawl.add_argument("--no-resume", action="store_true", help="Ignoriši postojeći state")
    crawl.add_argument("--translate-to", default=None, help="Odmah napravi i prevedenu kopiju, npr. sr-Latn")
    crawl.add_argument("--translated-output", default=None, help="Izlaz za prevedenu kopiju; podrazumevano <output>_translated")

    translate = subparsers.add_parser("translate", help="Prevedi već skinuti mirror uz očuvanje linkova")
    translate.add_argument("--input", required=True, help="Postojeći mirror direktorijum")
    translate.add_argument("--output", required=True, help="Direktorijum za prevedenu verziju")
    translate.add_argument("--language", default="sr-Latn", help="Ciljni jezik, npr. sr-Latn")
    translate.add_argument("--provider", default="openai", help="Provider prevoda (trenutno: openai kompatibilan)")
    translate.add_argument("--model", default="gpt-4o-mini", help="Model za prevod")
    translate.add_argument("--api-base", default="https://api.openai.com/v1", help="OpenAI kompatibilan API base URL")
    translate.add_argument("--overwrite", action="store_true", help="Prepiši postojeće prevedene fajlove")
    translate.add_argument("--max-chars-per-chunk", type=int, default=6000, help="Maksimalna veličina jednog translation batch-a")

    validate = subparsers.add_parser("validate", help="Validiraj lokalne linkove")
    validate.add_argument("--output", required=True, help="Izlazni direktorijum")
    validate.add_argument("--json", action="store_true", help="Vrati JSON")

    return parser



def run_translation(input_dir: str, output_dir: str, language: str, provider: str, model: str, api_base: str, overwrite: bool, max_chars_per_chunk: int) -> dict:
    config = TranslationConfig(
        language=language,
        provider=provider,
        model=model,
        api_base=api_base,
        overwrite=overwrite,
        max_chars_per_chunk=max_chars_per_chunk,
    )
    translator = OpenAICompatibleTranslator(config)
    md_translator = MarkdownTranslator(translator, config)
    return md_translator.translate_tree(Path(input_dir), Path(output_dir))



def cmd_crawl(args: argparse.Namespace) -> int:
    allowed_hosts = args.allowed_host or sorted({urlparse(seed).netloc for seed in args.seed})
    config = CrawlConfig(
        seeds=args.seed,
        output_dir=args.output,
        allowed_hosts=allowed_hosts,
        allowed_prefixes=args.allowed_prefix,
        max_pages=args.max_pages,
        timeout=args.timeout,
        delay=args.delay,
        download_assets=not args.no_assets,
        resume=not args.no_resume,
    )
    crawler = DocsCrawler(config)
    result = crawler.crawl()

    if args.translate_to:
        translated_output = args.translated_output or f"{args.output.rstrip('/')}__{args.translate_to}"
        result["translation"] = run_translation(
            input_dir=args.output,
            output_dir=translated_output,
            language=args.translate_to,
            provider="openai",
            model="gpt-4o-mini",
            api_base="https://api.openai.com/v1",
            overwrite=False,
            max_chars_per_chunk=6000,
        )
        result["translated_output_dir"] = translated_output

    print(json.dumps(result, indent=2, ensure_ascii=False))
    return 0



def cmd_translate(args: argparse.Namespace) -> int:
    result = run_translation(
        input_dir=args.input,
        output_dir=args.output,
        language=args.language,
        provider=args.provider,
        model=args.model,
        api_base=args.api_base,
        overwrite=args.overwrite,
        max_chars_per_chunk=args.max_chars_per_chunk,
    )
    print(json.dumps(result, indent=2, ensure_ascii=False))
    return 0



def cmd_validate(args: argparse.Namespace) -> int:
    validator = Validator(Path(args.output))
    result = validator.validate()
    if args.json:
        print(json.dumps(result, indent=2, ensure_ascii=False))
    else:
        print(validator.print_text_report(result))
    return 0 if result["ok"] else 1



def main() -> int:
    parser = build_parser()
    args = parser.parse_args()
    if args.command == "crawl":
        return cmd_crawl(args)
    if args.command == "translate":
        return cmd_translate(args)
    if args.command == "validate":
        return cmd_validate(args)
    parser.error("Nepoznata komanda")
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
