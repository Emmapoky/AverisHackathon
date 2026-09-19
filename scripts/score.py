#!/usr/bin/env python3
"""Score submission.json with the organisers' scorer (aggregate numbers only)
and save them to data/validation.json for the dashboard's "How it works" page.

Needs the organisers' Docker kit unzipped into _local/scoring-server/ (git-ignored).
We only ever read the aggregate scoreboard — never the answer key itself.
"""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SERVER = ROOT / "_local" / "scoring-server" / "server"
GT = ROOT / "_local" / "scoring-server" / "data_v2" / "ground_truth.json"
if not SERVER.exists():
    sys.exit("Scorer not found: unzip sdoc-hackathon-docker.zip into _local/scoring-server/")
sys.path.insert(0, str(SERVER))
from scoring import score_all  # noqa: E402

sub = json.loads((ROOT / "submission.json").read_text())
board = score_all(json.loads(GT.read_text()), sub)
keep = {"final_score": board["final_score"],
        "stage1": {k: board["stage1"][k] for k in ("accuracy", "macro_f1")},
        "stage3": {k: board["stage3"][k] for k in ("defect_precision", "defect_recall", "defect_f1", "field_f1")},
        "end_to_end": board["end_to_end"],
        "reliability": {k: board["reliability"][k] for k in ("escalation_recall", "escalation_precision", "gold_review", "pred_review")}}
(ROOT / "data" / "validation.json").write_text(json.dumps(keep, indent=2))
print(json.dumps(keep, indent=2))
