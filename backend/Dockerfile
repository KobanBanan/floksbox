FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

# Install system dependencies (if needed for building wheels)
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt

# Copy backend source only
COPY backend/ /app

RUN chmod +x /app/docker-entrypoint.sh

EXPOSE 8000

# Default command: run migrations, collect static, and start Gunicorn
CMD ["/app/docker-entrypoint.sh"]
