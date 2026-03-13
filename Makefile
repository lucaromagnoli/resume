IMAGE := cv-builder
DOCKER_RUN := docker run --rm \
	-e CV_EMAIL \
	-e CV_PHONE \
	-v $(CURDIR)/dist:/app/dist \
	$(IMAGE)

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
	@echo ""
	@echo "Set CV_EMAIL and CV_PHONE env vars for PDF/DOCX contact info:"
	@echo "  CV_EMAIL=you@example.com CV_PHONE='+44...' make build"

docker-build:
	docker build -t $(IMAGE) .

build: docker-build
	$(DOCKER_RUN) --all

html: docker-build
	$(DOCKER_RUN) --html

pdf: docker-build
	$(DOCKER_RUN) --pdf

docx: docker-build
	$(DOCKER_RUN) --docx

serve: build
	python -m http.server --directory dist 8000

clean:
	rm -rf dist/
