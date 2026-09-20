#!/usr/bin/env python3
"""Process the whole inbox once and save the results.

    python3 scripts/run_batch.py                 # rules + AI (if a free key is set in .env)
    python3 scripts/run_batch.py --no-llm        # rules only, no network
    python3 scripts/run_batch.py --only email_001 email_502

Writes data/results.json (what the dashboard shows) and submission.json
(the organisers' scorer format).
"""
import argparse
import json
import sys
import time
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from app.config import load_env  # noqa: E402

load_env()

from app import llm  # noqa: E402
from app.inbox import Inbox  # noqa: E402
from app.pipeline import process_email, to_submission  # noqa: E402


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--no-llm", action="store_true")
    ap.add_argument("--only", nargs="*")
    ap.add_argument("--source", default=str(ROOT / "data"))
    ap.add_argument("--out", default=str(ROOT / "data" / "results.json"))
    args = ap.parse_args()

    inbox = Inbox(args.source)
    emails = inbox.emails()
    if args.only:
        emails = [e for e in emails if e["email_id"] in set(args.only)]
    use_llm = not args.no_llm and llm.available()
    print(f"{len(emails)} emails · AI: {llm.model_name() + ' (' + llm.provider() + ')' if use_llm else 'off (rules only)'}")

    out_path = Path(args.out)
    results = json.loads(out_path.read_text(encoding="utf-8")) if (args.only and out_path.exists()) else {}
    t0 = time.time()
    for i, e in enumerate(emails, 1):
        results[e["email_id"]] = process_email(e, inbox.read_bytes, use_llm=use_llm)
        if i % 50 == 0:
            print(f"  {i}/{len(emails)}  ({time.time() - t0:.0f}s)")

    results = dict(sorted(results.items()))
    out_path.write_text(json.dumps(results, indent=1, ensure_ascii=False), encoding="utf-8")
    sub = {k: to_submission(v) for k, v in results.items()}
    (ROOT / "submission.json").write_text(json.dumps(sub, indent=2), encoding="utf-8")

    print(f"done in {time.time() - t0:.1f}s -> {out_path.relative_to(ROOT)}, submission.json")
    print("categories:", dict(Counter(r["category"] for r in results.values())))
    print("status:    ", dict(Counter(r["status"] for r in results.values())))
    print("decided_by:", dict(Counter(r["decided_by"] for r in results.values())))
    print("review:    ", dict(Counter(r["review_reason"] for r in results.values() if r["review_reason"])))


if __name__ == "__main__":
    main()
