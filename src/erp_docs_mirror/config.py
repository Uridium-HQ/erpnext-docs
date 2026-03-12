from dataclasses import dataclass, field
from pathlib import Path


@dataclass(slots=True)
class MirrorConfig:
    output_dir: Path
    max_pages: int = 100
    delay_seconds: float = 0.3
    timeout_seconds: int = 20
    user_agent: str = "ERPDocsMirror/0.1 (+local wiki export)"
    same_path_prefix_only: bool = False
    allowed_domains: set[str] = field(default_factory=set)
    seed_prefixes: list[str] = field(default_factory=list)
