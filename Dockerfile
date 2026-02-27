FROM ghcr.io/astral-sh/uv:python3.12-bookworm-slim

WORKDIR /app

# Copy dependency file first (better caching)
COPY requirements.txt .
RUN uv pip install --system -r requirements.txt

# Copy project files
COPY . .

EXPOSE 8000
CMD ["chainlit", "run", "ui.py", "--host", "0.0.0.0", "--port", "8000"]