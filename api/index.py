"""Vercel entry point: serves the whole app (dashboard + API) as one function.

Vercel's filesystem is read-only apart from /tmp, so anything the app writes at
runtime is redirected there. Reviews and live-upload results are persisted to
Supabase instead (SUPABASE_URL / SUPABASE_KEY), which is what makes them survive
between invocations — /tmp does not.
"""
import os
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

os.environ.setdefault("VERCEL", "1")          # app.api / app.llm then default to /tmp
os.environ.setdefault("UPLOADS_DIR", "/tmp/shipcheck-uploads")
os.environ.setdefault("LLM_CACHE_DIR", "/tmp/shipcheck-llm-cache")

from app.api import app  # noqa: E402  (ASGI app Vercel serves)
