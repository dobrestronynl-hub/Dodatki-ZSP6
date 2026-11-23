#!/usr/bin/env python3
"""Check this buildless catalogue with Python and the installed Node.js only."""
from __future__ import annotations

from html.parser import HTMLParser
from pathlib import Path
import re
import subprocess
import sys
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]


class Page(HTMLParser):
    def __init__(self, path: Path):
        super().__init__(convert_charrefs=True)
        self.path = path
        self.lang = None
        self.viewport = False
        self.h1 = 0
        self.ids: set[str] = set()
        self.duplicate_ids: set[str] = set()
        self.links: list[str] = []
        self.feed(path.read_text(encoding="utf-8"))

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == "html":
            self.lang = attrs.get("lang")
        if tag == "h1":
            self.h1 += 1
        if tag == "meta" and attrs.get("name", "").lower() == "viewport":
            self.viewport = "width=device-width" in attrs.get("content", "")
        if attrs.get("id"):
            if attrs["id"] in self.ids:
                self.duplicate_ids.add(attrs["id"])
            self.ids.add(attrs["id"])
        for attr in ("href", "src", "poster"):
            if attrs.get(attr):
                self.links.append(attrs[attr])
        if attrs.get("srcset"):
            self.links.extend(item.strip().split()[0] for item in attrs["srcset"].split(",") if item.strip())


def main() -> int:
    failures: list[str] = []
    modules = sorted(p for p in (ROOT / "moduly").iterdir() if p.is_dir())
    if len(modules) != 8:
        failures.append(f"Expected eight modules, found {len(modules)}")
    expected = [ROOT / "index.html"] + [m / "index.html" for m in modules]
    missing = [p for p in expected if not p.is_file()]
    failures.extend(f"Missing page: {p.relative_to(ROOT)}" for p in missing)
    pages = {p.resolve(): Page(p) for p in expected if p.is_file()}
    checked_links = 0

    def check_url(source: Path, value: str) -> None:
        nonlocal checked_links
        value = value.strip()
        if not value:
            return
        parts = urlsplit(value)
        if parts.scheme.lower() in {"javascript", "http"} or value.startswith("//"):
            failures.append(f"Unsafe or insecure URL in {source.relative_to(ROOT)}: {value}")
            return
        if parts.scheme or parts.netloc:
            return
        checked_links += 1
        if parts.path.startswith("/"):
            failures.append(f"Root-relative URL breaks project Pages in {source.relative_to(ROOT)}: {value}")
            return
        target = (source.parent / unquote(parts.path)).resolve() if parts.path else source.resolve()
        if not target.is_relative_to(ROOT):
            failures.append(f"URL leaves the project in {source.relative_to(ROOT)}: {value}")
            return
        if target.is_dir():
            target /= "index.html"
        if not target.is_file():
            failures.append(f"Missing target in {source.relative_to(ROOT)}: {value}")
            return
        if parts.fragment and target.suffix.lower() == ".html":
            target_page = pages.get(target)
            if target_page is None:
                target_page = Page(target)
                pages[target] = target_page
            if unquote(parts.fragment) not in target_page.ids:
                failures.append(f"Missing fragment in {source.relative_to(ROOT)}: {value}")

    for path, page in list(pages.items()):
        label = path.relative_to(ROOT)
        if page.lang != "pl":
            failures.append(f"Expected lang=pl: {label}")
        if not page.viewport:
            failures.append(f"Missing responsive viewport: {label}")
        if page.h1 != 1:
            failures.append(f"Expected one H1, found {page.h1}: {label}")
        if page.duplicate_ids:
            failures.append(f"Duplicate IDs in {label}: {sorted(page.duplicate_ids)}")
        for value in page.links:
            check_url(path, value)

    css_files = sorted(ROOT.glob("*.css")) + sorted((ROOT / "assets").rglob("*.css")) + sorted((ROOT / "moduly").rglob("*.css"))
    for path in css_files:
        for match in re.finditer(r"url\(\s*['\"]?([^)'\"]+)['\"]?\s*\)", path.read_text(encoding="utf-8")):
            check_url(path, match.group(1))

    scripts = sorted(ROOT.glob("*.mjs")) + sorted(ROOT.glob("*.js")) + sorted((ROOT / "assets").rglob("*.mjs")) + sorted((ROOT / "assets").rglob("*.js"))
    for module in modules:
        for name in ("logic.mjs", "module.mjs", "tests.mjs"):
            path = module / name
            if not path.is_file():
                failures.append(f"Missing module script: {path.relative_to(ROOT)}")
            else:
                scripts.append(path)
    for path in scripts:
        for value in re.findall(r"(?:from\s+|import\s*)['\"]([^'\"]+)['\"]", path.read_text(encoding="utf-8")):
            if value.startswith("."):
                check_url(path, value)
        result = subprocess.run(["node", "--check", str(path)], capture_output=True, text=True)
        if result.returncode:
            failures.append(f"Syntax error in {path.relative_to(ROOT)}:\n{result.stderr}")
    if failures:
        print("Validation failed:", file=sys.stderr)
        for error in failures:
            print(f"- {error}", file=sys.stderr)
        return 1
    print(f"PASS: {len(expected)} HTML pages, {len(modules)} independent modules, {checked_links} local URLs, {len(scripts)} JavaScript syntax checks.", flush=True)
    tests = [str(module / "tests.mjs") for module in modules]
    result = subprocess.run(["node", "--test", *tests], cwd=ROOT)
    return result.returncode


if __name__ == "__main__":
    sys.exit(main())
