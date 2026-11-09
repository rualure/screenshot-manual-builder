#!/usr/bin/env python3
"""Build a standalone screenshot manual from a JSON manifest."""

from __future__ import annotations

import argparse
import base64
import html
import json
import mimetypes
import re
import sys
from pathlib import Path
from urllib.parse import urlparse


TOKEN_PATTERN = re.compile(r"\{\{[A-Z_]+\}\}")


def esc(value: object) -> str:
    return html.escape(str(value or ""), quote=True)


def resolve_path(value: str, manifest_path: Path) -> Path:
    path = Path(value).expanduser()
    return path if path.is_absolute() else (manifest_path.parent / path).resolve()


def data_url(image_path: Path) -> str:
    if not image_path.is_file():
        raise ValueError(f"image does not exist: {image_path}")
    mime = mimetypes.guess_type(image_path.name)[0]
    if mime not in {"image/png", "image/jpeg", "image/webp", "image/gif"}:
        raise ValueError(f"unsupported image type: {image_path}")
    encoded = base64.b64encode(image_path.read_bytes()).decode("ascii")
    return f"data:{mime};base64,{encoded}"


def valid_url(url: str) -> bool:
    parsed = urlparse(url)
    return parsed.scheme in {"https", "http"} and bool(parsed.netloc)


def render_sources(sources: list[dict], heading: str = "公式リファレンス") -> str:
    if not sources:
        return ""
    links = []
    for source in sources:
        label = esc(source.get("label") or source.get("url"))
        url = str(source.get("url") or "")
        if not valid_url(url):
            raise ValueError(f"invalid source URL: {url!r}")
        links.append(f'<li><a href="{esc(url)}">{label}</a></li>')
    return f'<section class="sources"><h2>{esc(heading)}</h2><ul>{"".join(links)}</ul></section>'


def render_item(item: dict, manifest_path: Path) -> str:
    item_id = str(item.get("id") or "")
    if not re.fullmatch(r"[a-z0-9][a-z0-9-]*", item_id):
        raise ValueError(f"invalid item id: {item_id!r}")

    image_path = resolve_path(str(item.get("image") or ""), manifest_path)
    annotations = item.get("annotations") or []
    hotspots = []
    callouts = []
    for annotation in annotations:
        number = int(annotation["number"])
        x = float(annotation["x"])
        y = float(annotation["y"])
        width = float(annotation["width"])
        height = float(annotation["height"])
        if min(x, y, width, height) < 0 or x + width > 100 or y + height > 100:
            raise ValueError(f"annotation {number} is outside image bounds for {item_id}")
        style = f"--x:{x:.4f};--y:{y:.4f};--w:{width:.4f};--h:{height:.4f}"
        label = esc(annotation.get("label") or f"注釈 {number}")
        hotspots.append(
            f'<span class="hotspot" style="{style}" aria-hidden="true"><b>{number}</b></span>'
        )
        callouts.append(f"<li><b>{number}</b><span>{label}</span></li>")

    steps = item.get("steps") or []
    cautions = item.get("cautions") or []
    detail_parts = [
        f'<span class="number">{esc(item.get("number"))}</span>',
        f'<h3>{esc(item.get("title"))}</h3>',
    ]
    if item.get("meaning"):
        detail_parts.extend(["<h4>意味</h4>", f'<p>{esc(item["meaning"])}</p>'])
    if item.get("use_when"):
        detail_parts.extend(["<h4>使う場面</h4>", f'<p>{esc(item["use_when"])}</p>'])
    if steps:
        detail_parts.extend(["<h4>操作</h4>", "<ol>" + "".join(f"<li>{esc(step)}</li>" for step in steps) + "</ol>"])
    if cautions:
        detail_parts.extend(["<h4>注意</h4>", "<ul>" + "".join(f"<li>{esc(note)}</li>" for note in cautions) + "</ul>"])
    if callouts:
        detail_parts.extend(["<h4>画面内の番号</h4>", '<ol class="callouts">' + "".join(callouts) + "</ol>"])
    item_sources = render_sources(item.get("sources") or [], heading="この項目の出典")
    if item_sources:
        detail_parts.append(item_sources)

    return (
        f'<article class="card" id="{esc(item_id)}">'
        f'<figure class="visual"><img src="{data_url(image_path)}" alt="{esc(item.get("alt") or item.get("title"))}">'
        f'{"".join(hotspots)}</figure><div class="details">{"".join(detail_parts)}</div></article>'
    )


def build(manifest_path: Path, template_path: Path, output_path: Path) -> tuple[int, int]:
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    template = template_path.read_text(encoding="utf-8")
    sections = manifest.get("sections") or []
    if not sections:
        raise ValueError("manifest requires at least one section")

    seen_ids: set[str] = set()
    seen_numbers: set[str] = set()
    nav_parts = []
    content_parts = []
    item_count = 0
    image_count = 0

    for section_index, section in enumerate(sections, 1):
        section_items = section.get("items") or []
        if not section_items:
            raise ValueError(f"section {section_index} has no items")
        cards = []
        for item in section_items:
            item_id = str(item.get("id") or "")
            number = str(item.get("number") or "")
            if item_id in seen_ids:
                raise ValueError(f"duplicate item id: {item_id}")
            if number in seen_numbers:
                raise ValueError(f"duplicate item number: {number}")
            seen_ids.add(item_id)
            seen_numbers.add(number)
            nav_parts.append(f'<a href="#{esc(item_id)}">{esc(number)}　{esc(item.get("title"))}</a>')
            cards.append(render_item(item, manifest_path))
            item_count += 1
            image_count += 1
        content_parts.append(
            f'<section class="chapter"><h2>{esc(section.get("title") or f"Section {section_index}")}</h2>'
            f'{"".join(cards)}</section>'
        )

    notice = ""
    if manifest.get("privacy_notice"):
        notice = f'<aside class="notice"><strong>取り扱い上の注意：</strong> {esc(manifest["privacy_notice"])}</aside>'

    replacements = {
        "{{LANG}}": esc(manifest.get("language") or "ja"),
        "{{TITLE}}": esc(manifest.get("title") or "画面操作マニュアル"),
        "{{LEAD}}": esc(manifest.get("lead") or ""),
        "{{NOTICE}}": notice,
        "{{NAV}}": "".join(nav_parts),
        "{{CONTENT}}": "".join(content_parts),
        "{{SOURCES}}": render_sources(manifest.get("sources") or []),
    }
    output = template
    for token, value in replacements.items():
        output = output.replace(token, value)
    unresolved = TOKEN_PATTERN.findall(output)
    if unresolved:
        raise ValueError(f"unresolved template tokens: {sorted(set(unresolved))}")

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(output, encoding="utf-8")
    return item_count, image_count


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("manifest", type=Path, help="path to the JSON manifest")
    parser.add_argument("--output", type=Path, required=True, help="output HTML path")
    parser.add_argument(
        "--template",
        type=Path,
        default=Path(__file__).resolve().parents[1] / "assets" / "manual-template.html",
        help="HTML template path",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    try:
        items, images = build(args.manifest.resolve(), args.template.resolve(), args.output.resolve())
    except (OSError, KeyError, TypeError, ValueError, json.JSONDecodeError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1
    print(f"OK: wrote {args.output} with {items} cards and {images} embedded images")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
