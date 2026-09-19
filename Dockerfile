# One container: API + dashboard. Works on Hugging Face Spaces (free, no card),
# Render free tier, Koyeb, Fly.io, or any Docker host.
FROM python:3.12-slim

RUN useradd -m -u 1000 user
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY --chown=user src/ src/
COPY --chown=user scripts/ scripts/
COPY --chown=user data/ data/
USER user

# Hugging Face Spaces expects 7860; other hosts set $PORT themselves.
ENV PORT=7860 PYTHONUNBUFFERED=1
EXPOSE 7860
CMD ["sh", "-c", "uvicorn app.api:app --app-dir src --host 0.0.0.0 --port ${PORT}"]
