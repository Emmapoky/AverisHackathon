"""Same interface as the organisers' data/loader.py (local folder or their
HTTP server), so the app can point at either with INBOX_SOURCE."""
import importlib.util

from .config import ROOT

_spec = importlib.util.spec_from_file_location("organiser_loader", ROOT / "data" / "loader.py")
_mod = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_mod)
Inbox = _mod.Inbox
