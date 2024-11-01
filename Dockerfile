FROM python:3.12 AS base
WORKDIR /app

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    && rm -rf /var/lib/apt/lists/*

RUN pip3 install --upgrade pip
RUN curl -LsSf https://astral.sh/uv/install.sh | sh
COPY requirements.txt /app

RUN pip3 install --no-cache-dir --upgrade -r requirements.txt

FROM base AS backend

ENV DATABASE_URL="sqlite:///backend/app/db/database.db"

COPY backend /app/backend

EXPOSE 8002

CMD ["uvicorn", "backend.app.main:app", "--port", "8002", "--host", "0.0.0.0", "--reload"]

FROM base AS frontend

COPY frontend /app/frontend

EXPOSE 8003

CMD ["streamlit", "run", "frontend/🚀_Home.py", "--server.port=8003", "--server.address=0.0.0.0"]