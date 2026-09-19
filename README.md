# Averis Hackathon 2026: Shipping Document Verification

> **Project name:** _TBD_
> From email inbox to discrepancy report: an AI system that triages a shipping-ops inbox, compares Shipping Instructions (SI) against draft Bills of Lading (BL), flags mismatched fields, and escalates anything uncertain to a human.

🚨 **Preliminary submission deadline: Mon 22 Sep 2026, 12:00 PM.** See [docs/HACKATHON-RULES.md](docs/HACKATHON-RULES.md).

---

## 👥 Team

| Member | Role |
|---|---|
| Erwyna | _TBD_ |
| Nandhini | _TBD_ |
| Charvhi | _TBD_ |
| Riely | _TBD_ |
| Taabish | _TBD_ |

---

## 🧭 The Problem

A shipping operations team receives up to **2,000 emails a day** in one inbox: document-check requests, new SI requests, invoice queries, general updates and spam. For document checks, staff compare the SI (the reference) against the carrier's draft BL by hand across 7 fields:

`shipper` · `consignee` · `notify_party` · `port_of_loading` · `port_of_discharge` · `container_count` · `gross_weight_kg`

The same field is often labelled differently on each document (`Port of Loading` vs `Load Port`), and missed discrepancies cause amendments and delays.

## 💡 Our Solution

_TBD: fill in once we decide (see [docs/IDEA-CANVAS.md](docs/IDEA-CANVAS.md))._

1. **Classify:** `BL_COMPARISON` · `SI_REQUEST` · `INVOICE_QUERY` · `GENERAL` · `SPAM`
2. **Extract:** read SI/BL attachments (txt, pdf, docx, xlsx, scans) and the email body
3. **Compare:** report `OK`, `MISMATCH` (with SI vs BL values side by side), or `NEEDS_REVIEW`
4. **Escalate:** human-in-the-loop review with the reason and source evidence

## 🏗️ Architecture & Tech Stack

_TBD: diagram, AI components, cloud infrastructure._

## 🚀 Setup

```bash
git clone https://github.com/Emmapoky/AverisHackathon.git
cd AverisHackathon

# smoke-test the dataset
cd data && python3 loader.py .      # → "520 emails from ."
```

_TBD: install and run instructions for the app._

### Optional: local accuracy scorer
The organizers' Docker scorer is **not** in this repo because it contains the answer key. Unzip `sdoc-hackathon-docker.zip` (from the organizers' Drive) into `_local/scoring-server/`, then:

```bash
cd _local/scoring-server && docker compose up --build   # http://localhost:8080
```

## 🔗 Links

| | |
|---|---|
| Live demo | _TBD_ |
| Demo video (≤ 5 min) | _TBD_ |
| Slides / docs | _TBD_ |

## 📁 Repo Structure

```
├── README.md
├── docs/            ← brief, rules, brainstorm, idea canvas
├── data/            ← synthetic dataset from the organizers (520 emails + SI/BL attachments)
├── src/             ← our code
├── tests/
└── _local/          ← git-ignored (local scorer with answer key)
```

## 🗺️ Roadmap

_TBD._

---

_Dataset: synthetic data provided by the hackathon organizers, cleared for public repos._
