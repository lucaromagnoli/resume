# CV Publishing System

Markdown-as-source-of-truth CV pipeline. Edit `cv/cv.md`, run one build command, get HTML, PDF, and DOCX.

## Quick start

```bash
# Install dependencies
pip install -e .

# Install system tools (required for PDF)
# macOS: brew install pandoc basictex
# Linux: apt install pandoc texlive-xetex

# Build all outputs
make build
# or: python cv/build.py --all

# Preview locally
make serve
# Open http://localhost:8000
```

## Outputs

| Output | Path | Purpose |
|--------|------|---------|
| HTML | `dist/index.html` | Public hosted page |
| PDF | `dist/cv.pdf` | Recruiter download |
| DOCX | `dist/cv.docx` | Editable export |

The HTML page includes Download PDF and Download DOCX buttons.

## Project structure

```
cv/
  cv.md          # Source of truth
  build.py       # Build script
  templates/
    cv.html.j2   # HTML layout
    cv.tex       # LaTeX template for PDF
  styles/
    cv.css
  assets/        # Optional: avatar, icons
dist/            # Generated outputs (gitignored)
```

## Build options

```bash
python cv/build.py           # All outputs (default)
python cv/build.py --html    # HTML only
python cv/build.py --pdf     # PDF only
python cv/build.py --docx    # DOCX only
```

## Deployment

Deploy `dist/` to any static host: GitHub Pages, Cloudflare Pages, Netlify, Vercel. Ensure `index.html`, `cv.pdf`, `cv.docx`, and `cv.css` are published.

## Spec

Full specification: [SPEC.md](SPEC.md).
