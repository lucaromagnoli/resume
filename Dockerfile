FROM python:3.12-slim

# Install Pandoc and TeX Live (minimal + extras needed for CV)
RUN apt-get update && apt-get install -y --no-install-recommends \
    pandoc \
    texlive-xetex \
    texlive-fonts-recommended \
    texlive-fonts-extra \
    texlive-latex-extra \
    fontconfig \
    wget \
    unzip \
    && rm -rf /var/lib/apt/lists/*

# Install Inter font (static TTFs for full XeLaTeX compatibility)
RUN wget -q https://github.com/rsms/inter/releases/download/v4.1/Inter-4.1.zip -O /tmp/inter.zip \
    && mkdir -p /usr/share/fonts/truetype/inter \
    && unzip -q /tmp/inter.zip -d /tmp/inter \
    && cp /tmp/inter/extras/ttf/*.ttf /usr/share/fonts/truetype/inter/ \
    && fc-cache -f \
    && rm -rf /tmp/inter /tmp/inter.zip

WORKDIR /app

# Copy project files
COPY . .

# Install Python dependencies
RUN pip install --no-cache-dir jinja2

ENTRYPOINT ["python", "cv/build.py"]
CMD ["--all"]
