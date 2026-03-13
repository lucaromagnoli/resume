# CV Publishing System

[![Build & Deploy CV](https://github.com/lucaromagnoli/resume/actions/workflows/build-cv.yml/badge.svg)](https://github.com/lucaromagnoli/resume/actions/workflows/build-cv.yml)
[![GitHub Pages](https://img.shields.io/badge/live-lucaromagnoli.dev-blue)](https://lucaromagnoli.dev)
[![License](https://img.shields.io/github/license/lucaromagnoli/resume)](LICENSE)

Markdown-as-source-of-truth CV pipeline. Edit `cv/cv.md`, run one command, get HTML + PDF + DOCX.

## Quick start

Everything runs in Docker -- no local Pandoc or LaTeX install needed.

```bash
# Build all outputs
make build

# With contact info for PDF/DOCX
CV_EMAIL="you@example.com" CV_PHONE="+44..." make build

# Preview locally
make serve
# Open http://localhost:8000
```

## Outputs

| Output | Path | Purpose |
|--------|------|---------|
| HTML | `dist/index.html` | Public page with dark/light theme |
| PDF | `dist/cv.pdf` | Recruiter download (Inter font) |
| DOCX | `dist/cv.docx` | Editable export |

The HTML page includes download buttons and a theme toggle. Email and phone are excluded from the public HTML page.

## Project structure

```
cv/
  cv.md              # Source of truth
  build.py           # Build script
  CNAME              # Custom domain for GitHub Pages
  templates/
    cv.html.j2       # Tailwind HTML layout
    cv.tex           # LaTeX template (Inter, titlesec)
  styles/
    cv.css
Dockerfile           # Pandoc + TeX Live + Inter font
Makefile             # Docker-based build targets
.github/workflows/
  build-cv.yml       # CI: lint, build, deploy to GitHub Pages
.pre-commit-config.yaml  # ruff, uv-lock, rust fmt/clippy
dist/                # Generated outputs (gitignored)
```

## Make targets

```
make build        # Generate all outputs (HTML, PDF, DOCX)
make html         # HTML only
make pdf          # PDF only
make docx         # DOCX only
make serve        # Build and serve on port 8000
make clean        # Remove dist/
make docker-build # Build the Docker image only
```

## CI/CD

GitHub Actions pipeline on push to `main`:

1. **Lint** -- pre-commit checks (ruff, trailing whitespace, yaml, etc.)
2. **Build** -- Docker build, generate artifacts with secrets injected
3. **Deploy** -- publish to GitHub Pages at [lucaromagnoli.dev](https://lucaromagnoli.dev)

Contact info (`CV_EMAIL`, `CV_PHONE`) is stored as GitHub secrets and injected at build time.

## Spec

Full specification: [SPEC.md](SPEC.md).
