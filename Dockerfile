FROM python:3.11-alpine

# Instalar uv y zona horaria
RUN pip install --no-cache-dir uv && \
    apk add --no-cache tzdata && \
    cp /usr/share/zoneinfo/America/Santiago /etc/localtime

WORKDIR /app

COPY pyproject.toml uv.lock ./
RUN uv sync --frozen

COPY . .

EXPOSE 8000

CMD ["uv", "run", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
