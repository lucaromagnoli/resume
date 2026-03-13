IMAGE := cv-builder

.PHONY: all build clean serve help html pdf docx docker-build

all: help

help:
	@echo "Build CV from Markdown (cv/cv.md) to HTML, PDF, DOCX."
	@echo ""
	@echo "Targets:"
	@echo "  build        - Generate all outputs (HTML, PDF, DOCX) to dist/"
	@echo "  html         - Generate HTML only"
	@echo "  pdf          - Generate PDF only"
	@echo "  docx         - Generate DOCX only"
	@echo "  serve        - Build and serve dist/ locally on port 8000"
	@echo "  clean        - Remove dist/ and build artifacts"
	@echo "  docker-build - Build the Docker image"

docker-build:
	docker build -t $(IMAGE) .

build: docker-build
	docker run --rm -v $(CURDIR)/dist:/app/dist $(IMAGE) --all

html: docker-build
	docker run --rm -v $(CURDIR)/dist:/app/dist $(IMAGE) --html

pdf: docker-build
	docker run --rm -v $(CURDIR)/dist:/app/dist $(IMAGE) --pdf

docx: docker-build
	docker run --rm -v $(CURDIR)/dist:/app/dist $(IMAGE) --docx

serve: build
	python -m http.server --directory dist 8000

clean:
	rm -rf dist/
