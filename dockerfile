FROM python:3.12-slim

RUN apt update && apt install -y curl
RUN curl -LsSf https://astral.sh/uv/install.sh | sh
ENV PATH="/root/.local/bin:$PATH"
RUN apt-get clean && rm -rf /var/lib/apt/lists/*
ENV PYTHONDONTWRITEBYTECODE=1
    
RUN mkdir -p /app
COPY . /app/
WORKDIR /app
RUN uv sync

ENV SEARXNG_HOST=localhost
ENV SEARXNG_PORT=8080
ENV FIRECRAWL_HOST=localhost
ENV FIRECRAWL_PORT=3002
ENV FIRECRAWL_API_KEY=firecrawl_api_key

CMD uv run python main.py --searxng-host "${SEARXNG_HOST}" --searxng-port "${SEARXNG_PORT}" --firecrawl-host "${FIRECRAWL_HOST}" --firecrawl-port "${FIRECRAWL_PORT}" --firecrawl-api-key "${FIRECRAWL_API_KEY}"