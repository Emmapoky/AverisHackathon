#!/usr/bin/env python3
"""Deploy ShipCheck to a free Hugging Face Space in one command.

    python3 scripts/deploy_hf.py --dry-run          # just list what would be uploaded
    python3 scripts/deploy_hf.py                    # create/update <you>/shipcheck
    python3 scripts/deploy_hf.py --space myname/my-space

What it does:
 1. Logs in with your Hugging Face token (HF_TOKEN in .env, or `huggingface-cli login`).
 2. Creates the Space (Docker, public) if it doesn't exist.
 3. Copies DEEPSEEK_API_KEY (and GEMINI_API_KEY / SUPABASE_* if set) from .env into the
    Space as *secrets* — so the key never goes into code or chat.
 4. Uploads only what the app needs. Never uploads .env, _local/ (answer key),
    .git, tests or docs. Uses the HF API, so PDFs/Word/Excel need no git-lfs.
 5. Adds the Space header (sdk: docker, port 7860) to the Space's README only —
    the GitHub README stays clean.
"""
import argparse
import fnmatch
import os
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
from app.config import APP_NAME, load_env  # noqa: E402

load_env()

INCLUDE = ["Dockerfile", "requirements.txt", "src/**", "scripts/**", "data/**"]
EXCLUDE = [
    "**/__pycache__/**", "*.pyc", ".env", ".env.*",
    "data/reviews.json", "data/processed_extra.json", "data/uploads/**",
    "scripts/deploy_hf.py", "**/.DS_Store",
]

HEADER = f"""---
title: {APP_NAME}
emoji: 🚢
colorFrom: blue
colorTo: green
sdk: docker
app_port: 7860
pinned: false
---
"""


def files_to_upload() -> list[str]:
    out = []
    for p in sorted(ROOT.rglob("*")):
        if not p.is_file():
            continue
        rel = p.relative_to(ROOT).as_posix()
        if any(fnmatch.fnmatch(rel, pat) for pat in EXCLUDE):
            continue
        if any(fnmatch.fnmatch(rel, pat) for pat in INCLUDE):
            out.append(rel)
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--space", help="user/space-name (default: <your username>/shipcheck)")
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    files = files_to_upload()
    assert not any(f.startswith(("_local", ".env")) or "ground_truth" in f for f in files), "refusing to upload secrets/answer key"
    size = sum((ROOT / f).stat().st_size for f in files) / 1e6
    print(f"{len(files)} files, {size:.1f} MB to upload")
    if args.dry_run:
        for f in files:
            if not f.startswith(("data/attachments/", "data/inbox/", "data/llm_cache/")):
                print("  ", f)
        print("   + data/inbox/, data/attachments/ (the dataset)")
        return

    from huggingface_hub import HfApi
    token = os.environ.get("HF_TOKEN") or None
    api = HfApi(token=token)
    try:
        user = api.whoami()["name"]
    except Exception:
        sys.exit("Not logged in to Hugging Face. Put HF_TOKEN=hf_... in .env "
                 "(token with WRITE access from https://huggingface.co/settings/tokens) "
                 "or run: huggingface-cli login")
    repo_id = args.space or f"{user}/shipcheck"
    print(f"Space: {repo_id}")

    api.create_repo(repo_id, repo_type="space", space_sdk="docker", exist_ok=True, private=False)

    # Secrets come from your local .env — they're sent straight to HF, never printed.
    if os.environ.get("DEEPSEEK_API_KEY"):
        api.add_space_secret(repo_id, "DEEPSEEK_API_KEY", os.environ["DEEPSEEK_API_KEY"])
        api.add_space_variable(repo_id, "LLM_PROVIDER", "deepseek")
        api.add_space_variable(repo_id, "DEEPSEEK_MODEL", os.environ.get("DEEPSEEK_MODEL", "deepseek-chat"))
        print("✓ DeepSeek key saved as a Space secret")
    else:
        print("! No DEEPSEEK_API_KEY in .env — the app will run on rules only (you can add it later in Space settings)")
    if os.environ.get("GEMINI_API_KEY"):
        api.add_space_secret(repo_id, "GEMINI_API_KEY", os.environ["GEMINI_API_KEY"])
        print("✓ Gemini key saved as a Space secret (reads scanned PDFs)")
    for k in ("SUPABASE_URL", "SUPABASE_KEY"):
        if os.environ.get(k):
            api.add_space_secret(repo_id, k, os.environ[k])
            print(f"✓ {k} saved as a Space secret")
    if os.environ.get("APP_NAME"):
        api.add_space_variable(repo_id, "APP_NAME", os.environ["APP_NAME"])

    api.upload_folder(repo_id=repo_id, repo_type="space", folder_path=str(ROOT),
                      allow_patterns=INCLUDE, ignore_patterns=EXCLUDE,
                      commit_message="Deploy ShipCheck")
    readme = HEADER + "\n" + (ROOT / "README.md").read_text()
    api.upload_file(repo_id=repo_id, repo_type="space", path_or_fileobj=readme.encode(),
                    path_in_repo="README.md", commit_message="Space README")

    sub = repo_id.replace("/", "-").replace("_", "-").lower()
    print(f"\n✓ Uploaded. Building now (~3–5 min): https://huggingface.co/spaces/{repo_id}")
    print(f"  Live link when ready:            https://{sub}.hf.space")


if __name__ == "__main__":
    main()
