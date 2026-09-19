#!/usr/bin/env bash
# One-time setup (macOS / Linux / Windows Git Bash):  bash scripts/setup.sh
set -e
cd "$(dirname "$0")/.."

PY=python3; command -v python3 >/dev/null 2>&1 || PY=python
$PY -c 'import sys; assert sys.version_info >= (3, 10), "Python 3.10+ needed"' \
  || { echo "✗ Please install Python 3.10 or newer from https://www.python.org/downloads/"; exit 1; }

echo "→ Creating a private Python environment in .venv"
$PY -m venv .venv
if [ -f .venv/bin/activate ]; then . .venv/bin/activate; else . .venv/Scripts/activate; fi

echo "→ Installing libraries"
python -m pip install --quiet --upgrade pip
python -m pip install --quiet -r requirements-dev.txt

if [ ! -f .env ]; then
  cp .env.example .env
  echo "→ Created .env (add your AI keys later — the app works without them)"
fi

echo "→ Processing the 520 sample emails (rules only, takes ~1 s)"
python scripts/run_batch.py --no-llm | tail -3

echo "→ Running tests"
python -m pytest -q | tail -1

echo
echo "✓ All set. Start the app with:  bash scripts/start.sh"
