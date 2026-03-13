# CV Publishing System Spec

## Goal

Build a small system where:

- **Markdown is the source of truth**
- the CV can be rendered to:
  - HTML for a hosted public page
  - PDF for recruiter download
  - DOCX for editable/downloadable export
- the public page includes a Download CV section
- deployment is low-maintenance and ideally static-first
- future support for multiple CV variants remains possible

---

## Non-goals

Not building:

- a full Django/React app
- an admin panel
- a database-backed CMS
- LinkedIn sync as a critical dependency
- per-request heavy dynamic rendering unless later needed

---

## High-level Architecture

```
Markdown + metadata
        ↓
build pipeline
        ↓
HTML + PDF + DOCX artifacts
        ↓
static hosting
```

**Core idea:**

- author content in Markdown
- optionally store structured metadata separately
- generate all outputs during build/deploy
- host generated files statically
- no always-on backend required in v1

---

## Source of Truth

### Primary source: `cv/cv.md`

Contains: summary, experience, skills, projects, education, links

### Optional companion: `cv/cv.yaml`

Use only if needed for: contact info, reusable link metadata, profile variants, section toggles, dates/labels.

**Recommendation:** Start with `cv/cv.md` only. Add `cv.yaml` when Markdown becomes awkward.

---

## Functional Requirements

### Authoring

- user edits CV in Markdown
- source is version-controlled in Git
- content remains readable directly in raw Markdown

### Output generation

System must generate:

- `index.html`
- `cv.pdf`
- `cv.docx`

### Public page

Hosted page must:

- render CV content cleanly
- expose buttons/links for: Download PDF, Download DOCX
- optionally expose raw Markdown or GitHub source link

### Deployment

- automated from Git
- publishing a change regenerates all artifacts

### Extensibility

Support future variants: `/ai/`, `/backend/`, `/audio/` or equivalent.

---

## Non-functional Requirements

- **Simplicity:** minimal moving parts, no runtime database, no unnecessary frontend framework
- **Maintainability:** single source of truth, low cognitive load, easy local preview
- **Portability:** runs locally and in CI, no proprietary platform dependency
- **Performance:** static and fast, downloads served directly as files

---

## Repository Structure

```
repo/
  cv/
    cv.md
    build.py
    templates/
      cv.html.j2
      cv.tex
    styles/
      cv.css
  dist/
    index.html
    cv.pdf
    cv.docx
```

---

## Build Pipeline

| Output | Pipeline | Tools |
|--------|----------|-------|
| HTML | cv.md → template → styled index.html | Pandoc, Jinja2, CSS |
| PDF | cv.md → pandoc → LaTeX template → PDF | Pandoc, XeLaTeX/PDFLaTeX |
| DOCX | cv.md → pandoc → DOCX | Pandoc (optional reference DOCX) |

---

## Tooling

- **Required:** Python 3.x, Pandoc
- **Recommended:** TeX engine (xelatex), Jinja2, pyyaml (optional)
- **Optional:** make, GitHub Actions, pre-commit

---

## Build Script

`build.py` must:

1. read cv.md
2. optionally read cv.yaml
3. generate dist/index.html
4. generate dist/cv.pdf
5. generate dist/cv.docx
6. copy static assets if needed
7. fail clearly on missing dependencies

**Interface:**

```bash
python cv/build.py           # all outputs
python cv/build.py --html    # HTML only
python cv/build.py --pdf     # PDF only
python cv/build.py --docx    # DOCX only
python cv/build.py --all     # explicit all
```

---

## Acceptance Criteria

The system is complete when:

- CV content is maintained in Markdown
- one build command generates index.html, cv.pdf, cv.docx
- hosted page displays CV cleanly
- hosted page exposes download buttons
- recruiter can open page and download either format
- updating one Markdown file updates all formats
