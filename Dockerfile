# Project Chimera Dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY pyproject.toml ./
RUN pip install --upgrade pip && pip install poetry && poetry install --no-root

COPY . .

CMD ["pytest", "tests/"]
