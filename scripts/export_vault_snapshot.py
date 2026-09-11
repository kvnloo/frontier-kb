#!/usr/bin/env python3
"""Export a distilled vault snapshot for the humanity-vault frontend. No Postgres."""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
NOTE_DIRS = ("literature", "permanent", "harnesses", "domains", "atlas", "inbox")
REQUIRED = {"id", "title", "type", "status", "created", "updated"}
WIKI_RE = re.compile(r"\[\[([^\]|#]+)")
DEFAULT_DEST = ROOT / "apps" / "humanity-vault" / "content" / "snapshot.json"
LEARNING_IDS = (
    "domain-learning-acceleration",
    "domain-neuroscience",
    "lit-20260911-justin-sung-higher-order-encoding",
    "lit-20260911-huberman-plasticity-alert-rest",
    "lit-20260911-bryan-johnson-measure-dont-guess",
    "lit-20260911-rhonda-patrick-bdnf-exercise",
    "lit-20260911-synaptic-pruning-as-kb-policy",
    "lit-20260911-synaptic-homeostasis-sleep-shy",
    "lit-20260911-llm-frontier-teaching-surface",
    "perm-20260911-encoding-beats-exposure",
    "perm-20260911-plasticity-needs-alert-then-rest",
    "perm-20260911-measure-the-learning-loop",
    "perm-20260911-bdnf-is-a-learning-prerequisite",
    "perm-20260911-kb-is-a-brain-prune-and-potentiate",
    "perm-20260911-human-agent-synergy-is-the-loop",
    "perm-20260911-distill-then-retrieve-llm-frontier",
)
LLM_FRONTIER_IDS = (
    "perm-20260911-distill-then-retrieve-llm-frontier",
    "lit-20260911-llm-frontier-teaching-surface",
    "perm-20260910-swe-2-is-a-posttrained-model",
    "perm-20260910-scaffold-tool-shape-dominates",
    "perm-20260910-small-models-are-workers-or-specialists",
    "perm-20260910-postgres-is-the-operational-kb",
    "perm-20260910-no-universal-harness-plugin",
    "lit-20260910-context-triad",
)


def parse_frontmatter(text: str) -> tuple[dict, str]:
    if not text.startswith("---"):
        return {}, text
    parts = text.split("---", 2)
    if len(parts) < 3:
        return {}, text
    meta: dict = {}
    for line in parts[1].strip().splitlines():
        if ":" not in line:
            continue
        k, v = line.split(":", 1)
        meta[k.strip()] = v.strip().strip('"')
    return meta, parts[2].lstrip("\n")


def distill(body: str) -> str:
    for heading in ("## Idea (atomic)", "## Claim (one sentence)", "## Idea"):
        if heading in body:
            chunk = body.split(heading, 1)[1].split("##", 1)[0].strip()
            return " ".join(chunk.split())
    for line in body.splitlines():
        line = line.strip()
        if line and not line.startswith("#") and not line.startswith("-"):
            return line
    return ""


def parse_list(raw) -> list[str]:
    if raw is None:
        return []
    if isinstance(raw, list):
        return [str(x).strip() for x in raw]
    text = str(raw).strip().strip("[]")
    if not text:
        return []
    return [p.strip().strip("'\"") for p in text.split(",") if p.strip()]


def collect() -> dict:
    notes = []
    edges: list[tuple[str, str, str]] = []
    for folder in NOTE_DIRS:
        base = ROOT / folder
        if not base.exists():
            continue
        for path in sorted(base.rglob("*.md")):
            if path.name in {"README.md", ".gitkeep"}:
                continue
            text = path.read_text(encoding="utf-8")
            meta, body = parse_frontmatter(text)
            if REQUIRED - set(meta):
                continue
            nid = meta["id"]
            notes.append(
                {
                    "id": nid,
                    "path": str(path.relative_to(ROOT)),
                    "title": meta["title"].strip('"'),
                    "type": meta["type"],
                    "status": meta["status"],
                    "body": body,
                    "distilled": distill(body),
                    "tags": parse_list(meta.get("tags")),
                    "domains": parse_list(meta.get("domains")),
                    "created": meta.get("created"),
                    "updated": meta.get("updated"),
                    "weight": 1.0,
                    "lastFired": None,
                    "retrievalDue": True,
                }
            )
            for raw in WIKI_RE.findall(body):
                target = raw.strip().split("|", 1)[0].strip().rsplit("/", 1)[-1]
                if target:
                    edges.append((nid, target, "wikilink"))
    return {
        "version": 1,
        "generated": "2026-09-11",
        "clusters": {
            "LEARNING_ACCELERATION": list(LEARNING_IDS),
            "LLM_FRONTIER": list(LLM_FRONTIER_IDS),
        },
        "notes": notes,
        "edges": [{"src": s, "dst": d, "rel": r, "weight": 1.0, "fires": 0, "lastFired": None} for s, d, r in edges],
    }


def main() -> int:
    dest = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_DEST
    dest.parent.mkdir(parents=True, exist_ok=True)
    data = collect()
    dest.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(json.dumps({"ok": True, "notes": len(data["notes"]), "edges": len(data["edges"]), "path": str(dest)}))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
