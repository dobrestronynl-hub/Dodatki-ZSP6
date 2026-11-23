#!/usr/bin/env python3
"""Prepare an explicit static Pages artifact without dependencies or secrets."""
from pathlib import Path
import shutil

ROOT = Path(__file__).resolve().parents[1]
DIST = ROOT / "dist"
IGNORED = {".git", ".github", ".openai", "__pycache__", "node_modules", ".DS_Store", "dist"}


def copy_file(source: Path, target: Path) -> None:
    if source.is_symlink():
        raise RuntimeError(f"Refusing to package a symlink: {source.relative_to(ROOT)}")
    target.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(source, target)


def copy_folder(source: Path, target: Path) -> None:
    for path in sorted(source.iterdir()):
        if path.name in IGNORED or path.name.startswith("."):
            continue
        if path.is_symlink():
            raise RuntimeError(f"Refusing to package a symlink: {path.relative_to(ROOT)}")
        if path.is_dir():
            copy_folder(path, target / path.name)
        elif path.is_file():
            copy_file(path, target / path.name)


def main() -> None:
    if not (ROOT / "index.html").is_file():
        raise RuntimeError("Missing catalogue index.html")
    if DIST.is_symlink():
        raise RuntimeError("dist must be a real project directory, not a symlink")
    if DIST.exists():
        shutil.rmtree(DIST)
    DIST.mkdir()
    for path in sorted(ROOT.iterdir()):
        if path.is_file() and (path.name in {"index.html", "README.md", ".nojekyll"} or path.suffix in {".css", ".js", ".mjs"}):
            copy_file(path, DIST / path.name)
    for name in ("assets", "moduly", "docs"):
        source = ROOT / name
        if source.is_dir():
            copy_folder(source, DIST / name)
    (DIST / ".nojekyll").touch()
    count = sum(1 for path in DIST.rglob("*") if path.is_file())
    print(f"Static Pages build ready: {count} files in {DIST}")


if __name__ == "__main__":
    main()
