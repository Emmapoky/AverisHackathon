#!/usr/bin/env bash
# Start the app:  bash scripts/start.sh   → http://localhost:8000
cd "$(dirname "$0")/.."
if [ -f .venv/bin/activate ]; then . .venv/bin/activate; elif [ -f .venv/Scripts/activate ]; then . .venv/Scripts/activate; fi
PORT="${PORT:-8000}"
echo "ShipCheck running at http://localhost:$PORT   (Ctrl+C to stop)"
exec python -m uvicorn app.api:app --app-dir src --port "$PORT" --reload
