.PHONY: all build clean serve help html pdf docx

all: help

help:
	@echo "Build CV from Markdown (cv/cv.md) to HTML, PDF, DOCX."
	@echo ""
	@echo "Targets:"
	@echo "  build      - Generate all outputs (HTML, PDF, DOCX) to dist/"
	@echo "  html       - Generate HTML only"
	@echo "  pdf        - Generate PDF only"
	@echo "  docx       - Generate DOCX only"
	@echo "  serve      - Build and serve dist/ locally on port 8000"
	@echo "  clean      - Remove dist/ and build artifacts"

build:
	python cv/build.py --all

html:
	python cv/build.py --html

pdf:
	python cv/build.py --pdf

docx:
	python cv/build.py --docx

serve: build
	python -m http.server --directory dist 8000

clean:
	rm -rf dist/
