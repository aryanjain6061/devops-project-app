# Stage 1 — install dependencies
FROM python:3.11-slim AS builder
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Stage 2 — final image
FROM python:3.11-slim
WORKDIR /app

# Copy installed packages from builder
COPY --from=builder /usr/local/lib/python3.11/site-packages /usr/local/lib/python3.11/site-packages
COPY --from=builder /usr/local/bin /usr/local/bin

# Copy application code
COPY src/ ./src/
COPY requirements.txt .

EXPOSE 5000

# Run as non-root user
RUN useradd -m -u 1001 appuser
USER appuser

CMD ["python", "src/app.py"]
