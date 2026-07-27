# FROM ghcr.io/astral-sh/uv:python3.13-trixie AS builder
# SHELL ["/bin/bash", "-c"]
# ENV PYTHONUNBUFFERED=1 \
#     PYTHONDONTWRITEBYTECODE=1
# WORKDIR /app
# COPY ./pyproject.toml .
# RUN uv venv
# ENV PATH="/app/.venv/Scripts/Lib:$PATH"
# RUN uv sync

# FROM ghcr.io/astral-sh/uv:python3.13-trixie-slim
# WORKDIR /app
# COPY --from=builder /app/.venv .venv/
# ENV PATH="/app/.venv/Scripts/Lib:$PATH"
# COPY ./src ./src
# RUN ls -la
# RUN ls 
# # CMD ["fastapi dev src/main.py"]
# # CMD ["bash", "-c", "ls -la"]
# CMD ["fastapi", "run", "src/main.py"]

FROM ghcr.io/astral-sh/uv:python3.13-trixie AS builder
SHELL ["/bin/bash", "-c"]
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1
WORKDIR /app
COPY ./pyproject.toml .
RUN uv venv
ENV PATH="/app/.venv/bin:$PATH"
RUN uv sync
COPY . .
# CMD ["fastapi dev src/main.py"]fly 
# CMD ["bash", "-c", "ls -la && fastapi dev src/main.py"]
# CMD ["fastapi", "dev", "src/main.py"]
CMD ["fastapi", "dev", "src/main.py", "--host", "0.0.0.0", "--port", "8000"]
