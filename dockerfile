FROM python:3.12-slim

RUN apt-get update && \
    apt-get install -y \
    wget \
    bzip2 \
    ca-certificates \
    curl \
    git \
    build-essential \
    python3-dev

RUN apt-get install -y pkg-config

RUN curl -LsSf https://astral.sh/uv/install.sh | sh
ENV PATH="/root/.local/bin:$PATH"
RUN apt-get clean && rm -rf /var/lib/apt/lists/*
ENV PYTHONDONTWRITEBYTECODE=1
    
RUN mkdir -p /app
COPY . /app/
WORKDIR /app
RUN uv sync