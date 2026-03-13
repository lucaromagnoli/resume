#!/usr/bin/env python3
"""
CV build pipeline: Markdown → HTML, PDF, DOCX.

Reads cv.md and optionally cv.yaml, generates dist/index.html, dist/cv.pdf, dist/cv.docx.
Requires: Python 3.x, Pandoc, TeX (xelatex).
"""

from __future__ import annotations

import argparse
import shutil
import subprocess
from pathlib import Path

# Paths
CV_DIR = Path(__file__).resolve().parent
REPO_ROOT = CV_DIR.parent
DIST_DIR = REPO_ROOT / "dist"
CV_MD = CV_DIR / "cv.md"
CV_YAML = CV_DIR / "cv.yaml"
TEMPLATES_DIR = CV_DIR / "templates"
STYLES_DIR = CV_DIR / "styles"
ASSETS_DIR = CV_DIR / "assets"


def _run(cmd: list[str], env: dict | None = None) -> None:
    result = subprocess.run(cmd, capture_output=True, text=True, env=env)
    if result.returncode != 0:
        raise RuntimeError(
            f"Command failed: {' '.join(cmd)}\n{result.stderr or result.stdout}"
        )


def check_pandoc() -> None:
    try:
        subprocess.run(
            ["pandoc", "--version"],
            capture_output=True,
            check=True,
        )
    except (subprocess.CalledProcessError, FileNotFoundError) as e:
        raise SystemExit(
            "pandoc is required but not found. Install: https://pandoc.org/installing.html"
        ) from e


def check_latex() -> None:
    for cmd in ["xelatex", "pdflatex"]:
        try:
            subprocess.run(
                [cmd, "--version"],
                capture_output=True,
                check=True,
            )
            return
        except (subprocess.CalledProcessError, FileNotFoundError):
            continue
    raise SystemExit(
        "A TeX engine (xelatex or pdflatex) is required for PDF. Install a TeX distribution."
    )


PRIVATE_PATTERNS = ["Email:", "Phone:"]


def _strip_private_lines(md_text: str) -> str:
    """Remove lines containing private contact info for the public HTML build."""
    return "\n".join(
        line
        for line in md_text.splitlines()
        if not any(p in line for p in PRIVATE_PATTERNS)
    )


def md_to_html_body(md_path: Path) -> str:
    """Convert Markdown to HTML fragment (body only, no document wrapper)."""
    md_text = _strip_private_lines(md_path.read_text(encoding="utf-8"))
    result = subprocess.run(
        [
            "pandoc",
            "-f",
            "markdown",
            "-t",
            "html",
            "--wrap=none",
        ],
        input=md_text,
        capture_output=True,
        text=True,
        check=True,
    )
    return result.stdout


def build_html(md_path: Path) -> None:
    try:
        from jinja2 import Environment, FileSystemLoader
    except ImportError:
        raise SystemExit(
            "Jinja2 is required for HTML generation. Install: pip install jinja2"
        )

    body_html = md_to_html_body(md_path)
    env = Environment(loader=FileSystemLoader(str(TEMPLATES_DIR)))
    template = env.get_template("cv.html.j2")
    html = template.render(body=body_html)

    DIST_DIR.mkdir(parents=True, exist_ok=True)
    out_path = DIST_DIR / "index.html"
    out_path.write_text(html, encoding="utf-8")
    print(f"Generated {out_path}")


def build_pdf(md_path: Path) -> None:
    tex_template = TEMPLATES_DIR / "cv.tex"
    if not tex_template.exists():
        raise FileNotFoundError(f"LaTeX template not found: {tex_template}")

    DIST_DIR.mkdir(parents=True, exist_ok=True)
    out_path = DIST_DIR / "cv.pdf"

    cmd = [
        "pandoc",
        str(md_path),
        "-f",
        "markdown",
        "-o",
        str(out_path),
        f"--template={tex_template}",
        "--pdf-engine=xelatex",
    ]
    _run(cmd)
    print(f"Generated {out_path}")


def build_docx(md_path: Path) -> None:
    DIST_DIR.mkdir(parents=True, exist_ok=True)
    out_path = DIST_DIR / "cv.docx"

    cmd = [
        "pandoc",
        str(md_path),
        "-f",
        "markdown",
        "-o",
        str(out_path),
    ]
    _run(cmd)
    print(f"Generated {out_path}")


def copy_cname() -> None:
    cname = CV_DIR / "CNAME"
    if not cname.exists():
        return
    DIST_DIR.mkdir(parents=True, exist_ok=True)
    dst = DIST_DIR / "CNAME"
    shutil.copy2(cname, dst)
    print(f"Copied {dst}")


def copy_assets() -> None:
    if not ASSETS_DIR.is_dir():
        return
    dst = DIST_DIR / "assets"
    if dst.exists():
        shutil.rmtree(dst)
    shutil.copytree(ASSETS_DIR, dst)
    print(f"Copied assets to {dst}")


def copy_styles() -> None:
    css = STYLES_DIR / "cv.css"
    if not css.exists():
        return
    DIST_DIR.mkdir(parents=True, exist_ok=True)
    dst = DIST_DIR / "cv.css"
    shutil.copy2(css, dst)
    print(f"Copied {dst}")


def main() -> None:
    parser = argparse.ArgumentParser(description="Build CV outputs from Markdown.")
    parser.add_argument(
        "--html",
        action="store_true",
        help="Generate HTML only",
    )
    parser.add_argument(
        "--pdf",
        action="store_true",
        help="Generate PDF only",
    )
    parser.add_argument(
        "--docx",
        action="store_true",
        help="Generate DOCX only",
    )
    parser.add_argument(
        "--all",
        action="store_true",
        help="Generate all outputs (default)",
    )
    parser.add_argument(
        "--skip-check",
        action="store_true",
        help="Skip dependency checks",
    )
    args = parser.parse_args()

    do_all = args.all or not (args.html or args.pdf or args.docx)

    if not args.skip_check:
        check_pandoc()
        if do_all or args.pdf:
            check_latex()

    if not CV_MD.exists():
        raise SystemExit(f"Source file not found: {CV_MD}")

    if do_all:
        build_html(CV_MD)
        build_pdf(CV_MD)
        build_docx(CV_MD)
        copy_styles()
        copy_assets()
        copy_cname()
    else:
        if args.html:
            build_html(CV_MD)
            copy_styles()
            copy_assets()
            copy_cname()
        if args.pdf:
            build_pdf(CV_MD)
        if args.docx:
            build_docx(CV_MD)


if __name__ == "__main__":
    main()
